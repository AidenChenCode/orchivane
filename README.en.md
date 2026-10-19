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

Tested with Codex CLI 0.157.1: plugin0.3.1 is installed and enabled, and its cached skill is discovered as `orchivane:orchivane`. Say “Use Orchivane” or select the skill name shown by your client. A supported desktop client can expose the **Orchivane** source in its Plugins Directory; restart at a suitable time if that source has not refreshed. Desktop UI visibility and fresh desktop-chat loading have not been verified. See [official packaging guidance](https://developers.openai.com/plugins/build/plugins); command support depends on your installed CLI.

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

The former Session Control 0.3.0 standalone copy was discovered by Codex CLI 0.157.1, but three fresh desktop test chats still did not list it. Explicit file loading worked; desktop automatic discovery and plugin UI installation remain unresolved/unverified respectively. See the evaluation record for the current release's checks.

Read [the evaluation record](tests/evaluation.md), [native reproduction protocol](tests/native-e2e.md), and [compatibility notes](docs/compatibility.md). Static checks are not behavioral tests. A native chat experiment is not proof of marketplace auto-loading, archival safety, long-running scheduling or a performance improvement over one agent.

The workflow is primarily written in Chinese and can be requested in English; language-specific behavior has not been separately benchmarked. Missing native tools degrade to explicit files and copyable briefs, never a false claim that sessions were created or messages sent.

Design references include [Ponytail and Superpowers](docs/research.md), the Agent Skills format and current vendor guidance on context and multi-agent coordination. Their benchmark results are not claimed as results of this project. No upstream implementation is vendored.
