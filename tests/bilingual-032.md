# Orchivane 0.3.2: native bilingual and handoff check

[简体中文](bilingual-032.zh-CN.md)

Date: 2026-10-20. Subject: installed plugin 0.3.2, source `b473f8507f1e5867591a3f9724f7e73cfbcf563e`.

## Observed result

**The upgrade and fresh-chat loading passed. This is partial behavioral evidence, not a clean bilingual nonregression result.** Four new native chats dispatched eight of the ten allowed turns: seven completed and one failed. Actual turn contexts recorded `gpt-6.1-sol` with `high` effort. Cumulative native turn duration was 547.553 seconds, including the failed turn; this is not elapsed wall time or human coordination time.

| Check | Chinese → English | English → Chinese |
| --- | --- | --- |
| Installed 0.3.2 entry actually read by source and successor | Passed | Passed |
| Requested-language planning; minimal structure; no project writes | Passed | Passed |
| A1 once, input/configuration preservation, durable handoff | Passed; 5 preserved files | Passed; 8 preserved files |
| Fresh successor read-only acceptance | Incomplete: host capacity error | Passed; all project file hashes unchanged |
| Controller switch, A2 once against R2 | Not dispatched | Passed; 5/5 functional checks |
| Exact repeated dispatch, no extra apply | Not dispatched | Passed; actual audit remains A1 then A2 |
| Current records agree with final phase before controller closure | Not reached | Failed: current index remained at 4/5 and asked for an already completed final check |

Both source chats used the requested language, read setup, recommended one owner for this small task and did not repeat questions already answered. Neither changed project files during planning. Both A1 deliveries passed all five reused functional checks. The completed successor used Chinese to accept English materials, read setup and handoff, preserved the uncommitted configuration and A1 evidence, and correctly reported 5/5 used in its final response. Its duplicate turn left every project file unchanged; the protected source, configuration, input, result and actual audit hashes all matched the prior phase.

### Retained failures and controller closure

The English successor read the installed entry and began an English response, then the host ended its turn with `Selected model is at capacity. Please try a different model.` No acceptance receipt was completed. The controller retained the old owner, verified unchanged project files and did not dispatch A2 or retry. This is an infrastructure interruption, not evidence that English handoff passes or that translation caused a failure.

The Chinese successor's final response had the correct budget, while the current file still described phase 4. The protocol asked for current-record consistency, and the repeated execution prompt requested record updates, but the controller's phase-4 index also required the last phase to be read-only. This conflicting instruction is a test-harness limitation: the stale file is observable, but cannot be attributed to translation alone. A verbal explanation that a *current* index is historical does not update that entry for the next reader.

After grading, the controller preserved both pre-closure indices, wrote explicit closure records and verified unchanged business artifacts. The stopped chain now states no takeover or A2; the completed functional chain records 5/5 used and no next execution. This administrative correction is recorded separately and does not convert the original current-record check to a pass. No solver was awakened for repair. The skill and manifests remain unchanged at 0.3.2.

For a future trial, explicitly separate immutable business files from mutable coordination records. If the final check is wholly read-only, assign current-index closure to the controller in the frozen protocol and grade it after that closure. If the successor owns closure, permit only those record edits. Do not change the present trial's rules retroactively. A separate bounded run is still needed to finish the English acceptance direction and evaluate the clarified closure boundary.

An evaluator-only Git status command was initially run in the lab parent rather than a Git repository and returned 128. It made no fixture changes; subsequent inspection targeted the assigned repositories. It is not counted as a solver turn or a behavioral failure.

## Published evidence and replay

[Structured results](outputs/v0.3.2/results.json) include per-phase status, duration, cached module reads, functional grades and the failed current-record check. [Chinese-to-English artifacts](outputs/v0.3.2/zh-to-en-artifacts.json) end at A1; [English-to-Chinese artifacts](outputs/v0.3.2/en-to-zh-artifacts.json) end at A2. [First-chain records](outputs/v0.3.2/zh-to-en-records.json) and [second-chain records](outputs/v0.3.2/en-to-zh-records.json) preserve sanitized before/after controller closure. These are derivatives of private receipts, not independently authenticated raw chat exports.

Each artifact JSON includes the text of four business files and their hashes. To replay the five functional checks offline, place those four text values at their named paths in an empty temporary directory, copy `tests/fixtures/recovery/report.py` there, verify the provided hashes, then run `python tests/paired/grade.py S3 <temporary-directory> --phase 1` for Chinese-to-English, or `--phase 2` for English-to-Chinese. Inspect the JSON `passed` value; the grader process exit code alone is not the result. Offline replay cannot verify native discovery, language, ownership or duplicate behavior.

## Method fixed before execution

Two isolated copies of the existing [recovery fixture](fixtures/recovery/report.py) used identical starting files. Chinese planning/preparation was followed by a fresh English successor; English planning/preparation by a fresh Chinese successor. The four native chats received no old conversation transcript. Requests named Orchivane but supplied neither its installation path nor the expected version; each had to find and read the declared installed entry. This tests explicit discovery and use, not implicit selection frequency.

The ceiling was four chats and ten aggregate solver turns, five phases per case: read-only planning, A1 preparation, read-only successor acceptance, A2 execution after controller approval/ownership switch, and an identical repeated execution request. Each phase had one turn; a failed chain stopped without consuming later phases as repair. No model override, additional paid API or hard token cap was used. Controller dispatch, inspection and mechanical ownership/input updates are outside solver-turn totals and are not evidence of lower human coordination cost.

A1 consumes two rows totaling 5. After accepted takeover, the controller replaces the input with three rows totaling 9 for A2. The script appends on every apply and has no deduplication. Uncommitted configuration must retain `keep-local-change`; ignored input/audit files and A1 evidence must survive. The existing [paired S3 grader](paired/grade.py) checks result, input binding, attempt sequence, configuration and input. Controller inspection additionally checks language, actual tool reads, read-only file hashes, sole ownership and dispatch boundaries. No blind human calibration was performed.

The frozen [plan](outputs/v0.3.2/plan.json), [sanitized prompts](outputs/v0.3.2/prompts.json), [initial hashes](outputs/v0.3.2/initial-hashes.json) and [installation hashes](outputs/v0.3.2/installation.json) are public. Original native receipts, real chat identifiers, local paths and configuration backups remain private. Historical 0.3.1 evidence is a reference, not a new control arm.

## Installation

The prior 0.3.1 cache and local configuration were preserved privately. Marketplace upgrade and plugin installation reported 0.3.2 installed and enabled. All seven installed skill files matched source bytes. Fresh chats actually read the cached 0.3.2 entry without a path fallback. No restart or unrelated plugin changes were made. Desktop directory visibility remains the user's earlier observation; this run verifies actual fresh-chat loading rather than a new UI inspection.

## Repository checks and scope

Static package/link/privacy validation, all 21 existing unit tests, and both published artifact replays passed. The first publication check rejected a redacted controller-link placeholder that still used the private-link URI scheme; it was replaced by a plain placeholder before publication. Final installation inspection still reported 0.3.2 installed/enabled and seven unchanged skill hashes. These checks validate packaging and evidence consistency, not missing native phases.

Current English/Chinese READMEs, compatibility, evidence, evaluation and value-assessment entries were synchronized. Historical examples and paired outputs remain unchanged; research sources, code, skill instructions and manifests did not need changes. The incomplete direction and untested archival/concurrency properties remain explicitly unverified.

## Limits

Other installed plugins remained enabled; native traces also show Superpowers entry reads. Detailed prompts explicitly supplied stage boundaries and budgets. These observations cannot isolate Orchivane's causal contribution, prove translation equivalence, establish human time savings or certify all clients. One run per direction cannot estimate reliability. Real archival, concurrent writers, transport retries, crashes and implicit activation rates were not tested. Local preservation copies were checked for readability and byte equality, not survival after archival.
