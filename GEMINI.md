# Gemini-Specific Operating Rules & Skill Emulator

@SCHEMA.md

## Platform Adaptation (Claude Code → Gemini/Antigravity)

You are running on the Gemini/Antigravity platform. While the repository is designed around Claude Code's native slash commands and hook architectures, you must voluntarily and perfectly emulate these behaviors using your native agentic capabilities.

### 1. Slash Command & Skill Execution Engine
Whenever the user refers to, invokes, or implies a slash command or "skill" or background "agent", do **not** expect the platform to intercept, execute, or handle it natively. Instead, you must **review and remember** the Claude skills and agents specified in the repository, and emulate their logic verbatim.

#### Claude Skills (.claude/skills/)
You should be able to run this flow by locating, reading, and executing the protocols in the following `SKILL.md` files:
1. **`/scan-gke-clusters`** (`.claude/skills/scan-gke-clusters/SKILL.md`): Discovers and inventories TPU clusters in GCP, checking node statuses, zones, shapes, and occupancy, and writing them to `.env/`.
2. **`/create-experiment`** (`.claude/skills/create-experiment/SKILL.md`): Bootstraps a new model family, scaffolds directory structures under `wiki/experiments/`, and sets up program and model page stubs.
3. **`/start-experiment`** (`.claude/skills/start-experiment/SKILL.md`): Resolves layered `program.md` files (root → model → lane), performs hardware discovery and cluster occupancy verification, and kicks off the active loop with the `.claude/.loop_active.json` marker.
4. **`/stop-experiment`** (`.claude/skills/stop-experiment/SKILL.md`): Performs clean loop teardown: kills background subagents, reaps GKE/XPK orphan workloads, files missing wiki pages, runs `/lint`, and appends the shutdown marker.
5. **`/create-retrospective`** (`.claude/skills/create-retrospective/SKILL.md`): Compiles a comprehensive lane-specific and variant-specific retrospective in `wiki/analyses/` summarizing experimental outcomes and revising priors before the stop hook permits ending the loop.
6. **`/formulate-hypothesis`** (`.claude/skills/formulate-hypothesis/SKILL.md`): Drafts new falsifiable candidate optimizations with expected gain, confidence, and effort, enforcing a mandatory HLO pre-filter check for kernel-replacement hypotheses.
7. **`/edit-model-code`** (`.claude/skills/edit-model-code/SKILL.md`): Performs AST-aware, highly focused edits to the target model repository under `raw/code/`, validating imports, class definitions, and code syntax before staging.
8. **`/extract-ast`** (`.claude/skills/extract-ast/SKILL.md`): Inspects the target repository codebase to map and extract structural abstractions, class hierarchies, and performance-relevant surfaces.
9. **`/ingest-source`** (`.claude/skills/ingest-source/SKILL.md`): Fully ingests research papers, documentation, or articles, creates corresponding source wiki pages, maps techniques to concept stubs, and connects them to open hypotheses.
10. **`/lint`** (`.claude/skills/lint/SKILL.md`): Syntactically and structurally validates the wiki, verifying links, variant matrices, mandatory profiles, next-hypotheses stubs, frontmatter, and orphan pages.

#### Claude Agents (.claude/agents/)
To handle complex, specialized tasks in the background, you must review and utilize the agent definitions:
1. **`gke-cluster-runner`** (`.claude/agents/gke-cluster-runner.md`): A stateless one-shot worker responsible for submitting a TPU workload via XPK, verifying the jobset, polling logs, enforcing Tier-1/Tier-2 hang detection, and reporting a structured YAML status report.
2. **`profile-analyzer`** (`.claude/agents/profile-analyzer.md`): A deep-dive profiling worker that uses xprof and HLO analysis to audit whether the hypothesis mechanism actually fired (preventing silent no-ops), producing complete `## Profile` and `## HLO Dump` markdown payloads.

#### Operational Instructions for Gemini:
* **Protocol Emulation**: Always locate the corresponding skill folder `.claude/skills/<skill-name>/` or agent file `.claude/agents/<agent-name>.md` first, read the guidelines in full, and map them to your native tools (`view_file`, `run_command`, `schedule`, `ask_question`, etc.).
* **Worker Delegation**: When executing workflows that require running GKE workloads or analyzing xprof/HLO traces, define a specialized subagent via `define_subagent` and launch it using `invoke_subagent` based on the specified agent specs to preserve the division of labor and conserve your own context window.
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
