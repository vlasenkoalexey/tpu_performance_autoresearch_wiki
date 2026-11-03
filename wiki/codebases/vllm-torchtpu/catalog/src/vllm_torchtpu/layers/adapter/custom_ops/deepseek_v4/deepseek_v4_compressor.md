---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.deepseek_v4.deepseek_v4_compressor`/
symbols:
  VllmDeepseekCompressor._build_compressor_op: VllmDeepseekCompressor#_build_compressor_op().
  VllmDeepseekCompressor.forward: VllmDeepseekCompressor#forward().
  VllmCompressorStateCache.block_size: VllmCompressorStateCache#block_size.
  VllmCompressorStateCache._derive_block_size: VllmCompressorStateCache#_derive_block_size().
  VllmCompressorStateCache.compress_ratio: VllmCompressorStateCache#compress_ratio.
  VllmDeepseekCompressor: VllmDeepseekCompressor#
  VllmDeepseekCompressor.transpose_wkv_wgate: VllmDeepseekCompressor#transpose_wkv_wgate().
  _run_compressor: _run_compressor().
  VllmDeepseekCompressor._wkv_wgate_transposed: VllmDeepseekCompressor#_wkv_wgate_transposed.
  VllmDeepseekCompressor.compressor_op: VllmDeepseekCompressor#compressor_op().
  RunLocalStateSpec: RunLocalStateSpec#
  VllmCompressorStateCache.get_kv_cache_spec: VllmCompressorStateCache#get_kv_cache_spec().
  VllmCompressorStateCache.run_local: VllmCompressorStateCache#run_local().
  _compressor_op_cache: _compressor_op_cache.
  _compressor_jax_csa: _compressor_jax_csa().
  _compressor_jax_hca: _compressor_jax_hca().
  _compressor_jax_indexer: _compressor_jax_indexer().
  VllmCompressorStateCache.head_dim: VllmCompressorStateCache#head_dim.
  VllmDeepseekCompressor._as_kernel_cache_view: VllmDeepseekCompressor#_as_kernel_cache_view().
  logger: logger.
  RunLocalStateSpec.merge: RunLocalStateSpec#merge().
  RunLocalStateSpec.is_uniform_with_collection: RunLocalStateSpec#is_uniform_with_collection().
  VllmCompressorStateCache: VllmCompressorStateCache#
  VllmDeepseekCompressor._has_rope_cache: VllmDeepseekCompressor#_has_rope_cache().
  VllmDeepseekCompressor._separate_state: VllmDeepseekCompressor#_separate_state().
  VllmDeepseekCompressor._fake_compressor: VllmDeepseekCompressor#_fake_compressor().
  BATCH_AXIS: BATCH_AXIS.
  RunLocalStateSpec.prefix_cacheable: RunLocalStateSpec#prefix_cacheable().
  VllmCompressorStateCache.__init__: VllmCompressorStateCache#__init__().
  VllmDeepseekCompressor.__init__: VllmDeepseekCompressor#__init__().
  VllmDeepseekCompressor.num_layers: VllmDeepseekCompressor#num_layers.
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py)

## Classes
### <a id="RunLocalStateSpec"></a>`RunLocalStateSpec`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py:253`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L253)
- doc: Compressor state whose window is exactly one compressed run.
- signature: `class RunLocalStateSpec(SlidingWindowMLASpec):`
- members:
  - <a id="RunLocalStateSpec.is_uniform_with_collection"></a>`is_uniform_with_collection(self, kv_cache_specs: dict[str, KVCacheSpec])` — [`L289`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L289)
  - <a id="RunLocalStateSpec.merge"></a>`merge(cls, specs: list[Self])` — [`L279`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L279)
  - <a id="RunLocalStateSpec.prefix_cacheable"></a>`prefix_cacheable(self)` — [`L269`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L269)
- used by: [`block_size`](deepseek_v4_compressor.md#VllmCompressorStateCache.block_size), [`_classify_ds_v4_layers`](../../../../runner/kv_cache_dsv4.md#DsV4KVCacheAllocator._classify_ds_v4_layers)

### <a id="VllmCompressorStateCache"></a>`VllmCompressorStateCache`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py:297`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L297)
- doc: Compressor state cache, paged to fit the array that hosts it.
- signature: `class VllmCompressorStateCache(CompressorStateCache):`
- members:
  - <a id="VllmCompressorStateCache._derive_block_size"></a>`_derive_block_size(self, kv_cache_block_size: int)` — [`L324`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L324) — State tokens per page of the array that hosts this state. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
  - <a id="VllmCompressorStateCache.get_kv_cache_spec"></a>`get_kv_cache_spec(self, vllm_config: VllmConfig)` — [`L374`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L374)
  - <a id="VllmCompressorStateCache.run_local"></a>`run_local(self)` — [`L370`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L370) — Whether the state window is one compressed run (RunLocalStateSpec).
  - <a id="VllmCompressorStateCache.block_size"></a>`block_size` — [`L388`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L388) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
  - <a id="VllmCompressorStateCache.compress_ratio"></a>`compress_ratio` — [`L315`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L315)
  - <a id="VllmCompressorStateCache.head_dim"></a>`head_dim` — [`L314`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L314)
- protocol/private: <a id="VllmCompressorStateCache.__init__"></a>`__init__`[`L300`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L300)
- uses (calls/refs, reference-scoped): [`select_mode`](../../../../kernels/deepseek_v4/compress_and_store/config.md#select_mode), [`align_to`](../../../../utils.md#align_to), [`state_block_size`](../../../../kernels/deepseek_v4/compress_and_store/config.md#state_block_size), [`RunLocalStateSpec`](deepseek_v4_compressor.md#RunLocalStateSpec)
- used by: [`_build_compressor_op`](deepseek_v4_compressor.md#VllmDeepseekCompressor._build_compressor_op), [`_wkv_wgate_transposed`](deepseek_v4_compressor.md#VllmDeepseekCompressor._wkv_wgate_transposed)

### <a id="VllmDeepseekCompressor"></a>`VllmDeepseekCompressor`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py:405`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L405) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
- doc: TPU compressor: projects, saves state, compresses and stores.
- signature: `class VllmDeepseekCompressor(DeepseekCompressor):`
- members:
  - <a id="VllmDeepseekCompressor._as_kernel_cache_view"></a>`_as_kernel_cache_view(cache: torch.Tensor | None)` — [`L592`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L592) — The kernels require uint8; vLLM allocates as `kv_cache_dtype`.
  - <a id="VllmDeepseekCompressor.compressor_op"></a>`compressor_op(self)` — [`L463`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L463) — Built on first use, since `state_block_size` is baked in statically.
  - <a id="VllmDeepseekCompressor.forward"></a>`forward(self, hidden_states: torch.Tensor, positions: torch.Tensor, rotary_emb: nn.Module)` — [`L606`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L606) — documented in [custom-ops](../../../../../../../concepts/custom-ops.md)
  - <a id="VllmDeepseekCompressor.transpose_wkv_wgate"></a>`transpose_wkv_wgate(self)` — [`L429`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L429) — Stores ``fused_wkv_wgate.weight`` transposed, once, at load time.
  - <a id="VllmDeepseekCompressor.num_layers"></a>`num_layers` — [`L425`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L425)
- protocol/private: <a id="VllmDeepseekCompressor.__init__"></a>`__init__`[`L408`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L408), <a id="VllmDeepseekCompressor._build_compressor_op"></a>`_build_compressor_op`[`L476`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L476), <a id="VllmDeepseekCompressor._fake_compressor"></a>`_fake_compressor`[`L550`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L550), <a id="VllmDeepseekCompressor._has_rope_cache"></a>`_has_rope_cache`[`L455`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L455), <a id="VllmDeepseekCompressor._separate_state"></a>`_separate_state`[`L459`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L459), <a id="VllmDeepseekCompressor._wkv_wgate_transposed"></a>`_wkv_wgate_transposed`[`L410`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L410)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../../utils.md#synchronize_tensors), [`get_pallas_op_mesh`](../../../../models/vllm/vllm_model_wrapper_context.md#get_pallas_op_mesh), [`request_distribution`](../../../core/attention_metadata.md#AttentionMetadata.request_distribution), [`query_start_loc`](../../../core/attention_metadata.md#AttentionMetadata.query_start_loc), [`block_tables`](../../../core/attention_metadata.md#AttentionMetadata.block_tables), [`block_size`](deepseek_v4_compressor.md#VllmCompressorStateCache.block_size), [`run_local`](deepseek_v4_compressor.md#VllmCompressorStateCache.run_local), [`_compressor_op_cache`](deepseek_v4_compressor.md#_compressor_op_cache), [`_compressor_jax_csa`](deepseek_v4_compressor.md#_compressor_jax_csa), [`_compressor_jax_hca`](deepseek_v4_compressor.md#_compressor_jax_hca), [`_compressor_jax_indexer`](deepseek_v4_compressor.md#_compressor_jax_indexer), [`VllmCompressorStateCache`](deepseek_v4_compressor.md#VllmCompressorStateCache), [`BATCH_AXIS`](deepseek_v4_compressor.md#BATCH_AXIS)
- used by: [`__init__`](../../../../models/vllm/deepseek_v4/attention.md#VllmDeepseekV4MLAAttention.__init__), [`__init__`](deepseek_v4_indexer.md#VllmDeepseekV4Indexer.__init__), [`load_weights`](../../../../models/vllm/deepseek_v4/model.md#DeepseekV4ForCausalLM.load_weights)

## Functions
- <a id="_compressor_jax_csa"></a>`_compressor_jax_csa(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, norm_weight: jax.Array, cos_sin_cache: jax.Array, positions: jax.Array, state_block_tables: jax.Array, query_start_loc: jax.Array, k_block_tables: jax.Array, request_distribution: jax.Array, cache: jax.Array, rope_cache: jax.Array, *, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int)` — [`L105`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L105) — CSA: NoPE and RoPE in two arrays, state shares the NoPE buffer.
- <a id="_compressor_jax_hca"></a>`_compressor_jax_hca(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, norm_weight: jax.Array, cos_sin_cache: jax.Array, positions: jax.Array, state_block_tables: jax.Array, query_start_loc: jax.Array, k_block_tables: jax.Array, request_distribution: jax.Array, cache: jax.Array, state_cache: jax.Array, *, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int)` — [`L155`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L155) — HCA: no RoPE array, and the state lives on a CSA NoPE array.
- <a id="_compressor_jax_indexer"></a>`_compressor_jax_indexer(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, norm_weight: jax.Array, cos_sin_cache: jax.Array, positions: jax.Array, state_block_tables: jax.Array, query_start_loc: jax.Array, k_block_tables: jax.Array, request_distribution: jax.Array, cache: jax.Array, *, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int)` — [`L205`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L205) — Lightning indexer: one array holds the SEQ_ALONG_LANE records and state.
- <a id="_run_compressor"></a>`_run_compressor(hidden_states: jax.Array, wkv_wgate: jax.Array, ape: jax.Array, norm_weight: jax.Array, cos_sin_cache: jax.Array, positions: jax.Array, state_block_tables: jax.Array, query_start_loc: jax.Array, k_block_tables: jax.Array, request_distribution: jax.Array, cache: jax.Array, rope_cache: jax.Array | None, state_cache: jax.Array | None, *, state_block_size: int, head_dim: int, compress_ratio: int, overlap: bool, rms_eps: float, quant_block: int, seq_along_lane: bool = False)` — [`L54`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L54) — Shared body of the three op variants, for CSA compressor, HCA compressor, — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)

## Module values
- <a id="BATCH_AXIS"></a>`BATCH_AXIS` — [`L51`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L51)
- <a id="_compressor_op_cache"></a>`_compressor_op_cache` — [`L47`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L47)
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.py#L45)

