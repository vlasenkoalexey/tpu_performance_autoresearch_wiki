---
title: "Qwen3-jax: close the residual seq8192 gap to MaxText (kernel/scheduling)"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: refuted
expected_gain: "named-offload sub-lever refuted (v036 −18.6%); MXU/logical-axis sub-lever (~+3-4%) deferred"
confidence: medium
effort: S
origin: 2026-06-02-v035-maxtext-ce-s8k-bs3
hlo_prefilter: n/a
tags: [qwen3-cc, jax, seq8192, mfu-gap, splash, reduce-scatter, mxu, profile-driven]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-jax: close the residual seq8192 gap to MaxText

## Statement

The residual ~13% gap from the seq8192 frontier (v035, 34.6% / 6,030) to MaxText bs3 (45.3% / 6,942) is
dominated (~85%, +454 ms) by **remat policy**: our `nothing_saveable` recomputes every activation, making
loop-fusion (RMSNorm) 17.4% of the step vs MaxText's 7.2%. Switching to **named-offload**
(`--offload_remat` = `save_and_offload_only_these_names`, already implemented) — now that maxtext-CE has
removed the tokamax f32[H,V] weight-gather that confounded it in v030 — cuts the recompute and lifts the
seq8192 frontier toward MaxText.

## Rationale

The [v035 profile-analyzer attribution](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v035-maxtext-ce-s8k-bs3.md)
is decisive: per-layer norm time 19.7 ms (ours, recomputed) vs 7.1 ms (MaxText) — 2.78×. MaxText keeps the
backward cheap via named host-offload of Q/K/V/proj activations rather than recompute. We have the exact
mechanism (`--offload_remat`, validated equivalence-passing in v025–v027); it regressed in
[v030](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v030-scan-offload-ce-s8k-bs3.md)
ONLY because the tokamax-CE f32[H,V] weight all-gather (4.64G) dominated. With maxtext-CE (no gather), the
offload's host round-trip should be repaid by the recompute it saves. HBM at bs3 is 90.7% with
nothing_saveable; offload moves activations to pinned host, freeing HBM and skipping recompute.

Secondary lever (not this hypothesis): MXU occupancy 53.6% vs 61.2% (+156 ms) via logical-axis-rules tile
alignment — harder sharding work, deferred. Reduce-scatter is already better than MaxText (do not pursue).

## Proposed experiment

- [v036](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v036-maxtext-ce-offload-s8k-bs3.md):
  maxtext-CE + `--offload_remat` + bs3 seq8192 vs v035 (6,030). **RESULT: REFUTED** — v036 = 4,908 (−18.6%).
  Two reasons: (1) the offload tags proj/mlpwi outputs, not the norm outputs that the profile flagged as the
  recompute cost; (2) our pinned_host offload is **not pipelined** — the host round-trip lands on the critical
  path (+22% step), opposite of MaxText's <0.1% overlapped copy. Named-offload as-implemented cannot close the gap.

## Status / remaining sub-lever

The named-offload mechanism is **refuted**. The v035 profile's **secondary** lever — MXU occupancy 53.6% vs
MaxText 61.2% (+156 ms, ~+3-4%), via `logical_axis_rules` tile alignment — remains untested. It is a
sharding-layout rewrite (medium-high effort, uncertain payoff) and is **deferred/catalogued**, not the CE
directive's scope. Closing the rest would need a *pipelined* host offload (XLA/kernel-authoring, out of scope).

## See also

- [Qwen3 8B — jax](../models/qwen3-cc-jax.md) · [MaxText gap teardown](../analyses/2026-06-02-maxtext-vs-jax-qwen3-8b-mfu-gap.md) · [v035](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v035-maxtext-ce-s8k-bs3.md)
