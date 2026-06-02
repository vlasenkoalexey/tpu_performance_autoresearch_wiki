---
title: "Qwen3-8B jax v039 — MaxText exact offload recipe @ seq8192 bs3"
type: experiment
hypothesis: qwen3-jax-maxtext-offload-recipe
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-offload-recipe-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, remat, offload, host-offload, maxtext, scan, splash, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v039 — MaxText exact offload recipe @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: v036's offload regressed because it offloaded the WRONG tensors (the giant mlpwi, missing
decoder_layer_input). Replicating MaxText's exact recipe — offload `decoder_layer_input + q/k/v/o proj`,
**recompute** mlpwi — plus the MaxText offload-pipelining XLA flags (validated by v038), lifts the seq8192
frontier above v035 (6,030) toward MaxText (6,942).

**Mechanism**: image `qwen3-8b-jax:v039-offload-recipe` (FROM v033-maxtext-ce, `modeling_qwen3.py` swap:
decoder_layer_input `checkpoint_name` tag + offload-names = {decoder_layer_input, query_proj, key_proj,
value_proj, out_proj}, mlpwi dropped). `--use_remat --use_splash --use_scan --use_maxtext_ce --offload_remat
--batch_size=3 --seqlen=8192` + the validated MaxText flag superset (from v038). Equivalence PASS
(checkpoint_name = identity).

**Predicted signal**: fits; loss ~12.05 matching v035; tok/s/chip > v035 6,030 toward 6,942 (offload of the
attention path + recompute of the cheap-recompute MLP, with the host copy overlapped across scan via the
`*_in_chain` flags).

**Falsification criterion**: ≤ v035 6,030 — even MaxText's exact recipe doesn't pipeline on our libtpu/scan
build → the host-offload path genuinely differs at the runtime level (then the gap really is a build/kernel
wall). OOM → the offload-set change shifted the HBM balance unexpectedly.

## Setup
(populated on completion — dispatched after v038 reports the valid flag subset)
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
