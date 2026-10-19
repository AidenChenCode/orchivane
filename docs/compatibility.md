# Compatibility and current design basis

Checked against primary documentation on 2026-10-19. Availability is a capability question, not a brand-name guarantee.

| Surface | Supported claim | Limit |
| --- | --- | --- |
| Agent Skills-compatible reader | Standard SKILL.md, progressive references, no runtime dependency | The host must actually load the skill; no automatic tool entitlement |
| Codex desktop with native chat tools | This release includes a real creation → dispatch → artifact → review experiment | A documented run on one host is not every account/client version |
| Codex CLI / other skill clients | Instructions and records can be used | Native persistent-chat control must be verified separately; subagents are not a drop-in substitute |
| Claude Code agent teams | Relevant conceptual comparison | No tested adapter or Claude plugin manifest in this release |
| Portable / Codex plugin package | Root and compatibility manifests plus a repo-local catalog | Marketplace/UI installation is not certified by static validation |

The [Agent Skills specification](https://agentskills.io/specification) standardizes skill files and progressive loading; it does not standardize chat creation or archival. The core stays independent of a host, and the Codex reference documents native capabilities that must exist at execution time. Other clients can fall back to files and copyable task briefs without pretending a message was sent.

[OpenAI's plugin packaging guide](https://developers.openai.com/plugins/build/plugins) distinguishes portable manifests, compatibility manifests and local catalogs. The repository ships all three relevant files, no MCP server or hooks. The repo catalog points to its own root and makes the package available; it does not silently install or enable it.

[Claude Code's agent-team documentation](https://code.claude.com/docs/en/agent-teams) distinguishes teams and subagents and describes their coordination cost and lifecycle limits. That supports our distinction between durable user-visible roles and temporary helpers. It does not establish that Codex-native tools work in Claude Code. We do not copy tool names between runtimes or enable experimental features for the user.

[Anthropic's multi-agent research account](https://www.anthropic.com/engineering/multi-agent-research-system) emphasizes delegation boundaries, complementary work and evaluation. Its results belong to its research system; this project claims no inherited quality or efficiency gain. [Context engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) motivates concise durable records and loading only relevant evidence, rather than copying complete chat histories.

## Observed installation behavior

A full standalone copy in the documented user skill directory was discovered by Codex CLI 0.157.1 using app-server skills/list with forceReload=true, enabled=true, with no parsing errors. A symlink into this plugin repository appeared under a namespaced skill name in the CLI. Neither observation certifies the desktop skill catalog: three newly created desktop test chats did not list the skill, while an explicitly requested file read loaded version0.3.0 and all five references. Root cause remains unconfirmed. No desktop restart, plugin UI install or unrelated configuration changes were performed.

## What is deliberately outside the package

No background daemon, automatic role creation, centralized database, provider account access or new runtime protocol. Native tools already own those capabilities. Add an adapter only with a real target client, a minimal reproducible use case and an end-to-end result. Cross-host transfer, long-running scheduling, safe archival and interrupted-creation recovery each require separate real evidence before claiming support at the same level as the tested dispatch path.
