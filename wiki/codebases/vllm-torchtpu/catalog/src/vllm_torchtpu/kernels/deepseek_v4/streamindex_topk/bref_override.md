---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.bref_override`/
symbols:
  StreamIndexKVBufferedRef.copy_in: StreamIndexKVBufferedRef#copy_in().
  StreamIndexOBufferedRef.copy_out: StreamIndexOBufferedRef#copy_out().
  StreamIndexKVSeqAlongLaneBufferedRef.copy_in: StreamIndexKVSeqAlongLaneBufferedRef#copy_in().
  StreamIndexQBufferedRef.copy_in: StreamIndexQBufferedRef#copy_in().
  StreamIndexQBufferedRef.wait_in: StreamIndexQBufferedRef#wait_in().
  StreamIndexOBufferedRef.wait_out: StreamIndexOBufferedRef#wait_out().
  _token_window: _token_window().
  StreamIndexKVBufferedRef.page_size_per_kv_packing: StreamIndexKVBufferedRef#page_size_per_kv_packing.
  StreamIndexQBufferedRef.input: StreamIndexQBufferedRef#input().
  StreamIndexOBufferedRef._unpadded_slice: StreamIndexOBufferedRef#_unpadded_slice().
  _step_offset: _step_offset().
  StreamIndexKVBufferedRef.input: StreamIndexKVBufferedRef#input().
  StreamIndexKVSeqAlongLaneBufferedRef.input: StreamIndexKVSeqAlongLaneBufferedRef#input().
  StreamIndexOBufferedRef.output: StreamIndexOBufferedRef#output().
  StreamIndexOBufferedRef.num_sublanes: StreamIndexOBufferedRef#num_sublanes.
  StreamIndexOBufferedRef.chunk_idx: StreamIndexOBufferedRef#chunk_idx.
  StreamIndexKVBufferedRef.bkv_p: StreamIndexKVBufferedRef#bkv_p.
  StreamIndexKVSeqAlongLaneBufferedRef.bkv_p: StreamIndexKVSeqAlongLaneBufferedRef#bkv_p.
  StreamIndexKVSeqAlongLaneBufferedRef.page_size: StreamIndexKVSeqAlongLaneBufferedRef#page_size.
  StreamIndexQBufferedRef: StreamIndexQBufferedRef#
  StreamIndexQBufferedRef.bq_sz: StreamIndexQBufferedRef#bq_sz.
  StreamIndexQBufferedRef.seq_batch_size: StreamIndexQBufferedRef#seq_batch_size.
  StreamIndexQBufferedRef.chunk_tokens: StreamIndexQBufferedRef#chunk_tokens.
  StreamIndexQBufferedRef.chunk_idx: StreamIndexQBufferedRef#chunk_idx.
  StreamIndexOBufferedRef.bq_sz: StreamIndexOBufferedRef#bq_sz.
  StreamIndexOBufferedRef.seq_batch_size: StreamIndexOBufferedRef#seq_batch_size.
  StreamIndexKVBufferedRef: StreamIndexKVBufferedRef#
  StreamIndexKVBufferedRef.kv_packing: StreamIndexKVBufferedRef#kv_packing.
  StreamIndexKVBufferedRef.pages_per_seq: StreamIndexKVBufferedRef#pages_per_seq.
  StreamIndexKVBufferedRef.seq_batch_size: StreamIndexKVBufferedRef#seq_batch_size.
  StreamIndexKVBufferedRef.chunk_idx: StreamIndexKVBufferedRef#chunk_idx.
  StreamIndexKVBufferedRef.create: StreamIndexKVBufferedRef#create().
  StreamIndexKVSeqAlongLaneBufferedRef: StreamIndexKVSeqAlongLaneBufferedRef#
  StreamIndexKVSeqAlongLaneBufferedRef.pages_per_seq: StreamIndexKVSeqAlongLaneBufferedRef#pages_per_seq.
  StreamIndexKVSeqAlongLaneBufferedRef.seq_batch_size: StreamIndexKVSeqAlongLaneBufferedRef#seq_batch_size.
  StreamIndexKVSeqAlongLaneBufferedRef.chunk_idx: StreamIndexKVSeqAlongLaneBufferedRef#chunk_idx.
  StreamIndexKVSeqAlongLaneBufferedRef.create: StreamIndexKVSeqAlongLaneBufferedRef#create().
  StreamIndexQBufferedRef.create: StreamIndexQBufferedRef#create().
  StreamIndexOBufferedRef: StreamIndexOBufferedRef#
  StreamIndexOBufferedRef.create: StreamIndexOBufferedRef#create().
  StreamIndexKVBufferedRef.wait_in: StreamIndexKVBufferedRef#wait_in().
  StreamIndexKVSeqAlongLaneBufferedRef.wait_in: StreamIndexKVSeqAlongLaneBufferedRef#wait_in().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py)

## Classes
### <a id="StreamIndexKVBufferedRef"></a>`StreamIndexKVBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py:57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L57)
- doc: Handles fetching paged KV cache into VMEM buffers across sequence sublanes.
- signature: `class StreamIndexKVBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="StreamIndexKVBufferedRef.copy_in"></a>`copy_in(self, src_ref: tuple[jax.Ref, jax.Ref, Any], grid_indices: tuple[int | jax.Array, ...])` — [`L138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L138) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="StreamIndexKVBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, bkv_p: int, page_size_per_kv_packing: int, kv_packing: int, pages_per_seq: int, seq_batch_size: int, grid_rank: int = 1, chunk_idx: int = 0)` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L70)
  - <a id="StreamIndexKVBufferedRef.input"></a>`input(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_count: int, use_lookahead: bool, bkv_p: int, page_size_per_kv_packing: int, kv_packing: int, pages_per_seq: int, seq_batch_size: int, grid_rank: int = 1, chunk_idx: int = 0, **kwargs: Any)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L108)
  - <a id="StreamIndexKVBufferedRef.wait_in"></a>`wait_in(self, src_ref: tuple[jax.Ref, jax.Ref, Any], grid_indices: tuple[int | jax.Array, ...])` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L191)
  - <a id="StreamIndexKVBufferedRef.bkv_p"></a>`bkv_p` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L60)
  - <a id="StreamIndexKVBufferedRef.chunk_idx"></a>`chunk_idx` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L67)
  - <a id="StreamIndexKVBufferedRef.kv_packing"></a>`kv_packing` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L64)
  - <a id="StreamIndexKVBufferedRef.page_size_per_kv_packing"></a>`page_size_per_kv_packing` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L61)
  - <a id="StreamIndexKVBufferedRef.pages_per_seq"></a>`pages_per_seq` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L65)
  - <a id="StreamIndexKVBufferedRef.seq_batch_size"></a>`seq_batch_size` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L66)
- uses (calls/refs, reference-scoped): [`_step_offset`](bref_override.md#_step_offset)
- used by: [`kernel`](streamindex_topk.md#kernel)

### <a id="StreamIndexKVSeqAlongLaneBufferedRef"></a>`StreamIndexKVSeqAlongLaneBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py:213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L213)
- doc: Fetches paged KV cache into VMEM for the SEQ_ALONG_LANE layout.
- signature: `class StreamIndexKVSeqAlongLaneBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.copy_in"></a>`copy_in(self, src_ref: tuple[jax.Ref, jax.Ref, Any], grid_indices: tuple[int | jax.Array, ...])` — [`L294`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L294) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, bkv_p: int, page_size: int, pages_per_seq: int, seq_batch_size: int, grid_rank: int = 1, chunk_idx: int = 0)` — [`L230`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L230)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.input"></a>`input(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_count: int, use_lookahead: bool, bkv_p: int, page_size: int, pages_per_seq: int, seq_batch_size: int, grid_rank: int = 1, chunk_idx: int = 0, **kwargs: Any)` — [`L266`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L266)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.wait_in"></a>`wait_in(self, src_ref: tuple[jax.Ref, jax.Ref, Any], grid_indices: tuple[int | jax.Array, ...])` — [`L339`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L339)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.bkv_p"></a>`bkv_p` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L223)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.chunk_idx"></a>`chunk_idx` — [`L227`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L227)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.page_size"></a>`page_size` — [`L224`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L224)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.pages_per_seq"></a>`pages_per_seq` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L225)
  - <a id="StreamIndexKVSeqAlongLaneBufferedRef.seq_batch_size"></a>`seq_batch_size` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L226)
- uses (calls/refs, reference-scoped): [`_step_offset`](bref_override.md#_step_offset)
- used by: [`kernel`](streamindex_topk.md#kernel)

### <a id="StreamIndexOBufferedRef"></a>`StreamIndexOBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py:489`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L489)
- doc: Handles scattering computed Top-K scores back to HBM.
- signature: `class StreamIndexOBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="StreamIndexOBufferedRef._unpadded_slice"></a>`_unpadded_slice(self, vmem_src: Any, total_sz: int | jax.Array)` — [`L622`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L622) — Slices out valid tokens and unpadded sublanes (`num_sublanes`).
  - <a id="StreamIndexOBufferedRef.copy_out"></a>`copy_out(self, dst_ref: tuple[Any, ...], grid_indices: tuple[int | jax.Array, ...])` — [`L558`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L558) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="StreamIndexOBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, bq_sz: int, num_sublanes: int, seq_batch_size: int = 1, grid_rank: int = 1, chunk_idx: int = 0)` — [`L498`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L498)
  - <a id="StreamIndexOBufferedRef.output"></a>`output(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_count: int, use_lookahead: bool, bq_sz: int, num_sublanes: int, seq_batch_size: int = 1, grid_rank: int = 1, chunk_idx: int = 0, **kwargs: Any)` — [`L532`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L532)
  - <a id="StreamIndexOBufferedRef.wait_out"></a>`wait_out(self, dst_ref: tuple[Any, ...], grid_indices: tuple[int | jax.Array, ...])` — [`L595`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L595)
  - <a id="StreamIndexOBufferedRef.bq_sz"></a>`bq_sz` — [`L492`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L492)
  - <a id="StreamIndexOBufferedRef.chunk_idx"></a>`chunk_idx` — [`L495`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L495)
  - <a id="StreamIndexOBufferedRef.num_sublanes"></a>`num_sublanes` — [`L493`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L493)
  - <a id="StreamIndexOBufferedRef.seq_batch_size"></a>`seq_batch_size` — [`L494`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L494)
- uses (calls/refs, reference-scoped): [`_token_window`](bref_override.md#_token_window), [`_step_offset`](bref_override.md#_step_offset)
- used by: [`kernel`](streamindex_topk.md#kernel)

### <a id="StreamIndexQBufferedRef"></a>`StreamIndexQBufferedRef`  ·  implements/extends BufferedRef
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py:361`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L361)
- doc: Handles fetching query slices into VMEM buffers.
- signature: `class StreamIndexQBufferedRef(pltpu.BufferedRef):`
- members:
  - <a id="StreamIndexQBufferedRef.copy_in"></a>`copy_in(self, src_ref: tuple[Any, ...], grid_indices: tuple[int | jax.Array, ...])` — [`L430`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L430)
  - <a id="StreamIndexQBufferedRef.create"></a>`create(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_type: pltpu.BufferType, buffer_count: int, use_lookahead: bool, bq_sz: int, chunk_tokens: int, seq_batch_size: int = 1, grid_rank: int = 1, chunk_idx: int = 0)` — [`L370`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L370)
  - <a id="StreamIndexQBufferedRef.input"></a>`input(cls, spec: pl.BlockSpec, dtype_or_type: Any, buffer_count: int, use_lookahead: bool, bq_sz: int, chunk_tokens: int, seq_batch_size: int = 1, grid_rank: int = 1, chunk_idx: int = 0, **kwargs: Any)` — [`L404`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L404)
  - <a id="StreamIndexQBufferedRef.wait_in"></a>`wait_in(self, src_ref: tuple[Any, ...], grid_indices: tuple[int | jax.Array, ...])` — [`L457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L457)
  - <a id="StreamIndexQBufferedRef.bq_sz"></a>`bq_sz` — [`L364`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L364)
  - <a id="StreamIndexQBufferedRef.chunk_idx"></a>`chunk_idx` — [`L367`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L367)
  - <a id="StreamIndexQBufferedRef.chunk_tokens"></a>`chunk_tokens` — [`L366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L366)
  - <a id="StreamIndexQBufferedRef.seq_batch_size"></a>`seq_batch_size` — [`L365`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L365)
- uses (calls/refs, reference-scoped): [`_token_window`](bref_override.md#_token_window)
- used by: [`kernel`](streamindex_topk.md#kernel)

## Functions
- <a id="_step_offset"></a>`_step_offset(meta_ref: Any, chunk_idx: int)` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L25) — Flat schedule row where chunk `chunk_idx`'s pipeline steps begin.
- <a id="_token_window"></a>`_token_window(refs: tuple[Any, ...], p_id: int | jax.Array, chunk_tokens: int, *, bq_sz: int, seq_batch_size: int, chunk_idx: int = 0)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/bref_override.py#L30) — Flat-token rows one pipeline step covers, as (token_start, size).

