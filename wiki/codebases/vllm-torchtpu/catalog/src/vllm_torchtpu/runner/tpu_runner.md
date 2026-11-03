---
title: 'Module: src/vllm_torchtpu/runner/tpu_runner.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/tpu_runner.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.tpu_runner`/
symbols:
  TPUModelRunner.device: TPUModelRunner#device.
  TPUModelRunner.execute_model: TPUModelRunner#execute_model().
  TPUModelRunner.sample_tokens: TPUModelRunner#sample_tokens().
  TPUModelRunner._dummy_run: TPUModelRunner#_dummy_run().
  logger: logger.
  TPUModelRunner.position_ids: TPUModelRunner#position_ids.
  TPUModelRunner.speculative_config: TPUModelRunner#speculative_config.
  TPUModelRunner._sample_spec_verify_chunk: TPUModelRunner#_sample_spec_verify_chunk().
  TPUModelRunner._attn_metadata_builder_ctx: TPUModelRunner#_attn_metadata_builder_ctx.
  TPUModelRunner.num_reqs_most_model_len: TPUModelRunner#num_reqs_most_model_len.
  TPUModelRunner._prepare_inputs: TPUModelRunner#_prepare_inputs().
  TPUModelRunner._collect_mamba_state_seed_copies: TPUModelRunner#_collect_mamba_state_seed_copies().
  TPUModelRunner._precompile_rejection_sampler: TPUModelRunner#_precompile_rejection_sampler().
  TPUModelRunner.capture_model: TPUModelRunner#capture_model().
  TPUModelRunner.num_tokens_paddings: TPUModelRunner#num_tokens_paddings.
  TPUModelRunner.encoder_cudagraph_manager: TPUModelRunner#encoder_cudagraph_manager.
  TPUModelRunner._initialize_attention_kernels: TPUModelRunner#_initialize_attention_kernels().
  TPUModelRunner._pool_chunk: TPUModelRunner#_pool_chunk().
  TPUModelRunner._precompile_backbone: TPUModelRunner#_precompile_backbone().
  TPUModelRunner.max_num_reqs: TPUModelRunner#max_num_reqs.
  TPUModelRunner._precompile_pooler_subgraphs: TPUModelRunner#_precompile_pooler_subgraphs().
  TPUModelRunner.num_reqs_max_model_len: TPUModelRunner#num_reqs_max_model_len.
  TPUModelRunner._update_states: TPUModelRunner#_update_states().
  TPUModelRunner._precompile_structured_decoding: TPUModelRunner#_precompile_structured_decoding().
  TPUModelRunner._pre_async_results: TPUModelRunner#_pre_async_results.
  TPUModelRunner.max_num_tokens: TPUModelRunner#max_num_tokens.
  TPUModelRunner._attention_schedule_capacity: TPUModelRunner#_attention_schedule_capacity().
  TPUModelRunner._pp_wave: TPUModelRunner#_pp_wave.
  TPUModelRunner._add_pipeline_chunk_buckets: TPUModelRunner#_add_pipeline_chunk_buckets().
  TPUModelRunner.start_phased_profiling: TPUModelRunner#start_phased_profiling().
  TPUModelRunner._precompile_spec_logprobs: TPUModelRunner#_precompile_spec_logprobs().
  TPUModelRunner._warmup_spec_decode: TPUModelRunner#_warmup_spec_decode().
  TPUModelRunner.profile_run: TPUModelRunner#profile_run().
  TPUModelRunner._warmup_spec_decode_cleanup: TPUModelRunner#_warmup_spec_decode_cleanup().
  TPUModelRunner._precompile_timed: TPUModelRunner#_precompile_timed().
  TPUModelRunner._mtp_prefill_only: TPUModelRunner#_mtp_prefill_only.
  TPUModelRunner._run_dp_idle_pairing: TPUModelRunner#_run_dp_idle_pairing().
  TPUModelRunner._precompile_compute_top_tokens: TPUModelRunner#_precompile_compute_top_tokens().
  TPUModelRunner._precompile_sample_from_logits: TPUModelRunner#_precompile_sample_from_logits().
  TPUModelRunner._warmup_mtp_prefill: TPUModelRunner#_warmup_mtp_prefill().
  TPUModelRunner._warmup_handoff_forwards: TPUModelRunner#_warmup_handoff_forwards().
  TPUModelRunner._warmup_spec_batch: TPUModelRunner#_warmup_spec_batch().
  TPUModelRunner.drafter: TPUModelRunner#drafter.
  TPUModelRunner.kv_cache_config: TPUModelRunner#kv_cache_config.
  TPUModelRunner._precompile_substitute_placeholder_token: TPUModelRunner#_precompile_substitute_placeholder_token().
  TPUModelRunner._precompile_sampling_subgraphs: TPUModelRunner#_precompile_sampling_subgraphs().
  TPUModelRunner.profile_pipeline_chunks: TPUModelRunner#profile_pipeline_chunks().
  TPUModelRunner._precompile_min_tokens_mask: TPUModelRunner#_precompile_min_tokens_mask().
  TPUModelRunner.pp_handoff_hbm_reserve_bytes: TPUModelRunner#pp_handoff_hbm_reserve_bytes().
  TPUModelRunner._precompile_mamba_state_seed_copies: TPUModelRunner#_precompile_mamba_state_seed_copies().
  TPUModelRunner._update_num_xla_graphs: TPUModelRunner#_update_num_xla_graphs().
  TPUModelRunner.num_reqs_paddings: TPUModelRunner#num_reqs_paddings.
  TPUModelRunner._num_static_verify_reqs: TPUModelRunner#_num_static_verify_reqs.
  TPUModelRunner.model: TPUModelRunner#model.
  TPUModelRunner.most_model_len: TPUModelRunner#most_model_len.
  TPUModelRunner._precompile_compute_selected_logits: TPUModelRunner#_precompile_compute_selected_logits().
  TPUModelRunner.kv_cache_dtype: TPUModelRunner#kv_cache_dtype.
  TPUModelRunner.mamba_slot_read_offsets: TPUModelRunner#mamba_slot_read_offsets.
  TPUModelRunner._pp_intermediate_tensors: TPUModelRunner#_pp_intermediate_tensors().
  TPUModelRunner: TPUModelRunner#
  TPUModelRunner._warmup_one_spec_request: TPUModelRunner#_warmup_one_spec_request().
  TPUModelRunner._is_async_drafter: TPUModelRunner#_is_async_drafter().
  TPUModelRunner._precompile_dense_kv_cache_block_copies: TPUModelRunner#_precompile_dense_kv_cache_block_copies().
  TPUModelRunner._settle_draft_placeholders_for_min_tokens: TPUModelRunner#_settle_draft_placeholders_for_min_tokens().
  TPUModelRunner._precompile_gather_logprobs: TPUModelRunner#_precompile_gather_logprobs().
  TPUModelRunner._resolve_static_pooler: TPUModelRunner#_resolve_static_pooler().
  TPUModelRunner._precompile_mamba_rollback_helpers: TPUModelRunner#_precompile_mamba_rollback_helpers().
  TPUModelRunner.rejection_sampler: TPUModelRunner#rejection_sampler.
  TPUModelRunner._modify_prev_results: TPUModelRunner#_modify_prev_results().
  TPUModelRunner.max_num_blocks_per_req: TPUModelRunner#max_num_blocks_per_req.
  TPUModelRunner.post_profile_hbm_reserves: TPUModelRunner#post_profile_hbm_reserves().
  TPUModelRunner.mesh: TPUModelRunner#mesh.
  TPUModelRunner.build_attention_metadata_for_layers: TPUModelRunner#build_attention_metadata_for_layers().
  TPUModelRunner._apply_kv_cache_block_copies: TPUModelRunner#_apply_kv_cache_block_copies().
  TPUModelRunner._attention_kernel_shapes: TPUModelRunner#_attention_kernel_shapes().
  TPUModelRunner._precompile_compute_logits_from_hidden_states: TPUModelRunner#_precompile_compute_logits_from_hidden_states().
  TPUModelRunner._spec_warmup_bucket_grid: TPUModelRunner#_spec_warmup_bucket_grid().
  TPUModelRunner._build_attention_metadata: TPUModelRunner#_build_attention_metadata().
  TPUModelRunner._warmup_one_mtp_prefill: TPUModelRunner#_warmup_one_mtp_prefill().
  TPUModelRunner._dp_coordinated_step: TPUModelRunner#_dp_coordinated_step().
  TPUModelRunner._execute_dp_mm_encoder: TPUModelRunner#_execute_dp_mm_encoder().
  TPUModelRunner._backbone_dummy_runs: TPUModelRunner#_backbone_dummy_runs().
  _get_padded_token_len: _get_padded_token_len().
  TPUModelRunner._reset_read_offsets_for_new_requests: TPUModelRunner#_reset_read_offsets_for_new_requests().
  TPUModelRunner._precompile_top_token_verify: TPUModelRunner#_precompile_top_token_verify().
  TPUModelRunner._async_drafter: TPUModelRunner#_async_drafter().
  TPUModelRunner._copy_mamba_state_blocks: TPUModelRunner#_copy_mamba_state_blocks().
  _pp_step: _pp_step().
  TPUModelRunner._pp_topk_buffer: TPUModelRunner#_pp_topk_buffer.
  TPUModelRunner._mask_min_tokens: TPUModelRunner#_mask_min_tokens().
  TPUModelRunner._build_mamba_state_indices: TPUModelRunner#_build_mamba_state_indices().
  TPUModelRunner._verify_logits_paddings: TPUModelRunner#_verify_logits_paddings().
  TPUModelRunner.may_reinitialize_input_batch: TPUModelRunner#may_reinitialize_input_batch().
  TPUModelRunner._hidden_states_dtype: TPUModelRunner#_hidden_states_dtype.
  TPUModelRunner.spec_decode_manager: TPUModelRunner#spec_decode_manager.
  TPUModelRunner.structured_decoding_manager: TPUModelRunner#structured_decoding_manager.
  TPUModelRunner._prepare_async_token_substitution_indices: TPUModelRunner#_prepare_async_token_substitution_indices().
  TPUModelRunner._apply_async_token_substitution: TPUModelRunner#_apply_async_token_substitution().
  TPUModelRunner._min_tokens_batch_state: TPUModelRunner#_min_tokens_batch_state().
  TPUModelRunner._dummy_logits: TPUModelRunner#_dummy_logits().
  TPUModelRunner._sample_tokens_pp_intermediate_stage: TPUModelRunner#_sample_tokens_pp_intermediate_stage().
  TPUModelRunner.num_blocks_per_most_len_req: TPUModelRunner#num_blocks_per_most_len_req.
  TPUModelRunner.get_finished_kv_transfers: TPUModelRunner#get_finished_kv_transfers().
  TPUModelRunner._unified_kv_layout: TPUModelRunner#_unified_kv_layout.
  TPUModelRunner._stage_timing: TPUModelRunner#_stage_timing.
  TPUModelRunner.kv_cache_raw_tensors: TPUModelRunner#kv_cache_raw_tensors.
  TPUModelRunner.is_pooling_model: TPUModelRunner#is_pooling_model.
  TPUModelRunner.take_draft_token_ids: TPUModelRunner#take_draft_token_ids().
  TPUModelRunner._static_pooler_reason: TPUModelRunner#_static_pooler_reason.
  TPUModelRunner.num_xla_graphs: TPUModelRunner#num_xla_graphs.
  _validate_libtpu_version: _validate_libtpu_version().
  TPUModelRunner.kv_connector_no_forward: TPUModelRunner#kv_connector_no_forward().
  TPUModelRunner._relayout_tables: TPUModelRunner#_relayout_tables().
  TPUModelRunner._reorder_batch_for_rpa: TPUModelRunner#_reorder_batch_for_rpa().
  TPUModelRunner._init_mamba_slot_pool: TPUModelRunner#_init_mamba_slot_pool().
  TPUModelRunner._apply_dense_kv_cache_block_copies: TPUModelRunner#_apply_dense_kv_cache_block_copies().
  TPUModelRunner._cached_pre_next_tokens_indices: TPUModelRunner#_cached_pre_next_tokens_indices.
  TPUModelRunner._assemble_async_spec_substitution: TPUModelRunner#_assemble_async_spec_substitution().
  TPUModelRunner._pp_forward_rows: TPUModelRunner#_pp_forward_rows().
  TPUModelRunner._dp_num_tokens_across_dp: TPUModelRunner#_dp_num_tokens_across_dp().
  TPUModelRunner._mamba_state_index_groups: TPUModelRunner#_mamba_state_index_groups().
  TPUModelRunner._check_draft_buckets: TPUModelRunner#_check_draft_buckets().
  TPUModelRunner._greedy_top_tokens_this_step: TPUModelRunner#_greedy_top_tokens_this_step().
  TPUModelRunner._pp_is_last: TPUModelRunner#_pp_is_last.
  TPUModelRunner._greedy_head_owner: TPUModelRunner#_greedy_head_owner.
  TPUModelRunner.get_kv_cache_spec: TPUModelRunner#get_kv_cache_spec().
  TPUModelRunner._mamba_state_block_size: TPUModelRunner#_mamba_state_block_size.
  TPUModelRunner._dp_lockstep_enabled: TPUModelRunner#_dp_lockstep_enabled().
  TPUModelRunner.lora_manager: TPUModelRunner#lora_manager.
  TPUModelRunner._topk_candidate_blocks: TPUModelRunner#_topk_candidate_blocks().
  TPUModelRunner._sampler_topk_candidates: TPUModelRunner#_sampler_topk_candidates().
  TPUModelRunner.input_ids_cpu: TPUModelRunner#input_ids_cpu.
  TPUModelRunner.query_start_loc_np: TPUModelRunner#query_start_loc_np.
  TPUModelRunner.execute_model_state: TPUModelRunner#execute_model_state.
  TPUModelRunner._pad_to_bucket: TPUModelRunner#_pad_to_bucket().
  TPUModelRunner._sync_one_replicated_draft: TPUModelRunner#_sync_one_replicated_draft().
  TPUModelRunner._record_input_staging_fence: TPUModelRunner#_record_input_staging_fence().
  TPUModelRunner._run_dp_dummy_chunk: TPUModelRunner#_run_dp_dummy_chunk().
  TPUModelRunner._spec_verify_bucket_reachable: TPUModelRunner#_spec_verify_bucket_reachable().
  TPUModelRunner.widest_table: TPUModelRunner#widest_table().
  TPUModelRunner.block_table_cpu: TPUModelRunner#block_table_cpu.
  TPUModelRunner.enforce_eager: TPUModelRunner#enforce_eager.
  _rotate_precompile_sweep: _rotate_precompile_sweep().
  TPUModelRunner._pool_block_split: TPUModelRunner#_pool_block_split.
  TPUModelRunner._is_dspark_pd_producer: TPUModelRunner#_is_dspark_pd_producer.
  TPUModelRunner._pp_intermediate_template: TPUModelRunner#_pp_intermediate_template.
  TPUModelRunner.bm_pool_layout: TPUModelRunner#bm_pool_layout.
  TPUModelRunner._static_pooler_spec: TPUModelRunner#_static_pooler_spec.
  TPUModelRunner._min_tokens: TPUModelRunner#_min_tokens.
  TPUModelRunner.stop_phased_profiling: TPUModelRunner#stop_phased_profiling().
  TPUModelRunner._flush_disjoint_async_results: TPUModelRunner#_flush_disjoint_async_results().
  TPUModelRunner._count_input_chunks: TPUModelRunner#_count_input_chunks().
  TPUModelRunner.lora_slot_write_hbm_bytes: TPUModelRunner#lora_slot_write_hbm_bytes().
  TPUModelRunner._check_attention_schedule: TPUModelRunner#_check_attention_schedule().
  TPUModelRunner._token_padding_update: TPUModelRunner#_token_padding_update().
  TPUModelRunner.sample_from_logits: TPUModelRunner#sample_from_logits().
  _get_req_paddings: _get_req_paddings().
  _get_padded_num_reqs_with_upper_limit: _get_padded_num_reqs_with_upper_limit().
  ExecuteModelState.top_tokens: ExecuteModelState#top_tokens.
  TPUModelRunner.vocab_size: TPUModelRunner#vocab_size.
  TPUModelRunner._mamba_copy_plan: TPUModelRunner#_mamba_copy_plan.
  TPUModelRunner.phase_based_profiler: TPUModelRunner#phase_based_profiler.
  TPUModelRunner._upload_unless_unchanged: TPUModelRunner#_upload_unless_unchanged().
  TPUModelRunner._update_mamba_slot_read_offsets: TPUModelRunner#_update_mamba_slot_read_offsets().
  TPUModelRunner._refresh_smem_request_caps: TPUModelRunner#_refresh_smem_request_caps().
  TPUModelRunner._pp_take_topk_indices: TPUModelRunner#_pp_take_topk_indices().
  TPUModelRunner.compute_selected_logits: TPUModelRunner#compute_selected_logits().
  TPUModelRunner.sample_from_logits_func: TPUModelRunner#sample_from_logits_func.
  TPUModelRunner._hybrid_uniform_page_size_bytes: TPUModelRunner#_hybrid_uniform_page_size_bytes.
  TPUModelRunner._kv_cache_bundle: TPUModelRunner#_kv_cache_bundle.
  _rollback_offsets_seed_compiled: _rollback_offsets_seed_compiled.
  _rollback_offsets_migrate_compiled: _rollback_offsets_migrate_compiled.
  _rollback_offsets_migrate: _rollback_offsets_migrate().
  TPUModelRunner.maybe_wait_for_kv_save: TPUModelRunner#maybe_wait_for_kv_save().
  TPUModelRunner._dense_kv_copy_supported: TPUModelRunner#_dense_kv_copy_supported().
  TPUModelRunner._wait_input_staging_fence: TPUModelRunner#_wait_input_staging_fence().
  TPUModelRunner._profile_input: TPUModelRunner#_profile_input().
  TPUModelRunner._pp_outgoing_tensors: TPUModelRunner#_pp_outgoing_tensors().
  TPUModelRunner.compute_selected_top_tokens: TPUModelRunner#compute_selected_top_tokens().
  TPUModelRunner.compute_top_tokens_from_hidden_states: TPUModelRunner#compute_top_tokens_from_hidden_states().
  TPUModelRunner._attention_capacity: TPUModelRunner#_attention_capacity.
  TPUModelRunner.arange_np: TPUModelRunner#arange_np.
  TPUModelRunner._pcp_enabled: TPUModelRunner#_pcp_enabled.
  TPUModelRunner.query_start_loc_cpu: TPUModelRunner#query_start_loc_cpu.
  TPUModelRunner.kv_cache_manager: TPUModelRunner#kv_cache_manager.
  TPUModelRunner.tok_bucket: TPUModelRunner#tok_bucket().
  TPUModelRunner._sampler_applies_topk_topp: TPUModelRunner#_sampler_applies_topk_topp().
  _reset_read_offsets_compiled: _reset_read_offsets_compiled.
  _reset_read_offsets: _reset_read_offsets().
  _rollback_offsets_seed: _rollback_offsets_seed().
  _get_sequence_layout_planner_for_runner: _get_sequence_layout_planner_for_runner().
  TPUModelRunner._fence_spec_kv_under_token_copy: TPUModelRunner#_fence_spec_kv_under_token_copy().
  TPUModelRunner._profiler_world_size: TPUModelRunner#_profiler_world_size.
  TPUModelRunner._pp_is_first: TPUModelRunner#_pp_is_first.
  TPUModelRunner._mamba_slot_by_req_id: TPUModelRunner#_mamba_slot_by_req_id.
  TPUModelRunner._mamba_offset_seeded: TPUModelRunner#_mamba_offset_seeded.
  TPUModelRunner._dp_target_bucket: TPUModelRunner#_dp_target_bucket.
  TPUModelRunner.block_size: TPUModelRunner#block_size.
  TPUModelRunner._init_speculative_decoding: TPUModelRunner#_init_speculative_decoding().
  TPUModelRunner._truncate_rope_caches: TPUModelRunner#_truncate_rope_caches().
  TPUModelRunner._fresh_xla_graphs: TPUModelRunner#_fresh_xla_graphs().
  TPUModelRunner.initialize_kv_cache: TPUModelRunner#initialize_kv_cache().
  TPUModelRunner.get_kv_prewarm_shapes: TPUModelRunner#get_kv_prewarm_shapes().
  TPUModelRunner.prewarm_kv_offload_shape: TPUModelRunner#prewarm_kv_offload_shape().
  TPUModelRunner._build_mamba_copy_plan: TPUModelRunner#_build_mamba_copy_plan().
  TPUModelRunner._spec_seed_sources: TPUModelRunner#_spec_seed_sources().
  TPUModelRunner._flush_mamba_state_seed_copies: TPUModelRunner#_flush_mamba_state_seed_copies().
  TPUModelRunner._assemble_async_prefill_bootstrap: TPUModelRunner#_assemble_async_prefill_bootstrap().
  TPUModelRunner._execute_mm_encoder: TPUModelRunner#_execute_mm_encoder().
  TPUModelRunner._get_sampling_generator: TPUModelRunner#_get_sampling_generator().
  TPUModelRunner._read_offset_reset_scratch: TPUModelRunner#_read_offset_reset_scratch().
  TPUModelRunner._initialize_pallas_kernels: TPUModelRunner#_initialize_pallas_kernels().
  TPUModelRunner._initialize_quantization_kernels: TPUModelRunner#_initialize_quantization_kernels().
  TPUModelRunner.pp_push: TPUModelRunner#pp_push().
  TPUModelRunner.pp_settle: TPUModelRunner#pp_settle().
  ExecuteModelState.spec_decode_metadata_list: ExecuteModelState#spec_decode_metadata_list.
  _build_kv_connector_output: _build_kv_connector_output().
  TPUModelRunner._mtp_enabled: TPUModelRunner#_mtp_enabled.
  TPUModelRunner._mamba_ckpt_window: TPUModelRunner#_mamba_ckpt_window.
  TPUModelRunner.seq_lens_cpu: TPUModelRunner#seq_lens_cpu.
  TPUModelRunner._pp_pending_kv_save_nan_check: TPUModelRunner#_pp_pending_kv_save_nan_check.
  TPUModelRunner._greedy_sample: TPUModelRunner#_greedy_sample().
  TPUModelRunner._build_padded_sampling_params: TPUModelRunner#_build_padded_sampling_params().
  TPUModelRunner.use_spmd: TPUModelRunner#use_spmd.
  MIN_NUM_SEQS: MIN_NUM_SEQS.
  TPUModelRunner._has_mamba_state: TPUModelRunner#_has_mamba_state.
  TPUModelRunner._last_sequence_layout_plan: TPUModelRunner#_last_sequence_layout_plan.
  TPUModelRunner._mamba_state_pos: TPUModelRunner#_mamba_state_pos.
  TPUModelRunner._pending_mamba_state_copies: TPUModelRunner#_pending_mamba_state_copies.
  TPUModelRunner._bucket_len: TPUModelRunner#_bucket_len().
  TPUModelRunner._cached_comb_key: TPUModelRunner#_cached_comb_key.
  TPUModelRunner.gather_logprobs: TPUModelRunner#gather_logprobs().
  ExecuteModelState.draft_chunks: ExecuteModelState#draft_chunks.
  ExecuteModelState.kv_save_nan_check: ExecuteModelState#kv_save_nan_check.
  TPUModelRunner.get_pooling_metadata: TPUModelRunner#get_pooling_metadata().
  TPUModelRunner._dp_step_has_encoder_inputs: TPUModelRunner#_dp_step_has_encoder_inputs.
  TPUModelRunner.positions_cpu: TPUModelRunner#positions_cpu.
  TPUModelRunner.positions_np: TPUModelRunner#positions_np.
  TPUModelRunner.mrope_positions: TPUModelRunner#mrope_positions.
  TPUModelRunner.seq_lens_np: TPUModelRunner#seq_lens_np.
  TPUModelRunner.batch_counter: TPUModelRunner#batch_counter.
  TPUModelRunner._token_padding_state: TPUModelRunner#_token_padding_state.
  TPUModelRunner.phased_profiling_dir: TPUModelRunner#phased_profiling_dir.
  TPUModelRunner._pad_dev_to_bucket: TPUModelRunner#_pad_dev_to_bucket().
  TPUModelRunner._dense_kv_copy_pool_sets: TPUModelRunner#_dense_kv_copy_pool_sets().
  TPUModelRunner._get_model_inputs: TPUModelRunner#_get_model_inputs().
  TPUModelRunner.forward_model: TPUModelRunner#forward_model().
  TPUModelRunner.compute_logits_from_hidden_states: TPUModelRunner#compute_logits_from_hidden_states().
  TPUModelRunner.spec_logprob_row_tokens: TPUModelRunner#spec_logprob_row_tokens().
  TPUModelRunner._decode_device_cache_key: TPUModelRunner#_decode_device_cache_key.
  TPUModelRunner._mamba_num_blocks: TPUModelRunner#_mamba_num_blocks.
  TPUModelRunner._kv_cache_bundle_layer_index: TPUModelRunner#_kv_cache_bundle_layer_index.
  ExecuteModelState.logits_list: ExecuteModelState#logits_list.
  ExecuteModelState.num_reqs_list: ExecuteModelState#num_reqs_list.
  _TOPK_INDICES: _TOPK_INDICES.
  TPUModelRunner.empty_slot_mappings: TPUModelRunner#empty_slot_mappings.
  TPUModelRunner._dp_step_other_decode: TPUModelRunner#_dp_step_other_decode.
  TPUModelRunner._free_mamba_slots: TPUModelRunner#_free_mamba_slots.
  TPUModelRunner._request_distribution_cpu: TPUModelRunner#_request_distribution_cpu.
  TPUModelRunner.reorder_batch_threshold: TPUModelRunner#reorder_batch_threshold.
  TPUModelRunner._xla_graphs_checked_at: TPUModelRunner#_xla_graphs_checked_at.
  _spec_logprob_row_tokens: _spec_logprob_row_tokens().
  _pp_step.wrapper: _pp_step().wrapper().
  _find_topk_indices_buffer: _find_topk_indices_buffer().
  TPUModelRunner._create_mesh_for_parallelism: TPUModelRunner#_create_mesh_for_parallelism().
  TPUModelRunner._expand_pool_split: TPUModelRunner#_expand_pool_split().
  TPUModelRunner._install_spec_token_room_guard: TPUModelRunner#_install_spec_token_room_guard().
  TPUModelRunner.guarded: TPUModelRunner#guarded().
  TPUModelRunner._sync_replicated_drafts_across_tp: TPUModelRunner#_sync_replicated_drafts_across_tp().
  TPUModelRunner._cached_comb_dev: TPUModelRunner#_cached_comb_dev.
  TPUModelRunner._any_decode: TPUModelRunner#_any_decode().
  TPUModelRunner.load_model: TPUModelRunner#load_model().
  TPUModelRunner._profile_isolated_cache: TPUModelRunner#_profile_isolated_cache().
  TPUModelRunner._resolve_tpu_group_backend: TPUModelRunner#_resolve_tpu_group_backend().
  _PP_CARRIED_FILL._PP_CARRIED_FILL: _PP_CARRIED_FILL._PP_CARRIED_FILL.
  TPUModelRunner._uniform_mamba_layout: TPUModelRunner#_uniform_mamba_layout.
  TPUModelRunner._attention_kv_cache_group_id: TPUModelRunner#_attention_kv_cache_group_id.
  _tpu_compile: _tpu_compile.
  _spec_warmup_all_token_ids: _spec_warmup_all_token_ids().
  TPUModelRunner.device_config: TPUModelRunner#device_config.
  TPUModelRunner._dp_step_num_chunks: TPUModelRunner#_dp_step_num_chunks.
  TPUModelRunner._dp_step_max_reqs: TPUModelRunner#_dp_step_max_reqs.
  TPUModelRunner._tp_rank0_mask: TPUModelRunner#_tp_rank0_mask.
  TPUModelRunner._attn_layer_names: TPUModelRunner#_attn_layer_names.
  TPUModelRunner._input_staging_fence: TPUModelRunner#_input_staging_fence.
  TPUModelRunner._fenced_h2d_sources: TPUModelRunner#_fenced_h2d_sources.
  TPUModelRunner._sampling_generator: TPUModelRunner#_sampling_generator.
  TPUModelRunner._pp_chunk_granularity: TPUModelRunner#_pp_chunk_granularity.
  TPUModelRunner._attention_runs_batched_kernel: TPUModelRunner#_attention_runs_batched_kernel.
  TPUModelRunner._pp_pending_scheduler_output: TPUModelRunner#_pp_pending_scheduler_output.
  TPUModelRunner._MAX_DESCRIBED_GRAPHS: TPUModelRunner#_MAX_DESCRIBED_GRAPHS.
  TPUModelRunner.partition: TPUModelRunner#partition().
  TPUModelRunner.is_unified_pool_used: TPUModelRunner#is_unified_pool_used().
  TPUModelRunner.__init__: TPUModelRunner#__init__().
  TPUModelRunner.sequence_layout_planner: TPUModelRunner#sequence_layout_planner.
  TPUModelRunner._fast_token_substitution: TPUModelRunner#_fast_token_substitution.
  TPUModelRunner.is_mm_embed_cpu: TPUModelRunner#is_mm_embed_cpu.
  TPUModelRunner._sync_device: TPUModelRunner#_sync_device().
  TPUModelRunner._static_verify_q_len: TPUModelRunner#_static_verify_q_len.
  _get_num_slices_per_kv_cache_update_block: _get_num_slices_per_kv_cache_update_block().
  TPUModelRunner._mamba_slot_stride: TPUModelRunner#_mamba_slot_stride.
  TPUModelRunner._attention_kernel_block_size: TPUModelRunner#_attention_kernel_block_size.
  ExecuteModelState: ExecuteModelState#
  ExecuteModelState.scheduler_output: ExecuteModelState#scheduler_output.
  ExecuteModelState.pooler_output_list: ExecuteModelState#pooler_output_list.
  ExecuteModelState.mamba_state_indices_list: ExecuteModelState#mamba_state_indices_list.
  _reset_read_offsets_impl: _reset_read_offsets_impl().
  _rollback_offsets_seed_impl: _rollback_offsets_seed_impl().
  _rollback_offsets_migrate_impl: _rollback_offsets_migrate_impl().
  _substitute_placeholder_token: _substitute_placeholder_token().
  _suspend_kv_transfer_group: _suspend_kv_transfer_group().
  TPUModelRunner.input_ids: TPUModelRunner#input_ids.
  TPUModelRunner._read_offset_scratch: TPUModelRunner#_read_offset_scratch.
  TPUModelRunner._attention_kernels_initialized: TPUModelRunner#_attention_kernels_initialized.
  TPUModelRunner._unfenced_h2d_sources: TPUModelRunner#_unfenced_h2d_sources.
  TPUModelRunner._cached_query_start_loc: TPUModelRunner#_cached_query_start_loc.
  TPUModelRunner._cached_logits_indices: TPUModelRunner#_cached_logits_indices.
  TPUModelRunner._cached_request_distribution: TPUModelRunner#_cached_request_distribution.
  TPUModelRunner._h2d_reuse: TPUModelRunner#_h2d_reuse.
  TPUModelRunner._profile_inputs: TPUModelRunner#_profile_inputs.
  TPUModelRunner.maybe_setup_kv_connector: TPUModelRunner#maybe_setup_kv_connector().
  TPUModelRunner._xla_graph_compile_secs: TPUModelRunner#_xla_graph_compile_secs().
  TPUModelRunner.segment: TPUModelRunner#segment().
  TPUModelRunner._drafts_per_chunk: TPUModelRunner#_drafts_per_chunk().
  TPUModelRunner._prebuild_module_ops: TPUModelRunner#_prebuild_module_ops().
  TPUModelRunner.spec_bonus_and_target_logits: TPUModelRunner#spec_bonus_and_target_logits().
  TPUModelRunner.spec_bonus_and_target_tokens: TPUModelRunner#spec_bonus_and_target_tokens().
  TPUModelRunner.spec_gather_bonus_and_target_logits: TPUModelRunner#spec_gather_bonus_and_target_logits().
  _KV_CONNECTOR_OUTPUT_SUPPORTS_INVALID_BLOCK_GROUP: _KV_CONNECTOR_OUTPUT_SUPPORTS_INVALID_BLOCK_GROUP.
  SAMPLING_EPS: SAMPLING_EPS.
  _torch_tpu_wrapper: _torch_tpu_wrapper().
  _TOPK_BUFFER_ATTRIBUTE: _TOPK_BUFFER_ATTRIBUTE.
  TPUModelRunner._prefill_only_mtp: TPUModelRunner#_prefill_only_mtp().
  TPUModelRunner._profiler_rank: TPUModelRunner#_profiler_rank.
  TPUModelRunner.check_recompilation: TPUModelRunner#check_recompilation.
  TPUModelRunner.num_kv_heads: TPUModelRunner#num_kv_heads.
  TPUModelRunner.head_size: TPUModelRunner#head_size.
  TPUModelRunner.mm_embed_inputs: TPUModelRunner#mm_embed_inputs.
  TPUModelRunner._combined_request_distribution_cpu: TPUModelRunner#_combined_request_distribution_cpu.
  TPUModelRunner._init_phased_profiling: TPUModelRunner#_init_phased_profiling().
  TPUModelRunner._describe_xla_graph: TPUModelRunner#_describe_xla_graph().
  TPUModelRunner._cached_cur_input_indices: TPUModelRunner#_cached_cur_input_indices.
  TPUModelRunner._update_placeholder: TPUModelRunner#_update_placeholder().
  TPUModelRunner._tpu_pin_drafts_to_rank0: TPUModelRunner#_tpu_pin_drafts_to_rank0().
  TPUModelRunner._num_output_tokens: TPUModelRunner#_num_output_tokens().
  TPUModelRunner.load_lora_model: TPUModelRunner#load_lora_model().
  TPUModelRunner._apply_temperature: TPUModelRunner#_apply_temperature().
  _prev_power_of_2: _prev_power_of_2().
  TPUModelRunner.original_parallel_config: TPUModelRunner#original_parallel_config.
  TPUModelRunner.sliding_window: TPUModelRunner#sliding_window.
  TPUModelRunner.num_attn_layers: TPUModelRunner#num_attn_layers.
  TPUModelRunner._masked_dense_groups_requests: TPUModelRunner#_masked_dense_groups_requests.
  TPUModelRunner._free_h2d_sources: TPUModelRunner#_free_h2d_sources.
  TPUModelRunner._registered_h2d_sources: TPUModelRunner#_registered_h2d_sources.
  TPUModelRunner._init_device_properties: TPUModelRunner#_init_device_properties().
  TPUModelRunner._dense_kv_copy_cache: TPUModelRunner#_dense_kv_copy_cache.
  TPUModelRunner._cached_subst_key: TPUModelRunner#_cached_subst_key.
  _get_padded_num_kv_cache_update_slices: _get_padded_num_kv_cache_update_slices().
---
# Module: [`src/vllm_torchtpu/runner/tpu_runner.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py)

## Classes
### <a id="ExecuteModelState"></a>`ExecuteModelState`
- def: [`src/vllm_torchtpu/runner/tpu_runner.py:214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L214)
- signature: `class ExecuteModelState:`
- members:
  - <a id="ExecuteModelState.draft_chunks"></a>`draft_chunks` — [`L223`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L223)
  - <a id="ExecuteModelState.kv_save_nan_check"></a>`kv_save_nan_check` — [`L235`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L235)
  - <a id="ExecuteModelState.logits_list"></a>`logits_list` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L216)
  - <a id="ExecuteModelState.mamba_state_indices_list"></a>`mamba_state_indices_list` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L229)
  - <a id="ExecuteModelState.num_reqs_list"></a>`num_reqs_list` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L218)
  - <a id="ExecuteModelState.pooler_output_list"></a>`pooler_output_list` — [`L217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L217)
  - <a id="ExecuteModelState.scheduler_output"></a>`scheduler_output` — [`L215`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L215)
  - <a id="ExecuteModelState.spec_decode_metadata_list"></a>`spec_decode_metadata_list` — [`L219`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L219)
  - <a id="ExecuteModelState.top_tokens"></a>`top_tokens` — [`L234`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L234)
- uses (calls/refs, reference-scoped): [`DraftChunkInputs`](../spec_decode/utils.md#DraftChunkInputs), [`KVSaveNanCheck`](../distributed/kv_transfer/kv_save_nan_check.md#KVSaveNanCheck), [`SpecDecodeMetadata`](speculative_decoding_manager.md#SpecDecodeMetadata)
- used by: [`execute_model`](tpu_runner.md#TPUModelRunner.execute_model), [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`execute_model_state`](tpu_runner.md#TPUModelRunner.execute_model_state)

### <a id="TPUModelRunner"></a>`TPUModelRunner`
- def: [`src/vllm_torchtpu/runner/tpu_runner.py:642`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L642) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
- signature: `class TPUModelRunner(GPUModelRunner):`
- members:
  - <a id="TPUModelRunner._add_pipeline_chunk_buckets"></a>`_add_pipeline_chunk_buckets(self)` — [`L6203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6203) — Compile a token bucket at every chunk granule multiple, so a step — documented in [pcp-streaming-rpa-kernel](../../../../concepts/pcp-streaming-rpa-kernel.md)
  - <a id="TPUModelRunner._any_decode"></a>`_any_decode(self, scheduler_output: SchedulerOutput)` — [`L3778`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3778) — Whether this step schedules a request past its prompt; computed
  - <a id="TPUModelRunner._apply_async_token_substitution"></a>`_apply_async_token_substitution(self, input_ids: torch.Tensor, token_in_tpu_cur_input_indices: np.ndarray, token_in_tpu_pre_next_tokens_indices: np.ndarray)` — [`L2460`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2460) — Apply async token substitution if needed.
  - <a id="TPUModelRunner._apply_dense_kv_cache_block_copies"></a>`_apply_dense_kv_cache_block_copies(self, copies)` — [`L2360`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2360) — Copy CoW blocks in every per-layer KV cache tensor. — documented in [custom-ops](../../../../concepts/custom-ops.md)
  - <a id="TPUModelRunner._apply_kv_cache_block_copies"></a>`_apply_kv_cache_block_copies(self, copies)` — [`L2267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2267) — Copy CoW blocks within each unified pool buffer page-locally.
  - <a id="TPUModelRunner._assemble_async_prefill_bootstrap"></a>`_assemble_async_prefill_bootstrap(self, drafts, combined_selected_tokens, combined_real_lens)` — [`L2973`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2973) — Async eagle3 bootstrap assembler for the prefill / pure-non-spec step.
  - <a id="TPUModelRunner._assemble_async_spec_substitution"></a>`_assemble_async_spec_substitution(self, drafts, next_tokens_per_chunk, state)` — [`L2898`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2898) — Async-spec substitution assembler.
  - <a id="TPUModelRunner._attention_kernel_shapes"></a>`_attention_kernel_shapes(self, use_max_model_len: bool)` — [`L6138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6138) — (sequences, pages per sequence, page size) the batched attention
  - <a id="TPUModelRunner._attention_schedule_capacity"></a>`_attention_schedule_capacity(self, use_max_model_len: bool = True)` — [`L6072`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6072) — (pairs, bq, bkv) the batched attention kernel can schedule in — documented in [batched-ragged-paged-attention-kernel](../../../../concepts/batched-ragged-paged-attention-kernel.md)
  - <a id="TPUModelRunner._backbone_dummy_runs"></a>`_backbone_dummy_runs(self, num_tokens: int)` — [`L7222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7222) — One warmup forward of the backbone per context bucket.
  - <a id="TPUModelRunner._bucket_len"></a>`_bucket_len(n: int)` — [`L2171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2171) — Smallest ladder length >= `n`, so the copy op sees few shapes.
  - <a id="TPUModelRunner._build_attention_metadata"></a>`_build_attention_metadata(self, num_tokens: int = 0, num_reqs: int = 0, max_query_len: int = 1, num_tokens_padded: int | None = None, num_reqs_padded: int | None = None, slot_mappings: dict[int, torch.Tensor] | None = None)` — [`L1706`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1706) — Lean TPU group walk: stage one batched block-table upload, then
  - <a id="TPUModelRunner._build_mamba_copy_plan"></a>`_build_mamba_copy_plan(self, kv_cache_config: KVCacheConfig, layer_to_raw: dict[str, torch.Tensor], bm_pool_layout: BlockMajorPoolLayout | None)` — [`L1887`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1887) — Map each mamba kv-cache group to the raw pool buffers hosting its
  - <a id="TPUModelRunner._build_mamba_state_indices"></a>`_build_mamba_state_indices(self, start_index: int, num_reqs: int, target_num_reqs: int)` — [`L1836`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1836) — Build the device `mamba_state_indices` for the current chunk.
  - <a id="TPUModelRunner._check_attention_schedule"></a>`_check_attention_schedule(self, num_reqs: int, q_lens: np.ndarray, num_decode: int, use_max_model_len: bool = True)` — [`L6168`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6168) — Refuse a step whose attention schedule would overrun the
  - <a id="TPUModelRunner._check_draft_buckets"></a>`_check_draft_buckets(self)` — [`L7007`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7007) — Refuses to start a producer whose draft lacks a target bucket.
  - <a id="TPUModelRunner._collect_mamba_state_seed_copies"></a>`_collect_mamba_state_seed_copies(self, scheduler_output, start_index: int, num_reqs: int)` — [`L1953`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1953) — Stage this chunk's mamba state-block seed copies (the counterpart
  - <a id="TPUModelRunner._count_input_chunks"></a>`_count_input_chunks(self, scheduler_output: SchedulerOutput)` — [`L3657`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3657) — Match _prepare_inputs chunking without staging any tensors.
  - <a id="TPUModelRunner._dense_kv_copy_pool_sets"></a>`_dense_kv_copy_pool_sets(self)` — [`L2336`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2336) — Group the unique per-layer caches by manager-block split.
  - <a id="TPUModelRunner._dense_kv_copy_supported"></a>`_dense_kv_copy_supported(self)` — [`L2308`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2308) — Whether CoW copies run on the per-layer KV cache tensors.
  - <a id="TPUModelRunner._describe_xla_graph"></a>`_describe_xla_graph(entry)` — [`L1508`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1508) — One line describing a cache entry, from whatever fields it carries.
  - <a id="TPUModelRunner._dp_coordinated_step"></a>`_dp_coordinated_step(self, local_num_tokens: int, local_num_chunks: int, local_num_reqs: int = 0, has_encoder_inputs: bool = False, local_any_decode: bool = False)` — [`L3728`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3728) — Return the DP-wide padded token bucket and forward chunk count.
  - <a id="TPUModelRunner._drafts_per_chunk"></a>`_drafts_per_chunk(drafts: torch.Tensor | list[torch.Tensor], num_reqs_list: list[int])` — [`L2880`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2880) — Per-chunk view of a proposer's device drafts.
  - <a id="TPUModelRunner._dummy_run"></a>`_dummy_run(self, num_tokens: int, num_reqs: int, num_blocks: int, use_max_model_len: bool = True, dp_lockstep: bool = False, profile_prefix: int | None = None, through_handoff: bool = False)` — [`L5822`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5822) — Run the forward at one bucket shape. — documented in [attention-and-layer-core](../../../../concepts/attention-and-layer-core.md)
  - <a id="TPUModelRunner._execute_mm_encoder"></a>`_execute_mm_encoder(self, scheduler_output: SchedulerOutput)` — [`L3582`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3582) — Run the vision encoder with optional video frame chunking.
  - <a id="TPUModelRunner._expand_pool_split"></a>`_expand_pool_split(self, src: torch.Tensor, dst: torch.Tensor)` — [`L2200`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2200) — Device twin of the manager-block -> pool-block expansion.
  - <a id="TPUModelRunner._fence_spec_kv_under_token_copy"></a>`_fence_spec_kv_under_token_copy(self)` — [`L691`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L691) — A KV producer whose Stage-3 registration is published ahead of
  - <a id="TPUModelRunner._fresh_xla_graphs"></a>`_fresh_xla_graphs(self, entries)` — [`L1537`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1537) — The entries this process compiled since the previous report.
  - <a id="TPUModelRunner._get_sampling_generator"></a>`_get_sampling_generator(self)` — [`L4450`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4450) — Return the dedicated non-greedy sampling generator, seeded once.
  - <a id="TPUModelRunner._greedy_sample"></a>`_greedy_sample(self, logits: torch.Tensor)` — [`L4625`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4625) — argmax logits, only used when `all_greedy` is True.
  - <a id="TPUModelRunner._init_mamba_slot_pool"></a>`_init_mamba_slot_pool(self, mamba_num_blocks: int)` — [`L1810`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1810) — (Re)initialize the per-request mamba recurrent-slot allocator.
  - <a id="TPUModelRunner._init_phased_profiling"></a>`_init_phased_profiling(self)` — [`L1158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1158) — Resolves whether USE_PHASED_PROFILER is set and where its traces go.
  - <a id="TPUModelRunner._initialize_attention_kernels"></a>`_initialize_attention_kernels(self, force: bool = False)` — [`L5683`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5683) — Pre-build Pallas RPA and custom attention kernels before torch.compile. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._install_spec_token_room_guard"></a>`_install_spec_token_room_guard(self)` — [`L2588`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2588) — Wrap InputBatch.update_req_spec_token_ids to clamp its *write*.
  - <a id="TPUModelRunner._is_async_drafter"></a>`_is_async_drafter(self)` — [`L677`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L677) — Whether this worker runs a hidden-state drafter.
  - <a id="TPUModelRunner._mamba_state_index_groups"></a>`_mamba_state_index_groups(self)` — [`L4513`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4513) — This chunk's mamba state slot/block ids, one tensor per group.
  - <a id="TPUModelRunner._mask_min_tokens"></a>`_mask_min_tokens(self, logits: torch.Tensor, rows: min_tokens_mask.StateRows, min_toks: min_tokens_mask.MinTokensState)` — [`L4683`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4683) — Masks the stop tokens of the rows still below min_tokens; `rows` as
  - <a id="TPUModelRunner._min_tokens_batch_state"></a>`_min_tokens_batch_state(self)` — [`L4637`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4637) — This step's batch rows still below min_tokens (empty if none).
  - <a id="TPUModelRunner._pad_dev_to_bucket"></a>`_pad_dev_to_bucket(self, ids: torch.Tensor)` — [`L2187`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2187) — `_pad_to_bucket` for an already-on-device id tensor.
  - <a id="TPUModelRunner._pad_to_bucket"></a>`_pad_to_bucket(cls, values: list, pad=0)` — [`L2179`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2179) — Pad a CPU pair/id list up to the seed-copy bucket ladder.
  - <a id="TPUModelRunner._pool_chunk"></a>`_pool_chunk(self, scheduler_output: SchedulerOutput, hidden_states: torch.Tensor, start_index: int, num_reqs: int, num_tokens_padded: int, padded_num_reqs: int, logits_indices: torch.Tensor | None, layout_plan: Any)` — [`L4351`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4351) — Pool one chunk of requests. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._pp_forward_rows"></a>`_pp_forward_rows(self, scheduler_output: SchedulerOutput)` — [`L3698`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3698) — The padded token count of each forward this step runs, in order,
  - <a id="TPUModelRunner._pp_intermediate_tensors"></a>`_pp_intermediate_tensors(self, num_tokens: int, zeros: bool, random: bool = False)` — [`L8151`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8151) — Buffers shaped like this stage's input from the previous stage:
  - <a id="TPUModelRunner._pp_outgoing_tensors"></a>`_pp_outgoing_tensors(self, tensors: dict[str, torch.Tensor], rows: int)` — [`L8206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8206) — What this stage hands the next one: the model's activations, plus
  - <a id="TPUModelRunner._pp_take_topk_indices"></a>`_pp_take_topk_indices(self, intermediate_tensors: IntermediateTensors | None, rows: int)` — [`L8190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8190) — Take the incoming top-k table into the buffer this stage's sparse
  - <a id="TPUModelRunner._precompile_backbone"></a>`_precompile_backbone(self)` — [`L7164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7164) — Compile the backbone for every token bucket. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TPUModelRunner._precompile_dense_kv_cache_block_copies"></a>`_precompile_dense_kv_cache_block_copies(self)` — [`L2383`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2383) — Warm the dense CoW copy program at every bucket length. — documented in [custom-ops](../../../../concepts/custom-ops.md)
  - <a id="TPUModelRunner._precompile_mamba_rollback_helpers"></a>`_precompile_mamba_rollback_helpers(self)` — [`L7321`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7321) — Warm the compiled rollback scatters at every bucket length.
  - <a id="TPUModelRunner._precompile_mamba_state_seed_copies"></a>`_precompile_mamba_state_seed_copies(self)` — [`L7279`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7279) — Warm the seed-copy program for every raw-pool set at every bucket
  - <a id="TPUModelRunner._precompile_pooler_subgraphs"></a>`_precompile_pooler_subgraphs(self)` — [`L6868`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6868) — AOT-compile the static pooler over the reachable (token, request) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._precompile_rejection_sampler"></a>`_precompile_rejection_sampler(self)` — [`L6606`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6606) — Warm the spec-decode verify path so it doesn't recompile at runtime. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._precompile_sampling_subgraphs"></a>`_precompile_sampling_subgraphs(self)` — [`L6824`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6824) — Compile sampling-path subgraphs so their bottom-HBM reservations
  - <a id="TPUModelRunner._precompile_spec_logprobs"></a>`_precompile_spec_logprobs(self)` — [`L6532`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6532) — Warm the logprobs graphs of a spec-decode verify step. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._precompile_timed"></a>`_precompile_timed(self, name: str)` — [`L6345`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6345) — Common boilerplate for each AOT bucket precompile pass.
  - <a id="TPUModelRunner._precompile_top_token_verify"></a>`_precompile_top_token_verify(self, num_tokens: int, draft_token_ids: torch.Tensor, target_logits_indices: torch.Tensor, segment_ids: torch.Tensor, group_indices: torch.Tensor, draft_lengths: torch.Tensor, bonus_logits_indices: torch.Tensor, warm_accept_u: torch.Tensor)` — [`L6793`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6793) — The greedy verify path on greedy tokens (TPU_GREEDY_TOP_TOKENS).
  - <a id="TPUModelRunner._prefill_only_mtp"></a>`_prefill_only_mtp(parallel_config: ParallelConfig, pcp_enabled: bool, mtp_enabled: bool)` — [`L663`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L663) — Whether MTP runs over prefill chunks only, never verifying.
  - <a id="TPUModelRunner._profile_input"></a>`_profile_input(self, name: str, shape: tuple[int, ...], dtype: torch.dtype)` — [`L6058`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6058) — Random host tensor for profile runs: token ids over the vocabulary
  - <a id="TPUModelRunner._read_offset_reset_scratch"></a>`_read_offset_reset_scratch(self, width: int, device: torch.device)` — [`L4601`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4601) — Reusable `(keep_cpu, keep_dev, null)` of length `width`.
  - <a id="TPUModelRunner._record_input_staging_fence"></a>`_record_input_staging_fence(self)` — [`L3536`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3536) — Fence the uploads issued from the reusable host staging tensors.
  - <a id="TPUModelRunner._refresh_smem_request_caps"></a>`_refresh_smem_request_caps(self, kv_cache_config: KVCacheConfig | None = None)` — [`L7992`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7992) — Use the widest attention table each kernel invocation will prefetch.
  - <a id="TPUModelRunner._relayout_tables"></a>`_relayout_tables(self, model: torch.nn.Module | None)` — [`L1396`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1396) — Give ``model`` the row-major table layouts the env knobs ask for.
  - <a id="TPUModelRunner._reorder_batch_for_rpa"></a>`_reorder_batch_for_rpa(self, scheduler_output: SchedulerOutput)` — [`L1625`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1625) — Reorder active requests into an RPA-friendly decode-first layout.
  - <a id="TPUModelRunner._reset_read_offsets_for_new_requests"></a>`_reset_read_offsets_for_new_requests(self, start_index: int, num_reqs: int)` — [`L4529`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4529) — Zero the read offset when a request acquires new state storage.
  - <a id="TPUModelRunner._resolve_static_pooler"></a>`_resolve_static_pooler(self)` — [`L6845`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6845) — Pick the static compiled pooler for eligible embed poolers.
  - <a id="TPUModelRunner._run_dp_idle_pairing"></a>`_run_dp_idle_pairing(self, bucket: int, num_chunks: int)` — [`L3851`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3851) — Pair encoder, target and draft collectives on an idle EP-DP rank.
  - <a id="TPUModelRunner._sample_spec_verify_chunk"></a>`_sample_spec_verify_chunk(self, logits: torch.Tensor, md: SpecDecodeMetadata, grammar_output: GrammarOutput | None, scheduler_output: SchedulerOutput, cur_start_idx: int, cur_end_idx: int, all_greedy: bool, sampling_generator: torch.Generator | None, top_tokens: bool = False, min_toks: min_tokens_mask.MinTokensState | None = None)` — [`L4698`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4698) — Bonus-token sampling + draft rejection for one spec-verify chunk. — documented in [vllm-layer-adapters](../../../../concepts/vllm-layer-adapters.md)
  - <a id="TPUModelRunner._sample_tokens_pp_intermediate_stage"></a>`_sample_tokens_pp_intermediate_stage(self)` — [`L8228`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8228) — Sampling runs on the last stage only; earlier stages report just
  - <a id="TPUModelRunner._sampler_applies_topk_topp"></a>`_sampler_applies_topk_topp(self)` — [`L8315`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8315) — False when speculative decoding is on and no running request sets
  - <a id="TPUModelRunner._sampler_topk_candidates"></a>`_sampler_topk_candidates(self, cur_start_idx: int, cur_end_idx: int, grammar_output: object | None)` — [`L8332`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8332) — Returns candidate blocks for this chunk's top-k sampling, or 0.
  - <a id="TPUModelRunner._settle_draft_placeholders_for_min_tokens"></a>`_settle_draft_placeholders_for_min_tokens(self)` — [`L4650`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4650) — Under async scheduling a request's output still ends with the
  - <a id="TPUModelRunner._spec_seed_sources"></a>`_spec_seed_sources(self, state_srcs: list[int], ckpt_rows: list[list[int]], new_owners: list[bool])` — [`L2217`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2217) — Seed source per crossing: the checkpoint being resumed from.
  - <a id="TPUModelRunner._spec_verify_bucket_reachable"></a>`_spec_verify_bucket_reachable(self, num_tokens: int, num_reqs: int)` — [`L6323`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6323) — Whether a spec-decode verify step can land in this bucket pair.
  - <a id="TPUModelRunner._spec_warmup_bucket_grid"></a>`_spec_warmup_bucket_grid(self, mixed: bool)` — [`L7470`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7470) — Request counts to warm: the first count at which any program bucket
  - <a id="TPUModelRunner._sync_replicated_drafts_across_tp"></a>`_sync_replicated_drafts_across_tp(self, drafts: torch.Tensor | list[torch.Tensor] | None)` — [`L2828`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2828) — Pin a replicated drafter's device proposal to rank 0's on every rank.
  - <a id="TPUModelRunner._token_padding_update"></a>`_token_padding_update(self, num_tokens_padded: int)` — [`L8109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8109) — Record which of this step's token rows are padding.
  - <a id="TPUModelRunner._topk_candidate_blocks"></a>`_topk_candidate_blocks(self)` — [`L8304`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8304) — Returns TPU_SAMPLER_TOPK_CANDIDATES if the vocab allows it, else 0.
  - <a id="TPUModelRunner._truncate_rope_caches"></a>`_truncate_rope_caches(self)` — [`L1410`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1410) — Slice rotary cos_sin caches to max_model_len which can reduce
  - <a id="TPUModelRunner._update_mamba_slot_read_offsets"></a>`_update_mamba_slot_read_offsets(self, indices_per_group: list[torch.Tensor] | None, next_tokens: torch.Tensor | None, num_reqs: int)` — [`L4469`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4469) — Scatter this chunk's mamba read offsets into the slot-indexed buffer.
  - <a id="TPUModelRunner._upload_unless_unchanged"></a>`_upload_unless_unchanged(self, slot: str, host: torch.Tensor)` — [`L3564`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3564) — `host.to(self.device)`, reusing `slot`'s previous upload when the
  - <a id="TPUModelRunner._verify_logits_paddings"></a>`_verify_logits_paddings(self)` — [`L6450`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6450) — Row counts a verify chunk's logits and its target rows are padded
  - <a id="TPUModelRunner._warmup_handoff_forwards"></a>`_warmup_handoff_forwards(self)` — [`L7240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7240) — Run every token bucket once through the pipeline hand-off. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._warmup_mtp_prefill"></a>`_warmup_mtp_prefill(self)` — [`L7032`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7032) — Warm the real prefill-only MTP K1 proposal and nothing else. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._warmup_one_mtp_prefill"></a>`_warmup_one_mtp_prefill(self, P: int, quiet: bool = False)` — [`L7100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7100) — Run one synthetic prefill through target sampling + K1 propose.
  - <a id="TPUModelRunner._warmup_one_spec_request"></a>`_warmup_one_spec_request(self, P: int, idx: int, quiet: bool = False, greedy: bool = True)` — [`L7701`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7701) — Run one synthetic spec-decode request (prefill P + decodes).
  - <a id="TPUModelRunner._warmup_spec_batch"></a>`_warmup_spec_batch(self, R: int, P: int, greedy: bool = True, *, short: bool = False, mixed: bool = False)` — [`L7519`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7519) — Warm an nr=R decode batch: prefill R synthetic requests then decode
  - <a id="TPUModelRunner._warmup_spec_decode"></a>`_warmup_spec_decode(self)` — [`L7354`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7354) — Warm the real spec-decode dispatch so the first request doesn't recompile. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner._warmup_spec_decode_cleanup"></a>`_warmup_spec_decode_cleanup(self, rids)` — [`L7821`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7821) — Tear down the synthetic warmup request(s) so serving starts clean.
  - <a id="TPUModelRunner.build_attention_metadata_for_layers"></a>`build_attention_metadata_for_layers(self, layer_names: Collection[str], num_reqs_padded: int)` — [`L1742`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1742) — Build attention metadata for only the groups owning `layer_names`.
  - <a id="TPUModelRunner.capture_model"></a>`capture_model(self)` — [`L6930`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6930) — Precompile every torch.compile subgraph across all input buckets. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
  - <a id="TPUModelRunner.compute_logits_from_hidden_states"></a>`compute_logits_from_hidden_states(self, hidden_states: torch.Tensor)` — [`L8366`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8366)
  - <a id="TPUModelRunner.compute_selected_logits"></a>`compute_selected_logits(self, hidden_states: torch.Tensor, indices_do_sample: torch.Tensor)` — [`L8357`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8357)
  - <a id="TPUModelRunner.compute_selected_top_tokens"></a>`compute_selected_top_tokens(self, hidden_states: torch.Tensor, indices_do_sample: torch.Tensor)` — [`L8380`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8380)
  - <a id="TPUModelRunner.compute_top_tokens_from_hidden_states"></a>`compute_top_tokens_from_hidden_states(self, hidden_states: torch.Tensor)` — [`L8391`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8391)
  - <a id="TPUModelRunner.execute_model"></a>`execute_model(self, scheduler_output: SchedulerOutput, intermediate_tensors: IntermediateTensors | None = None)` — [`L3884`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3884) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
  - <a id="TPUModelRunner.forward_model"></a>`forward_model(self, input_ids, positions, inputs_embeds=None, intermediate_tensors=None)` — [`L8122`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8122)
  - <a id="TPUModelRunner.gather_logprobs"></a>`gather_logprobs(self, logits: torch.Tensor, sampled_tokens: torch.Tensor)` — [`L8509`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8509) — Gather the top_logprobs with corresponding tokens. Use a fixed number
  - <a id="TPUModelRunner.get_finished_kv_transfers"></a>`get_finished_kv_transfers(self, scheduler_output)` — [`L1278`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1278) — documented in [kv-transfer-and-disaggregated-serving](../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPUModelRunner.get_kv_cache_spec"></a>`get_kv_cache_spec(self)` — [`L1795`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1795)
  - <a id="TPUModelRunner.get_kv_prewarm_shapes"></a>`get_kv_prewarm_shapes(self)` — [`L1804`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1804)
  - <a id="TPUModelRunner.get_pooling_metadata"></a>`get_pooling_metadata(batch)` — [`L777`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L777)
  - <a id="TPUModelRunner.guarded"></a>`guarded(request, scheduled_spec_tokens)` — [`L2617`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2617)
  - <a id="TPUModelRunner.initialize_kv_cache"></a>`initialize_kv_cache(self, kv_cache_config: KVCacheConfig)` — [`L1800`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1800)
  - <a id="TPUModelRunner.is_unified_pool_used"></a>`is_unified_pool_used(self)` — [`L2261`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2261) — Whether the attention-shaped unified KV block pool is active
  - <a id="TPUModelRunner.kv_connector_no_forward"></a>`kv_connector_no_forward(self, scheduler_output, vllm_config)` — [`L1331`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1331)
  - <a id="TPUModelRunner.load_lora_model"></a>`load_lora_model(self, model: torch.nn.Module, vllm_config: VllmConfig, device: torch.device)` — [`L5626`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5626) — Wraps the model's layers for LoRA. load_model calls it when LoRA is
  - <a id="TPUModelRunner.load_model"></a>`load_model(self)` — [`L5511`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5511)
  - <a id="TPUModelRunner.lora_slot_write_hbm_bytes"></a>`lora_slot_write_hbm_bytes(self)` — [`L5643`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5643) — HBM an adapter swap takes while it runs, which the KV cache budget
  - <a id="TPUModelRunner.may_reinitialize_input_batch"></a>`may_reinitialize_input_batch(self, kv_cache_config: KVCacheConfig, kernel_block_sizes: list[int] | None = None)` — [`L8068`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8068) — Override to keep TPUModelRunner block accounting in sync with upstream.
  - <a id="TPUModelRunner.maybe_setup_kv_connector"></a>`maybe_setup_kv_connector(self, scheduler_output, wait_for_completion: bool = False, report_completion: bool = True)` — [`L1245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1245)
  - <a id="TPUModelRunner.maybe_wait_for_kv_save"></a>`maybe_wait_for_kv_save(self, nan_check: KVSaveNanCheck | None = None)` — [`L1270`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1270)
  - <a id="TPUModelRunner.partition"></a>`partition(start: int, end: int, first)` — [`L1661`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1661) — Two-pointer partition of [start, end]: requests for which
  - <a id="TPUModelRunner.post_profile_hbm_reserves"></a>`post_profile_hbm_reserves(self)` — [`L5652`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5652) — HBM that profile_run does not see, which the KV cache budget must — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="TPUModelRunner.pp_handoff_hbm_reserve_bytes"></a>`pp_handoff_hbm_reserve_bytes(self)` — [`L6900`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6900) — Device memory the ring hand-off's buffers can take beyond the — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.pp_push"></a>`pp_push(self)` — [`L8216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8216) — A pipeline hand-off that carries nothing, so the forwards in
  - <a id="TPUModelRunner.pp_settle"></a>`pp_settle(self)` — [`L8222`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8222) — Close the pipeline hand-off burst once nothing is in flight; a
  - <a id="TPUModelRunner.prewarm_kv_offload_shape"></a>`prewarm_kv_offload_shape(self, p: int)` — [`L1807`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1807)
  - <a id="TPUModelRunner.profile_pipeline_chunks"></a>`profile_pipeline_chunks(self)` — [`L6263`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6263) — Time this stage's forward at the points the pipeline chunk — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.profile_run"></a>`profile_run(self, num_tokens: int)` — [`L7923`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7923) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.sample_from_logits"></a>`sample_from_logits(self, logits: torch.Tensor, temperatures: torch.Tensor, u: torch.Tensor, top_k: torch.Tensor, top_p: torch.Tensor, all_greedy: bool = False, topk_candidates: int = 0, apply_topk_topp: bool = True)` — [`L8461`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8461) — Sample with xla-friendly function. This function is to be traced
  - <a id="TPUModelRunner.sample_tokens"></a>`sample_tokens(self, grammar_output: GrammarOutput | None)` — [`L4864`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4864) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.segment"></a>`segment(req_id: str)` — [`L1652`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1652)
  - <a id="TPUModelRunner.spec_bonus_and_target_logits"></a>`spec_bonus_and_target_logits(self, logits: torch.Tensor, bonus_logits_indices: torch.Tensor, target_logits_indices: torch.Tensor)` — [`L8401`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8401)
  - <a id="TPUModelRunner.spec_bonus_and_target_tokens"></a>`spec_bonus_and_target_tokens(self, tokens: torch.Tensor, bonus_logits_indices: torch.Tensor, target_logits_indices: torch.Tensor)` — [`L8421`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8421)
  - <a id="TPUModelRunner.spec_gather_bonus_and_target_logits"></a>`spec_gather_bonus_and_target_logits(self, logits: torch.Tensor, bonus_logits_indices: torch.Tensor, target_logits_indices: torch.Tensor)` — [`L8434`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8434)
  - <a id="TPUModelRunner.spec_logprob_row_tokens"></a>`spec_logprob_row_tokens(self, next_tokens: torch.Tensor, bonus_logits_indices: torch.Tensor, draft_lengths: torch.Tensor, final_logits_indices: torch.Tensor)` — [`L8497`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8497)
  - <a id="TPUModelRunner.start_phased_profiling"></a>`start_phased_profiling(self, profile_prefix: str | None = None, profiler_kwargs: dict[str, Any] | None = None)` — [`L1173`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1173) — Arms the phase-based profiler. Called from TPUWorker.profile(). — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="TPUModelRunner.stop_phased_profiling"></a>`stop_phased_profiling(self)` — [`L1226`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1226) — Disarms the phase-based profiler. Called from TPUWorker.profile().
  - <a id="TPUModelRunner.take_draft_token_ids"></a>`take_draft_token_ids(self)` — [`L4445`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4445)
  - <a id="TPUModelRunner.tok_bucket"></a>`tok_bucket(n: int)` — [`L7488`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7488)
  - <a id="TPUModelRunner.widest_table"></a>`widest_table(model_len: int | None)` — [`L8035`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8035)
  - <a id="TPUModelRunner.arange_np"></a>`arange_np` — [`L1025`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1025)
  - <a id="TPUModelRunner.batch_counter"></a>`batch_counter` — [`L1119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1119)
  - <a id="TPUModelRunner.block_size"></a>`block_size` — [`L920`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L920)
  - <a id="TPUModelRunner.block_table_cpu"></a>`block_table_cpu` — [`L981`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L981)
  - <a id="TPUModelRunner.bm_pool_layout"></a>`bm_pool_layout` — [`L868`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L868)
  - <a id="TPUModelRunner.check_recompilation"></a>`check_recompilation` — [`L894`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L894)
  - <a id="TPUModelRunner.device"></a>`device` — [`L5513`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5513) — documented in [quantization-methods](../../../../concepts/quantization-methods.md)
  - <a id="TPUModelRunner.device_config"></a>`device_config` — [`L795`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L795)
  - <a id="TPUModelRunner.drafter"></a>`drafter` — [`L644`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L644) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.empty_slot_mappings"></a>`empty_slot_mappings` — [`L651`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L651)
  - <a id="TPUModelRunner.encoder_cudagraph_manager"></a>`encoder_cudagraph_manager` — [`L6973`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6973) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.enforce_eager"></a>`enforce_eager` — [`L898`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L898)
  - <a id="TPUModelRunner.execute_model_state"></a>`execute_model_state` — [`L1043`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1043)
  - <a id="TPUModelRunner.head_size"></a>`head_size` — [`L963`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L963)
  - <a id="TPUModelRunner.input_ids"></a>`input_ids` — [`L650`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L650)
  - <a id="TPUModelRunner.input_ids_cpu"></a>`input_ids_cpu` — [`L974`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L974)
  - <a id="TPUModelRunner.is_mm_embed_cpu"></a>`is_mm_embed_cpu` — [`L1019`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1019)
  - <a id="TPUModelRunner.is_pooling_model"></a>`is_pooling_model` — [`L762`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L762)
  - <a id="TPUModelRunner.kv_cache_config"></a>`kv_cache_config` — [`L870`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L870)
  - <a id="TPUModelRunner.kv_cache_dtype"></a>`kv_cache_dtype` — [`L909`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L909)
  - <a id="TPUModelRunner.kv_cache_manager"></a>`kv_cache_manager` — [`L1111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1111)
  - <a id="TPUModelRunner.kv_cache_raw_tensors"></a>`kv_cache_raw_tensors` — [`L864`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L864)
  - <a id="TPUModelRunner.lora_manager"></a>`lora_manager` — [`L5638`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5638)
  - <a id="TPUModelRunner.mamba_slot_read_offsets"></a>`mamba_slot_read_offsets` — [`L844`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L844)
  - <a id="TPUModelRunner.max_num_blocks_per_req"></a>`max_num_blocks_per_req` — [`L931`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L931)
  - <a id="TPUModelRunner.max_num_reqs"></a>`max_num_reqs` — [`L950`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L950) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.max_num_tokens"></a>`max_num_tokens` — [`L958`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L958) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.mesh"></a>`mesh` — [`L1118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1118) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.mm_embed_inputs"></a>`mm_embed_inputs` — [`L1042`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1042)
  - <a id="TPUModelRunner.model"></a>`model` — [`L648`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L648)
  - <a id="TPUModelRunner.most_model_len"></a>`most_model_len` — [`L921`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L921)
  - <a id="TPUModelRunner.mrope_positions"></a>`mrope_positions` — [`L1004`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1004)
  - <a id="TPUModelRunner.num_attn_layers"></a>`num_attn_layers` — [`L959`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L959)
  - <a id="TPUModelRunner.num_blocks_per_most_len_req"></a>`num_blocks_per_most_len_req` — [`L943`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L943)
  - <a id="TPUModelRunner.num_kv_heads"></a>`num_kv_heads` — [`L962`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L962)
  - <a id="TPUModelRunner.num_reqs_max_model_len"></a>`num_reqs_max_model_len` — [`L8051`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8051) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.num_reqs_most_model_len"></a>`num_reqs_most_model_len` — [`L8056`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8056) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.num_reqs_paddings"></a>`num_reqs_paddings` — [`L1026`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1026) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.num_tokens_paddings"></a>`num_tokens_paddings` — [`L955`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L955) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.num_xla_graphs"></a>`num_xla_graphs` — [`L899`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L899)
  - <a id="TPUModelRunner.original_parallel_config"></a>`original_parallel_config` — [`L794`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L794)
  - <a id="TPUModelRunner.phase_based_profiler"></a>`phase_based_profiler` — [`L1171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1171)
  - <a id="TPUModelRunner.phased_profiling_dir"></a>`phased_profiling_dir` — [`L1168`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1168)
  - <a id="TPUModelRunner.position_ids"></a>`position_ids` — [`L3240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3240) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.positions_cpu"></a>`positions_cpu` — [`L977`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L977)
  - <a id="TPUModelRunner.positions_np"></a>`positions_np` — [`L980`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L980)
  - <a id="TPUModelRunner.query_start_loc_cpu"></a>`query_start_loc_cpu` — [`L1007`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1007)
  - <a id="TPUModelRunner.query_start_loc_np"></a>`query_start_loc_np` — [`L1013`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1013)
  - <a id="TPUModelRunner.rejection_sampler"></a>`rejection_sampler` — [`L646`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L646)
  - <a id="TPUModelRunner.reorder_batch_threshold"></a>`reorder_batch_threshold` — [`L1107`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1107)
  - <a id="TPUModelRunner.sample_from_logits_func"></a>`sample_from_logits_func` — [`L1038`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1038) — ---
  - <a id="TPUModelRunner.seq_lens_cpu"></a>`seq_lens_cpu` — [`L1014`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1014)
  - <a id="TPUModelRunner.seq_lens_np"></a>`seq_lens_np` — [`L1017`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1017)
  - <a id="TPUModelRunner.sequence_layout_planner"></a>`sequence_layout_planner` — [`L760`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L760)
  - <a id="TPUModelRunner.sliding_window"></a>`sliding_window` — [`L919`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L919)
  - <a id="TPUModelRunner.spec_decode_manager"></a>`spec_decode_manager` — [`L1108`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1108)
  - <a id="TPUModelRunner.speculative_config"></a>`speculative_config` — [`L1087`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1087) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUModelRunner.structured_decoding_manager"></a>`structured_decoding_manager` — [`L1110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1110)
  - <a id="TPUModelRunner.use_spmd"></a>`use_spmd` — [`L895`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L895)
  - <a id="TPUModelRunner.vocab_size"></a>`vocab_size` — [`L964`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L964)
- protocol/private: <a id="TPUModelRunner._MAX_DESCRIBED_GRAPHS"></a>`_MAX_DESCRIBED_GRAPHS`[`L1499`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1499), <a id="TPUModelRunner.__init__"></a>`__init__`[`L705`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L705), <a id="TPUModelRunner._apply_temperature"></a>`_apply_temperature`[`L8452`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8452), <a id="TPUModelRunner._async_drafter"></a>`_async_drafter`[`L657`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L657), <a id="TPUModelRunner._attention_capacity"></a>`_attention_capacity`[`L1033`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1033), <a id="TPUModelRunner._attention_kernel_block_size"></a>`_attention_kernel_block_size`[`L1134`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1134), <a id="TPUModelRunner._attention_kernels_initialized"></a>`_attention_kernels_initialized`[`L967`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L967), <a id="TPUModelRunner._attention_kv_cache_group_id"></a>`_attention_kv_cache_group_id`[`L1138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1138), <a id="TPUModelRunner._attention_runs_batched_kernel"></a>`_attention_runs_batched_kernel`[`L1132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1132), <a id="TPUModelRunner._attn_layer_names"></a>`_attn_layer_names`[`L1052`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1052), <a id="TPUModelRunner._attn_metadata_builder_ctx"></a>`_attn_metadata_builder_ctx`[`L3463`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3463), <a id="TPUModelRunner._build_padded_sampling_params"></a>`_build_padded_sampling_params`[`L8269`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8269), <a id="TPUModelRunner._cached_comb_dev"></a>`_cached_comb_dev`[`L3454`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3454), <a id="TPUModelRunner._cached_comb_key"></a>`_cached_comb_key`[`L3455`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3455), <a id="TPUModelRunner._cached_cur_input_indices"></a>`_cached_cur_input_indices`[`L2536`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2536), <a id="TPUModelRunner._cached_logits_indices"></a>`_cached_logits_indices`[`L1081`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1081), <a id="TPUModelRunner._cached_pre_next_tokens_indices"></a>`_cached_pre_next_tokens_indices`[`L2537`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2537), <a id="TPUModelRunner._cached_query_start_loc"></a>`_cached_query_start_loc`[`L1080`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1080), <a id="TPUModelRunner._cached_request_distribution"></a>`_cached_request_distribution`[`L1082`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1082), <a id="TPUModelRunner._cached_subst_key"></a>`_cached_subst_key`[`L2535`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2535), <a id="TPUModelRunner._combined_request_distribution_cpu"></a>`_combined_request_distribution_cpu`[`L1064`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1064), <a id="TPUModelRunner._copy_mamba_state_blocks"></a>`_copy_mamba_state_blocks`[`L2251`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2251), <a id="TPUModelRunner._create_mesh_for_parallelism"></a>`_create_mesh_for_parallelism`[`L1464`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1464), <a id="TPUModelRunner._decode_device_cache_key"></a>`_decode_device_cache_key`[`L1065`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1065), <a id="TPUModelRunner._dense_kv_copy_cache"></a>`_dense_kv_copy_cache`[`L2333`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2333), <a id="TPUModelRunner._dp_lockstep_enabled"></a>`_dp_lockstep_enabled`[`L3648`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3648), <a id="TPUModelRunner._dp_num_tokens_across_dp"></a>`_dp_num_tokens_across_dp`[`L3872`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3872), <a id="TPUModelRunner._dp_step_has_encoder_inputs"></a>`_dp_step_has_encoder_inputs`[`L890`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L890), <a id="TPUModelRunner._dp_step_max_reqs"></a>`_dp_step_max_reqs`[`L889`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L889), <a id="TPUModelRunner._dp_step_num_chunks"></a>`_dp_step_num_chunks`[`L888`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L888), <a id="TPUModelRunner._dp_step_other_decode"></a>`_dp_step_other_decode`[`L654`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L654), <a id="TPUModelRunner._dp_target_bucket"></a>`_dp_target_bucket`[`L887`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L887), <a id="TPUModelRunner._dummy_logits"></a>`_dummy_logits`[`L6353`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6353), <a id="TPUModelRunner._execute_dp_mm_encoder"></a>`_execute_dp_mm_encoder`[`L3794`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3794), <a id="TPUModelRunner._fast_token_substitution"></a>`_fast_token_substitution`[`L922`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L922), <a id="TPUModelRunner._fenced_h2d_sources"></a>`_fenced_h2d_sources`[`L1077`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1077), <a id="TPUModelRunner._flush_disjoint_async_results"></a>`_flush_disjoint_async_results`[`L2568`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2568), <a id="TPUModelRunner._flush_mamba_state_seed_copies"></a>`_flush_mamba_state_seed_copies`[`L2244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2244), <a id="TPUModelRunner._free_h2d_sources"></a>`_free_h2d_sources`[`L1078`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1078), <a id="TPUModelRunner._free_mamba_slots"></a>`_free_mamba_slots`[`L817`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L817), <a id="TPUModelRunner._get_model_inputs"></a>`_get_model_inputs`[`L3607`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3607), <a id="TPUModelRunner._greedy_head_owner"></a>`_greedy_head_owner`[`L1153`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1153), <a id="TPUModelRunner._greedy_top_tokens_this_step"></a>`_greedy_top_tokens_this_step`[`L8371`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8371), <a id="TPUModelRunner._h2d_reuse"></a>`_h2d_reuse`[`L1085`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1085), <a id="TPUModelRunner._has_mamba_state"></a>`_has_mamba_state`[`L839`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L839), <a id="TPUModelRunner._hidden_states_dtype"></a>`_hidden_states_dtype`[`L916`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L916), <a id="TPUModelRunner._hybrid_uniform_page_size_bytes"></a>`_hybrid_uniform_page_size_bytes`[`L799`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L799), <a id="TPUModelRunner._init_device_properties"></a>`_init_device_properties`[`L1236`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1236), <a id="TPUModelRunner._init_speculative_decoding"></a>`_init_speculative_decoding`[`L1364`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1364), <a id="TPUModelRunner._initialize_pallas_kernels"></a>`_initialize_pallas_kernels`[`L5667`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5667), <a id="TPUModelRunner._initialize_quantization_kernels"></a>`_initialize_quantization_kernels`[`L5671`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5671), <a id="TPUModelRunner._input_staging_fence"></a>`_input_staging_fence`[`L1069`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1069), <a id="TPUModelRunner._is_dspark_pd_producer"></a>`_is_dspark_pd_producer`[`L1090`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1090), <a id="TPUModelRunner._kv_cache_bundle"></a>`_kv_cache_bundle`[`L881`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L881), <a id="TPUModelRunner._kv_cache_bundle_layer_index"></a>`_kv_cache_bundle_layer_index`[`L882`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L882), <a id="TPUModelRunner._last_sequence_layout_plan"></a>`_last_sequence_layout_plan`[`L873`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L873), <a id="TPUModelRunner._mamba_ckpt_window"></a>`_mamba_ckpt_window`[`L834`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L834), <a id="TPUModelRunner._mamba_copy_plan"></a>`_mamba_copy_plan`[`L991`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L991), <a id="TPUModelRunner._mamba_num_blocks"></a>`_mamba_num_blocks`[`L810`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L810), <a id="TPUModelRunner._mamba_offset_seeded"></a>`_mamba_offset_seeded`[`L847`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L847), <a id="TPUModelRunner._mamba_slot_by_req_id"></a>`_mamba_slot_by_req_id`[`L816`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L816), <a id="TPUModelRunner._mamba_slot_stride"></a>`_mamba_slot_stride`[`L833`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L833), <a id="TPUModelRunner._mamba_state_block_size"></a>`_mamba_state_block_size`[`L1904`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1904), <a id="TPUModelRunner._mamba_state_pos"></a>`_mamba_state_pos`[`L990`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L990), <a id="TPUModelRunner._masked_dense_groups_requests"></a>`_masked_dense_groups_requests`[`L971`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L971), <a id="TPUModelRunner._min_tokens"></a>`_min_tokens`[`L1045`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1045), <a id="TPUModelRunner._modify_prev_results"></a>`_modify_prev_results`[`L2714`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2714), <a id="TPUModelRunner._mtp_enabled"></a>`_mtp_enabled`[`L721`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L721), <a id="TPUModelRunner._mtp_prefill_only"></a>`_mtp_prefill_only`[`L726`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L726), <a id="TPUModelRunner._num_output_tokens"></a>`_num_output_tokens`[`L4646`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L4646), <a id="TPUModelRunner._num_static_verify_reqs"></a>`_num_static_verify_reqs`[`L1374`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1374), <a id="TPUModelRunner._pcp_enabled"></a>`_pcp_enabled`[`L720`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L720), <a id="TPUModelRunner._pending_mamba_state_copies"></a>`_pending_mamba_state_copies`[`L997`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L997), <a id="TPUModelRunner._pool_block_split"></a>`_pool_block_split`[`L994`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L994), <a id="TPUModelRunner._pp_chunk_granularity"></a>`_pp_chunk_granularity`[`L1129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1129), <a id="TPUModelRunner._pp_intermediate_template"></a>`_pp_intermediate_template`[`L1142`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1142), <a id="TPUModelRunner._pp_is_first"></a>`_pp_is_first`[`L725`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L725), <a id="TPUModelRunner._pp_is_last"></a>`_pp_is_last`[`L725`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L725), <a id="TPUModelRunner._pp_pending_kv_save_nan_check"></a>`_pp_pending_kv_save_nan_check`[`L1148`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1148), <a id="TPUModelRunner._pp_pending_scheduler_output"></a>`_pp_pending_scheduler_output`[`L1147`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1147), <a id="TPUModelRunner._pp_topk_buffer"></a>`_pp_topk_buffer`[`L1126`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1126), <a id="TPUModelRunner._pp_wave"></a>`_pp_wave`[`L653`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L653), <a id="TPUModelRunner._pre_async_results"></a>`_pre_async_results`[`L1044`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1044), <a id="TPUModelRunner._prebuild_module_ops"></a>`_prebuild_module_ops`[`L5764`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L5764), <a id="TPUModelRunner._precompile_compute_logits_from_hidden_states"></a>`_precompile_compute_logits_from_hidden_states`[`L6377`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6377), <a id="TPUModelRunner._precompile_compute_selected_logits"></a>`_precompile_compute_selected_logits`[`L6359`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6359), <a id="TPUModelRunner._precompile_compute_top_tokens"></a>`_precompile_compute_top_tokens`[`L6389`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6389), <a id="TPUModelRunner._precompile_gather_logprobs"></a>`_precompile_gather_logprobs`[`L6520`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6520), <a id="TPUModelRunner._precompile_min_tokens_mask"></a>`_precompile_min_tokens_mask`[`L6461`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6461), <a id="TPUModelRunner._precompile_sample_from_logits"></a>`_precompile_sample_from_logits`[`L6482`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6482), <a id="TPUModelRunner._precompile_structured_decoding"></a>`_precompile_structured_decoding`[`L6418`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6418), <a id="TPUModelRunner._precompile_substitute_placeholder_token"></a>`_precompile_substitute_placeholder_token`[`L6571`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L6571), <a id="TPUModelRunner._prepare_async_token_substitution_indices"></a>`_prepare_async_token_substitution_indices`[`L2407`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2407), <a id="TPUModelRunner._prepare_inputs"></a>`_prepare_inputs`[`L3031`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3031), <a id="TPUModelRunner._profile_inputs"></a>`_profile_inputs`[`L1140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1140), <a id="TPUModelRunner._profile_isolated_cache"></a>`_profile_isolated_cache`[`L7899`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7899), <a id="TPUModelRunner._profiler_rank"></a>`_profiler_rank`[`L717`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L717), <a id="TPUModelRunner._profiler_world_size"></a>`_profiler_world_size`[`L718`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L718), <a id="TPUModelRunner._read_offset_scratch"></a>`_read_offset_scratch`[`L850`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L850), <a id="TPUModelRunner._registered_h2d_sources"></a>`_registered_h2d_sources`[`L1079`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1079), <a id="TPUModelRunner._request_distribution_cpu"></a>`_request_distribution_cpu`[`L1053`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1053), <a id="TPUModelRunner._resolve_tpu_group_backend"></a>`_resolve_tpu_group_backend`[`L7979`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L7979), <a id="TPUModelRunner._run_dp_dummy_chunk"></a>`_run_dp_dummy_chunk`[`L3842`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3842), <a id="TPUModelRunner._sampling_generator"></a>`_sampling_generator`[`L1115`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1115), <a id="TPUModelRunner._stage_timing"></a>`_stage_timing`[`L1156`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1156), <a id="TPUModelRunner._static_pooler_reason"></a>`_static_pooler_reason`[`L767`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L767), <a id="TPUModelRunner._static_pooler_spec"></a>`_static_pooler_spec`[`L766`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L766), <a id="TPUModelRunner._static_verify_q_len"></a>`_static_verify_q_len`[`L1373`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1373), <a id="TPUModelRunner._sync_device"></a>`_sync_device`[`L1242`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1242), <a id="TPUModelRunner._sync_one_replicated_draft"></a>`_sync_one_replicated_draft`[`L2846`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2846), <a id="TPUModelRunner._token_padding_state"></a>`_token_padding_state`[`L1151`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1151), <a id="TPUModelRunner._tp_rank0_mask"></a>`_tp_rank0_mask`[`L1048`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1048), <a id="TPUModelRunner._tpu_pin_drafts_to_rank0"></a>`_tpu_pin_drafts_to_rank0`[`L2868`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2868), <a id="TPUModelRunner._unfenced_h2d_sources"></a>`_unfenced_h2d_sources`[`L1076`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1076), <a id="TPUModelRunner._unified_kv_layout"></a>`_unified_kv_layout`[`L863`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L863), <a id="TPUModelRunner._uniform_mamba_layout"></a>`_uniform_mamba_layout`[`L857`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L857), <a id="TPUModelRunner._update_num_xla_graphs"></a>`_update_num_xla_graphs`[`L1566`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1566), <a id="TPUModelRunner._update_placeholder"></a>`_update_placeholder`[`L2796`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2796), <a id="TPUModelRunner._update_states"></a>`_update_states`[`L2660`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L2660), <a id="TPUModelRunner._wait_input_staging_fence"></a>`_wait_input_staging_fence`[`L3555`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L3555), <a id="TPUModelRunner._xla_graph_compile_secs"></a>`_xla_graph_compile_secs`[`L1532`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1532), <a id="TPUModelRunner._xla_graphs_checked_at"></a>`_xla_graphs_checked_at`[`L1505`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L1505)
- uses (calls/refs, reference-scoped): [`initialize_kv_cache`](kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`synchronize_tensors`](../utils.md#synchronize_tensors), [`logger`](tpu_runner.md#logger), [`build`](../layers/core/attention_metadata.md#AttentionMetadataBuilder.build), [`load_model`](../spec_decode/dflash.md#DFlashProposer.load_model), [`get_kv_cache_spec`](kv_cache_manager.md#KVCacheManager.get_kv_cache_spec), [`get_spec_decode_metadata`](speculative_decoding_manager.md#SpeculativeDecodingManager.get_spec_decode_metadata), [`start_forward`](../distributed/pp_ring.md#PPRing.start_forward), [`initialize_kernel`](../layers/adapter/attention.md#PallasAttentionBackendImpl.initialize_kernel), [`get_tpu_quantization_config`](../layers/adapter/quantization/__init__.md#get_tpu_quantization_config), [`arm`](../layers/adapter/moe_tp_decode.md#arm), [`draft_model`](../spec_decode/dflash.md#DFlashProposer.draft_model), [`precompile`](../spec_decode/dflash.md#DFlashProposer.precompile), [`set_vllm_model_wrapper_context`](../models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`AttentionMetadata`](../layers/core/attention_metadata.md#AttentionMetadata), [`settle`](../distributed/pp_wave.md#PPWave.settle), [`warmup`](../distributed/pp_ring.md#PPRing.warmup), [`validate_online_fp8`](../layers/adapter/quantization/online_fp8.md#validate_online_fp8), [`stage_block_table_uploads`](../layers/core/attention_metadata.md#stage_block_table_uploads), [`static_pool`](tpu_pooling.md#static_pool), [`build_static_pool_inputs`](tpu_pooling.md#build_static_pool_inputs), [`build_dummy_static_pool_inputs`](tpu_pooling.md#build_dummy_static_pool_inputs), [`end_forward`](../distributed/pp_wave.md#PPWave.end_forward), [`from_vllm_config`](../platforms/pcp_validation.md#PcpStaticSupportValidator.from_vllm_config), [`TraceAnnotation`](../tracing/annotation.md#TraceAnnotation), [`PallasAttentionBackend`](../layers/adapter/attention.md#PallasAttentionBackend), [`end_forward`](../distributed/pp_ring.md#PPRing.end_forward), [`begin_step`](../distributed/pp_ring.md#PPRing.begin_step), [`propose_draft_token_ids`](speculative_decoding_manager.md#SpeculativeDecodingManager.propose_draft_token_ids), [`DraftChunkInputs`](../spec_decode/utils.md#DraftChunkInputs), [`resolve_static_pooler_spec`](tpu_pooling.md#resolve_static_pooler_spec), [`stage`](stage_timing.md#RunnerStageTiming.stage), [`push`](../distributed/pp_wave.md#PPWave.push), [`start_forward`](../distributed/pp_wave.md#PPWave.start_forward), [`get_output`](tpu_runner_async_output.md#AsyncTPUModelRunnerOutput.get_output), [`PallasAttentionBackendImpl`](../layers/adapter/attention.md#PallasAttentionBackendImpl), [`compute_tpu_compilation_hash`](../compilation/tpu_compiler.md#compute_tpu_compilation_hash), [`take_samples`](stage_timing.md#RunnerStageTiming.take_samples), [`BlockMajorPoolLayout`](../block_major_pool.md#BlockMajorPoolLayout), [`SequenceLayoutKind`](../layers/core/sequence_layout.md#SequenceLayoutKind)  (+285 more)
- used by: [`initialize_kv_cache`](kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`_admit_raiden_hybrid_kv_cache`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`_build_dp_dummy_draft`](../spec_decode/eagle3.md#Eagle3Proposer._build_dp_dummy_draft), [`propose`](../spec_decode/eagle3.md#Eagle3Proposer.propose), [`_initialize_unified_kv_cache`](kv_cache_manager.md#KVCacheManager._initialize_unified_kv_cache), [`_admit_raiden_dsv4_kv_cache`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_dsv4_kv_cache), [`_build_draft_attn_metadata`](../spec_decode/eagle3.md#Eagle3Proposer._build_draft_attn_metadata), [`_admit_raiden_glm_kv_cache`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_glm_kv_cache), [`load_model`](../spec_decode/eagle3.md#Eagle3Proposer.load_model), [`load_model`](../spec_decode/dflash.md#DFlashProposer.load_model), [`get_kv_cache_spec`](kv_cache_manager.md#KVCacheManager.get_kv_cache_spec), [`get_spec_decode_metadata`](speculative_decoding_manager.md#SpeculativeDecodingManager.get_spec_decode_metadata), [`profile`](../worker/tpu_worker.md#TPUWorker.profile), [`_prepare_draft_inputs`](../spec_decode/eagle3.md#Eagle3Proposer._prepare_draft_inputs), [`determine_available_memory`](../worker/tpu_worker.md#TPUWorker.determine_available_memory), [`precompile`](../spec_decode/dflash.md#DFlashProposer.precompile), [`_measure_stage3_layout`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._measure_stage3_layout), [`model_runner`](../worker/tpu_worker.md#TPUWorker.model_runner), [`propose`](../spec_decode/dflash.md#DFlashProposer.propose), [`_forward_draft`](../spec_decode/eagle3.md#Eagle3Proposer._forward_draft), [`register_runner`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker.register_runner), [`_build_mtp_fused_loop`](../spec_decode/eagle3.md#Eagle3Proposer._build_mtp_fused_loop), [`_refresh_ds_v4_request_caps`](kv_cache_dsv4.md#DsV4KVCacheAllocator._refresh_ds_v4_request_caps), [`_build_attn_metadata_for_draft`](../spec_decode/dflash.md#DFlashProposer._build_attn_metadata_for_draft), [`_build_mtp_loop_model`](../spec_decode/eagle3.md#Eagle3Proposer._build_mtp_loop_model), [`_dummy_kv_update_inputs`](../spec_decode/dflash.md#DFlashProposer._dummy_kv_update_inputs), [`_load_draft_model`](../spec_decode/eagle3.md#Eagle3Proposer._load_draft_model), [`_precompile_compute_logits`](../spec_decode/eagle3.md#Eagle3Proposer._precompile_compute_logits), [`_dummy_draft_forward`](../spec_decode/dflash.md#DFlashProposer._dummy_draft_forward), [`_init_mtp_index_sharing`](../spec_decode/eagle3.md#Eagle3Proposer._init_mtp_index_sharing), [`_precompile_combine_hidden_states`](../spec_decode/eagle3.md#Eagle3Proposer._precompile_combine_hidden_states), [`_update_draft_kv_cache_from_target`](../spec_decode/dflash.md#DFlashProposer._update_draft_kv_cache_from_target), [`_update_mamba_page_size_padded`](kv_cache_manager.md#KVCacheManager._update_mamba_page_size_padded), [`_run_mtp_fused_loop`](../spec_decode/eagle3.md#Eagle3Proposer._run_mtp_fused_loop), [`_update_attention_page_size_padded`](kv_cache_manager.md#KVCacheManager._update_attention_page_size_padded), [`_dummy_precompute_and_update_kv_cache`](../spec_decode/dflash.md#DFlashProposer._dummy_precompute_and_update_kv_cache), [`propose_draft_token_ids`](speculative_decoding_manager.md#SpeculativeDecodingManager.propose_draft_token_ids), [`_loop_step_attn_inputs`](../spec_decode/eagle3.md#Eagle3Proposer._loop_step_attn_inputs), [`_load_draft_model`](../spec_decode/dflash.md#DFlashProposer._load_draft_model), [`_precompile_draft_seed`](../spec_decode/eagle3.md#Eagle3Proposer._precompile_draft_seed)  (+48 more)

## Functions
- <a id="_build_kv_connector_output"></a>`_build_kv_connector_output(*, finished_sending: set[str] | None, finished_recving: set[str] | None, failed_recving: set[str], kv_connector_worker_meta: Any | None, invalid_block_ids: set[int], invalid_block_group_index: int | None, kv_connector_stats: Any | None = None)` — [`L487`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L487) — Build the runner's KVConnectorOutput.
- <a id="_find_topk_indices_buffer"></a>`_find_topk_indices_buffer(model: torch.nn.Module)` — [`L617`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L617) — The one top-k table this process's layers share, or None.
- <a id="_get_num_slices_per_kv_cache_update_block"></a>`_get_num_slices_per_kv_cache_update_block(page_size_bytes: int)` — [`L8602`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8602) — Find the optimum number of slices to copy per Pallas program instance.
- <a id="_get_padded_num_kv_cache_update_slices"></a>`_get_padded_num_kv_cache_update_slices(num_tokens: int, max_num_reqs: int, page_size: int)` — [`L8580`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8580) — Calculates the padded number of KV cache update slices to avoid
- <a id="_get_padded_num_reqs_with_upper_limit"></a>`_get_padded_num_reqs_with_upper_limit(x: int, upper_limit: int)` — [`L8560`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8560)
- <a id="_get_padded_token_len"></a>`_get_padded_token_len(paddings: list[int], x: int)` — [`L8565`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8565) — Return the first element in paddings list greater or equal to x. — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
- <a id="_get_req_paddings"></a>`_get_req_paddings(min_req_size: int, max_req_size: int)` — [`L8547`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8547)
- <a id="_get_sequence_layout_planner_for_runner"></a>`_get_sequence_layout_planner_for_runner(runner: Any)` — [`L523`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L523)
- <a id="_pp_step"></a>`_pp_step(method: Callable[Concatenate[Any, P], R])` — [`L410`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L410) — Brackets a runner call that traces device ops with the pipeline wave's
- <a id="_prev_power_of_2"></a>`_prev_power_of_2(n: int)` — [`L8595`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L8595) — The previous power of 2 (inclusive)
- <a id="_reset_read_offsets"></a>`_reset_read_offsets(read_offsets: torch.Tensor, keep_dev: torch.Tensor, stacked_groups: torch.Tensor, null: torch.Tensor)` — [`L280`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L280)
- <a id="_reset_read_offsets_impl"></a>`_reset_read_offsets_impl(read_offsets: torch.Tensor, keep_dev: torch.Tensor, stacked_groups: torch.Tensor, null: torch.Tensor)` — [`L243`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L243) — Scatter reset across all mamba groups in a single program.
- <a id="_rollback_offsets_migrate"></a>`_rollback_offsets_migrate(read_offsets: torch.Tensor, src_t: torch.Tensor, dst_t: torch.Tensor)` — [`L303`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L303)
- <a id="_rollback_offsets_migrate_impl"></a>`_rollback_offsets_migrate_impl(read_offsets: torch.Tensor, src_t: torch.Tensor, dst_t: torch.Tensor)` — [`L268`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L268)
- <a id="_rollback_offsets_seed"></a>`_rollback_offsets_seed(read_offsets: torch.Tensor, dst_t: torch.Tensor)` — [`L294`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L294)
- <a id="_rollback_offsets_seed_impl"></a>`_rollback_offsets_seed_impl(read_offsets: torch.Tensor, dst_t: torch.Tensor)` — [`L257`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L257)
- <a id="_rotate_precompile_sweep"></a>`_rotate_precompile_sweep(items: Collection[Any], sweep: str)` — [`L427`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L427) — Start this local rank at its own share of a precompile sweep.
- <a id="_spec_logprob_row_tokens"></a>`_spec_logprob_row_tokens(next_tokens: torch.Tensor, bonus_logits_indices: torch.Tensor, draft_lengths: torch.Tensor, final_logits_indices: torch.Tensor)` — [`L314`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L314) — The token each verify-logits row's slot chose, for gather_logprobs.
- <a id="_spec_warmup_all_token_ids"></a>`_spec_warmup_all_token_ids(req_ids: list[str], num_computed_tokens: list[int])` — [`L454`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L454) — Build complete synthetic token histories for async cached requests.
- <a id="_substitute_placeholder_token"></a>`_substitute_placeholder_token(input_ids: torch.Tensor, token_in_tpu_cur_input_indices: torch.Tensor, token_in_tpu_pre_next_tokens_indices: torch.Tensor, next_tokens: torch.Tensor)` — [`L357`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L357) — Substitute placeholder tokens from TPU for async scheduler.
- <a id="_suspend_kv_transfer_group"></a>`_suspend_kv_transfer_group()` — [`L471`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L471) — Hide the process-global connector during worker-local warmup.
- <a id="_torch_tpu_wrapper"></a>`_torch_tpu_wrapper()` — [`L561`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L561) — Alias torch.cuda.* to torch.accelerator.* during inherited GPUModelRunner
- <a id="_validate_libtpu_version"></a>`_validate_libtpu_version()` — [`L527`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L527) — Validate libtpu opportunistically if it is present.
- <a id="_pp_step.wrapper"></a>`wrapper(self: Any, *args: P.args, **kwargs: P.kwargs)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L417)

## Module values
- <a id="MIN_NUM_SEQS"></a>`MIN_NUM_SEQS` — [`L519`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L519)
- <a id="SAMPLING_EPS"></a>`SAMPLING_EPS` — [`L520`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L520)
- <a id="_KV_CONNECTOR_OUTPUT_SUPPORTS_INVALID_BLOCK_GROUP"></a>`_KV_CONNECTOR_OUTPUT_SUPPORTS_INVALID_BLOCK_GROUP` — [`L481`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L481)
- <a id="_PP_CARRIED_FILL._PP_CARRIED_FILL"></a>`_PP_CARRIED_FILL` — [`L614`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L614)
- <a id="_TOPK_BUFFER_ATTRIBUTE"></a>`_TOPK_BUFFER_ATTRIBUTE` — [`L610`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L610)
- <a id="_TOPK_INDICES"></a>`_TOPK_INDICES` — [`L609`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L609)
- <a id="_reset_read_offsets_compiled"></a>`_reset_read_offsets_compiled` — [`L275`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L275)
- <a id="_rollback_offsets_migrate_compiled"></a>`_rollback_offsets_migrate_compiled` — [`L277`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L277)
- <a id="_rollback_offsets_seed_compiled"></a>`_rollback_offsets_seed_compiled` — [`L276`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L276)
- <a id="_tpu_compile"></a>`_tpu_compile` — [`L274`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L274)
- <a id="logger"></a>`logger` — [`L407`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner.py#L407)

