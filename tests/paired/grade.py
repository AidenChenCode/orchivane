import argparse
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True


def load(path):
    spec = importlib.util.spec_from_file_location('candidate', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def grade(task, root, phase=2):
    results = []

    def check(name, function):
        try:
            assert function(), 'assertion false'
            results.append({'check': name, 'passed': True})
        except Exception as exc:
            results.append({'check': name, 'passed': False, 'error': str(exc)})

    if task == 'S1':
        fn = load(root / 'normalize.py').normalize
        check('trim_lower_and_drop_blank', lambda: fn([' A ', 'a', ' ', 'B']) == ['a', 'a', 'b'])
        check('empty_list', lambda: fn([]) == [])
        check('order_duplicates_whitespace', lambda: fn(['\tZ\n', ' x ', 'Z']) == ['z', 'x', 'z'])
        proc = subprocess.run([sys.executable, '-B', str(root / 'normalize.py'), ' A ', ' ', 'A'], capture_output=True, text=True, timeout=20)
        check('cli', lambda: proc.returncode == 0 and json.loads(proc.stdout) == ['a', 'a'])
    elif task == 'S2':
        fn = load(root / 'stock.py').summarize
        check('group_and_sort', lambda: fn([{'sku': ' B ', 'quantity': '2'}, {'sku': 'a', 'quantity': '0'}, {'sku': 'b', 'quantity': '3'}]) == [{'sku': 'a', 'quantity': 0}, {'sku': 'b', 'quantity': 5}])
        check('empty', lambda: fn([]) == [])
        for name, row in [('negative', {'sku': 'a', 'quantity': '-1'}), ('fractional', {'sku': 'a', 'quantity': '1.5'}), ('empty_sku', {'sku': ' ', 'quantity': '1'})]:
            def rejects(row=row):
                try:
                    fn([row])
                except ValueError:
                    return True
                return False
            check(name, rejects)
        expected = {'schema_version': phase, 'sku_case': 'lower', 'input_encoding': 'utf-8' if phase == 1 else 'utf-8-sig', 'default_status': 'active', 'ignored_statuses': [] if phase == 1 else ['archived']}
        check('contract', lambda: all(json.loads((root / 'contract.json').read_text()).get(k) == v for k, v in expected.items()))
        if phase == 2:
            check('archived_skipped_before_validation', lambda: fn([{'sku': '', 'quantity': 'bad', 'status': ' Archived '}, {'sku': ' A ', 'quantity': '2', 'status': ' ACTIVE '}, {'sku': 'a', 'quantity': '1', 'status': ''}]) == [{'sku': 'a', 'quantity': 3}])
            def reject_status():
                try:
                    fn([{'sku': 'x', 'quantity': '1', 'status': 'pending'}])
                except ValueError:
                    return True
                return False
            check('unknown_status', reject_status)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'input.csv'
            text = 'sku,quantity\n B ,2\nb,3\n' if phase == 1 else '\ufeffsku,quantity,status\n B ,2,active\nb,3,\n,bad,archived\n'
            path.write_text(text, encoding='utf-8')
            proc = subprocess.run([sys.executable, '-B', str(root / 'stock.py'), str(path)], capture_output=True, text=True, timeout=20)
            check('cli', lambda: proc.returncode == 0 and json.loads(proc.stdout) == [{'sku': 'b', 'quantity': 5}])
    elif task == 'S3':
        result = json.loads((root / 'result.json').read_text())
        entries = [json.loads(line) for line in (root / '.runtime/executions.jsonl').read_text().splitlines()]
        check('current_result', lambda: result['attempt'] == ('T1/A1' if phase == 1 else 'T1/A2') and result['total'] == (5 if phase == 1 else 9))
        check('input_binding', lambda: result['input_sha256'] == hashlib.sha256((root / '.runtime/input.csv').read_bytes()).hexdigest())
        check('one_execution_per_attempt', lambda: [e['attempt'] for e in entries] == (['T1/A1'] if phase == 1 else ['T1/A1', 'T1/A2']))
        check('uncommitted_config_preserved', lambda: json.loads((root / 'config.json').read_text())['label'] == 'keep-local-change')
        check('readable_current_input', lambda: sum(int(row['quantity']) for row in csv.DictReader((root / '.runtime/input.csv').read_text().splitlines())) == (5 if phase == 1 else 9))
    return {'task': task, 'phase': phase, 'passed': all(x['passed'] for x in results), 'checks': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task')
    parser.add_argument('root', type=Path)
    parser.add_argument('--phase', type=int, default=2)
    args = parser.parse_args()
    try:
        value = grade(args.task, args.root, args.phase)
    except Exception as exc:
        value = {'task': args.task, 'phase': args.phase, 'passed': False, 'error': str(exc)}
    print(json.dumps(value, ensure_ascii=False, indent=2))
