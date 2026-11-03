---
title: 'Module: src/vllm_torchtpu/kernels/partial_kv_update.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/partial_kv_update.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.partial_kv_update`/
symbols:
  pallas_scatter_slots: pallas_scatter_slots().
  _pallas_scatter_torch_op: _pallas_scatter_torch_op.
  _scatter_slots_nd: _scatter_slots_nd().
  _make_sublane_block_kernel: _make_sublane_block_kernel().
  _scatter_slots_2d: _scatter_slots_2d().
  _jax_scatter_op: _jax_scatter_op().
  pallas_index_copy_: pallas_index_copy_().
  _blockspec_kernel: _blockspec_kernel().
  _make_sublane_block_kernel._kernel: _make_sublane_block_kernel()._kernel().
  _fake_scatter_op: _fake_scatter_op().
---
# Module: [`src/vllm_torchtpu/kernels/partial_kv_update.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py)

## Functions
- <a id="_blockspec_kernel"></a>`_blockspec_kernel(_sidx_ref, vals_ref, _pool_in_ref, pool_out_ref)` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L63) — One slot per grid step.
- <a id="_fake_scatter_op"></a>`_fake_scatter_op(pool: torch.Tensor, indices: torch.Tensor, vals: torch.Tensor)` — [`L210`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L210)
- <a id="_jax_scatter_op"></a>`_jax_scatter_op(pool: jax.Array, indices: jax.Array, vals: jax.Array)` — [`L199`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L199)
- <a id="_make_sublane_block_kernel._kernel"></a>`_kernel(sidx_ref, vals_ref, pool_in_ref, pool_out_ref)` — [`L111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L111)
- <a id="_make_sublane_block_kernel"></a>`_make_sublane_block_kernel(width: int, sublanes: int, num_updates: int)` — [`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L98) — Rank 2 on TensorCore: a sublane-tall block, read-modify-write.
- <a id="_scatter_slots_2d"></a>`_scatter_slots_2d(pool, indices, vals)` — [`L136`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L136) — Rank 2 via an 8-row block. See ``_make_sublane_block_kernel``.
- <a id="_scatter_slots_nd"></a>`_scatter_slots_nd(pool, indices, vals)` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L74) — Rank >= 3: native block spec, no manual DMA, no scratch.
- <a id="pallas_index_copy_"></a>`pallas_index_copy_(cache: torch.Tensor, indices: torch.Tensor, updates: torch.Tensor)` — [`L222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L222) — Drop-in for ``cache.index_copy_(0, indices, updates)`` on TPU.
- <a id="pallas_scatter_slots"></a>`pallas_scatter_slots(pool: jax.Array, indices: jax.Array, vals: jax.Array)` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L174) — ``pool[indices[i]] = vals[i]``, in place, cost O(len(indices)).

## Module values
- <a id="_pallas_scatter_torch_op"></a>`_pallas_scatter_torch_op` — [`L205`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/partial_kv_update.py#L205)

