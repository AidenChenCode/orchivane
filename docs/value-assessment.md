# Value and optimization priorities

**English** · [简体中文](value-assessment.zh-CN.md)

Assessment: 2026-10-19; updated with recovery and paired-pilot evidence on 2026-10-20. This is a positioning assessment based on repository experiments, fixed-source reviews and the primary materials linked below. It is not a demand survey or proof of efficiency. This translation does not add a new upstream research run.

## Worth exploring; coordination savings remain unproven

The useful hypothesis is **one controller entry point for a long-running project, with durable ownership, effective decisions, delivery evidence and handoff responsibility**. New projects can clarify their needs in one chat, adding roles only when persistent independent context or acceptance warrants it. Small tasks need no roles merely to use the plugin.

Likely use cases include individuals and small teams already working across persistent chats, changing requirements across phases and needing independent acceptance. One-off fixes, short questions or workflows already handled well by the host often fit a single chat or existing engineering skills better. This is a workflow judgment; user-scale and willingness-to-pay data are unavailable.

The problem has external support, but the approach is not unique. Anthropic's long-running application report uses planning, generation, verification and structured handoffs, while describing how better models can make some process unnecessary and extra verification may not pay for every task. Our inference is to keep testing the smallest useful structure rather than prescribing a role count. [Source](https://www.anthropic.com/engineering/harness-design-long-running-apps).

Anthropic's Claude Code study associates domain expertise with successful outcomes, but uses model-based classification and does not directly measure the real-world value of artifacts. It is not an Orchivane experiment. It supports attention to user judgment and outcome verification, not a claim that adding a controller improves success. [Source](https://www.anthropic.com/research/claude-code-expertise).

## Relationship to existing approaches

| Approach | Capability emphasized in reviewed materials | Implication for Orchivane |
| --- | --- | --- |
| [Ponytail](research.md#lessons-from-ponytail) | Minimal implementation, reuse, scope and validation | Complement its engineering principles rather than duplicating them |
| [Superpowers](research.md#lessons-from-superpowers) | Planning, implementation, debugging and review workflows | Reuse engineering methods; focus here on persistent roles and continuity |
| [cablate/baton and jpawchan/baton](research.md#related-collaboration-projects) | Splitting costs, task contracts, frozen inputs and bound review evidence | Orchestration and acceptance are not unique; adopt evidence practices without another runtime |
| [uchimata2/handoff-skill](https://github.com/uchimata2/handoff-skill/blob/b4296dcc7476d9c4ec8be5ac6c9937b7b7dc23a8/README.md) | Cross-project handoff, a single source of truth and stale-document checks | A generated summary alone offers little distinction; verify successor runnability, sole ownership and preserved data |
| [Entire skills](https://github.com/entireio/skills/blob/fe5266f76d846222c73b080ce39fd803dd705198/README.md) | Retrieval, explanation and handoff using Entire checkpoints, sessions and Git history | Reuse an existing record system as evidence instead of building a transcript database |

[Research notes](research.md) identify the fixed source snapshots for the first four repositories. Only the READMEs and HEADs of the final two were reviewed; their implementations were not executed or audited. Comparisons cover what was read and do not assert missing competitor features. Native platforms may absorb more coordination capabilities, making portable rules and reproducible evidence more useful than dependence on particular tool names.

## What the evidence supports

- **Installation and actual use:** the [desktop record](evidence.md#desktop-installation) supports the local plugin route. The single unnamed-request case had title and co-installed-plugin confounds; it is not a reliable trigger-rate measurement.
- **Native creation, dispatch and independent acceptance:** the tool-library case finished at 19/20 and failed. It exposed frozen-reference and state-consistency issues, giving a reviewable failure rather than evidence of an advantage over one chat. [Case summary](evidence.md#native-project-example).
- **A strong baseline:** earlier no-skill responses already respected key constraints. Organizing rules is not automatically a new model capability.
- **Bounded recovery:** real takeover and subsequent execution, ignored-input recovery, stale receipts and serial duplicate dispatch were exercised. Initial review found two stale controller records. Archival, concurrency, context loss and crash windows remain untested. [Summary](evidence.md#handoff-and-recovery).
- **Paired pilot:** identical tasks, model and four-turn ceilings; three tasks completed per arm, zero extra coordination requests in both. Single-chat active duration was 216.163 seconds versus 293.142 for Orchivane. Reported total tokens were 1,120,054 versus 1,536,528, with extensive caching and unknown monetary cost. No specialist roles or real human timing were involved. S2 tested cross-file changes, not actual cross-role pressure. [Summary](evidence.md#paired-pilot).

## Priorities and acceptance conditions

1. **The first minute after installation:** documentation now separates visibility, enablement, discovery, reading and actual use. Preserve the older failed route as history; use native tools without adding another installer or permissions.
2. **Handoff and recovery:** the bounded experiment is complete, with the initial controller omissions corrected and independently rechecked. An injected ownership declaration is not a real old writer. Unknown creation outcomes, real archival and crash recovery need separately bounded inputs, costs and stop conditions. Existing rules already covered record synchronization; one omission did not justify more rules.
3. **Coordination cost:** the first paired pilot observed no reduction. Its short, well-specified tasks reached a zero-request floor in the baseline. Do not keep expanding the same easy suite to chase a positive result. Select a sanitized workflow with existing coordination burden and sustained role context; record real human minutes and relays before freezing independent repeats and their budgets. Equal turn ceilings are not equal token spend, and the native tool cannot enforce a token cap.

A relay is the user copying or restating existing information to synchronize another role; a new requirement is not a relay. Repeated explanation means an already confirmed constraint had to be supplied again after a transfer failure. Match business requirements and acceptance between arms rather than expanding the multi-chat arm's scope. Freeze costs and correction allowances first. If collaboration offers no benefit or adds burden, combine roles, remove unnecessary process or recognize that the task does not fit.

No independent service, database, wake-up hook, additional platform adapter or dashboard is planned without an actual target and test case. Those additions cannot answer whether the user coordinates less while delivery stays sound.

The immediate improvement is honest positioning, a clear single-chat path and reproducible comparative evidence. The pilot kept Skill 0.3.1 unchanged. Version 0.3.2 subsequently introduces English-first instructions and bilingual entry points; prior outcomes are not reassigned to the translated version. A separate [0.3.2 native check](../tests/bilingual-032.md) provides partial bilingual evidence, including a capacity interruption and a current-record closure gap; it does not measure coordination savings. Long-term value depends on representative workflow evidence, not the quantity of role tables and handoff documents produced.
