# demo — autoresearch playback tool (for demo / marketing video)

A tool that **replays a completed optimization series as a fast, scripted walkthrough**, so
it can be screen-recorded for a demo/marketing video without waiting for a real optimization
run (which takes hours/days).

The live product does: *ingest → hypothesize → run on TPU → profile → update priors → next
hypothesis*. In a video we want to show that loop **as it already happened**, compressed into
a couple of minutes of screen time.

> Status: **built.** Player + diff-precompute implemented; all four qwen3 jax series precomputed.
> See [Usage](#usage).

---

## Where this sits in the video

The full video is montaged from several parts:

1. *(recorded live, not this tool)* Start the agent, discover the GKE cluster, kick off an
   optimization. This is the "getting started" segment.
2. **This tool** — the payoff segment. Instead of watching a real multi-hour run, we play back
   an *already-completed* experiment series and narrate the loop: idea → change → result,
   experiment by experiment, with the MFU frontier climbing on screen.

---

## What the user selects

The user names **one experiment series** to demonstrate. A series is the tuple:

| Axis | Values (current) | Notes |
|------|------------------|-------|
| model / architecture | `qwen3` (also `gemma4`, `llama3`) | the `<architecture>` prefix |
| **agent type** | `cc` (Claude) · `ag` (Antigravity) · `cx` (Codex) · `cc5` (Fable5) | drives the **color scheme** |
| execution lane | `jax` · `torchax` · `maxtext` | the framework/code path |
| context length | `2k` (2048) · `8k` (8192) | filters the points shown |

This resolves to an experiments directory, e.g.:

```
wiki/experiments/qwen3_<agent>_autoresearch_optimization/<lane>/experiments/*.md
```

and the matching model page `wiki/models/qwen3-<agent>-<lane>.md`.

> **Terminology caution.** In this wiki "lane" is overloaded. The color-carrying axis the user cares
> about here is the **agent type** (`cc`/`ag`/`cx`/`cc5`), *not* the execution lane (`jax`/…). The
> explorer's `COLORS` map is keyed by agent type: `cc=#1f77b4, ag=#ff7f0e, cx=#2ca02c, cc5=#d62728`
> (see `wiki/analyses/qwen3/build_explorer.py`).

---

## What the tool does

1. **Collect** every experiment record for the selected series, in run order (sorted by the `vNNN`
   in the filename, same key `build_explorer.py` uses). Filter to the chosen context length.
2. **Step through** them one experiment at a time. For each experiment, present three screens in order:

   **(a) Hypothesis screen — "the idea it came up with"**
   - Render the linked hypothesis page (`wiki/hypotheses/<slug>.md`, from the experiment's
     `hypothesis:` frontmatter): the falsifiable Statement + Rationale.

   **(b) Diff screen — "the change it applied"**
   - Show what changed for this experiment vs. the previous one — either a **code diff** (model /
     trainer / sharding) or a **flag/command diff** for flag-only runs. Source is a per-experiment
     snapshot, see [Diff source](#diff-source-resolved) below.

   **(c) Result screen — "what it got"**
   - Show the MFU explorer (`wiki/analyses/qwen3/mfu-explorer.html` style chart) **filtered to only
     the experiments demonstrated up to and including this one**, so the frontier visibly grows.
   - Overlay a **large label `Best MFU: XX.X%`** (the running-best over the shown points) in the
     selected agent type's color.

3. **Advance** to the next experiment and repeat, so the recording shows the frontier climbing:
   idea → change → result → idea → change → result …

---

## Visual / output requirements

- **Browser-rendered self-contained HTML player** (this is what gets screen-recorded), reusing the
  existing Plotly explorer look so the demo matches the real product UI. Single file, no external
  CDN (offline/CSP-safe).
- **Color scheme = agent type color** throughout (frontier line, Best-MFU label, accents).
- **Filtered frontier**: at experiment *k*, only points `1..k` of the series are plotted; the
  running-best line and the `Best MFU` number reflect only those.
- **Playback control (decided):**
  - **Auto-advance** through the screens at a configurable speed. Speed is a build arg
    (e.g. `--speed 1.0`, seconds-per-screen or a multiplier — to finalize) **and** adjustable at
    play time.
  - **Manual navigation with `<` and `>` keys** — step back / forward one screen. Space toggles
    play/pause. Auto-advance and manual nav coexist.
  - Deterministic, no dependence on wall-clock/random (safe for clean re-recording).
- Reuse `mfu_data.json` (already emitted by `build_explorer.py`) as the data source rather than
  re-parsing experiment markdown, where possible.

---

## Inputs & data sources (grounded)

| Need | Source |
|------|--------|
| ordered experiment list + metrics + verdicts | `wiki/analyses/qwen3/mfu_data.json` (per record: `lane`=agent, `slug`, `order`, `seq`, `mfu`, `tps`, `verdict`, `success`, `link`) |
| hypothesis text | experiment frontmatter `hypothesis:` → `wiki/hypotheses/<slug>.md` |
| model / flag diff | precomputed per-experiment unified diffs + manifest under `diffs/<series>/` (see [Diffs](#diffs-precomputed)) |
| colors / labels | `COLORS` + `LANE_NAME` in `build_explorer.py` |
| chart rendering | pattern from `mfu-explorer.html` / `explorer_lib.py` |

---

## Usage

Two steps: **precompute the diffs once** (git archaeology — slow), then **build the player** (fast,
re-run freely to re-pace / re-theme).

```bash
# 1. Precompute per-experiment diffs + manifest into diffs/<series>/  (already done for all 4 series)
python tools/demo/precompute_diffs_cc.py                 # qwen3-cc-jax (has real code diffs)
python tools/demo/precompute_diffs_series.py ag          # qwen3-ag-jax  (flag diffs)
python tools/demo/precompute_diffs_series.py cx          # qwen3-cx-jax
python tools/demo/precompute_diffs_series.py cc5         # qwen3-cc5-jax

# 2. Build the self-contained player
python tools/demo/build_demo.py --series qwen3-ag-jax --seq 2048 --speed 3.2
#   --series  qwen3-<cc|ag|cx|cc5>-jax
#   --seq     2048 | 8192 | all        (context length; default 2048)
#   --speed   seconds per slide         (also editable live in the footer)
#   --include metric | all              (all experiments, or only metric-bearing)
#   --out     tools/demo/demo.html

# 3. View — serve the dir and open demo.html
python -m http.server 8799 --bind 127.0.0.1 --directory tools/demo
#   → http://localhost:8799/demo.html
```

Player controls: auto-advances at `--speed`; `<` / `>` step, **Space** pause, **T** theme
(light/dark), **H** hide/show the bottom control bar. The footer has a live **seconds-per-slide**
input.

## Diffs (precomputed)

Per-experiment unified diffs live in `diffs/<series>/<slug>.diff` with a `manifest.json` index; the
player inlines them at build time (no git access at play time). Git history on `main` is
batch-committed (one commit spans many `vNNN`, e.g. `v035→v045`), so a clean per-experiment code diff
usually can't be extracted — hence precompute, with this fallback hierarchy per experiment:

1. **code** — a real `git show` diff of the model dir, when a commit's named lever maps to the
   experiment that introduces it (e.g. cc: v004 gradient-remat, v028 scan-over-layers, v041 activation
   sharding). Batched commits attribute to the first experiment that introduces the lever.
2. **flag** — a synthesized `run.sh` unified diff of the launch flags vs. the previous experiment,
   read verbatim from the page's `## Setup` (no flag names invented; unmapped lane-specific
   descriptors render as truthful `# lever:` comment lines).
3. **none** — baselines / no documented change (rendered as a single "starting point" screen).

`diffs/` is **gitignored** (private, regenerable — carries launch flags / model code). Regenerate any
time with the precompute scripts. The player build **falls back** to a diff-less manifest synthesized
from `mfu_data.json` + the markdown pages if `diffs/<series>/` is absent, so it stays previewable.

Coverage note: `cc` and `ag` are the clean series; `cx`/`cc5` document config sparsely, so their flag
diffs are noisier (some `# lever:` comment lines, arc-boundary boolean resets).

## Configurable behaviour

- **Context length** (`--seq`) and **inclusion policy** (`--include`) are build flags. Default:
  metric-bearing experiments only on the chart; every experiment gets hypothesis/diff screens except
  baselines (no idea/change → chart-only "starting point").
- **Speed** is a build default and a live footer control.
- **Theme** is light/dark, follows OS preference, toggled live.
- **Agent icon** (top-left): drop a real logo SVG at `assets/<agent>.svg` (`cc`/`ag`/`cx`/`cc5`) and
  it is inlined; otherwise a clean accent-colored monogram badge is used.

---

## Non-goals

- Not a real optimizer — it never launches TPU work; pure replay of recorded results.
- Does not modify any wiki page, `raw/`, or experiment records.
- Not tied to the autoresearch loop's `program.md`; this is presentation tooling only.

---

## Layout

```
tools/demo/
  README.md                     ← this file
  build_demo.py                 ← builds the self-contained player from a series' manifest
  player.html.template          ← the player (HTML/CSS/JS); __PAYLOAD__ is injected at build
  precompute_diffs_cc.py        ← diff precompute for qwen3-cc-jax (real code diffs + flag diffs)
  precompute_diffs_series.py    ← diff precompute for the flag-only lanes (ag / cx / cc5)
  assets/<agent>.svg            ← optional real logo per agent (else monogram fallback)
  diffs/<series>/               ← precomputed <slug>.diff + manifest.json   (gitignored, private)
  demo.html                     ← generated player output
```
