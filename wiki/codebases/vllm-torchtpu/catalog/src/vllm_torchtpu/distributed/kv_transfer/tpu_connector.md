---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.tpu_connector`/
symbols:
  TPURaidenConnectorWorker._submit_stage3_loads: TPURaidenConnectorWorker#_submit_stage3_loads().
  TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache: TPURaidenConnectorWorker#_admit_raiden_hybrid_kv_cache().
  TPURaidenConnectorWorker._register_stage3_request_blocks: TPURaidenConnectorWorker#_register_stage3_request_blocks().
  TPURaidenConnectorWorker._poll_finished: TPURaidenConnectorWorker#_poll_finished().
  TPURaidenConnectorScheduler._stage3_publish_send: TPURaidenConnectorScheduler#_stage3_publish_send().
  TPURaidenConnectorWorker._register_stage3_request_row_spans: TPURaidenConnectorWorker#_register_stage3_request_row_spans().
  logger: logger.
  TPURaidenConnectorWorker._stage_stage3_submit_task: TPURaidenConnectorWorker#_stage_stage3_submit_task().
  TPURaidenConnectorWorker.get_finished: TPURaidenConnectorWorker#get_finished().
  TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4: TPURaidenConnectorWorker#_register_stage3_request_blocks_dsv4().
  TPURaidenConnectorWorker._apply_stage3_submit_outcome: TPURaidenConnectorWorker#_apply_stage3_submit_outcome().
  TPURaidenConnectorWorker.process_send_load: TPURaidenConnectorWorker#process_send_load().
  TPURaidenConnectorWorker._admit_raiden_dsv4_kv_cache: TPURaidenConnectorWorker#_admit_raiden_dsv4_kv_cache().
  TPURaidenConnectorScheduler._update_stage3_state_after_alloc: TPURaidenConnectorScheduler#_update_stage3_state_after_alloc().
  TPURaidenConnectorWorker._admit_raiden_glm_kv_cache: TPURaidenConnectorWorker#_admit_raiden_glm_kv_cache().
  TPURaidenConnectorWorker.vllm_config: TPURaidenConnectorWorker#vllm_config.
  TPURaidenConnectorWorker._stage3_state_pool_spans: TPURaidenConnectorWorker#_stage3_state_pool_spans().
  TPURaidenConnectorScheduler._fail_load: TPURaidenConnectorScheduler#_fail_load().
  TPURaidenConnectorWorker._construct_raiden_transfer_engine: TPURaidenConnectorWorker#_construct_raiden_transfer_engine().
  TPURaidenConnectorWorker._register_raiden_stage3_work_unit: TPURaidenConnectorWorker#_register_raiden_stage3_work_unit().
  TPURaidenConnectorWorker.tp_rank: TPURaidenConnectorWorker#tp_rank.
  TPUConnector.connector_scheduler: TPUConnector#connector_scheduler.
  TPURaidenConnectorScheduler._enqueue_stage3_release: TPURaidenConnectorScheduler#_enqueue_stage3_release().
  TPURaidenConnectorWorker._maybe_host_reshard_store: TPURaidenConnectorWorker#_maybe_host_reshard_store().
  TPURaidenConnectorWorker.is_producer: TPURaidenConnectorWorker#is_producer.
  TPURaidenConnectorWorker._execute_stage3_submit: TPURaidenConnectorWorker#_execute_stage3_submit().
  TPURaidenConnectorWorker._measure_stage3_layout: TPURaidenConnectorWorker#_measure_stage3_layout().
  TPURaidenConnectorScheduler.update_state_after_alloc: TPURaidenConnectorScheduler#update_state_after_alloc().
  TPURaidenConnectorWorker._drain_stage3_pending_submits: TPURaidenConnectorWorker#_drain_stage3_pending_submits().
  TPUConnectorScheduler.request_finished: TPUConnectorScheduler#request_finished().
  TPURaidenConnectorWorker.get_kv_connector_stats: TPURaidenConnectorWorker#get_kv_connector_stats().
  TPURaidenConnectorWorker.register_runner: TPURaidenConnectorWorker#register_runner().
  TPURaidenConnectorWorker._stage3_release_producer_registration: TPURaidenConnectorWorker#_stage3_release_producer_registration().
  TPURaidenConnectorWorker.tp_size: TPURaidenConnectorWorker#tp_size.
  TPURaidenConnectorWorker._local_raiden_transfer_rank: TPURaidenConnectorWorker#_local_raiden_transfer_rank().
  TPURaidenConnectorWorker.transfer_stats: TPURaidenConnectorWorker#transfer_stats.
  TPURaidenConnectorWorker._dispatch_stage3_load_submit: TPURaidenConnectorWorker#_dispatch_stage3_load_submit().
  TPURaidenConnectorWorker._stage3_row_geometry: TPURaidenConnectorWorker#_stage3_row_geometry.
  TPURaidenConnectorWorker._stage3_source_work_units: TPURaidenConnectorWorker#_stage3_source_work_units().
  TPURaidenConnectorWorker._probe_stage3_registrations: TPURaidenConnectorWorker#_probe_stage3_registrations().
  TPURaidenConnectorWorker._submit_stage3_load_as_leader: TPURaidenConnectorWorker#_submit_stage3_load_as_leader().
  TPUConnectorScheduler.update_state_after_alloc: TPUConnectorScheduler#update_state_after_alloc().
  TPURaidenConnectorScheduler._stage3_register_ahead: TPURaidenConnectorScheduler#_stage3_register_ahead().
  TPUConnector._stage3_transfer_groups: TPUConnector#_stage3_transfer_groups.
  TPURaidenConnectorWorker._stage3_registered_sends: TPURaidenConnectorWorker#_stage3_registered_sends.
  TPUConnector.request_finished_all_groups: TPUConnector#request_finished_all_groups().
  TPUConnectorWorker._maybe_enable_kv_scatter: TPUConnectorWorker#_maybe_enable_kv_scatter().
  TPURaidenConnectorWorker._raiden_stage3_enabled: TPURaidenConnectorWorker#_raiden_stage3_enabled().
  TPUConnectorScheduler.vllm_config: TPUConnectorScheduler#vllm_config.
  TPURaidenConnectorWorker._glm_dcp_producer_topology: TPURaidenConnectorWorker#_glm_dcp_producer_topology().
  TPURaidenConnectorWorker._measure_dsv4_pool_plan: TPURaidenConnectorWorker#_measure_dsv4_pool_plan().
  TPURaidenConnectorWorker._validate_gdn_transfer_geometry: TPURaidenConnectorWorker#_validate_gdn_transfer_geometry().
  TPURaidenConnectorWorker._sync_stage3_tp_submit_states: TPURaidenConnectorWorker#_sync_stage3_tp_submit_states().
  TPURaidenConnectorScheduler.request_finished: TPURaidenConnectorScheduler#request_finished().
  TPURaidenConnectorWorker._raiden_work_unit_fields: TPURaidenConnectorWorker#_raiden_work_unit_fields().
  TPURaidenConnectorScheduler._validate_load_params: TPURaidenConnectorScheduler#_validate_load_params().
  _Stage3RegisteredSend.uuid: _Stage3RegisteredSend#uuid.
  TPUConnector.connector_worker: TPUConnector#connector_worker.
  TPURaidenConnectorScheduler._stage3_register_ahead_enabled: TPURaidenConnectorScheduler#_stage3_register_ahead_enabled().
  TPURaidenConnectorWorker._stage3_dsv4_group_blocks: TPURaidenConnectorWorker#_stage3_dsv4_group_blocks().
  TPUConnector._stage3_mamba_group_indices: TPUConnector#_stage3_mamba_group_indices.
  TPUConnectorScheduler._admit_kv_transfer_params: TPUConnectorScheduler#_admit_kv_transfer_params().
  TPURaidenConnectorScheduler._request_finished_stage3: TPURaidenConnectorScheduler#_request_finished_stage3().
  TPURaidenConnectorWorker._raiden_glm_admission_topology: TPURaidenConnectorWorker#_raiden_glm_admission_topology().
  TPURaidenConnectorWorker._validate_glm_dcp_destination: TPURaidenConnectorWorker#_validate_glm_dcp_destination().
  TPURaidenConnectorWorker._validate_stage3_transfer_parallelism: TPURaidenConnectorWorker#_validate_stage3_transfer_parallelism().
  TPURaidenConnectorWorker._stage3_ready_producer_send_terminals: TPURaidenConnectorWorker#_stage3_ready_producer_send_terminals().
  _use_raiden_stage3_transport: _use_raiden_stage3_transport().
  _uses_tp_stage3_source: _uses_tp_stage3_source().
  TPURaidenConnectorWorker._stage3_kimi: TPURaidenConnectorWorker#_stage3_kimi.
  TPURaidenConnectorWorker._drain_stage3_submit_outcomes: TPURaidenConnectorWorker#_drain_stage3_submit_outcomes().
  TPURaidenConnectorWorker._stage3_sharded_consumer: TPURaidenConnectorWorker#_stage3_sharded_consumer().
  TPURaidenConnectorWorker._wait_for_recving: TPURaidenConnectorWorker#_wait_for_recving().
  _as_int: _as_int().
  TPUConnectorScheduler.reqs_to_load: TPUConnectorScheduler#reqs_to_load.
  _engine_is_pipeline: _engine_is_pipeline().
  TPUConnectorScheduler.build_connector_meta: TPUConnectorScheduler#build_connector_meta().
  TPURaidenConnectorScheduler.get_finished_count: TPURaidenConnectorScheduler#get_finished_count().
  TPURaidenConnectorWorker._raiden_endpoint_identity: TPURaidenConnectorWorker#_raiden_endpoint_identity().
  TPURaidenConnectorWorker._resolve_remote_endpoint: TPURaidenConnectorWorker#_resolve_remote_endpoint().
  TPURaidenConnectorWorker._record_stage3_load_failure: TPURaidenConnectorWorker#_record_stage3_load_failure().
  TPURaidenConnectorWorker._stage3_fa_skip_bytes: TPURaidenConnectorWorker#_stage3_fa_skip_bytes().
  TPURaidenConnectorWorker._ensure_stage3_submit_workers: TPURaidenConnectorWorker#_ensure_stage3_submit_workers().
  TPURaidenConnectorWorker._stage3_terminal_sends: TPURaidenConnectorWorker#_stage3_terminal_sends.
  _Stage3TransferGroup.cache_group_index: _Stage3TransferGroup#cache_group_index.
  _Stage3RegisteredSend.num_tokens: _Stage3RegisteredSend#num_tokens.
  _use_raiden_dsv4_admission: _use_raiden_dsv4_admission().
  TPURaidenConnectorScheduler.build_connector_meta: TPURaidenConnectorScheduler#build_connector_meta().
  TPURaidenConnectorWorker._raiden_manifest: TPURaidenConnectorWorker#_raiden_manifest.
  TPURaidenConnectorWorker._raiden_kimi_k3_admission_topology: TPURaidenConnectorWorker#_raiden_kimi_k3_admission_topology().
  TPURaidenConnectorWorker._stage3_state_registration_tags: TPURaidenConnectorWorker#_stage3_state_registration_tags().
  _stage3_transfer_groups: _stage3_transfer_groups().
  _use_raiden_glm_admission: _use_raiden_glm_admission().
  TPUConnectorScheduler.side_channel_port: TPUConnectorScheduler#side_channel_port.
  TPUConnectorWorker._build_d2h_views: TPUConnectorWorker#_build_d2h_views().
  TPURaidenConnectorWorker._raiden_interleave_tokens: TPURaidenConnectorWorker#_raiden_interleave_tokens().
  _Stage3RegisteredSend.local_block_ids: _Stage3RegisteredSend#local_block_ids.
  TPURaidenConnectorWorker.dp_rank: TPURaidenConnectorWorker#dp_rank.
  TPURaidenConnectorWorker._ensure_raiden_transfer_engine: TPURaidenConnectorWorker#_ensure_raiden_transfer_engine().
  TPURaidenConnectorScheduler._stage3_transfer_groups: TPURaidenConnectorScheduler#_stage3_transfer_groups.
  TPURaidenConnectorScheduler.on_new_request: TPURaidenConnectorScheduler#on_new_request().
  TPURaidenConnectorScheduler.get_num_new_matched_tokens: TPURaidenConnectorScheduler#get_num_new_matched_tokens().
  TPURaidenConnectorWorker._raiden_qwen35_admission_topology: TPURaidenConnectorWorker#_raiden_qwen35_admission_topology().
  TPURaidenConnectorWorker._gdn_head_geometry: TPURaidenConnectorWorker#_gdn_head_geometry().
  TPURaidenConnectorWorker._stage3_record_producer_send_terminals: TPURaidenConnectorWorker#_stage3_record_producer_send_terminals().
  TPURaidenConnectorWorker.get_transfer_results: TPURaidenConnectorWorker#get_transfer_results().
  TPURaidenConnectorWorker._num_raiden_slots: TPURaidenConnectorWorker#_num_raiden_slots().
  TPURaidenConnectorScheduler._stage3_prefix_aware_load_enabled: TPURaidenConnectorScheduler#_stage3_prefix_aware_load_enabled.
  TPURaidenConnectorWorker._stage3_state_group_count: TPURaidenConnectorWorker#_stage3_state_group_count.
  TPURaidenConnectorScheduler._reject_kv_transfer_params: TPURaidenConnectorScheduler#_reject_kv_transfer_params().
  TPURaidenConnectorWorker._model_config_int: TPURaidenConnectorWorker#_model_config_int().
  _raiden_dst_dcp_size: _raiden_dst_dcp_size().
  TPUConnectorScheduler._validate_load_params: TPUConnectorScheduler#_validate_load_params().
  TPURaidenConnectorWorker._stage3_send_outcomes: TPURaidenConnectorWorker#_stage3_send_outcomes.
  TPURaidenConnectorWorker._stage3_controller_accepted: TPURaidenConnectorWorker#_stage3_controller_accepted.
  TPURaidenConnectorWorker._maybe_delay_stage3_registration_for_test: TPURaidenConnectorWorker#_maybe_delay_stage3_registration_for_test().
  TPURaidenConnectorWorker._release: TPURaidenConnectorWorker#_release().
  TPURaidenConnectorWorker._mark_stage3_source_unreachable: TPURaidenConnectorWorker#_mark_stage3_source_unreachable().
  TPURaidenConnectorWorker._raiden_destination_work_units: TPURaidenConnectorWorker#_raiden_destination_work_units().
  _use_per_layer_pool_tags: _use_per_layer_pool_tags().
  _resolved_reshard_controller_address: _resolved_reshard_controller_address().
  TPUConnectorScheduler.is_producer: TPUConnectorScheduler#is_producer.
  _Stage3RegisteredSend.expiration_time: _Stage3RegisteredSend#expiration_time.
  _as_str: _as_str().
  _use_raiden_connector: _use_raiden_connector().
  TPURaidenConnectorScheduler._stage3_finished_sends: TPURaidenConnectorScheduler#_stage3_finished_sends.
  TPURaidenConnectorWorker._raiden_work_unit: TPURaidenConnectorWorker#_raiden_work_unit.
  TPURaidenConnectorWorker._load_block_ids: TPURaidenConnectorWorker#_load_block_ids.
  TPURaidenConnectorWorker._get_raiden_stats: TPURaidenConnectorWorker#_get_raiden_stats().
  TPURaidenConnectorWorker._require_stage3_controller: TPURaidenConnectorWorker#_require_stage3_controller().
  TPURaidenConnectorWorker._stage3_submit_worker_loop: TPURaidenConnectorWorker#_stage3_submit_worker_loop().
  TPURaidenConnectorWorker._raiden_staging_blocks_per_pool: TPURaidenConnectorWorker#_raiden_staging_blocks_per_pool().
  _raiden_dst_shards: _raiden_dst_shards().
  _pipeline_parallel_size: _pipeline_parallel_size().
  TPUConnector.register_kv_caches: TPUConnector#register_kv_caches().
  TPUConnector.start_load_kv: TPUConnector#start_load_kv().
  TPURaidenConnector.build_connector_worker_meta: TPURaidenConnector#build_connector_worker_meta().
  TPUConnectorScheduler.reqs_to_send: TPUConnectorScheduler#reqs_to_send.
  TPUConnectorScheduler.kv_ip: TPUConnectorScheduler#kv_ip.
  TPUConnectorWorker._try_fast_scatter: TPUConnectorWorker#_try_fast_scatter().
  TPURaidenConnectorScheduler.reqs_to_release: TPURaidenConnectorScheduler#reqs_to_release.
  TPURaidenConnectorWorker._stage3_pending_controller_failures: TPURaidenConnectorWorker#_stage3_pending_controller_failures.
  TPURaidenConnectorWorker._failed_recving: TPURaidenConnectorWorker#_failed_recving.
  TPUConnector._connector_metadata: TPUConnector#_connector_metadata.
  TPUConnectorScheduler._reject_kv_transfer_params: TPUConnectorScheduler#_reject_kv_transfer_params().
  TPURaidenConnectorScheduler.kv_port: TPURaidenConnectorScheduler#kv_port.
  TPURaidenConnectorWorker.runner: TPURaidenConnectorWorker#runner.
  TPURaidenConnectorWorker.kv_transfer_port: TPURaidenConnectorWorker#kv_transfer_port.
  TPURaidenConnectorWorker._stage3_pending_submits: TPURaidenConnectorWorker#_stage3_pending_submits.
  TPURaidenConnectorWorker._raiden_engine_id: TPURaidenConnectorWorker#_raiden_engine_id().
  TPURaidenConnectorWorker._start_stage3_transfer_with_d5_retry: TPURaidenConnectorWorker#_start_stage3_transfer_with_d5_retry().
  TPURaidenConnectorWorker._register_raiden_pools: TPURaidenConnectorWorker#_register_raiden_pools().
  _Stage3TransferGroup.page_tokens: _Stage3TransferGroup#page_tokens.
  _Stage3RegisteredSend: _Stage3RegisteredSend#
  _raiden_dst_interleave_tokens: _raiden_dst_interleave_tokens().
  _prefix_aware_load_enabled: _prefix_aware_load_enabled().
  TPURaidenConnectorWorker._pd_send_results: TPURaidenConnectorWorker#_pd_send_results.
  TPURaidenConnectorWorker._raiden_transfer_engine: TPURaidenConnectorWorker#_raiden_transfer_engine.
  TPURaidenConnectorWorker._stage3_inflight_submits: TPURaidenConnectorWorker#_stage3_inflight_submits.
  TPURaidenConnectorScheduler._send_completion_enabled: TPURaidenConnectorScheduler#_send_completion_enabled.
  TPURaidenConnectorScheduler._stage3_truncates_prompt: TPURaidenConnectorScheduler#_stage3_truncates_prompt().
  TPURaidenConnectorScheduler._raiden_engine_id: TPURaidenConnectorScheduler#_raiden_engine_id().
  TPURaidenConnectorWorker._raiden_dsv4_admission_topology: TPURaidenConnectorWorker#_raiden_dsv4_admission_topology().
  TPURaidenConnectorWorker._raiden_transfer_parallelism: TPURaidenConnectorWorker#_raiden_transfer_parallelism().
  TPURaidenConnectorWorker._raiden_hybrid_admission_topology: TPURaidenConnectorWorker#_raiden_hybrid_admission_topology().
  TPURaidenConnectorWorker.take_pd_send_results: TPURaidenConnectorWorker#take_pd_send_results().
  TPUConnectorScheduler.block_size: TPUConnectorScheduler#block_size.
  TPURaidenConnectorWorker._stage3_terminal_cleanup: TPURaidenConnectorWorker#_stage3_terminal_cleanup.
  TPURaidenConnectorWorker._stage3_reported_sends: TPURaidenConnectorWorker#_stage3_reported_sends.
  TPURaidenConnectorWorker._stage3_submitted_loads: TPURaidenConnectorWorker#_stage3_submitted_loads.
  TPURaidenConnectorWorker._stage3_terminal_loads: TPURaidenConnectorWorker#_stage3_terminal_loads.
  TPURaidenConnectorWorker._done_recving: TPURaidenConnectorWorker#_done_recving.
  TPURaidenConnectorWorker._stage3_fa_registration_tags: TPURaidenConnectorWorker#_stage3_fa_registration_tags().
  _pipeline_stage_pcp_size: _pipeline_stage_pcp_size().
  _reshard_store_mode: _reshard_store_mode().
  TPUConnector.supports_divergent_local_hybrid_hits: TPUConnector#supports_divergent_local_hybrid_hits().
  TPUConnector.build_connector_meta: TPUConnector#build_connector_meta().
  TPUConnector.register_runner: TPUConnector#register_runner().
  TPUConnector.get_transfer_results: TPUConnector#get_transfer_results().
  TPUConnector.get_block_ids_with_load_errors_group_index: TPUConnector#get_block_ids_with_load_errors_group_index().
  TPUConnectorScheduler.get_num_new_matched_tokens: TPUConnectorScheduler#get_num_new_matched_tokens().
  TPURaidenConnectorWorker._stage3_dsv4_plan: TPURaidenConnectorWorker#_stage3_dsv4_plan.
  _Stage3LoadMeta: _Stage3LoadMeta#
  _Stage3PendingSubmit.destination_req_id: _Stage3PendingSubmit#destination_req_id.
  _Stage3PendingSubmit.local_blocks: _Stage3PendingSubmit#local_blocks.
  _raiden_seq_on_lane_layout: _raiden_seq_on_lane_layout().
  _reshard_service_address: _reshard_service_address().
  _reshard_dispatch_address: _reshard_dispatch_address().
  TPURaidenConnectorScheduler._stage3_mamba_group_indices: TPURaidenConnectorScheduler#_stage3_mamba_group_indices.
  TPURaidenConnectorScheduler._normalize: TPURaidenConnectorScheduler#_normalize().
  TPURaidenConnectorWorker._failed_block_ids: TPURaidenConnectorWorker#_failed_block_ids.
  TPURaidenConnectorWorker._stage3_state_regions: TPURaidenConnectorWorker#_stage3_state_regions().
  TPURaidenConnectorWorker._stage3_source_unreachable: TPURaidenConnectorWorker#_stage3_source_unreachable().
  _Stage3SubmitOutcome.task: _Stage3SubmitOutcome#task.
  _Stage3TransferGroup: _Stage3TransferGroup#
  _stage3_trim_window_pages: _stage3_trim_window_pages().
  _stage3_recycled_transfer_pages: _stage3_recycled_transfer_pages().
  _Stage3LoadMeta.source_req_id: _Stage3LoadMeta#source_req_id.
  _Stage3SubmitOutcome: _Stage3SubmitOutcome#
  _Stage3SubmitOutcome.error: _Stage3SubmitOutcome#error.
  TPURaidenConnectorWorker._stage3_source_facades: TPURaidenConnectorWorker#_stage3_source_facades.
  TPURaidenConnectorWorker._stage3_status_probe_next: TPURaidenConnectorWorker#_stage3_status_probe_next.
  TPURaidenConnectorWorker._stage3_destination_req_ids: TPURaidenConnectorWorker#_stage3_destination_req_ids.
  TPURaidenConnectorWorker._stage3_finished_loads_pending_cleanup: TPURaidenConnectorWorker#_stage3_finished_loads_pending_cleanup.
  TPURaidenConnectorWorker._stage3_deferred_native_failures: TPURaidenConnectorWorker#_stage3_deferred_native_failures.
  TPURaidenConnectorWorker._done_sending: TPURaidenConnectorWorker#_done_sending.
  TPURaidenConnectorWorker._suppress_done_recving: TPURaidenConnectorWorker#_suppress_done_recving.
  TPURaidenConnectorWorker._measure_raiden_glm_layout: TPURaidenConnectorWorker#_measure_raiden_glm_layout().
  TPURaidenConnectorWorker._measure_glm_tag_geometry: TPURaidenConnectorWorker#_measure_glm_tag_geometry().
  TPURaidenConnectorWorker._stage3_state_live_bytes: TPURaidenConnectorWorker#_stage3_state_live_bytes().
  TPURaidenConnectorWorker._bind_stage3_request_ids: TPURaidenConnectorWorker#_bind_stage3_request_ids().
  _Stage3SubmitTask.pending: _Stage3SubmitTask#pending.
  _reshard_advertise_host: _reshard_advertise_host().
  TPUConnectorScheduler.kv_port: TPUConnectorScheduler#kv_port.
  TPURaidenConnectorWorker._stage3_submitted_load_metas: TPURaidenConnectorWorker#_stage3_submitted_load_metas.
  TPURaidenConnectorWorker._stage3_submit_outcomes: TPURaidenConnectorWorker#_stage3_submit_outcomes.
  TPURaidenConnectorWorker._stage3_prune_state_send_tracking: TPURaidenConnectorWorker#_stage3_prune_state_send_tracking().
  TPURaidenConnectorWorker._flattened_kv_cache_tensors: TPURaidenConnectorWorker#_flattened_kv_cache_tensors().
  TPURaidenConnectorWorker._rank_control_port: TPURaidenConnectorWorker#_rank_control_port().
  TPURaidenConnectorScheduler: TPURaidenConnectorScheduler#
  _Stage3Dsv4Pool.tag: _Stage3Dsv4Pool#tag.
  _Stage3Dsv4GroupPages.pages: _Stage3Dsv4GroupPages#pages.
  _Stage3LoadMeta.num_tokens: _Stage3LoadMeta#num_tokens.
  _Stage3PendingSubmit: _Stage3PendingSubmit#
  _Stage3PendingSubmit.num_tokens: _Stage3PendingSubmit#num_tokens.
  TPUConnector.on_new_request: TPUConnector#on_new_request().
  TPUConnector.get_num_new_matched_tokens: TPUConnector#get_num_new_matched_tokens().
  TPUConnector.update_state_after_alloc: TPUConnector#update_state_after_alloc().
  TPUConnector.request_finished: TPUConnector#request_finished().
  TPUConnector.get_finished_count: TPUConnector#get_finished_count().
  TPUConnector.get_kv_connector_stats: TPUConnector#get_kv_connector_stats().
  TPUConnector.build_kv_connector_stats: TPUConnector#build_kv_connector_stats().
  TPUConnector.get_finished: TPUConnector#get_finished().
  TPUConnector.update_connector_output: TPUConnector#update_connector_output().
  TPUConnectorScheduler.on_new_request: TPUConnectorScheduler#on_new_request().
  TPUConnectorScheduler.get_finished_count: TPUConnectorScheduler#get_finished_count().
  TPUConnectorWorker.process_send_load: TPUConnectorWorker#process_send_load().
  TPURaidenConnectorScheduler._stage3_active_source_req_ids: TPURaidenConnectorScheduler#_stage3_active_source_req_ids.
  TPURaidenConnectorScheduler._stage3_early_sends: TPURaidenConnectorScheduler#_stage3_early_sends.
  TPURaidenConnectorWorker._raiden_admission_summary: TPURaidenConnectorWorker#_raiden_admission_summary.
  TPURaidenConnectorWorker._stage3_tp_submits: TPURaidenConnectorWorker#_stage3_tp_submits.
  TPURaidenConnectorWorker._reported_recving: TPURaidenConnectorWorker#_reported_recving.
  TPURaidenConnectorWorker._local_head_count: TPURaidenConnectorWorker#_local_head_count().
  _as_int_list: _as_int_list().
  _reshard_service_port: _reshard_service_port().
  _prefix_aware_load_requested: _prefix_aware_load_requested().
  TPURaidenConnectorWorker.node_id: TPURaidenConnectorWorker#node_id.
  TPURaidenConnectorWorker._stage3_dsv4_transfer_groups: TPURaidenConnectorWorker#_stage3_dsv4_transfer_groups.
  TPURaidenConnectorWorker._stage3_fa_token_bytes: TPURaidenConnectorWorker#_stage3_fa_token_bytes().
  TPURaidenConnectorWorker._stage3_source_request_id: TPURaidenConnectorWorker#_stage3_source_request_id().
  TPURaidenConnectorWorker._stage3_destination_request_id: TPURaidenConnectorWorker#_stage3_destination_request_id().
  TPURaidenConnectorWorker._max_request_blocks: TPURaidenConnectorWorker#_max_request_blocks().
  _Stage3TransferGroup.window_tokens: _Stage3TransferGroup#window_tokens.
  _Stage3Dsv4Pool: _Stage3Dsv4Pool#
  _Stage3Dsv4Pool.plan_position: _Stage3Dsv4Pool#plan_position.
  _Stage3LoadMeta.uuid: _Stage3LoadMeta#uuid.
  _Stage3LoadMeta.src_controller_address: _Stage3LoadMeta#src_controller_address.
  _Stage3LoadMeta.src_job_name: _Stage3LoadMeta#src_job_name.
  _Stage3LoadMeta.src_engine_id: _Stage3LoadMeta#src_engine_id.
  _Stage3LoadMeta.src_data_replica_idx: _Stage3LoadMeta#src_data_replica_idx.
  _Stage3LoadMeta.src_parallelism: _Stage3LoadMeta#src_parallelism.
  _Stage3PendingSubmit.req_meta: _Stage3PendingSubmit#req_meta.
  _Stage3PendingSubmit.source_req_id: _Stage3PendingSubmit#source_req_id.
  _Stage3PendingSubmit.uuid: _Stage3PendingSubmit#uuid.
  _Stage3PendingSubmit.defer_deadline: _Stage3PendingSubmit#defer_deadline.
  _Stage3PendingSubmit.task: _Stage3PendingSubmit#task.
  _Stage3SubmitTask: _Stage3SubmitTask#
  _Stage3SubmitTask.call_kwargs: _Stage3SubmitTask#call_kwargs.
  _Stage3SubmitOutcome.submit_ms: _Stage3SubmitOutcome#submit_ms.
  _Stage3SubmitOutcome.attempted_at: _Stage3SubmitOutcome#attempted_at.
  TPUConnector.use_raiden: TPUConnector#use_raiden.
  TPUConnector._stage3_fa_group_index: TPUConnector#_stage3_fa_group_index.
  TPURaidenConnectorScheduler._stage3_fa_group_index: TPURaidenConnectorScheduler#_stage3_fa_group_index.
  TPURaidenConnectorWorker.named_kv_caches: TPURaidenConnectorWorker#named_kv_caches.
  TPURaidenConnectorWorker._pending_failed_recving: TPURaidenConnectorWorker#_pending_failed_recving.
  TPURaidenConnectorWorker._reshard_store: TPURaidenConnectorWorker#_reshard_store.
  TPURaidenConnectorWorker._stage3_submitted_load_tokens: TPURaidenConnectorWorker#_stage3_submitted_load_tokens.
  TPURaidenConnectorWorker._legacy_registered_sends: TPURaidenConnectorWorker#_legacy_registered_sends.
  TPURaidenConnectorWorker._legacy_submitted_loads: TPURaidenConnectorWorker#_legacy_submitted_loads.
  TPURaidenConnectorWorker._stage3_source_req_ids: TPURaidenConnectorWorker#_stage3_source_req_ids.
  TPURaidenConnectorWorker._stage3_submit_queue: TPURaidenConnectorWorker#_stage3_submit_queue.
  TPURaidenConnectorWorker._stage3_submit_lock: TPURaidenConnectorWorker#_stage3_submit_lock.
  TPURaidenConnectorWorker._new_raiden_controller_facade: TPURaidenConnectorWorker#_new_raiden_controller_facade().
  TPURaidenConnectorWorker: TPURaidenConnectorWorker#
  _prefix_aware_load_supported: _prefix_aware_load_supported().
  TPUConnector: TPUConnector#
  TPURaidenConnectorScheduler.update_connector_output: TPURaidenConnectorScheduler#update_connector_output().
  TPURaidenConnectorWorker.host_ip: TPURaidenConnectorWorker#host_ip.
  TPURaidenConnectorWorker._stage3_fail_uncertain_loads_early: TPURaidenConnectorWorker#_stage3_fail_uncertain_loads_early.
  TPURaidenConnectorWorker._measure_raiden_dsv4_layout: TPURaidenConnectorWorker#_measure_raiden_dsv4_layout().
  TPURaidenConnectorWorker._measure_raiden_fa_layout: TPURaidenConnectorWorker#_measure_raiden_fa_layout().
  TPUConnectorWorker: TPUConnectorWorker#
  _STAGE3_FINISH_DEDUP_LIMIT: _STAGE3_FINISH_DEDUP_LIMIT.
  _STAGE3_REGISTRATION_CANCELLED_ERROR: _STAGE3_REGISTRATION_CANCELLED_ERROR.
  _KV_PARAMS_ADMITTED: _KV_PARAMS_ADMITTED.
  _KV_PARAMS_REJECTED: _KV_PARAMS_REJECTED.
  _Stage3Dsv4Pool.page_tokens: _Stage3Dsv4Pool#page_tokens.
  _Stage3Dsv4Pool.live_bytes_per_block: _Stage3Dsv4Pool#live_bytes_per_block.
  _Stage3Dsv4Pool.row_bytes: _Stage3Dsv4Pool#row_bytes.
  _Stage3Dsv4GroupPages: _Stage3Dsv4GroupPages#
  _Stage3LoadMeta.local_block_ids: _Stage3LoadMeta#local_block_ids.
  _Stage3LoadMeta.report_completion: _Stage3LoadMeta#report_completion.
  _Stage3PendingSubmit.wait_logged: _Stage3PendingSubmit#wait_logged.
  _Stage3SubmitTask.facade: _Stage3SubmitTask#facade.
  _Stage3RegisteredSend.finish_pending: _Stage3RegisteredSend#finish_pending.
  _get_extra_config: _get_extra_config().
  TPURaidenConnectorScheduler._stage3_mamba_num_speculative_blocks: TPURaidenConnectorScheduler#_stage3_mamba_num_speculative_blocks.
  TPURaidenConnectorScheduler._stage3_early_requests: TPURaidenConnectorScheduler#_stage3_early_requests.
  TPURaidenConnectorScheduler._stage3_block_tables: TPURaidenConnectorScheduler#_stage3_block_tables.
  TPURaidenConnectorWorker._pending_failed_block_ids: TPURaidenConnectorWorker#_pending_failed_block_ids.
  TPURaidenConnectorWorker._stage3_load_start_times: TPURaidenConnectorWorker#_stage3_load_start_times.
  TPURaidenConnectorWorker._new_raiden_id: TPURaidenConnectorWorker#_new_raiden_id().
  _DONE_FUTURE: _DONE_FUTURE.
  TPUConnector.build_prom_metrics: TPUConnector#build_prom_metrics().
  TPUConnector.get_block_ids_with_load_errors: TPUConnector#get_block_ids_with_load_errors().
  TPURaidenConnector: TPURaidenConnector#
  TPUConnectorWorker._stage_d2h: TPUConnectorWorker#_stage_d2h().
  TPUConnectorWorker._stage_d2h_sync: TPUConnectorWorker#_stage_d2h_sync().
  TPUConnectorWorker._h2d_into_device: TPUConnectorWorker#_h2d_into_device().
  TPUConnectorWorker._h2d_into_device_async: TPUConnectorWorker#_h2d_into_device_async().
  TPUConnectorWorker._synchronize_device: TPUConnectorWorker#_synchronize_device().
  TPURaidenConnectorScheduler.__init__: TPURaidenConnectorScheduler#__init__().
  TPURaidenConnectorWorker.raiden_admission_summary: TPURaidenConnectorWorker#raiden_admission_summary().
  TPURaidenConnectorWorker.get_block_ids_with_load_errors: TPURaidenConnectorWorker#get_block_ids_with_load_errors().
  _STAGE3_STATE_CLASS_TAGS: _STAGE3_STATE_CLASS_TAGS.
  _STAGE3_UNREACHABLE_SOURCE_BACKOFF_S: _STAGE3_UNREACHABLE_SOURCE_BACKOFF_S.
  _select_committed_mamba_blocks: _select_committed_mamba_blocks().
  _STAGE3_NULL_BLOCK_ID: _STAGE3_NULL_BLOCK_ID.
  _stage3_skipped_window_pages: _stage3_skipped_window_pages().
  _Stage3Dsv4GroupPages.num_tokens: _Stage3Dsv4GroupPages#num_tokens.
  _Stage3LoadMeta.release_only: _Stage3LoadMeta#release_only.
  _Stage3PendingSubmit.dst_controller_address: _Stage3PendingSubmit#dst_controller_address.
  _Stage3PendingSubmit.dst_units: _Stage3PendingSubmit#dst_units.
  _Stage3PendingSubmit.first_attempt_s: _Stage3PendingSubmit#first_attempt_s.
  _Stage3PendingSubmit.last_attempt_s: _Stage3PendingSubmit#last_attempt_s.
  _Stage3SubmitTask.skip_tokens: _Stage3SubmitTask#skip_tokens.
  _Stage3SubmitTask.fa_skip_bytes: _Stage3SubmitTask#fa_skip_bytes.
  _Stage3SubmitTask.source_units: _Stage3SubmitTask#source_units.
  _Stage3SubmitTask.retry_inline: _Stage3SubmitTask#retry_inline.
  stage3_fa_raiden_id_fields: stage3_fa_raiden_id_fields().
  _is_kimi: _is_kimi().
  TPURaidenConnectorScheduler._incomplete_pages: TPURaidenConnectorScheduler#_incomplete_pages().
  TPURaidenConnectorScheduler._stage3_transfer_tokens: TPURaidenConnectorScheduler#_stage3_transfer_tokens().
  TPURaidenConnectorWorker._raiden_layout_fingerprint_payload: TPURaidenConnectorWorker#_raiden_layout_fingerprint_payload.
  TPURaidenConnectorWorker._raiden_controller_facade: TPURaidenConnectorWorker#_raiden_controller_facade.
  TPURaidenConnectorWorker._raiden_controller_address: TPURaidenConnectorWorker#_raiden_controller_address.
  TPURaidenConnectorWorker._stage3_unreachable_sources: TPURaidenConnectorWorker#_stage3_unreachable_sources.
  TPURaidenConnectorWorker._stage3_submit_threads: TPURaidenConnectorWorker#_stage3_submit_threads.
  TPURaidenConnectorWorker._raiden_hbm_memory_type: TPURaidenConnectorWorker#_raiden_hbm_memory_type().
  TPURaidenConnectorWorker.signature: TPURaidenConnectorWorker#signature().
  TPURaidenConnectorWorker._stage3_source_down: TPURaidenConnectorWorker#_stage3_source_down().
  TPURaidenConnectorWorker._wait_for_address_ready: TPURaidenConnectorWorker#_wait_for_address_ready().
  get_uuid: get_uuid().
  TPUConnectorScheduler: TPUConnectorScheduler#
  _DoneFuture: _DoneFuture#
  _STAGE3_D5_REGISTRATION_WAIT_S: _STAGE3_D5_REGISTRATION_WAIT_S.
  _STAGE3_REGISTRY_STATUS_UNKNOWN: _STAGE3_REGISTRY_STATUS_UNKNOWN.
  _STAGE3_REGISTRY_STATUS_CANCELLED: _STAGE3_REGISTRY_STATUS_CANCELLED.
  _STAGE3_REGISTRATION_REATTEMPT_MIN_INTERVAL_S: _STAGE3_REGISTRATION_REATTEMPT_MIN_INTERVAL_S.
  _STAGE3_GLM_TRANSFER_POOL_TAGS: _STAGE3_GLM_TRANSFER_POOL_TAGS.
  _STAGE3_SUBMIT_WORKERS: _STAGE3_SUBMIT_WORKERS.
  _STAGE3_LEGACY_ROUTING_FIELDS: _STAGE3_LEGACY_ROUTING_FIELDS.
  _stage3_group_window_tokens: _stage3_group_window_tokens().
  _Stage3LoadMeta.mamba_state_block_ids: _Stage3LoadMeta#mamba_state_block_ids.
  _Stage3LoadMeta.group_block_ids: _Stage3LoadMeta#group_block_ids.
  _Stage3LoadMeta.skip_tokens: _Stage3LoadMeta#skip_tokens.
  _Stage3LoadMeta.fail_only: _Stage3LoadMeta#fail_only.
  _as_bool: _as_bool().
  TPUConnector.force_raiden_connector: TPUConnector#force_raiden_connector.
  TPUConnectorScheduler.__init__: TPUConnectorScheduler#__init__().
  TPUConnectorScheduler.config: TPUConnectorScheduler#config.
  TPUConnectorScheduler._maybe_truncate_prompt_for_handoff: TPUConnectorScheduler#_maybe_truncate_prompt_for_handoff().
  TPURaidenConnectorScheduler._stage3_normalize_producer_blocks: TPURaidenConnectorScheduler#_stage3_normalize_producer_blocks().
  TPURaidenConnectorWorker.config: TPURaidenConnectorWorker#config.
  TPURaidenConnectorWorker._raiden_layout_fingerprint: TPURaidenConnectorWorker#_raiden_layout_fingerprint.
  TPURaidenConnectorWorker._new_raiden_manager: TPURaidenConnectorWorker#_new_raiden_manager().
  TPURaidenConnectorWorker._stage3_tp_group: TPURaidenConnectorWorker#_stage3_tp_group().
  __all__: __all__.
  _DoneFuture.wait: _DoneFuture#wait().
  TPUConnector.__init__: TPUConnector#__init__().
  TPUConnector.wait_for_layer_load: TPUConnector#wait_for_layer_load().
  TPUConnector.save_kv_layer: TPUConnector#save_kv_layer().
  TPUConnector.wait_for_save: TPUConnector#wait_for_save().
  TPURaidenConnector.force_raiden_connector: TPURaidenConnector#force_raiden_connector.
  TPUConnectorWorker._wait_stage: TPUConnectorWorker#_wait_stage().
  TPURaidenConnectorWorker.__init__: TPURaidenConnectorWorker#__init__().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py)

## Classes
### <a id="TPUConnector"></a>`TPUConnector`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:769`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L769)
- signature: `class TPUConnector(KVConnectorBase_V1, SupportsHMA):`
- members:
  - <a id="TPUConnector.build_connector_meta"></a>`build_connector_meta(self, scheduler_output: SchedulerOutput)` — [`L871`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L871)
  - <a id="TPUConnector.build_kv_connector_stats"></a>`build_kv_connector_stats(cls, data: dict[str, Any] | None = None)` — [`L959`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L959)
  - <a id="TPUConnector.build_prom_metrics"></a>`build_prom_metrics(cls, vllm_config: VllmConfig, metric_types: dict[type[PromMetric], type[PromMetricT]], labelnames: list[str], per_engine_labelvalues: dict[int, list[object]])` — [`L969`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L969)
  - <a id="TPUConnector.get_block_ids_with_load_errors"></a>`get_block_ids_with_load_errors(self)` — [`L1040`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1040)
  - <a id="TPUConnector.get_block_ids_with_load_errors_group_index"></a>`get_block_ids_with_load_errors_group_index(self)` — [`L1048`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1048) — Scopes Stage-3 load errors to the one transferred FA group.
  - <a id="TPUConnector.get_finished"></a>`get_finished(self, finished_req_ids: set[str])` — [`L1028`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1028)
  - <a id="TPUConnector.get_finished_count"></a>`get_finished_count(self)` — [`L946`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L946)
  - <a id="TPUConnector.get_kv_connector_stats"></a>`get_kv_connector_stats(self)` — [`L950`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L950) — Get the KV transfer stats for the connector.
  - <a id="TPUConnector.get_num_new_matched_tokens"></a>`get_num_new_matched_tokens(self, request: Request, num_computed_tokens: int)` — [`L855`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L855)
  - <a id="TPUConnector.get_transfer_results"></a>`get_transfer_results(self, finished_req_ids: set[str])` — [`L1032`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1032)
  - <a id="TPUConnector.on_new_request"></a>`on_new_request(self, request: Request)` — [`L851`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L851)
  - <a id="TPUConnector.register_kv_caches"></a>`register_kv_caches(self, kv_caches: dict[str, Any])` — [`L981`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L981) — Registers the named cache materialization when the backend needs it.
  - <a id="TPUConnector.register_runner"></a>`register_runner(self, runner: TPUModelRunner)` — [`L993`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L993)
  - <a id="TPUConnector.request_finished"></a>`request_finished(self, request: Request, block_ids: list[int])` — [`L878`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L878)
  - <a id="TPUConnector.request_finished_all_groups"></a>`request_finished_all_groups(self, request: Request, block_ids: tuple[list[int], ...])` — [`L886`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L886)
  - <a id="TPUConnector.save_kv_layer"></a>`save_kv_layer(self, *args, **kwargs)` — [`L1016`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1016) — Layer-wise save is not supported on TPU.
  - <a id="TPUConnector.start_load_kv"></a>`start_load_kv(self, _, wait_for_completion: bool = False, report_completion: bool = True, **kwargs)` — [`L997`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L997)
  - <a id="TPUConnector.supports_divergent_local_hybrid_hits"></a>`supports_divergent_local_hybrid_hits(self)` — [`L773`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L773) — Stage-3 suffix loads also restore the committed Mamba state.
  - <a id="TPUConnector.update_connector_output"></a>`update_connector_output(self, connector_output: Any)` — [`L1054`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1054) — Retires scheduler-side Stage-3 dedup state on real completion.
  - <a id="TPUConnector.update_state_after_alloc"></a>`update_state_after_alloc(self, request: Request, blocks: KVCacheBlocks, num_external_tokens: int)` — [`L863`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L863)
  - <a id="TPUConnector.wait_for_layer_load"></a>`wait_for_layer_load(self, layer_name: str)` — [`L1012`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1012) — Layer-wise load is not supported on TPU.
  - <a id="TPUConnector.wait_for_save"></a>`wait_for_save(self)` — [`L1020`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1020) — No-op. See comment in vllm_torchtpu's TPUConnector: reqs_to_send is
  - <a id="TPUConnector.connector_scheduler"></a>`connector_scheduler` — [`L832`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L832)
  - <a id="TPUConnector.connector_worker"></a>`connector_worker` — [`L845`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L845)
  - <a id="TPUConnector.force_raiden_connector"></a>`force_raiden_connector` — [`L770`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L770)
  - <a id="TPUConnector.use_raiden"></a>`use_raiden` — [`L792`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L792)
- protocol/private: <a id="TPUConnector.__init__"></a>`__init__`[`L782`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L782), <a id="TPUConnector._connector_metadata"></a>`_connector_metadata`[`L790`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L790), <a id="TPUConnector._stage3_fa_group_index"></a>`_stage3_fa_group_index`[`L793`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L793), <a id="TPUConnector._stage3_mamba_group_indices"></a>`_stage3_mamba_group_indices`[`L803`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L803), <a id="TPUConnector._stage3_transfer_groups"></a>`_stage3_transfer_groups`[`L794`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L794)
- uses (calls/refs, reference-scoped): [`logger`](tpu_connector.md#logger), [`get_finished`](tpu_connector.md#TPURaidenConnectorWorker.get_finished), [`process_send_load`](tpu_connector.md#TPURaidenConnectorWorker.process_send_load), [`update_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler.update_state_after_alloc), [`get_kv_connector_stats`](tpu_connector.md#TPURaidenConnectorWorker.get_kv_connector_stats), [`register_runner`](tpu_connector.md#TPURaidenConnectorWorker.register_runner), [`data`](tpu_connector_stats.md#TpuKVConnectorStats.data), [`request_finished`](tpu_connector.md#TPURaidenConnectorScheduler.request_finished), [`TPUModelRunner`](../../runner/tpu_runner.md#TPUModelRunner), [`_use_raiden_stage3_transport`](tpu_connector.md#_use_raiden_stage3_transport), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`get_finished_count`](tpu_connector.md#TPURaidenConnectorScheduler.get_finished_count), [`_use_raiden_dsv4_admission`](tpu_connector.md#_use_raiden_dsv4_admission), [`build_connector_meta`](tpu_connector.md#TPURaidenConnectorScheduler.build_connector_meta), [`cache_group_index`](tpu_connector.md#_Stage3TransferGroup.cache_group_index), [`_stage3_transfer_groups`](tpu_connector.md#_stage3_transfer_groups), [`_stage3_transfer_groups`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_transfer_groups), [`get_num_new_matched_tokens`](tpu_connector.md#TPURaidenConnectorScheduler.get_num_new_matched_tokens), [`get_transfer_results`](tpu_connector.md#TPURaidenConnectorWorker.get_transfer_results), [`on_new_request`](tpu_connector.md#TPURaidenConnectorScheduler.on_new_request), [`_use_raiden_connector`](tpu_connector.md#_use_raiden_connector), [`TpuKVConnectorStats`](tpu_connector_stats.md#TpuKVConnectorStats), [`_prefix_aware_load_enabled`](tpu_connector.md#_prefix_aware_load_enabled), [`_stage3_mamba_group_indices`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_mamba_group_indices), [`_Stage3TransferGroup`](tpu_connector.md#_Stage3TransferGroup), [`TPURaidenConnectorScheduler`](tpu_connector.md#TPURaidenConnectorScheduler), [`TPURaidenConnectorWorker`](tpu_connector.md#TPURaidenConnectorWorker), [`_stage3_fa_group_index`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_fa_group_index), [`named_kv_caches`](tpu_connector.md#TPURaidenConnectorWorker.named_kv_caches), [`TPUConnectorWorker`](tpu_connector.md#TPUConnectorWorker), [`update_connector_output`](tpu_connector.md#TPURaidenConnectorScheduler.update_connector_output), [`_stage3_mamba_num_speculative_blocks`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_mamba_num_speculative_blocks), [`TPURaidenConnector`](tpu_connector.md#TPURaidenConnector), [`TPUConnectorScheduler`](tpu_connector.md#TPUConnectorScheduler), [`TpuKVConnectorPromMetrics`](tpu_connector_stats.md#TpuKVConnectorPromMetrics)
- used by: [`build_connector_worker_meta`](tpu_connector.md#TPURaidenConnector.build_connector_worker_meta), [`TPURaidenConnector`](tpu_connector.md#TPURaidenConnector)

### <a id="TPUConnectorScheduler"></a>`TPUConnectorScheduler`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:1075`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1075)
- members:
  - <a id="TPUConnectorScheduler._admit_kv_transfer_params"></a>`_admit_kv_transfer_params(self, request: Request)` — [`L1152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1152) — Returns whether a decoder request carries usable remote-KV params.
  - <a id="TPUConnectorScheduler._maybe_truncate_prompt_for_handoff"></a>`_maybe_truncate_prompt_for_handoff(self, request: Request)` — [`L1114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1114) — P-side: drop the last prompt token so P stops where the handoff does.
  - <a id="TPUConnectorScheduler._reject_kv_transfer_params"></a>`_reject_kv_transfer_params(self, request: Request, params: dict[str, Any], reason: str)` — [`L1220`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1220) — Marks the params unusable so every hook skips the remote load.
  - <a id="TPUConnectorScheduler._validate_load_params"></a>`_validate_load_params(self, request: Request, params: dict[str, Any])` — [`L1177`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1177) — Checks the ZMQ/legacy-Raiden routing fields.
  - <a id="TPUConnectorScheduler.build_connector_meta"></a>`build_connector_meta(self, scheduler_output: SchedulerOutput | None = None)` — [`L1312`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1312)
  - <a id="TPUConnectorScheduler.get_finished_count"></a>`get_finished_count(self)` — [`L1326`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1326)
  - <a id="TPUConnectorScheduler.get_num_new_matched_tokens"></a>`get_num_new_matched_tokens(self, request: Request, num_computed_tokens: int)` — [`L1233`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1233) — D workers use this to get the number of new tokens
  - <a id="TPUConnectorScheduler.on_new_request"></a>`on_new_request(self, request: Request)` — [`L1147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1147) — Validates decoder kv_transfer_params once at admission. The Raiden
  - <a id="TPUConnectorScheduler.request_finished"></a>`request_finished(self, request: Request, block_ids: list[int])` — [`L1329`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1329)
  - <a id="TPUConnectorScheduler.update_state_after_alloc"></a>`update_state_after_alloc(self, request: Request, blocks: KVCacheBlocks, num_external_tokens: int)` — [`L1274`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1274)
  - <a id="TPUConnectorScheduler.block_size"></a>`block_size` — [`L1082`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1082)
  - <a id="TPUConnectorScheduler.config"></a>`config` — [`L1079`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1079)
  - <a id="TPUConnectorScheduler.is_producer"></a>`is_producer` — [`L1080`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1080)
  - <a id="TPUConnectorScheduler.kv_ip"></a>`kv_ip` — [`L1089`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1089)
  - <a id="TPUConnectorScheduler.kv_port"></a>`kv_port` — [`L1103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1103)
  - <a id="TPUConnectorScheduler.reqs_to_load"></a>`reqs_to_load` — [`L1087`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1087)
  - <a id="TPUConnectorScheduler.reqs_to_send"></a>`reqs_to_send` — [`L1085`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1085)
  - <a id="TPUConnectorScheduler.side_channel_port"></a>`side_channel_port` — [`L1106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1106)
  - <a id="TPUConnectorScheduler.vllm_config"></a>`vllm_config` — [`L1077`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1077)
- protocol/private: <a id="TPUConnectorScheduler.__init__"></a>`__init__`[`L1076`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1076)
- uses (calls/refs, reference-scoped): [`logger`](tpu_connector.md#logger), [`update_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler.update_state_after_alloc), [`request_finished`](tpu_connector.md#TPURaidenConnectorScheduler.request_finished), [`_validate_load_params`](tpu_connector.md#TPURaidenConnectorScheduler._validate_load_params), [`uuid`](connector_metadata.md#LoadMeta.uuid), [`get_p2p_wait_pull_timeout`](../utils.md#get_p2p_wait_pull_timeout), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`_as_int`](tpu_connector.md#_as_int), [`local_block_ids`](connector_metadata.md#LoadMeta.local_block_ids), [`get_finished_count`](tpu_connector.md#TPURaidenConnectorScheduler.get_finished_count), [`remote_host`](connector_metadata.md#LoadMeta.remote_host), [`LoadMeta`](connector_metadata.md#LoadMeta), [`ReqId`](connector_metadata.md#ReqId), [`build_connector_meta`](tpu_connector.md#TPURaidenConnectorScheduler.build_connector_meta), [`remote_block_ids`](connector_metadata.md#LoadMeta.remote_block_ids), [`reqs_to_send`](connector_metadata.md#TPUConnectorMetadata.reqs_to_send), [`remote_port`](connector_metadata.md#LoadMeta.remote_port), [`uuid`](connector_metadata.md#SendMeta.uuid), [`get_num_new_matched_tokens`](tpu_connector.md#TPURaidenConnectorScheduler.get_num_new_matched_tokens), [`on_new_request`](tpu_connector.md#TPURaidenConnectorScheduler.on_new_request), [`_reject_kv_transfer_params`](tpu_connector.md#TPURaidenConnectorScheduler._reject_kv_transfer_params), [`reqs_to_load`](connector_metadata.md#TPUConnectorMetadata.reqs_to_load), [`_as_str`](tpu_connector.md#_as_str), [`get_kv_ports`](../utils.md#get_kv_ports), [`local_block_ids`](connector_metadata.md#SendMeta.local_block_ids), [`get_kv_ips`](../utils.md#get_kv_ips), [`remote_side_channel_port`](connector_metadata.md#LoadMeta.remote_side_channel_port), [`SendMeta`](connector_metadata.md#SendMeta), [`expiration_time`](connector_metadata.md#SendMeta.expiration_time), [`get_side_channel_port`](../utils.md#get_side_channel_port), [`_as_int_list`](tpu_connector.md#_as_int_list), [`_KV_PARAMS_ADMITTED`](tpu_connector.md#_KV_PARAMS_ADMITTED), [`_KV_PARAMS_REJECTED`](tpu_connector.md#_KV_PARAMS_REJECTED), [`get_uuid`](tpu_connector.md#get_uuid)
- used by: [`_stage3_publish_send`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_publish_send), [`_update_stage3_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler._update_stage3_state_after_alloc), [`_fail_load`](tpu_connector.md#TPURaidenConnectorScheduler._fail_load), [`_enqueue_stage3_release`](tpu_connector.md#TPURaidenConnectorScheduler._enqueue_stage3_release), [`update_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler.update_state_after_alloc), [`request_finished`](tpu_connector.md#TPURaidenConnectorScheduler.request_finished), [`_validate_load_params`](tpu_connector.md#TPURaidenConnectorScheduler._validate_load_params), [`_stage3_register_ahead_enabled`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_register_ahead_enabled), [`_stage3_mamba_group_indices`](tpu_connector.md#TPUConnector._stage3_mamba_group_indices), [`_request_finished_stage3`](tpu_connector.md#TPURaidenConnectorScheduler._request_finished_stage3), [`get_finished_count`](tpu_connector.md#TPURaidenConnectorScheduler.get_finished_count), [`build_connector_meta`](tpu_connector.md#TPURaidenConnectorScheduler.build_connector_meta), [`get_num_new_matched_tokens`](tpu_connector.md#TPURaidenConnectorScheduler.get_num_new_matched_tokens), [`on_new_request`](tpu_connector.md#TPURaidenConnectorScheduler.on_new_request), [`_reject_kv_transfer_params`](tpu_connector.md#TPURaidenConnectorScheduler._reject_kv_transfer_params), [`kv_port`](tpu_connector.md#TPURaidenConnectorScheduler.kv_port), [`_raiden_engine_id`](tpu_connector.md#TPURaidenConnectorScheduler._raiden_engine_id), [`_send_completion_enabled`](tpu_connector.md#TPURaidenConnectorScheduler._send_completion_enabled), [`TPURaidenConnectorScheduler`](tpu_connector.md#TPURaidenConnectorScheduler), [`__init__`](tpu_connector.md#TPURaidenConnectorScheduler.__init__)

### <a id="TPUConnectorWorker"></a>`TPUConnectorWorker`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:1377`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1377)
- members:
  - <a id="TPUConnectorWorker._maybe_enable_kv_scatter"></a>`_maybe_enable_kv_scatter(self)` — [`L1463`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1463) — Run the startup smoke test for the multi-layer scatter kernel
  - <a id="TPUConnectorWorker.process_send_load"></a>`process_send_load(self, metadata: TPUConnectorMetadata, wait_for_completion: bool = False, report_completion: bool = True)` — [`L1380`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1380)
- protocol/private: <a id="TPUConnectorWorker._build_d2h_views"></a>`_build_d2h_views`[`L1389`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1389), <a id="TPUConnectorWorker._h2d_into_device"></a>`_h2d_into_device`[`L1429`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1429), <a id="TPUConnectorWorker._h2d_into_device_async"></a>`_h2d_into_device_async`[`L1436`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1436), <a id="TPUConnectorWorker._stage_d2h"></a>`_stage_d2h`[`L1409`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1409), <a id="TPUConnectorWorker._stage_d2h_sync"></a>`_stage_d2h_sync`[`L1418`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1418), <a id="TPUConnectorWorker._synchronize_device"></a>`_synchronize_device`[`L1443`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1443), <a id="TPUConnectorWorker._try_fast_scatter"></a>`_try_fast_scatter`[`L1446`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1446), <a id="TPUConnectorWorker._wait_stage"></a>`_wait_stage`[`L1426`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1426)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../utils.md#synchronize_tensors), [`logger`](tpu_connector.md#logger), [`node_id`](zmq_shm_base.md#ZmqShmKvConnectorBase.node_id), [`tp_rank`](zmq_shm_base.md#ZmqShmKvConnectorBase.tp_rank), [`_coord_pool`](zmq_shm_base.md#ZmqShmKvConnectorBase._coord_pool), [`layer_view`](host_kv_shm.md#HostKVShmPool.layer_view), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`local_tp_rank`](zmq_shm_base.md#ZmqShmKvConnectorBase.local_tp_rank), [`runner`](zmq_shm_base.md#ZmqShmKvConnectorBase.runner), [`device`](zmq_shm_base.md#ZmqShmKvConnectorBase.device), [`is_producer`](zmq_shm_base.md#ZmqShmKvConnectorBase.is_producer), [`multi_layer_scatter_into`](kv_scatter.md#multi_layer_scatter_into), [`process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase.process_send_load), [`smoke_test_multi_layer_scatter`](kv_scatter.md#smoke_test_multi_layer_scatter), [`_kv_scatter_enabled`](zmq_shm_base.md#ZmqShmKvConnectorBase._kv_scatter_enabled), [`scatter_available`](kv_scatter.md#scatter_available), [`shape`](zmq_shm_base.md#ZmqShmKvConnectorBase.shape), [`ZmqShmKvConnectorBase`](zmq_shm_base.md#ZmqShmKvConnectorBase), [`dtype`](zmq_shm_base.md#ZmqShmKvConnectorBase.dtype), [`prepare_scatter_args`](kv_scatter.md#prepare_scatter_args)
- used by: [`_stage3_mamba_group_indices`](tpu_connector.md#TPUConnector._stage3_mamba_group_indices), [`process_send_load`](zmq_shm_base.md#ZmqShmKvConnectorBase.process_send_load), [`_synchronize_device`](zmq_shm_base.md#ZmqShmKvConnectorBase._synchronize_device), [`_wait_stage`](zmq_shm_base.md#ZmqShmKvConnectorBase._wait_stage), [`_h2d_into_device_async`](zmq_shm_base.md#ZmqShmKvConnectorBase._h2d_into_device_async), [`_try_fast_scatter`](zmq_shm_base.md#ZmqShmKvConnectorBase._try_fast_scatter), [`_h2d_into_device`](zmq_shm_base.md#ZmqShmKvConnectorBase._h2d_into_device), [`_maybe_enable_kv_scatter`](zmq_shm_base.md#ZmqShmKvConnectorBase._maybe_enable_kv_scatter), [`_stage_d2h`](zmq_shm_base.md#ZmqShmKvConnectorBase._stage_d2h), [`_stage_d2h_sync`](zmq_shm_base.md#ZmqShmKvConnectorBase._stage_d2h_sync)

### <a id="TPURaidenConnector"></a>`TPURaidenConnector`  ·  implements/extends TPUConnector
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:1061`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1061)
- doc: Explicit Raiden connector class for callers that prefer connector name
- signature: `class TPURaidenConnector(TPUConnector):`
- members:
  - <a id="TPURaidenConnector.build_connector_worker_meta"></a>`build_connector_worker_meta(self)` — [`L1067`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1067)
  - <a id="TPURaidenConnector.force_raiden_connector"></a>`force_raiden_connector` — [`L1065`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1065)
- uses (calls/refs, reference-scoped): [`connector_worker`](tpu_connector.md#TPUConnector.connector_worker), [`RaidenSendResults`](raiden_pd_completion.md#RaidenSendResults), [`take_pd_send_results`](tpu_connector.md#TPURaidenConnectorWorker.take_pd_send_results), [`TPURaidenConnectorWorker`](tpu_connector.md#TPURaidenConnectorWorker), [`TPUConnector`](tpu_connector.md#TPUConnector)
- used by: [`TPUConnector`](tpu_connector.md#TPUConnector)

### <a id="TPURaidenConnectorScheduler"></a>`TPURaidenConnectorScheduler`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:1506`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1506)
- members:
  - <a id="TPURaidenConnectorScheduler._enqueue_stage3_release"></a>`_enqueue_stage3_release(self, request: Request, *, report_completion: bool = False)` — [`L2094`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2094) — Full local hit, pre-pull abort or rejected params: nothing to pull;
  - <a id="TPURaidenConnectorScheduler._fail_load"></a>`_fail_load(self, request: Request, local_block_ids: list[int], reason: str)` — [`L2061`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2061) — Fails one admitted request's remote load. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorScheduler._stage3_normalize_producer_blocks"></a>`_stage3_normalize_producer_blocks(block_ids: Sequence[int], *, num_tokens: int, page_tokens: int, pcp_size: int)` — [`L2038`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2038) — Trims one producer block table to the transfer prefix.
  - <a id="TPURaidenConnectorScheduler._stage3_publish_send"></a>`_stage3_publish_send(self, request: Request, block_ids: list[int], mamba_block_ids: list[list[int]] | None, num_tokens: int, *, computed_tokens: int, group_block_ids: list[list[int]] | None = None, ahead: bool = False)` — [`L2319`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2319) — Enqueues the request's Stage-3 SendMeta for the workers and — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorScheduler._stage3_register_ahead"></a>`_stage3_register_ahead(self, scheduler_output: SchedulerOutput)` — [`L2152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2152) — Publishes a producer's Stage-3 send in the step whose chunk
  - <a id="TPURaidenConnectorScheduler._stage3_register_ahead_enabled"></a>`_stage3_register_ahead_enabled(self)` — [`L1582`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1582) — Whether this producer publishes a request's Stage-3 send in the
  - <a id="TPURaidenConnectorScheduler._stage3_transfer_tokens"></a>`_stage3_transfer_tokens(request: Request, computed_tokens: int)` — [`L2303`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2303) — Transfer extent of a producer request whose first
  - <a id="TPURaidenConnectorScheduler._stage3_truncates_prompt"></a>`_stage3_truncates_prompt(self)` — [`L1571`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1571) — Whether P must stop one token short of the prompt.
  - <a id="TPURaidenConnectorScheduler._update_stage3_state_after_alloc"></a>`_update_stage3_state_after_alloc(self, request: Request, blocks: KVCacheBlocks, num_external_tokens: int)` — [`L1856`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1856) — Declares a destination transfer without source physical IDs. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorScheduler.build_connector_meta"></a>`build_connector_meta(self, scheduler_output: SchedulerOutput | None = None)` — [`L2141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2141)
  - <a id="TPURaidenConnectorScheduler.get_finished_count"></a>`get_finished_count(self)` — [`L2595`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2595)
  - <a id="TPURaidenConnectorScheduler.get_num_new_matched_tokens"></a>`get_num_new_matched_tokens(self, request: Request, num_computed_tokens: int)` — [`L1725`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1725)
  - <a id="TPURaidenConnectorScheduler.on_new_request"></a>`on_new_request(self, request: Request)` — [`L1606`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1606) — Truncates the P-side prompt at admission, ahead of the scheduler's
  - <a id="TPURaidenConnectorScheduler.request_finished"></a>`request_finished(self, request: Request, block_ids: list[int], mamba_block_ids: list[list[int]] | None = None, group_block_ids: list[list[int]] | None = None)` — [`L2224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2224)
  - <a id="TPURaidenConnectorScheduler.update_connector_output"></a>`update_connector_output(self, connector_output: Any)` — [`L2591`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2591)
  - <a id="TPURaidenConnectorScheduler.update_state_after_alloc"></a>`update_state_after_alloc(self, request: Request, blocks: KVCacheBlocks, num_external_tokens: int)` — [`L1769`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1769)
  - <a id="TPURaidenConnectorScheduler.kv_port"></a>`kv_port` — [`L1562`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1562)
  - <a id="TPURaidenConnectorScheduler.reqs_to_release"></a>`reqs_to_release` — [`L1548`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1548)
- protocol/private: <a id="TPURaidenConnectorScheduler.__init__"></a>`__init__`[`L1509`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1509), <a id="TPURaidenConnectorScheduler._incomplete_pages"></a>`_incomplete_pages`[`L1913`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1913), <a id="TPURaidenConnectorScheduler._normalize"></a>`_normalize`[`L2374`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2374), <a id="TPURaidenConnectorScheduler._raiden_engine_id"></a>`_raiden_engine_id`[`L2023`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2023), <a id="TPURaidenConnectorScheduler._reject_kv_transfer_params"></a>`_reject_kv_transfer_params`[`L1712`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1712), <a id="TPURaidenConnectorScheduler._request_finished_stage3"></a>`_request_finished_stage3`[`L2250`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2250), <a id="TPURaidenConnectorScheduler._send_completion_enabled"></a>`_send_completion_enabled`[`L1511`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1511), <a id="TPURaidenConnectorScheduler._stage3_active_source_req_ids"></a>`_stage3_active_source_req_ids`[`L1540`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1540), <a id="TPURaidenConnectorScheduler._stage3_block_tables"></a>`_stage3_block_tables`[`L1546`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1546), <a id="TPURaidenConnectorScheduler._stage3_early_requests"></a>`_stage3_early_requests`[`L1545`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1545), <a id="TPURaidenConnectorScheduler._stage3_early_sends"></a>`_stage3_early_sends`[`L1547`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1547), <a id="TPURaidenConnectorScheduler._stage3_fa_group_index"></a>`_stage3_fa_group_index`[`L1534`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1534), <a id="TPURaidenConnectorScheduler._stage3_finished_sends"></a>`_stage3_finished_sends`[`L1531`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1531), <a id="TPURaidenConnectorScheduler._stage3_mamba_group_indices"></a>`_stage3_mamba_group_indices`[`L1536`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1536), <a id="TPURaidenConnectorScheduler._stage3_mamba_num_speculative_blocks"></a>`_stage3_mamba_num_speculative_blocks`[`L1537`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1537), <a id="TPURaidenConnectorScheduler._stage3_prefix_aware_load_enabled"></a>`_stage3_prefix_aware_load_enabled`[`L1513`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1513), <a id="TPURaidenConnectorScheduler._stage3_transfer_groups"></a>`_stage3_transfer_groups`[`L1535`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1535), <a id="TPURaidenConnectorScheduler._validate_load_params"></a>`_validate_load_params`[`L1619`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L1619)
- uses (calls/refs, reference-scoped): [`logger`](tpu_connector.md#logger), [`request_finished`](tpu_connector.md#TPUConnectorScheduler.request_finished), [`vllm_config`](tpu_connector.md#TPUConnectorScheduler.vllm_config), [`uuid`](connector_metadata.md#LoadMeta.uuid), [`get_p2p_wait_pull_timeout`](../utils.md#get_p2p_wait_pull_timeout), [`_admit_kv_transfer_params`](tpu_connector.md#TPUConnectorScheduler._admit_kv_transfer_params), [`_use_raiden_stage3_transport`](tpu_connector.md#_use_raiden_stage3_transport), [`_uses_tp_stage3_source`](tpu_connector.md#_uses_tp_stage3_source), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`_as_int`](tpu_connector.md#_as_int), [`local_block_ids`](connector_metadata.md#LoadMeta.local_block_ids), [`reqs_to_load`](tpu_connector.md#TPUConnectorScheduler.reqs_to_load), [`_engine_is_pipeline`](tpu_connector.md#_engine_is_pipeline), [`build_connector_meta`](tpu_connector.md#TPUConnectorScheduler.build_connector_meta), [`remote_host`](connector_metadata.md#LoadMeta.remote_host), [`LoadMeta`](connector_metadata.md#LoadMeta), [`ReqId`](connector_metadata.md#ReqId), [`_use_raiden_dsv4_admission`](tpu_connector.md#_use_raiden_dsv4_admission), [`cache_group_index`](tpu_connector.md#_Stage3TransferGroup.cache_group_index), [`remote_block_ids`](connector_metadata.md#LoadMeta.remote_block_ids), [`remote_port`](connector_metadata.md#LoadMeta.remote_port), [`uuid`](connector_metadata.md#SendMeta.uuid), [`_use_raiden_glm_admission`](tpu_connector.md#_use_raiden_glm_admission), [`_raiden_dst_dcp_size`](tpu_connector.md#_raiden_dst_dcp_size), [`_validate_load_params`](tpu_connector.md#TPUConnectorScheduler._validate_load_params), [`_resolved_reshard_controller_address`](tpu_connector.md#_resolved_reshard_controller_address), [`is_producer`](tpu_connector.md#TPUConnectorScheduler.is_producer), [`_as_str`](tpu_connector.md#_as_str), [`_raiden_dst_shards`](tpu_connector.md#_raiden_dst_shards), [`_pipeline_parallel_size`](tpu_connector.md#_pipeline_parallel_size), [`kv_ip`](tpu_connector.md#TPUConnectorScheduler.kv_ip), [`reqs_to_send`](tpu_connector.md#TPUConnectorScheduler.reqs_to_send), [`_reject_kv_transfer_params`](tpu_connector.md#TPUConnectorScheduler._reject_kv_transfer_params), [`get_kv_ports`](../utils.md#get_kv_ports), [`get_raiden_inline_load`](../utils.md#get_raiden_inline_load), [`_prefix_aware_load_enabled`](tpu_connector.md#_prefix_aware_load_enabled), [`_raiden_dst_interleave_tokens`](tpu_connector.md#_raiden_dst_interleave_tokens), [`local_block_ids`](connector_metadata.md#SendMeta.local_block_ids), [`page_tokens`](tpu_connector.md#_Stage3TransferGroup.page_tokens), [`block_size`](tpu_connector.md#TPUConnectorScheduler.block_size)  (+46 more)
- used by: [`connector_scheduler`](tpu_connector.md#TPUConnector.connector_scheduler), [`request_finished`](tpu_connector.md#TPUConnectorScheduler.request_finished), [`update_state_after_alloc`](tpu_connector.md#TPUConnectorScheduler.update_state_after_alloc), [`request_finished_all_groups`](tpu_connector.md#TPUConnector.request_finished_all_groups), [`_stage3_mamba_group_indices`](tpu_connector.md#TPUConnector._stage3_mamba_group_indices), [`build_connector_meta`](tpu_connector.md#TPUConnectorScheduler.build_connector_meta), [`_validate_load_params`](tpu_connector.md#TPUConnectorScheduler._validate_load_params), [`_reject_kv_transfer_params`](tpu_connector.md#TPUConnectorScheduler._reject_kv_transfer_params), [`build_connector_meta`](tpu_connector.md#TPUConnector.build_connector_meta), [`get_num_new_matched_tokens`](tpu_connector.md#TPUConnectorScheduler.get_num_new_matched_tokens), [`get_finished_count`](tpu_connector.md#TPUConnector.get_finished_count), [`get_finished_count`](tpu_connector.md#TPUConnectorScheduler.get_finished_count), [`get_num_new_matched_tokens`](tpu_connector.md#TPUConnector.get_num_new_matched_tokens), [`on_new_request`](tpu_connector.md#TPUConnector.on_new_request), [`on_new_request`](tpu_connector.md#TPUConnectorScheduler.on_new_request), [`request_finished`](tpu_connector.md#TPUConnector.request_finished), [`update_connector_output`](tpu_connector.md#TPUConnector.update_connector_output), [`update_state_after_alloc`](tpu_connector.md#TPUConnector.update_state_after_alloc)

### <a id="TPURaidenConnectorWorker"></a>`TPURaidenConnectorWorker`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:2615`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2615)
- members:
  - <a id="TPURaidenConnectorWorker._admit_raiden_dsv4_kv_cache"></a>`_admit_raiden_dsv4_kv_cache(self, runner: TPUModelRunner)` — [`L3291`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3291) — Constructs the Raiden engine over DeepSeek-V4's cache classes. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._admit_raiden_glm_kv_cache"></a>`_admit_raiden_glm_kv_cache(self, runner: TPUModelRunner)` — [`L3080`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3080) — Constructs Raiden engine over the GLM MLA cache classes — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache"></a>`_admit_raiden_hybrid_kv_cache(self, runner: TPUModelRunner)` — [`L2864`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2864) — Construct the Raiden engine over the model's hybrid pools. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._apply_stage3_submit_outcome"></a>`_apply_stage3_submit_outcome(self, outcome: _Stage3SubmitOutcome)` — [`L6058`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6058) — Applies one RPC outcome to the scheduler-visible tables. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._bind_stage3_request_ids"></a>`_bind_stage3_request_ids(self, destination_req_id: str, source_req_id: str)` — [`L5420`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5420) — Binds the native/controller identity to the local scheduler ID.
  - <a id="TPURaidenConnectorWorker._dispatch_stage3_load_submit"></a>`_dispatch_stage3_load_submit(self, pending: _Stage3PendingSubmit, synchronous: bool = False)` — [`L5910`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5910) — Issues one coordination attempt for a staged load.
  - <a id="TPURaidenConnectorWorker._drain_stage3_pending_submits"></a>`_drain_stage3_pending_submits(self, finished_req_ids: set[str] | None)` — [`L6261`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6261) — Re-attempts parked Stage-3 loads once per scheduler step, paced
  - <a id="TPURaidenConnectorWorker._drain_stage3_submit_outcomes"></a>`_drain_stage3_submit_outcomes(self)` — [`L6223`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6223) — Applies actual RPC outcomes before releasing submission ownership.
  - <a id="TPURaidenConnectorWorker._execute_stage3_submit"></a>`_execute_stage3_submit(self, task: _Stage3SubmitTask)` — [`L6003`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6003) — Runs one coordination RPC; safe on any thread.
  - <a id="TPURaidenConnectorWorker._gdn_head_geometry"></a>`_gdn_head_geometry(self)` — [`L4040`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4040) — Use the compute path's QK replication and V-head ownership.
  - <a id="TPURaidenConnectorWorker._glm_dcp_producer_topology"></a>`_glm_dcp_producer_topology(self, supported: str)` — [`L3224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3224) — Validates a DCP producer, which holds a token shard per rank.
  - <a id="TPURaidenConnectorWorker._maybe_delay_stage3_registration_for_test"></a>`_maybe_delay_stage3_registration_for_test(metadata: TPUConnectorMetadata)` — [`L4217`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4217) — TEST-ONLY fault injection (TPU_RAIDEN_TEST_REGISTRATION_DELAY_S):
  - <a id="TPURaidenConnectorWorker._maybe_host_reshard_store"></a>`_maybe_host_reshard_store(self)` — [`L3672`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3672) — In-engine hosting (zero sidecars): each engine's transfer-rank-0
  - <a id="TPURaidenConnectorWorker._measure_dsv4_pool_plan"></a>`_measure_dsv4_pool_plan(self, manifest: Any, kv_cache_groups: Sequence[Any])` — [`L3388`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3388) — Builds one `_Stage3Dsv4Pool` per DSv4 tag in the manifest.
  - <a id="TPURaidenConnectorWorker._measure_glm_tag_geometry"></a>`_measure_glm_tag_geometry(manifest: Any)` — [`L4530`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4530) — Per-tag (live_bytes_per_block, row_bytes) of an admitted GLM
  - <a id="TPURaidenConnectorWorker._measure_stage3_layout"></a>`_measure_stage3_layout(self, manifest: Any)` — [`L3486`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3486) — Layout identity and page geometry of the admitted model.
  - <a id="TPURaidenConnectorWorker._probe_stage3_registrations"></a>`_probe_stage3_registrations(self, facade: Any, now: float)` — [`L5301`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5301) — Observes consumer-side cancellations of this rank's unclaimed
  - <a id="TPURaidenConnectorWorker._raiden_destination_work_units"></a>`_raiden_destination_work_units(self)` — [`L6301`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6301) — Every TP worker of this decode engine, in tp_rank order (the
  - <a id="TPURaidenConnectorWorker._raiden_dsv4_admission_topology"></a>`_raiden_dsv4_admission_topology(self)` — [`L3435`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3435) — Step 1: P and D run the same DP-attention sharding, so each rank
  - <a id="TPURaidenConnectorWorker._raiden_endpoint_identity"></a>`_raiden_endpoint_identity(self)` — [`L7016`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7016) — (endpoint rank, node id) of this worker's transfer engine.
  - <a id="TPURaidenConnectorWorker._raiden_glm_admission_topology"></a>`_raiden_glm_admission_topology(self)` — [`L3176`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3176) — Validates the supported topologies. Anything else fails closed here.
  - <a id="TPURaidenConnectorWorker._raiden_interleave_tokens"></a>`_raiden_interleave_tokens(self, page_tokens: int, transfer_parallelism: int)` — [`L3734`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3734) — Returns the kernel interleave driving byte-span lowering.
  - <a id="TPURaidenConnectorWorker._raiden_staging_blocks_per_pool"></a>`_raiden_staging_blocks_per_pool(self, manifest: Any, kv_cache_groups: Any)` — [`L7073`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7073) — Bounded host staging hints, one per pool in manifest order.
  - <a id="TPURaidenConnectorWorker._register_raiden_pools"></a>`_register_raiden_pools(self, engine: Any, manifest: Any, kv_cache_groups: Any)` — [`L7126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7126) — Registers the manifest's pools, with bounded host staging when the
  - <a id="TPURaidenConnectorWorker._register_raiden_stage3_work_unit"></a>`_register_raiden_stage3_work_unit(self, *, engine: Any, manifest: Any, controller_address: str)` — [`L3793`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3793) — Measure and register this worker with its cluster controller.
  - <a id="TPURaidenConnectorWorker._register_stage3_request_blocks"></a>`_register_stage3_request_blocks(self, metadata: TPUConnectorMetadata)` — [`L4239`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4239) — Registers only this PCP rank's interleaved physical source blocks. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4"></a>`_register_stage3_request_blocks_dsv4(self, metadata: TPUConnectorMetadata)` — [`L4810`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4810) — Registers this producer's span set, one registration per pool tag. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._register_stage3_request_row_spans"></a>`_register_stage3_request_row_spans(self, metadata: TPUConnectorMetadata)` — [`L4553`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4553) — Register this producer rank's row-granular span stripe. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._stage3_dsv4_group_blocks"></a>`_stage3_dsv4_group_blocks(self, req_meta: Any, num_tokens: int)` — [`L4767`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4767) — Each cache group's still-live pages, in plan order.
  - <a id="TPURaidenConnectorWorker._stage3_fa_registration_tags"></a>`_stage3_fa_registration_tags(self)` — [`L5068`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5068) — FA pool tags this rank declares spans for: the class tag, or one
  - <a id="TPURaidenConnectorWorker._stage3_fa_skip_bytes"></a>`_stage3_fa_skip_bytes(self, skip_tokens: int)` — [`L5763`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5763) — Use the same destination byte space for inline and queued submits.
  - <a id="TPURaidenConnectorWorker._stage3_fa_token_bytes"></a>`_stage3_fa_token_bytes(self, page_tokens: int)` — [`L5000`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5000) — Bytes per token of the admitted FA pools, measured from the
  - <a id="TPURaidenConnectorWorker._stage3_prune_state_send_tracking"></a>`_stage3_prune_state_send_tracking(self, base_req_id: str)` — [`L5251`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5251) — Drops producer terminal tracking with the base tombstone.
  - <a id="TPURaidenConnectorWorker._stage3_ready_producer_send_terminals"></a>`_stage3_ready_producer_send_terminals(self)` — [`L5278`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5278) — Returns terminal base requests (T3.1: no sibling aggregation). — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._stage3_record_producer_send_terminals"></a>`_stage3_record_producer_send_terminals(self, done_sending, failed_sending)` — [`L5255`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5255) — Records native terminals (T3.1: one uuid, base req ids only).
  - <a id="TPURaidenConnectorWorker._stage3_release_producer_registration"></a>`_stage3_release_producer_registration(self, destination_req_id: str, req_meta: _Stage3LoadMeta, synchronous: bool = False)` — [`L5459`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5459) — Full local hit: cancel the producer's unclaimed request-block
  - <a id="TPURaidenConnectorWorker._stage3_sharded_consumer"></a>`_stage3_sharded_consumer(self)` — [`L6311`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6311) — A head-sharded Qwen3.5 decode engine (dp{N}tp{tp}_decode): its TP
  - <a id="TPURaidenConnectorWorker._stage3_source_work_units"></a>`_stage3_source_work_units(self, req_meta: _Stage3LoadMeta)` — [`L4959`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4959) — Enumerates the producer units this destination pulls from: the
  - <a id="TPURaidenConnectorWorker._stage3_state_live_bytes"></a>`_stage3_state_live_bytes(self, tag: str)` — [`L5019`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5019) — Return the admitted whole-slot byte size for an exact state tag.
  - <a id="TPURaidenConnectorWorker._stage3_state_pool_spans"></a>`_stage3_state_pool_spans(self, mamba_state_block_ids, transfer_rank: int, parallelism: int)` — [`L5114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5114) — Producer: the GDN state classes' span registrations. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._stage3_state_regions"></a>`_stage3_state_regions(self, tag: str)` — [`L5038`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5038) — Return one uniform admitted live-region map for a state tag.
  - <a id="TPURaidenConnectorWorker._stage3_state_registration_tags"></a>`_stage3_state_registration_tags(self)` — [`L5083`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5083) — (exact state tag, mamba group ordinal) pairs this rank declares:
  - <a id="TPURaidenConnectorWorker._stage3_tp_group"></a>`_stage3_tp_group()` — [`L6329`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6329) — The TP cpu group for the leader broadcast, or None when no
  - <a id="TPURaidenConnectorWorker._stage_stage3_submit_task"></a>`_stage_stage3_submit_task(self, pending: _Stage3PendingSubmit, synchronous: bool)` — [`L5789`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5789) — Prepares the coordination call for one staged load. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._start_stage3_transfer_with_d5_retry"></a>`_start_stage3_transfer_with_d5_retry(facade: Any, **kwargs: Any)` — [`L5386`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5386) — Bridges the one-step P scheduler-to-worker registration window.
  - <a id="TPURaidenConnectorWorker._submit_stage3_load_as_leader"></a>`_submit_stage3_load_as_leader(self, *, req_meta: Any, source_req_id: str, destination_req_id: str, uuid: int, num_tokens: int, local_blocks: list, dst_controller_address: str, dst_units: list)` — [`L6339`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6339) — Runs the source-store coordination for one request and classifies
  - <a id="TPURaidenConnectorWorker._submit_stage3_loads"></a>`_submit_stage3_loads(self, metadata: TPUConnectorMetadata, engine: KVCacheManager, synchronous: bool = False)` — [`L5534`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5534) — Starts exactly one source-controller transfer per request. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker._sync_stage3_tp_submit_states"></a>`_sync_stage3_tp_submit_states(self)` — [`L6235`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6235) — Fan out final submission decisions, never rank-local timestamps.
  - <a id="TPURaidenConnectorWorker._validate_gdn_transfer_geometry"></a>`_validate_gdn_transfer_geometry(self, source: GdnHeadGeometry)` — [`L4052`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4052) — Reject state mappings the byte-span lowering cannot represent. — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="TPURaidenConnectorWorker._validate_stage3_transfer_parallelism"></a>`_validate_stage3_transfer_parallelism(self, transfer_parallelism: int)` — [`L3546`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3546) — The producer must shard the transfer over exactly the rank set its
  - <a id="TPURaidenConnectorWorker.get_block_ids_with_load_errors"></a>`get_block_ids_with_load_errors(self)` — [`L6887`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6887)
  - <a id="TPURaidenConnectorWorker.get_finished"></a>`get_finished(self, finished_req_ids: set[str] | None = None)` — [`L6459`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6459) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker.get_kv_connector_stats"></a>`get_kv_connector_stats(self)` — [`L2786`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2786)
  - <a id="TPURaidenConnectorWorker.get_transfer_results"></a>`get_transfer_results(self, finished_req_ids: set[str] | None = None)` — [`L6576`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6576)
  - <a id="TPURaidenConnectorWorker.process_send_load"></a>`process_send_load(self, metadata: TPUConnectorMetadata, wait_for_completion: bool = False, report_completion: bool = True)` — [`L4090`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4090) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker.raiden_admission_summary"></a>`raiden_admission_summary(self)` — [`L3892`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3892)
  - <a id="TPURaidenConnectorWorker.register_runner"></a>`register_runner(self, runner: TPUModelRunner)` — [`L2810`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2810)
  - <a id="TPURaidenConnectorWorker.signature"></a>`signature(pool: Any)` — [`L5048`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5048)
  - <a id="TPURaidenConnectorWorker.take_pd_send_results"></a>`take_pd_send_results(self)` — [`L5378`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5378)
  - <a id="TPURaidenConnectorWorker.config"></a>`config` — [`L2625`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2625)
  - <a id="TPURaidenConnectorWorker.dp_rank"></a>`dp_rank` — [`L2637`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2637)
  - <a id="TPURaidenConnectorWorker.host_ip"></a>`host_ip` — [`L2642`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2642)
  - <a id="TPURaidenConnectorWorker.is_producer"></a>`is_producer` — [`L2626`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2626)
  - <a id="TPURaidenConnectorWorker.kv_transfer_port"></a>`kv_transfer_port` — [`L2643`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2643)
  - <a id="TPURaidenConnectorWorker.named_kv_caches"></a>`named_kv_caches` — [`L2647`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2647)
  - <a id="TPURaidenConnectorWorker.node_id"></a>`node_id` — [`L2634`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2634)
  - <a id="TPURaidenConnectorWorker.runner"></a>`runner` — [`L2633`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2633)
  - <a id="TPURaidenConnectorWorker.tp_rank"></a>`tp_rank` — [`L2635`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2635)
  - <a id="TPURaidenConnectorWorker.tp_size"></a>`tp_size` — [`L2636`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2636)
  - <a id="TPURaidenConnectorWorker.transfer_stats"></a>`transfer_stats` — [`L2756`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2756) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
  - <a id="TPURaidenConnectorWorker.vllm_config"></a>`vllm_config` — [`L2623`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2623)
- protocol/private: <a id="TPURaidenConnectorWorker.__init__"></a>`__init__`[`L2622`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2622), <a id="TPURaidenConnectorWorker._construct_raiden_transfer_engine"></a>`_construct_raiden_transfer_engine`[`L6939`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6939), <a id="TPURaidenConnectorWorker._done_recving"></a>`_done_recving`[`L2736`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2736), <a id="TPURaidenConnectorWorker._done_sending"></a>`_done_sending`[`L2735`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2735), <a id="TPURaidenConnectorWorker._ensure_raiden_transfer_engine"></a>`_ensure_raiden_transfer_engine`[`L6928`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6928), <a id="TPURaidenConnectorWorker._ensure_stage3_submit_workers"></a>`_ensure_stage3_submit_workers`[`L5941`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5941), <a id="TPURaidenConnectorWorker._failed_block_ids"></a>`_failed_block_ids`[`L2749`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2749), <a id="TPURaidenConnectorWorker._failed_recving"></a>`_failed_recving`[`L2737`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2737), <a id="TPURaidenConnectorWorker._flattened_kv_cache_tensors"></a>`_flattened_kv_cache_tensors`[`L6918`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6918), <a id="TPURaidenConnectorWorker._get_raiden_stats"></a>`_get_raiden_stats`[`L2770`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2770), <a id="TPURaidenConnectorWorker._legacy_registered_sends"></a>`_legacy_registered_sends`[`L2668`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2668), <a id="TPURaidenConnectorWorker._legacy_submitted_loads"></a>`_legacy_submitted_loads`[`L2669`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2669), <a id="TPURaidenConnectorWorker._load_block_ids"></a>`_load_block_ids`[`L2747`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2747), <a id="TPURaidenConnectorWorker._local_head_count"></a>`_local_head_count`[`L4026`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4026), <a id="TPURaidenConnectorWorker._local_raiden_transfer_rank"></a>`_local_raiden_transfer_rank`[`L3620`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3620), <a id="TPURaidenConnectorWorker._mark_stage3_source_unreachable"></a>`_mark_stage3_source_unreachable`[`L5992`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5992), <a id="TPURaidenConnectorWorker._max_request_blocks"></a>`_max_request_blocks`[`L7055`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7055), <a id="TPURaidenConnectorWorker._measure_raiden_dsv4_layout"></a>`_measure_raiden_dsv4_layout`[`L3451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3451), <a id="TPURaidenConnectorWorker._measure_raiden_fa_layout"></a>`_measure_raiden_fa_layout`[`L3461`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3461), <a id="TPURaidenConnectorWorker._measure_raiden_glm_layout"></a>`_measure_raiden_glm_layout`[`L3471`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3471), <a id="TPURaidenConnectorWorker._model_config_int"></a>`_model_config_int`[`L4017`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4017), <a id="TPURaidenConnectorWorker._new_raiden_controller_facade"></a>`_new_raiden_controller_facade`[`L3595`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3595), <a id="TPURaidenConnectorWorker._new_raiden_id"></a>`_new_raiden_id`[`L3604`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3604), <a id="TPURaidenConnectorWorker._new_raiden_manager"></a>`_new_raiden_manager`[`L3609`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3609), <a id="TPURaidenConnectorWorker._num_raiden_slots"></a>`_num_raiden_slots`[`L7175`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7175), <a id="TPURaidenConnectorWorker._pd_send_results"></a>`_pd_send_results`[`L2628`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2628), <a id="TPURaidenConnectorWorker._pending_failed_block_ids"></a>`_pending_failed_block_ids`[`L2632`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2632), <a id="TPURaidenConnectorWorker._pending_failed_recving"></a>`_pending_failed_recving`[`L2631`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2631), <a id="TPURaidenConnectorWorker._poll_finished"></a>`_poll_finished`[`L6597`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6597), <a id="TPURaidenConnectorWorker._raiden_admission_summary"></a>`_raiden_admission_summary`[`L2648`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2648), <a id="TPURaidenConnectorWorker._raiden_controller_address"></a>`_raiden_controller_address`[`L2653`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2653), <a id="TPURaidenConnectorWorker._raiden_controller_facade"></a>`_raiden_controller_facade`[`L2652`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2652), <a id="TPURaidenConnectorWorker._raiden_engine_id"></a>`_raiden_engine_id`[`L3658`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3658), <a id="TPURaidenConnectorWorker._raiden_hbm_memory_type"></a>`_raiden_hbm_memory_type`[`L4955`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4955), <a id="TPURaidenConnectorWorker._raiden_hybrid_admission_topology"></a>`_raiden_hybrid_admission_topology`[`L3897`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3897), <a id="TPURaidenConnectorWorker._raiden_kimi_k3_admission_topology"></a>`_raiden_kimi_k3_admission_topology`[`L3902`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3902), <a id="TPURaidenConnectorWorker._raiden_layout_fingerprint"></a>`_raiden_layout_fingerprint`[`L2650`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2650), <a id="TPURaidenConnectorWorker._raiden_layout_fingerprint_payload"></a>`_raiden_layout_fingerprint_payload`[`L2651`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2651), <a id="TPURaidenConnectorWorker._raiden_manifest"></a>`_raiden_manifest`[`L2649`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2649), <a id="TPURaidenConnectorWorker._raiden_qwen35_admission_topology"></a>`_raiden_qwen35_admission_topology`[`L3934`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3934), <a id="TPURaidenConnectorWorker._raiden_stage3_enabled"></a>`_raiden_stage3_enabled`[`L2861`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2861), <a id="TPURaidenConnectorWorker._raiden_transfer_engine"></a>`_raiden_transfer_engine`[`L2646`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2646), <a id="TPURaidenConnectorWorker._raiden_transfer_parallelism"></a>`_raiden_transfer_parallelism`[`L3614`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3614), <a id="TPURaidenConnectorWorker._raiden_work_unit"></a>`_raiden_work_unit`[`L2656`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2656), <a id="TPURaidenConnectorWorker._raiden_work_unit_fields"></a>`_raiden_work_unit_fields`[`L3773`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3773), <a id="TPURaidenConnectorWorker._rank_control_port"></a>`_rank_control_port`[`L7034`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7034), <a id="TPURaidenConnectorWorker._record_stage3_load_failure"></a>`_record_stage3_load_failure`[`L4994`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4994), <a id="TPURaidenConnectorWorker._release"></a>`_release`[`L5492`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5492), <a id="TPURaidenConnectorWorker._reported_recving"></a>`_reported_recving`[`L2743`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2743), <a id="TPURaidenConnectorWorker._require_stage3_controller"></a>`_require_stage3_controller`[`L4206`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L4206), <a id="TPURaidenConnectorWorker._reshard_store"></a>`_reshard_store`[`L2655`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2655), <a id="TPURaidenConnectorWorker._resolve_remote_endpoint"></a>`_resolve_remote_endpoint`[`L7039`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7039), <a id="TPURaidenConnectorWorker._stage3_controller_accepted"></a>`_stage3_controller_accepted`[`L2698`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2698), <a id="TPURaidenConnectorWorker._stage3_deferred_native_failures"></a>`_stage3_deferred_native_failures`[`L2734`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2734), <a id="TPURaidenConnectorWorker._stage3_destination_req_ids"></a>`_stage3_destination_req_ids`[`L2697`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2697), <a id="TPURaidenConnectorWorker._stage3_destination_request_id"></a>`_stage3_destination_request_id`[`L5453`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5453), <a id="TPURaidenConnectorWorker._stage3_dsv4_plan"></a>`_stage3_dsv4_plan`[`L2679`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2679), <a id="TPURaidenConnectorWorker._stage3_dsv4_transfer_groups"></a>`_stage3_dsv4_transfer_groups`[`L2681`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2681), <a id="TPURaidenConnectorWorker._stage3_fail_uncertain_loads_early"></a>`_stage3_fail_uncertain_loads_early`[`L2751`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2751), <a id="TPURaidenConnectorWorker._stage3_finished_loads_pending_cleanup"></a>`_stage3_finished_loads_pending_cleanup`[`L2704`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2704), <a id="TPURaidenConnectorWorker._stage3_inflight_submits"></a>`_stage3_inflight_submits`[`L2733`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2733), <a id="TPURaidenConnectorWorker._stage3_kimi"></a>`_stage3_kimi`[`L2627`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2627), <a id="TPURaidenConnectorWorker._stage3_load_start_times"></a>`_stage3_load_start_times`[`L2667`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2667), <a id="TPURaidenConnectorWorker._stage3_pending_controller_failures"></a>`_stage3_pending_controller_failures`[`L2709`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2709), <a id="TPURaidenConnectorWorker._stage3_pending_submits"></a>`_stage3_pending_submits`[`L2712`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2712), <a id="TPURaidenConnectorWorker._stage3_registered_sends"></a>`_stage3_registered_sends`[`L2660`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2660), <a id="TPURaidenConnectorWorker._stage3_reported_sends"></a>`_stage3_reported_sends`[`L2663`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2663), <a id="TPURaidenConnectorWorker._stage3_row_geometry"></a>`_stage3_row_geometry`[`L3023`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3023), <a id="TPURaidenConnectorWorker._stage3_send_outcomes"></a>`_stage3_send_outcomes`[`L2689`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2689), <a id="TPURaidenConnectorWorker._stage3_source_down"></a>`_stage3_source_down`[`L5983`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5983), <a id="TPURaidenConnectorWorker._stage3_source_facades"></a>`_stage3_source_facades`[`L2675`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2675), <a id="TPURaidenConnectorWorker._stage3_source_req_ids"></a>`_stage3_source_req_ids`[`L2696`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2696), <a id="TPURaidenConnectorWorker._stage3_source_request_id"></a>`_stage3_source_request_id`[`L5444`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5444), <a id="TPURaidenConnectorWorker._stage3_source_unreachable"></a>`_stage3_source_unreachable`[`L5977`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5977), <a id="TPURaidenConnectorWorker._stage3_state_group_count"></a>`_stage3_state_group_count`[`L2676`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2676), <a id="TPURaidenConnectorWorker._stage3_status_probe_next"></a>`_stage3_status_probe_next`[`L2691`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2691), <a id="TPURaidenConnectorWorker._stage3_submit_lock"></a>`_stage3_submit_lock`[`L2726`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2726), <a id="TPURaidenConnectorWorker._stage3_submit_outcomes"></a>`_stage3_submit_outcomes`[`L2727`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2727), <a id="TPURaidenConnectorWorker._stage3_submit_queue"></a>`_stage3_submit_queue`[`L2725`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2725), <a id="TPURaidenConnectorWorker._stage3_submit_threads"></a>`_stage3_submit_threads`[`L2729`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2729), <a id="TPURaidenConnectorWorker._stage3_submit_worker_loop"></a>`_stage3_submit_worker_loop`[`L5961`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L5961), <a id="TPURaidenConnectorWorker._stage3_submitted_load_metas"></a>`_stage3_submitted_load_metas`[`L2666`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2666), <a id="TPURaidenConnectorWorker._stage3_submitted_load_tokens"></a>`_stage3_submitted_load_tokens`[`L2665`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2665), <a id="TPURaidenConnectorWorker._stage3_submitted_loads"></a>`_stage3_submitted_loads`[`L2664`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2664), <a id="TPURaidenConnectorWorker._stage3_terminal_cleanup"></a>`_stage3_terminal_cleanup`[`L2662`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2662), <a id="TPURaidenConnectorWorker._stage3_terminal_loads"></a>`_stage3_terminal_loads`[`L2703`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2703), <a id="TPURaidenConnectorWorker._stage3_terminal_sends"></a>`_stage3_terminal_sends`[`L2661`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2661), <a id="TPURaidenConnectorWorker._stage3_tp_submits"></a>`_stage3_tp_submits`[`L2716`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2716), <a id="TPURaidenConnectorWorker._stage3_unreachable_sources"></a>`_stage3_unreachable_sources`[`L2728`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2728), <a id="TPURaidenConnectorWorker._suppress_done_recving"></a>`_suppress_done_recving`[`L2738`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L2738), <a id="TPURaidenConnectorWorker._validate_glm_dcp_destination"></a>`_validate_glm_dcp_destination`[`L3263`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L3263), <a id="TPURaidenConnectorWorker._wait_for_address_ready"></a>`_wait_for_address_ready`[`L6999`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6999), <a id="TPURaidenConnectorWorker._wait_for_recving"></a>`_wait_for_recving`[`L6894`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L6894)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../utils.md#synchronize_tensors), [`logger`](tpu_connector.md#logger), [`build_qwen35_pool_manifest`](raiden/pool_manifest.md#build_qwen35_pool_manifest), [`build_glm_mla_pool_manifest`](raiden/pool_manifest.md#build_glm_mla_pool_manifest), [`build_dsv4_pool_manifest`](raiden/pool_manifest.md#build_dsv4_pool_manifest), [`build_kimi_k3_pool_manifest`](raiden/pool_manifest.md#build_kimi_k3_pool_manifest), [`lower_fa_spans_sol`](raiden/seq_on_lane.md#lower_fa_spans_sol), [`sol_fa_geometry_from_manifest`](raiden/seq_on_lane.md#sol_fa_geometry_from_manifest), [`measured_sol_layout_fingerprint`](raiden/seq_on_lane.md#measured_sol_layout_fingerprint), [`derive_gdn_head_geometry`](../../kernels/gdn/head_geometry.md#derive_gdn_head_geometry), [`measured_fa_layout_fingerprint`](raiden/layout_fingerprint.md#measured_fa_layout_fingerprint), [`lower_glm_dcp_row_spans`](raiden/byte_spans.md#lower_glm_dcp_row_spans), [`lower_fa_spans`](raiden/byte_spans.md#lower_fa_spans), [`lower_glm_dcp_identity_spans`](raiden/byte_spans.md#lower_glm_dcp_identity_spans), [`lower_dsv4_row_spans`](raiden/byte_spans.md#lower_dsv4_row_spans), [`lower_glm_row_spans`](raiden/byte_spans.md#lower_glm_row_spans), [`TraceAnnotation`](../../tracing/annotation.md#TraceAnnotation), [`measured_kimi_k3_layout_fingerprint`](raiden/layout_fingerprint.md#measured_kimi_k3_layout_fingerprint), [`pools`](raiden/pool_manifest.md#PoolManifest.pools), [`data`](tpu_connector_stats.md#TpuKVConnectorStats.data), [`kv_cache_config`](../../runner/tpu_runner.md#TPUModelRunner.kv_cache_config), [`sol_fa_page_tokens`](raiden/seq_on_lane.md#sol_fa_page_tokens), [`geometry_by_tag`](raiden/pool_manifest.md#PoolManifest.geometry_by_tag), [`tag`](raiden/pool_manifest.md#PoolEntry.tag), [`TPUModelRunner`](../../runner/tpu_runner.md#TPUModelRunner), [`uuid`](connector_metadata.md#LoadMeta.uuid), [`uuid`](tpu_connector.md#_Stage3RegisteredSend.uuid), [`get_p2p_wait_pull_timeout`](../utils.md#get_p2p_wait_pull_timeout), [`_use_raiden_stage3_transport`](tpu_connector.md#_use_raiden_stage3_transport), [`_uses_tp_stage3_source`](tpu_connector.md#_uses_tp_stage3_source), [`class_tag`](raiden/tags.md#class_tag), [`spans`](raiden/byte_spans.md#PoolSpanRegistration.spans), [`TAG_FA`](raiden/tags.md#TAG_FA), [`TPUConnectorMetadata`](connector_metadata.md#TPUConnectorMetadata), [`fa_page_tokens`](raiden/layout_fingerprint.md#fa_page_tokens), [`lower_kda_state_shard_spans`](raiden/byte_spans.md#lower_kda_state_shard_spans), [`registration_source_bytes`](raiden/seq_on_lane.md#registration_source_bytes), [`TAG_GDN_CONV`](raiden/tags.md#TAG_GDN_CONV), [`local_block_ids`](connector_metadata.md#LoadMeta.local_block_ids), [`_engine_is_pipeline`](tpu_connector.md#_engine_is_pipeline)  (+178 more)
- used by: [`_stage3_mamba_group_indices`](tpu_connector.md#TPUConnector._stage3_mamba_group_indices), [`build_connector_worker_meta`](tpu_connector.md#TPURaidenConnector.build_connector_worker_meta), [`register_kv_caches`](tpu_connector.md#TPUConnector.register_kv_caches), [`start_load_kv`](tpu_connector.md#TPUConnector.start_load_kv), [`get_transfer_results`](tpu_connector.md#TPUConnector.get_transfer_results), [`register_runner`](tpu_connector.md#TPUConnector.register_runner), [`get_finished`](tpu_connector.md#TPUConnector.get_finished), [`get_kv_connector_stats`](tpu_connector.md#TPUConnector.get_kv_connector_stats)

### <a id="_DoneFuture"></a>`_DoneFuture`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:134`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L134)
- signature: `class _DoneFuture:`
- members:
  - <a id="_DoneFuture.wait"></a>`wait(self)` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L135)
- used by: [`_DONE_FUTURE`](tpu_connector.md#_DONE_FUTURE)

### <a id="_Stage3Dsv4GroupPages"></a>`_Stage3Dsv4GroupPages`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:371`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L371)
- doc: One cache group's transferable pages, and the tokens they hold.
- signature: `class _Stage3Dsv4GroupPages:`
- members:
  - <a id="_Stage3Dsv4GroupPages.num_tokens"></a>`num_tokens` — [`L379`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L379)
  - <a id="_Stage3Dsv4GroupPages.pages"></a>`pages` — [`L378`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L378)
- used by: [`_stage_stage3_submit_task`](tpu_connector.md#TPURaidenConnectorWorker._stage_stage3_submit_task), [`_register_stage3_request_blocks_dsv4`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4), [`_stage3_dsv4_group_blocks`](tpu_connector.md#TPURaidenConnectorWorker._stage3_dsv4_group_blocks)

### <a id="_Stage3Dsv4Pool"></a>`_Stage3Dsv4Pool`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L353)
- doc: One tag in the DSv4 transfer plan, and the geometry to move it.
- signature: `class _Stage3Dsv4Pool:`
- members:
  - <a id="_Stage3Dsv4Pool.live_bytes_per_block"></a>`live_bytes_per_block` — [`L364`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L364)
  - <a id="_Stage3Dsv4Pool.page_tokens"></a>`page_tokens` — [`L363`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L363)
  - <a id="_Stage3Dsv4Pool.plan_position"></a>`plan_position` — [`L362`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L362)
  - <a id="_Stage3Dsv4Pool.row_bytes"></a>`row_bytes` — [`L367`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L367)
  - <a id="_Stage3Dsv4Pool.tag"></a>`tag` — [`L358`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L358)
- used by: [`_stage_stage3_submit_task`](tpu_connector.md#TPURaidenConnectorWorker._stage_stage3_submit_task), [`_register_stage3_request_blocks_dsv4`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4), [`_admit_raiden_dsv4_kv_cache`](tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_dsv4_kv_cache), [`_measure_dsv4_pool_plan`](tpu_connector.md#TPURaidenConnectorWorker._measure_dsv4_pool_plan), [`_stage3_dsv4_plan`](tpu_connector.md#TPURaidenConnectorWorker._stage3_dsv4_plan)

### <a id="_Stage3LoadMeta"></a>`_Stage3LoadMeta`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:383`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L383)
- doc: Decode-local declaration for one controller-driven FA transfer.
- signature: `class _Stage3LoadMeta:`
- members:
  - <a id="_Stage3LoadMeta.fail_only"></a>`fail_only` — [`L422`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L422)
  - <a id="_Stage3LoadMeta.group_block_ids"></a>`group_block_ids` — [`L407`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L407)
  - <a id="_Stage3LoadMeta.local_block_ids"></a>`local_block_ids` — [`L393`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L393)
  - <a id="_Stage3LoadMeta.mamba_state_block_ids"></a>`mamba_state_block_ids` — [`L404`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L404)
  - <a id="_Stage3LoadMeta.num_tokens"></a>`num_tokens` — [`L394`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L394)
  - <a id="_Stage3LoadMeta.release_only"></a>`release_only` — [`L415`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L415)
  - <a id="_Stage3LoadMeta.report_completion"></a>`report_completion` — [`L420`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L420)
  - <a id="_Stage3LoadMeta.skip_tokens"></a>`skip_tokens` — [`L412`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L412)
  - <a id="_Stage3LoadMeta.source_req_id"></a>`source_req_id` — [`L392`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L392)
  - <a id="_Stage3LoadMeta.src_controller_address"></a>`src_controller_address` — [`L395`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L395)
  - <a id="_Stage3LoadMeta.src_data_replica_idx"></a>`src_data_replica_idx` — [`L398`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L398)
  - <a id="_Stage3LoadMeta.src_engine_id"></a>`src_engine_id` — [`L397`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L397)
  - <a id="_Stage3LoadMeta.src_job_name"></a>`src_job_name` — [`L396`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L396)
  - <a id="_Stage3LoadMeta.src_parallelism"></a>`src_parallelism` — [`L399`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L399)
  - <a id="_Stage3LoadMeta.uuid"></a>`uuid` — [`L391`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L391)
- used by: [`_submit_stage3_loads`](tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads), [`_update_stage3_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler._update_stage3_state_after_alloc), [`_fail_load`](tpu_connector.md#TPURaidenConnectorScheduler._fail_load), [`_enqueue_stage3_release`](tpu_connector.md#TPURaidenConnectorScheduler._enqueue_stage3_release), [`_stage3_release_producer_registration`](tpu_connector.md#TPURaidenConnectorWorker._stage3_release_producer_registration), [`_stage3_source_work_units`](tpu_connector.md#TPURaidenConnectorWorker._stage3_source_work_units), [`_stage3_submitted_load_metas`](tpu_connector.md#TPURaidenConnectorWorker._stage3_submitted_load_metas)

### <a id="_Stage3PendingSubmit"></a>`_Stage3PendingSubmit`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:426`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L426)
- doc: One consumer load parked because the producer's request-block
- signature: `class _Stage3PendingSubmit:`
- members:
  - <a id="_Stage3PendingSubmit.defer_deadline"></a>`defer_deadline` — [`L447`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L447)
  - <a id="_Stage3PendingSubmit.destination_req_id"></a>`destination_req_id` — [`L440`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L440)
  - <a id="_Stage3PendingSubmit.dst_controller_address"></a>`dst_controller_address` — [`L444`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L444)
  - <a id="_Stage3PendingSubmit.dst_units"></a>`dst_units` — [`L445`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L445)
  - <a id="_Stage3PendingSubmit.first_attempt_s"></a>`first_attempt_s` — [`L448`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L448)
  - <a id="_Stage3PendingSubmit.last_attempt_s"></a>`last_attempt_s` — [`L451`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L451)
  - <a id="_Stage3PendingSubmit.local_blocks"></a>`local_blocks` — [`L443`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L443)
  - <a id="_Stage3PendingSubmit.num_tokens"></a>`num_tokens` — [`L442`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L442)
  - <a id="_Stage3PendingSubmit.req_meta"></a>`req_meta` — [`L438`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L438)
  - <a id="_Stage3PendingSubmit.source_req_id"></a>`source_req_id` — [`L439`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L439)
  - <a id="_Stage3PendingSubmit.task"></a>`task` — [`L454`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L454)
  - <a id="_Stage3PendingSubmit.uuid"></a>`uuid` — [`L441`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L441)
  - <a id="_Stage3PendingSubmit.wait_logged"></a>`wait_logged` — [`L449`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L449)
- used by: [`_submit_stage3_loads`](tpu_connector.md#TPURaidenConnectorWorker._submit_stage3_loads), [`_stage_stage3_submit_task`](tpu_connector.md#TPURaidenConnectorWorker._stage_stage3_submit_task), [`_apply_stage3_submit_outcome`](tpu_connector.md#TPURaidenConnectorWorker._apply_stage3_submit_outcome), [`_execute_stage3_submit`](tpu_connector.md#TPURaidenConnectorWorker._execute_stage3_submit), [`_drain_stage3_pending_submits`](tpu_connector.md#TPURaidenConnectorWorker._drain_stage3_pending_submits), [`_dispatch_stage3_load_submit`](tpu_connector.md#TPURaidenConnectorWorker._dispatch_stage3_load_submit), [`_stage3_pending_submits`](tpu_connector.md#TPURaidenConnectorWorker._stage3_pending_submits), [`pending`](tpu_connector.md#_Stage3SubmitTask.pending)

### <a id="_Stage3RegisteredSend"></a>`_Stage3RegisteredSend`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:489`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L489)
- doc: Worker-local D5 registration retained until terminal send state.
- signature: `class _Stage3RegisteredSend:`
- members:
  - <a id="_Stage3RegisteredSend.expiration_time"></a>`expiration_time` — [`L495`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L495)
  - <a id="_Stage3RegisteredSend.finish_pending"></a>`finish_pending` — [`L499`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L499)
  - <a id="_Stage3RegisteredSend.local_block_ids"></a>`local_block_ids` — [`L493`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L493)
  - <a id="_Stage3RegisteredSend.num_tokens"></a>`num_tokens` — [`L494`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L494)
  - <a id="_Stage3RegisteredSend.uuid"></a>`uuid` — [`L492`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L492)
- used by: [`_register_stage3_request_blocks`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_poll_finished`](tpu_connector.md#TPURaidenConnectorWorker._poll_finished), [`_register_stage3_request_row_spans`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans), [`get_finished`](tpu_connector.md#TPURaidenConnectorWorker.get_finished), [`_register_stage3_request_blocks_dsv4`](tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks_dsv4), [`_probe_stage3_registrations`](tpu_connector.md#TPURaidenConnectorWorker._probe_stage3_registrations), [`_stage3_registered_sends`](tpu_connector.md#TPURaidenConnectorWorker._stage3_registered_sends), [`_stage3_terminal_sends`](tpu_connector.md#TPURaidenConnectorWorker._stage3_terminal_sends)

### <a id="_Stage3SubmitOutcome"></a>`_Stage3SubmitOutcome`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:478`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L478)
- doc: Result of one coordination RPC, applied on the model-runner thread.
- signature: `class _Stage3SubmitOutcome:`
- members:
  - <a id="_Stage3SubmitOutcome.attempted_at"></a>`attempted_at` — [`L485`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L485)
  - <a id="_Stage3SubmitOutcome.error"></a>`error` — [`L482`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L482)
  - <a id="_Stage3SubmitOutcome.submit_ms"></a>`submit_ms` — [`L483`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L483)
  - <a id="_Stage3SubmitOutcome.task"></a>`task` — [`L481`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L481)
- uses (calls/refs, reference-scoped): [`_Stage3SubmitTask`](tpu_connector.md#_Stage3SubmitTask)
- used by: [`_apply_stage3_submit_outcome`](tpu_connector.md#TPURaidenConnectorWorker._apply_stage3_submit_outcome), [`_execute_stage3_submit`](tpu_connector.md#TPURaidenConnectorWorker._execute_stage3_submit), [`_stage3_submit_outcomes`](tpu_connector.md#TPURaidenConnectorWorker._stage3_submit_outcomes)

### <a id="_Stage3SubmitTask"></a>`_Stage3SubmitTask`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:458`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L458)
- doc: One staged source-controller coordination call.
- signature: `class _Stage3SubmitTask:`
- members:
  - <a id="_Stage3SubmitTask.call_kwargs"></a>`call_kwargs` — [`L471`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L471)
  - <a id="_Stage3SubmitTask.fa_skip_bytes"></a>`fa_skip_bytes` — [`L468`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L468)
  - <a id="_Stage3SubmitTask.facade"></a>`facade` — [`L470`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L470)
  - <a id="_Stage3SubmitTask.pending"></a>`pending` — [`L466`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L466)
  - <a id="_Stage3SubmitTask.retry_inline"></a>`retry_inline` — [`L474`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L474)
  - <a id="_Stage3SubmitTask.skip_tokens"></a>`skip_tokens` — [`L467`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L467)
  - <a id="_Stage3SubmitTask.source_units"></a>`source_units` — [`L469`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L469)
- uses (calls/refs, reference-scoped): [`_Stage3PendingSubmit`](tpu_connector.md#_Stage3PendingSubmit)
- used by: [`_stage_stage3_submit_task`](tpu_connector.md#TPURaidenConnectorWorker._stage_stage3_submit_task), [`_apply_stage3_submit_outcome`](tpu_connector.md#TPURaidenConnectorWorker._apply_stage3_submit_outcome), [`_execute_stage3_submit`](tpu_connector.md#TPURaidenConnectorWorker._execute_stage3_submit), [`task`](tpu_connector.md#_Stage3SubmitOutcome.task)

### <a id="_Stage3TransferGroup"></a>`_Stage3TransferGroup`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py:193`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L193)
- doc: One paged KV cache group Stage 3 moves, and the size of its pages.
- signature: `class _Stage3TransferGroup:`
- members:
  - <a id="_Stage3TransferGroup.cache_group_index"></a>`cache_group_index` — [`L201`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L201)
  - <a id="_Stage3TransferGroup.page_tokens"></a>`page_tokens` — [`L202`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L202)
  - <a id="_Stage3TransferGroup.window_tokens"></a>`window_tokens` — [`L203`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L203)
- used by: [`_stage3_publish_send`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_publish_send), [`_update_stage3_state_after_alloc`](tpu_connector.md#TPURaidenConnectorScheduler._update_stage3_state_after_alloc), [`_stage3_transfer_groups`](tpu_connector.md#TPUConnector._stage3_transfer_groups), [`request_finished_all_groups`](tpu_connector.md#TPUConnector.request_finished_all_groups), [`_measure_dsv4_pool_plan`](tpu_connector.md#TPURaidenConnectorWorker._measure_dsv4_pool_plan), [`_stage3_dsv4_group_blocks`](tpu_connector.md#TPURaidenConnectorWorker._stage3_dsv4_group_blocks), [`_stage3_transfer_groups`](tpu_connector.md#_stage3_transfer_groups), [`_stage3_transfer_groups`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_transfer_groups), [`_stage3_truncates_prompt`](tpu_connector.md#TPURaidenConnectorScheduler._stage3_truncates_prompt), [`_stage3_dsv4_transfer_groups`](tpu_connector.md#TPURaidenConnectorWorker._stage3_dsv4_transfer_groups)

## Functions
- <a id="_as_bool"></a>`_as_bool(value: Any, default: bool = False)` — [`L509`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L509)
- <a id="_as_int"></a>`_as_int(value: Any)` — [`L523`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L523)
- <a id="_as_int_list"></a>`_as_int_list(value: Any)` — [`L544`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L544)
- <a id="_as_str"></a>`_as_str(value: Any)` — [`L538`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L538)
- <a id="_engine_is_pipeline"></a>`_engine_is_pipeline(vllm_config: VllmConfig)` — [`L608`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L608) — A pipeline-parallel engine: each stage transfers its own layers, so
- <a id="_get_extra_config"></a>`_get_extra_config(vllm_config: VllmConfig)` — [`L502`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L502)
- <a id="_is_kimi"></a>`_is_kimi(vllm_config: VllmConfig)` — [`L715`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L715)
- <a id="_pipeline_parallel_size"></a>`_pipeline_parallel_size(vllm_config: VllmConfig)` — [`L601`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L601)
- <a id="_pipeline_stage_pcp_size"></a>`_pipeline_stage_pcp_size(vllm_config: VllmConfig)` — [`L614`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L614) — PCP ranks inside each pipeline stage: a PP x PCP stage splits its
- <a id="_prefix_aware_load_enabled"></a>`_prefix_aware_load_enabled()` — [`L755`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L755) — Whether suffix-only Stage-3 loads are requested and supported. — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="_prefix_aware_load_requested"></a>`_prefix_aware_load_requested()` — [`L731`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L731)
- <a id="_prefix_aware_load_supported"></a>`_prefix_aware_load_supported()` — [`L736`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L736) — Whether the installed reshard client can encode suffix clips.
- <a id="_raiden_dst_dcp_size"></a>`_raiden_dst_dcp_size(vllm_config: VllmConfig)` — [`L645`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L645) — Destination geometry needed before the producer publishes its spans.
- <a id="_raiden_dst_interleave_tokens"></a>`_raiden_dst_interleave_tokens(vllm_config: VllmConfig)` — [`L657`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L657)
- <a id="_raiden_dst_shards"></a>`_raiden_dst_shards()` — [`L637`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L637)
- <a id="_raiden_seq_on_lane_layout"></a>`_raiden_seq_on_lane_layout()` — [`L628`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L628) — Decision D1: the batched-RPA seq-along-lane FA pool (either kernel
- <a id="_reshard_advertise_host"></a>`_reshard_advertise_host(dp_rank: int)` — [`L666`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L666)
- <a id="_reshard_dispatch_address"></a>`_reshard_dispatch_address(dp_rank: int)` — [`L691`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L691)
- <a id="_reshard_service_address"></a>`_reshard_service_address(dp_rank: int)` — [`L687`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L687)
- <a id="_reshard_service_port"></a>`_reshard_service_port(dp_rank: int)` — [`L683`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L683)
- <a id="_reshard_store_mode"></a>`_reshard_store_mode()` — [`L622`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L622) — In-engine hosting: the reshard service lives in each engine's rank-0
- <a id="_resolved_reshard_controller_address"></a>`_resolved_reshard_controller_address(dp_rank: int)` — [`L696`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L696) — The address the facade dials and the handoff advertises: the
- <a id="_select_committed_mamba_blocks"></a>`_select_committed_mamba_blocks(block_tables: list[list[int]], num_speculative_blocks: int)` — [`L171`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L171) — Select each Mamba group's last committed state checkpoint.
- <a id="_stage3_group_window_tokens"></a>`_stage3_group_window_tokens(group_spec: Any)` — [`L290`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L290) — The sliding window of a cache group, or None if it is full attention.
- <a id="_stage3_recycled_transfer_pages"></a>`_stage3_recycled_transfer_pages(block_ids: Sequence[int], *, num_tokens: int, page_tokens: int, window_tokens: int | None)` — [`L267`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L267) — Counts the pages this send would carry that the allocator already freed.
- <a id="_stage3_skipped_window_pages"></a>`_stage3_skipped_window_pages(*, num_tokens: int, page_tokens: int, window_tokens: int | None)` — [`L211`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L211) — Leading pages of a sliding-window block table that hold no live KV.
- <a id="_stage3_transfer_groups"></a>`_stage3_transfer_groups(kv_cache_groups: Sequence[Any], *, multi_group: bool)` — [`L301`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L301) — The KV cache groups whose pages Stage 3 transfers, in group order.
- <a id="_stage3_trim_window_pages"></a>`_stage3_trim_window_pages(block_ids: Sequence[int], *, num_tokens: int, page_tokens: int, window_tokens: int | None, group_label: str)` — [`L224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L224) — `block_ids` without the dead prefix a sliding window leaves.
- <a id="_use_per_layer_pool_tags"></a>`_use_per_layer_pool_tags()` — [`L597`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L597)
- <a id="_use_raiden_connector"></a>`_use_raiden_connector(vllm_config: VllmConfig)` — [`L760`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L760)
- <a id="_use_raiden_dsv4_admission"></a>`_use_raiden_dsv4_admission()` — [`L709`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L709)
- <a id="_use_raiden_glm_admission"></a>`_use_raiden_glm_admission()` — [`L705`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L705)
- <a id="_use_raiden_stage3_transport"></a>`_use_raiden_stage3_transport()` — [`L593`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L593)
- <a id="_uses_tp_stage3_source"></a>`_uses_tp_stage3_source(vllm_config: VllmConfig)` — [`L722`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L722) — Whether the producer's TP ranks are transfer ranks.
- <a id="get_uuid"></a>`get_uuid()` — [`L7194`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L7194)
- <a id="stage3_fa_raiden_id_fields"></a>`stage3_fa_raiden_id_fields(*, job_name: str, engine_id: str, dp_rank: int, transfer_rank: int = 0, is_producer: bool = True, per_rank_unit: bool | None = None)` — [`L553`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L553) — Build the canonical Stage-3 FA work-unit identity.

## Module values
- <a id="_DONE_FUTURE"></a>`_DONE_FUTURE` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L139)
- <a id="_KV_PARAMS_ADMITTED"></a>`_KV_PARAMS_ADMITTED` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L164)
- <a id="_KV_PARAMS_REJECTED"></a>`_KV_PARAMS_REJECTED` — [`L165`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L165)
- <a id="_STAGE3_D5_REGISTRATION_WAIT_S"></a>`_STAGE3_D5_REGISTRATION_WAIT_S` — [`L141`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L141)
- <a id="_STAGE3_FINISH_DEDUP_LIMIT"></a>`_STAGE3_FINISH_DEDUP_LIMIT` — [`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L140)
- <a id="_STAGE3_GLM_TRANSFER_POOL_TAGS"></a>`_STAGE3_GLM_TRANSFER_POOL_TAGS` — [`L157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L157)
- <a id="_STAGE3_LEGACY_ROUTING_FIELDS"></a>`_STAGE3_LEGACY_ROUTING_FIELDS` — [`L166`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L166)
- <a id="_STAGE3_NULL_BLOCK_ID"></a>`_STAGE3_NULL_BLOCK_ID` — [`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L208)
- <a id="_STAGE3_REGISTRATION_CANCELLED_ERROR"></a>`_STAGE3_REGISTRATION_CANCELLED_ERROR` — [`L149`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L149)
- <a id="_STAGE3_REGISTRATION_REATTEMPT_MIN_INTERVAL_S"></a>`_STAGE3_REGISTRATION_REATTEMPT_MIN_INTERVAL_S` — [`L148`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L148)
- <a id="_STAGE3_REGISTRY_STATUS_CANCELLED"></a>`_STAGE3_REGISTRY_STATUS_CANCELLED` — [`L145`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L145)
- <a id="_STAGE3_REGISTRY_STATUS_UNKNOWN"></a>`_STAGE3_REGISTRY_STATUS_UNKNOWN` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L144)
- <a id="_STAGE3_STATE_CLASS_TAGS"></a>`_STAGE3_STATE_CLASS_TAGS` — [`L156`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L156)
- <a id="_STAGE3_SUBMIT_WORKERS"></a>`_STAGE3_SUBMIT_WORKERS` — [`L161`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L161)
- <a id="_STAGE3_UNREACHABLE_SOURCE_BACKOFF_S"></a>`_STAGE3_UNREACHABLE_SOURCE_BACKOFF_S` — [`L162`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L162)
- <a id="__all__"></a>`__all__` — [`L118`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L118)
- <a id="logger"></a>`logger` — [`L116`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.py#L116)

