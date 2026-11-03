---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce_v2.wrapper`/
symbols:
  ragged_gather_reduce_v2: ragged_gather_reduce_v2().
  main_kernel: main_kernel().
  _preprocess_scalar_data: _preprocess_scalar_data().
  _fallback_implementation: _fallback_implementation().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py)

## Functions
- <a id="_fallback_implementation"></a>`_fallback_implementation(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py#L29)
- <a id="_preprocess_scalar_data"></a>`_preprocess_scalar_data(indices: jax.Array, valid_rows_mask: jax.Array, cfg: config.Config)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py#L43) — Sorts valid source rows to the front of each row partition. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="main_kernel"></a>`main_kernel(scalar_ref: memory_ref.IndexRef, in_hbm_ref: jax.Ref, topk_weights_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, scratch_ref: memory_ref.ScratchRef, *, cfg: config.Config)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py#L91) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="ragged_gather_reduce_v2"></a>`ragged_gather_reduce_v2(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/wrapper.py#L135) — Gathers ``x`` by ``indices``, weights and masks, then reduces by group. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)

