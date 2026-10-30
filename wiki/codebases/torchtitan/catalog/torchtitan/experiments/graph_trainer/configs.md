---
title: 'Module: torchtitan/experiments/graph_trainer/configs.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/configs.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.configs`/
symbols:
  GraphTrainerCompileConfig: GraphTrainerCompileConfig#
  to_graph_trainer_config: to_graph_trainer_config().
  validate_ep_overlap_config: validate_ep_overlap_config().
  EpOverlapConfig: EpOverlapConfig#
  GraphTrainerCompileConfig.ep_overlap: GraphTrainerCompileConfig#ep_overlap.
  trace_input_preparer_keys: trace_input_preparer_keys().
  validate_autoparallel_config: validate_autoparallel_config().
  GraphTrainerCompileConfig.mode: GraphTrainerCompileConfig#mode.
  EpOverlapConfig.module_fqn: EpOverlapConfig#module_fqn.
  EpOverlapConfig.enabled: EpOverlapConfig#enabled.
  EpOverlapConfig.chunk_dim: EpOverlapConfig#chunk_dim.
  EpOverlapConfig.strategy: EpOverlapConfig#strategy.
  GraphTrainerCompileConfig.enable_passes: GraphTrainerCompileConfig#enable_passes.
  GraphTrainerCompileConfig.memory_policy: GraphTrainerCompileConfig#memory_policy.
  GraphTrainerCompileConfig.backend: GraphTrainerCompileConfig#backend.
  GraphTrainerCompileConfig.passes: GraphTrainerCompileConfig#passes.
  GraphTrainerCompileConfig.inductor_compilation: GraphTrainerCompileConfig#inductor_compilation.
  EpOverlapChunkDim: EpOverlapChunkDim.
  MOE_BLOCK_FQN: MOE_BLOCK_FQN.
  SUPPORTED_EP_OVERLAP_MODULE_FQNS: SUPPORTED_EP_OVERLAP_MODULE_FQNS.
  GraphTrainerCompileConfig.precompile_artifact_dir: GraphTrainerCompileConfig#precompile_artifact_dir.
  GraphTrainerCompileConfig.full_recompute_save_ops: GraphTrainerCompileConfig#full_recompute_save_ops.
  GraphTrainerCompileConfig.cpu_offload_budget_gb: GraphTrainerCompileConfig#cpu_offload_budget_gb.
  GraphTrainerCompileConfig.enable_autoparallel: GraphTrainerCompileConfig#enable_autoparallel.
  TRANSFORMER_BLOCK_FQN: TRANSFORMER_BLOCK_FQN.
  GraphTrainerCompileConfig.disable_passes: GraphTrainerCompileConfig#disable_passes.
  GraphTrainerMemoryPolicy: GraphTrainerMemoryPolicy.
  EpOverlapConfig.disable_early_grad_accumulation: EpOverlapConfig#disable_early_grad_accumulation.
  GraphTrainerCompileConfig.numerics_changing_optim: GraphTrainerCompileConfig#numerics_changing_optim.
  EpOverlapChunkStrategy: EpOverlapChunkStrategy.
  GraphTrainerCompileConfig.cpu_offload_prefetch_n_layers: GraphTrainerCompileConfig#cpu_offload_prefetch_n_layers.
  GraphTrainerCompileConfig.cpu_offload_defer_n_layers: GraphTrainerCompileConfig#cpu_offload_defer_n_layers.
  GraphTrainerCompileConfig.enable_inplace_graph_gradient_accumulation: GraphTrainerCompileConfig#enable_inplace_graph_gradient_accumulation.
  GraphTrainerCompileConfig.debug_graph_passes: GraphTrainerCompileConfig#debug_graph_passes.
  GraphTrainerCompileConfig.enable_fsdp_ag_rs_overlap: GraphTrainerCompileConfig#enable_fsdp_ag_rs_overlap.
  GraphTrainerCompileConfig.enable_fsdp_dense_region_overlap: GraphTrainerCompileConfig#enable_fsdp_dense_region_overlap.
  GraphTrainerCompileConfig.pass_pipeline: GraphTrainerCompileConfig#pass_pipeline.
---
# Module: [`torchtitan/experiments/graph_trainer/configs.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py)

## Classes
### <a id="EpOverlapConfig"></a>`EpOverlapConfig`
- def: [`torchtitan/experiments/graph_trainer/configs.py:32`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L32) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- signature: `class EpOverlapConfig:`
- members:
  - <a id="EpOverlapConfig.chunk_dim"></a>`chunk_dim` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L36) — ---
  - <a id="EpOverlapConfig.disable_early_grad_accumulation"></a>`disable_early_grad_accumulation` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L58) — ---
  - <a id="EpOverlapConfig.enabled"></a>`enabled` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L33) — ---
  - <a id="EpOverlapConfig.module_fqn"></a>`module_fqn` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L50) — ---
  - <a id="EpOverlapConfig.strategy"></a>`strategy` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L43) — ---
- uses (calls/refs, reference-scoped): [`EpOverlapChunkDim`](configs.md#EpOverlapChunkDim), [`TRANSFORMER_BLOCK_FQN`](configs.md#TRANSFORMER_BLOCK_FQN), [`EpOverlapChunkStrategy`](configs.md#EpOverlapChunkStrategy)
- used by: [`compute_config_fingerprint`](precompile.md#compute_config_fingerprint), [`maybe_apply_ep_overlap_eager_chunking`](ep_eager_chunk.md#maybe_apply_ep_overlap_eager_chunking), [`validate_ep_overlap_config`](configs.md#validate_ep_overlap_config), [`ep_overlap`](configs.md#GraphTrainerCompileConfig.ep_overlap), [`trace_input_preparer_keys`](configs.md#trace_input_preparer_keys)  (8 test-only)

### <a id="GraphTrainerCompileConfig"></a>`GraphTrainerCompileConfig`  ·  implements/extends CompileConfig
- def: [`torchtitan/experiments/graph_trainer/configs.py:69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L69) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- signature: `class GraphTrainerCompileConfig(CompileConfig):`
- members:
  - <a id="GraphTrainerCompileConfig.backend"></a>`backend` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L77)
  - <a id="GraphTrainerCompileConfig.cpu_offload_budget_gb"></a>`cpu_offload_budget_gb` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L162) — ---
  - <a id="GraphTrainerCompileConfig.cpu_offload_defer_n_layers"></a>`cpu_offload_defer_n_layers` — [`L158`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L158) — ---
  - <a id="GraphTrainerCompileConfig.cpu_offload_prefetch_n_layers"></a>`cpu_offload_prefetch_n_layers` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L154) — ---
  - <a id="GraphTrainerCompileConfig.debug_graph_passes"></a>`debug_graph_passes` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L110) — ---
  - <a id="GraphTrainerCompileConfig.disable_passes"></a>`disable_passes` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L105) — ---
  - <a id="GraphTrainerCompileConfig.enable_autoparallel"></a>`enable_autoparallel` — [`L194`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L194) — ---
  - <a id="GraphTrainerCompileConfig.enable_fsdp_ag_rs_overlap"></a>`enable_fsdp_ag_rs_overlap` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L166) — ---
  - <a id="GraphTrainerCompileConfig.enable_fsdp_dense_region_overlap"></a>`enable_fsdp_dense_region_overlap` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L172) — ---
  - <a id="GraphTrainerCompileConfig.enable_inplace_graph_gradient_accumulation"></a>`enable_inplace_graph_gradient_accumulation` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L92) — ---
  - <a id="GraphTrainerCompileConfig.enable_passes"></a>`enable_passes` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L85) — ---
  - <a id="GraphTrainerCompileConfig.ep_overlap"></a>`ep_overlap` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L183) — ---
  - <a id="GraphTrainerCompileConfig.full_recompute_save_ops"></a>`full_recompute_save_ops` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L128) — ---
  - <a id="GraphTrainerCompileConfig.inductor_compilation"></a>`inductor_compilation` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L140) — ---
  - <a id="GraphTrainerCompileConfig.memory_policy"></a>`memory_policy` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L113) — ---
  - <a id="GraphTrainerCompileConfig.mode"></a>`mode` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L70) — ---
  - <a id="GraphTrainerCompileConfig.numerics_changing_optim"></a>`numerics_changing_optim` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L150) — ---
  - <a id="GraphTrainerCompileConfig.pass_pipeline"></a>`pass_pipeline` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L136) — ---
  - <a id="GraphTrainerCompileConfig.passes"></a>`passes` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L79) — ---
  - <a id="GraphTrainerCompileConfig.precompile_artifact_dir"></a>`precompile_artifact_dir` — [`L186`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L186) — ---
- uses (calls/refs, reference-scoped): [`CompileConfig`](../../config/configs.md#CompileConfig), [`TpuGraphTrainerCompileConfig`](../tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig), [`EpOverlapConfig`](configs.md#EpOverlapConfig), [`GraphTrainerMemoryPolicy`](configs.md#GraphTrainerMemoryPolicy)
- used by: [`_build_stage_graphs`](graph_pp/graph_builder.md#_build_stage_graphs), [`CompileConfig`](../../config/configs.md#CompileConfig), [`apply_tpu_graph_trainer_model_transforms`](../tpu/graph_trainer/config.md#apply_tpu_graph_trainer_model_transforms), [`graph_pipeline_llm`](graph_pp/pipeline.md#graph_pipeline_llm), [`parallelize_autoparallel_deepseekv3`](deepseek_v3/parallelize_autoparallel.md#parallelize_autoparallel_deepseekv3), [`parallelize_autoparallel_llama`](llama3/parallelize_autoparallel.md#parallelize_autoparallel_llama), [`compute_config_fingerprint`](precompile.md#compute_config_fingerprint), [`construct_tpu_transform_passes`](../tpu/graph_trainer/tpu_backend_pass.md#construct_tpu_transform_passes), [`parallelize_qwen3`](qwen3/parallelize.md#parallelize_qwen3), [`_build_graph_pp_overlap_graphs`](graph_pp/graph_builder.md#_build_graph_pp_overlap_graphs), [`parallelize_deepseekv3`](deepseek_v3/parallelize.md#parallelize_deepseekv3), [`maybe_apply_ep_overlap_eager_chunking`](ep_eager_chunk.md#maybe_apply_ep_overlap_eager_chunking), [`_apply_graph_pp_pre_partition_passes`](graph_pp/graph_builder.md#_apply_graph_pp_pre_partition_passes), [`from_trainer_config`](../tpu/graph_trainer/graph_split.md#GraphSplitter.from_trainer_config), [`apply_compile`](compile.md#apply_compile), [`graph_trainer_deepseek_v3_debugmodel_mxfp8`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_mxfp8), [`apply_graph_passes`](passes.md#apply_graph_passes), [`_compile_stage_graphs`](graph_pp/graph_builder.md#_compile_stage_graphs), [`parallelize_muse_glimmer`](muse_glimmer/parallelize.md#parallelize_muse_glimmer), [`graph_trainer_llama3_debugmodel_sdpa`](llama3/config_registry.md#graph_trainer_llama3_debugmodel_sdpa), [`graph_trainer_llama3_debugmodel_mxfp8`](llama3/config_registry.md#graph_trainer_llama3_debugmodel_mxfp8), [`_compile_graph_pp_module`](graph_pp/graph_builder.md#_compile_graph_pp_module), [`final_inductor_compile_passes`](passes.md#final_inductor_compile_passes), [`TpuGraphTrainerCompileConfig`](../tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig), [`graph_trainer_deepseek_v3_debugmodel_eager_pp`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_eager_pp), [`graph_trainer_llama3_8b_mxfp8`](llama3/config_registry.md#graph_trainer_llama3_8b_mxfp8), [`get_compile_backend_with_passes`](jit_backend.md#get_compile_backend_with_passes), [`_validate_graph_pp_config`](graph_pp/pipeline.md#_validate_graph_pp_config), [`graph_trainer_deepseek_v3_16b`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_16b), [`graph_trainer_deepseek_v3_debugmodel`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel), [`graph_trainer_llama3_8b`](llama3/config_registry.md#graph_trainer_llama3_8b), [`graph_trainer_llama3_debugmodel`](llama3/config_registry.md#graph_trainer_llama3_debugmodel), [`compile`](trainer.md#GraphTrainer.Config.compile), [`graph_trainer_deepseek_v3_16b_minimal_async_ep`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_16b_minimal_async_ep), [`graph_trainer_deepseek_v3_671b`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_671b), [`graph_trainer_deepseek_v3_debugmodel_hybridep`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_hybridep), [`graph_trainer_deepseek_v3_debugmodel_minimal_async_ep`](deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel_minimal_async_ep), [`graph_trainer_llama3_405b`](llama3/config_registry.md#graph_trainer_llama3_405b), [`graph_trainer_llama3_70b`](llama3/config_registry.md#graph_trainer_llama3_70b), [`graph_trainer_llama3_debugmodel_dist_gemm`](llama3/config_registry.md#graph_trainer_llama3_debugmodel_dist_gemm)  (+15 more; 31 test-only)

## Functions
- <a id="to_graph_trainer_config"></a>`to_graph_trainer_config(base_config: Trainer.Config, model_registry: Callable[[str], ModelSpec], target_cls: Any = None)` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L256) — Convert a base Trainer.Config to a GraphTrainer.Config. — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- <a id="trace_input_preparer_keys"></a>`trace_input_preparer_keys(compile_config: GraphTrainerCompileConfig)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L241) — Return feature names whose trace-input hooks should run.
- <a id="validate_autoparallel_config"></a>`validate_autoparallel_config(compile_config: GraphTrainerCompileConfig)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L199)
- <a id="validate_ep_overlap_config"></a>`validate_ep_overlap_config(ep_overlap_config: EpOverlapConfig)` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L209)

## Module values
- <a id="EpOverlapChunkDim"></a>`EpOverlapChunkDim` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L20)
- <a id="EpOverlapChunkStrategy"></a>`EpOverlapChunkStrategy` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L21)
- <a id="GraphTrainerMemoryPolicy"></a>`GraphTrainerMemoryPolicy` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L22)
- <a id="MOE_BLOCK_FQN"></a>`MOE_BLOCK_FQN` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L27)
- <a id="SUPPORTED_EP_OVERLAP_MODULE_FQNS"></a>`SUPPORTED_EP_OVERLAP_MODULE_FQNS` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L28)
- <a id="TRANSFORMER_BLOCK_FQN"></a>`TRANSFORMER_BLOCK_FQN` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/configs.py#L26)

