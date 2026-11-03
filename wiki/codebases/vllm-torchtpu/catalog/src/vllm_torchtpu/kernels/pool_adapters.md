---
title: 'Module: src/vllm_torchtpu/kernels/pool_adapters.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/pool_adapters.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.pool_adapters`/
symbols:
  gather_region: gather_region().
  scatter_region: scatter_region().
  _gather_window: _gather_window().
  _scatter_window: _scatter_window().
  copy_blocks: copy_blocks().
  _pool_geometry: _pool_geometry().
  _bitcast_payload: _bitcast_payload().
  _rescale_rows: _rescale_rows().
  _out_rows: _out_rows().
  gather_region._kernel: gather_region()._kernel().
  _gather_window._kernel: _gather_window()._kernel().
  _scatter_window._kernel: _scatter_window()._kernel().
  scatter_region._kernel: scatter_region()._kernel().
  copy_blocks._copy_kernel: copy_blocks()._copy_kernel().
---
# Module: [`src/vllm_torchtpu/kernels/pool_adapters.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py)

## Functions
- <a id="_bitcast_payload"></a>`_bitcast_payload(payload: tuple[int, ...], pool_dtype, out_dtype)` — [`L50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L50) — Payload dims of a region block after an in-kernel bitcast.
- <a id="copy_blocks._copy_kernel"></a>`_copy_kernel(src_ref, dst_ref, pool_in_ref, pool_out_ref)` — [`L412`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L412)
- <a id="_gather_window"></a>`_gather_window(pool, mgr_indices, *, split: int, kb0: int, nblocks: int, out_dtype, out_lanes: int | None = None)` — [`L189`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L189) — Typed read of `nblocks` whole kernel blocks inside each request's
- <a id="gather_region._kernel"></a>`_kernel(sidx_ref, pool_ref, o_ref)` — [`L167`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L167)
- <a id="_gather_window._kernel"></a>`_kernel(sidx_ref, pool_ref, o_ref)` — [`L227`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L227)
- <a id="_scatter_window._kernel"></a>`_kernel(sidx_ref, val_ref, pool_in_ref, pool_out_ref)` — [`L283`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L283)
- <a id="scatter_region._kernel"></a>`_kernel(sidx_ref, val_ref, pool_in_ref, pool_out_ref)` — [`L375`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L375)
- <a id="_out_rows"></a>`_out_rows(payload: tuple[int, ...], ntok: int)` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L75)
- <a id="_pool_geometry"></a>`_pool_geometry(pool)` — [`L44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L44) — (block_size, payload dims between token and lane, lanes).
- <a id="_rescale_rows"></a>`_rescale_rows(rows: int, pool_dtype, out_dtype)` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L67)
- <a id="_scatter_window"></a>`_scatter_window(pool, vals, mgr_indices, *, split: int, kb0: int, nblocks: int)` — [`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L252) — Typed write of `nblocks` whole kernel blocks inside each request's
- <a id="copy_blocks"></a>`copy_blocks(pool, src_indices, dst_indices)` — [`L400`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L400) — Whole-block copies within the pool: pool[dst[i]] = pool[src[i]].
- <a id="gather_region"></a>`gather_region(pool, state_indices, *, tok0: int, ntok: int, out_dtype, out_lanes: int | None = None, split: int = 1)` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L82) — Per-request typed read of a pool token-range. — documented in [custom-ops](../../../../concepts/custom-ops.md)
- <a id="scatter_region"></a>`scatter_region(pool, vals, state_indices, *, tok0: int, ntok: int, split: int = 1)` — [`L316`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/pool_adapters.py#L316) — Per-request typed write of a pool token-range (in place); mirrors — documented in [custom-ops](../../../../concepts/custom-ops.md)

