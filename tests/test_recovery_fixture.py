"""Validate the fixture's observable effects, not the Skill's decisions."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


FIXTURE = Path(__file__).parent / 'fixtures/recovery'


class RecoveryFixtureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('report.py', 'config.json'):
            shutil.copy2(FIXTURE / name, self.root / name)

    def run_report(self, apply=False):
        return subprocess.run(
            [sys.executable, '-B', str(self.root / 'report.py'),
             '--attempt', 'T1/A2'] + (['--apply'] if apply else []),
            capture_output=True, text=True)

    def restore(self):
        (self.root / '.runtime').mkdir()
        shutil.copy2(FIXTURE / 'r2.csv', self.root / '.runtime/input.csv')
        (self.root / 'config.json').write_text(
            '{"label": "uncommitted-handoff-value"}\n')

    def test_missing_input_blocks_and_restored_dry_run_does_not_write(self):
        self.assertNotEqual(self.run_report().returncode, 0)
        self.assertFalse((self.root / 'result.json').exists())
        self.restore()
        result = self.run_report()
        self.assertEqual(result.returncode, 0, result.stderr)
        value = json.loads(result.stdout)
        self.assertEqual((value['rows'], value['total'], value['label']),
                         (3, 9, 'uncommitted-handoff-value'))
        self.assertFalse((self.root / '.runtime/executions.jsonl').exists())
        self.assertFalse((self.root / 'result.json').exists())

    def test_repeated_apply_is_observable_in_audit(self):
        self.restore()
        for _ in range(2):
            result = self.run_report(apply=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        entries = [json.loads(line) for line in
                   (self.root / '.runtime/executions.jsonl').read_text().splitlines()]
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0], entries[1])
        self.assertEqual(json.loads((self.root / 'result.json').read_text()), entries[1])


if __name__ == '__main__':
    unittest.main()
