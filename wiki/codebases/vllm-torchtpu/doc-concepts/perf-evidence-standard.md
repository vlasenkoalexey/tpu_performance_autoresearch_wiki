---
title: Performance evidence standard (traces, compiled artifacts, matched budgets)
type: doc-concept
provenance: doc
source: docs/developers_guide/optimization_best_practices.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Performance evidence standard (traces, compiled artifacts, matched budgets)

## Definition
The maintainers' rule set for what counts as proof of a performance change in
vllm-torchtpu (rules PR-1..PR-4 and P-1..P-4 of the optimization guide). In short:
**xprof traces are the unit of evidence**, compiler claims are proven from the compiled
artifact, tradeoffs are quantified on both axes, and parallelism comparisons are made at
a matched global token budget. End-to-end numbers alone prove nothing.

## The rules
| ID | Rule | Practical consequence |
|---|---|---|
| P-1 | A perf claim needs a trace plus a mechanism explanation; a "no-op on the hot path" claim needs a trace under realistic large-batch load | Padding / repeat overhead is invisible at small batch |
| P-2 | Prove compiler impact from HLO dumps / graph viewer | No guessing about layouts or fusions |
| P-3 | Scheduler changes report throughput **and** latency; extra rounding ops are measured for the quality/perf tradeoff | |
| P-4 | Parallelism A/Bs compare at matched **global** token budget (DP per-rank budget x N vs TP at the same total) | A win the mechanism does not predict is usually a batch-size artifact |
| PR-1 | Perf PRs are tiny, mechanism-described, carry per-mode speedups (decode / prefill / mixed), and update CI perf thresholds in the same PR | |
| PR-2 | Revert fast on numeric issues; root-cause offline | Mirrors the repo's revert-on-breakage policy for `main` |
| PR-3 | Ported code states source repo/file and what changed; kernels are versioned (v2, v3) and the superseded one deleted; a kernel with two homes is updated in both | |
| PR-4 | An honest Limitations section (unsupported shapes/configs, perf gaps, TODOs) | |
| Q-6 | Any weight-loading or model-level change compares server `total_hbm_used_gb` before/after, on the largest checkpoint that fits, across TP/EP/DP, including a non-128-divisible sharded last dim | Resident HBM growth directly shrinks the KV cache |

## In vllm-torchtpu (grounded)
- The tools these rules assume are in-tree: per-mode traces from the
  [phased profiler](phased-profiler.md) (prefill_only / decode_only / mixed phases map
  onto PR-1's decode / prefill / mixed speedups), merged per-rank sessions from the
  [multi-rank capture](multi-rank-trace-capture.md), and the
  [benchmark harness](benchmark-harness-and-regression-gates.md) whose checked-in
  baselines are the "CI perf thresholds" of PR-1.
- The HBM log line Q-6 refers to is emitted by
  [`TPUWorker.determine_available_memory`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.determine_available_memory)
  (`Memory statistics | total_hbm_limit_gb=... | total_hbm_used_gb=... |
  kv_connector_hbm_reserve_gb=... | total_hbm_avail_gb=...`), computed from
  [`compute_hbm_budget`](../catalog/src/vllm_torchtpu/utils.md#compute_hbm_budget) /
  [`HbmBudget`](../catalog/src/vllm_torchtpu/utils.md#HbmBudget) after the profile run,
  minus post-profile reserves (KV connector buffers, LoRA slot writes, PP hand-off).
  Whatever is left becomes KV cache, which is why resident-weight growth costs
  throughput.
- The same evidence rules are echoed in the coding guidance author checklist (item 4:
  xprof trace for hot-path claims, HLO diff for "no compiler impact", before/after HBM
  logs for weight-loading changes) and in R-8.9: perf measurement belongs in the
  benchmark harness, never as timing asserts in `tests/`.

## Why it matters / when it applies
These rules exist because inference regressions are usually silent - a padding path or a
`lax.cond` in a kernel loop costs a few percent everywhere without failing anything.
Anyone attributing a speedup in this codebase (including an automated optimization
loop) should expect to show: the trace with the mechanism visible, the HLO evidence for
fusion/layout claims, both throughput and latency, matched global batch for parallelism
changes, and the HBM delta for anything touching weights.

## Connections
- Code concepts: [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [tracing-annotations](../concepts/tracing-annotations.md)
- Module catalogs: [tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md),
  [utils](../catalog/src/vllm_torchtpu/utils.md)
- Related doc-concepts: [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [tuned-block-size-tables](tuned-block-size-tables.md),
  [weight-load-time-preprocessing](weight-load-time-preprocessing.md),
  [generic-quantization-machinery](generic-quantization-machinery.md),
  [phased-profiler](phased-profiler.md),
  [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md)

## Source
Extracted from `docs/developers_guide/optimization_best_practices.md` sections 0 and 1.1
(plus Q-6 of section 2), with the matching checklist items of
`docs/developers_guide/coding_guidance.md` (kept in place).
