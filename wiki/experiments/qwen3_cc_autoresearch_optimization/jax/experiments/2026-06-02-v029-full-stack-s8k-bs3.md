---
title: "Qwen3-8B jax v029 — full stack (scan+offload+CE-bf16+overlap) @ seq8192 bs3"
type: experiment
hypothesis: qwen3-jax-host-offload-bs3-seq8192
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-fullstack-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, scan, offload, tokamax-ce, overlap, splash, remat, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v029 — full MaxText-equivalent stack @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: The full stack — scan (v028, makes overlap productive) + named-offload (frees activation
HBM) + tokamax-CE with **bf16 lm_head weight** (clears the v027 f32-weight 4.64G wall; matches plain-CE
precision) + the overlap flags — fits **bs3** at seq8192 AND amortizes the batch (now that collectives
overlap, unlike v016's sync-collective bs2<bs1), approaching the MaxText ceiling (45.3% / 6,942 tok/s/chip).

**Mechanism**: image `qwen3-8b-jax:v029-full`. `--use_remat --use_splash --use_scan --offload_remat
--use_tokamax_ce --tokamax_ce_impl=mosaic_tpu --batch_size=3 --seqlen=8192` + 7 scheduler + 4 overlap flags.
CE-weight fix: mosaic_tpu now gets the lm_head weight in bf16 (tiles V, accumulates lse in f32 internally)
→ no full f32[H,V] materialization. Scan validated (v028); CE-weight-bf16 validated on TPU by the loss
trajectory here (must be ~12.07 stable / no NaN — else the bf16 CE is wrong → invalid).

**Predicted signal**: bs3 **fits** (CE-bf16 saves ~2.49G + offload frees activations; v027 was +2.34G over);
loss ~12.07 stable; MFU/tok-s-chip > v028 5,632 (bs3 amortizes with overlap), toward 6,942.

**Falsification criterion**: OOM at bs3 (still over budget → attack next temp); loss NaN/divergence
(bf16-CE numerically wrong → invalid, revert CE-weight change); or MFU ≤ v028 5,632 (bs3 doesn't amortize
even with scan+overlap → batch genuinely doesn't help our stack; v028 bs1 is the seq8192 frontier).

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
