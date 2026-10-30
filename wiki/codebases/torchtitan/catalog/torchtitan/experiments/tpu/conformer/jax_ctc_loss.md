---
title: 'Module: torchtitan/experiments/tpu/conformer/jax_ctc_loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/conformer/jax_ctc_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.conformer.jax_ctc_loss`/
symbols:
  e: e.
  ctc_loss_fwd: ctc_loss_fwd.
  ctc_loss_backward_jax: ctc_loss_backward_jax().
  ctc_loss_bwd: ctc_loss_bwd.
  ctc_loss_backward_jax.surrogate: ctc_loss_backward_jax().surrogate().
  backward: backward().
  jax_ctc_loss: jax_ctc_loss().
  ctc_loss_forward_jax: ctc_loss_forward_jax().
  setup_context: setup_context().
---
# Module: [`torchtitan/experiments/tpu/conformer/jax_ctc_loss.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py)

## Functions
- <a id="backward"></a>`backward(ctx, d_loss)` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L83)
- <a id="ctc_loss_backward_jax"></a>`ctc_loss_backward_jax(logits: jax.Array, labels: jax.Array, d_loss: jax.Array)` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L43) — Computes CTC loss gradient w.r.t logits using JAX autodiff.
- <a id="ctc_loss_forward_jax"></a>`ctc_loss_forward_jax(logits: jax.Array, labels: jax.Array)` — [`L11`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L11) — Computes CTC loss using optax.
- <a id="jax_ctc_loss"></a>`jax_ctc_loss(logits: torch.Tensor, labels: torch.Tensor)` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L99) — PyTorch entry point for JAX CTC loss.
- <a id="setup_context"></a>`setup_context(ctx, inputs, output)` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L78)
- <a id="ctc_loss_backward_jax.surrogate"></a>`surrogate(logits_local)` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L57)

## Module values
- <a id="ctc_loss_bwd"></a>`ctc_loss_bwd` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L72)
- <a id="ctc_loss_fwd"></a>`ctc_loss_fwd` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L68)
- <a id="e"></a>`e` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/jax_ctc_loss.py#L92)

