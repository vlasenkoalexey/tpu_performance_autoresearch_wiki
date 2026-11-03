---
title: 'Module: src/vllm_torchtpu/layers/core/attention_metadata.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/attention_metadata.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.attention_metadata`/
symbols:
  AttentionMetadataBuilder.build: AttentionMetadataBuilder#build().
  AttentionMetadata: AttentionMetadata#
  stage_block_table_uploads: stage_block_table_uploads().
  AttentionMetadataBuilder._block_table_geometry: AttentionMetadataBuilder#_block_table_geometry().
  AttentionMetadata.request_distribution: AttentionMetadata#request_distribution.
  stage_h2d_upload: stage_h2d_upload().
  AttentionMetadata.seq_lens: AttentionMetadata#seq_lens.
  AttentionMetadata.query_start_loc: AttentionMetadata#query_start_loc.
  AttentionMetadata.block_tables: AttentionMetadata#block_tables.
  AttentionMetadataBuilder._mamba_row_plan: AttentionMetadataBuilder#_mamba_row_plan().
  AttentionMetadataBuilderContext: AttentionMetadataBuilderContext#
  AttentionMetadataBuilderContext.use_max_model_len: AttentionMetadataBuilderContext#use_max_model_len.
  AttentionMetadataBuilderContext.seq_lens: AttentionMetadataBuilderContext#seq_lens.
  AttentionMetadataBuilderContext.position_ids_override: AttentionMetadataBuilderContext#position_ids_override.
  AttentionMetadataBuilderContext.mamba_ckpt_window: AttentionMetadataBuilderContext#mamba_ckpt_window.
  AttentionMetadataBuilderContext.sequence_layout_descriptor: AttentionMetadataBuilderContext#sequence_layout_descriptor.
  AttentionMetadataBuilder.target_block_size: AttentionMetadataBuilder#target_block_size.
  AttentionMetadata.input_positions: AttentionMetadata#input_positions.
  AttentionMetadataBuilderContext.query_start_loc: AttentionMetadataBuilderContext#query_start_loc.
  AttentionMetadataBuilderContext.mamba_state_indices: AttentionMetadataBuilderContext#mamba_state_indices.
  AttentionMetadata.sequence_layout_kind: AttentionMetadata#sequence_layout_kind.
  AttentionMetadataBuilderContext.num_reqs: AttentionMetadataBuilderContext#num_reqs.
  AttentionMetadataBuilderContext.start_index: AttentionMetadataBuilderContext#start_index.
  AttentionMetadataBuilderContext.request_distribution: AttentionMetadataBuilderContext#request_distribution.
  AttentionMetadataBuilder: AttentionMetadataBuilder#
  zeros_h2d_source: zeros_h2d_source().
  attention_block_table_width: attention_block_table_width().
  AttentionMetadata.mamba_state_indices: AttentionMetadata#mamba_state_indices.
  AttentionMetadata.sequence_layout_protocol: AttentionMetadata#sequence_layout_protocol.
  AttentionMetadata.mamba_slot_read_offsets: AttentionMetadata#mamba_slot_read_offsets.
  AttentionMetadata.mamba_request_distribution: AttentionMetadata#mamba_request_distribution.
  AttentionMetadataBuilderContext.staged_block_tables: AttentionMetadataBuilderContext#staged_block_tables.
  AttentionMetadataBuilder.kv_cache_group_id: AttentionMetadataBuilder#kv_cache_group_id.
  AttentionMetadataBuilder.is_mamba_group: AttentionMetadataBuilder#is_mamba_group.
  _staged_walk_products_compiled: _staged_walk_products_compiled().
  AttentionMetadata.mamba_ckpt_indices: AttentionMetadata#mamba_ckpt_indices.
  AttentionMetadataBuilderContext.unified_mamba_state_indices: AttentionMetadataBuilderContext#unified_mamba_state_indices.
  AttentionMetadata.sequence_layout_version: AttentionMetadata#sequence_layout_version.
  AttentionMetadataBuilderContext.mamba_slot_read_offsets: AttentionMetadataBuilderContext#mamba_slot_read_offsets.
  AttentionMetadataBuilderContext.mamba_request_distribution: AttentionMetadataBuilderContext#mamba_request_distribution.
  AttentionMetadataBuilderContext.mamba_row_plans: AttentionMetadataBuilderContext#mamba_row_plans.
  _staged_walk_products: _staged_walk_products().
  stage_h2d_upload.release_cb: stage_h2d_upload().release_cb().
  AttentionMetadataBuilder.runner: AttentionMetadataBuilder#runner.
  AttentionMetadataBuilderContext.staged_mamba_products: AttentionMetadataBuilderContext#staged_mamba_products.
  _DEFAULT_MAX_H2D_BUFFERS: _DEFAULT_MAX_H2D_BUFFERS.
  _noop_release: _noop_release().
  AttentionMetadata.query_start_loc_cpu: AttentionMetadata#query_start_loc_cpu.
  AttentionMetadata.seq_lens_cpu: AttentionMetadata#seq_lens_cpu.
  AttentionMetadataBuilder.__init__: AttentionMetadataBuilder#__init__().
---
# Module: [`src/vllm_torchtpu/layers/core/attention_metadata.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py)

## Classes
### <a id="AttentionMetadata"></a>`AttentionMetadata`
- def: [`src/vllm_torchtpu/layers/core/attention_metadata.py:80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L80) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- signature: `class AttentionMetadata:`
- members:
  - <a id="AttentionMetadata.block_tables"></a>`block_tables` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L84) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadata.input_positions"></a>`input_positions` — [`L82`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L82)
  - <a id="AttentionMetadata.mamba_ckpt_indices"></a>`mamba_ckpt_indices` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L111)
  - <a id="AttentionMetadata.mamba_request_distribution"></a>`mamba_request_distribution` — [`L121`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L121)
  - <a id="AttentionMetadata.mamba_slot_read_offsets"></a>`mamba_slot_read_offsets` — [`L107`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L107)
  - <a id="AttentionMetadata.mamba_state_indices"></a>`mamba_state_indices` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L97)
  - <a id="AttentionMetadata.query_start_loc"></a>`query_start_loc` — [`L88`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L88) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadata.query_start_loc_cpu"></a>`query_start_loc_cpu` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L126)
  - <a id="AttentionMetadata.request_distribution"></a>`request_distribution` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L90) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadata.seq_lens"></a>`seq_lens` — [`L86`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L86) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadata.seq_lens_cpu"></a>`seq_lens_cpu` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L127)
  - <a id="AttentionMetadata.sequence_layout_kind"></a>`sequence_layout_kind` — [`L122`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L122)
  - <a id="AttentionMetadata.sequence_layout_protocol"></a>`sequence_layout_protocol` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L123)
  - <a id="AttentionMetadata.sequence_layout_version"></a>`sequence_layout_version` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L124)
- uses (calls/refs, reference-scoped): [`SequenceLayoutKind`](sequence_layout.md#SequenceLayoutKind), [`ALL`](sequence_layout.md#SequenceLayoutKind.ALL), [`DEFAULT_SEQUENCE_LAYOUT_PROTOCOL`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_PROTOCOL)
- used by: [`_dummy_run`](../../runner/tpu_runner.md#TPUModelRunner._dummy_run), [`forward`](../../models/vllm/kimi_k3/attention.md#KimiDeltaAttention.forward), [`_build_draft_attn_metadata`](../../spec_decode/eagle3.md#Eagle3Proposer._build_draft_attn_metadata), [`forward`](../adapter/attention.md#PallasAttentionBackendImpl.forward), [`build`](attention_metadata.md#AttentionMetadataBuilder.build), [`_pallas_rpa_kernel_impl`](../adapter/attention.md#_pallas_rpa_kernel_impl), [`_core_attention_pooled`](../../models/vllm/kimi_k3/attention.md#KimiDeltaAttention._core_attention_pooled), [`_dummy_kv_update_inputs`](../../spec_decode/dflash.md#DFlashProposer._dummy_kv_update_inputs), [`make_attention_metadata`](../../experimental/export/universal_adapter.md#make_attention_metadata), [`_dummy_precompute_and_update_kv_cache`](../../spec_decode/dflash.md#DFlashProposer._dummy_precompute_and_update_kv_cache), [`mla_attention_core_tpu`](../adapter/attention.md#PallasMLAttentionBackendImpl.mla_attention_core_tpu), [`forward_oot`](../adapter/custom_ops/mla_attention_op.md#VllmTPUSparseAttnIndexer.forward_oot), [`attention`](attention_interface.md#attention), [`_run_dcp_forward`](../adapter/attention.md#PallasAttentionBackendImpl._run_dcp_forward), [`forward`](../adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.md#VllmDeepseekCompressor.forward), [`attention_bundled`](attention_interface.md#attention_bundled), [`_pallas_rpa_kernel_default_bundled`](../adapter/attention.md#_pallas_rpa_kernel_default_bundled), [`build_attention_metadata_for_layers`](../../runner/tpu_runner.md#TPUModelRunner.build_attention_metadata_for_layers), [`_build_attention_metadata`](../../runner/tpu_runner.md#TPUModelRunner._build_attention_metadata), [`mla_attention`](attention_interface.md#mla_attention), [`_target_draft_attn_metadata`](../../spec_decode/eagle3.md#Eagle3Proposer._target_draft_attn_metadata), [`forward`](../adapter/custom_ops/deepseek_v4/deepseek_v4_indexer.md#VllmDeepseekV4Indexer.forward), [`_tpu_precompute_and_update_kv_cache`](../../spec_decode/dflash.md#DFlashProposer._tpu_precompute_and_update_kv_cache), [`_build_draft_layer_metadata`](../../spec_decode/dflash.md#DFlashProposer._build_draft_layer_metadata), [`_metadata`](../../models/vllm/kimi_k3/attention.md#KimiDeltaAttention._metadata), [`_dummy_kv_input_cache`](../../spec_decode/dflash.md#DFlashProposer._dummy_kv_input_cache), [`forward_mha`](../adapter/attention.md#PallasMLAttentionBackendImpl.forward_mha), [`forward_mqa`](../adapter/attention.md#PallasMLAttentionBackendImpl.forward_mqa)

### <a id="AttentionMetadataBuilder"></a>`AttentionMetadataBuilder`
- def: [`src/vllm_torchtpu/layers/core/attention_metadata.py:333`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L333)
- doc: Single shared metadata builder for every TPU attention group.
- signature: `class AttentionMetadataBuilder(BaseAttentionMetadataBuilder):`
- members:
  - <a id="AttentionMetadataBuilder._block_table_geometry"></a>`_block_table_geometry(self, ctx: AttentionMetadataBuilderContext)` — [`L398`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L398) — The (block_table_obj, target_num_blocks) this group's build() uses. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadataBuilder._mamba_row_plan"></a>`_mamba_row_plan(self, ctx: AttentionMetadataBuilderContext, target_num_blocks: int)` — [`L353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L353) — Row offsets into a mamba block table, cached and shared across groups. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadataBuilder.build"></a>`build(self, common_prefix_len, common_attn_metadata, fast_build=False)` — [`L441`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L441) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AttentionMetadataBuilder.is_mamba_group"></a>`is_mamba_group` — [`L342`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L342)
  - <a id="AttentionMetadataBuilder.kv_cache_group_id"></a>`kv_cache_group_id` — [`L341`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L341)
  - <a id="AttentionMetadataBuilder.runner"></a>`runner` — [`L340`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L340)
  - <a id="AttentionMetadataBuilder.target_block_size"></a>`target_block_size` — [`L343`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L343)
- protocol/private: <a id="AttentionMetadataBuilder.__init__"></a>`__init__`[`L336`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L336)
- uses (calls/refs, reference-scoped): [`AttentionMetadata`](attention_metadata.md#AttentionMetadata), [`request_distribution`](attention_metadata.md#AttentionMetadata.request_distribution), [`stage_h2d_upload`](attention_metadata.md#stage_h2d_upload), [`query_start_loc`](attention_metadata.md#AttentionMetadata.query_start_loc), [`seq_lens`](attention_metadata.md#AttentionMetadata.seq_lens), [`block_tables`](attention_metadata.md#AttentionMetadata.block_tables), [`AttentionMetadataBuilderContext`](attention_metadata.md#AttentionMetadataBuilderContext), [`seq_lens`](attention_metadata.md#AttentionMetadataBuilderContext.seq_lens), [`use_max_model_len`](attention_metadata.md#AttentionMetadataBuilderContext.use_max_model_len), [`mamba_ckpt_window`](attention_metadata.md#AttentionMetadataBuilderContext.mamba_ckpt_window), [`input_positions`](attention_metadata.md#AttentionMetadata.input_positions), [`sequence_layout_kind`](attention_metadata.md#AttentionMetadata.sequence_layout_kind), [`zeros_h2d_source`](attention_metadata.md#zeros_h2d_source), [`attention_block_table_width`](attention_metadata.md#attention_block_table_width), [`mamba_state_indices`](attention_metadata.md#AttentionMetadata.mamba_state_indices), [`sequence_layout_protocol`](attention_metadata.md#AttentionMetadata.sequence_layout_protocol), [`mamba_request_distribution`](attention_metadata.md#AttentionMetadata.mamba_request_distribution), [`mamba_slot_read_offsets`](attention_metadata.md#AttentionMetadata.mamba_slot_read_offsets), [`mamba_ckpt_indices`](attention_metadata.md#AttentionMetadata.mamba_ckpt_indices), [`mamba_row_plans`](attention_metadata.md#AttentionMetadataBuilderContext.mamba_row_plans), [`sequence_layout_version`](attention_metadata.md#AttentionMetadata.sequence_layout_version)
- used by: [`initialize_kv_cache`](../../runner/kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`_initialize_unified_kv_cache`](../../runner/kv_cache_manager.md#KVCacheManager._initialize_unified_kv_cache), [`build_attention_metadata_for_layers`](../../runner/tpu_runner.md#TPUModelRunner.build_attention_metadata_for_layers), [`_build_attention_metadata`](../../runner/tpu_runner.md#TPUModelRunner._build_attention_metadata)

### <a id="AttentionMetadataBuilderContext"></a>`AttentionMetadataBuilderContext`
- def: [`src/vllm_torchtpu/layers/core/attention_metadata.py:131`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L131) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- doc: Per-call inputs the TPU metadata builder reads from the runner.
- signature: `class AttentionMetadataBuilderContext:`
- members:
  - <a id="AttentionMetadataBuilderContext.mamba_ckpt_window"></a>`mamba_ckpt_window` — [`L159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L159)
  - <a id="AttentionMetadataBuilderContext.mamba_request_distribution"></a>`mamba_request_distribution` — [`L160`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L160)
  - <a id="AttentionMetadataBuilderContext.mamba_row_plans"></a>`mamba_row_plans` — [`L176`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L176)
  - <a id="AttentionMetadataBuilderContext.mamba_slot_read_offsets"></a>`mamba_slot_read_offsets` — [`L155`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L155)
  - <a id="AttentionMetadataBuilderContext.mamba_state_indices"></a>`mamba_state_indices` — [`L152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L152)
  - <a id="AttentionMetadataBuilderContext.num_reqs"></a>`num_reqs` — [`L142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L142)
  - <a id="AttentionMetadataBuilderContext.position_ids_override"></a>`position_ids_override` — [`L148`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L148)
  - <a id="AttentionMetadataBuilderContext.query_start_loc"></a>`query_start_loc` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L146)
  - <a id="AttentionMetadataBuilderContext.request_distribution"></a>`request_distribution` — [`L147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L147)
  - <a id="AttentionMetadataBuilderContext.seq_lens"></a>`seq_lens` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L145)
  - <a id="AttentionMetadataBuilderContext.sequence_layout_descriptor"></a>`sequence_layout_descriptor` — [`L167`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L167)
  - <a id="AttentionMetadataBuilderContext.staged_block_tables"></a>`staged_block_tables` — [`L182`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L182)
  - <a id="AttentionMetadataBuilderContext.staged_mamba_products"></a>`staged_mamba_products` — [`L186`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L186)
  - <a id="AttentionMetadataBuilderContext.start_index"></a>`start_index` — [`L143`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L143)
  - <a id="AttentionMetadataBuilderContext.unified_mamba_state_indices"></a>`unified_mamba_state_indices` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L166)
  - <a id="AttentionMetadataBuilderContext.use_max_model_len"></a>`use_max_model_len` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L144) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- uses (calls/refs, reference-scoped): [`DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR), [`SequenceLayoutDescriptor`](sequence_layout.md#SequenceLayoutDescriptor)
- used by: [`execute_model`](../../runner/tpu_runner.md#TPUModelRunner.execute_model), [`_dummy_run`](../../runner/tpu_runner.md#TPUModelRunner._dummy_run), [`_build_dp_dummy_draft`](../../spec_decode/eagle3.md#Eagle3Proposer._build_dp_dummy_draft), [`propose`](../../spec_decode/eagle3.md#Eagle3Proposer.propose), [`_build_draft_attn_metadata`](../../spec_decode/eagle3.md#Eagle3Proposer._build_draft_attn_metadata), [`_attn_metadata_builder_ctx`](../../runner/tpu_runner.md#TPUModelRunner._attn_metadata_builder_ctx), [`_prepare_draft_inputs`](../../spec_decode/eagle3.md#Eagle3Proposer._prepare_draft_inputs), [`_prepare_dflash_inputs`](../../spec_decode/dflash.md#DFlashProposer._prepare_dflash_inputs), [`stage_block_table_uploads`](attention_metadata.md#stage_block_table_uploads), [`_build_attn_metadata_for_draft`](../../spec_decode/dflash.md#DFlashProposer._build_attn_metadata_for_draft), [`_loop_step_attn_inputs`](../../spec_decode/eagle3.md#Eagle3Proposer._loop_step_attn_inputs), [`_build_draft_attn_metadata`](../../spec_decode/dflash.md#DFlashProposer._build_draft_attn_metadata), [`_block_table_geometry`](attention_metadata.md#AttentionMetadataBuilder._block_table_geometry), [`build_attention_metadata_for_layers`](../../runner/tpu_runner.md#TPUModelRunner.build_attention_metadata_for_layers), [`_build_attention_metadata`](../../runner/tpu_runner.md#TPUModelRunner._build_attention_metadata), [`attn_ctx`](../../spec_decode/utils.md#DraftChunkInputs.attn_ctx), [`_target_draft_attn_metadata`](../../spec_decode/eagle3.md#Eagle3Proposer._target_draft_attn_metadata), [`logger`](../../spec_decode/utils.md#logger), [`_mamba_row_plan`](attention_metadata.md#AttentionMetadataBuilder._mamba_row_plan), [`_mamba_state_index_groups`](../../runner/tpu_runner.md#TPUModelRunner._mamba_state_index_groups), [`_chunk_num_reqs_device`](../../spec_decode/dflash.md#DFlashProposer._chunk_num_reqs_device)

## Functions
- <a id="_noop_release"></a>`_noop_release()` — [`L263`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L263)
- <a id="_staged_walk_products"></a>`_staged_walk_products(staged_dev: torch.Tensor, seq_lens: torch.Tensor, table_geom: tuple, mamba_geom: tuple, ckpt_window: int)` — [`L189`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L189) — Splits the staged flat block-table buffer into per-group tables and
- <a id="_staged_walk_products_compiled"></a>`_staged_walk_products_compiled(staged_dev: torch.Tensor, seq_lens: torch.Tensor, table_geom: tuple, mamba_geom: tuple, ckpt_window: int)` — [`L224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L224) — One device program for everything the metadata walk consumes:
- <a id="attention_block_table_width"></a>`attention_block_table_width(block_table: Any, spec: KVCacheSpec, vllm_config: Any, model_len: int | None = None)` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L43) — Match allocated, rank-local kernel page ordinals, including block splits.
- <a id="stage_h2d_upload.release_cb"></a>`release_cb()` — [`L285`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L285)
- <a id="stage_block_table_uploads"></a>`stage_block_table_uploads(runner: Any, ctx: AttentionMetadataBuilderContext, num_reqs_padded: int, gids: set[int] | None = None)` — [`L562`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L562) — One batched H2D transfer for every block table a walk will build. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="stage_h2d_upload"></a>`stage_h2d_upload(runner: Any, host: torch.Tensor)` — [`L267`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L267) — `host.to(runner.device, non_blocking=True)`, keeping `host` alive until
- <a id="zeros_h2d_source"></a>`zeros_h2d_source(runner: Any, numel: int, dtype: torch.dtype = torch.int32, max_buffers: int = _DEFAULT_MAX_H2D_BUFFERS)` — [`L297`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L297) — Return a zeroed 1D CPU buffer of `(numel, dtype)`, recycling one

## Module values
- <a id="_DEFAULT_MAX_H2D_BUFFERS"></a>`_DEFAULT_MAX_H2D_BUFFERS` — [`L260`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/attention_metadata.py#L260)

