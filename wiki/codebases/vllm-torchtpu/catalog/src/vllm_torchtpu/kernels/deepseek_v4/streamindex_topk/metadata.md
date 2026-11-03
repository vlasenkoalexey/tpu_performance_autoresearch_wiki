---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.metadata`/
symbols:
  compute_batched_seq_metadata: compute_batched_seq_metadata().
  compute_batched_seq_metadata._compute_schedule: compute_batched_seq_metadata()._compute_schedule().
  compute_metadata: compute_metadata().
  MetadataRef: MetadataRef#
  MetadataRef.start_seq_idx: MetadataRef#start_seq_idx().
  cp_local_length: cp_local_length().
  cp_local_to_global: cp_local_to_global().
  cp_owner_rank: cp_owner_rank().
  cp_global_to_local: cp_global_to_local().
  cp_rank_as_data: cp_rank_as_data().
  MetadataRef.batch_tile_idx: MetadataRef#batch_tile_idx.
  MetadataRef.create: MetadataRef#create().
  next_power_of_2: next_power_of_2().
  MetadataRef.num_steps: MetadataRef#num_steps.
  MetadataRef.bq_idx: MetadataRef#bq_idx.
  MetadataRef.bkv_idx: MetadataRef#bkv_idx.
  generate_max_steps: generate_max_steps().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py)

## Classes
### <a id="MetadataRef"></a>`MetadataRef`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py:79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L79)
- doc: Ref containers for pipeline step schedule indexing arrays.
- signature: `class MetadataRef:`
- members:
  - <a id="MetadataRef.create"></a>`create(cls, num_steps: Any, batch_tile_idx: Any, bq_idx: Any, bkv_idx: Any)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L88)
  - <a id="MetadataRef.start_seq_idx"></a>`start_seq_idx(self)` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L103) — Returns starting sequence index per step (alias for batch_tile_idx).
  - <a id="MetadataRef.batch_tile_idx"></a>`batch_tile_idx` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L83)
  - <a id="MetadataRef.bkv_idx"></a>`bkv_idx` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L85)
  - <a id="MetadataRef.bq_idx"></a>`bq_idx` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L84)
  - <a id="MetadataRef.num_steps"></a>`num_steps` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L82)
- used by: [`_compute_schedule`](metadata.md#compute_batched_seq_metadata._compute_schedule), [`compute_batched_seq_metadata`](metadata.md#compute_batched_seq_metadata), [`compute_metadata`](metadata.md#compute_metadata)

## Functions
- <a id="compute_batched_seq_metadata._compute_schedule"></a>`_compute_schedule()` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L211)
- <a id="compute_batched_seq_metadata"></a>`compute_batched_seq_metadata(seq_lens: jax.Array, cu_q_lens: jax.Array, start_seq_idx: jax.Array | int, end_seq_idx: jax.Array | int, bq_sz: int, bkv_sz: int, pages_per_seq: int, page_size: int, max_num_tokens: int, compression_ratio: int = 1, static_q_len: int | None = None, seq_batch_size: int = 1, chunk_token_start: int | tuple[int | None, ...] | None = None, chunk_tokens: int | None = None, cp_rank: jax.Array | int = 0, cp_size: int = 1, interleave_c: int = 1)` — [`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L140)
- <a id="compute_metadata"></a>`compute_metadata(seq_lens: jax.Array, cu_q_lens: jax.Array, start_seq_idx: jax.Array | int, end_seq_idx: jax.Array | int, bq_sz: int, bkv_sz: int, pages_per_seq: int, page_size: int, max_num_tokens: int, compression_ratio: int = 1, static_q_len: int | None = None, seq_batch_size: int = 1, chunk_token_start: int | tuple[int | None, ...] | None = None, chunk_tokens: int | None = None, cp_rank: jax.Array | int = 0, cp_size: int = 1, interleave_c: int = 1)` — [`L333`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L333) — Unified metadata calculation for batch_tile_idx, bq_idx, and bkv_idx.
- <a id="cp_global_to_local"></a>`cp_global_to_local(global_idx, cp_size: int, interleave_c: int)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L62) — Inverse of `cp_local_to_global`, evaluated on the owning rank.
- <a id="cp_local_length"></a>`cp_local_length(global_len, cp_rank, cp_size: int, interleave_c: int)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L42) — Count compressed positions ``< global_len`` owned by `cp_rank`.
- <a id="cp_local_to_global"></a>`cp_local_to_global(local_idx, cp_rank, cp_size: int, interleave_c: int)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L30) — Map a rank-local compressed index to its global compressed position.
- <a id="cp_owner_rank"></a>`cp_owner_rank(global_idx, cp_size: int, interleave_c: int)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L55) — Which rank owns global compressed position `global_idx`.
- <a id="cp_rank_as_data"></a>`cp_rank_as_data(cp_axis_name: str, cp_size: int)` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L70) — This shard's index along `cp_axis_name`, without `lax.axis_index`.
- <a id="generate_max_steps"></a>`generate_max_steps(num_seqs: int, max_pages_per_seq: int)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L113) — Calculates upper bound on max_steps based on TPU SMEM capacity.
- <a id="next_power_of_2"></a>`next_power_of_2(x)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/metadata.py#L108)

