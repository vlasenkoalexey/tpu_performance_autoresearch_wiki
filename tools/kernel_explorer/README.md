# kernel_explorer

Interactive hill-climbing viewer for the kernel lane: one static HTML page (Plotly) plotting every
kernel family's optimization trajectory — big points are experiments, small hollow points are the
K7 candidate-ledger attempts clustered around each `vNNN` tick, and the step line is the running
frontier. That step line is the hill climb: flat where a lever was refuted, jumping where the
frontier advanced.

Kernel-lane sibling of the model lane's `wiki/analyses/explorer_lib.py` (which lives in the public
`tpu_performance_autoresearch_wiki` repo, not here).

> **⚠ WARM-TIER / ANSWER-BEARING.** The page carries per-problem winning numbers and mechanism
> descriptions for the JAXBench families. Never paste it (or `kernel_data.json`) into an author
> brief; a cold `capability-eval` run must not retrieve it — the auditor's contamination class.

## Run

```bash
python3 tools/kernel_explorer/kernel_explorer.py
```

No arguments, no checkout needed, safe while a campaign is live: each arm's ledgers are read
straight out of its branch with `git archive` into a cache dir, so the working tree is never
touched. Works from `main` even though `main` doesn't track `wiki/kernel_experiments/**`.

Writes `kernel-explorer.html` + `kernel_data.json` next to the script (or `$KERNEL_EXPLORER_OUTDIR`).
Both are gitignored — regenerable output.

```bash
python3 -m http.server 8000 --directory tools/kernel_explorer
# ?kernel=gqa-attention&llm=all     compare all three LLMs on one kernel
# ?kernel=all&llm=opus5             one LLM's whole campaign
# ?kernel=gqa-attention&llm=opus5   detail view: verdicts + K7 candidates
```

## The controls

**Kernel** is a dropdown (one family, or all). **LLM** is one checkbox per arm, so any subset can
be shown — at least one stays checked. Each arm is an independent run of the same K0–K9 process by
a different model on its own campaign branch:

| Arm | Label | Branch |
|---|---|---|
| `opus5` | Claude Opus 5 | `pallas-kernel-optimization-opus5-process` |
| `codex` | Codex GPT-5.6 | `pallas-kernel-optimization-codex-process` |
| `gemini` | Gemini Flash 3.6 | `pallas-kernel-optimization-antigravity-process6` |

The combinations give four different views — one frontier per LLM (the comparison), one per family,
the single-kernel detail view with candidates, or every `(family, arm)` pair. Selection is mirrored
into the URL (`?kernel=…&llm=all` or `&llm=opus5,codex`), so any view is a shareable link, and the
checkbox labels are tinted to match each arm's series colour.

## Visual encoding — one rule, no exceptions

- **Colour = model.** Every mark belonging to an arm carries that arm's colour: experiment points,
  frontier lines, candidate marks. The checkbox labels are tinted to match. Colour never means
  anything else.
- **Shape = experiment verdict.** ● supported · ◆ partial · ✕ refuted · ✖ invalid · ■ inconclusive
  · □ pending/no-metric. Candidates are small and hollow: ○ ran, ✗ failed before timing.
- **Dash = family**, and only when several families share the plot (`kernel=all`). Families are
  separated by line pattern rather than colour precisely so the colour axis stays exclusively about
  the model.

Earlier versions coloured points by *verdict* in the single-kernel view and by series elsewhere,
while shape was verdict-coded throughout — so the same visual channel meant two different things
depending on the selection. That is fixed; the rule above now holds in every view.

A consequence worth knowing: arms have very different verdict mixes, so they legitimately look
different in shape. Gemini's arm is 98 `supported` (●) against Opus 5's 88 `refuted` (✕) — that is
a real difference in outcomes, not a styling artifact. Exactly one `partial` (◆) exists in the whole
dataset.

**Candidates** has its own checkbox (`show K7 candidates`) — it is the single biggest change to how
busy the plot looks, so it sits in its own group rather than buried among the **Show** toggles.
Unchecking it drops the whole candidate layer (the small hollow marks and their connecting step
lines), leaving one point per experiment. On the **TFLOP/s** metric the box is disabled with an
inline reason: the ledger records no per-candidate TFLOP/s, so the layer is unavailable there rather
than merely switched off — previously it silently did nothing on that view.

**Show** toggles the rest: refuted/invalid/inconclusive experiments, pending/no-metric rows, the
roofline, and the MK⁵ line.

## MaxKernel reference line (MK⁵)

The **MaxKernel best (MK⁵)** checkbox draws MaxKernel's published best-of-5 speedup as a horizontal
reference — the external bar each family is being measured against. Speedup-only: it has no meaning
on the p50-ms or TFLOP/s axes, so it is drawn on the speedup view only.

Values live in `MK_BEST`, transcribed from the MK⁵ column of
`wiki/analyses/2026-07-17-combined-kernel-scoreboard.md` (24 problems, `1p`–`49k`).

**Six MK cells are flagged as artifacts** — device-framing or physically impossible — and are drawn
magenta dash-dot with an explicit "flagged artifact — not a real bar" label rather than being
silently dropped, because "MK claims 26.86× and it isn't real" is itself the useful fact:

| Problem | Family | MK⁵ | Why flagged |
|---|---|---|---|
| 7p | ragged-paged-attention | 4.44 | scoreboard ✗ |
| 9p | swiglu-mlp | *Fail* | MK failed outright |
| 12p | rms-norm | 1.63 | invalidated; the real bar is 1.39 |
| 21k | gemm-divide-sum-scaling | 15.11 | scoreboard ✗ |
| 26k | bmm-instancenorm-sum-residualadd-multiply | 10.10 | scoreboard ✗ |
| 30k | matmul-scaling-residualadd | 26.86 | scoreboard ✗ |

An artifact value never rescales the y-axis for the real data — 30k's 26.86× against data at 0.23×
would flatten the chart into a single line at the bottom. When an artifact line falls off-scale it
becomes a small magenta note in the top-left corner instead.

Override the arms without editing the file:

```bash
KERNEL_EXPLORER_ARMS='opus5|Claude Opus 5|some-branch,codex|Codex|other-branch' \
  python3 tools/kernel_explorer/kernel_explorer.py
```

Labels come from what each branch's own artifacts say the model was, not from the branch name —
the codex branch's pages say **gpt-5.6-sol**, so it is labelled GPT-5.6, not 5.5.

## Links point at the arm's branch

Clicking a point opens the experiment page at
`github.com/<owner>/<repo>/blob/<that arm's branch>/wiki/kernel_experiments/…`. This matters:
none of these ledgers are on `main`, so a `blob/main` URL 404s, and each arm's pages only exist
on its own branch. `origin/<branch>` is preferred when it resolves, since that is what a blob URL
can actually reach. Where an arm used a non-canonical family slug the link keeps the real
directory name while the chart groups under the canonical slug (see `FAMILY_ALIAS`).

Plotly loads from `cdn.plot.ly`, so viewing needs network. That also means the page **cannot be
published as a claude.ai Artifact as-is** — the Artifact CSP blocks external hosts; Plotly would
have to be inlined first.

## Data source

`wiki/kernel_experiments/<family>/pallas/` — `RESULTS.tsv` is the primary ledger (per-family
schemas differ; parsing is header-driven and normalized), experiment pages supply verdicts/titles,
contribute pending/no-metric rows for `vNNN` pages the TSV hasn't caught up with, and carry the
candidate ledgers. Selection is by `?kernel=<slug>` or the dropdown, kept in the URL via
`history.replaceState` so views are shareable links.

## Comparing arms fairly

The arms are **not** like-for-like and the page does not pretend otherwise:

- **Different problem sets.** Only 6 families are shared by all three arms (`flash-attn-mha`,
  `gqa-attention`, `mla-attention`, `paged-attention`, `ragged-paged-attention`,
  `sparse-attention`). Gemini's branch carries 18 families neither other arm attempted. A
  cross-arm claim outside the shared 6 is comparing different work.
- **Different depth per family.** Frontier height tracks how many experiments an arm spent —
  e.g. Gemini's `retnet-retention` has 62 experiments, its `ragged-dot` has 1. Read the experiment
  count alongside the frontier.
- **COLD vs PRIMED.** Results filed after the 2026-07-27 K2 class-lever rule are class-page-primed,
  not cold, so they are not interchangeable with cold-arm numbers. See the COLD/PRIMED banner on
  `wiki/analyses/2026-07-17-combined-kernel-scoreboard.md`.
- **Verdict ≠ frontier.** Per BRIEFS §3 the frontier follows the best verified parity-passing
  candidate regardless of verdict, so a `refuted` experiment can still hold the frontier.

## Two cautions when reading it

- **Roofline is not a metric.** The dotted ceiling line is *implied* — `max(tflops/util)` over
  receipts — not a measured bound.
- **Some util figures are impossible and the ceiling inherits the error.** The current data has
  `megablox-gmm` at 1393% util, `mamba2-ssd` at 148%, `paged-attention` at 104.7%. Any util above
  100% means the util column was computed against the wrong denominator, and it drags that family's
  implied ceiling with it (megablox reads `ceil 0.16x`, i.e. below 1.0, which is nonsense). Treat
  those three families' ceiling lines as void until the util basis is fixed upstream in the ledgers.

## Provenance

Promoted from `wiki/analyses/kernel_explorer_lib.py` on the kernel campaign branch. Renamed: the
`_lib` suffix was a misnomer — it is an executable generator, not a library. The only code changes
were `KERNEL_EXPLORER_REPO` / `KERNEL_EXPLORER_OUTDIR` env overrides, needed because `main` does not
carry the ledgers, plus the corrected `view:` hint.

## See also

`tools/kernel_charts/` — static matplotlib bars for cross-*arm* comparison at a point in time
(which agent won which family). Different question: this tool shows the climb within one arm over
time; that one shows the final standings across arms.
