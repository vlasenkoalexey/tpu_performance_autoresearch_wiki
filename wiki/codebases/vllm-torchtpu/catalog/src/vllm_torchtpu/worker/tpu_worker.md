---
title: 'Module: src/vllm_torchtpu/worker/tpu_worker.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/worker/tpu_worker.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.worker.tpu_worker`/
symbols:
  TPUWorker.init_device: TPUWorker#init_device().
  TPUWorker.profile: TPUWorker#profile().
  TPUWorker.determine_available_memory: TPUWorker#determine_available_memory().
  TPUWorker.model_runner: TPUWorker#model_runner.
  logger: logger.
  TPUWorker.execute_dummy_batch: TPUWorker#execute_dummy_batch().
  TPUWorker.load_model: TPUWorker#load_model().
  TPUWorker.get_node_kv_ip_port: TPUWorker#get_node_kv_ip_port().
  TPUWorker.profile_capture_dir: TPUWorker#profile_capture_dir.
  TPUWorker.profile_world_size: TPUWorker#profile_world_size.
  TPUWorker.__init__: TPUWorker#__init__().
  TPUWorker.compile_or_warm_up_model: TPUWorker#compile_or_warm_up_model().
  TPUWorker.reload_kernels: TPUWorker#reload_kernels().
  TPUWorker.profile_context: TPUWorker#profile_context.
  TPUWorker.kv_cache_dtype: TPUWorker#kv_cache_dtype.
  TPUWorker.profile_rank: TPUWorker#profile_rank.
  TPUWorker._pooling_kv_cache_cap_bytes: TPUWorker#_pooling_kv_cache_cap_bytes().
  TPUWorker._next_profile_session_key: TPUWorker#_next_profile_session_key().
  TPUWorker.devices: TPUWorker#devices.
  TPUWorker.execute_model: TPUWorker#execute_model().
  TPUWorker.sample_tokens: TPUWorker#sample_tokens().
  TPUWorker.pp_push: TPUWorker#pp_push().
  TPUWorker.pp_settle: TPUWorker#pp_settle().
  TPUWorker.pp_drains_before_handoff: TPUWorker#pp_drains_before_handoff().
  TPUWorker.profile_pipeline_chunks: TPUWorker#profile_pipeline_chunks().
  TPUWorker.take_draft_token_ids: TPUWorker#take_draft_token_ids().
  TPUWorker.get_kv_cache_spec: TPUWorker#get_kv_cache_spec().
  TPUWorker.get_kv_prewarm_shapes: TPUWorker#get_kv_prewarm_shapes().
  TPUWorker.prewarm_kv_offload_shape: TPUWorker#prewarm_kv_offload_shape().
  TPUWorker.initialize_from_config: TPUWorker#initialize_from_config().
  _release_free_host_heap: _release_free_host_heap().
  TPUWorker.profile_dir: TPUWorker#profile_dir.
  TPUWorker.profile_canonical_ts: TPUWorker#profile_canonical_ts.
  TPUWorker.profile_session_key: TPUWorker#profile_session_key.
  TPUWorker.profile_run_dir: TPUWorker#profile_run_dir.
  TPUWorker.device_ranks: TPUWorker#device_ranks.
  TPUWorker.get_model: TPUWorker#get_model().
  TPUWorker.get_supported_tasks: TPUWorker#get_supported_tasks().
  TPUWorker.add_lora: TPUWorker#add_lora().
  TPUWorker.remove_lora: TPUWorker#remove_lora().
  TPUWorker.pin_lora: TPUWorker#pin_lora().
  TPUWorker.list_loras: TPUWorker#list_loras().
  TPUWorker.sync_weights: TPUWorker#sync_weights().
  TPUWorker.get_kv_connector_handshake_metadata: TPUWorker#get_kv_connector_handshake_metadata().
  TPUWorker.profile_session_index: TPUWorker#profile_session_index.
  _get_kv_connector_handshake_metadata_key: _get_kv_connector_handshake_metadata_key().
  _configure_tpu_process_env: _configure_tpu_process_env().
  TPUWorker: TPUWorker#
  TPUWorker.set_kv_cache_layout: TPUWorker#set_kv_cache_layout().
  TPUWorker.initialize_cache: TPUWorker#initialize_cache().
  TPUWorker.get_num_gpu_blocks_override: TPUWorker#get_num_gpu_blocks_override().
---
# Module: [`src/vllm_torchtpu/worker/tpu_worker.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py)

## Classes
### <a id="TPUWorker"></a>`TPUWorker`
- def: [`src/vllm_torchtpu/worker/tpu_worker.py:95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L95)
- signature: `class TPUWorker(WorkerBase):`
- members:
  - <a id="TPUWorker._next_profile_session_key"></a>`_next_profile_session_key(self)` — [`L772`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L772) — Marker key for the start/stop cycle that is beginning.
  - <a id="TPUWorker._pooling_kv_cache_cap_bytes"></a>`_pooling_kv_cache_cap_bytes(self)` — [`L593`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L593) — Deterministic KV budget for pure pooling models, or None.
  - <a id="TPUWorker.add_lora"></a>`add_lora(self, lora_request: LoRARequest)` — [`L847`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L847)
  - <a id="TPUWorker.compile_or_warm_up_model"></a>`compile_or_warm_up_model(self)` — [`L793`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L793)
  - <a id="TPUWorker.determine_available_memory"></a>`determine_available_memory(self)` — [`L503`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L503) — documented in [kv-cache-layout-and-hbm-budget](../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="TPUWorker.execute_dummy_batch"></a>`execute_dummy_batch(self)` — [`L648`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L648) — Run an idle DP step with the same collective pattern as active DP.
  - <a id="TPUWorker.execute_model"></a>`execute_model(self, scheduler_output)` — [`L624`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L624)
  - <a id="TPUWorker.get_kv_cache_spec"></a>`get_kv_cache_spec(self)` — [`L844`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L844)
  - <a id="TPUWorker.get_kv_connector_handshake_metadata"></a>`get_kv_connector_handshake_metadata(self)` — [`L897`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L897)
  - <a id="TPUWorker.get_kv_prewarm_shapes"></a>`get_kv_prewarm_shapes(self)` — [`L862`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L862)
  - <a id="TPUWorker.get_model"></a>`get_model(self)` — [`L838`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L838)
  - <a id="TPUWorker.get_node_kv_ip_port"></a>`get_node_kv_ip_port(self)` — [`L873`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L873)
  - <a id="TPUWorker.get_num_gpu_blocks_override"></a>`get_num_gpu_blocks_override(self)` — [`L859`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L859)
  - <a id="TPUWorker.get_supported_tasks"></a>`get_supported_tasks(self)` — [`L841`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L841)
  - <a id="TPUWorker.init_device"></a>`init_device(self)` — [`L194`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L194) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TPUWorker.initialize_cache"></a>`initialize_cache(self, num_gpu_blocks: int, num_cpu_blocks: int)` — [`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L190)
  - <a id="TPUWorker.initialize_from_config"></a>`initialize_from_config(self, kv_cache_config: KVCacheConfig)` — [`L868`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L868)
  - <a id="TPUWorker.list_loras"></a>`list_loras(self)` — [`L856`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L856)
  - <a id="TPUWorker.load_model"></a>`load_model(self, *, load_dummy_weights: bool = False)` — [`L783`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L783)
  - <a id="TPUWorker.pin_lora"></a>`pin_lora(self, lora_id: int)` — [`L853`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L853)
  - <a id="TPUWorker.pp_drains_before_handoff"></a>`pp_drains_before_handoff(self)` — [`L636`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L636) — Whether this worker's stage drains the slice before each hand-off
  - <a id="TPUWorker.pp_push"></a>`pp_push(self)` — [`L630`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L630)
  - <a id="TPUWorker.pp_settle"></a>`pp_settle(self)` — [`L633`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L633)
  - <a id="TPUWorker.prewarm_kv_offload_shape"></a>`prewarm_kv_offload_shape(self, p: int)` — [`L865`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L865)
  - <a id="TPUWorker.profile"></a>`profile(self, is_start: bool = True, profile_prefix: str | None = None, profiler_kwargs: dict[str, Any] | None = None)` — [`L667`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L667) — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="TPUWorker.profile_pipeline_chunks"></a>`profile_pipeline_chunks(self)` — [`L642`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L642)
  - <a id="TPUWorker.reload_kernels"></a>`reload_kernels(self, modules: list[str] | None = None)` — [`L814`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L814) — Kernel-iteration hot-reload: re-import the reloadable kernel — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TPUWorker.remove_lora"></a>`remove_lora(self, lora_id: int)` — [`L850`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L850)
  - <a id="TPUWorker.sample_tokens"></a>`sample_tokens(self, grammar_output)` — [`L627`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L627)
  - <a id="TPUWorker.set_kv_cache_layout"></a>`set_kv_cache_layout(self, kv_cache_layout: str)` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L178)
  - <a id="TPUWorker.sync_weights"></a>`sync_weights(self, updated_weights, mappings: dict[str, tuple[str, tuple[str]]], transpose_keys: dict[str, tuple[int]], reshard_fn=None)` — [`L883`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L883)
  - <a id="TPUWorker.take_draft_token_ids"></a>`take_draft_token_ids(self)` — [`L645`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L645)
  - <a id="TPUWorker.device_ranks"></a>`device_ranks` — [`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L141)
  - <a id="TPUWorker.devices"></a>`devices` — [`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L140)
  - <a id="TPUWorker.kv_cache_dtype"></a>`kv_cache_dtype` — [`L145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L145)
  - <a id="TPUWorker.model_runner"></a>`model_runner` — [`L481`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L481) — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="TPUWorker.profile_canonical_ts"></a>`profile_canonical_ts` — [`L163`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L163)
  - <a id="TPUWorker.profile_capture_dir"></a>`profile_capture_dir` — [`L162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L162)
  - <a id="TPUWorker.profile_context"></a>`profile_context` — [`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L160)
  - <a id="TPUWorker.profile_dir"></a>`profile_dir` — [`L159`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L159)
  - <a id="TPUWorker.profile_rank"></a>`profile_rank` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L169)
  - <a id="TPUWorker.profile_run_dir"></a>`profile_run_dir` — [`L161`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L161)
  - <a id="TPUWorker.profile_session_index"></a>`profile_session_index` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L165)
  - <a id="TPUWorker.profile_session_key"></a>`profile_session_key` — [`L164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L164)
  - <a id="TPUWorker.profile_world_size"></a>`profile_world_size` — [`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L170)
- protocol/private: <a id="TPUWorker.__init__"></a>`__init__`[`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L96)
- uses (calls/refs, reference-scoped): [`execute_model`](../runner/tpu_runner.md#TPUModelRunner.execute_model), [`sample_tokens`](../runner/tpu_runner.md#TPUModelRunner.sample_tokens), [`_dummy_run`](../runner/tpu_runner.md#TPUModelRunner._dummy_run), [`capture_model`](../runner/tpu_runner.md#TPUModelRunner.capture_model), [`num_tokens_paddings`](../runner/tpu_runner.md#TPUModelRunner.num_tokens_paddings), [`get_tpu_worker_binding`](tpu_rank_binding.md#get_tpu_worker_binding), [`num_reqs_max_model_len`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_max_model_len), [`apply`](../patch_registry.md#apply), [`max_num_tokens`](../runner/tpu_runner.md#TPUModelRunner.max_num_tokens), [`_pp_wave`](../runner/tpu_runner.md#TPUModelRunner._pp_wave), [`profile_run`](../runner/tpu_runner.md#TPUModelRunner.profile_run), [`start_phased_profiling`](../runner/tpu_runner.md#TPUModelRunner.start_phased_profiling), [`_run_dp_idle_pairing`](../runner/tpu_runner.md#TPUModelRunner._run_dp_idle_pairing), [`TpuPlatform`](../platforms/tpu_platform.md#TpuPlatform), [`profile_pipeline_chunks`](../runner/tpu_runner.md#TPUModelRunner.profile_pipeline_chunks), [`TPUModelRunner`](../runner/tpu_runner.md#TPUModelRunner), [`logger`](tpu_worker.md#logger), [`max_num_blocks_per_req`](../runner/tpu_runner.md#TPUModelRunner.max_num_blocks_per_req), [`post_profile_hbm_reserves`](../runner/tpu_runner.md#TPUModelRunner.post_profile_hbm_reserves), [`resolve_profile_dir_and_opts`](../tracing/options.md#resolve_profile_dir_and_opts), [`resolve_canonical_dst_ts`](../profiler_trace.md#resolve_canonical_dst_ts), [`_dp_coordinated_step`](../runner/tpu_runner.md#TPUModelRunner._dp_coordinated_step), [`ensure_runai_aux_files`](runai_repull.md#ensure_runai_aux_files), [`compute_hbm_budget`](../utils.md#compute_hbm_budget), [`as_env`](tpu_rank_binding.md#TpuWorkerBinding.as_env), [`GBYTES`](../utils.md#GBYTES), [`take_draft_token_ids`](../runner/tpu_runner.md#TPUModelRunner.take_draft_token_ids), [`widen_message_rings`](../distributed/pp_push.md#widen_message_rings), [`reload_kernels`](../compilation/kernel_reload.md#reload_kernels), [`get_kv_cache_spec`](../runner/tpu_runner.md#TPUModelRunner.get_kv_cache_spec), [`TPU_KERNEL_ITER_MODE`](../envs.md#TPU_KERNEL_ITER_MODE), [`TPU_STR_DTYPE_TO_TORCH_DTYPE`](../layers/adapter/attention.md#TPU_STR_DTYPE_TO_TORCH_DTYPE), [`local_rank`](tpu_rank_binding.md#TpuWorkerBinding.local_rank), [`world_size`](tpu_rank_binding.md#TpuWorkerBinding.world_size), [`get_dp_size`](../utils.md#get_dp_size), [`stop_phased_profiling`](../runner/tpu_runner.md#TPUModelRunner.stop_phased_profiling), [`clear_canonical_ts_marker`](../profiler_trace.md#clear_canonical_ts_marker), [`init_local_rank`](tpu_rank_binding.md#TpuWorkerBinding.init_local_rank), [`rank`](tpu_rank_binding.md#TpuWorkerBinding.rank), [`local_world_size`](tpu_rank_binding.md#TpuWorkerBinding.local_world_size)  (+36 more)

## Functions
- <a id="_configure_tpu_process_env"></a>`_configure_tpu_process_env(rank: int, local_rank: int, world_size: int, local_world_size: int)` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L72)
- <a id="_get_kv_connector_handshake_metadata_key"></a>`_get_kv_connector_handshake_metadata_key(metadata=None)` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L62)
- <a id="_release_free_host_heap"></a>`_release_free_host_heap()` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L84) — Return free allocator pages from model loading and compilation to the OS.

## Module values
- <a id="logger"></a>`logger` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/worker/tpu_worker.py#L59)

