---
title: "Qwen3-8B jax v041 — activation sharding constraints @ seq8192 bs3"
type: experiment
hypothesis: qwen3-jax-activation-sharding-constraints
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-shard-acts-2026-06-03
status: in_progress
tags: [qwen3-cc, jax, sharding, activation-sharding, with-logical-constraint, maxtext, scan, splash, seq8192, bs3, v6e-8]
created: 2026-06-03
updated: 2026-06-03
---

# Qwen3-8B jax v041 — activation sharding constraints @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: the obvious code gap vs MaxText — we apply **no** activation sharding constraints; MaxText pins
every layer-boundary activation. Adding `--shard_acts` (pin activations to `P("fsdp", ...)` at the layer input,
both post-norms, attention output, and MLP intermediate, mirroring MaxText's `with_logical_constraint`) cuts the
spurious layout conversions (our loop-fusion 17.4% vs MaxText 7.2%, data-formatting 3.8% vs 1.8%) and lifts the
frontier above v035 (6,030).

**Mechanism**: image `qwen3-8b-jax:v041-shard-acts` (FROM v033-maxtext-ce, swaps modeling_qwen3.py + __init__ +
train.py: flag-gated `_sac()` applying `jax.lax.with_sharding_constraint`). v035 config + `--shard_acts`:
`--use_remat --use_splash --use_scan --use_maxtext_ce --shard_acts --batch_size=3 --seqlen=8192` + base 12-flag
bundle. NO offload (isolate the constraint variable vs v035). equivalence PASS; shard_acts path validated on the
Auto-axis mesh.

**Predicted signal**: tok/s/chip > v035 6,030 (loop-fusion + data-formatting buckets drop toward MaxText); loss
parity (with_sharding_constraint = identity on values); exit 0.

**Falsification criterion**: ≤ 6,030 beyond noise — in pure FSDP XLA already infers the batch-sharded layout, so
the constraints are no-ops (then the inflated buckets are intrinsic recompute, not layout conversion).

## Setup
(populated on completion)
## Results
(populated on completion)
## Profile
(populated on completion)
## HLO Dump
(populated on completion)
## Verdict
(populated on completion)

## Next hypotheses
(populated on completion)
