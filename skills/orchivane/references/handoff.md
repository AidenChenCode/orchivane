# Built-in handoff: leave work ready to continue

This module handles controller and specialist handoffs without a separate `session-handoff` installation. Appropriate reasons include a changed phase goal or repeated confusion about current requirements after correcting the materials. Chat length, age or one context compaction alone is not sufficient; do not invent context-usage thresholds.

## Preparation and authorization

“Prepare a handoff” authorizes materials only. Creation, task messages, ownership transfer, automation changes and archival each follow the user's explicit scope; do not ask again where authorization is sufficient. Handoff grants no new business execution, model-call, external-communication or publication authority.

Read the index, relevant changes, actual chat status and necessary history. Record coverage and failed reads; do not claim a summary covers the full history. Check old-owner writes and the handoff boundary. If work is still running, coordinate its authorized stopping point rather than interrupting it without permission.

## One package, receipts added as steps complete

Default location: `docs/handoffs/<handoff-id>.md`; reuse the project's existing layout. For an interrupted handoff, read the same package and inspect already-created targets before retrying. Avoid duplicate creation, transfers or archival.

```markdown
# Handoff ID
Status: preparing / awaiting takeover / blocked / accepted / switched / archived / post-archive verified
Old/new chats: actual titles, IDs, links; roles; current sole owner
Authorization: original request, scope of each action, effective budget/stop conditions
Current goal and decisions: sources, superseded decisions, unresolved conflicts
Deliverables and versions: entries, actual directory, worktree/branch/commit or material batch
Validation: verified, unverified, applicability of historical evidence
Next steps: unfinished work, dependencies, completion criteria, first action
Local dependencies and automation: locations, runtime needs, frozen inputs, schedule ID/target/cadence/status
Preservation: independent destination, scope/checks, known missing items, recovery/read checks
Takeover receipt: actual reading/verification, role understanding, next step, gaps
Switch/archive receipts: actual results, failure/retry point, post-archive owner and verification
```

Keep the summary about one page; attach large asset inventories separately. Do not copy whole transcripts or store real credentials.

## Safe execution order

1. **Ensure dependencies survive the old chat.** Check attached worktrees, uncommitted source, ignored/untracked materials, databases and runtime dependencies. Native chat archival can also archive its worktree, and Git snapshots generally exclude ignored data. Preserve necessary materials somewhere independent of the old chat's archival; verify the inventory, key content hashes and actual readability. A symlink back into the directory being archived is not an independent backup. Use a consistent database backup or agreed write pause, not a live raw-file copy presented as reliable. Record already-missing materials separately; do not claim they were restored.
2. **Create or reuse the successor.** If the user wants a clean conversation, create a new task; a fork inherits history. Verify the actual ready ID. Inspect uncertain outcomes before creating again.
3. **Verify initial takeover read-only.** Give the recipient the package and a minimal task. Require its role, materials actually read, versions/paths, unfinished work, next step and gaps. The controller reads and checks that receipt; acknowledgment is not acceptance. Do not immediately rerun the business operation. Establish runnability with necessary low-cost checks, without unauthorized paid calls or deployment.
4. **Verify automation continuity.** Read the actual target and effective configuration. Rebinding must be authorized; preserve the prompt, cadence and other fields, then read them back. If live configuration differs from history, record the difference and check the effective source instead of restoring an old cadence. When only history is stale, the complete live configuration is verifiable, original human authorization does not conflict, and only target changes are allowed, preserve live settings and rebind the target, stating the historical scope checked. Do not block solely to reconstruct every past edit. Resolve conflicts involving explicit prohibitions, budgets/stop conditions, unknown task identity or concurrent writes before switching. Record rebinding separately from the first successful scheduled execution. Pausing/resuming also requires authority; prevent old and new owners from writing concurrently.
5. **Switch sole ownership only after acceptance.** Retain the original relationship if necessary materials are unreadable, old-owner writes conflict, important decisions are unverified or automation continuity is unclear. When conditions hold, update the current index and affected entries while preserving history and supersession. Without archival authorization, retain the old chat; the handoff can still be delivered.
6. **Archive last, then verify the actual state.** Archive only after authorization, preservation, takeover and automation checks. Keep the original name/link; do not manually delete directories. Confirm the old chat's status with native archival tools, then check required paths, independent preserved data and successor runnability. Pre-archive readability does not prove post-archive survival. On failure, handle only unfinished steps and use native recovery capabilities if needed; do not recreate an already-established successor.

**Additional requirement for controller handoff:** self-archival may end the current execution. Before archiving, name an authorized, actually accepted successor responsible for post-archive verification; it may perform final archival itself. If no capable owner has accepted, retain the old controller rather than archiving first and promising a later check. Mark the full process complete only with a takeover receipt, native archival confirmation and post-archive verification.

If preservation cannot be guaranteed, keep the old chat. If tools are unavailable, deliver the package and precise gaps, stating what was not created, switched or archived. Editing a status to “complete” cannot substitute for execution.
