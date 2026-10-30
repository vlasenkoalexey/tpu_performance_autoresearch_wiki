---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.config`/
symbols:
  apply_tpu_graph_trainer_model_transforms: apply_tpu_graph_trainer_model_transforms().
  _validate_fsdp_allreduce_slice: _validate_fsdp_allreduce_slice().
  TpuGraphTrainerCompileConfig.graph_split: TpuGraphTrainerCompileConfig#graph_split.
  TpuGraphTrainerCompileConfig.memory_policy: TpuGraphTrainerCompileConfig#memory_policy.
  TpuGraphTrainerCompileConfig: TpuGraphTrainerCompileConfig#
  maybe_use_maxtext_flops: maybe_use_maxtext_flops().
  _validate_tpu_selective: _validate_tpu_selective().
  TpuGraphTrainerCompileConfig.fsdp_barrier_policy: TpuGraphTrainerCompileConfig#fsdp_barrier_policy.
  TpuGraphTrainerCompileConfig.use_scan_layers: TpuGraphTrainerCompileConfig#use_scan_layers.
  TpuGraphTrainerCompileConfig.optimizer_compile: TpuGraphTrainerCompileConfig#optimizer_compile.
  TpuGraphTrainerCompileConfig.enable_remat_barriers: TpuGraphTrainerCompileConfig#enable_remat_barriers.
  GraphSplitterConfig.backward_partition_mode: GraphSplitterConfig#backward_partition_mode.
  GraphSplitterConfig.enabled: GraphSplitterConfig#enabled.
  TpuGraphTrainerCompileConfig.save_regions: TpuGraphTrainerCompileConfig#save_regions.
  GraphSplitterConfig.forward_layers_per_executable: GraphSplitterConfig#forward_layers_per_executable.
  TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_parameter_patterns: TpuGraphTrainerCompileConfig#fsdp_allreduce_slice_parameter_patterns.
  GraphSplitterConfig.backward_layers_per_executable: GraphSplitterConfig#backward_layers_per_executable.
  GraphSplitterConfig.cpu_offload_prefetch_executables: GraphSplitterConfig#cpu_offload_prefetch_executables.
  TpuGraphTrainerCompileConfig.save_last_n_layers: TpuGraphTrainerCompileConfig#save_last_n_layers.
  TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_max_input_bytes: TpuGraphTrainerCompileConfig#fsdp_allreduce_slice_max_input_bytes.
  GraphSplitterConfig: GraphSplitterConfig#
  TpuGraphTrainerCompileConfig.compile_grad_norm: TpuGraphTrainerCompileConfig#compile_grad_norm.
  TpuGraphTrainerMemoryPolicy: TpuGraphTrainerMemoryPolicy.
  apply_tpu_graph_trainer_model_transforms.parallelize_fn_with_shard_dims: apply_tpu_graph_trainer_model_transforms().parallelize_fn_with_shard_dims().
  TpuGraphTrainerCompileConfig.fsdp_barrier_prefetch_distance: TpuGraphTrainerCompileConfig#fsdp_barrier_prefetch_distance.
  GraphSplitterConfig.forward_isolate_prefix: GraphSplitterConfig#forward_isolate_prefix.
  GraphSplitterConfig.donate_internal_buffers: GraphSplitterConfig#donate_internal_buffers.
  TpuGraphTrainerCompileConfig.backend: TpuGraphTrainerCompileConfig#backend.
  TpuGraphTrainerCompileConfig.pass_pipeline: TpuGraphTrainerCompileConfig#pass_pipeline.
  GraphTrainerFSDPBarrierPolicy: GraphTrainerFSDPBarrierPolicy.
  BackwardPartitionMode: BackwardPartitionMode.
  TpuGraphTrainerOptimizerCompileMode: TpuGraphTrainerOptimizerCompileMode.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/config.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py)

## Classes
### <a id="GraphSplitterConfig"></a>`GraphSplitterConfig`
- def: [`torchtitan/experiments/tpu/graph_trainer/config.py:58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L58)
- doc: Partition a joint forward/backward trace into TPU executables.
- signature: `class GraphSplitterConfig:`
- members:
  - <a id="GraphSplitterConfig.backward_layers_per_executable"></a>`backward_layers_per_executable` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L97)
  - <a id="GraphSplitterConfig.backward_partition_mode"></a>`backward_partition_mode` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L93)
  - <a id="GraphSplitterConfig.cpu_offload_prefetch_executables"></a>`cpu_offload_prefetch_executables` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L107)
  - <a id="GraphSplitterConfig.donate_internal_buffers"></a>`donate_internal_buffers` — [`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L104)
  - <a id="GraphSplitterConfig.enabled"></a>`enabled` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L83)
  - <a id="GraphSplitterConfig.forward_isolate_prefix"></a>`forward_isolate_prefix` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L88)
  - <a id="GraphSplitterConfig.forward_layers_per_executable"></a>`forward_layers_per_executable` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L86)
- uses (calls/refs, reference-scoped): [`BackwardPartitionMode`](config.md#BackwardPartitionMode)
- used by: [`_qwen3_moe_235b_fsdp_only`](../qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`apply_tpu_graph_trainer_model_transforms`](config.md#apply_tpu_graph_trainer_model_transforms), [`split_and_compile`](graph_split.md#GraphSplitter.split_and_compile), [`from_trainer_config`](graph_split.md#GraphSplitter.from_trainer_config), [`_qwen3_moe_235b_fsdp_activation_offload`](../qwen3/config_registry.md#_qwen3_moe_235b_fsdp_activation_offload), [`graph_split`](config.md#TpuGraphTrainerCompileConfig.graph_split), [`config`](graph_split.md#GraphSplitter.config)  (6 test-only)

### <a id="TpuGraphTrainerCompileConfig"></a>`TpuGraphTrainerCompileConfig`  ·  implements/extends GraphTrainerCompileConfig
- def: [`torchtitan/experiments/tpu/graph_trainer/config.py:111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L111) — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- doc: Compilation and graph-transformation policy for TPU GraphTrainer.
- signature: `class TpuGraphTrainerCompileConfig(GraphTrainerCompileConfig):`
- members:
  - <a id="TpuGraphTrainerCompileConfig.backend"></a>`backend` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L120)
  - <a id="TpuGraphTrainerCompileConfig.compile_grad_norm"></a>`compile_grad_norm` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L138)
  - <a id="TpuGraphTrainerCompileConfig.enable_remat_barriers"></a>`enable_remat_barriers` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L151)
  - <a id="TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_max_input_bytes"></a>`fsdp_allreduce_slice_max_input_bytes` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L165)
  - <a id="TpuGraphTrainerCompileConfig.fsdp_allreduce_slice_parameter_patterns"></a>`fsdp_allreduce_slice_parameter_patterns` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L164)
  - <a id="TpuGraphTrainerCompileConfig.fsdp_barrier_policy"></a>`fsdp_barrier_policy` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L158)
  - <a id="TpuGraphTrainerCompileConfig.fsdp_barrier_prefetch_distance"></a>`fsdp_barrier_prefetch_distance` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L160)
  - <a id="TpuGraphTrainerCompileConfig.graph_split"></a>`graph_split` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L161)
  - <a id="TpuGraphTrainerCompileConfig.memory_policy"></a>`memory_policy` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L122)
  - <a id="TpuGraphTrainerCompileConfig.optimizer_compile"></a>`optimizer_compile` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L136)
  - <a id="TpuGraphTrainerCompileConfig.pass_pipeline"></a>`pass_pipeline` — [`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L121)
  - <a id="TpuGraphTrainerCompileConfig.save_last_n_layers"></a>`save_last_n_layers` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L133)
  - <a id="TpuGraphTrainerCompileConfig.save_regions"></a>`save_regions` — [`L127`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L127)
  - <a id="TpuGraphTrainerCompileConfig.use_scan_layers"></a>`use_scan_layers` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L143)
- uses (calls/refs, reference-scoped): [`GraphTrainerCompileConfig`](../../graph_trainer/configs.md#GraphTrainerCompileConfig), [`GraphSplitterConfig`](config.md#GraphSplitterConfig), [`TpuGraphTrainerMemoryPolicy`](config.md#TpuGraphTrainerMemoryPolicy), [`GraphTrainerFSDPBarrierPolicy`](config.md#GraphTrainerFSDPBarrierPolicy), [`TpuGraphTrainerOptimizerCompileMode`](config.md#TpuGraphTrainerOptimizerCompileMode)
- used by: [`qwen3_8b`](../qwen3/config_registry.md#qwen3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](../qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`qwen3_moe_30b`](../qwen3/config_registry.md#qwen3_moe_30b), [`compile`](tpu_graph_trainer.md#TpuGraphTrainer.Config.compile), [`qwen3_moe_235b_scan`](../qwen3/config_registry.md#qwen3_moe_235b_scan), [`_qwen3_moe_235b_fsdp_only`](../qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`GraphTrainerCompileConfig`](../../graph_trainer/configs.md#GraphTrainerCompileConfig), [`start_trainer`](../train.md#start_trainer), [`apply_tpu_graph_trainer_model_transforms`](config.md#apply_tpu_graph_trainer_model_transforms), [`qwen3_32b`](../qwen3/config_registry.md#qwen3_32b), [`muse_glimmer_30b_full_logits`](../muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits), [`_on_scan_lane`](../llama3/config_registry.md#_on_scan_lane), [`from_trainer_config`](graph_split.md#GraphSplitter.from_trainer_config), [`_qwen3_moe_235b_fsdp_activation_offload`](../qwen3/config_registry.md#_qwen3_moe_235b_fsdp_activation_offload), [`qwen3_8b_zero3`](../qwen3/config_registry.md#qwen3_8b_zero3), [`_validate_fsdp_allreduce_slice`](config.md#_validate_fsdp_allreduce_slice), [`graph_trainer_qwen3_debugmodel`](../qwen3/config_registry.md#graph_trainer_qwen3_debugmodel), [`qwen3_32b_4x8x8`](../qwen3/config_registry.md#qwen3_32b_4x8x8), [`graph_trainer_deepseek_v3_debugmodel`](../deepseek_v3/config_registry.md#graph_trainer_deepseek_v3_debugmodel), [`graph_trainer_llama3_debugmodel`](../llama3/config_registry.md#graph_trainer_llama3_debugmodel), [`graph_trainer_muse_glimmer_debugmodel`](../muse_glimmer/config_registry.md#graph_trainer_muse_glimmer_debugmodel), [`_validate_tpu_selective`](config.md#_validate_tpu_selective), [`_compiled_grad_norm`](tpu_graph_trainer.md#TpuGraphTrainer._compiled_grad_norm), [`muse_glimmer_30b_fused_ce`](../muse_glimmer/config_registry.md#muse_glimmer_30b_fused_ce), [`__post_init__`](tpu_graph_trainer.md#TpuGraphTrainer.Config.__post_init__), [`_without_splash_saves`](../qwen3/config_registry.md#_without_splash_saves), [`_optimizer_in_graph`](tpu_graph_trainer.md#TpuGraphTrainer._optimizer_in_graph), [`_optimizer_separate_graph`](tpu_graph_trainer.md#TpuGraphTrainer._optimizer_separate_graph)  (29 test-only)

## Functions
- <a id="_validate_fsdp_allreduce_slice"></a>`_validate_fsdp_allreduce_slice(config: TpuGraphTrainer.Config)` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L168)
- <a id="_validate_tpu_selective"></a>`_validate_tpu_selective(config: TpuGraphTrainer.Config)` — [`L195`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L195)
- <a id="apply_tpu_graph_trainer_model_transforms"></a>`apply_tpu_graph_trainer_model_transforms(config: TpuGraphTrainer.Config)` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L244) — Validate TPU graph options and apply CLI-selected model transforms. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="maybe_use_maxtext_flops"></a>`maybe_use_maxtext_flops(train_config: TPUTrainerConfig, graph_config: TpuGraphTrainer.Config)` — [`L219`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L219) — Carry a recipe's MaxText FLOP accounting into its GraphTrainer config.
- <a id="apply_tpu_graph_trainer_model_transforms.parallelize_fn_with_shard_dims"></a>`parallelize_fn_with_shard_dims(model: nn.Module, **kwargs: Any)` — [`L345`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L345)

## Module values
- <a id="BackwardPartitionMode"></a>`BackwardPartitionMode` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L41)
- <a id="GraphTrainerFSDPBarrierPolicy"></a>`GraphTrainerFSDPBarrierPolicy` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L40)
- <a id="TpuGraphTrainerMemoryPolicy"></a>`TpuGraphTrainerMemoryPolicy` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L48)
- <a id="TpuGraphTrainerOptimizerCompileMode"></a>`TpuGraphTrainerOptimizerCompileMode` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L43)
- <a id="__all__"></a>`__all__` — [`L364`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/config.py#L364)

