---
name: lint
description: Run the LINT operation defined in SCHEMA.md across the wiki. Checks every invariant the schema declares — orphan pages, broken links, missing profile/HLO sections, missing hypothesis-firing audits, stuck `status: in_progress` stubs, missing stub labels (Hypothesis/Mechanism/Predicted signal/Falsification criterion), log routing violations (loop-iteration in global log; ingest in per-lane log), stale codebase commit pins, model-page variant-matrix drift, knobs-translation-matrix coverage gaps, model-optimization-index catalog rot, per-model refuted-patterns referencing non-existent v-IDs, experiment commits on the code-repo side missing `exp:` footer, and more. Fixes mechanical issues automatically; surfaces judgment calls as a punch list for the user. Invoke periodically (every few days during active iteration), from `/stop-experiment` at session end (already wired), or whenever the wiki shape changed substantially (post-rename, post-bulk-import, post-SCHEMA-update).
---

# /lint — run the SCHEMA LINT operation

Wraps SCHEMA's LINT operation as a standalone callable skill. Mostly mechanical; surfaces judgment calls for human review. Should be invoked periodically — drift accumulates silently otherwise.

## When to invoke

- **Periodic hygiene** — every few days during active iteration, or weekly during quieter periods.
- **At session end** — `/stop-experiment` Step 5 already runs LINT (this skill is the canonical implementation it points at).
- **Post-substantial wiki change** — after a rename, a bulk import, a SCHEMA update, or a topic-taxonomy revision. Things drift when shapes shift.
- **Pre-merge / CI** — could be wired into git pre-push or a CI workflow to catch issues before they land.
- **NOT during the autoresearch loop's normal cadence** — LINT is too noisy + expensive to run per-iteration.

## Cardinal rules

- **Auto-fix mechanical issues** (broken markdown links to renamed files, stale `updated:` dates inconsistent with last edit, etc.). Surface what was auto-fixed in the report.
- **Flag judgment calls** — anything that requires a human decision (contradiction adjudication, unresolved `[!warning]` blocks, semantic alignment between Current best and latest supported experiment) — surfaces these as a punch list with file:line references.
- **Don't auto-commit.** User reviews the auto-fix diffs + decides what to commit.
- **Don't fail on first issue.** Run ALL checks; produce a comprehensive report. A single broken link shouldn't hide 10 other issues.

## Step 1 — Run every check from SCHEMA's LINT section

Per SCHEMA.md's "Operations → LINT" section. The canonical list (extend if SCHEMA gains new checks):

### Cross-cutting wiki invariants

1. **Unresolved `[!warning]` contradictions** — grep `wiki/**.md` for `> [!warning]` blocks; report each with file:line + the contradicting claim.
2. **Orphan pages** — pages with zero inbound markdown links. Special case: `_`-prefixed dirs/files in `wiki/` are auto-generated; SKIP orphan check for them. Also SKIP the wikify-generated grounded catalogs under `wiki/codebases/<slug>/` (`catalog/`, `concepts/`, `doc-concepts/`, `overview.md`) — they are internally cross-linked and lint-gated by `wikify finalize`, not by this skill.
3. **Broken markdown links** — relative paths whose target `.md` doesn't exist.
4. **Concept/entity names mentioned in prose but not linked** — heuristic: substrings from known concept page titles that appear unlinked in prose. Surface as advisory; many false positives.

### Experiment-page invariants

5. **Experiments without profile artifacts in `raw/profiles/`** — frontmatter says verdict was assigned, but no profile dir exists. Exception: `backfilled: true`.
6. **Experiments missing `## Profile` or `## HLO Dump` section** — profile-analyzer wasn't dispatched or its output wasn't pasted. Exception: `backfilled: true`.
7. **Experiments missing the Phase 3 hypothesis-firing audit** in `## HLO Dump` (the silent-noop verification result line). Exception: `backfilled: true`.
8. **Stub-fill drift** — experiments with `verdict:` assigned (status: filed) whose `## Hypothesis under test` section is missing any of the four required labeled paragraphs (`**Hypothesis**`, `**Mechanism**`, `**Predicted signal**`, `**Falsification criterion**`). Exception: `backfilled: true`.
9. **Stuck stubs** — `status: in_progress` for > 24 hours. Either re-dispatch profile-analyzer to complete or mark `verdict: inconclusive`. `/stop-experiment` Step 4.5 resolves these proactively.
10. **Experiments missing `variant:` field** or whose `variant:` doesn't appear in the parent model page's Variant matrix.
11. **Experiment commit messages on the model-code-repo side missing the `exp: <wiki-path>` footer** (run `git log --grep=exp:` on the relevant branch; flag commits referenced by experiment pages but missing the footer).
12. **Experiment `.md` or other wiki artifact accidentally duplicated into the model code repo** — `grep -r "type: experiment" <code-repo>/` should return nothing.

### Model-page invariants

13. **Model pages where any variant row's `Current best` doesn't match the latest `supported` experiment** for that variant.
14. **Model pages where the Knobs translation matrix is missing entries** for techniques that have multiple supported experiments across different variants.
15. **Hypotheses with `variants:` listing rows that aren't in the parent model page's matrix.**
16. **Hypotheses `open` with no activity for > 14 days** on an actively-optimized model.

### Catalog-rot checks

17. **Per-model `refuted-patterns.md` referencing experiment v-IDs that don't exist** in `wiki/experiments/<model>_autoresearch_optimization/<lane>/`.
18. **`model-optimization-index.md` or `model-optimization-blueprint.md` referencing concept/observation/source pages that don't exist.**

### Hook-health invariants (the never-stop loop's control plane)

The autoresearch never-stop loop is governed *entirely* by a Stop hook; if it is unwired or shadowed by a rogue hook in another settings scope, the discipline fails **silently**. This check is not optional hygiene — it validates the loop's control plane.

23. **Hook health** — run `python3 .claude/scripts/check-hook-health.py`. It scans every settings scope (`~/.claude/settings*.json`, project `.claude/settings*.json`) and hard-fails (ERROR) if: the never-stop Stop hook (`.claude/stop_hook.sh`) isn't wired, its script is missing/non-executable, or any command hook references a script that doesn't exist. It WARNs on rogue global Stop hooks and hook commands that read non-durable `/tmp` paths (the two anti-patterns behind the 2026-06 `v6e32_stop_hook.json` staleness bug). Fold its ERRORS into the punch list; surface WARNINGS advisory. Do **not** auto-edit `~/.claude` settings — global scope affects every project, so flag global-scope findings for the user.

### Codebase invariants

19. **Stale codebase pages** whose `commit:` is far behind the current checkout (`git -C raw/code/<slug> rev-parse HEAD` vs frontmatter `commit:`).

### Log-routing invariants (per SCHEMA's two-tier convention)

20. **`loop-iteration` entries in global `wiki/log.md`** (post-migration cutoff). LINT fails if found.
21. **`ingest-*` / `lint` / `loop-pool` entries in any per-lane log.** LINT fails if found.
22. **Per-lane log file missing for an active lane** (any `<lane>/` dir with experiment pages but no `log.md`). Advisory, not hard fail.

## Step 2 — Auto-fix mechanical issues

The following are safe to auto-fix:

- **Broken markdown links to recently-renamed files** — if `git log --follow` traces the target to a known rename, auto-update the link.
- **Stale `updated:` fields** — if frontmatter `updated: 2026-04-15` but `git log -1 --format=%cd` for the file is `2026-05-22`, auto-bump.
- **Missing trailing `## See also` or `## Sources` section** — if the page-type template requires them and they're absent, add empty placeholders (with a "TODO" comment for the user to fill in).
- **Inconsistent counts in `wiki/index.md`** — if the index says `## Sources (79)` but `ls wiki/sources/ | wc -l` returns 81, auto-correct.

The following require human judgment — surface them, don't auto-fix:

- Contradiction adjudication
- Orphan page disposition (delete? add inbound link? consolidate?)
- Knobs matrix entries (cross-variant claim requires per-variant evidence)
- Stuck stub resolution (re-dispatch vs mark inconclusive — depends on cluster state)
- Concept-name-mentioned-but-not-linked (heuristic, many false positives)

## Step 3 — Generate report

```markdown
# LINT report — <YYYY-MM-DD HH:MM UTC>

**Scope**: <wiki/ paths checked>
**Pages scanned**: <N>
**Checks run**: 23 of 23

## Auto-fixed (N issues)

<list each with file:line + what was changed>

## Human review required (N issues)

### Cross-cutting (N)
- [page:line] <issue> — <suggestion>
- ...

### Experiment pages (N)
- ...

### Model pages (N)
- ...

### Catalog rot (N)
- ...

### Codebase (N)
- ...

### Log routing (N)
- ...

### Hook health (N)
- [scope] <ERROR/WARN from check-hook-health.py> — <fix>

## Summary

- Clean: <N> checks passed with no issues
- Auto-fixed: <N> mechanical issues resolved (review the diff)
- Punch list: <N> items need human review

Next steps:
- Review auto-fixes via `git diff` (changes staged, not committed)
- Walk the human-review punch list above; address per-issue
- Re-run `/lint` to confirm
```

## Step 4 — Append to global `wiki/log.md`

Per SCHEMA's log routing rules, `lint` op is GLOBAL only.

```markdown
## [YYYY-MM-DD] lint | LINT run — <N> findings

**Op**: lint
**Pages created**: (none)
**Pages updated**: <list of auto-fixed pages>, wiki/log.md
**Key result**: Scanned <N> pages across 22 checks. Auto-fixed <N>; punch list <N>.
**Notes**: <high-level summary of dominant issues; pointers to the report>
```

## Step 5 — Return to user

The report from Step 3. If running interactively, also offer to:
- Open the first punch-list item for resolution
- Drill into a specific check (e.g., "show all stuck stubs")
- Re-run after manual fixes

## Failure modes to handle

- **No wiki/ directory** — refuse with hint (probably running from wrong CWD).
- **SCHEMA.md missing or modified to remove the LINT operation** — surface as a meta-issue; still run all checks the skill knows about.
- **One check's data is unavailable** (e.g., `raw/code/<slug>/` not present for the codebase commit-staleness check) — skip THAT check, run the rest, note in report.
- **Massive number of findings** (>100) — group + summarize rather than list each. Suggest "run lint per-subdir to iterate" if the wiki is in a degraded state.

## Cost expectations

- **Per check**: most are sub-second to a few seconds (grep + ls patterns).
- **Total**: ~30 seconds to 2 minutes for a typical-sized wiki (200+ experiments + 100+ concepts + 50+ sources).
- **Tokens**: ~20-50K for the report depending on findings count.

## What this skill does NOT do

- **Does not auto-commit** auto-fixes. User reviews the diff.
- **Does not adjudicate contradictions.** Surfaces them.
- **Does not delete pages** (even orphans). Always flags for human decision.
- **Does not modify `raw/`.**
- **Does not modify SCHEMA.md.** If SCHEMA needs a new LINT check, that's a separate manual edit.
- **Does not enforce style consistency** (markdown formatting beyond what SCHEMA explicitly requires). Use a separate markdown linter for style.
- **Does not catch semantic content issues** (factual errors in claims, misinterpretation of profile data). LINT is structural / invariant-based.

## See also

- `SCHEMA.md` — the LINT operation contract this skill implements (canonical check list)
- `.claude/skills/stop-experiment/SKILL.md` Step 5 — wired to invoke this skill
- `.claude/skills/ingest-source/SKILL.md` — the index/log updates LINT verifies
