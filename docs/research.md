# Design lessons from Ponytail, Superpowers and related projects

**English** · [简体中文](research.zh-CN.md)

Research date: 2026-10-19; paired-pilot follow-up: 2026-10-20. The original review read public source and manifests, not just READMEs. Upstream hooks and installers were not executed. Commit references identify the reviewed snapshots, not promises about future upstream behavior. This English edition translates that research; it is not a new upstream audit.

| Project | Reviewed version | Fixed source |
| --- | --- | --- |
| Ponytail | Manifest 5.3.2 | [09c434ab73ca43761c5d8b0c5d341926c2fba710](https://github.com/DietrichGebert/ponytail/tree/09c434ab73ca43761c5d8b0c5d341926c2fba710) |
| Superpowers | Manifest 7.0.0 | [bb92a77741419a4ab5f06e711a283343f1ada0c3](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) |

The locally installed Superpowers skills were 6.4.2; the source review covered 7.0.0. These are different observations. Orchivane generalizes an existing multi-chat workflow and personal handoff/health-check practices, excluding original project identities, private material and runtime data.

## Lessons from Ponytail

**Reuse before building another system.** Its skill prefers existing capabilities, the standard library and minimal implementation while retaining validation, error handling and safety. Orchivane uses native chat tools and Markdown records instead of a message bus, scheduler, role database or additional MCP service. [Core skill](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/skills/ponytail/SKILL.md).

**Separate instructions from distribution.** Ponytail ships skills, manifests and lifecycle hooks. Orchivane adopts the lightweight packaging pattern but does not copy automatic per-session or per-prompt injection; its instructions apply to collaboration tasks. [Manifest](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/.codex-plugin/plugin.json), [hook configuration](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/hooks/claude-codex-hooks.json).

**Efficiency claims need corresponding correctness evidence.** The reviewed 2026-10-07 benchmark reports its models, CLI, 39 tasks, five runs per arm and three arms totaling 585 runs, with restrictions on agent shell access. Eighteen surgical tasks had hidden correctness tests; delivery/compilation checks on other tasks do not establish comprehensive quality. We learn from those explicit limits rather than borrowing its savings claims. [Benchmark report](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/benchmarks/results/2026-10-07-agentic.md).

## Lessons from Superpowers

**Route at the entry; load details by phase.** Separate planning, execution, debugging and review skills avoid loading everything at once. Orchivane uses one entry with progressive references, reducing competing similar triggers and assigning concrete outputs to setup, dispatch, inspection and handoff. [Skill directory](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills).

**Give implementers a contract and controllers real receipts.** Its implementer brief includes goals, context, constraints, self-checks and delivery status. Execution records preserve progress across context recovery. Orchivane adapts these ideas to persistent-chat briefs and change records while distinguishing specification compliance from actual quality. [Implementer prompt](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/implementer-prompt.md), [execution skill](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/SKILL.md).

**Test skills through behavior.** Its writing guidance uses pressure scenarios to check whether rules change execution. More text is not proof of effectiveness. Orchivane keeps baseline responses, actual generated artifacts and limits. The early baseline already respected key boundaries, so those checks did not establish an improvement. [Writing skills](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-skills/SKILL.md).

We do not transplant the whole engineering workflow: temporary subagents and persistent specialists have different lifecycles, small changes need not receive repeated review, and collaboration does not always require a full development process. The reviewed 7.0.0 execution mechanism cannot override user budgets, stop conditions or pauses. Its Codex manifest explicitly has empty hooks; Orchivane likewise installs no lifecycle hook. [Codex manifest](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/.codex-plugin/plugin.json).

## Practices retained in Orchivane

1. One user-facing controller; roles follow deliverables, and existing authorization is reused.
2. Specialists provide artifacts, versions, validation and remaining issues; the controller verifies closure.
3. Corrections reach affected current records while original sources and frozen versions remain intact.
4. Handoffs verify actual takeover, automation continuity, independent preservation of ignored data and post-archive survival.
5. Health checks focus on changes, disclose gaps and avoid repeated wake-ups.

This collaboration layer can complement Ponytail's implementation principles and Superpowers' engineering skills. It does not replace host permissions or turn a skill file into an autonomous runtime.

## Packaging basis

The root portable `plugin.json`, compatibility `.codex-plugin/plugin.json` and standalone skill follow the [packaging documentation](https://developers.openai.com/plugins/build/plugins) and [skill concepts](https://developers.openai.com/plugins/concepts/skills) read during the original review. A manifest is not proof of installation. Official-directory submission and cross-client installation were not performed in that review; later local plugin evidence is recorded separately.

## Related collaboration projects

These projects were found while checking the proposed name Baton on 2026-10-19. The review read fixed skills, protocols and evaluation documents, without installing or executing them. Their mechanisms are documented concepts, not effects verified by Orchivane.

| Project and snapshot | Useful ideas | Orchivane's choice |
| --- | --- | --- |
| [cablate/baton](https://github.com/cablate/baton/tree/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943) | Evaluate a single-worker alternative, independence, one write owner and a final integrator; include rereading and integration costs | Setup already considers single-chat work and overhead; test that decision rather than filling idle parallel slots |
| [jpawchan/baton](https://github.com/jpawchan/baton/tree/ca53c1649f9d1242e51ac43fc3712513067fafcf) | Freeze dispatched context; bind review to task, attempt, report and diff; use leases to prevent stale writes | Keep native chat tools and trace attempts/evidence in existing records; no demonstrated need for another lock, lease, CLI or scheduler runtime |

Sources: [dispatch skill](https://github.com/cablate/baton/blob/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943/SKILL.md), [paired protocol](https://github.com/cablate/baton/blob/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943/benchmarks/case-01-multi-surface-refactor/protocol.md), [task/review specification](https://github.com/jpawchan/baton/blob/ca53c1649f9d1242e51ac43fc3712513067fafcf/SPEC.md), [benchmark records](https://github.com/jpawchan/baton/blob/ca53c1649f9d1242e51ac43fc3712513067fafcf/benchmarks/README.md).

## Follow-up priorities and actual progress

1. **Installation experience:** the local 0.3.1 plugin route passed enablement, user-observed desktop visibility and actual use in fresh chats. The README includes a read-only check. The older standalone-discovery failure remains unexplained; this is not a cross-platform fix. [Evidence](evidence.md#desktop-installation).
2. **Trace dispatch and acceptance to the same attempt:** reuse change records for dispatch attempts, frozen inputs, tool results and artifact versions. Confirm repeated need before adding a reference checker, and target observed relative-path failures rather than building a task database.
3. **Recovery:** a bounded 2026-10-20 experiment covered successor continuation, missing ignored inputs, stale evidence, injected ownership conflict and serial duplicate dispatch. It exposed stale controller records. Unknown creation outcomes, real concurrency, context loss and archival remain untested. [Evidence](evidence.md#handoff-and-recovery).
4. **Whether splitting pays:** the first paired pilot completed three tasks per arm with zero extra coordination requests in both; Orchivane used more cumulative time and tokens. No specialists were created, so sustained splitting remains unmeasured. Find a real cross-role coordination burden and measure human time before claiming savings. [Evidence](evidence.md#paired-pilot).

See the [value assessment](value-assessment.md) for current decisions. The project remains focused on persistent roles, one controller and continuity across phases, without borrowing upstream results or expanding into a background orchestration platform without a demonstrated need.
