---
slug: torchtitan
repo: raw/code/torchtitan
acquire: submodule
# google-pytorch/torchtitan main HEAD (2026-10-28): the TorchTitan fork with the TorchTPU backend
# (torchtitan/experiments/tpu); upstream pytorch/torchtitan has no TPU backend.
ref: 2ad96c9390ea7206a154b1cade409b589ef6d9e7
wiki_subdir: codebases
source_type: code
languages: [python]
index_shards: ["torchtitan/*"]
catalog: full   # per-module catalog pages, like the other silos in this wiki (citations link to them)
agenda: subsystems
# experiments/ is on wikify's default discovery exclude list; the TPU backend and the other lanes are
# pinned explicitly under ## Concepts. The top-level torchtitan/models unit (registry glue) is dropped.
agenda_exclude:
  - torchtitan/models
  - torchtitan
coverage_collapse: ["tests/**", "**/test_*.py", "**/*_test.py", "benchmarks/**"]
docs:
  - README.md
  - torchtitan/**/README.md
  - torchtitan/experiments/tpu/*.md
  - torchtitan/components/quantization/*.md
  - torchtitan/models/**/*.md
  - torchtitan/observability/*.md
  - torchtitan/experiments/rl/docs/*.md
  - torchtitan/experiments/graph_trainer/MANIFESTO.md
synthesis_focus: "TPU performance - how a job config selects a model spec and builds the device mesh, how each parallelism axis (FSDP, TP, PP, CP, EP) is applied and composed, activation checkpointing and torch.compile integration, attention/kernel backends, MoE dispatch, precision and quantization, and the experiments/tpu backend that retunes strategy for TorchTPU (and the jax/torchax lanes)"
---

## Concepts
<!-- Discovery-driven: the subsystem planner proposes the units; entries here pin, rename and add. -->
- **trainer-and-train-loop** - seeds: `Trainer::__init__`, `Trainer::train`, `Trainer::train_step`, `Trainer::forward_backward_step`, `Trainer::init_distributed`, `Trainer::_clip_grad_norm`, `_maybe_enable_min_cost_redistribute`, `ConfigManager::parse_args`
- **model-building-blocks** - seeds: (subsystem: torchtitan/models/common)
- **model-spec-protocols** - seeds: (subsystem: torchtitan/protocols)
- **job-config** - seeds: (subsystem: torchtitan/config)
- **parallel-dims-and-parallelization** - seeds: (subsystem: torchtitan/distributed)
- **flex-shard** - seeds: (subsystem: torchtitan/distributed/flex_shard)
- **training-components** - seeds: (subsystem: torchtitan/components)
- **data-loading** - seeds: (subsystem: torchtitan/components/data)
- **checkpointing** - seeds: (subsystem: torchtitan/components/checkpointer)
- **optimizers-and-lr-schedulers** - seeds: (subsystem: torchtitan/components/optimizer)
- **quantization** - seeds: (subsystem: torchtitan/components/quantization)
- **hf-datasets** - seeds: (subsystem: torchtitan/hf_datasets)
- **observability** - seeds: (subsystem: torchtitan/observability)
- **debug-and-profiling-tools** - seeds: (subsystem: torchtitan/tools)
- **config-overrides** - seeds: (subsystem: torchtitan/overrides)
- **llama3-model** - seeds: (subsystem: torchtitan/models/llama3)
- **qwen3-model** - seeds: (subsystem: torchtitan/models/qwen3)
- **qwen3-5-model** - seeds: (subsystem: torchtitan/models/qwen3_5)
- **deepseek-v3-model** - seeds: (subsystem: torchtitan/models/deepseek_v3)
- **deepseek-v4-model** - seeds: (subsystem: torchtitan/models/deepseek_v4)
- **kimi-k2-7-model** - seeds: (subsystem: torchtitan/models/kimi_k2_7)
- **kimi-k3-model** - seeds: (subsystem: torchtitan/models/kimi_k3)
- **gpt-oss-model** - seeds: (subsystem: torchtitan/models/gpt_oss)
- **muse-glimmer-model** - seeds: (subsystem: torchtitan/models/muse_glimmer)
- **flux-diffusion-model** - seeds: (subsystem: torchtitan/models/flux)
- **tpu-trainer-and-job-config** - seeds: `TPUTrainer`, `start_trainer`, `TPUConfig`, `TpuTrainerCompileConfig`, `SplashAttentionKernelConfig`, `LossKernelConfig`, `BaseTPUTrainerConfig`, `TPUTrainerConfig`, `run_distributed`, `cpu_only_env`, `FlagMap`, `merge_flags`, `parse_flags`, `resolve_flags`, `apply_init_flags`, `apply_patches`, `use_splash_attention_patch`, `use_tokamax_splash_attention_patch`, `PallasLossLinear`, `use_gmm_kernel_patch`, `get_maxtext_decoder_nparams_and_flops`
- **tpu-moe-dispatch-and-grouped-experts** - seeds: `TpuAllToAllTokenDispatcher`, `TpuRoutedExperts`, `TpuRoutedExpertsConverter`, `TpuTokenDispatcherConverter`, `scale_route_weights`, `stable_grouped_reduce`, `local_reorder`, `TpuGroupedExperts`, `TpuGroupedExpertsConverter`
- **tpu-context-parallel-attention** - seeds: `UlyssesCPInnerAttention`, `KVAllGatherCPInnerAttention`, `reorder_sequence`, `headtail_chunk_order`, `headtail_positions`, `make_headtail_splash_mask`, `make_cp_segment_ids`, `slice_cp_mask_info`
- **tpu-layer-loop-remat-and-layouts** - seeds: `TpuLayerLoop`, `runs_layer_loop`, `builds_layer_loop`, `annotate_region`, `TPUSelectiveAC`, `tpu_selective_ac_config`, `AttentionSavingSelectiveAC`, `apply_scan_reverse_backward_patch`, `apply_bld_layout`, `bld_skip_reason`, `TpuPackedQKVLinear`, `TpuPackedQKVConverter`, `configure_qwen_simple_fsdp_shard_dims`
- **tpu-pallas-kernels** - seeds: `SplashAttention`, `SplashAttentionKernel`, `SplashConfig`, `TokamaxConfig`, `SbdConfig`, `MaskInfo`, `ChunkedCausalMask`, `flash_attention_kernel`, `TorchGMM`, `grouped_matrix_multiply`, `fp8_gmm_fwd`, `fp8_gmm_bwd`, `fp8_segment_matmul_pallas_2d`, `TorchLinearLoss`, `linear_softmax_cross_entropy_loss`, `get_heuristic_fwd_config`, `get_heuristic_bwd_config`, `fill_indices`
- **tpu-graph-trainer** - seeds: `TpuGraphTrainer`, `TpuGraphTrainerCompileConfig`, `GraphSplitter`, `SplitForwardBackwardGraph`, `LayerStack`, `StackedLayers`, `ScanFSDPSpec`, `TpuReplicateComputation`, `construct_tpu_pass_pipeline`, `construct_tpu_transform_passes`, `apply_tpu_remat_schedule`, `apply_tpu_fsdp_rs_deadline_schedule`, `apply_tpu_remat_fsdp_all_gather_schedule`, `apply_combine_barrier_pass`, `offload_scan_activations`, `check_scan_was_applied`, `full_remat_with_saves`, `MfuBenchmark`
- **jax-lane** - seeds: `JaxTrainer`, `JaxJobConfig`, `JaxConfig`, `JaxMetricsProcessor`, `ScannedTransformerBlocks`, `build_splash_attention_callable`, `make_splash_attention_fn`, `apply_sharding_to_state`, `shard_input`, `sharded_device_put`, `torch_loader_to_jax`, `main_train_loop`
- **graph-trainer** - seeds: `GraphTrainer`, `GraphTrainerCompileConfig`, `CompiledModule`, `GraphRunner`, `AutoParallelGraph`, `GraphPipelineRuntime`, `GraphPipelineStage`, `JointManualOverlapScheduler`, `FSDPParamOrderBucketer`, `ChunkedLossWrapperWithParamGrads`, `PrecompiledFxTraceArtifact`, `ReplicateComputation`, `EpOverlapConfig`
- **rl-training** - seeds: `PolicyTrainer`, `Controller`, `GRPOLoss`, `DAPOLoss`, `AdvantageEstimator`, `Rollout`, `RolloutGroup`, `RequestDispatcher`, `AsyncLoopConfig`, `InferenceParallelismConfig`, `GenerationRequest`, `PerHostProvisioner`
