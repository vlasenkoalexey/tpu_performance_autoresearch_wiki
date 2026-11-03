---
title: 'Module: src/vllm_torchtpu/megakernel/pool/pack.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/pool/pack.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.pool.pack`/
symbols:
  pool_to_states: pool_to_states().
  states_to_pool: states_to_pool().
  allocate_test_layout: allocate_test_layout().
  ssm_to_raw_pages: ssm_to_raw_pages().
  conv_to_raw_page: conv_to_raw_page().
  raw_page_to_conv: raw_page_to_conv().
  raw_pages_to_ssm: raw_pages_to_ssm().
  _pages_per_seq: _pages_per_seq().
  _DEFAULT_LAYOUT: _DEFAULT_LAYOUT.
  kv_to_raw_page: kv_to_raw_page().
  _unfold: _unfold().
  raw_page_to_kv: raw_page_to_kv().
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/pool/pack.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py)

## Functions
- <a id="_pages_per_seq"></a>`_pages_per_seq(ex: ExecSpec)` — [`L159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L159) — Pages per sequence (`ex.ctx // page_size`); requires `ctx % page_size == 0`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="_unfold"></a>`_unfold(x: Any, R: int)` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L37) — `[R * N0, ...] -> [R, N0, ...]` (inverse of the rank-folded state layout).
- <a id="allocate_test_layout"></a>`allocate_test_layout(layout: PoolLayout, ex: ExecSpec)` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L168) — Allocate disjoint `page_table`, `ckpt_indices`, `read_offsets`, and `min_pages`.
- <a id="conv_to_raw_page"></a>`conv_to_raw_page(taps_qkv: Any, layout: PoolLayout | None = None)` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L124) — Pack `(conv_taps, QKV)` conv taps into one conv page `kv_page_shape` fp8.
- <a id="kv_to_raw_page"></a>`kv_to_raw_page(k_page: Any, v_page: Any)` — [`L45`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L45) — Pack `(page_size, HD)` K and V into `(2, HD // 4, 4, page_size) fp8`.
- <a id="pool_to_states"></a>`pool_to_states(layout: PoolLayout, ex: ExecSpec, raw_pools: tuple[jax.Array, ...] | list[jax.Array], page_table: Any, ckpt_indices: Any = None)` — [`L315`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L315) — Unpack rank-folded raw pools into unfolded logical states `[R, ...]`. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)
- <a id="raw_page_to_conv"></a>`raw_page_to_conv(raw_1page: Any, QKV: int, layout: PoolLayout | None = None)` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L141) — Unpack one conv page `kv_page_shape` fp8 into `(conv_taps, QKV) f32`.
- <a id="raw_page_to_kv"></a>`raw_page_to_kv(raw_page: Any)` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L61) — Unpack `(2, HD // 4, 4, page_size) fp8` into `(k_page, v_page)`.
- <a id="raw_pages_to_ssm"></a>`raw_pages_to_ssm(raw_4pages: Any, vh: int, KD: int = 128, VD: int = 128, layout: PoolLayout | None = None)` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L98) — Unpack `(rec_pages_per_slot, *kv_page_shape) fp8` into `(vh, KD, VD) bf16`.
- <a id="ssm_to_raw_pages"></a>`ssm_to_raw_pages(rec_slice: Any, layout: PoolLayout | None = None)` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L70) — Pack key-major `(vh, KD, VD) bf16` into the slot's recurrent pages.
- <a id="states_to_pool"></a>`states_to_pool(layout: PoolLayout, ex: ExecSpec, states: dict[str, Any], page_table: Any, ckpt_indices: Any = None, read_offsets: Any = None)` — [`L210`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L210) — Pack unfolded or folded states into `layout.num_pools` raw pools. — documented in [megakernel-pool](../../../../../concepts/megakernel-pool.md)

## Module values
- <a id="_DEFAULT_LAYOUT"></a>`_DEFAULT_LAYOUT` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L34)
- <a id="__all__"></a>`__all__` — [`L410`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/pool/pack.py#L410)

