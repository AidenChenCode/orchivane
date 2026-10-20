# Orchivane 0.3.1

[中文](README.md) · [MIT](LICENSE) · [Contributing](CONTRIBUTING.md)

**One intent. Many minds. Work carried forward.** Orchivane combines the imagery of orchestration and a direction vane: specialist roles working toward one shared goal.

## Who keeps the project moving across AI conversations?

You open separate AI conversations for research, implementation and testing. Each can handle a task, while the coordination still lands on you:

- Copying conclusions between windows and explaining the same constraints again.
- Reconciling overlapping edits and work based on outdated interfaces.
- Starting a fresh conversation without losing decisions, local changes or unfinished responsibilities.
- Figuring out whether “done” means written, tested, accepted, pushed or deployed.
- Deciding who should act next, what context they need and which result to trust.

Orchivane gives that work a single controller entry point. The controller clarifies the goal, chooses a useful collaboration structure, assigns one owner per deliverable and verifies results against explicit inputs and acceptance conditions. Handoffs carry decisions, evidence, limits and next steps forward. Small tasks can stay in one conversation.

For example, ask the controller to add login to an existing product. It first checks the current identity design and interfaces, decides how implementation and independent review should be divided, then reports implementation, verification, push and deployment separately. You guide the goal and important tradeoffs without repeating the whole request in every role's chat. This illustrates the intended workflow; actual tool availability and tested limits are documented below.

## Start from an idea

A reusable skill for **one controller + persistent specialist chats**. Start with an idea, research and clarify the work, choose a collaboration structure, then dispatch and accept concrete deliverables. No existing sessions or repository are required.

The controller remains the user's single coordination point. Each deliverable has one owner. Existing human authorization is reused, results are checked against actual artifacts and versions, and safe handoff preserves local data and responsibilities. Temporary subagents and persistent user-visible sessions have different lifecycles.

## Start

```text
Use $orchivane. I have a new project idea and no other sessions.
Research it with me, clarify the important constraints, and recommend
the right collaboration structure and a concrete starting plan.
```

The skill may recommend staying in one conversation for a small or unclear task. When multiple sessions are useful, it defines outputs, dependencies, write ownership and acceptance before creating or messaging them within the user's authorized scope.

| Mode | Output |
| --- | --- |
| Discovery / setup | Research-backed brief, role rationale, first tasks |
| Dispatch / acceptance | Concrete assignments, actual receipts, versioned outcomes |
| Incremental audit | Changed issues and evidence gaps, without repeated pings |
| Handoff | Successor acceptance, data preservation, schedule transfer and post-archive checks |

## Install

### Plugin installation (recommended)

Add the GitHub marketplace source, then install the plugin. No manual clone is required:

```sh
codex plugin marketplace add alexzhu0/orchivane
codex plugin add orchivane@orchivane-local
codex plugin list --marketplace orchivane-local --json
```

Tested with Codex CLI 0.157.1: plugin 0.3.1 is installed and enabled, and its cached skill is discovered as `orchivane:orchivane`. On 2026-10-19, the user confirmed visibility in the desktop Plugins Directory, and two fresh desktop chats actually read and used the cached skill without restarting the app. One request body did not name the skill. See [observations, limits and reproduction steps](tests/desktop-plugin.md). Say “Use Orchivane” or select the skill name shown by your client. See [official packaging guidance](https://developers.openai.com/plugins/build/plugins); command support depends on your installed CLI.

There is no background process to start: the host loads these instructions when relevant. To check your installation, ask a new chat to find Orchivane in its available-skills list, read the declared entry, report its version and recommend whether an unclear new project needs multiple roles. Ask it to report absence rather than search for a fallback file, and not to create chats or dispatch work. Being listed, being read and being used are separate checks. Name the skill explicitly when you want reliable selection; implicit selection depends on the host, model and other skills.

This installs from the public GitHub source; Orchivane is not listed in the official curated directory. Preserve any existing standalone skill outside discovery directories and keep only one active installation source after verifying the plugin. Do not discard local customizations.

### Standalone skill

```sh
git clone https://github.com/alexzhu0/orchivane.git
cd orchivane
```

Version 0.3.1 renames Session Control to Orchivane; invoke it with `$orchivane`. If you installed `session-control`, first preserve that directory and any local customizations outside skill discovery directories, then install the new directory. Historical tests retain their original name and version; renaming is not a new behavioral result.

Copy the complete `skills/orchivane` directory into a skill directory supported by your host. For current Codex local skill discovery, use the user `.agents/skills/` directory; keep an existing supported `.codex/skills/` installation rather than installing a duplicate. See the [Chinese README](README.md) for a non-overwriting macOS/Linux command and [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for current paths.

The repo also includes portable and Codex compatibility manifests plus a repo-local plugin catalog. Use either the standalone skill or the plugin, not both. Catalog availability, installation and native chat tools depend on the client. This package supplies instructions, not new tool permissions, a daemon or an MCP server.

The skill has **no runtime dependency**. Python and PyYAML are only used for the offline development checks:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

## Evidence and limits

The [real native example](examples/tool-library/README.md) completed creation, dispatch and independent review: 17/20 initially, 19/20 after the one allowed correction, with final acceptance still **failed**. The experiment used frozen skill 0.2.0; 0.3.0 incorporates the resulting changes and has not had a full native rerun.

A separate [0.3.1 handoff/recovery experiment](tests/handoff-recovery.md) used three native desktop chats and an isolated CSV fixture. It exercised missing ignored inputs, backup restoration, preserved uncommitted configuration, an injected ownership conflict, stale evidence and serial duplicate dispatch. A successor actually completed the new input version once. Initial independent review found two stale controller records despite the six behavioral checks being supported; one correction and an independent closure review resolved them. Failed checks and measurement corrections remain documented. This does not test archival, real concurrent writers, crashes or retries after context loss.

The former Session Control 0.3.0 standalone copy was discovered by Codex CLI 0.157.1, but three fresh desktop test chats did not list it. That route's root cause remains unknown. The later 0.3.1 plugin installation route passed discovery and use in fresh desktop chats; this does not retroactively fix or retest standalone installation. UI visibility was user-reported; installation used the CLI, not UI buttons.

Read [the evaluation record](tests/evaluation.md), [native reproduction protocol](tests/native-e2e.md), and [compatibility notes](docs/compatibility.md). Static checks are not behavioral tests. A native chat experiment is not proof of marketplace auto-loading, archival safety, long-running scheduling or a performance improvement over one agent.

The workflow is primarily written in Chinese and can be requested in English; language-specific behavior has not been separately benchmarked. Missing native tools degrade to explicit files and copyable briefs, never a false claim that sessions were created or messages sent.

Design references include [Ponytail and Superpowers](docs/research.md), the Agent Skills format and current vendor guidance on context and multi-agent coordination. Their benchmark results are not claimed as results of this project. No upstream implementation is vendored.

The [value assessment and priorities](docs/value-assessment.md) focus on durable role ownership, evidence-backed handoffs and reducing human coordination. Quantified benefits still require controlled tests; broader orchestration infrastructure is not planned without demonstrated need.
