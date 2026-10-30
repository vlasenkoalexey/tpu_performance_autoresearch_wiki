---
title: 'Module: torchtitan/experiments/tpu/kernels/gmm.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/gmm.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.gmm`/
symbols:
  _get_gmm_kernels: _get_gmm_kernels().
  grouped_matrix_multiply: grouped_matrix_multiply().
  _gmm_fwd_cache: _gmm_fwd_cache.
  TorchGMM.forward: TorchGMM#forward().
  TorchGMM.backward: TorchGMM#backward().
  _gmm_bwd_cache: _gmm_bwd_cache.
  _get_gmm_kernels.fwd_fn: _get_gmm_kernels().fwd_fn().
  _get_gmm_kernels.bwd_fn: _get_gmm_kernels().bwd_fn().
  TorchGMM: TorchGMM#
---
# Module: [`torchtitan/experiments/tpu/kernels/gmm.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py)

## Classes
### <a id="TorchGMM"></a>`TorchGMM`
- def: [`torchtitan/experiments/tpu/kernels/gmm.py:75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L75) — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)
- doc: Custom PyTorch autograd function for Grouped Matrix Multiply.
- signature: `class TorchGMM(torch.autograd.Function):`
- members:
  - <a id="TorchGMM.backward"></a>`backward(ctx, grad_output)` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L88)
  - <a id="TorchGMM.forward"></a>`forward(ctx, lhs, rhs, group_sizes_tpu)` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L79)
- uses (calls/refs, reference-scoped): [`_get_gmm_kernels`](gmm.md#_get_gmm_kernels)
- used by: [`grouped_matrix_multiply`](gmm.md#grouped_matrix_multiply)

## Functions
- <a id="_get_gmm_kernels"></a>`_get_gmm_kernels(group_sizes_tpu: Tuple[int, ...])` — [`L16`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L16) — Creates and caches the TorchTPU bridging kernels for Grouped Matrix Multiply.
- <a id="_get_gmm_kernels.bwd_fn"></a>`bwd_fn(dout_j, lhs_j, rhs_j)` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L45)
- <a id="_get_gmm_kernels.fwd_fn"></a>`fwd_fn(lhs_j, rhs_j)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L38)
- <a id="grouped_matrix_multiply"></a>`grouped_matrix_multiply(lhs: torch.Tensor, rhs: torch.Tensor, offs: torch.Tensor)` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L98) — Executes Grouped Matrix Multiply on TPU. — documented in [tpu-pallas-kernels](../../../../../concepts/tpu-pallas-kernels.md)

## Module values
- <a id="_gmm_bwd_cache"></a>`_gmm_bwd_cache` — [`L13`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L13)
- <a id="_gmm_fwd_cache"></a>`_gmm_fwd_cache` — [`L12`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/gmm.py#L12)

