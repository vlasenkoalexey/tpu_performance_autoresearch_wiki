---
title: 'Module: src/vllm_torchtpu/envs.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/envs.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.envs`/
symbols:
  env_bool: env_bool().
  environment_variables.environment_variables: environment_variables.environment_variables.
  env_nonnegative_int: env_nonnegative_int().
  env_int: env_int().
  env_with_choices: env_with_choices().
  env_optional_int: env_optional_int().
  env_float: env_float().
  env_str: env_str().
  TPU_KERNEL_ITER_MODE: TPU_KERNEL_ITER_MODE.
  env_optional_bool: env_optional_bool().
  env_positive_int_or_none: env_positive_int_or_none().
  env_nonnegative_float: env_nonnegative_float().
  TPU_MULTIHOST_BACKEND: TPU_MULTIHOST_BACKEND.
  TPU_MOE_COLLECTION_CHUNK_SIZE: TPU_MOE_COLLECTION_CHUNK_SIZE.
  VLLM_TPU_BLOCK_MAJOR_KV: VLLM_TPU_BLOCK_MAJOR_KV.
  __getattr__: __getattr__().
  env_bool._get_bool_env: env_bool()._get_bool_env().
  env_nonnegative_int_or_auto: env_nonnegative_int_or_auto().
  MOE_REQUANTIZE_BLOCK_SIZE: MOE_REQUANTIZE_BLOCK_SIZE.
  TPU_MOE_SKIP_PADDED_TOKENS: TPU_MOE_SKIP_PADDED_TOKENS.
  USE_MOE_FUSED_EP_KERNEL: USE_MOE_FUSED_EP_KERNEL.
  enable_envs_cache: enable_envs_cache().
  TPU_K3_SP_PREFILL: TPU_K3_SP_PREFILL.
  TPU_RAIDEN_TRANSFER_PARALLELISM: TPU_RAIDEN_TRANSFER_PARALLELISM.
  TPU_MOE_SEQUENCE_PARALLEL: TPU_MOE_SEQUENCE_PARALLEL.
  TPU_PP_RING_DEPTH: TPU_PP_RING_DEPTH.
  _nonnegative: _nonnegative().
  TPU_USE_RAIDEN_KV_CACHE_MANAGER: TPU_USE_RAIDEN_KV_CACHE_MANAGER.
  TPU_PARALLEL_PRECOMPILE: TPU_PARALLEL_PRECOMPILE.
  TPU_PRECOMPILE_PEER_REPLAY: TPU_PRECOMPILE_PEER_REPLAY.
  VLLM_TPU_INDEXER_KV_CACHE_MODE: VLLM_TPU_INDEXER_KV_CACHE_MODE.
  TPU_MOE_FP8_ALL_GATHER: TPU_MOE_FP8_ALL_GATHER.
  TORCH_TPU_BASE_PORT: TORCH_TPU_BASE_PORT.
  is_indexer_kv_cache_mode_explicit: is_indexer_kv_cache_mode_explicit().
  TPU_RAIDEN_KIMIK3_ADMISSION: TPU_RAIDEN_KIMIK3_ADMISSION.
  TPU_RAIDEN_JOB_NAME: TPU_RAIDEN_JOB_NAME.
  TPU_RAIDEN_DST_SHARDS: TPU_RAIDEN_DST_SHARDS.
  USE_MOE_SPARSE_CORE: USE_MOE_SPARSE_CORE.
  FUSED_MOE_DECODE_KERNEL: FUSED_MOE_DECODE_KERNEL.
  USE_PHASED_PROFILER: USE_PHASED_PROFILER.
  TPU_GDN_CONV_QK_PAIR_LAYOUT: TPU_GDN_CONV_QK_PAIR_LAYOUT.
  MOE_FUSED_EP_ENABLE_W4A8: MOE_FUSED_EP_ENABLE_W4A8.
  MOE_FUSED_EP_KERNEL_MIN_TOKENS: MOE_FUSED_EP_KERNEL_MIN_TOKENS.
  TPU_PP_CHUNK_SLACK: TPU_PP_CHUNK_SLACK.
  TPU_STREAMIDX_CHUNK_TOKENS: TPU_STREAMIDX_CHUNK_TOKENS.
  USE_RPA_PIPELINED_DMA_STAGING: USE_RPA_PIPELINED_DMA_STAGING.
  TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT: TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT.
  TPU_LOCAL_RANK_OFFSET: TPU_LOCAL_RANK_OFFSET.
  __dir__: __dir__().
  _TRUE_STRINGS: _TRUE_STRINGS.
  _FALSE_STRINGS: _FALSE_STRINGS.
  DEFAULT_INDEXER_KV_CACHE_MODE: DEFAULT_INDEXER_KV_CACHE_MODE.
  use_raiden_glm_admission: use_raiden_glm_admission().
  TPU_LIBRARY_PATH: TPU_LIBRARY_PATH.
  ENABLE_QUANTIZED_MATMUL_KERNEL: ENABLE_QUANTIZED_MATMUL_KERNEL.
  REQUANTIZE_BLOCK_SIZE: REQUANTIZE_BLOCK_SIZE.
  REQUANTIZE_WEIGHT_DTYPE: REQUANTIZE_WEIGHT_DTYPE.
  TPU_FP8_LINEAR_W8A16_MAX_ROWS: TPU_FP8_LINEAR_W8A16_MAX_ROWS.
  MOE_REQUANTIZE_WEIGHT_DTYPE: MOE_REQUANTIZE_WEIGHT_DTYPE.
  TPU_KV_RESHARD_TRANSPORT: TPU_KV_RESHARD_TRANSPORT.
  TPU_RAIDEN_CONTROLLER_ADDRESS: TPU_RAIDEN_CONTROLLER_ADDRESS.
  TPU_RAIDEN_ENGINE_ID: TPU_RAIDEN_ENGINE_ID.
  TPU_RAIDEN_STORE_DISPATCH_PORT_BASE: TPU_RAIDEN_STORE_DISPATCH_PORT_BASE.
  DP_SCHED_ENABLED: DP_SCHED_ENABLED.
  TPU_MLA_MASKED_DENSE_ENABLED: TPU_MLA_MASKED_DENSE_ENABLED.
  MOE_FUSED_EP_KERNEL_IMPL: MOE_FUSED_EP_KERNEL_IMPL.
  MOE_FUSED_EP_SORTED_GATHER: MOE_FUSED_EP_SORTED_GATHER.
  TPU_ROPE_CACHE_ROW_MAJOR: TPU_ROPE_CACHE_ROW_MAJOR.
  TPU_MOE_HASH_TABLE_ROW_MAJOR: TPU_MOE_HASH_TABLE_ROW_MAJOR.
  TPU_PRECOMPILE_BIGGEST_FIRST: TPU_PRECOMPILE_BIGGEST_FIRST.
  TPU_PRECOMPILE_PEER_WAIT_S: TPU_PRECOMPILE_PEER_WAIT_S.
  TPU_STREAMIDX_SMALL_BUCKET_BQ: TPU_STREAMIDX_SMALL_BUCKET_BQ.
  TPU_STREAMIDX_SMALL_BUCKET_BKVP: TPU_STREAMIDX_SMALL_BUCKET_BKVP.
  TPU_STREAMIDX_SMALL_BUCKET_TOKENS: TPU_STREAMIDX_SMALL_BUCKET_TOKENS.
  TPU_SPARSE_MLA_DCP_FUSED_Q_GATHER: TPU_SPARSE_MLA_DCP_FUSED_Q_GATHER.
  TPU_EVICT_WEIGHTS_PAGE_CACHE: TPU_EVICT_WEIGHTS_PAGE_CACHE.
  TPU_SPARSE_MLA_ROPE_LAYOUT: TPU_SPARSE_MLA_ROPE_LAYOUT.
  SPEC_WARMUP: SPEC_WARMUP.
  VLLM_TPU_SRPT_ATTN_WORK_CAP: VLLM_TPU_SRPT_ATTN_WORK_CAP.
  env_with_choices._get_validated_env: env_with_choices()._get_validated_env().
  env_int._get_int_env: env_int()._get_int_env().
  _nonnegative._get_nonnegative_env: _nonnegative()._get_nonnegative_env().
  env_float._get_float_env: env_float()._get_float_env().
  env_nonnegative_float._get_nonnegative_float_env: env_nonnegative_float()._get_nonnegative_float_env().
  env_str._get_str_env: env_str()._get_str_env().
  env_optional_bool._get_optional_bool_env: env_optional_bool()._get_optional_bool_env().
  env_nonnegative_int_or_auto._get_nonnegative_int_or_auto_env: env_nonnegative_int_or_auto()._get_nonnegative_int_or_auto_env().
  env_optional_int._get_optional_int_env: env_optional_int()._get_optional_int_env().
  env_positive_int_or_none._get_positive_int_or_none_env: env_positive_int_or_none()._get_positive_int_or_none_env().
  TPU_ATTN_MOE_OVERLAP: TPU_ATTN_MOE_OVERLAP.
  TPU_DCP_MLA_TOPK_CAP: TPU_DCP_MLA_TOPK_CAP.
  TPU_DCP_MLA_TOPK_CAP_CHUNK: TPU_DCP_MLA_TOPK_CAP_CHUNK.
  TPU_DCP_LSE_MERGE_A2A: TPU_DCP_LSE_MERGE_A2A.
  TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS: TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS.
  TPU_DCP_RS_OUT_PRECISION: TPU_DCP_RS_OUT_PRECISION.
  TPU_MLA_SPARSE_SPLIT_Q: TPU_MLA_SPARSE_SPLIT_Q.
  JAX_PLATFORMS: JAX_PLATFORMS.
  TPU_ACCELERATOR_TYPE: TPU_ACCELERATOR_TYPE.
  TPU_NAME: TPU_NAME.
  TPU_WORKER_ID: TPU_WORKER_ID.
  PYTHON_TRACER_LEVEL: PYTHON_TRACER_LEVEL.
  HOST_TRACER_LEVEL: HOST_TRACER_LEVEL.
  DEVICE_TRACER_LEVEL: DEVICE_TRACER_LEVEL.
  TPU_TRACE_MODE: TPU_TRACE_MODE.
  TPU_NUM_SPARSE_CORES_TO_TRACE: TPU_NUM_SPARSE_CORES_TO_TRACE.
  TPU_NUM_SPARSE_CORE_TILES_TO_TRACE: TPU_NUM_SPARSE_CORE_TILES_TO_TRACE.
  RAY_USAGE_STATS_ENABLED: RAY_USAGE_STATS_ENABLED.
  TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL: TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL.
  TPU_RAIDEN_QWEN35_ADMISSION: TPU_RAIDEN_QWEN35_ADMISSION.
  TPU_RAIDEN_DSV4_ADMISSION: TPU_RAIDEN_DSV4_ADMISSION.
  TPU_RAIDEN_POOL_TAGS_PER_LAYER: TPU_RAIDEN_POOL_TAGS_PER_LAYER.
  TPU_RAIDEN_MAX_TRANSFER_TOKENS: TPU_RAIDEN_MAX_TRANSFER_TOKENS.
  TPU_RAIDEN_RESHARD_IMPL: TPU_RAIDEN_RESHARD_IMPL.
  TPU_RAIDEN_ADVERTISE_HOST: TPU_RAIDEN_ADVERTISE_HOST.
  TPU_RAIDEN_RESHARD_PORT_BASE: TPU_RAIDEN_RESHARD_PORT_BASE.
  TPU_RAIDEN_PREFIX_AWARE_LOAD: TPU_RAIDEN_PREFIX_AWARE_LOAD.
  ONEHOT_MOE_PERMUTE_THRESHOLD: ONEHOT_MOE_PERMUTE_THRESHOLD.
  TPU_MOE_OWNER_OUTPUT_MODE: TPU_MOE_OWNER_OUTPUT_MODE.
  TPU_MOE_DENSE_EXPERT_THRESHOLD: TPU_MOE_DENSE_EXPERT_THRESHOLD.
  FUSED_MOE_DECODE_KERNEL_MAX_TOKENS: FUSED_MOE_DECODE_KERNEL_MAX_TOKENS.
  TPU_MOE_SINGLE_SORT: TPU_MOE_SINGLE_SORT.
  TPU_MOE_COUNTING_SORT: TPU_MOE_COUNTING_SORT.
  USE_MOE_TP_DECODE_KERNEL: USE_MOE_TP_DECODE_KERNEL.
  RAGGED_GATHER_REDUCE_VERSION: RAGGED_GATHER_REDUCE_VERSION.
  TPU_KERNEL_RELOAD_MODULES: TPU_KERNEL_RELOAD_MODULES.
  TPU_GREEDY_TOP_TOKENS: TPU_GREEDY_TOP_TOKENS.
  MLA_XPOSE_N_TILE_SIZE: MLA_XPOSE_N_TILE_SIZE.
  MIXED_Q_SPLIT: MIXED_Q_SPLIT.
  MIXED_NUM_QUERIES_PER_BLOCK: MIXED_NUM_QUERIES_PER_BLOCK.
  MIXED_NUM_KV_PAGES_PER_BLOCK: MIXED_NUM_KV_PAGES_PER_BLOCK.
  VLLM_TPU_MOST_MODEL_LEN: VLLM_TPU_MOST_MODEL_LEN.
  TPU_ENABLE_GDN_DYNAMIC_TILING: TPU_ENABLE_GDN_DYNAMIC_TILING.
  TPU_MOE_HIERARCHICAL_EP: TPU_MOE_HIERARCHICAL_EP.
  TPU_MOE_ROUTER_TOPK: TPU_MOE_ROUTER_TOPK.
  MOE_FUSED_EP_V2_SHARDED_PLAN: MOE_FUSED_EP_V2_SHARDED_PLAN.
  MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE: MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE.
  TPU_LATENT_PROJ_INTRA_CHIP_TP: TPU_LATENT_PROJ_INTRA_CHIP_TP.
  TPU_DSV4_ATTN_INTRA_CHIP_TP: TPU_DSV4_ATTN_INTRA_CHIP_TP.
  TPU_TOKEN_BUCKET_EXTRA: TPU_TOKEN_BUCKET_EXTRA.
  TPU_TOKEN_BUCKET_LINEAR: TPU_TOKEN_BUCKET_LINEAR.
  TPU_PP_DYNAMIC_CHUNKS: TPU_PP_DYNAMIC_CHUNKS.
  TPU_PP_LAZY_PUSH: TPU_PP_LAZY_PUSH.
  TPU_PP_HANDOFF: TPU_PP_HANDOFF.
  TPU_ROPE_CACHE_TRUNCATE: TPU_ROPE_CACHE_TRUNCATE.
  TPU_PRECOMPILE_TRACE_FIRST: TPU_PRECOMPILE_TRACE_FIRST.
  TPU_SPEC_STATIC_VERIFY: TPU_SPEC_STATIC_VERIFY.
  TPU_DCP_INDEXER_A2A_MERGE: TPU_DCP_INDEXER_A2A_MERGE.
  TPU_DCP_INDEXER_A2A_MIN_TOKENS: TPU_DCP_INDEXER_A2A_MIN_TOKENS.
  TPU_SPARSE_MLA_CHUNK_TOKENS: TPU_SPARSE_MLA_CHUNK_TOKENS.
  TPU_PCP_TOPOLOGY_AWARE_MESH: TPU_PCP_TOPOLOGY_AWARE_MESH.
  TPU_SPARSE_MLA_NOPE_LAYOUT: TPU_SPARSE_MLA_NOPE_LAYOUT.
  TPU_KV_TRANSFER_PORT: TPU_KV_TRANSFER_PORT.
  TPU_SIDE_CHANNEL_PORT: TPU_SIDE_CHANNEL_PORT.
  TPU_NODE_ID: TPU_NODE_ID.
  TPU_KV_TRANSFER_CHANNEL_NUMBER: TPU_KV_TRANSFER_CHANNEL_NUMBER.
  TPU_KV_COORD_EXECUTOR_MAX_WORKERS: TPU_KV_COORD_EXECUTOR_MAX_WORKERS.
  TPU_KV_CHANNEL_EXECUTOR_MAX_WORKERS: TPU_KV_CHANNEL_EXECUTOR_MAX_WORKERS.
  TPU_KV_STAGE_WAITER_POOL_SIZE: TPU_KV_STAGE_WAITER_POOL_SIZE.
  TPU_P2P_WAIT_PULL_TIMEOUT: TPU_P2P_WAIT_PULL_TIMEOUT.
  TPU_RAIDEN_STAGE3_STATUS_PROBE_S: TPU_RAIDEN_STAGE3_STATUS_PROBE_S.
  TPU_RAIDEN_STAGE3_DEFERRED_SUBMIT: TPU_RAIDEN_STAGE3_DEFERRED_SUBMIT.
  TPU_RAIDEN_STAGE3_REGISTER_AHEAD: TPU_RAIDEN_STAGE3_REGISTER_AHEAD.
  TPU_RAIDEN_STAGE3_REGISTRATION_WAIT_S: TPU_RAIDEN_STAGE3_REGISTRATION_WAIT_S.
  TPU_RAIDEN_TEST_REGISTRATION_DELAY_S: TPU_RAIDEN_TEST_REGISTRATION_DELAY_S.
  TPU_KV_STAGE_WAIT_TIMEOUT_SECS: TPU_KV_STAGE_WAIT_TIMEOUT_SECS.
  TPU_KV_SHM_POOL_GB: TPU_KV_SHM_POOL_GB.
  TPU_KV_TRANSFER_NAMESPACE: TPU_KV_TRANSFER_NAMESPACE.
  TPU_IPC_SOCKET_DIR: TPU_IPC_SOCKET_DIR.
  TPU_KV_WARMUP_ENABLED: TPU_KV_WARMUP_ENABLED.
  TPU_KV_LATENCY_LOG_INTERVAL: TPU_KV_LATENCY_LOG_INTERVAL.
  TPU_KV_PIN_SHM: TPU_KV_PIN_SHM.
  TPU_USE_RAIDEN_CONNECTOR: TPU_USE_RAIDEN_CONNECTOR.
  TPU_RAIDEN_TRANSFER_NUM_SLOTS: TPU_RAIDEN_TRANSFER_NUM_SLOTS.
  TPU_RAIDEN_POOL_STAGING_LEASES: TPU_RAIDEN_POOL_STAGING_LEASES.
  TPU_RAIDEN_INLINE_LOAD: TPU_RAIDEN_INLINE_LOAD.
  QUANTIZE_ON_LOAD_PREFIXES: QUANTIZE_ON_LOAD_PREFIXES.
  KDA_MANUAL_STATE_DMA: KDA_MANUAL_STATE_DMA.
  KDA_MANUAL_H0_DMA: KDA_MANUAL_H0_DMA.
  KDA_MANUAL_HT_DMA: KDA_MANUAL_HT_DMA.
  KDA_OVERLAP_H0_DMA: KDA_OVERLAP_H0_DMA.
  KDA_OVERLAP_HT_DMA: KDA_OVERLAP_HT_DMA.
  KDA_PACK_HEAD_INV: KDA_PACK_HEAD_INV.
  KDA_PACKED_METADATA: KDA_PACKED_METADATA.
  KDA_FWD_MB: KDA_FWD_MB.
  SC_ALLREDUCE_ALLGATHER_OFFLOAD_MIN_BYTES: SC_ALLREDUCE_ALLGATHER_OFFLOAD_MIN_BYTES.
  RAIDEN_DISABLE_SINGLETON_WORKER: RAIDEN_DISABLE_SINGLETON_WORKER.
  RAIDEN_SHM_KEY: RAIDEN_SHM_KEY.
  RAIDEN_STORAGE_PATH: RAIDEN_STORAGE_PATH.
  RAIDEN_STORAGE_TYPE: RAIDEN_STORAGE_TYPE.
  RAIDEN_STORAGE_CAPACITY_GB: RAIDEN_STORAGE_CAPACITY_GB.
  RAIDEN_STORAGE_PROPERTIES: RAIDEN_STORAGE_PROPERTIES.
  EXPERIMENTAL_RAIDEN_STORAGE_SKIP_PARALLELISM_CHECK: EXPERIMENTAL_RAIDEN_STORAGE_SKIP_PARALLELISM_CHECK.
  VLLM_TPU_OFFLOAD_WAIT_TIMEOUT_S: VLLM_TPU_OFFLOAD_WAIT_TIMEOUT_S.
  VLLM_TPU_OFFLOAD_SAVE_RETRIES: VLLM_TPU_OFFLOAD_SAVE_RETRIES.
  VLLM_TPU_DISABLE_EAGLE_BLOCK_DROP: VLLM_TPU_DISABLE_EAGLE_BLOCK_DROP.
  VLLM_TORCHTPU_IPC_KEY: VLLM_TORCHTPU_IPC_KEY.
  TPU_SHARDED_LOAD_SYNC_EVERY: TPU_SHARDED_LOAD_SYNC_EVERY.
  VLLM_TPU_MXFP4_DEVICE_DEQUANT: VLLM_TPU_MXFP4_DEVICE_DEQUANT.
  VLLM_TPU_DEBUG_PCP_LAYOUT: VLLM_TPU_DEBUG_PCP_LAYOUT.
  VLLM_TPU_DEVICE_ORDER: VLLM_TPU_DEVICE_ORDER.
  DEBUG_TPU_LOCAL_RANK_OFFSET: DEBUG_TPU_LOCAL_RANK_OFFSET.
  TORCH_TPU_MP_RENDEZVOUS_PORT: TORCH_TPU_MP_RENDEZVOUS_PORT.
  VLLM_TPU_FAST_TOKEN_SUBSTITUTION: VLLM_TPU_FAST_TOKEN_SUBSTITUTION.
  VLLM_TPU_FUSED_DRAFT_LOOP: VLLM_TPU_FUSED_DRAFT_LOOP.
  TPU_SAMPLER_TOPK_CANDIDATES: TPU_SAMPLER_TOPK_CANDIDATES.
  MM_ENCODER_FRAME_CHUNK_PATCH_SIZE: MM_ENCODER_FRAME_CHUNK_PATCH_SIZE.
  VLLM_TPU_STATIC_POOLER: VLLM_TPU_STATIC_POOLER.
  VLLM_TPU_POOLING_KV_CACHE_TOKENS: VLLM_TPU_POOLING_KV_CACHE_TOKENS.
  VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS: VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS.
  VLLM_TPU_SRPT_ATTN_TILE_TOKENS: VLLM_TPU_SRPT_ATTN_TILE_TOKENS.
  VLLM_XLA_CHECK_RECOMPILATION: VLLM_XLA_CHECK_RECOMPILATION.
  VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE: VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE.
  TPU_RAIDEN_GLM_ADMISSION: TPU_RAIDEN_GLM_ADMISSION.
  TPU_MLA_MASKED_DENSE_ANALYTIC_MAX_KV_LEN: TPU_MLA_MASKED_DENSE_ANALYTIC_MAX_KV_LEN.
  TPU_MLA_MASKED_DENSE_MAX_KV_LEN: TPU_MLA_MASKED_DENSE_MAX_KV_LEN.
  USE_PIPELINED_DMA_STAGING: USE_PIPELINED_DMA_STAGING.
---
# Module: [`src/vllm_torchtpu/envs.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py)

## Functions
- <a id="__dir__"></a>`__dir__()` — [`L1271`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L1271)
- <a id="__getattr__"></a>`__getattr__(name: str)` — [`L1240`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L1240) — Gets environment variables lazily.
- <a id="env_bool._get_bool_env"></a>`_get_bool_env()` — [`L267`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L267)
- <a id="env_float._get_float_env"></a>`_get_float_env()` — [`L330`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L330)
- <a id="env_int._get_int_env"></a>`_get_int_env()` — [`L290`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L290)
- <a id="_nonnegative._get_nonnegative_env"></a>`_get_nonnegative_env()` — [`L318`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L318)
- <a id="env_nonnegative_float._get_nonnegative_float_env"></a>`_get_nonnegative_float_env()` — [`L352`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L352)
- <a id="env_nonnegative_int_or_auto._get_nonnegative_int_or_auto_env"></a>`_get_nonnegative_int_or_auto_env()` — [`L394`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L394)
- <a id="env_optional_bool._get_optional_bool_env"></a>`_get_optional_bool_env()` — [`L380`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L380)
- <a id="env_optional_int._get_optional_int_env"></a>`_get_optional_int_env()` — [`L410`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L410)
- <a id="env_positive_int_or_none._get_positive_int_or_none_env"></a>`_get_positive_int_or_none_env()` — [`L426`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L426)
- <a id="env_str._get_str_env"></a>`_get_str_env()` — [`L364`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L364)
- <a id="env_with_choices._get_validated_env"></a>`_get_validated_env()` — [`L228`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L228)
- <a id="_nonnegative"></a>`_nonnegative(parse: Callable[[], Any], env_name: str)` — [`L315`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L315) — Wrap a number parser so a negative value raises instead of passing.
- <a id="enable_envs_cache"></a>`enable_envs_cache()` — [`L1252`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L1252) — Enables caching of environment variables by wrapping the module's __getattr__
- <a id="env_bool"></a>`env_bool(env_name: str, default: bool = False)` — [`L259`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L259) — Accepts numeric strings ("0", "1"), boolean strings ("true", "false"),
- <a id="env_float"></a>`env_float(env_name: str, default: float)` — [`L327`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L327) — Float knob with a default. An unparseable value raises.
- <a id="env_int"></a>`env_int(env_name: str, default: int)` — [`L286`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L286) — Integer knob with a default. An unparseable value raises rather than
- <a id="env_nonnegative_float"></a>`env_nonnegative_float(env_name: str, default: float)` — [`L344`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L344) — Float knob that must be finite and not negative.
- <a id="env_nonnegative_int"></a>`env_nonnegative_int(env_name: str, default: int)` — [`L304`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L304) — Integer knob that must not be negative.
- <a id="env_nonnegative_int_or_auto"></a>`env_nonnegative_int_or_auto(env_name: str)` — [`L388`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L388) — Size knob where unset, empty or ``auto`` (any case) reads as ``None``,
- <a id="env_optional_bool"></a>`env_optional_bool(env_name: str)` — [`L373`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L373) — Same parsing as ``env_bool``, but an unset variable reads as ``None`` so
- <a id="env_optional_int"></a>`env_optional_int(env_name: str)` — [`L403`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L403) — Integer parsing where, like ``env_optional_bool``, an unset or empty
- <a id="env_positive_int_or_none"></a>`env_positive_int_or_none(env_name: str)` — [`L419`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L419) — Optional size knob that must be greater than zero when it is set.
- <a id="env_str"></a>`env_str(env_name: str, default: str)` — [`L361`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L361) — String knob with a default, surrounding whitespace stripped.
- <a id="env_with_choices"></a>`env_with_choices(env_name: str, default: str | None, choices: list[str] | Callable[[], list[str]], case_sensitive: bool = True)` — [`L209`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L209) — Create a lambda that validates environment variable against allowed choices
- <a id="is_indexer_kv_cache_mode_explicit"></a>`is_indexer_kv_cache_mode_explicit()` — [`L1281`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L1281) — True when VLLM_TPU_INDEXER_KV_CACHE_MODE was explicitly set. — documented in [deepseek-v4-streamindex-topk-kernel](../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="use_raiden_glm_admission"></a>`use_raiden_glm_admission()` — [`L1275`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L1275) — True when Raiden KV-cache manager and GLM Stage-3 admission are both enabled.

## Module values
- <a id="DEBUG_TPU_LOCAL_RANK_OFFSET"></a>`DEBUG_TPU_LOCAL_RANK_OFFSET` — [`L195`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L195)
- <a id="DEFAULT_INDEXER_KV_CACHE_MODE"></a>`DEFAULT_INDEXER_KV_CACHE_MODE` — [`L256`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L256)
- <a id="DEVICE_TRACER_LEVEL"></a>`DEVICE_TRACER_LEVEL` — [`L40`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L40) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="DP_SCHED_ENABLED"></a>`DP_SCHED_ENABLED` — [`L86`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L86)
- <a id="ENABLE_QUANTIZED_MATMUL_KERNEL"></a>`ENABLE_QUANTIZED_MATMUL_KERNEL` — [`L46`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L46)
- <a id="EXPERIMENTAL_RAIDEN_STORAGE_SKIP_PARALLELISM_CHECK"></a>`EXPERIMENTAL_RAIDEN_STORAGE_SKIP_PARALLELISM_CHECK` — [`L185`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L185) — documented in [host-offload](../../../concepts/host-offload.md)
- <a id="FUSED_MOE_DECODE_KERNEL"></a>`FUSED_MOE_DECODE_KERNEL` — [`L76`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L76)
- <a id="FUSED_MOE_DECODE_KERNEL_MAX_TOKENS"></a>`FUSED_MOE_DECODE_KERNEL_MAX_TOKENS` — [`L77`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L77)
- <a id="HOST_TRACER_LEVEL"></a>`HOST_TRACER_LEVEL` — [`L39`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L39) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="JAX_PLATFORMS"></a>`JAX_PLATFORMS` — [`L31`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L31)
- <a id="KDA_FWD_MB"></a>`KDA_FWD_MB` — [`L175`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L175)
- <a id="KDA_MANUAL_H0_DMA"></a>`KDA_MANUAL_H0_DMA` — [`L169`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L169)
- <a id="KDA_MANUAL_HT_DMA"></a>`KDA_MANUAL_HT_DMA` — [`L170`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L170)
- <a id="KDA_MANUAL_STATE_DMA"></a>`KDA_MANUAL_STATE_DMA` — [`L168`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L168)
- <a id="KDA_OVERLAP_H0_DMA"></a>`KDA_OVERLAP_H0_DMA` — [`L171`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L171)
- <a id="KDA_OVERLAP_HT_DMA"></a>`KDA_OVERLAP_HT_DMA` — [`L172`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L172)
- <a id="KDA_PACKED_METADATA"></a>`KDA_PACKED_METADATA` — [`L174`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L174)
- <a id="KDA_PACK_HEAD_INV"></a>`KDA_PACK_HEAD_INV` — [`L173`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L173)
- <a id="MIXED_NUM_KV_PAGES_PER_BLOCK"></a>`MIXED_NUM_KV_PAGES_PER_BLOCK` — [`L90`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L90)
- <a id="MIXED_NUM_QUERIES_PER_BLOCK"></a>`MIXED_NUM_QUERIES_PER_BLOCK` — [`L89`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L89)
- <a id="MIXED_Q_SPLIT"></a>`MIXED_Q_SPLIT` — [`L88`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L88)
- <a id="MLA_XPOSE_N_TILE_SIZE"></a>`MLA_XPOSE_N_TILE_SIZE` — [`L87`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L87)
- <a id="MM_ENCODER_FRAME_CHUNK_PATCH_SIZE"></a>`MM_ENCODER_FRAME_CHUNK_PATCH_SIZE` — [`L201`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L201)
- <a id="MOE_FUSED_EP_ENABLE_W4A8"></a>`MOE_FUSED_EP_ENABLE_W4A8` — [`L102`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L102)
- <a id="MOE_FUSED_EP_KERNEL_IMPL"></a>`MOE_FUSED_EP_KERNEL_IMPL` — [`L101`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L101)
- <a id="MOE_FUSED_EP_KERNEL_MIN_TOKENS"></a>`MOE_FUSED_EP_KERNEL_MIN_TOKENS` — [`L103`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L103)
- <a id="MOE_FUSED_EP_SORTED_GATHER"></a>`MOE_FUSED_EP_SORTED_GATHER` — [`L105`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L105)
- <a id="MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE"></a>`MOE_FUSED_EP_V2_HEIGHT_RUNGS_OVERRIDE` — [`L106`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L106) — documented in [fused-moe-kernels](../../../concepts/fused-moe-kernels.md)
- <a id="MOE_FUSED_EP_V2_SHARDED_PLAN"></a>`MOE_FUSED_EP_V2_SHARDED_PLAN` — [`L104`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L104)
- <a id="MOE_REQUANTIZE_BLOCK_SIZE"></a>`MOE_REQUANTIZE_BLOCK_SIZE` — [`L51`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L51)
- <a id="MOE_REQUANTIZE_WEIGHT_DTYPE"></a>`MOE_REQUANTIZE_WEIGHT_DTYPE` — [`L50`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L50)
- <a id="ONEHOT_MOE_PERMUTE_THRESHOLD"></a>`ONEHOT_MOE_PERMUTE_THRESHOLD` — [`L72`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L72)
- <a id="PYTHON_TRACER_LEVEL"></a>`PYTHON_TRACER_LEVEL` — [`L38`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L38) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="QUANTIZE_ON_LOAD_PREFIXES"></a>`QUANTIZE_ON_LOAD_PREFIXES` — [`L167`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L167)
- <a id="RAGGED_GATHER_REDUCE_VERSION"></a>`RAGGED_GATHER_REDUCE_VERSION` — [`L81`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L81)
- <a id="RAIDEN_DISABLE_SINGLETON_WORKER"></a>`RAIDEN_DISABLE_SINGLETON_WORKER` — [`L179`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L179)
- <a id="RAIDEN_SHM_KEY"></a>`RAIDEN_SHM_KEY` — [`L180`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L180)
- <a id="RAIDEN_STORAGE_CAPACITY_GB"></a>`RAIDEN_STORAGE_CAPACITY_GB` — [`L183`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L183)
- <a id="RAIDEN_STORAGE_PATH"></a>`RAIDEN_STORAGE_PATH` — [`L181`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L181)
- <a id="RAIDEN_STORAGE_PROPERTIES"></a>`RAIDEN_STORAGE_PROPERTIES` — [`L184`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L184)
- <a id="RAIDEN_STORAGE_TYPE"></a>`RAIDEN_STORAGE_TYPE` — [`L182`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L182)
- <a id="RAY_USAGE_STATS_ENABLED"></a>`RAY_USAGE_STATS_ENABLED` — [`L44`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L44)
- <a id="REQUANTIZE_BLOCK_SIZE"></a>`REQUANTIZE_BLOCK_SIZE` — [`L47`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L47)
- <a id="REQUANTIZE_WEIGHT_DTYPE"></a>`REQUANTIZE_WEIGHT_DTYPE` — [`L48`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L48)
- <a id="SC_ALLREDUCE_ALLGATHER_OFFLOAD_MIN_BYTES"></a>`SC_ALLREDUCE_ALLGATHER_OFFLOAD_MIN_BYTES` — [`L177`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L177)
- <a id="SPEC_WARMUP"></a>`SPEC_WARMUP` — [`L178`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L178)
- <a id="TORCH_TPU_BASE_PORT"></a>`TORCH_TPU_BASE_PORT` — [`L196`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L196)
- <a id="TORCH_TPU_MP_RENDEZVOUS_PORT"></a>`TORCH_TPU_MP_RENDEZVOUS_PORT` — [`L197`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L197)
- <a id="TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT"></a>`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT` — [`L176`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L176)
- <a id="TPU_ACCELERATOR_TYPE"></a>`TPU_ACCELERATOR_TYPE` — [`L32`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L32)
- <a id="TPU_ATTN_MOE_OVERLAP"></a>`TPU_ATTN_MOE_OVERLAP` — [`L23`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L23)
- <a id="TPU_DCP_INDEXER_A2A_MERGE"></a>`TPU_DCP_INDEXER_A2A_MERGE` — [`L126`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L126)
- <a id="TPU_DCP_INDEXER_A2A_MIN_TOKENS"></a>`TPU_DCP_INDEXER_A2A_MIN_TOKENS` — [`L127`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L127)
- <a id="TPU_DCP_LSE_MERGE_A2A"></a>`TPU_DCP_LSE_MERGE_A2A` — [`L27`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L27)
- <a id="TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS"></a>`TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS` — [`L28`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L28)
- <a id="TPU_DCP_MLA_TOPK_CAP"></a>`TPU_DCP_MLA_TOPK_CAP` — [`L25`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L25)
- <a id="TPU_DCP_MLA_TOPK_CAP_CHUNK"></a>`TPU_DCP_MLA_TOPK_CAP_CHUNK` — [`L26`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L26)
- <a id="TPU_DCP_RS_OUT_PRECISION"></a>`TPU_DCP_RS_OUT_PRECISION` — [`L29`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L29)
- <a id="TPU_DSV4_ATTN_INTRA_CHIP_TP"></a>`TPU_DSV4_ATTN_INTRA_CHIP_TP` — [`L108`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L108)
- <a id="TPU_ENABLE_GDN_DYNAMIC_TILING"></a>`TPU_ENABLE_GDN_DYNAMIC_TILING` — [`L96`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L96) — documented in [gated-deltanet-kernels](../../../concepts/gated-deltanet-kernels.md)
- <a id="TPU_EVICT_WEIGHTS_PAGE_CACHE"></a>`TPU_EVICT_WEIGHTS_PAGE_CACHE` — [`L140`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L140)
- <a id="TPU_FP8_LINEAR_W8A16_MAX_ROWS"></a>`TPU_FP8_LINEAR_W8A16_MAX_ROWS` — [`L49`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L49)
- <a id="TPU_GDN_CONV_QK_PAIR_LAYOUT"></a>`TPU_GDN_CONV_QK_PAIR_LAYOUT` — [`L95`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L95)
- <a id="TPU_GREEDY_TOP_TOKENS"></a>`TPU_GREEDY_TOP_TOKENS` — [`L85`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L85)
- <a id="TPU_IPC_SOCKET_DIR"></a>`TPU_IPC_SOCKET_DIR` — [`L159`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L159)
- <a id="TPU_K3_SP_PREFILL"></a>`TPU_K3_SP_PREFILL` — [`L24`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L24)
- <a id="TPU_KERNEL_ITER_MODE"></a>`TPU_KERNEL_ITER_MODE` — [`L83`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L83) — documented in [pcp-streaming-rpa-kernel](../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="TPU_KERNEL_RELOAD_MODULES"></a>`TPU_KERNEL_RELOAD_MODULES` — [`L84`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L84)
- <a id="TPU_KV_CHANNEL_EXECUTOR_MAX_WORKERS"></a>`TPU_KV_CHANNEL_EXECUTOR_MAX_WORKERS` — [`L148`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L148)
- <a id="TPU_KV_COORD_EXECUTOR_MAX_WORKERS"></a>`TPU_KV_COORD_EXECUTOR_MAX_WORKERS` — [`L147`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L147)
- <a id="TPU_KV_LATENCY_LOG_INTERVAL"></a>`TPU_KV_LATENCY_LOG_INTERVAL` — [`L161`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L161)
- <a id="TPU_KV_PIN_SHM"></a>`TPU_KV_PIN_SHM` — [`L162`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L162)
- <a id="TPU_KV_RESHARD_TRANSPORT"></a>`TPU_KV_RESHARD_TRANSPORT` — [`L58`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L58) — documented in [tpu-schedulers](../../../concepts/tpu-schedulers.md)
- <a id="TPU_KV_SHM_POOL_GB"></a>`TPU_KV_SHM_POOL_GB` — [`L157`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L157)
- <a id="TPU_KV_STAGE_WAITER_POOL_SIZE"></a>`TPU_KV_STAGE_WAITER_POOL_SIZE` — [`L149`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L149)
- <a id="TPU_KV_STAGE_WAIT_TIMEOUT_SECS"></a>`TPU_KV_STAGE_WAIT_TIMEOUT_SECS` — [`L156`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L156)
- <a id="TPU_KV_TRANSFER_CHANNEL_NUMBER"></a>`TPU_KV_TRANSFER_CHANNEL_NUMBER` — [`L146`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L146)
- <a id="TPU_KV_TRANSFER_NAMESPACE"></a>`TPU_KV_TRANSFER_NAMESPACE` — [`L158`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L158)
- <a id="TPU_KV_TRANSFER_PORT"></a>`TPU_KV_TRANSFER_PORT` — [`L143`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L143)
- <a id="TPU_KV_WARMUP_ENABLED"></a>`TPU_KV_WARMUP_ENABLED` — [`L160`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L160)
- <a id="TPU_LATENT_PROJ_INTRA_CHIP_TP"></a>`TPU_LATENT_PROJ_INTRA_CHIP_TP` — [`L107`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L107)
- <a id="TPU_LIBRARY_PATH"></a>`TPU_LIBRARY_PATH` — [`L34`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L34)
- <a id="TPU_LOCAL_RANK_OFFSET"></a>`TPU_LOCAL_RANK_OFFSET` — [`L193`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L193)
- <a id="TPU_MLA_MASKED_DENSE_ANALYTIC_MAX_KV_LEN"></a>`TPU_MLA_MASKED_DENSE_ANALYTIC_MAX_KV_LEN` — [`L92`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L92)
- <a id="TPU_MLA_MASKED_DENSE_ENABLED"></a>`TPU_MLA_MASKED_DENSE_ENABLED` — [`L91`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L91)
- <a id="TPU_MLA_MASKED_DENSE_MAX_KV_LEN"></a>`TPU_MLA_MASKED_DENSE_MAX_KV_LEN` — [`L93`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L93)
- <a id="TPU_MLA_SPARSE_SPLIT_Q"></a>`TPU_MLA_SPARSE_SPLIT_Q` — [`L30`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L30)
- <a id="TPU_MOE_COLLECTION_CHUNK_SIZE"></a>`TPU_MOE_COLLECTION_CHUNK_SIZE` — [`L134`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L134)
- <a id="TPU_MOE_COUNTING_SORT"></a>`TPU_MOE_COUNTING_SORT` — [`L79`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L79)
- <a id="TPU_MOE_DENSE_EXPERT_THRESHOLD"></a>`TPU_MOE_DENSE_EXPERT_THRESHOLD` — [`L75`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L75)
- <a id="TPU_MOE_FP8_ALL_GATHER"></a>`TPU_MOE_FP8_ALL_GATHER` — [`L135`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L135)
- <a id="TPU_MOE_HASH_TABLE_ROW_MAJOR"></a>`TPU_MOE_HASH_TABLE_ROW_MAJOR` — [`L118`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L118)
- <a id="TPU_MOE_HIERARCHICAL_EP"></a>`TPU_MOE_HIERARCHICAL_EP` — [`L98`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L98)
- <a id="TPU_MOE_OWNER_OUTPUT_MODE"></a>`TPU_MOE_OWNER_OUTPUT_MODE` — [`L74`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L74)
- <a id="TPU_MOE_ROUTER_TOPK"></a>`TPU_MOE_ROUTER_TOPK` — [`L99`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L99)
- <a id="TPU_MOE_SEQUENCE_PARALLEL"></a>`TPU_MOE_SEQUENCE_PARALLEL` — [`L73`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L73)
- <a id="TPU_MOE_SINGLE_SORT"></a>`TPU_MOE_SINGLE_SORT` — [`L78`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L78)
- <a id="TPU_MOE_SKIP_PADDED_TOKENS"></a>`TPU_MOE_SKIP_PADDED_TOKENS` — [`L97`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L97)
- <a id="TPU_MULTIHOST_BACKEND"></a>`TPU_MULTIHOST_BACKEND` — [`L36`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L36)
- <a id="TPU_NAME"></a>`TPU_NAME` — [`L33`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L33)
- <a id="TPU_NODE_ID"></a>`TPU_NODE_ID` — [`L145`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L145)
- <a id="TPU_NUM_SPARSE_CORES_TO_TRACE"></a>`TPU_NUM_SPARSE_CORES_TO_TRACE` — [`L42`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L42) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="TPU_NUM_SPARSE_CORE_TILES_TO_TRACE"></a>`TPU_NUM_SPARSE_CORE_TILES_TO_TRACE` — [`L43`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L43) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="TPU_P2P_WAIT_PULL_TIMEOUT"></a>`TPU_P2P_WAIT_PULL_TIMEOUT` — [`L150`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L150)
- <a id="TPU_PARALLEL_PRECOMPILE"></a>`TPU_PARALLEL_PRECOMPILE` — [`L119`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L119)
- <a id="TPU_PCP_TOPOLOGY_AWARE_MESH"></a>`TPU_PCP_TOPOLOGY_AWARE_MESH` — [`L136`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L136)
- <a id="TPU_PP_CHUNK_SLACK"></a>`TPU_PP_CHUNK_SLACK` — [`L112`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L112) — documented in [tpu-schedulers](../../../concepts/tpu-schedulers.md)
- <a id="TPU_PP_DYNAMIC_CHUNKS"></a>`TPU_PP_DYNAMIC_CHUNKS` — [`L111`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L111)
- <a id="TPU_PP_HANDOFF"></a>`TPU_PP_HANDOFF` — [`L114`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L114)
- <a id="TPU_PP_LAZY_PUSH"></a>`TPU_PP_LAZY_PUSH` — [`L113`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L113)
- <a id="TPU_PP_RING_DEPTH"></a>`TPU_PP_RING_DEPTH` — [`L115`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L115)
- <a id="TPU_PRECOMPILE_BIGGEST_FIRST"></a>`TPU_PRECOMPILE_BIGGEST_FIRST` — [`L120`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L120)
- <a id="TPU_PRECOMPILE_PEER_REPLAY"></a>`TPU_PRECOMPILE_PEER_REPLAY` — [`L121`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L121)
- <a id="TPU_PRECOMPILE_PEER_WAIT_S"></a>`TPU_PRECOMPILE_PEER_WAIT_S` — [`L122`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L122)
- <a id="TPU_PRECOMPILE_TRACE_FIRST"></a>`TPU_PRECOMPILE_TRACE_FIRST` — [`L123`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L123)
- <a id="TPU_RAIDEN_ADVERTISE_HOST"></a>`TPU_RAIDEN_ADVERTISE_HOST` — [`L67`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L67)
- <a id="TPU_RAIDEN_CONTROLLER_ADDRESS"></a>`TPU_RAIDEN_CONTROLLER_ADDRESS` — [`L59`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L59)
- <a id="TPU_RAIDEN_DST_SHARDS"></a>`TPU_RAIDEN_DST_SHARDS` — [`L63`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L63)
- <a id="TPU_RAIDEN_DSV4_ADMISSION"></a>`TPU_RAIDEN_DSV4_ADMISSION` — [`L57`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L57)
- <a id="TPU_RAIDEN_ENGINE_ID"></a>`TPU_RAIDEN_ENGINE_ID` — [`L61`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L61)
- <a id="TPU_RAIDEN_GLM_ADMISSION"></a>`TPU_RAIDEN_GLM_ADMISSION` — [`L56`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L56)
- <a id="TPU_RAIDEN_INLINE_LOAD"></a>`TPU_RAIDEN_INLINE_LOAD` — [`L166`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L166)
- <a id="TPU_RAIDEN_JOB_NAME"></a>`TPU_RAIDEN_JOB_NAME` — [`L60`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L60)
- <a id="TPU_RAIDEN_KIMIK3_ADMISSION"></a>`TPU_RAIDEN_KIMIK3_ADMISSION` — [`L55`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L55)
- <a id="TPU_RAIDEN_MAX_TRANSFER_TOKENS"></a>`TPU_RAIDEN_MAX_TRANSFER_TOKENS` — [`L65`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L65)
- <a id="TPU_RAIDEN_POOL_STAGING_LEASES"></a>`TPU_RAIDEN_POOL_STAGING_LEASES` — [`L165`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L165)
- <a id="TPU_RAIDEN_POOL_TAGS_PER_LAYER"></a>`TPU_RAIDEN_POOL_TAGS_PER_LAYER` — [`L64`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L64)
- <a id="TPU_RAIDEN_PREFIX_AWARE_LOAD"></a>`TPU_RAIDEN_PREFIX_AWARE_LOAD` — [`L70`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L70) — documented in [kv-transfer-and-disaggregated-serving](../../../concepts/kv-transfer-and-disaggregated-serving.md)
- <a id="TPU_RAIDEN_QWEN35_ADMISSION"></a>`TPU_RAIDEN_QWEN35_ADMISSION` — [`L54`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L54)
- <a id="TPU_RAIDEN_RESHARD_IMPL"></a>`TPU_RAIDEN_RESHARD_IMPL` — [`L66`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L66)
- <a id="TPU_RAIDEN_RESHARD_PORT_BASE"></a>`TPU_RAIDEN_RESHARD_PORT_BASE` — [`L68`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L68)
- <a id="TPU_RAIDEN_STAGE3_DEFERRED_SUBMIT"></a>`TPU_RAIDEN_STAGE3_DEFERRED_SUBMIT` — [`L152`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L152)
- <a id="TPU_RAIDEN_STAGE3_REGISTER_AHEAD"></a>`TPU_RAIDEN_STAGE3_REGISTER_AHEAD` — [`L153`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L153)
- <a id="TPU_RAIDEN_STAGE3_REGISTRATION_WAIT_S"></a>`TPU_RAIDEN_STAGE3_REGISTRATION_WAIT_S` — [`L154`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L154)
- <a id="TPU_RAIDEN_STAGE3_STATUS_PROBE_S"></a>`TPU_RAIDEN_STAGE3_STATUS_PROBE_S` — [`L151`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L151)
- <a id="TPU_RAIDEN_STORE_DISPATCH_PORT_BASE"></a>`TPU_RAIDEN_STORE_DISPATCH_PORT_BASE` — [`L69`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L69)
- <a id="TPU_RAIDEN_TEST_REGISTRATION_DELAY_S"></a>`TPU_RAIDEN_TEST_REGISTRATION_DELAY_S` — [`L155`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L155)
- <a id="TPU_RAIDEN_TRANSFER_NUM_SLOTS"></a>`TPU_RAIDEN_TRANSFER_NUM_SLOTS` — [`L164`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L164)
- <a id="TPU_RAIDEN_TRANSFER_PARALLELISM"></a>`TPU_RAIDEN_TRANSFER_PARALLELISM` — [`L62`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L62)
- <a id="TPU_ROPE_CACHE_ROW_MAJOR"></a>`TPU_ROPE_CACHE_ROW_MAJOR` — [`L117`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L117)
- <a id="TPU_ROPE_CACHE_TRUNCATE"></a>`TPU_ROPE_CACHE_TRUNCATE` — [`L116`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L116)
- <a id="TPU_SAMPLER_TOPK_CANDIDATES"></a>`TPU_SAMPLER_TOPK_CANDIDATES` — [`L200`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L200)
- <a id="TPU_SHARDED_LOAD_SYNC_EVERY"></a>`TPU_SHARDED_LOAD_SYNC_EVERY` — [`L190`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L190)
- <a id="TPU_SIDE_CHANNEL_PORT"></a>`TPU_SIDE_CHANNEL_PORT` — [`L144`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L144)
- <a id="TPU_SPARSE_MLA_CHUNK_TOKENS"></a>`TPU_SPARSE_MLA_CHUNK_TOKENS` — [`L133`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L133)
- <a id="TPU_SPARSE_MLA_DCP_FUSED_Q_GATHER"></a>`TPU_SPARSE_MLA_DCP_FUSED_Q_GATHER` — [`L132`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L132)
- <a id="TPU_SPARSE_MLA_NOPE_LAYOUT"></a>`TPU_SPARSE_MLA_NOPE_LAYOUT` — [`L141`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L141)
- <a id="TPU_SPARSE_MLA_ROPE_LAYOUT"></a>`TPU_SPARSE_MLA_ROPE_LAYOUT` — [`L142`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L142)
- <a id="TPU_SPEC_STATIC_VERIFY"></a>`TPU_SPEC_STATIC_VERIFY` — [`L125`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L125)
- <a id="TPU_STREAMIDX_CHUNK_TOKENS"></a>`TPU_STREAMIDX_CHUNK_TOKENS` — [`L124`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L124)
- <a id="TPU_STREAMIDX_SMALL_BUCKET_BKVP"></a>`TPU_STREAMIDX_SMALL_BUCKET_BKVP` — [`L129`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L129)
- <a id="TPU_STREAMIDX_SMALL_BUCKET_BQ"></a>`TPU_STREAMIDX_SMALL_BUCKET_BQ` — [`L128`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L128)
- <a id="TPU_STREAMIDX_SMALL_BUCKET_TOKENS"></a>`TPU_STREAMIDX_SMALL_BUCKET_TOKENS` — [`L130`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L130)
- <a id="TPU_TOKEN_BUCKET_EXTRA"></a>`TPU_TOKEN_BUCKET_EXTRA` — [`L109`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L109)
- <a id="TPU_TOKEN_BUCKET_LINEAR"></a>`TPU_TOKEN_BUCKET_LINEAR` — [`L110`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L110)
- <a id="TPU_TRACE_MODE"></a>`TPU_TRACE_MODE` — [`L41`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L41) — documented in [tracing-annotations](../../../concepts/tracing-annotations.md)
- <a id="TPU_USE_RAIDEN_CONNECTOR"></a>`TPU_USE_RAIDEN_CONNECTOR` — [`L163`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L163)
- <a id="TPU_USE_RAIDEN_KV_CACHE_MANAGER"></a>`TPU_USE_RAIDEN_KV_CACHE_MANAGER` — [`L53`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L53)
- <a id="TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL"></a>`TPU_VLLM_ENABLE_UNIFIED_BLOCK_POOL` — [`L52`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L52)
- <a id="TPU_WORKER_ID"></a>`TPU_WORKER_ID` — [`L35`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L35)
- <a id="USE_MOE_FUSED_EP_KERNEL"></a>`USE_MOE_FUSED_EP_KERNEL` — [`L100`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L100)
- <a id="USE_MOE_SPARSE_CORE"></a>`USE_MOE_SPARSE_CORE` — [`L71`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L71)
- <a id="USE_MOE_TP_DECODE_KERNEL"></a>`USE_MOE_TP_DECODE_KERNEL` — [`L80`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L80)
- <a id="USE_PHASED_PROFILER"></a>`USE_PHASED_PROFILER` — [`L82`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L82)
- <a id="USE_PIPELINED_DMA_STAGING"></a>`USE_PIPELINED_DMA_STAGING` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L138)
- <a id="USE_RPA_PIPELINED_DMA_STAGING"></a>`USE_RPA_PIPELINED_DMA_STAGING` — [`L137`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L137) — documented in [ragged-paged-attention-kernel](../../../concepts/ragged-paged-attention-kernel.md)
- <a id="VLLM_TORCHTPU_IPC_KEY"></a>`VLLM_TORCHTPU_IPC_KEY` — [`L189`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L189)
- <a id="VLLM_TPU_BLOCK_MAJOR_KV"></a>`VLLM_TPU_BLOCK_MAJOR_KV` — [`L139`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L139) — documented in [host-offload](../../../concepts/host-offload.md)
- <a id="VLLM_TPU_DEBUG_PCP_LAYOUT"></a>`VLLM_TPU_DEBUG_PCP_LAYOUT` — [`L192`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L192)
- <a id="VLLM_TPU_DEVICE_ORDER"></a>`VLLM_TPU_DEVICE_ORDER` — [`L194`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L194)
- <a id="VLLM_TPU_DISABLE_EAGLE_BLOCK_DROP"></a>`VLLM_TPU_DISABLE_EAGLE_BLOCK_DROP` — [`L188`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L188)
- <a id="VLLM_TPU_FAST_TOKEN_SUBSTITUTION"></a>`VLLM_TPU_FAST_TOKEN_SUBSTITUTION` — [`L198`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L198)
- <a id="VLLM_TPU_FUSED_DRAFT_LOOP"></a>`VLLM_TPU_FUSED_DRAFT_LOOP` — [`L199`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L199)
- <a id="VLLM_TPU_INDEXER_KV_CACHE_MODE"></a>`VLLM_TPU_INDEXER_KV_CACHE_MODE` — [`L131`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L131) — documented in [deepseek-v4-streamindex-topk-kernel](../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="VLLM_TPU_MOST_MODEL_LEN"></a>`VLLM_TPU_MOST_MODEL_LEN` — [`L94`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L94)
- <a id="VLLM_TPU_MXFP4_DEVICE_DEQUANT"></a>`VLLM_TPU_MXFP4_DEVICE_DEQUANT` — [`L191`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L191)
- <a id="VLLM_TPU_OFFLOAD_SAVE_RETRIES"></a>`VLLM_TPU_OFFLOAD_SAVE_RETRIES` — [`L187`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L187)
- <a id="VLLM_TPU_OFFLOAD_WAIT_TIMEOUT_S"></a>`VLLM_TPU_OFFLOAD_WAIT_TIMEOUT_S` — [`L186`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L186)
- <a id="VLLM_TPU_POOLING_KV_CACHE_TOKENS"></a>`VLLM_TPU_POOLING_KV_CACHE_TOKENS` — [`L203`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L203)
- <a id="VLLM_TPU_SRPT_ATTN_TILE_TOKENS"></a>`VLLM_TPU_SRPT_ATTN_TILE_TOKENS` — [`L206`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L206)
- <a id="VLLM_TPU_SRPT_ATTN_WORK_CAP"></a>`VLLM_TPU_SRPT_ATTN_WORK_CAP` — [`L205`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L205)
- <a id="VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS"></a>`VLLM_TPU_SRPT_MAX_CONSECUTIVE_HOLDS` — [`L204`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L204)
- <a id="VLLM_TPU_STATIC_POOLER"></a>`VLLM_TPU_STATIC_POOLER` — [`L202`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L202)
- <a id="VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE"></a>`VLLM_USE_RAY_COMPILED_DAG_CHANNEL_TYPE` — [`L45`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L45)
- <a id="VLLM_XLA_CHECK_RECOMPILATION"></a>`VLLM_XLA_CHECK_RECOMPILATION` — [`L37`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L37)
- <a id="_FALSE_STRINGS"></a>`_FALSE_STRINGS` — [`L255`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L255)
- <a id="_TRUE_STRINGS"></a>`_TRUE_STRINGS` — [`L254`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L254)
- <a id="environment_variables.environment_variables"></a>`environment_variables` — [`L435`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/envs.py#L435) — documented in [compilation-and-graph-capture](../../../concepts/compilation-and-graph-capture.md)

