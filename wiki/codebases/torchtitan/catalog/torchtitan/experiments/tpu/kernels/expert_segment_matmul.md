---
title: 'Module: torchtitan/experiments/tpu/kernels/expert_segment_matmul.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/kernels/expert_segment_matmul.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.kernels.expert_segment_matmul`/
symbols:
  segment_matmul_pallas_2d: segment_matmul_pallas_2d().
  _grouped_mm_fwd: _grouped_mm_fwd().
  _grouped_mm_bwd: _grouped_mm_bwd().
  _tiling: _tiling().
  _backward: _backward().
  _setup_context: _setup_context().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/kernels/expert_segment_matmul.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py)

## Functions
- <a id="_backward"></a>`_backward(ctx, grad_output)` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L156)
- <a id="_grouped_mm_bwd"></a>`_grouped_mm_bwd(dout: jax.Array, lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, tile_m: int, tile_k: int, tile_n: int, tgmm_tile_m: int, tgmm_tile_k: int, tgmm_tile_n: int, transpose_rhs: bool)` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L72)
- <a id="_grouped_mm_fwd"></a>`_grouped_mm_fwd(lhs: jax.Array, rhs: jax.Array, group_sizes: jax.Array, tile_m: int, tile_k: int, tile_n: int, tgmm_tile_m: int, tgmm_tile_k: int, tgmm_tile_n: int, transpose_rhs: bool)` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L42)
- <a id="_setup_context"></a>`_setup_context(ctx, inputs, output)` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L149)
- <a id="_tiling"></a>`_tiling(tile_m: int, tile_k: int, tile_n: int, k_dim: int, n_dim: int)` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L26) — Resolve zero-valued K/N tiles to the corresponding full dimension.
- <a id="segment_matmul_pallas_2d"></a>`segment_matmul_pallas_2d(lhs: torch.Tensor, rhs: torch.Tensor, group_sizes: torch.Tensor, *, tile_m: int = 1024, tile_k: int = 0, tile_n: int = 0, tgmm_tiling: tuple[int, int, int] = (128, 128, 128), transpose_rhs: bool = False)` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L167) — Compute per-expert matmuls without moving group sizes to the host.

## Module values
- <a id="__all__"></a>`__all__` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/kernels/expert_segment_matmul.py#L200)

