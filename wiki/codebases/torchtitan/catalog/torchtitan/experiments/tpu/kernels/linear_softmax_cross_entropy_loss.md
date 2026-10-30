---
title: 'Module: torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.linear_softmax_cross_entropy_loss`/
symbols:
  _get_loss_op_names: _get_loss_op_names().
  linear_softmax_cross_entropy_loss: linear_softmax_cross_entropy_loss().
  _my_bwd: _my_bwd().
  _my_fwd: _my_fwd().
  _has_logit_transform: _has_logit_transform().
  _dummy_jaxtyped: _dummy_jaxtyped().
  _loss_op_name_cache: _loss_op_name_cache.
  TorchLinearLoss.forward: TorchLinearLoss#forward().
  TorchLinearLoss.backward: TorchLinearLoss#backward().
  _real_jaxtyped: _real_jaxtyped.
  _dummy_jaxtyped.decorator: _dummy_jaxtyped().decorator().
  _get_loss_op_names.fwd_wrapped: _get_loss_op_names().fwd_wrapped().
  _get_loss_op_names.bwd_wrapped: _get_loss_op_names().bwd_wrapped().
  TorchLinearLoss: TorchLinearLoss#
---
# Module: [`torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py)

## Classes
### <a id="TorchLinearLoss"></a>`TorchLinearLoss`
- def: [`torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py:282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L282) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- doc: Linear Softmax Cross-Entropy Loss autograd function.
- signature: `class TorchLinearLoss(torch.autograd.Function):`
- members:
  - <a id="TorchLinearLoss.backward"></a>`backward(ctx, grad_output)` — [`L324`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L324)
  - <a id="TorchLinearLoss.forward"></a>`forward(ctx, x, labels, weights, reduction="sum", implementation="mosaic_tpu", b_block_size=1024, h_block_size=512, v_block_size=2048, soft_cap=None, output_multiplier=1)` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L286)
- uses (calls/refs, reference-scoped): [`_get_loss_op_names`](linear_softmax_cross_entropy_loss.md#_get_loss_op_names)
- used by: [`linear_softmax_cross_entropy_loss`](linear_softmax_cross_entropy_loss.md#linear_softmax_cross_entropy_loss)

## Functions
- <a id="_dummy_jaxtyped"></a>`_dummy_jaxtyped(*args, **kwargs)` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L34)
- <a id="_get_loss_op_names"></a>`_get_loss_op_names(reduction, implementation, b_block_size, h_block_size, v_block_size, soft_cap=None, output_multiplier=1)` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L184)
- <a id="_has_logit_transform"></a>`_has_logit_transform(soft_cap, output_multiplier)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L52)
- <a id="_my_bwd"></a>`_my_bwd(dout, lse, x, labels, weights, reduction, implementation, b_block_size, h_block_size, v_block_size, soft_cap=None, output_multiplier=1)` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L108)
- <a id="_my_fwd"></a>`_my_fwd(x, labels, weights, reduction, implementation, b_block_size, h_block_size, v_block_size, soft_cap=None, output_multiplier=1)` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L56)
- <a id="_get_loss_op_names.bwd_wrapped"></a>`bwd_wrapped(dout, lse, x, labels, weights)` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L228)
- <a id="_dummy_jaxtyped.decorator"></a>`decorator(f)` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L35)
- <a id="_get_loss_op_names.fwd_wrapped"></a>`fwd_wrapped(x, labels, weights)` — [`L214`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L214)
- <a id="linear_softmax_cross_entropy_loss"></a>`linear_softmax_cross_entropy_loss(x: torch.Tensor, labels: torch.Tensor, weights: torch.Tensor, reduction: str = "sum", implementation: str = "mosaic_tpu", b_block_size: int = 1024, h_block_size: int = 512, v_block_size: int = 2048, soft_cap: float | None = None, output_multiplier: float = 1)` — [`L347`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L347) — Linear Softmax Cross-Entropy Loss. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)

## Module values
- <a id="_loss_op_name_cache"></a>`_loss_op_name_cache` — [`L180`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L180)
- <a id="_real_jaxtyped"></a>`_real_jaxtyped` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py#L30)

