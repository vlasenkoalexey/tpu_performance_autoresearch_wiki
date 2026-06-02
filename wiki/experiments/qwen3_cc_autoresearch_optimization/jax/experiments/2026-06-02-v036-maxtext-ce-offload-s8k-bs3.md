---
title: "Qwen3-8B jax v036 — maxtext-CE + named-offload remat @ seq8192 bs3"
type: experiment
hypothesis: qwen3-jax-seq8192-kernel-gap
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, cross-entropy, maxtext, custom-vjp, offload, scan, overlap, splash, remat, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v036 — maxtext-CE + named-offload remat @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: the v035 profile attributed ~85% of the residual MaxText gap (+454 ms) to `nothing_saveable`
recompute (loop-fusion/norms 17.4% vs MaxText 7.2%). Adding `--offload_remat`
(`save_and_offload_only_these_names`, offloads the `checkpoint_name`-tagged Q/K/V/O-proj + mlpwi
activations to pinned host instead of recomputing) — now that maxtext-CE removed the tokamax f32[H,V]
weight-gather that confounded [v030](2026-06-02-v030-scan-offload-ce-s8k-bs3.md) — cuts the backward
recompute and lifts the seq8192 frontier above v035 (6,030) toward MaxText (6,942).

**Mechanism**: image `qwen3-8b-jax:v033-maxtext-ce`. `--use_remat --use_splash --use_scan --use_maxtext_ce
--offload_remat --batch_size=3 --seqlen=8192` + 7 scheduler + 4 overlap flags. Only change vs v035 is
`--offload_remat`.

**Predicted signal**: fits (offload frees HBM from the 90.7% nothing_saveable peak); loss ~12.05 matching
v035; tok/s/chip > v035 6,030 toward 6,942.

**Falsification criterion**: ≤ v035 6,030 beyond noise — the host round-trip isn't repaid even without the
tokamax gather (the recompute cost is in the RMSNorms, which the proj/mlpwi-tagged offload doesn't cover →
would point to needing a norm-inclusive offload/save policy instead).

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
