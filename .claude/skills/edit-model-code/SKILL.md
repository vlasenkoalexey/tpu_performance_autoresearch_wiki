---
name: edit-model-code
description: Coding-discipline guidelines for surgically modifying model code inside a per-experiment fork in the autoresearch loop. Adapts Andrej Karpathy's LLM-coding guidelines (think before coding, simplicity first, surgical changes, goal-driven execution) to this project's invariants — no semantics drift, one mechanism per experiment, the training run is the test, no kernel fallbacks. Invoke BEFORE opening any model-code file in the experiment fork (step 4 of program.md's "experiment loop"). Helps weaker LLMs stay disciplined under autoresearch-loop pressure where the agent is autonomous and can't ask clarifying questions. NOT for wiki edits, infra scripts, or trunk merges — those are out of scope.
---

You are about to modify model code inside a per-experiment fork. Read these guidelines FIRST and keep them in scope while editing. The goal is one minimal, surgical change that tests exactly one hypothesis.

This skill adapts [Andrej Karpathy's LLM-coding guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) (MIT-licensed) to the autoresearch loop. Where the upstream conflicts with this project's invariants, the autoresearch version wins.

## When to invoke this skill

- BEFORE step 4 ("Implement") of program.md's experiment loop — before opening any file in `wiki/experiments/<model>_autoresearch_optimization/<lane>/.repo/<exp-name>/<model-repo>/`.
- Re-invoke if the edit scope grows mid-session (you start touching files outside the original plan).
- Re-invoke for any cross-cutting refactor you're tempted to do "while you're in there".

NOT for: wiki page writes, infra scripts, the build step, the launch step. Those have their own discipline elsewhere.

## The four principles (Karpathy, adapted)

### 1. Think before coding — and document, don't ask

**Surface assumptions in the experiment page, not by interrupting the loop.**

The gke-cluster-runner is autonomous; the master loop can't pause to interactively clarify with the user. So the adaptation is:

- State your assumptions in the experiment page's "Hypothesis under test" or "Setup" section before editing.
- If multiple interpretations of the hypothesis exist, pick the **smaller-blast-radius** one and document why in the experiment page. Don't make both changes.
- If something is genuinely unclear and the wrong choice would burn cluster time, **refute the hypothesis cheaply with an inconclusive run** and surface the ambiguity in the verdict — that's a valid outcome of the loop.

### 2. Simplicity first — one mechanism per experiment

**Minimum code that tests this one hypothesis. Nothing speculative.**

- No features beyond what the hypothesis tests.
- No "while I'm here" cleanups, no abstractions for a single-use code path.
- No error handling for impossible scenarios (the training job will surface real errors).
- If you find yourself writing 200 lines of plumbing to test a 5-line idea, **the hypothesis is wrong** — refute it cheaply or reformulate.
- One mechanism per experiment. Don't bundle "fix imports + tune block size + add a fallback path". The wiki's signal depends on one variable changing per run.

The test: would a senior MLE on this stack say "you're doing too much"? If yes, simplify.

### 3. Surgical changes — stay inside the fork, match the codebase

**Touch only what you must. The fork is throwaway; the trunk is not.**

When editing inside the per-experiment fork:
- Don't "improve" adjacent code, formatting, or comments. They merge back to trunk on `supported` — gratuitous diffs make merges worse.
- Don't refactor things that aren't broken. The codebase's existing patterns are **load-bearing**: `shard_map` wrap, `set_*()` flags, FSDP rules, `with jax.default_device(...)` blocks. Match them.
- Don't touch files outside the hypothesis scope. Don't touch other experiments' folders. Don't touch trunk.
- If you notice unrelated dead code: mention it in the experiment page's "Observations", don't delete it.

Orphan cleanup rule: remove imports/variables/functions YOUR changes orphaned. Leave pre-existing dead code alone.

**The test**: every changed line should trace directly to the hypothesis being tested.

### 4. Goal-driven execution — the training run is the test

**The verifier is the cluster, not pytest.**

Transform the hypothesis into a verifiable goal stated in the experiment page:
- "Add tokamax CE kernel" → "Loss trajectory matches baseline within bf16 noise over ≥20 steps AND step MFU ≥ frontier + 0.3 pp"
- "Tune block size" → "Step MFU strictly increases vs current frontier with no compile-time / runtime regressions"

Refuted is a valid success of the loop. Don't try to "fix" a refutation by tweaking the test — that's how invariants get violated. If your code runs without crashing and produces a clean signal, your job is done; the verdict belongs to the master.

**Don't write pytest tests for experimental code.** The training run validates it. Unit tests are for code that's graduating upstream (unless explicitly instructed).

## Autoresearch-specific corollaries

These supplement the four principles and override the upstream Karpathy skill where they conflict.

### A. No semantics drift — this is THE invariant

bf16 stays bf16. The attention pattern doesn't change. Tokenizer doesn't change. Output distribution must be identical to the baseline at a fixed seed within bf16 noise.

If an optimization mutates output distribution: the verdict is `invalid` (not "supported with caveats"). Do not "fix" by tweaking the equivalence test, the seed, or the comparison window. Some math changes are acceptable WITH human approval (numerically-equivalent kernel swap, fused CE, equivalent RoPE) — see program.md's "What you CANNOT do" — but the loop runs autonomously so the answer is usually "ask in the experiment page's Verdict, don't decide unilaterally".

### B. No fallback paths in kernel code

A Pallas kernel that fails should **fail**, not silently fall back to XLA. `try/except` around a kernel call defeats the experiment's signal: the loop can't distinguish "kernel didn't fire" from "kernel fired and was slower". Let it crash; the verdict captures the signal.

Same rule for: shard_map wraps, fused ops, custom_vjp paths. If it errors, it errors loud.

### C. Comment policy

Only comment when the **WHY** is non-obvious — a hidden constraint, a subtle invariant, a workaround for a specific compiler / runtime bug.

Skip:
- WHAT comments (the well-named identifier is the doc).
- Experiment-narrative comments (`# v391y change`, `# perf: 4.18 pp lift`). Those belong in the wiki, not the code. Code outlives experiments.
- TODO comments. Use the wiki's hypothesis backlog.

A short `# perf: see wiki/experiments/<...>` is acceptable ONLY when a future code reader genuinely needs the pointer at the change site (rare — usually the commit message footer suffices).

### D. The commit footer is mandatory

Every commit in the fork carries this footer in its commit message:

```
exp: wiki/experiments/<model>_autoresearch_optimization/<lane>/experiments/<YYYY-MM-DD>-v<NNN>-<slug>.md
```

This is the back-pointer that lets `git log --grep=exp:` enumerate every experiment-bound commit. Don't skip it.

### E. Don't add Python tests for the model edit

The training run is the test. The exception is when the change is graduating upstream as a stable feature (step 11, supported merge to trunk) AND the feature has a unit-testable invariant that protects against regression. Most experiment-fork edits never need a unit test.

### F. Match patch-file derivation rules

For layered Python-only patches (the common case): the file you `COPY` into the new docker image **MUST** be derived from the previous image's bundled version, not from current trunk. Trunk may have diverged (dataclass shape, tyro annotations, module paths). See program.md step 5 for the exact `docker run --rm <BASE_IMAGE> cat ...` workflow. Skipping this is a 10-second pre-compile failure that wastes cluster dispatch time.

## Self-check before declaring the edit done

Read these out loud (or to yourself, deliberately) before committing:

1. **Surgical?** Is every changed line traceable to the hypothesis? Any "while-I'm-here" cleanups? Revert them.
2. **One mechanism?** Does this edit test exactly one variable? If two changes are bundled, split or pick one.
3. **Semantics preserved?** Would this change the output distribution at fixed seed? If yes, you're in `invalid` territory unless this was pre-approved.
4. **No fallbacks?** Any `try/except` around kernel calls or new code paths? Remove unless there's a genuine recovery path (rare).
5. **Comments minimal?** Any WHAT comments or experiment-narrative comments? Strip them.
6. **Commit footer present?** `exp: wiki/experiments/...` line in the commit message?
7. **Fork-bounded?** Did you only touch files inside `<lane>/.repo/<exp-name>/<model-repo>/`? Nothing in trunk, nothing in other experiments' folders, nothing in the wiki?
8. **Patch-derivation correct?** If this is a layered Python-only patch, was the file extracted from the BASE_IMAGE (not trunk)?

If any check fails: revert that part of the edit, don't add to it.

## What this skill does NOT cover

- **Wiki page edits** — different discipline (clear, complete sentences, link liberally, dates absolute, etc.). The wiki is the durable narrative; code is throwaway.
- **Build / launch / poll** — gke-cluster-runner's job, not yours.
- **Verdict assignment** — master's job after gke-cluster-runner reports.
- **Trunk merges** — step 11 only, supported verdicts only, `git merge --no-ff` from fork. Different review bar.

## Failure modes

- **Edit grew mid-session**: stop, re-invoke this skill, re-evaluate against principle #2.
- **Hypothesis ambiguous**: don't pick silently. Document the assumption in the experiment page and pick the smaller-blast-radius option.
- **Tempted to add a fallback to "make it work"**: don't. Let the experiment refute cleanly.
- **Compiler error from a "small change"**: the change wasn't small. Revert, simplify, retry.

## See also

- Upstream skill: [karpathy-guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) (MIT)
- [`wiki/experiments/program.md`](../../wiki/experiments/program.md) — the procedural spec; step 4 ("Implement") is the invocation point
- [`.claude/skills/formulate-hypothesis/SKILL.md`](../formulate-hypothesis/SKILL.md) — the upstream skill that produced the hypothesis being implemented
- [`SCHEMA.md`](../../SCHEMA.md) — wiki structure and the experiment-narrative-vs-model-code separation
