---
title: 'Module: src/vllm_torchtpu/megakernel/pool/backend.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/backend.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.backend`/
symbols:
  make_pool_backend: make_pool_backend().
  can_pool_gather: can_pool_gather().
  check_ckpt_bounds: check_ckpt_bounds().
  make_pool_backend._scatter: make_pool_backend()._scatter().
  make_pool_backend._gather: make_pool_backend()._gather().
  kernel_debug_check: kernel_debug_check().
  POOL_KERNEL_NAMES: POOL_KERNEL_NAMES.
  resolve_active_seqs: resolve_active_seqs().
  make_pool_backend._can_pool_gather: make_pool_backend()._can_pool_gather().
  RecChunk: RecChunk.
  GATHER_KERNEL_NAME: GATHER_KERNEL_NAME.
  SCATTER_KERNEL_NAME: SCATTER_KERNEL_NAME.
  kernel_debug_check._cb: kernel_debug_check()._cb().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/backend.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py)

## Functions
- <a id="make_pool_backend._can_pool_gather"></a>`_can_pool_gather(ex_paged: ExecSpec)` — [`L321`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L321)
- <a id="kernel_debug_check._cb"></a>`_cb(ok: Any)` — [`L196`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L196)
- <a id="make_pool_backend._gather"></a>`_gather(ex_paged: ExecSpec, raw_pools: tuple[jax.Array, ...], ckpt_indices: jax.Array | None, read_offsets: jax.Array | None, active_seqs: Any)` — [`L269`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L269) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="make_pool_backend._scatter"></a>`_scatter(ex_paged: ExecSpec, raw_pools: tuple[jax.Array, ...], pos: jax.Array, page_table: jax.Array, out_map: dict[str, Any], ckpt_indices: jax.Array | None, active_seqs: Any)` — [`L292`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L292) — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="can_pool_gather"></a>`can_pool_gather(layout: PoolLayout, ex: ExecSpec, rec_chunk: RecChunk | None = None)` — [`L207`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L207) — Whether verify bucket `ex` can gather recurrent state in-kernel (`GPR`). — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="check_ckpt_bounds"></a>`check_ckpt_bounds(ckpt_indices: Any, num_pages: int, layout: PoolLayout, *, act_mode: str = "from_ckpt", active_mask: Any = None, read_offsets: Any = None, raw_pools: Any = None, ns: int | None = None, min_k: int = 1)` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L70) — Validate pool/ckpt shapes and concrete active slot bounds in `[0, num_pages)`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="kernel_debug_check"></a>`kernel_debug_check(cond: Any, msg: str, *, interpret: bool)` — [`L191`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L191) — Emit `pl.debug_check` and enforce it in CPU `interpret` mode when enabled.
- <a id="make_pool_backend"></a>`make_pool_backend(layout: PoolLayout, *, check: Callable[[ExecSpec], None] | None = None, rec_chunk: RecChunk | None = None, supports_fused_io: bool = True, supports_pool_gather: bool | None = None)` — [`L240`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L240) — Build the `PoolBackend` (gather / scatter callbacks) for `layout`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="resolve_active_seqs"></a>`resolve_active_seqs(active_seqs: jax.Array | str | None, *, default_mode: str = "from_ckpt", ns: int | None = None, has_recurrent: bool = True)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L41) — Normalize `active_seqs` into `(act_mode, active_mask_array)`.

## Module values
- <a id="GATHER_KERNEL_NAME"></a>`GATHER_KERNEL_NAME` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L36)
- <a id="POOL_KERNEL_NAMES"></a>`POOL_KERNEL_NAMES` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L38)
- <a id="RecChunk"></a>`RecChunk` — [`L204`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L204)
- <a id="SCATTER_KERNEL_NAME"></a>`SCATTER_KERNEL_NAME` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L37)
- <a id="__all__"></a>`__all__` — [`L336`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/backend.py#L336)

