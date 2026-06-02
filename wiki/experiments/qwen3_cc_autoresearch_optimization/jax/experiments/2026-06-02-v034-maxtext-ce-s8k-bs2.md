---
title: "Qwen3-8B jax v034 — MaxText custom_vjp CE @ seq8192 bs2 (the batch-wall test)"
type: experiment
hypothesis: qwen3-jax-maxtext-ce
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, cross-entropy, maxtext, custom-vjp, scan, overlap, splash, remat, seq8192, bs2, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v034 — MaxText custom_vjp CE @ seq8192 bs2

## Hypothesis under test

**Hypothesis**: the documented seq8192 batch wall (plain-CE bs1 5,632 > bs2 5,553 (v031) > bs3 4,595
(v030)) is partly the CE backward's transient peak. MaxText's `custom_vjp` CE computes the logit
gradient in a single fused pass (`softmax − onehot`) rather than autodiff through `log_softmax`,
lowering that transient. If the bs>1 regression was CE-backward-transient-bound, **bs2 with maxtext-CE
beats v028 bs1 (5,632)** — the wall cracks. If it's collective/attention-bound, bs2 ≤ v031's 5,553 —
the CE swap doesn't move the wall.

**Mechanism**: image `qwen3-8b-jax:v033-maxtext-ce`. Config = v031 shape (bs2, no offload) but with
maxtext-CE instead of tokamax-CE: `--use_remat --use_splash --use_scan --use_maxtext_ce --batch_size=2
--seqlen=8192` + 7 scheduler + 4 overlap flags.

**Predicted signal**: bs2 tok/s/chip vs v031 plain-CE bs2 (5,553) and v028 bs1 (5,632).

**Falsification criterion**: ≤ v031 5,553 beyond noise ⇒ maxtext-CE doesn't change the batch wall
(wall is not CE-backward-bound) ⇒ the documented hard wall stands; only a pipelined offload kernel
remains. > 5,632 ⇒ wall cracked, pursue bs3.

## Setup
(populated on completion — only dispatched after v033 bs1 parity confirms the CE swap is clean)
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
