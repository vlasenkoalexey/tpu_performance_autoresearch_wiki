# Codex Instructions

This repository is an autoresearch wiki for TPU model performance optimization.
The canonical cross-agent protocol is `SCHEMA.md`; read it and `wiki/index.md`
before doing wiki, experiment, or analysis work.

## Compatibility

- Keep `.claude/` as the canonical source for shared skills, scripts, and
  Claude Code agents.
- `.agents/skills` exposes the same skills to Codex. Treat the skill bodies as
  shared cross-agent workflow definitions.
- `.codex/` contains Codex-only adapters: MCP config, custom-agent wrappers,
  and hook wiring. Keep repo behavior additive so Claude and Antigravity remain
  compatible.

## Operating Rules

- Follow `SCHEMA.md` for page formats, wiki paths, lint rules, and the
  autoresearch loop.
- Do not modify `raw/` except through the controlled workflows documented in
  `SCHEMA.md` and `wiki/experiments/program.md`.
- Update `wiki/index.md` and the appropriate log after material wiki changes.
- Use one experiment page per run.
- For executed experiments, XProf and HLO analysis are mandatory before assigning
  a final verdict.
- Prefer repo skills in `.agents/skills` for lifecycle operations such as
  hypothesis formulation, experiment start/stop, retrospectives, lint, source
  ingestion, cluster scans, and AST extraction.

## Codex Translation Notes

- When a shared skill mentions `AskUserQuestion`, ask the user directly unless
  the current Codex surface provides an equivalent structured prompt.
- When a shared skill mentions Claude `/loop`, `ScheduleWakeup`, `Task`,
  `TaskStop`, or background subagent notifications, translate that step to the
  available Codex subagent, hook, or automation mechanism. Do not pretend the
  Claude primitive exists.
- When a shared skill references `.claude/scripts`, use those scripts in place;
  they are intentionally shared.
- When a shared skill references `.claude/agents`, use the corresponding
  `.codex/agents/*.toml` wrapper if running under Codex.
