---
title: 'Module: src/vllm_torchtpu/runner/kv_cache_dsv4.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/kv_cache_dsv4.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.kv_cache_dsv4`/
symbols:
  DsV4KVCacheAllocator._initialize_ds_v4_kv_cache: DsV4KVCacheAllocator#_initialize_ds_v4_kv_cache().
  DsV4KVCacheAllocator._refresh_ds_v4_request_caps: DsV4KVCacheAllocator#_refresh_ds_v4_request_caps().
  DsV4KVCacheAllocator._create_cache: DsV4KVCacheAllocator#_create_cache().
  DsV4KVCacheAllocator._classify_ds_v4_layers: DsV4KVCacheAllocator#_classify_ds_v4_layers().
  DsV4KVCacheAllocator._ds_v4_compressed_kv_layer_name: DsV4KVCacheAllocator#_ds_v4_compressed_kv_layer_name().
  logger: logger.
  DsV4KVCacheAllocator._host_at: DsV4KVCacheAllocator#_host_at().
  DsV4KVCacheAllocator.widest_table: DsV4KVCacheAllocator#widest_table().
  DsV4KVCacheAllocator.runner: DsV4KVCacheAllocator#runner.
  DsV4KVCacheAllocator._validate_ds_v4_overlay: DsV4KVCacheAllocator#_validate_ds_v4_overlay().
  DsV4KVCacheAllocator: DsV4KVCacheAllocator#
  DsV4KVCacheAllocator._ds_v4_cache_arrays: DsV4KVCacheAllocator#_ds_v4_cache_arrays().
  DsV4KVCacheAllocator.__init__: DsV4KVCacheAllocator#__init__().
  DsV4KVCacheAllocator._DS_V4_STATE_CACHE_SUFFIX: DsV4KVCacheAllocator#_DS_V4_STATE_CACHE_SUFFIX.
  DsV4KVCacheAllocator._DS_V4_CSA_COMPRESS_RATIO: DsV4KVCacheAllocator#_DS_V4_CSA_COMPRESS_RATIO.
  DsV4KVCacheAllocator._DS_V4_INDEXER_CACHE_SUFFIX: DsV4KVCacheAllocator#_DS_V4_INDEXER_CACHE_SUFFIX.
  DsV4KVCacheAllocator._DS_V4_ROPE_CACHE_SUFFIX: DsV4KVCacheAllocator#_DS_V4_ROPE_CACHE_SUFFIX.
  DsV4KVCacheAllocator._DS_V4_KV_PACKING: DsV4KVCacheAllocator#_DS_V4_KV_PACKING.
  DsV4KVCacheAllocator._is_ds_v4_swa_layer: DsV4KVCacheAllocator#_is_ds_v4_swa_layer().
---
# Module: [`src/vllm_torchtpu/runner/kv_cache_dsv4.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py)

## Classes
### <a id="DsV4KVCacheAllocator"></a>`DsV4KVCacheAllocator`
- def: [`src/vllm_torchtpu/runner/kv_cache_dsv4.py:50`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L50)
- doc: Owns the DeepSeek-V4 special cases in KV-cache allocation.
- signature: `class DsV4KVCacheAllocator:`
- members:
  - <a id="DsV4KVCacheAllocator._classify_ds_v4_layers"></a>`_classify_ds_v4_layers(self, kv_cache_config: KVCacheConfig, per_layer_spec: Callable[[str], KVCacheSpec])` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L92) — Split DSv4's layers by the kernel that reads their array.
  - <a id="DsV4KVCacheAllocator._ds_v4_cache_arrays"></a>`_ds_v4_cache_arrays(entry)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L417) — Every array a bound DSv4 KV entry holds.
  - <a id="DsV4KVCacheAllocator._ds_v4_compressed_kv_layer_name"></a>`_ds_v4_compressed_kv_layer_name(state_cache_name: str)` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L63) — The layer whose compressed-KV records a DSv4 state cache accompanies.
  - <a id="DsV4KVCacheAllocator._host_at"></a>`_host_at(hosts: list[torch.Tensor], position: int)` — [`L270`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L270) — `hosts[position]`, growing the list with standalone arrays.
  - <a id="DsV4KVCacheAllocator._initialize_ds_v4_kv_cache"></a>`_initialize_ds_v4_kv_cache(self, kv_cache_config: KVCacheConfig, per_layer_spec: Callable[[str], KVCacheSpec], kv_caches: dict[str, torch.Tensor], num_blocks: int)` — [`L156`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L156) — Allocate and alias DeepSeek-V4's KV caches. — documented in [deepseek-v4-compress-and-store-kernel](../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="DsV4KVCacheAllocator._is_ds_v4_swa_layer"></a>`_is_ds_v4_swa_layer(layer_name: str, spec: KVCacheSpec)` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L85) — A DSv4 sliding-window cache (not a compressor state cache).
  - <a id="DsV4KVCacheAllocator._refresh_ds_v4_request_caps"></a>`_refresh_ds_v4_request_caps(self, kv_cache_config: KVCacheConfig, swa_layer_groups: list[list[str]], state_layer_names: list[str])` — [`L348`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L348) — Set the requests-per-forward caps from the compressed-KV tables only. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="DsV4KVCacheAllocator._validate_ds_v4_overlay"></a>`_validate_ds_v4_overlay(cls, kv_cache_config: KVCacheConfig, kv_caches: dict[str, torch.Tensor])` — [`L429`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L429) — No two layers of one cache group may share an array.
  - <a id="DsV4KVCacheAllocator.widest_table"></a>`widest_table(model_len: int | None)` — [`L381`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L381)
  - <a id="DsV4KVCacheAllocator.runner"></a>`runner` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L60)
- protocol/private: <a id="DsV4KVCacheAllocator._DS_V4_CSA_COMPRESS_RATIO"></a>`_DS_V4_CSA_COMPRESS_RATIO`[`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L57), <a id="DsV4KVCacheAllocator._DS_V4_INDEXER_CACHE_SUFFIX"></a>`_DS_V4_INDEXER_CACHE_SUFFIX`[`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L54), <a id="DsV4KVCacheAllocator._DS_V4_KV_PACKING"></a>`_DS_V4_KV_PACKING`[`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L56), <a id="DsV4KVCacheAllocator._DS_V4_ROPE_CACHE_SUFFIX"></a>`_DS_V4_ROPE_CACHE_SUFFIX`[`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L55), <a id="DsV4KVCacheAllocator._DS_V4_STATE_CACHE_SUFFIX"></a>`_DS_V4_STATE_CACHE_SUFFIX`[`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L53), <a id="DsV4KVCacheAllocator.__init__"></a>`__init__`[`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L59), <a id="DsV4KVCacheAllocator._create_cache"></a>`_create_cache`[`L206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L206)
- uses (calls/refs, reference-scoped): [`device`](tpu_runner.md#TPUModelRunner.device), [`num_reqs_most_model_len`](tpu_runner.md#TPUModelRunner.num_reqs_most_model_len), [`max_num_reqs`](tpu_runner.md#TPUModelRunner.max_num_reqs), [`num_reqs_max_model_len`](tpu_runner.md#TPUModelRunner.num_reqs_max_model_len), [`max_num_tokens`](tpu_runner.md#TPUModelRunner.max_num_tokens), [`PallasAttentionBackend`](../layers/adapter/attention.md#PallasAttentionBackend), [`most_model_len`](tpu_runner.md#TPUModelRunner.most_model_len), [`TPUModelRunner`](tpu_runner.md#TPUModelRunner), [`SAL_SUBLANE_GROUPS`](../kernels/deepseek_v4/compress_and_store/config.md#SAL_SUBLANE_GROUPS), [`num_blocks_per_most_len_req`](tpu_runner.md#TPUModelRunner.num_blocks_per_most_len_req), [`ROW_WORDS`](../kernels/deepseek_v4/csa_cache_layout.md#ROW_WORDS), [`ROPE_TOKENS_PER_ROW`](../kernels/deepseek_v4/csa_cache_layout.md#ROPE_TOKENS_PER_ROW), [`_attention_capacity`](tpu_runner.md#TPUModelRunner._attention_capacity), [`attention_block_table_width`](../layers/core/attention_metadata.md#attention_block_table_width), [`logger`](kv_cache_dsv4.md#logger), [`RunLocalStateSpec`](../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.md#RunLocalStateSpec), [`get_max_num_seqs_for_pages`](../layers/adapter/attention.md#PallasAttentionBackend.get_max_num_seqs_for_pages), [`check_seq_along_lane_page_size`](../kernels/deepseek_v4/compress_and_store/config.md#check_seq_along_lane_page_size), [`_decode_device_cache_key`](tpu_runner.md#TPUModelRunner._decode_device_cache_key)
- used by: [`initialize_kv_cache`](kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`ds_v4`](kv_cache_manager.md#KVCacheManager.ds_v4)

## Module values
- <a id="logger"></a>`logger` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/kv_cache_dsv4.py#L47)

