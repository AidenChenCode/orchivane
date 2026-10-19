# Reproduce the native multi-session experiment

This is an opt-in manual behavioral test. CI must not create real user sessions, send messages or consume external model budgets. Use a fresh isolated lab outside any production repository. The operator must authorize session creation and dispatch; archive, schedules, external communications and publication remain separate actions.

## Inputs and environment

- Freeze the complete Skill directory and record its metadata version and per-file SHA-256 hashes. If testing an older Skill without metadata, keep the release manifest with the snapshot.
- Record host/client version if available, actual tools used, which model settings were selected or left at host defaults, and any unrelated installed skills that could affect behavior. Do not invent unavailable token/cost measurements.
- Start with one controller and zero specialist chats. Ask the user to choose or delegate selection of the scenario. Record actual replies; distinguish controller-chosen fixture parameters from user requirements or research findings.
- Scenario: a fictional 20-item low-risk hand-tool lending pilot; manual confirmation, no fee/deposit, no real participants or deployment. The desired outputs are sourced research, a borrowing plan and inventory, and independent acceptance.

## Native sequence

1. The controller researches enough to understand the work and records a brief, role rationale, limits and acceptance criteria. Three roles are used here to exercise coordination, not to prove this small task requires three chats.
2. Create native research, design and review chats. Each receives the frozen Skill, an absolute shared lab path, explicit write ownership, its task, inputs, output contract and the original human authorization reference. Record each real returned ID immediately. Never replace native chats with temporary subagents while calling the run native E2E.
3. Research produces at least three primary-source references with facts and limitations. Design initially acknowledges readable inputs and waits for research. Review writes a checklist independently of the finished design. Neither waits in a file-polling loop.
4. Read actual outcomes, freeze research with a version/hash, dispatch the design task to the existing design chat, and retain the send result separately from acceptance.
5. Freeze the delivered plan and CSV, then dispatch the reviewer. Reviewer verifies sources and runs concrete scenarios against that exact version; only the review directory is writable.
6. If the reviewer finds issues, the controller sends one bounded correction task to the original author. Freeze the corrected version and request one independent retest. Preserve old inputs and failure findings. Stop after that round and report any remaining failure honestly.
7. Read final receipts and inspect actual files. Reconcile the current registry and task states; leave idle chats available unless archival was explicitly requested and separately verified.

## Required observations

Record created, dispatched, substantively accepted, delivered and independently reviewed as separate facts. Test shared-directory readability, input version identity, role/write boundaries, source provenance and unapproved-action avoidance. Record incidental failures such as stale registration or broken URLs and their actual resolution. An acceptance checklist is not an acceptance result.

Do not force a failure into the example to manufacture a fix. A reviewer may pass or fail it. Do not repeat until green without a new scope decision. Metrics may include real message count, iterations, observed elapsed time and verified artifacts, with their collection method; omit unavailable cost figures.

## Publication

Keep raw receipts, native IDs and private paths in the local lab. Publish a clearly labeled sanitized example with relative paths, frozen versions, substantive results and known limits. Hashes identify the sanitized published files; do not describe them as hashes of unchanged native logs. Readers can reproduce the protocol, but cannot use the original owner's session IDs.

This test does not validate marketplace auto-loading, archival, automated schedules, production operation, cross-client portability or statistical improvements over a single agent. Those require separate experiments.
