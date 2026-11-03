---
title: 'Module: src/vllm_torchtpu/platforms/tpu_platform.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/platforms/tpu_platform.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.platforms.tpu_platform`/
symbols:
  TpuPlatform.check_and_update_config: TpuPlatform#check_and_update_config().
  logger: logger.
  get_tpu_multihost_topology: get_tpu_multihost_topology().
  TpuPlatform: TpuPlatform#
  TpuPlatform.update_block_size_for_backend: TpuPlatform#update_block_size_for_backend().
  _configure_pipeline_chunks: _configure_pipeline_chunks().
  _get_linear_token_paddings: _get_linear_token_paddings().
  _validate_peer_replay_config: _validate_peer_replay_config().
  _configure_sequence_parallel_moe: _configure_sequence_parallel_moe().
  _unwrap_dynamic_compile_fns: _unwrap_dynamic_compile_fns().
  _patch_api_server_kernel_reload_endpoint: _patch_api_server_kernel_reload_endpoint().
  TpuPlatform._prepare_singlehost_tpu_env: TpuPlatform#_prepare_singlehost_tpu_env().
  TpuPlatform._find_non_ssm_backend: TpuPlatform#_find_non_ssm_backend().
  _get_token_paddings: _get_token_paddings().
  TpuPlatform.get_worker_distributed_backend: TpuPlatform#get_worker_distributed_backend().
  _configure_torchtpu_eager_mode: _configure_torchtpu_eager_mode().
  TpuPlatform.device_id_to_physical_device_id: TpuPlatform#device_id_to_physical_device_id().
  TpuPlatform.get_attn_backend_cls: TpuPlatform#get_attn_backend_cls().
  TpuPlatform.fp8_dtype: TpuPlatform#fp8_dtype().
  TpuPlatform.device_count: TpuPlatform#device_count().
  _validate_phased_profiling_config: _validate_phased_profiling_config().
  _register_tpu_kv_connectors: _register_tpu_kv_connectors().
  _dynamic_compile_unwrapped: _dynamic_compile_unwrapped.
  _tpu_kv_connectors_registered: _tpu_kv_connectors_registered.
  TpuPlatform.get_default_ir_op_priority: TpuPlatform#get_default_ir_op_priority().
  TpuPlatform.is_pin_memory_available: TpuPlatform#is_pin_memory_available().
  TpuPlatform.get_device_communicator_cls: TpuPlatform#get_device_communicator_cls().
  TpuPlatform.dist_backend: TpuPlatform#dist_backend.
  TpuPlatform.device_control_env_var: TpuPlatform#device_control_env_var.
  TpuPlatform._get_tpu_topology: TpuPlatform#_get_tpu_topology().
  TpuPlatform.get_device_name: TpuPlatform#get_device_name().
  _TpuAttentionBackend.get_page_size: _TpuAttentionBackend#get_page_size().
  _TpuAttentionBackend.get_min_page_size: _TpuAttentionBackend#get_min_page_size().
  _TpuAttentionBackend.get_preferred_block_size: _TpuAttentionBackend#get_preferred_block_size().
  TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP: TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP.
  TPU_3D_TORUS_MULTIHOST_TOPOLOGY_MAP: TPU_3D_TORUS_MULTIHOST_TOPOLOGY_MAP.
  TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP: TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP.
  TPU_8I_MULTIHOST_TOPOLOGY_MAP: TPU_8I_MULTIHOST_TOPOLOGY_MAP.
  _TPU_2D_TORUS_GENERATIONS: _TPU_2D_TORUS_GENERATIONS.
  _TPU_DUAL_DEVICE_GENERATIONS: _TPU_DUAL_DEVICE_GENERATIONS.
  _TPU_8I_GENERATIONS: _TPU_8I_GENERATIONS.
  _patch_api_server_kernel_reload_endpoint.build_app_with_reload: _patch_api_server_kernel_reload_endpoint().build_app_with_reload().
  _validate_lora_config: _validate_lora_config().
  _get_exponential_token_paddings: _get_exponential_token_paddings().
  _LINEAR_BUCKETS_FROM_BUDGET_FRACTION: _LINEAR_BUCKETS_FROM_BUDGET_FRACTION.
  _LINEAR_BUCKET_STEPS_PER_BUDGET: _LINEAR_BUCKET_STEPS_PER_BUDGET.
  _MAX_LINEAR_BUCKETS: _MAX_LINEAR_BUCKETS.
  _is_sequence_parallel_bucket: _is_sequence_parallel_bucket().
  _validate_token_budget_fits_compile_sizes: _validate_token_budget_fits_compile_sizes().
  _DYNAMIC_COMPILE_TARGETS._DYNAMIC_COMPILE_TARGETS: _DYNAMIC_COMPILE_TARGETS._DYNAMIC_COMPILE_TARGETS.
  _TpuAttentionBackend: _TpuAttentionBackend#
  _patch_api_server_kernel_reload_endpoint.build_app_with_reload.reload_kernel: _patch_api_server_kernel_reload_endpoint().build_app_with_reload().reload_kernel().
  TpuPlatform._enum: TpuPlatform#_enum.
  TpuPlatform.device_name: TpuPlatform#device_name.
  TpuPlatform.device_type: TpuPlatform#device_type.
  TpuPlatform.dispatch_key: TpuPlatform#dispatch_key.
  TpuPlatform.ray_device_key: TpuPlatform#ray_device_key.
  TpuPlatform.simple_compile_backend: TpuPlatform#simple_compile_backend.
  TpuPlatform._is_hybrid: TpuPlatform#_is_hybrid.
  TpuPlatform.supported_quantization: TpuPlatform#supported_quantization.
  TpuPlatform.additional_env_vars: TpuPlatform#additional_env_vars.
  TpuPlatform.import_kernels: TpuPlatform#import_kernels().
  TpuPlatform.import_ir_kernels: TpuPlatform#import_ir_kernels().
  TpuPlatform.is_available: TpuPlatform#is_available().
  TpuPlatform.current_device: TpuPlatform#current_device().
  TpuPlatform.current_device_index: TpuPlatform#current_device_index().
  TpuPlatform.set_device: TpuPlatform#set_device().
  TpuPlatform.set_device_index: TpuPlatform#set_device_index().
  TpuPlatform.synchronize: TpuPlatform#synchronize().
  TpuPlatform.current_stream: TpuPlatform#current_stream().
  TpuPlatform.set_stream: TpuPlatform#set_stream().
  TpuPlatform.get_device_total_memory: TpuPlatform#get_device_total_memory().
  TpuPlatform.get_current_memory_usage: TpuPlatform#get_current_memory_usage().
  TpuPlatform.is_async_output_supported: TpuPlatform#is_async_output_supported().
  TpuPlatform.get_punica_wrapper: TpuPlatform#get_punica_wrapper().
  TpuPlatform.get_infinity_values: TpuPlatform#get_infinity_values().
  TpuPlatform.can_update_inplace: TpuPlatform#can_update_inplace().
  TpuPlatform.inference_mode: TpuPlatform#inference_mode().
  TpuPlatform.get_compile_backend: TpuPlatform#get_compile_backend().
  TpuPlatform.set_additional_forward_context: TpuPlatform#set_additional_forward_context().
  TpuPlatform.use_all_gather: TpuPlatform#use_all_gather().
  TpuPlatform.supports_v1: TpuPlatform#supports_v1().
  TpuPlatform.validate_request: TpuPlatform#validate_request().
  TpuPlatform.is_kv_cache_dtype_supported: TpuPlatform#is_kv_cache_dtype_supported().
  TpuPlatform.use_sync_weight_loader: TpuPlatform#use_sync_weight_loader().
  TpuPlatform.support_hybrid_kv_cache: TpuPlatform#support_hybrid_kv_cache().
---
# Module: [`src/vllm_torchtpu/platforms/tpu_platform.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py)

## Classes
### <a id="TpuPlatform"></a>`TpuPlatform`
- def: [`src/vllm_torchtpu/platforms/tpu_platform.py:453`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L453) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- members:
  - <a id="TpuPlatform._find_non_ssm_backend"></a>`_find_non_ssm_backend(cls, vllm_config: VllmConfig)` — [`L1249`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1249) — First non-SSM attention backend in layer order, or None. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TpuPlatform._get_tpu_topology"></a>`_get_tpu_topology(cls, world_size: int)` — [`L664`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L664) — Return the torch_tpu-reported topology for the requested world size.
  - <a id="TpuPlatform._prepare_singlehost_tpu_env"></a>`_prepare_singlehost_tpu_env(cls, world_size: int)` — [`L624`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L624) — Set TORCH_TPU_* env vars needed by PjRt initialization. — documented in [omni-diffusion-support](../../../../concepts/omni-diffusion-support.md)
  - <a id="TpuPlatform.can_update_inplace"></a>`can_update_inplace(cls)` — [`L754`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L754)
  - <a id="TpuPlatform.check_and_update_config"></a>`check_and_update_config(cls, vllm_config: VllmConfig)` — [`L785`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L785) — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
  - <a id="TpuPlatform.current_device"></a>`current_device(cls)` — [`L584`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L584)
  - <a id="TpuPlatform.current_device_index"></a>`current_device_index(cls)` — [`L588`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L588)
  - <a id="TpuPlatform.current_stream"></a>`current_stream(cls, device: torch.device | None = None)` — [`L604`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L604)
  - <a id="TpuPlatform.device_count"></a>`device_count(cls)` — [`L559`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L559) — Local physical chip count on this host, stable across contexts.
  - <a id="TpuPlatform.device_id_to_physical_device_id"></a>`device_id_to_physical_device_id(cls, device_id: int)` — [`L544`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L544) — Map logical DP/TP device id to a local physical TPU device.
  - <a id="TpuPlatform.fp8_dtype"></a>`fp8_dtype(cls)` — [`L722`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L722)
  - <a id="TpuPlatform.get_attn_backend_cls"></a>`get_attn_backend_cls(cls, selected_backend: AttentionBackendEnum, attn_selector_config: AttentionSelectorConfig, num_heads: int | None = None, **kwargs)` — [`L672`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L672)
  - <a id="TpuPlatform.get_compile_backend"></a>`get_compile_backend(cls)` — [`L762`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L762)
  - <a id="TpuPlatform.get_current_memory_usage"></a>`get_current_memory_usage(cls, device: torch.types.Device | None = None)` — [`L733`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L733)
  - <a id="TpuPlatform.get_default_ir_op_priority"></a>`get_default_ir_op_priority(cls, vllm_config: VllmConfig)` — [`L525`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L525) — Prefer the CUDA-numerics ``tpu`` RMSNorm providers over ``native``.
  - <a id="TpuPlatform.get_device_communicator_cls"></a>`get_device_communicator_cls(cls)` — [`L1325`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1325)
  - <a id="TpuPlatform.get_device_name"></a>`get_device_name(cls, device_id: int = 0)` — [`L718`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L718) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TpuPlatform.get_device_total_memory"></a>`get_device_total_memory(cls, device_id: int = 0)` — [`L729`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L729)
  - <a id="TpuPlatform.get_infinity_values"></a>`get_infinity_values(cls, dtype)` — [`L750`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L750)
  - <a id="TpuPlatform.get_punica_wrapper"></a>`get_punica_wrapper(cls)` — [`L746`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L746)
  - <a id="TpuPlatform.get_worker_distributed_backend"></a>`get_worker_distributed_backend(cls, world_size: int)` — [`L612`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L612) — Pick torch.distributed backend used by worker bootstrap. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TpuPlatform.import_ir_kernels"></a>`import_ir_kernels(cls)` — [`L515`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L515) — Register the TPU providers for vLLM IR ops on top of the built-ins.
  - <a id="TpuPlatform.import_kernels"></a>`import_kernels(cls)` — [`L511`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L511)
  - <a id="TpuPlatform.inference_mode"></a>`inference_mode(cls)` — [`L758`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L758)
  - <a id="TpuPlatform.is_async_output_supported"></a>`is_async_output_supported(cls, enforce_eager: bool | None)` — [`L742`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L742)
  - <a id="TpuPlatform.is_available"></a>`is_available(cls)` — [`L580`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L580)
  - <a id="TpuPlatform.is_kv_cache_dtype_supported"></a>`is_kv_cache_dtype_supported(cls, kv_cache_dtype: str, _model_config: ModelConfig)` — [`L1360`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1360)
  - <a id="TpuPlatform.is_pin_memory_available"></a>`is_pin_memory_available(cls)` — [`L1320`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1320)
  - <a id="TpuPlatform.set_additional_forward_context"></a>`set_additional_forward_context(cls, *args, **kwargs)` — [`L766`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L766) — Move DP metadata onto the TPU for DP+EP.
  - <a id="TpuPlatform.set_device"></a>`set_device(cls, device: torch.device | int)` — [`L592`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L592)
  - <a id="TpuPlatform.set_device_index"></a>`set_device_index(cls, device: torch.device | int)` — [`L596`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L596)
  - <a id="TpuPlatform.set_stream"></a>`set_stream(cls, stream: torch.Stream)` — [`L608`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L608)
  - <a id="TpuPlatform.support_hybrid_kv_cache"></a>`support_hybrid_kv_cache(cls)` — [`L1375`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1375)
  - <a id="TpuPlatform.supports_v1"></a>`supports_v1(cls, model_config: ModelConfig)` — [`L1337`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1337)
  - <a id="TpuPlatform.synchronize"></a>`synchronize(cls, device: torch.device | int | None = None)` — [`L600`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L600)
  - <a id="TpuPlatform.update_block_size_for_backend"></a>`update_block_size_for_backend(cls, vllm_config: VllmConfig)` — [`L1261`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1261) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TpuPlatform.use_all_gather"></a>`use_all_gather(cls)` — [`L1333`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1333)
  - <a id="TpuPlatform.use_sync_weight_loader"></a>`use_sync_weight_loader(cls)` — [`L1367`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1367) — Returns if the current platform needs to sync weight loader.
  - <a id="TpuPlatform.validate_request"></a>`validate_request(cls, processed_inputs: EngineInput, params: Union[SamplingParams, PoolingParams])` — [`L1342`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1342) — Raises if this request is unsupported on this platform
  - <a id="TpuPlatform.additional_env_vars"></a>`additional_env_vars` — [`L475`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L475)
  - <a id="TpuPlatform.device_control_env_var"></a>`device_control_env_var` — [`L461`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L461)
  - <a id="TpuPlatform.device_name"></a>`device_name` — [`L456`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L456)
  - <a id="TpuPlatform.device_type"></a>`device_type` — [`L457`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L457)
  - <a id="TpuPlatform.dispatch_key"></a>`dispatch_key` — [`L458`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L458)
  - <a id="TpuPlatform.dist_backend"></a>`dist_backend` — [`L460`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L460) — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="TpuPlatform.ray_device_key"></a>`ray_device_key` — [`L459`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L459)
  - <a id="TpuPlatform.simple_compile_backend"></a>`simple_compile_backend` — [`L462`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L462)
  - <a id="TpuPlatform.supported_quantization"></a>`supported_quantization` — [`L465`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L465)
- protocol/private: <a id="TpuPlatform._enum"></a>`_enum`[`L455`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L455), <a id="TpuPlatform._is_hybrid"></a>`_is_hybrid`[`L463`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L463)
- uses (calls/refs, reference-scoped): [`apply`](../patch_registry.md#apply), [`logger`](tpu_platform.md#logger), [`validate_platform_config`](pcp_validation.md#PcpStaticSupportValidator.validate_platform_config), [`PallasAttentionBackend`](../layers/adapter/attention.md#PallasAttentionBackend), [`PallasMLAttentionBackend`](../layers/adapter/attention.md#PallasMLAttentionBackend), [`validate_pipeline_parallel_config`](pp_validation.md#validate_pipeline_parallel_config), [`prepare_mp_multihost_dp_env`](../distributed/tpu_mp_multihost.md#prepare_mp_multihost_dp_env), [`prepare_mp_multihost_env`](../distributed/tpu_mp_multihost.md#prepare_mp_multihost_env), [`_configure_pipeline_chunks`](tpu_platform.md#_configure_pipeline_chunks), [`unified_kv_layout_enabled`](tpu_block_size_utils.md#unified_kv_layout_enabled), [`patch_engine_core_for_lazy_push`](../core/pp_lazy_step.md#patch_engine_core_for_lazy_push), [`patch_executor_for_pp_handoff`](../distributed/pp_push.md#patch_executor_for_pp_handoff), [`_get_linear_token_paddings`](tpu_platform.md#_get_linear_token_paddings), [`TPU_KERNEL_ITER_MODE`](../envs.md#TPU_KERNEL_ITER_MODE), [`update_tpu_block_size_and_slot_config`](tpu_block_size_utils.md#update_tpu_block_size_and_slot_config), [`_configure_sequence_parallel_moe`](tpu_platform.md#_configure_sequence_parallel_moe), [`_validate_peer_replay_config`](tpu_platform.md#_validate_peer_replay_config), [`supported_kv_cache_layouts`](../layers/adapter/attention.md#PallasAttentionBackend.supported_kv_cache_layouts), [`enabled`](pcp_validation.md#PcpStaticConfig.enabled), [`get_num_chips`](../tpu_info.md#get_num_chips), [`is_registered_attention_backend`](../layers/adapter/attention_backend.md#is_registered_attention_backend), [`PcpStaticSupportValidator`](pcp_validation.md#PcpStaticSupportValidator), [`TPU_MULTIHOST_BACKEND`](../envs.md#TPU_MULTIHOST_BACKEND), [`check_attention_backend_config`](../layers/adapter/attention_backend.md#check_attention_backend_config), [`_get_token_paddings`](tpu_platform.md#_get_token_paddings), [`TPU_IR_PROVIDER`](../layers/adapter/ir_ops.md#TPU_IR_PROVIDER), [`TPU_MOE_SEQUENCE_PARALLEL`](../envs.md#TPU_MOE_SEQUENCE_PARALLEL), [`pcp_size`](pcp_validation.md#PcpStaticConfig.pcp_size), [`PallasBatchedRPAAttentionBackend`](../layers/adapter/attention.md#PallasBatchedRPAAttentionBackend), [`TpuDeviceCommunicator`](../distributed/tpu_communicator.md#TpuDeviceCommunicator), [`TpuMultiprocExecutor`](../executors/tpu_multiproc_executor.md#TpuMultiprocExecutor), [`_register_tpu_kv_connectors`](tpu_platform.md#_register_tpu_kv_connectors), [`_validate_phased_profiling_config`](tpu_platform.md#_validate_phased_profiling_config), [`OmniTpuPlatform`](../omni/platform.md#OmniTpuPlatform), [`RayDistributedExecutor`](../executors/ray_distributed_executor.md#RayDistributedExecutor), [`RayDistributedExecutorV2`](../executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2), [`DP_SCHED_ENABLED`](../envs.md#DP_SCHED_ENABLED), [`get_page_size`](../layers/adapter/attention.md#PallasMLAttentionBackend.get_page_size), [`TPU_TOKEN_BUCKET_EXTRA`](../envs.md#TPU_TOKEN_BUCKET_EXTRA), [`TPU_TOKEN_BUCKET_LINEAR`](../envs.md#TPU_TOKEN_BUCKET_LINEAR)  (+5 more)
- used by: [`initialize_kv_cache`](../runner/kv_cache_manager.md#KVCacheManager.initialize_kv_cache), [`init_device`](../worker/tpu_worker.md#TPUWorker.init_device), [`get_kv_cache_spec`](../runner/kv_cache_manager.md#KVCacheManager.get_kv_cache_spec), [`get_tpu_multihost_topology`](tpu_platform.md#get_tpu_multihost_topology), [`_update_mamba_page_size_padded`](../runner/kv_cache_manager.md#KVCacheManager._update_mamba_page_size_padded), [`_update_attention_page_size_padded`](../runner/kv_cache_manager.md#KVCacheManager._update_attention_page_size_padded), [`set_device`](../omni/platform.md#OmniTpuPlatform.set_device), [`resolve_attention_geometry`](../offload/raiden_store.md#resolve_attention_geometry), [`_worker_env`](../experimental/export/cli.md#_worker_env), [`dist_backend`](../omni/platform.md#OmniTpuPlatform.dist_backend), [`init_export_distributed_environment`](../experimental/export/universal_adapter.md#init_export_distributed_environment), [`register_tpu_platform`](__init__.md#register_tpu_platform), [`OmniTpuPlatform`](../omni/platform.md#OmniTpuPlatform), [`get_device_count`](../omni/platform.md#OmniTpuPlatform.get_device_count)

### <a id="_TpuAttentionBackend"></a>`_TpuAttentionBackend`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/platforms/tpu_platform.py:52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L52)
- doc: Typing-only view of the TPU classmethods on our attention backends.
- signature: `class _TpuAttentionBackend(Protocol):`
- members:
  - <a id="_TpuAttentionBackend.get_min_page_size"></a>`get_min_page_size(vllm_config: VllmConfig)` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L59)
  - <a id="_TpuAttentionBackend.get_page_size"></a>`get_page_size(vllm_config: VllmConfig)` — [`L56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L56)
  - <a id="_TpuAttentionBackend.get_preferred_block_size"></a>`get_preferred_block_size(cls, default_block_size: int)` — [`L62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L62)
- used by: [`update_block_size_for_backend`](tpu_platform.md#TpuPlatform.update_block_size_for_backend)

## Functions
- <a id="_configure_pipeline_chunks"></a>`_configure_pipeline_chunks(vllm_config: VllmConfig)` — [`L1441`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1441) — Install the time-budget scheduler for a pipeline and the engine-core — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_configure_sequence_parallel_moe"></a>`_configure_sequence_parallel_moe(vllm_config: VllmConfig)` — [`L1505`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1505) — Validate architecture and filter compile buckets for sequence-parallel MoE. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_configure_torchtpu_eager_mode"></a>`_configure_torchtpu_eager_mode()` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L218)
- <a id="_get_exponential_token_paddings"></a>`_get_exponential_token_paddings(min_token_size: int, max_token_size: int)` — [`L1379`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1379) — Sizes doubling from min_token_size, capped exactly at max_token_size.
- <a id="_get_linear_token_paddings"></a>`_get_linear_token_paddings(max_token_size: int, longest_pass: int)` — [`L1413`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1413) — Multiples of the linear step above max_token_size / 4, up to the — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_get_token_paddings"></a>`_get_token_paddings(min_token_size: int, max_token_size: int, extra_bucket_sizes: list[int] | None = None)` — [`L1474`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1474) — Generate a list of padding size, starting from min_token_size, — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_is_sequence_parallel_bucket"></a>`_is_sequence_parallel_bucket(size: int, tp: int)` — [`L1497`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1497)
- <a id="_patch_api_server_kernel_reload_endpoint"></a>`_patch_api_server_kernel_reload_endpoint()` — [`L268`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L268) — Add ``POST /reload_kernel`` to the OpenAI API server. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_register_tpu_kv_connectors"></a>`_register_tpu_kv_connectors()` — [`L419`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L419) — Register TPU-specific KV connectors in vLLM's factory name registry.
- <a id="_unwrap_dynamic_compile_fns"></a>`_unwrap_dynamic_compile_fns()` — [`L239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L239) — Unwrap all known ``@torch.compile(dynamic=True)`` decorators in vllm. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_validate_lora_config"></a>`_validate_lora_config(vllm_config: VllmConfig)` — [`L364`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L364) — Rejects LoRA settings that the TPU LoRA path does not support yet.
- <a id="_validate_peer_replay_config"></a>`_validate_peer_replay_config()` — [`L321`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L321) — Fail fast on TPU_PRECOMPILE_PEER_REPLAY with vLLM's compile cache off. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
- <a id="_validate_phased_profiling_config"></a>`_validate_phased_profiling_config(vllm_config: VllmConfig)` — [`L343`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L343) — Fail fast on phased-profiling settings that would silently do nothing.
- <a id="_validate_token_budget_fits_compile_sizes"></a>`_validate_token_budget_fits_compile_sizes(vllm_config: VllmConfig)` — [`L1567`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1567) — Reject a per-step token budget larger than the largest compile size.
- <a id="_patch_api_server_kernel_reload_endpoint.build_app_with_reload"></a>`build_app_with_reload(*args, **kwargs)` — [`L287`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L287)
- <a id="get_tpu_multihost_topology"></a>`get_tpu_multihost_topology(world_size: int, device_name: str | None = None)` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L155) — Return the multi-host mesh topology string for a TPU cluster. — documented in [distributed-parallelism-and-meshes](../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_patch_api_server_kernel_reload_endpoint.build_app_with_reload.reload_kernel"></a>`reload_kernel(raw_request: Request)` — [`L293`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L293)

## Module values
- <a id="TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP"></a>`TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP` — [`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L89)
- <a id="TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP"></a>`TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP` — [`L112`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L112)
- <a id="TPU_3D_TORUS_MULTIHOST_TOPOLOGY_MAP"></a>`TPU_3D_TORUS_MULTIHOST_TOPOLOGY_MAP` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L100)
- <a id="TPU_8I_MULTIHOST_TOPOLOGY_MAP"></a>`TPU_8I_MULTIHOST_TOPOLOGY_MAP` — [`L125`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L125)
- <a id="_DYNAMIC_COMPILE_TARGETS._DYNAMIC_COMPILE_TARGETS"></a>`_DYNAMIC_COMPILE_TARGETS` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L203)
- <a id="_LINEAR_BUCKETS_FROM_BUDGET_FRACTION"></a>`_LINEAR_BUCKETS_FROM_BUDGET_FRACTION` — [`L1403`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1403)
- <a id="_LINEAR_BUCKET_STEPS_PER_BUDGET"></a>`_LINEAR_BUCKET_STEPS_PER_BUDGET` — [`L1404`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1404)
- <a id="_MAX_LINEAR_BUCKETS"></a>`_MAX_LINEAR_BUCKETS` — [`L1410`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L1410)
- <a id="_TPU_2D_TORUS_GENERATIONS"></a>`_TPU_2D_TORUS_GENERATIONS` — [`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L144)
- <a id="_TPU_8I_GENERATIONS"></a>`_TPU_8I_GENERATIONS` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L152)
- <a id="_TPU_DUAL_DEVICE_GENERATIONS"></a>`_TPU_DUAL_DEVICE_GENERATIONS` — [`L149`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L149)
- <a id="_dynamic_compile_unwrapped"></a>`_dynamic_compile_unwrapped` — [`L214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L214)
- <a id="_tpu_kv_connectors_registered"></a>`_tpu_kv_connectors_registered` — [`L215`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L215)
- <a id="logger"></a>`logger` — [`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/platforms/tpu_platform.py#L73)

