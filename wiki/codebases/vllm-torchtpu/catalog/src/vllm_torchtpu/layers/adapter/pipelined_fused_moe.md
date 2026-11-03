---
title: 'Module: src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.pipelined_fused_moe`/
symbols:
  pipelined_fused_moe_gmm: pipelined_fused_moe_gmm().
  enable_pipelined_collective_and_compute: enable_pipelined_collective_and_compute().
  collection_chunks: collection_chunks().
  _log_active_chunk_pipeline: _log_active_chunk_pipeline().
  _quantized_all_gather: _quantized_all_gather().
  _fixed_chunk_buckets._fixed_chunk_buckets: _fixed_chunk_buckets._fixed_chunk_buckets.
  fixed_moe_collection_chunks: fixed_moe_collection_chunks().
  _get_moe_collective_group: _get_moe_collective_group().
  pipelined_fused_moe_gmm._all_gather_hs: pipelined_fused_moe_gmm()._all_gather_hs().
  logger: logger.
  enable_pipeline_collective_and_compute: enable_pipeline_collective_and_compute.
  fixed_chunk_count: fixed_chunk_count().
  calculate_moe_chunks: calculate_moe_chunks().
---
# Module: [`src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py)

## Functions
- <a id="pipelined_fused_moe_gmm._all_gather_hs"></a>`_all_gather_hs(hs_slice)` — [`L329`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L329)
- <a id="_get_moe_collective_group"></a>`_get_moe_collective_group()` — [`L160`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L160) — Select the collective group whose expert shards the kernel combines.
- <a id="_log_active_chunk_pipeline"></a>`_log_active_chunk_pipeline()` — [`L178`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L178) — Emit trace-time evidence without passing symbolic values to logging.
- <a id="_quantized_all_gather"></a>`_quantized_all_gather(collective_group, hidden_states: torch.Tensor)` — [`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L109) — All-gather activations in fp8, restored on arrival.
- <a id="calculate_moe_chunks"></a>`calculate_moe_chunks(seq_len: int, parallel_size: int, chunk_size: int)` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L125) — Calculate the number of chunks and local chunk size for MoE chunk pipelining.
- <a id="collection_chunks"></a>`collection_chunks(seq_len: int, parallel_size: int)` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L83) — Chunk count and local chunk size for this rank's ``seq_len`` tokens.
- <a id="enable_pipelined_collective_and_compute"></a>`enable_pipelined_collective_and_compute()` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L95) — Check whether collective communication and compute pipelining is enabled.
- <a id="fixed_chunk_count"></a>`fixed_chunk_count(buckets: Sequence[int], parallel_size: int, chunk_size: int)` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L63) — Chunk count that keeps every gather at or under ``chunk_size``.
- <a id="fixed_moe_collection_chunks"></a>`fixed_moe_collection_chunks(buckets: Sequence[int])` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L44) — Runs every MoE collection under this context in a fixed chunk count.
- <a id="pipelined_fused_moe_gmm"></a>`pipelined_fused_moe_gmm(hidden_states: torch.Tensor, w1: torch.Tensor, w2: torch.Tensor, w1_scale: torch.Tensor | None, w2_scale: torch.Tensor | None, w1_bias: torch.Tensor | None, w2_bias: torch.Tensor | None, topk_weights: torch.Tensor, topk_ids: torch.Tensor, experts_start: torch.Tensor | None, topk: int, activation: str, rhs_quant_dtype=None, skip_padded_tokens: bool | None = None)` — [`L192`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L192) — Wrapper around fused_moe_gmm to pipeline DP/PCP collectives and compute. — documented in [quantization-methods](../../../../../concepts/quantization-methods.md)

## Module values
- <a id="_fixed_chunk_buckets._fixed_chunk_buckets"></a>`_fixed_chunk_buckets` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L40)
- <a id="enable_pipeline_collective_and_compute"></a>`enable_pipeline_collective_and_compute` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L106)
- <a id="logger"></a>`logger` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/pipelined_fused_moe.py#L35)

