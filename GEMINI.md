# Gemini/Antigravity Operating Rules

@SCHEMA.md

## Platform Adaptation (Claude Code → Gemini/Antigravity)

You are running on Antigravity. Read `SCHEMA.md` (the cross-agent protocol) and `wiki/index.md` first. **Skills load natively** (see §1); the sections below map the few remaining Claude-Code-specific mechanisms — background agents, hooks, loops — to your native capabilities.

### 1. Skills — native, no emulation
Antigravity **natively discovers and runs** the skills under `.agents/skills/`: it loads each `SKILL.md`'s `name`/`description`, semantic-matches your intent, and loads the full skill on demand — the **same as Codex**. There is nothing to enumerate or emulate here, and no list to keep in sync; the `SKILL.md` files are the source of truth (this includes `/wikify-ingest-repo` for grounded codebase ingestion — see SCHEMA `INGEST-CODEBASE` step 5 / `ANSWER-CODEBASE-INTERNALS`).

The `.claude/agents/` definitions below are **different** — they are Claude-Code subagents, not native skills, so you must map them to your native subagent tools yourself.

#### Claude Agents (.claude/agents/)
To handle complex, specialized tasks in the background, you must review and utilize the agent definitions:
1. **`gke-cluster-runner`** (`.claude/agents/gke-cluster-runner.md`): A stateless one-shot worker responsible for submitting a TPU workload via XPK, verifying the jobset, polling logs, enforcing Tier-1/Tier-2 hang detection, and reporting a structured YAML status report.
2. **`profile-analyzer`** (`.claude/agents/profile-analyzer.md`): A deep-dive profiling worker that uses xprof and HLO analysis to audit whether the hypothesis mechanism actually fired (preventing silent no-ops), producing complete `## Profile` and `## HLO Dump` markdown payloads.

#### Operational Instructions for Gemini:
* **Agent mapping**: Skills are exposed natively — just follow the matched `SKILL.md`. For the `.claude/agents/` definitions, read the `<agent-name>.md` file first and map its guidelines to your native subagent tools.
* **Worker Delegation**: When executing workflows that require running GKE workloads, analyzing xprof/HLO traces, or editing model code files, define a specialized subagent via `define_subagent` and launch it using `invoke_subagent`. Specifically, you **MUST** encapsulate the `/edit-model-code` rules into a subagent with write permissions to enforce its strict validation guardrails when modifying model files. Do not modify model files natively.
* **Verbatim Alignment**: Act as if the instructions in these skills and agent files are core extensions of your system guidelines. Do not skip steps, ignore constraints, or bypass verification rules.

### 2. Never-Stop Hook & Retrospectives
* **Never-Stop Loop**: If `.claude/.loop_active.json` exists in the repository, you are in an active, autonomous never-stop session.
* **Stop Guardrail**: Do **NOT** stop or conclude the session unless a recent lane-specific retrospective file matching `*<model>*<lane>*retrospective*.md` exists in `wiki/analyses/` (written in the last 6 hours).
* **Voluntary Enforcement**: Since you do not have an automated shell-level hook to block your turn-end, you must **self-enforce** this guardrail by reading `.claude/stop_hook.sh` rules, running `/create-retrospective` when needed, and refusing to stop if the retrospective due-diligence is incomplete.

### 3. Session and Transcript Resolution
* In any script or instruction asking to locate Claude's transcript under `~/.claude/projects/` to extract `session_id`, bypass it by reading your own `Conversation ID` from your environment metadata. Write this Conversation ID directly as the `session_id` into `.claude/.loop_active.json`.

### 4. Background Loops and Scheduling
* Map any Claude-style `ScheduleWakeup` or `/loop` harness to your native `schedule` tool (One-shot timer or recurring cron mode) to handle autonomous, self-paced iterations cleanly and safely.

### 5. Subagent Dispatch
* Emulate Claude-style background agents (like `profile-analyzer` or `gke-cluster-runner`) by utilizing your native `invoke_subagent` or `define_subagent` tools. Pass explicit directory/GCS paths to subagents to ensure zero path translation issues.
