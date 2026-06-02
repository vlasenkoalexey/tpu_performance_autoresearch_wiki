---
title: "Qwen3-8B jax v033 — MaxText custom_vjp CE @ seq8192 bs1 (parity anchor)"
type: experiment
hypothesis: qwen3-jax-maxtext-ce
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, cross-entropy, maxtext, custom-vjp, scan, overlap, splash, remat, seq8192, bs1, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v033 — MaxText custom_vjp CE @ seq8192 bs1

## Hypothesis under test

**Hypothesis**: swapping our `_ce` (autodiff through `jax.nn.log_softmax`) for MaxText's verbatim T5X
`@jax.custom_vjp cross_entropy_with_logits` (one-hot targets, z_loss=0) is **numerically identical**
(CPU check: |Δloss|=0, |Δgrad|=0) and **does not regress** bs1 seq8192 vs the v028 frontier
(32.3% / 5,632 tok/s/chip). This is the parity anchor before the bs2 wall-test (v034).

**Mechanism**: image `qwen3-8b-jax:v033-maxtext-ce` (FROM v030-scan-full, swaps `train.py` only —
adds the module-level custom_vjp + `--use_maxtext_ce` flag; diff vs v030 is ONLY the CE additions,
verified). Config = v028 frontier + `--use_maxtext_ce=True` (NO tokamax CE, NO offload):
`--use_remat --use_splash --use_scan --use_maxtext_ce --batch_size=1 --seqlen=8192` + 7 scheduler + 4
async-collective-fusion overlap flags.

**Predicted signal**: ≈ v028 5,632 (within noise); loss ~12.07 stable matching v028; exit 0.

**Falsification criterion**: < 5,632 beyond noise ⇒ the custom_vjp graph compiles worse at bs1
(unexpected given identical math) ⇒ reconsider before the bs2 test.

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
