---
title: 'Module map: torchtitan'
type: catalog-map
provenance: extracted
---
# Module map: torchtitan @ 2ad96c9390

690 modules, 14209 documentable symbols, 14209 index rows (overloads share a row), 44898 caller edges. The index is tab-separated; grep it by anchor, never read a file whole. Columns: anchor, path, line, kind, rank, hash, callers, citing pages, then signature and doc line in the full profile. Hubs have hundreds of callers and a search tool shows about 50 lines: count first, narrow by directory, end every listing with `head`.

```
grep -P '^<path>#<Name>\t' catalog/symbols/*.tsv                            # one symbol's row
grep -P '[#.]<Name>\t' catalog/symbols/*.tsv | sort -t$'\t' -k5 -nr | head -20   # by bare name, best first
grep -P '^<dir>/.*#<Name>\t' catalog/symbols/*.tsv | head -20                    # a name within an area
awk -F'\t' '$2=="<path>"' catalog/symbols/*.tsv | cut -f1,3,4 | head -40         # everything a module defines
grep -c -P '^<path>#<Name>\t' catalog/edges/*.tsv                         # how many callers (count first)
grep -P '^<path>#<Name>\t' catalog/edges/*.tsv | cut -f2 | cut -d/ -f1-2 | sort | uniq -c   # callers by directory
grep -P '^<path>#<Name>\t<dir>/' catalog/edges/*.tsv | cut -f2 | head -20      # callers in one directory
grep -P '\t<path>#<Name>$' catalog/edges/*.tsv | cut -f1 | head -20           # what it calls
```

## Index files

| Shard | Symbols | Edges |
|---|---|---|
| `scripts` | [`symbols/scripts.tsv`](symbols/scripts.tsv) — 36 rows | [`edges/scripts.tsv`](edges/scripts.tsv) — 63 edges |
| `tests` | [`symbols/tests.tsv`](symbols/tests.tsv) — 4 rows | [`edges/tests.tsv`](edges/tests.tsv) — 7 edges |
| `tests/integration_tests` | [`symbols/tests-integration_tests.tsv`](symbols/tests-integration_tests.tsv) — 41 rows | [`edges/tests-integration_tests.tsv`](edges/tests-integration_tests.tsv) — 150 edges |
| `torchtitan` | [`symbols/torchtitan.tsv`](symbols/torchtitan.tsv) — 71 rows | [`edges/torchtitan.tsv`](edges/torchtitan.tsv) — 2422 edges |
| `torchtitan/components` | [`symbols/torchtitan-components.tsv`](symbols/torchtitan-components.tsv) — 774 rows | [`edges/torchtitan-components.tsv`](edges/torchtitan-components.tsv) — 4249 edges |
| `torchtitan/config` | [`symbols/torchtitan-config.tsv`](symbols/torchtitan-config.tsv) — 147 rows | [`edges/torchtitan-config.tsv`](edges/torchtitan-config.tsv) — 2994 edges |
| `torchtitan/distributed` | [`symbols/torchtitan-distributed.tsv`](symbols/torchtitan-distributed.tsv) — 680 rows | [`edges/torchtitan-distributed.tsv`](edges/torchtitan-distributed.tsv) — 2751 edges |
| `torchtitan/experiments` | [`symbols/torchtitan-experiments.tsv`](symbols/torchtitan-experiments.tsv) — 9081 rows | [`edges/torchtitan-experiments.tsv`](edges/torchtitan-experiments.tsv) — 19147 edges |
| `torchtitan/hf_datasets` | [`symbols/torchtitan-hf_datasets.tsv`](symbols/torchtitan-hf_datasets.tsv) — 89 rows | [`edges/torchtitan-hf_datasets.tsv`](edges/torchtitan-hf_datasets.tsv) — 244 edges |
| `torchtitan/models` | [`symbols/torchtitan-models.tsv`](symbols/torchtitan-models.tsv) — 2682 rows | [`edges/torchtitan-models.tsv`](edges/torchtitan-models.tsv) — 9586 edges |
| `torchtitan/observability` | [`symbols/torchtitan-observability.tsv`](symbols/torchtitan-observability.tsv) — 149 rows | [`edges/torchtitan-observability.tsv`](edges/torchtitan-observability.tsv) — 316 edges |
| `torchtitan/ops` | [`symbols/torchtitan-ops.tsv`](symbols/torchtitan-ops.tsv) — 3 rows | [`edges/torchtitan-ops.tsv`](edges/torchtitan-ops.tsv) — 3 edges |
| `torchtitan/overrides` | [`symbols/torchtitan-overrides.tsv`](symbols/torchtitan-overrides.tsv) — 142 rows | [`edges/torchtitan-overrides.tsv`](edges/torchtitan-overrides.tsv) — 158 edges |
| `torchtitan/protocols` | [`symbols/torchtitan-protocols.tsv`](symbols/torchtitan-protocols.tsv) — 85 rows | [`edges/torchtitan-protocols.tsv`](edges/torchtitan-protocols.tsv) — 2006 edges |
| `torchtitan/tools` | [`symbols/torchtitan-tools.tsv`](symbols/torchtitan-tools.tsv) — 123 rows | [`edges/torchtitan-tools.tsv`](edges/torchtitan-tools.tsv) — 682 edges |
| `torchtitan_recipes/tests` | [`symbols/torchtitan_recipes-tests.tsv`](symbols/torchtitan_recipes-tests.tsv) — 102 rows | [`edges/torchtitan_recipes-tests.tsv`](edges/torchtitan_recipes-tests.tsv) — 120 edges |

Below, one row per module: entry points are the symbols with the most callers; *cited by* lists the concept pages that cite into the module.

## `scripts`

Index: [`symbols/scripts.tsv`](symbols/scripts.tsv) (36 rows), [`edges/scripts.tsv`](edges/scripts.tsv) (63 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`scripts/loss_compare.py`](scripts/loss_compare.md) | 36 | `log_print`, `LOG_PREFIX`, `log_and_save` |  |

## `tests`

Index: [`symbols/tests.tsv`](symbols/tests.tsv) (4 rows), [`edges/tests.tsv`](edges/tests.tsv) (7 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`tests/utils.py`](tests/utils.md) | 4 | `hash_gradient`, `hash_model`, `_hash_model_impl` |  |

## `tests/integration_tests`

Index: [`symbols/tests-integration_tests.tsv`](symbols/tests-integration_tests.tsv) (41 rows), [`edges/tests-integration_tests.tsv`](edges/tests-integration_tests.tsv) (150 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`tests/integration_tests/__init__.py`](tests/integration_tests/__init__.md) | 15 | `OverrideDefinitions`, `ngpu`, `test_name` |  |
| [`tests/integration_tests/b200.py`](tests/integration_tests/b200.md) | 1 | `build_b200_tests_list` |  |
| [`tests/integration_tests/features.py`](tests/integration_tests/features.md) | 1 | `build_features_test_list` |  |
| [`tests/integration_tests/h100.py`](tests/integration_tests/h100.md) | 1 | `build_h100_tests_list` |  |
| [`tests/integration_tests/models.py`](tests/integration_tests/models.md) | 1 | `build_model_tests_list` |  |
| [`tests/integration_tests/run_tests.py`](tests/integration_tests/run_tests.md) | 22 | `run_tests`, `run_single_test`, `_TEST_SUITES_FUNCTION` |  |

## `torchtitan`

Index: [`symbols/torchtitan.tsv`](symbols/torchtitan.tsv) (71 rows), [`edges/torchtitan.tsv`](edges/torchtitan.tsv) (2422 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/__init__.py`](torchtitan/__init__.md) | 1 | `__version__` |  |
| [`torchtitan/train.py`](torchtitan/train.md) | 2 | `_maybe_enable_min_cost_redistribute`, `main` | [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/trainer.py`](torchtitan/trainer.md) | 68 | `parallelism`, `training`, `Trainer` | [checkpointing](../concepts/checkpointing.md), [job-config](../concepts/job-config.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |

## `torchtitan/components`

Index: [`symbols/torchtitan-components.tsv`](symbols/torchtitan-components.tsv) (774 rows), [`edges/torchtitan-components.tsv`](edges/torchtitan-components.tsv) (4249 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/components/checkpointer/__init__.py`](torchtitan/components/checkpointer/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/components/checkpointer/base.py`](torchtitan/components/checkpointer/base.md) | 79 | `interval`, `last_save_model_only`, `enable` | [checkpointing](../concepts/checkpointing.md) |
| [`torchtitan/components/checkpointer/dcp.py`](torchtitan/components/checkpointer/dcp.md) | 36 | `CheckpointManager`, `Config`, `AsyncMode` | [checkpointing](../concepts/checkpointing.md) |
| [`torchtitan/components/checkpointer/torch_checkpointing.py`](torchtitan/components/checkpointer/torch_checkpointing.md) | 40 | `_manager_config`, `_manager`, `_storage` | [checkpointing](../concepts/checkpointing.md), [training-components](../concepts/training-components.md) |
| [`torchtitan/components/checkpointer/utils.py`](torchtitan/components/checkpointer/utils.md) | 3 | `canonical_fqn`, `_WRAPPER_PREFIXES`, `__all__` |  |
| [`torchtitan/components/data/__init__.py`](torchtitan/components/data/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/components/data/collators.py`](torchtitan/components/data/collators.md) | 12 | `TrainerBatch`, `Collator`, `Config` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/data/dataset.py`](torchtitan/components/data/dataset.md) | 29 | `processor`, `SingleDatasetConfig`, `source` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/data/loader.py`](torchtitan/components/data/loader.md) | 26 | `GrainDataLoader`, `Config`, `dataset` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/data/packing.py`](torchtitan/components/data/packing.md) | 35 | `dataset`, `ConcatThenSplitPackingConfig`, `dataset` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/data/sources.py`](torchtitan/components/data/sources.md) | 52 | `HuggingFaceRandomAccessSource`, `Config`, `path` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/data/types.py`](torchtitan/components/data/types.md) | 13 | `DatasetBuildContext`, `DatasetIterationPolicy`, `tokenizer` | [data-loading](../concepts/data-loading.md) |
| [`torchtitan/components/lora.py`](torchtitan/components/lora.md) | 29 | `Config`, `LoRAConverter`, `rank` |  |
| [`torchtitan/components/loss.py`](torchtitan/components/loss.md) | 53 | `CrossEntropyLoss`, `Config`, `ChunkedLossWrapper` | [graph-trainer](../concepts/graph-trainer.md), [training-components](../concepts/training-components.md) |
| [`torchtitan/components/metrics.py`](torchtitan/components/metrics.md) | 67 | `MetricsProcessor`, `Config`, `log_freq` | [training-components](../concepts/training-components.md) |
| [`torchtitan/components/optimizer/__init__.py`](torchtitan/components/optimizer/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/components/optimizer/lr_scheduler.py`](torchtitan/components/optimizer/lr_scheduler.md) | 18 | `LRSchedulersContainer`, `warmup_steps`, `Config` | [jax-lane](../concepts/jax-lane.md), [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md) |
| [`torchtitan/components/optimizer/optimizer.py`](torchtitan/components/optimizer/optimizer.md) | 47 | `default_adamw`, `OptimizersContainer`, `implementation` | [flex-shard](../concepts/flex-shard.md), [llama3-model](../concepts/llama3-model.md), [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md) |
| [`torchtitan/components/optimizer/utils.py`](torchtitan/components/optimizer/utils.md) | 8 | `init_optim_state`, `get_flat_optim_state_dict`, `_flatten_state_nested` | [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md) |
| [`torchtitan/components/quantization/__init__.py`](torchtitan/components/quantization/__init__.md) | 4 | `model_compile_enabled`, `QuantizationConverter`, `Config` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/_fsdp_tensor.py`](torchtitan/components/quantization/_fsdp_tensor.md) | 30 | `_UnshardedFSDPTensor`, `_operands`, `_ShardedFSDPTensor` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/float8.py`](torchtitan/components/quantization/float8.md) | 28 | `Float8LinearConverter`, `filter_fqns`, `Float8Linear` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/mxfp8/__init__.py`](torchtitan/components/quantization/mxfp8/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/components/quantization/mxfp8/converter.py`](torchtitan/components/quantization/mxfp8/converter.md) | 26 | `MXFP8LinearConverter`, `Config`, `MXFP8GroupedExpertsConverter` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/mxfp8/linear.py`](torchtitan/components/quantization/mxfp8/linear.md) | 17 | `MXFP8Linear`, `Config`, `input_activation_format_for_backward` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/mxfp8/tensor.py`](torchtitan/components/quantization/mxfp8/tensor.md) | 10 | `_MXFP8_BLOCK_SIZE`, `weight_qdata_dgrad_NK`, `_LinearShardedTensorWithMXFP8Compute` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/nvfp4.py`](torchtitan/components/quantization/nvfp4.md) | 24 | `NVFP4LinearConverter`, `Config`, `fqns` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/quantization/utils.py`](torchtitan/components/quantization/utils.md) | 3 | `swap_token_dispatcher`, `module_filter_fn`, `has_quantization` | [quantization](../concepts/quantization.md) |
| [`torchtitan/components/tokenizer.py`](torchtitan/components/tokenizer.md) | 49 | `HuggingFaceTokenizer`, `MultiModalTokenizer`, `Config` | [training-components](../concepts/training-components.md) |
| [`torchtitan/components/validate.py`](torchtitan/components/validate.md) | 32 | `Validator`, `Config`, `steps` | [training-components](../concepts/training-components.md) |

## `torchtitan/config`

Index: [`symbols/torchtitan-config.tsv`](symbols/torchtitan-config.tsv) (147 rows), [`edges/torchtitan-config.tsv`](edges/torchtitan-config.tsv) (2994 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/config/__init__.py`](torchtitan/config/__init__.md) | 2 | `TORCH_DTYPE_MAP`, `__all__` | [job-config](../concepts/job-config.md) |
| [`torchtitan/config/configs.py`](torchtitan/config/configs.md) | 62 | `ParallelismConfig`, `num_tokens_per_microbatch_per_dp_rank`, `max_context_length` | [flux-diffusion-model](../concepts/flux-diffusion-model.md), [job-config](../concepts/job-config.md) |
| [`torchtitan/config/configurable.py`](torchtitan/config/configurable.md) | 10 | `build`, `Configurable`, `Config` | [config-overrides](../concepts/config-overrides.md), [job-config](../concepts/job-config.md) |
| [`torchtitan/config/function.py`](torchtitan/config/function.md) | 7 | `Function`, `R`, `Config` |  |
| [`torchtitan/config/manager.py`](torchtitan/config/manager.md) | 15 | `ConfigManager`, `parse_args`, `custom_registry` | [job-config](../concepts/job-config.md) |
| [`torchtitan/config/override.py`](torchtitan/config/override.md) | 32 | `imports`, `derive`, `apply_overrides` | [job-config](../concepts/job-config.md) |
| [`torchtitan/config/transform/__init__.py`](torchtitan/config/transform/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/config/transform/apply.py`](torchtitan/config/transform/apply.md) | 5 | `apply_transforms`, `transform_model_config_`, `_ordered` | [job-config](../concepts/job-config.md) |
| [`torchtitan/config/transform/base.py`](torchtitan/config/transform/base.md) | 6 | `ModelConfigTransform`, `transform`, `convert_config_type` |  |
| [`torchtitan/config/transform/context_parallel.py`](torchtitan/config/transform/context_parallel.md) | 5 | `inner_attention`, `ContextParallelTransform`, `transform` | [job-config](../concepts/job-config.md) |
| [`torchtitan/config/validation.py`](torchtitan/config/validation.md) | 2 | `validate_context_parallel`, `__all__` | [job-config](../concepts/job-config.md) |

## `torchtitan/distributed`

Index: [`symbols/torchtitan-distributed.tsv`](symbols/torchtitan-distributed.tsv) (680 rows), [`edges/torchtitan-distributed.tsv`](edges/torchtitan-distributed.tsv) (2751 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/distributed/__init__.py`](torchtitan/distributed/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/distributed/activation_checkpoint.py`](torchtitan/distributed/activation_checkpoint.md) | 37 | `SelectiveAC`, `Config`, `FullAC` | [graph-trainer](../concepts/graph-trainer.md), [jax-lane](../concepts/jax-lane.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/compile.py`](torchtitan/distributed/compile.md) | 5 | `apply_compile`, `_maybe_enable_async_tp`, `_maybe_regional_inductor_backend` | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/context_parallel/__init__.py`](torchtitan/distributed/context_parallel/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/distributed/context_parallel/api.py`](torchtitan/distributed/context_parallel/api.md) | 3 | `prepare_context_parallel_input`, `cp_shard`, `_cp_shard_dims` |  |
| [`torchtitan/distributed/cudagraph.py`](torchtitan/distributed/cudagraph.md) | 49 | `CUDAGraphWrapper`, `cudagraph_teardown`, `_manager` |  |
| [`torchtitan/distributed/deepep/deepep.py`](torchtitan/distributed/deepep/deepep.md) | 29 | `_buffer`, `_handle_cache`, `_lib` |  |
| [`torchtitan/distributed/deepep/hybridep.py`](torchtitan/distributed/deepep/hybridep.md) | 30 | `DispatchHandle`, `_buffer`, `value` |  |
| [`torchtitan/distributed/flex_shard/__init__.py`](torchtitan/distributed/flex_shard/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.py`](torchtitan/distributed/flex_shard/_optimizer_reshard_runtime.md) | 62 | `_BucketWork`, `_BufferSlot`, `buffers` | [flex-shard](../concepts/flex-shard.md) |
| [`torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.py`](torchtitan/distributed/flex_shard/_optimizer_reshard_schedule.md) | 102 | `_ItemT`, `_TensorRegion`, `shape` | [flex-shard](../concepts/flex-shard.md) |
| [`torchtitan/distributed/flex_shard/dist_muon.py`](torchtitan/distributed/flex_shard/dist_muon.md) | 99 | `_ParameterComputeLayout`, `param`, `storage_is_compute_ready` | [flex-shard](../concepts/flex-shard.md) |
| [`torchtitan/distributed/flex_shard/optimizer_reshard.py`](torchtitan/distributed/flex_shard/optimizer_reshard.md) | 37 | `ComputeLayout`, `BlockShard`, `dim` | [flex-shard](../concepts/flex-shard.md) |
| [`torchtitan/distributed/fsdp.py`](torchtitan/distributed/fsdp.md) | 11 | `resolve_fsdp_mesh`, `apply_fsdp_to_decoder`, `resolve_sparse_fsdp_mesh` | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/linear.py`](torchtitan/distributed/linear.md) | 13 | `LinearReduceScatter`, `ensure_symm_mem_ops`, `AllGatherLinear` |  |
| [`torchtitan/distributed/minimal_async_ep/__init__.py`](torchtitan/distributed/minimal_async_ep/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/distributed/minimal_async_ep/api.py`](torchtitan/distributed/minimal_async_ep/api.md) | 52 | `_buffer_state`, `group`, `_copy_rows_to_peers_and_wait_cuda` | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/minimal_async_ep/kernels.py`](torchtitan/distributed/minimal_async_ep/kernels.md) | 20 | `_MAX_BLOCK_N`, `reduce_topk_slots_kernel`, `_COUNT_COPY_BLOCK_SIZE` |  |
| [`torchtitan/distributed/parallel_dims.py`](torchtitan/distributed/parallel_dims.md) | 56 | `ParallelDims`, `MeshAxisName`, `get_mesh` | [config-overrides](../concepts/config-overrides.md), [flux-diffusion-model](../concepts/flux-diffusion-model.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/pipeline_parallel.py`](torchtitan/distributed/pipeline_parallel.md) | 12 | `pipeline_llm`, `pipeline_with_first_stage_modules`, `_generate_llm_fqn_per_model_part` | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/spmd_types.py`](torchtitan/distributed/spmd_types.md) | 23 | `current_spmd_mesh`, `spmd_mesh_size`, `annotate_input_spmd_types` | [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |
| [`torchtitan/distributed/tensor_parallel.py`](torchtitan/distributed/tensor_parallel.md) | 9 | `_prepare_input_fn`, `_prepare_output_fn`, `desired_input_layout` |  |
| [`torchtitan/distributed/utils.py`](torchtitan/distributed/utils.md) | 27 | `get_spmd_backend`, `get_spmd_context`, `is_in_batch_invariant_mode` | [config-overrides](../concepts/config-overrides.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) |

## `torchtitan/experiments`

Index: [`symbols/torchtitan-experiments.tsv`](symbols/torchtitan-experiments.tsv) (9081 rows), [`edges/torchtitan-experiments.tsv`](edges/torchtitan-experiments.tsv) (19147 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/experiments/__init__.py`](torchtitan/experiments/__init__.md) | 1 | `_supported_experiments` |  |
| [`torchtitan/experiments/graph_trainer/autoparallel_api.py`](torchtitan/experiments/graph_trainer/autoparallel_api.md) | 11 | `AutoParallelModelOutput`, `AutoParallelGraph`, `output_mesh` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/chunked_loss.py`](torchtitan/experiments/graph_trainer/chunked_loss.md) | 6 | `ChunkedLossWrapperWithParamGrads`, `Config`, `_gradient_backprop` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/common_utils.py`](torchtitan/experiments/graph_trainer/common_utils.md) | 39 | `_MODULE_FQN`, `_is_backward_node`, `_get_layer_id` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/compile.py`](torchtitan/experiments/graph_trainer/compile.md) | 2 | `apply_compile`, `_apply_jit_compile` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/configs.py`](torchtitan/experiments/graph_trainer/configs.md) | 37 | `GraphTrainerCompileConfig`, `to_graph_trainer_config`, `mode` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/cpu_offload.py`](torchtitan/experiments/graph_trainer/cpu_offload.md) | 29 | `tag_all_offloadable_activations`, `apply_cpu_offload_pass`, `_is_view` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/cudagraph.py`](torchtitan/experiments/graph_trainer/cudagraph.md) | 11 | `cudagraph_pass`, `insert_kernel_annotations_pass`, `is_cudagraphable` |  |
| [`torchtitan/experiments/graph_trainer/custom_codegen.py`](torchtitan/experiments/graph_trainer/custom_codegen.md) | 33 | `_code_path`, `_CodegenGraphModule`, `custom_codegen_pass` |  |
| [`torchtitan/experiments/graph_trainer/debug_utils.py`](torchtitan/experiments/graph_trainer/debug_utils.md) | 4 | `snapshot_graph`, `log_graph_diff`, `tlparse_log_graph_pass` |  |
| [`torchtitan/experiments/graph_trainer/decompositions.py`](torchtitan/experiments/graph_trainer/decompositions.md) | 3 | `apply_decompositions_pass`, `_apply_decompositions`, `_copy_attr` |  |
| [`torchtitan/experiments/graph_trainer/deepseek_v3/__init__.py`](torchtitan/experiments/graph_trainer/deepseek_v3/__init__.md) | 3 | `model_registry`, `_parallelize_fn`, `_post_optimizer_build_fn` |  |
| [`torchtitan/experiments/graph_trainer/deepseek_v3/config_registry.py`](torchtitan/experiments/graph_trainer/deepseek_v3/config_registry.md) | 9 | `graph_trainer_deepseek_v3_16b`, `graph_trainer_deepseek_v3_debugmodel`, `graph_trainer_deepseek_v3_debugmodel_mxfp8` | [quantization](../concepts/quantization.md) |
| [`torchtitan/experiments/graph_trainer/deepseek_v3/model.py`](torchtitan/experiments/graph_trainer/deepseek_v3/model.md) | 4 | `GraphTrainerDeepSeekV3Model`, `Config`, `init_states` |  |
| [`torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.py`](torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.md) | 2 | `annotate_deepseekv3`, `parallelize_deepseekv3` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.py`](torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.md) | 6 | `parallelize_autoparallel_deepseekv3`, `input_fn`, `_preserve_moe_attributes` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/dynamic_shapes.py`](torchtitan/experiments/graph_trainer/dynamic_shapes.md) | 8 | `_wrapper_subclass_has_marked_dynamic_dims`, `_fakeify_input`, `copy_tensor_annotations` |  |
| [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py`](torchtitan/experiments/graph_trainer/ep_chunk_pass.md) | 108 | `ChunkMode`, `region`, `_Plan` |  |
| [`torchtitan/experiments/graph_trainer/ep_eager_chunk.py`](torchtitan/experiments/graph_trainer/ep_eager_chunk.md) | 23 | `maybe_apply_ep_overlap_eager_chunking`, `root_fqn`, `root_kind` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/ep_overlap_pass.py`](torchtitan/experiments/graph_trainer/ep_overlap_pass.md) | 46 | `_schedule_ep_overlap_regions`, `_TokenExchange`, `_ScheduledRegion` |  |
| [`torchtitan/experiments/graph_trainer/ep_pass_utils.py`](torchtitan/experiments/graph_trainer/ep_pass_utils.md) | 60 | `tensor_meta`, `free_symbols`, `ChunkOwner` |  |
| [`torchtitan/experiments/graph_trainer/ep_process_group_pass.py`](torchtitan/experiments/graph_trainer/ep_process_group_pass.md) | 9 | `isolate_ep_process_group_pass`, `_EXTRA_EP_PG_REGISTRY`, `c10d` |  |
| [`torchtitan/experiments/graph_trainer/fsdp_passes.py`](torchtitan/experiments/graph_trainer/fsdp_passes.md) | 65 | `schedule_fsdp_comms_to_dense_regions_pass`, `reassign_collective_pgs_pass`, `deduplicate_fsdp_unshard_chains_pass` | [graph-trainer](../concepts/graph-trainer.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/fsdp_patterns.py`](torchtitan/experiments/graph_trainer/fsdp_patterns.md) | 14 | `find_fsdp_unshard_outputs`, `find_fsdp_reduce_grad_input`, `find_fsdp_unshard_save_nodes` |  |
| [`torchtitan/experiments/graph_trainer/gradient_accumulation.py`](torchtitan/experiments/graph_trainer/gradient_accumulation.md) | 19 | `GraphGradientState`, `create`, `buffers` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/__init__.py`](torchtitan/experiments/graph_trainer/graph_pp/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py`](torchtitan/experiments/graph_trainer/graph_pp/graph_builder.md) | 81 | `meta`, `modules`, `_execute_graph_module` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/graph_pp/graph_multiplex.py`](torchtitan/experiments/graph_trainer/graph_pp/graph_multiplex.md) | 2 | `multiplex_fw_bw_graph`, `_copy_prefixed_get_attrs` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/partition.py`](torchtitan/experiments/graph_trainer/graph_pp/partition.md) | 29 | `partition_joint_graph`, `fwd_flat_input_indices`, `backward_grad_input_names` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/pipeline.py`](torchtitan/experiments/graph_trainer/graph_pp/pipeline.md) | 2 | `_validate_graph_pp_config`, `graph_pipeline_llm` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/graph_pp/runner.py`](torchtitan/experiments/graph_trainer/graph_pp/runner.md) | 36 | `stage_graphs`, `schedule`, `ensure_ready` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py`](torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.md) | 11 | `split_di_dw_graph`, `num_input_grads`, `bw_di_module` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py`](torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.md) | 16 | `split_forward_fsdp_collectives`, `unshard_module`, `reduce_grad_module` |  |
| [`torchtitan/experiments/graph_trainer/graph_pp/stage.py`](torchtitan/experiments/graph_trainer/graph_pp/stage.md) | 30 | `GraphPipelineStage`, `state`, `sharded_param_grads` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/graph_pp/utils.py`](torchtitan/experiments/graph_trainer/graph_pp/utils.md) | 54 | `unique_in_order`, `dst_shape_env`, `trace_graph_pp_graph` |  |
| [`torchtitan/experiments/graph_trainer/graph_utils.py`](torchtitan/experiments/graph_trainer/graph_utils.md) | 22 | `inner`, `_overrides`, `export_joint` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/inductor_passes.py`](torchtitan/experiments/graph_trainer/inductor_passes.md) | 10 | `full_inductor_compilation_pass`, `annotate_flex_attention_for_regional_inductor_pass`, `regional_inductor_pass` |  |
| [`torchtitan/experiments/graph_trainer/jit_backend.py`](torchtitan/experiments/graph_trainer/jit_backend.md) | 3 | `get_compile_backend_with_passes`, `inductor_autobucketing_reordering_pass`, `inductor_transformer_block_bucketing_reordering_pass` |  |
| [`torchtitan/experiments/graph_trainer/llama3/__init__.py`](torchtitan/experiments/graph_trainer/llama3/__init__.md) | 2 | `model_registry`, `_parallelize_fn` |  |
| [`torchtitan/experiments/graph_trainer/llama3/config_registry.py`](torchtitan/experiments/graph_trainer/llama3/config_registry.md) | 12 | `graph_trainer_llama3_debugmodel_sdpa`, `graph_trainer_llama3_debugmodel_sdc_replay`, `graph_trainer_llama3_8b` |  |
| [`torchtitan/experiments/graph_trainer/llama3/model.py`](torchtitan/experiments/graph_trainer/llama3/model.md) | 4 | `GraphTrainerLlama3Model`, `Config`, `init_states` |  |
| [`torchtitan/experiments/graph_trainer/llama3/parallelize.py`](torchtitan/experiments/graph_trainer/llama3/parallelize.md) | 2 | `annotate_llama`, `parallelize_llama` |  |
| [`torchtitan/experiments/graph_trainer/llama3/parallelize_autoparallel.py`](torchtitan/experiments/graph_trainer/llama3/parallelize_autoparallel.md) | 2 | `parallelize_autoparallel_llama`, `input_fn` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/log_activation_memory_policy.py`](torchtitan/experiments/graph_trainer/log_activation_memory_policy.md) | 21 | `_SYMBOLIC_NBYTES`, `_format_bytes`, `_tensor_nbytes` |  |
| [`torchtitan/experiments/graph_trainer/make_fx_tracer.py`](torchtitan/experiments/graph_trainer/make_fx_tracer.md) | 50 | `minimal_fx_tracer`, `gm`, `example_inputs` |  |
| [`torchtitan/experiments/graph_trainer/memory_policy.py`](torchtitan/experiments/graph_trainer/memory_policy.md) | 25 | `tag_sac_policy`, `_make_full_memory_policy`, `tag_with_memory_policy_pass` |  |
| [`torchtitan/experiments/graph_trainer/muse_glimmer/__init__.py`](torchtitan/experiments/graph_trainer/muse_glimmer/__init__.md) | 1 | `model_registry` |  |
| [`torchtitan/experiments/graph_trainer/muse_glimmer/config_registry.py`](torchtitan/experiments/graph_trainer/muse_glimmer/config_registry.md) | 1 | `graph_trainer_muse_glimmer_debugmodel` |  |
| [`torchtitan/experiments/graph_trainer/muse_glimmer/model.py`](torchtitan/experiments/graph_trainer/muse_glimmer/model.md) | 4 | `GraphTrainerMuseGlimmerModel`, `Config`, `init_states` |  |
| [`torchtitan/experiments/graph_trainer/muse_glimmer/parallelize.py`](torchtitan/experiments/graph_trainer/muse_glimmer/parallelize.md) | 1 | `parallelize_muse_glimmer` |  |
| [`torchtitan/experiments/graph_trainer/passes.py`](torchtitan/experiments/graph_trainer/passes.md) | 10 | `apply_graph_passes`, `compile_time_passes`, `construct_default_graph_passes` |  |
| [`torchtitan/experiments/graph_trainer/performance_passes.py`](torchtitan/experiments/graph_trainer/performance_passes.md) | 1 | `annotate_rmsnorm_for_regional_inductor_pass` |  |
| [`torchtitan/experiments/graph_trainer/precompile.py`](torchtitan/experiments/graph_trainer/precompile.md) | 23 | `compute_config_fingerprint`, `PrecompiledFxTraceArtifact`, `ConfigFingerprint` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/precompile_main.py`](torchtitan/experiments/graph_trainer/precompile_main.md) | 6 | `_prepare_loss_for_precompile`, `_precompile_aot_fx_trace`, `_common_setup` |  |
| [`torchtitan/experiments/graph_trainer/qwen3/__init__.py`](torchtitan/experiments/graph_trainer/qwen3/__init__.md) | 1 | `model_registry` |  |
| [`torchtitan/experiments/graph_trainer/qwen3/config_registry.py`](torchtitan/experiments/graph_trainer/qwen3/config_registry.md) | 4 | `graph_trainer_qwen3_14b`, `graph_trainer_qwen3_30b_a3b_global_aux`, `graph_trainer_qwen3_debugmodel` |  |
| [`torchtitan/experiments/graph_trainer/qwen3/model.py`](torchtitan/experiments/graph_trainer/qwen3/model.md) | 4 | `GraphTrainerQwen3Model`, `Config`, `init_states` |  |
| [`torchtitan/experiments/graph_trainer/qwen3/parallelize.py`](torchtitan/experiments/graph_trainer/qwen3/parallelize.md) | 2 | `annotate_qwen3`, `parallelize_qwen3` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/registry.py`](torchtitan/experiments/graph_trainer/registry.md) | 15 | `register_memory_policy`, `_make_registry_decorator`, `MEMORY_POLICY_REGISTRY` |  |
| [`torchtitan/experiments/graph_trainer/remove_noop_passes.py`](torchtitan/experiments/graph_trainer/remove_noop_passes.md) | 12 | `remove_identity_slice_pass`, `remove_parameter_gradient_markers_pass`, `remove_identity_view_pass` |  |
| [`torchtitan/experiments/graph_trainer/runner.py`](torchtitan/experiments/graph_trainer/runner.md) | 18 | `GraphRunner`, `validate_state`, `_traced_result` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/selective_activation_remat.py`](torchtitan/experiments/graph_trainer/selective_activation_remat.md) | 11 | `selective_activation_remat_pass`, `_gather`, `log` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/simple_fsdp.py`](torchtitan/experiments/graph_trainer/simple_fsdp.md) | 26 | `data_parallel`, `MixedPrecisionPolicy`, `param_dtype` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/storage.py`](torchtitan/experiments/graph_trainer/storage.md) | 13 | `DiskStorageAdapter`, `save`, `exists` |  |
| [`torchtitan/experiments/graph_trainer/subgraph_regions.py`](torchtitan/experiments/graph_trainer/subgraph_regions.md) | 28 | `SUBGRAPH_REGION`, `apply_subgraph_region_annotations_pass`, `SUBGRAPH_REGION_ROLE` |  |
| [`torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.py`](torchtitan/experiments/graph_trainer/tests/_trainer_test_utils.md) | 1 | `build_minimal_trainer` |  |
| [`torchtitan/experiments/graph_trainer/tests/integration_tests.py`](torchtitan/experiments/graph_trainer/tests/integration_tests.md) | 17 | `_build_llama3_tests`, `_build_deepseek_v3_tests`, `_build_qwen3_tests` |  |
| [`torchtitan/experiments/graph_trainer/tests/run_precompile_tests.py`](torchtitan/experiments/graph_trainer/tests/run_precompile_tests.md) | 12 | `test_name`, `ngpu`, `test_descr` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_autoparallel.py`](torchtitan/experiments/graph_trainer/tests/test_autoparallel.md) | 39 | `_FakeAutoParallelGraph`, `instances`, `_FakeMesh` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_bitwise_deterministic.py`](torchtitan/experiments/graph_trainer/tests/test_bitwise_deterministic.md) | 79 | `_run_steps`, `model`, `_assert_runs_match` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py`](torchtitan/experiments/graph_trainer/tests/test_chunked_loss.md) | 20 | `output`, `_make_model_and_loss`, `Config` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py`](torchtitan/experiments/graph_trainer/tests/test_cpu_offload.md) | 24 | `_make_fake_val`, `_build_joint_graph`, `_build_view_chain_graph` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_custom_codegen.py`](torchtitan/experiments/graph_trainer/tests/test_custom_codegen.md) | 21 | `_codegen_dir`, `linear`, `_original_enrich` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.py`](torchtitan/experiments/graph_trainer/tests/test_graph_pp_passes.md) | 46 | `traced`, `_trace_dsv3_moe_block_stage`, `_backward_args_from_partition` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_graph_pp_runner.py`](torchtitan/experiments/graph_trainer/tests/test_graph_pp_runner.md) | 73 | `_make_test_stage`, `_build_test_stage_graphs`, `loss_fn` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_graph_runner.py`](torchtitan/experiments/graph_trainer/tests/test_graph_runner.md) | 18 | `forward`, `named_parameters_calls`, `CountingLinear` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_numerics.py`](torchtitan/experiments/graph_trainer/tests/test_numerics.md) | 63 | `mode`, `_run_deepseek_v3_loss_compare`, `DEBUGMODEL_TRAINING_OPTIONS` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_passes.py`](torchtitan/experiments/graph_trainer/tests/test_passes.md) | 434 | `_chunk_batch`, `_symbolic_batch_fake_mode`, `_tag_fsdp_schedule_node` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/tests/test_performance_passes.py`](torchtitan/experiments/graph_trainer/tests/test_performance_passes.md) | 7 | `_build_rmsnorm_gm`, `_count_tagged_nodes`, `test_fwd_and_bwd_both_tagged` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_precompile.py`](torchtitan/experiments/graph_trainer/tests/test_precompile.md) | 58 | `_make_stub_model`, `_StubCompileConfig`, `_StubParallelDims` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_profiler.py`](torchtitan/experiments/graph_trainer/tests/test_profiler.md) | 18 | `_run_profiler`, `ANNOTATIONS`, `ffn` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_remat_metadata.py`](torchtitan/experiments/graph_trainer/tests/test_remat_metadata.md) | 15 | `layers`, `full_step`, `_Block` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.py`](torchtitan/experiments/graph_trainer/tests/test_sac_peak_memory.md) | 20 | `_build_model`, `DEBUGMODEL`, `loss` | [graph-trainer](../concepts/graph-trainer.md) |
| [`torchtitan/experiments/graph_trainer/tests/test_simple_fsdp.py`](torchtitan/experiments/graph_trainer/tests/test_simple_fsdp.md) | 5 | `test_param_cast_to_bf16_at_ngpu_1`, `test_spmd_types_uses_dtensor_storage_and_local_compute`, `TestApplySimpleFSDPSingleRank` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_subgraph_regions.py`](torchtitan/experiments/graph_trainer/tests/test_subgraph_regions.md) | 14 | `_invoke_subgraph_nodes`, `_annotate_region`, `_subgraph_modules` |  |
| [`torchtitan/experiments/graph_trainer/tests/test_trace_module.py`](torchtitan/experiments/graph_trainer/tests/test_trace_module.md) | 182 | `SimpleMLP`, `DEVICE`, `forward` |  |
| [`torchtitan/experiments/graph_trainer/trainer.py`](torchtitan/experiments/graph_trainer/trainer.md) | 23 | `GraphTrainer`, `Config`, `_traced_step` | [graph-trainer](../concepts/graph-trainer.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/jax/data_utils.py`](torchtitan/experiments/jax/data_utils.md) | 2 | `fake_dataloader`, `torch_loader_to_jax` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/distributed.py`](torchtitan/experiments/jax/distributed.md) | 9 | `_match_path`, `sharded_device_put`, `_process_sharding_name` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/jax_job_config.py`](torchtitan/experiments/jax/jax_job_config.md) | 8 | `JaxJobConfig`, `JaxConfig`, `use_scan` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/jax_profiling.py`](torchtitan/experiments/jax/jax_profiling.md) | 8 | `logger`, `tracing`, `maybe_enable_profiling` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/llama3/__init__.py`](torchtitan/experiments/jax/llama3/__init__.md) | 2 | `args`, `__all__` |  |
| [`torchtitan/experiments/jax/llama3/config_registry.py`](torchtitan/experiments/jax/llama3/config_registry.md) | 2 | `_model_spec`, `llama3_debugmodel` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/llama3/model.py`](torchtitan/experiments/jax/llama3/model.md) | 70 | `dim`, `ModelArgs`, `n_heads` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/llama3/sharding.py`](torchtitan/experiments/jax/llama3/sharding.md) | 2 | `sharding_map_original`, `sharding_map_scan` |  |
| [`torchtitan/experiments/jax/metrics.py`](torchtitan/experiments/jax/metrics.md) | 20 | `num_flops_per_token`, `data_loading_times`, `ntokens_since_last_log` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/splash_attn.py`](torchtitan/experiments/jax/splash_attn.md) | 6 | `make_splash_attention_fn`, `logger`, `build_splash_attention_callable` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/tests/test_distributed.py`](torchtitan/experiments/jax/tests/test_distributed.md) | 22 | `test_jax_llama3_non_scan`, `test_jax_llama3_scan`, `test_hit` |  |
| [`torchtitan/experiments/jax/tests/test_train_distributed.py`](torchtitan/experiments/jax/tests/test_train_distributed.md) | 2 | `test_train_jax`, `TestJaxDistributed` |  |
| [`torchtitan/experiments/jax/train_minimal.py`](torchtitan/experiments/jax/train_minimal.md) | 5 | `main_train_loop`, `logger`, `_maybe_init_jax_distributed` | [jax-lane](../concepts/jax-lane.md) |
| [`torchtitan/experiments/jax/trainer.py`](torchtitan/experiments/jax/trainer.md) | 22 | `logger`, `mesh`, `train` | [jax-lane](../concepts/jax-lane.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/jax/utils.py`](torchtitan/experiments/jax/utils.md) | 1 | `get_accelerator_short_name` |  |
| [`torchtitan/experiments/rl/__init__.py`](torchtitan/experiments/rl/__init__.md) | 2 | `__all__`, `__getattr__` |  |
| [`torchtitan/experiments/rl/actors/generator.py`](torchtitan/experiments/rl/actors/generator.md) | 119 | `SamplingConfig`, `parallelism`, `VLLMGenerator` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/actors/rollout_worker.py`](torchtitan/experiments/rl/actors/rollout_worker.md) | 6 | `_worker`, `RolloutWorkerActor`, `run_group` |  |
| [`torchtitan/experiments/rl/actors/trainer.py`](torchtitan/experiments/rl/actors/trainer.md) | 46 | `parallelism`, `training`, `PolicyTrainer` | [rl-training](../concepts/rl-training.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/rl/batch_invariance.py`](torchtitan/experiments/rl/batch_invariance.md) | 9 | `force_logprobs_fn_for_batch_invariance`, `Config`, `BatchInvariantFlexConverter` |  |
| [`torchtitan/experiments/rl/components/batcher.py`](torchtitan/experiments/rl/components/batcher.md) | 30 | `Batcher`, `Config`, `add_training_samples` |  |
| [`torchtitan/experiments/rl/components/training_sample_builder.py`](torchtitan/experiments/rl/components/training_sample_builder.md) | 8 | `TrainingSampleBuilder`, `Config`, `drop_zero_std_reward_groups` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/components/weight_sync.py`](torchtitan/experiments/rl/components/weight_sync.md) | 17 | `start_async_push_pull`, `wait_prev_pull`, `wait_prev_push` |  |
| [`torchtitan/experiments/rl/components/work_buffer.py`](torchtitan/experiments/rl/components/work_buffer.md) | 28 | `RolloutGroupWorkBuffer`, `_condition`, `RolloutGroupWork` |  |
| [`torchtitan/experiments/rl/controller.py`](torchtitan/experiments/rl/controller.md) | 64 | `Controller`, `Config`, `trainer` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/controller_metrics.py`](torchtitan/experiments/rl/controller_metrics.md) | 10 | `compute_perf_ratio_metrics`, `compute_policy_age_metrics`, `compute_rollout_metrics` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/environment/__init__.py`](torchtitan/experiments/rl/environment/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/environment/message.py`](torchtitan/experiments/rl/environment/message.md) | 13 | `MessageEnv`, `env_messages`, `done` |  |
| [`torchtitan/experiments/rl/environment/token.py`](torchtitan/experiments/rl/environment/token.md) | 25 | `TokenEnv`, `Config`, `status` |  |
| [`torchtitan/experiments/rl/examples/alphabet_sort/__init__.py`](torchtitan/experiments/rl/examples/alphabet_sort/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/examples/alphabet_sort/config_registry.py`](torchtitan/experiments/rl/examples/alphabet_sort/config_registry.md) | 22 | `_qwen3_rl_model_registry`, `_BATCH_INVARIANT_DEBUG`, `_qwen3_5_rl_model_registry` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/examples/alphabet_sort/data.py`](torchtitan/experiments/rl/examples/alphabet_sort/data.md) | 27 | `AlphabetSortDataset`, `Config`, `new_names_per_turn` |  |
| [`torchtitan/experiments/rl/examples/alphabet_sort/env.py`](torchtitan/experiments/rl/examples/alphabet_sort/env.md) | 7 | `AlphabetSortEnv`, `Config`, `step` |  |
| [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py`](torchtitan/experiments/rl/examples/alphabet_sort/rollouter.md) | 9 | `AlphabetSortRollouter`, `Config`, `AlphabetSortWorker` |  |
| [`torchtitan/experiments/rl/examples/alphabet_sort/rubric.py`](torchtitan/experiments/rl/examples/alphabet_sort/rubric.md) | 10 | `RewardAlphabetSort`, `Config`, `score_sorted_list` |  |
| [`torchtitan/experiments/rl/examples/dapo_math/__init__.py`](torchtitan/experiments/rl/examples/dapo_math/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/examples/dapo_math/config_registry.py`](torchtitan/experiments/rl/examples/dapo_math/config_registry.md) | 3 | `_qwen3_4b_dapo_math_config`, `rl_dapo_qwen3_4b_math_32k`, `rl_dapo_qwen3_4b_math_8k` | [job-config](../concepts/job-config.md) |
| [`torchtitan/experiments/rl/examples/dapo_math/data.py`](torchtitan/experiments/rl/examples/dapo_math/data.md) | 31 | `DapoMathSample`, `ground_truth`, `prompt` |  |
| [`torchtitan/experiments/rl/examples/dapo_math/env.py`](torchtitan/experiments/rl/examples/dapo_math/env.md) | 6 | `Config`, `DapoMathEnv`, `init` |  |
| [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py`](torchtitan/experiments/rl/examples/dapo_math/rollouter.md) | 11 | `DapoMathWorker`, `Config`, `DapoMathRollouter` |  |
| [`torchtitan/experiments/rl/examples/dapo_math/rubric.py`](torchtitan/experiments/rl/examples/dapo_math/rubric.md) | 6 | `score_math_response`, `RewardMathVerify`, `Config` |  |
| [`torchtitan/experiments/rl/examples/search_r1/__init__.py`](torchtitan/experiments/rl/examples/search_r1/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/examples/search_r1/config_registry.py`](torchtitan/experiments/rl/examples/search_r1/config_registry.md) | 4 | `rl_grpo_qwen3_1_7b_search_r1`, `rl_grpo_qwen3_30b_a3b_deepep_search_r1_perf`, `rl_grpo_muse_glimmer_30b_search_r1` | [job-config](../concepts/job-config.md) |
| [`torchtitan/experiments/rl/examples/search_r1/data.py`](torchtitan/experiments/rl/examples/search_r1/data.md) | 22 | `SearchR1Sample`, `_order`, `_rng` |  |
| [`torchtitan/experiments/rl/examples/search_r1/env.py`](torchtitan/experiments/rl/examples/search_r1/env.md) | 18 | `step`, `SearchR1Env`, `Config` |  |
| [`torchtitan/experiments/rl/examples/search_r1/rollouter.py`](torchtitan/experiments/rl/examples/search_r1/rollouter.md) | 10 | `SearchR1Worker`, `Config`, `SearchR1Rollouter` |  |
| [`torchtitan/experiments/rl/examples/search_r1/rubric.py`](torchtitan/experiments/rl/examples/search_r1/rubric.md) | 16 | `RewardExactMatch`, `Config`, `_normalize_answer` |  |
| [`torchtitan/experiments/rl/examples/verifiers/components/__init__.py`](torchtitan/experiments/rl/examples/verifiers/components/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/examples/verifiers/components/data.py`](torchtitan/experiments/rl/examples/verifiers/components/data.md) | 17 | `verifiers_taskset`, `VerifiersTaskDataset`, `Config` |  |
| [`torchtitan/experiments/rl/examples/verifiers/components/env_server.py`](torchtitan/experiments/rl/examples/verifiers/components/env_server.md) | 19 | `environment`, `serve`, `Config` |  |
| [`torchtitan/experiments/rl/examples/verifiers/components/generation_server.py`](torchtitan/experiments/rl/examples/verifiers/components/generation_server.md) | 30 | `VerifiersGenerationMetadata`, `GenerationServer`, `Config` |  |
| [`torchtitan/experiments/rl/examples/verifiers/components/rollouter.py`](torchtitan/experiments/rl/examples/verifiers/components/rollouter.md) | 34 | `VerifiersRollouter`, `_generation_server`, `trace_to_rollout_turns` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/examples/verifiers/dapo_math/__init__.py`](torchtitan/experiments/rl/examples/verifiers/dapo_math/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.py`](torchtitan/experiments/rl/examples/verifiers/dapo_math/config_registry.md) | 3 | `_qwen3_4b_verifiers_config`, `rl_dapo_qwen3_4b_verifiers_32k`, `rl_dapo_qwen3_4b_verifiers_8k` |  |
| [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py`](torchtitan/experiments/rl/examples/verifiers/dapo_math/data.md) | 12 | `VerifiersMathTasksetConfig`, `VerifiersMathData`, `VerifiersMathTask` |  |
| [`torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py`](torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.md) | 7 | `VerifiersMathRollouter`, `Config`, `_math_taskset_config` |  |
| [`torchtitan/experiments/rl/generate.py`](torchtitan/experiments/rl/generate.md) | 3 | `logger`, `_parse_args`, `generate` |  |
| [`torchtitan/experiments/rl/losses/__init__.py`](torchtitan/experiments/rl/losses/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/losses/dapo.py`](torchtitan/experiments/rl/losses/dapo.md) | 9 | `DAPOLoss`, `Config`, `ratio_clip_high` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/losses/grpo.py`](torchtitan/experiments/rl/losses/grpo.md) | 4 | `GRPOLoss`, `Config`, `clip_eps` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/models/attention.py`](torchtitan/experiments/rl/models/attention.md) | 29 | `VLLMAttentionWrapper`, `Config`, `head_dim` |  |
| [`torchtitan/experiments/rl/models/cast_linear.py`](torchtitan/experiments/rl/models/cast_linear.md) | 13 | `LMHeadCastConverter`, `Config`, `Config` |  |
| [`torchtitan/experiments/rl/models/gdn.py`](torchtitan/experiments/rl/models/gdn.md) | 29 | `head_k_dim`, `tensor_parallel_size`, `head_v_dim` |  |
| [`torchtitan/experiments/rl/models/muse_glimmer/atem.py`](torchtitan/experiments/rl/models/muse_glimmer/atem.md) | 8 | `parse_atem_tool_calls`, `render_atem_tool_call`, `calls` |  |
| [`torchtitan/experiments/rl/models/muse_glimmer/renderer.py`](torchtitan/experiments/rl/models/muse_glimmer/renderer.md) | 62 | `MuseGlimmerRendererConfig`, `EOT_ID`, `render_ids` |  |
| [`torchtitan/experiments/rl/models/vllm_registry.py`](torchtitan/experiments/rl/models/vllm_registry.md) | 22 | `tensor_parallel_degree`, `InferenceParallelismConfig`, `data_parallel_degree` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/models/vllm_worker.py`](torchtitan/experiments/rl/models/vllm_worker.md) | 4 | `TorchTitanGPUModelRunner`, `_pad_for_sequence_parallelism`, `init_device` |  |
| [`torchtitan/experiments/rl/models/vllm_wrapper.py`](torchtitan/experiments/rl/models/vllm_wrapper.md) | 40 | `model`, `parallel_dims`, `config` |  |
| [`torchtitan/experiments/rl/observability/metrics/__init__.py`](torchtitan/experiments/rl/observability/metrics/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/observability/metrics/console.py`](torchtitan/experiments/rl/observability/metrics/console.md) | 5 | `log_to_console`, `fmt_metric_value`, `_COLOR_CYCLE` |  |
| [`torchtitan/experiments/rl/observability/metrics/processor.py`](torchtitan/experiments/rl/observability/metrics/processor.md) | 14 | `MetricsProcessor`, `_aggregate_metrics`, `Config` |  |
| [`torchtitan/experiments/rl/observability/metrics/types.py`](torchtitan/experiments/rl/observability/metrics/types.md) | 58 | `Metric`, `NoReduce`, `Mean` |  |
| [`torchtitan/experiments/rl/observability/vllm_otel_stat_logger.py`](torchtitan/experiments/rl/observability/vllm_otel_stat_logger.md) | 57 | `Config`, `VllmOtelStatLogger`, `kv_cache_usage` |  |
| [`torchtitan/experiments/rl/renderer.py`](torchtitan/experiments/rl/renderer.md) | 19 | `renderers_config`, `RenderersLibraryConfig`, `RendererConfig` |  |
| [`torchtitan/experiments/rl/rollout/__init__.py`](torchtitan/experiments/rl/rollout/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/rollout/advantage.py`](torchtitan/experiments/rl/rollout/advantage.md) | 6 | `AdvantageEstimator`, `Config`, `should_std_normalize` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/rollout/rollouter.py`](torchtitan/experiments/rl/rollout/rollouter.md) | 38 | `Rollouter`, `RolloutWorker`, `Config` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/rollout/types.py`](torchtitan/experiments/rl/rollout/types.md) | 41 | `Rollout`, `turns`, `RolloutStatus` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/rollout_recorder.py`](torchtitan/experiments/rl/rollout_recorder.md) | 20 | `record`, `Config`, `Config` |  |
| [`torchtitan/experiments/rl/routing/__init__.py`](torchtitan/experiments/rl/routing/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/routing/inter_generator_router.py`](torchtitan/experiments/rl/routing/inter_generator_router.md) | 32 | `_route`, `_generators`, `InterGeneratorRouter` |  |
| [`torchtitan/experiments/rl/routing/intra_generator_router.py`](torchtitan/experiments/rl/routing/intra_generator_router.md) | 12 | `IntraGeneratorRouter`, `Config`, `strategy` |  |
| [`torchtitan/experiments/rl/routing/strategies.py`](torchtitan/experiments/rl/routing/strategies.md) | 24 | `LeastLoadedRoutingStrategy`, `Config`, `StickySessionRoutingStrategy` |  |
| [`torchtitan/experiments/rl/routing/types.py`](torchtitan/experiments/rl/routing/types.md) | 5 | `RoutingContext`, `session_id`, `RoutingCandidate` |  |
| [`torchtitan/experiments/rl/rubrics/__init__.py`](torchtitan/experiments/rl/rubrics/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/rl/rubrics/rubric.py`](torchtitan/experiments/rl/rubrics/rubric.md) | 20 | `RewardFn`, `Rubric`, `Config` |  |
| [`torchtitan/experiments/rl/runtime_env.py`](torchtitan/experiments/rl/runtime_env.md) | 2 | `apply_env_defaults`, `RL_ENV_DEFAULTS` |  |
| [`torchtitan/experiments/rl/scripts/loss_compare.py`](torchtitan/experiments/rl/scripts/loss_compare.md) | 9 | `log_print`, `assert_losses_equal`, `extract_losses_from_tensorboard` |  |
| [`torchtitan/experiments/rl/tests/integration_tests.py`](torchtitan/experiments/rl/tests/integration_tests.md) | 5 | `build_rl_test_list`, `run_tests`, `run_single_test` |  |
| [`torchtitan/experiments/rl/tests/test_alphabet_sort.py`](torchtitan/experiments/rl/tests/test_alphabet_sort.md) | 25 | `_patch_names`, `_assistant_turn`, `_rollout` |  |
| [`torchtitan/experiments/rl/tests/test_async_controller.py`](torchtitan/experiments/rl/tests/test_async_controller.md) | 31 | `_trainable_group`, `_build_batcher`, `_untrainable_group` |  |
| [`torchtitan/experiments/rl/tests/test_bitwise_parity.py`](torchtitan/experiments/rl/tests/test_bitwise_parity.md) | 76 | `BitwiseParityTestBase`, `prompt_ids`, `engine` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/tests/test_cast_linear.py`](torchtitan/experiments/rl/tests/test_cast_linear.md) | 8 | `_qwen3_config`, `test_converter_swaps_only_lm_head`, `test_converter_returns_model_config` |  |
| [`torchtitan/experiments/rl/tests/test_dapo_math.py`](torchtitan/experiments/rl/tests/test_dapo_math.md) | 13 | `_rollout`, `_dapo_rows`, `load_dataset` |  |
| [`torchtitan/experiments/rl/tests/test_engine_loop.py`](torchtitan/experiments/rl/tests/test_engine_loop.md) | 8 | `_bare_generator`, `_request`, `test_step_sticky_session_reuses_dp_rank` |  |
| [`torchtitan/experiments/rl/tests/test_generator.py`](torchtitan/experiments/rl/tests/test_generator.md) | 39 | `_request_output`, `_dispatcher`, `_generator` |  |
| [`torchtitan/experiments/rl/tests/test_inter_generator_router.py`](torchtitan/experiments/rl/tests/test_inter_generator_router.md) | 51 | `_router`, `_Actor`, `release` |  |
| [`torchtitan/experiments/rl/tests/test_intra_generator_router.py`](torchtitan/experiments/rl/tests/test_intra_generator_router.md) | 9 | `_loads`, `test_least_loaded_balances_in_flight_count`, `test_release_frees_load` |  |
| [`torchtitan/experiments/rl/tests/test_metrics.py`](torchtitan/experiments/rl/tests/test_metrics.md) | 93 | `_RecordingBackend`, `_logger`, `calls` |  |
| [`torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py`](torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.md) | 30 | `_renderer`, `TOOLS`, `CASES` |  |
| [`torchtitan/experiments/rl/tests/test_renderer.py`](torchtitan/experiments/rl/tests/test_renderer.md) | 9 | `_TOKENIZER_PATH`, `_Holder`, `renderer` |  |
| [`torchtitan/experiments/rl/tests/test_rollout_recorder.py`](torchtitan/experiments/rl/tests/test_rollout_recorder.md) | 16 | `_group`, `_recorder`, `_read_lines` |  |
| [`torchtitan/experiments/rl/tests/test_rollout_utils.py`](torchtitan/experiments/rl/tests/test_rollout_utils.md) | 10 | `_turn`, `_scored_rollout`, `rollout_to_training_samples` |  |
| [`torchtitan/experiments/rl/tests/test_rollout_worker.py`](torchtitan/experiments/rl/tests/test_rollout_worker.md) | 34 | `_CustomWorker`, `envs`, `calls` |  |
| [`torchtitan/experiments/rl/tests/test_rollouter_pool.py`](torchtitan/experiments/rl/tests/test_rollouter_pool.md) | 35 | `_WorkerActorMesh`, `_WorkerMesh`, `actor_mesh` |  |
| [`torchtitan/experiments/rl/tests/test_runtime_env.py`](torchtitan/experiments/rl/tests/test_runtime_env.md) | 2 | `test_apply_env_defaults`, `test_apply_env_defaults_preserves_existing_values` |  |
| [`torchtitan/experiments/rl/tests/test_search_r1.py`](torchtitan/experiments/rl/tests/test_search_r1.md) | 15 | `_rollout`, `EX`, `_build_env` |  |
| [`torchtitan/experiments/rl/tests/test_shutdown.py`](torchtitan/experiments/rl/tests/test_shutdown.md) | 80 | `_FakeController`, `instances`, `config` | [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/rl/tests/test_token_env.py`](torchtitan/experiments/rl/tests/test_token_env.md) | 14 | `calls`, `_TOOLS`, `run` |  |
| [`torchtitan/experiments/rl/tests/test_verifiers.py`](torchtitan/experiments/rl/tests/test_verifiers.md) | 9 | `generate_fn`, `generate_fn`, `run_test` |  |
| [`torchtitan/experiments/rl/tests/test_verifiers_example.py`](torchtitan/experiments/rl/tests/test_verifiers_example.md) | 4 | `test_verifiers_task_dataset_is_resumable`, `test_verifiers_environment_uses_no_sandbox`, `test_verifiers_config_keeps_dapo_training_recipe` |  |
| [`torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.py`](torchtitan/experiments/rl/tests/test_vllm_otel_stat_logger.md) | 25 | `_context`, `_vllm_config`, `create_meter_provider` |  |
| [`torchtitan/experiments/rl/tests/test_vllm_registry.py`](torchtitan/experiments/rl/tests/test_vllm_registry.md) | 4 | `Model`, `FakeStateCopyFuncCalculator`, `test_gdn_hybrid_model_registers_state_copy_funcs` |  |
| [`torchtitan/experiments/rl/tests/test_vllm_wrapper.py`](torchtitan/experiments/rl/tests/test_vllm_wrapper.md) | 1 | `test_state_dict_layouts_include_split_expert_weights` |  |
| [`torchtitan/experiments/rl/tests/test_weight_sync.py`](torchtitan/experiments/rl/tests/test_weight_sync.md) | 45 | `_manager`, `_FakeBuffer`, `_FakeRouter` |  |
| [`torchtitan/experiments/rl/train.py`](torchtitan/experiments/rl/train.md) | 19 | `main`, `allocate`, `next_gpu` | [rl-training](../concepts/rl-training.md) |
| [`torchtitan/experiments/rl/types.py`](torchtitan/experiments/rl/types.md) | 41 | `RolloutTurnID`, `turn_id`, `group_id` |  |
| [`torchtitan/experiments/torchft/__init__.py`](torchtitan/experiments/torchft/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/torchft/checkpoint.py`](torchtitan/experiments/torchft/checkpoint.md) | 19 | `enable_ft_dataloader_checkpoints`, `TorchFTCheckpointManager`, `Config` |  |
| [`torchtitan/experiments/torchft/config/__init__.py`](torchtitan/experiments/torchft/config/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/torchft/config/job_config.py`](torchtitan/experiments/torchft/config/job_config.md) | 11 | `FaultTolerance`, `FaultTolerantModelSpec`, `num_fragments` |  |
| [`torchtitan/experiments/torchft/diloco/__init__.py`](torchtitan/experiments/torchft/diloco/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/torchft/diloco/utils.py`](torchtitan/experiments/torchft/diloco/utils.md) | 3 | `fragment_llm`, `module_split`, `_build_fragment_from_modules` |  |
| [`torchtitan/experiments/torchft/llama3/__init__.py`](torchtitan/experiments/torchft/llama3/__init__.md) | 1 | `model_registry` |  |
| [`torchtitan/experiments/torchft/llama3/config_registry.py`](torchtitan/experiments/torchft/llama3/config_registry.md) | 1 | `llama3_torchft_debugmodel` |  |
| [`torchtitan/experiments/torchft/manager.py`](torchtitan/experiments/torchft/manager.md) | 24 | `TorchFTManager`, `use_async_quorum`, `_manager` |  |
| [`torchtitan/experiments/torchft/optimizer.py`](torchtitan/experiments/torchft/optimizer.md) | 12 | `TorchFTOptimizersContainer`, `Config`, `cache_state_dict` |  |
| [`torchtitan/experiments/torchft/tests/integration_tests.py`](torchtitan/experiments/torchft/tests/integration_tests.md) | 6 | `logger`, `run_single_test`, `run_tests` |  |
| [`torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py`](torchtitan/experiments/torchft/tests/test_torchft_checkpoint.md) | 45 | `test_folder`, `_build_replica`, `DummyFTManager` |  |
| [`torchtitan/experiments/torchft/trainer.py`](torchtitan/experiments/torchft/trainer.md) | 12 | `ft_manager`, `train_step`, `init_distributed` | [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/tpu/accelerator_device_type.py`](torchtitan/experiments/tpu/accelerator_device_type.md) | 4 | `AcceleratorDeviceType`, `TPU`, `CPU` |  |
| [`torchtitan/experiments/tpu/activation_checkpoint.py`](torchtitan/experiments/tpu/activation_checkpoint.md) | 12 | `TPUSelectiveAC`, `Config`, `tpu_selective_ac_config` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/base_device_test.py`](torchtitan/experiments/tpu/base_device_test.md) | 9 | `accelerator_device`, `BaseAcceleratorDeviceTest`, `_create_input_tensor_cpu_device` |  |
| [`torchtitan/experiments/tpu/base_distributed_device_test.py`](torchtitan/experiments/tpu/base_distributed_device_test.md) | 49 | `accelerator_device_type`, `num_devices`, `InputDistribution` |  |
| [`torchtitan/experiments/tpu/bld_layout.py`](torchtitan/experiments/tpu/bld_layout.md) | 19 | `apply_bld_layout`, `_BLDGQAttention`, `forward` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/cloud_distributed_utils.py`](torchtitan/experiments/tpu/cloud_distributed_utils.md) | 12 | `get_slice_id`, `get_slice_id_from_worker_hostnames`, `_maybe_init_distributed_on_gke` |  |
| [`torchtitan/experiments/tpu/compiled_optimizers/functional.py`](torchtitan/experiments/tpu/compiled_optimizers/functional.md) | 5 | `_get_optstate_buffer`, `functional_adamw_step`, `_get_param_by_fqn` |  |
| [`torchtitan/experiments/tpu/compiled_optimizers/separate_graph.py`](torchtitan/experiments/tpu/compiled_optimizers/separate_graph.md) | 8 | `apply_compiled_optimizer`, `_tpu_backend_compile_pass`, `_build_compiled_optimizer_groups` |  |
| [`torchtitan/experiments/tpu/compiled_optimizers/tests/test_separate_graph.py`](torchtitan/experiments/tpu/compiled_optimizers/tests/test_separate_graph.md) | 12 | `step`, `DummyTrainer`, `optimizers` |  |
| [`torchtitan/experiments/tpu/conformer/__init__.py`](torchtitan/experiments/tpu/conformer/__init__.md) | 2 | `conformer_args`, `__all__` |  |
| [`torchtitan/experiments/tpu/conformer/config_registry.py`](torchtitan/experiments/tpu/conformer/config_registry.md) | 3 | `_conformer_model_spec`, `conformer_test`, `conformer_debugmodel` |  |
| [`torchtitan/experiments/tpu/conformer/infra/parallelize.py`](torchtitan/experiments/tpu/conformer/infra/parallelize.md) | 11 | `ParallelStrategy`, `DDP`, `DDP_W_SIMPLEFSDP` |  |
| [`torchtitan/experiments/tpu/conformer/jax_ctc_loss.py`](torchtitan/experiments/tpu/conformer/jax_ctc_loss.md) | 9 | `ctc_loss_forward_jax`, `ctc_loss_fwd`, `ctc_loss_backward_jax` |  |
| [`torchtitan/experiments/tpu/conformer/model.py`](torchtitan/experiments/tpu/conformer/model.md) | 56 | `hidden_dim`, `vocab_size`, `ConformerModelArgs` |  |
| [`torchtitan/experiments/tpu/conformer/tests/model_test.py`](torchtitan/experiments/tpu/conformer/tests/model_test.md) | 12 | `out_proj`, `in_proj`, `num_heads` |  |
| [`torchtitan/experiments/tpu/conformer/tests/test_jax_ctc_loss.py`](torchtitan/experiments/tpu/conformer/tests/test_jax_ctc_loss.md) | 2 | `test_equivalence`, `JAXLossEquivalenceTest` |  |
| [`torchtitan/experiments/tpu/conformer/tests/test_train_minimal_distributed.py`](torchtitan/experiments/tpu/conformer/tests/test_train_minimal_distributed.md) | 2 | `TrainMinimalDistributedTest`, `test_conformer_train_minimal` |  |
| [`torchtitan/experiments/tpu/conformer/train_minimal.py`](torchtitan/experiments/tpu/conformer/train_minimal.md) | 6 | `start_trainer`, `logger`, `TORCH_DTYPE_MAP` | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |
| [`torchtitan/experiments/tpu/cp_attention.py`](torchtitan/experiments/tpu/cp_attention.md) | 63 | `KVAllGatherCPScaledDotProductInnerAttention`, `UlyssesCPScaledDotProductInnerAttention`, `_CP_RANK_CACHE` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/datasets.py`](torchtitan/experiments/tpu/datasets.md) | 8 | `c4_test_dataloader`, `_text_dataset`, `Config` |  |
| [`torchtitan/experiments/tpu/deepseek_v3/__init__.py`](torchtitan/experiments/tpu/deepseek_v3/__init__.md) | 5 | `deepseekv3_configs`, `_testmodel`, `_testmodel_moe` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/experiments/tpu/deepseek_v3/config_registry.py`](torchtitan/experiments/tpu/deepseek_v3/config_registry.md) | 2 | `deepseek_v3_debugmodel`, `graph_trainer_deepseek_v3_debugmodel` |  |
| [`torchtitan/experiments/tpu/deepseek_v3/tests/test_deepseek_v3.py`](torchtitan/experiments/tpu/deepseek_v3/tests/test_deepseek_v3.md) | 9 | `_get_model_config`, `FULL_MODEL_TEST_CONFIGS`, `setUp` |  |
| [`torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py`](torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.md) | 14 | `_get_deepseek_v3_model_config`, `TEST_BATCH_SIZE`, `TEST_SEQ_LEN` |  |
| [`torchtitan/experiments/tpu/device_env.py`](torchtitan/experiments/tpu/device_env.md) | 3 | `cpu_only_env`, `_BACKEND_AUTOLOAD`, `_CUDA_VISIBLE_DEVICES` | [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/distributed.py`](torchtitan/experiments/tpu/distributed.md) | 3 | `run_distributed`, `_ensure_device_type_set`, `_run_in_gdist_worker` | [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/distributed_utils.py`](torchtitan/experiments/tpu/distributed_utils.md) | 1 | `maybe_init_distributed` |  |
| [`torchtitan/experiments/tpu/examples/dilated_conv.py`](torchtitan/experiments/tpu/examples/dilated_conv.md) | 9 | `K`, `ng`, `max_pad` |  |
| [`torchtitan/experiments/tpu/examples/gemma4/__init__.py`](torchtitan/experiments/tpu/examples/gemma4/__init__.md) | 18 | `_build_flavor_config`, `model_registry`, `_gemma4_norm` | [model-building-blocks](../concepts/model-building-blocks.md), [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/examples/gemma4/config_registry.py`](torchtitan/experiments/tpu/examples/gemma4/config_registry.md) | 5 | `gemma4_debugmodel`, `gemma4_31b`, `gemma4_moe_testmodel` |  |
| [`torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.py`](torchtitan/experiments/tpu/examples/gemma4/infra/parallelize.md) | 5 | `parallelize_gemma4`, `_apply_ac_gemma4`, `_apply_compile_gemma4` |  |
| [`torchtitan/experiments/tpu/examples/gemma4/model.py`](torchtitan/experiments/tpu/examples/gemma4/model.md) | 87 | `Gemma4Model`, `Config`, `moe` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/examples/gemma4/sharding.py`](torchtitan/experiments/tpu/examples/gemma4/sharding.md) | 3 | `set_gemma4_sharding_config`, `_set_gemma4_layer_sharding`, `_GROUPED_EXPERTS_PARAM_LAYOUT` |  |
| [`torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.py`](torchtitan/experiments/tpu/examples/gemma4/state_dict_adapter.md) | 10 | `Gemma4StateDictAdapter`, `from_hf`, `to_hf` |  |
| [`torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.py`](torchtitan/experiments/tpu/examples/gemma4/tests/test_gemma4.md) | 32 | `_SEQ_LEN`, `_EXPERTS_INIT`, `_build_hf_reference` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/examples/mamba2/__init__.py`](torchtitan/experiments/tpu/examples/mamba2/__init__.md) | 21 | `mamba2_130m`, `mamba2_debug`, `mamba2_1_3b` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/config_registry.py`](torchtitan/experiments/tpu/examples/mamba2/config_registry.md) | 16 | `model_registry`, `mamba2_configs`, `mamba2_130m` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.py`](torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.md) | 16 | `ssd_chunk_scan_pallas`, `_pallas_ssd_fwd`, `ssd_scan_pure_jax` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/model.py`](torchtitan/experiments/tpu/examples/mamba2/model.md) | 63 | `d_model`, `Mamba2Config`, `n_heads` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/parallelize.py`](torchtitan/experiments/tpu/examples/mamba2/parallelize.md) | 1 | `parallelize_mamba2` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/tests/model_test.py`](torchtitan/experiments/tpu/examples/mamba2/tests/model_test.md) | 6 | `test_weight_tying`, `test_grouped_heads_model`, `test_instantiation_and_forward` |  |
| [`torchtitan/experiments/tpu/examples/mamba2/tests/test_mamba2_pallas.py`](torchtitan/experiments/tpu/examples/mamba2/tests/test_mamba2_pallas.md) | 14 | `arr`, `reference_sequential_ssd`, `_MockRef` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/__init__.py`](torchtitan/experiments/tpu/examples/mamba3/__init__.md) | 10 | `mamba3_2_7b_256k`, `model_registry`, `mamba3_tpu_configs` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/config_registry.py`](torchtitan/experiments/tpu/examples/mamba3/config_registry.md) | 5 | `model_registry`, `mamba3_configs`, `mamba3_2_7b_256k` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.py`](torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.md) | 70 | `_CHUNK_SIZE`, `_cumsum_via_matmul`, `_ssd3_core` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/model.py`](torchtitan/experiments/tpu/examples/mamba3/model.md) | 72 | `d_model`, `Mamba3Config`, `n_heads` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/parallelize.py`](torchtitan/experiments/tpu/examples/mamba3/parallelize.md) | 1 | `parallelize_mamba3` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/tests/model_test.py`](torchtitan/experiments/tpu/examples/mamba3/tests/model_test.md) | 6 | `test_mimo_model`, `test_weight_tying`, `test_instantiation_and_forward` |  |
| [`torchtitan/experiments/tpu/examples/mamba3/tests/test_mamba3_pallas.py`](torchtitan/experiments/tpu/examples/mamba3/tests/test_mamba3_pallas.md) | 3 | `Mamba3PallasKernelTest`, `test_backward_gradient_computation`, `test_forward_shape_and_execution` |  |
| [`torchtitan/experiments/tpu/examples/tests/test_dilated_conv.py`](torchtitan/experiments/tpu/examples/tests/test_dilated_conv.md) | 3 | `TestTPUDilatedConv`, `naive_dilated_causal_conv`, `test_causal_dilated_conv_parity` |  |
| [`torchtitan/experiments/tpu/float8_converter.py`](torchtitan/experiments/tpu/float8_converter.md) | 8 | `TpuFloat8LinearConverter`, `Config`, `config` |  |
| [`torchtitan/experiments/tpu/flux/__init__.py`](torchtitan/experiments/tpu/flux/__init__.md) | 3 | `_upstream_flavor`, `flux_configs`, `__all__` |  |
| [`torchtitan/experiments/tpu/flux/config_registry.py`](torchtitan/experiments/tpu/flux/config_registry.md) | 2 | `_TEST_ASSETS`, `flux_testmodel` |  |
| [`torchtitan/experiments/tpu/flux/infra/parallelize.py`](torchtitan/experiments/tpu/flux/infra/parallelize.md) | 1 | `parallelize_flux` |  |
| [`torchtitan/experiments/tpu/gdist.py`](torchtitan/experiments/tpu/gdist.md) | 18 | `torchrun`, `default_nproc_per_node`, `default_nnodes` |  |
| [`torchtitan/experiments/tpu/gmain.py`](torchtitan/experiments/tpu/gmain.md) | 6 | `global_start_trainer_func`, `_start_trainer`, `main` |  |
| [`torchtitan/experiments/tpu/grad_norm.py`](torchtitan/experiments/tpu/grad_norm.md) | 8 | `clip_grad_norm_`, `CompiledGradNorm`, `GradSignature` |  |
| [`torchtitan/experiments/tpu/graph_trainer/config.py`](torchtitan/experiments/tpu/graph_trainer/config.md) | 33 | `memory_policy`, `TpuGraphTrainerCompileConfig`, `use_scan_layers` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/graph_split.py`](torchtitan/experiments/tpu/graph_trainer/graph_split.md) | 56 | `backward_graph`, `GraphSplitter`, `split_backward_graph_by_layer` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/layer_stack.py`](torchtitan/experiments/tpu/graph_trainer/layer_stack.md) | 49 | `STACK_ATTR`, `check_layers_are_stackable`, `layer_shapes` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.py`](torchtitan/experiments/tpu/graph_trainer/mfu_benchmark.md) | 8 | `final_step`, `start_step`, `record` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/muse_glimmer.py`](torchtitan/experiments/tpu/graph_trainer/muse_glimmer.md) | 2 | `model_registry`, `parallelize_muse_glimmer` |  |
| [`torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.py`](torchtitan/experiments/tpu/graph_trainer/passes/insert_combine_barriers.md) | 6 | `_TAG_VAL`, `apply_combine_barrier_pass`, `_has_tag` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.py`](torchtitan/experiments/tpu/graph_trainer/passes/reduce_scatter_allreduce.md) | 6 | `apply_selected_reduce_scatter_allreduce_pass`, `_WAIT_TENSOR`, `_find_reduce_scatter` |  |
| [`torchtitan/experiments/tpu/graph_trainer/qwen3.py`](torchtitan/experiments/tpu/graph_trainer/qwen3.md) | 7 | `model_registry`, `MaxTextTpuGraphTrainerQwen3Model`, `parallelize_qwen3` |  |
| [`torchtitan/experiments/tpu/graph_trainer/remat_schedule.py`](torchtitan/experiments/tpu/graph_trainer/remat_schedule.md) | 20 | `apply_tpu_remat_fsdp_all_gather_schedule`, `_optimization_barrier`, `apply_tpu_remat_schedule` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/scan_fsdp.py`](torchtitan/experiments/tpu/graph_trainer/scan_fsdp.md) | 24 | `plan_stacked_gathers`, `gather_slice`, `gather_dim` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/scan_guards.py`](torchtitan/experiments/tpu/graph_trainer/scan_guards.md) | 3 | `check_scan_was_applied`, `check_scan_parallelism`, `__all__` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.py`](torchtitan/experiments/tpu/graph_trainer/scan_remat_policy.md) | 17 | `scan_body_remat_window`, `_aten`, `_reached_from_counts` |  |
| [`torchtitan/experiments/tpu/graph_trainer/simple_fsdp.py`](torchtitan/experiments/tpu/graph_trainer/simple_fsdp.md) | 11 | `install_tpu_replicate_computation`, `TpuReplicateComputation`, `replicate_compute` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.py`](torchtitan/experiments/tpu/graph_trainer/split_cpu_offload.md) | 12 | `is_ao_transfer`, `HostDonorSpec`, `thread_host_offload_donors` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_graph_split.md) | 34 | `_trace_toy_model`, `_trace_cpu_offload_graph`, `_apply_passes_and_split` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack.md) | 49 | `_build`, `TOKENS`, `_toy_layer` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_distributed.md) | 22 | `_on_devices`, `a_sharded_stack_gathers_and_reduces_like_unrolled`, `_models` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_layer_stack_reshard_distributed.md) | 20 | `_process_group`, `_build`, `_round_trip` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_reduce_scatter_allreduce.md) | 15 | `_make_graph`, `_MAX_INPUT_BYTES`, `_QKV_PATTERN` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.md) | 32 | `_trace_simple_fsdp_remat_graph`, `moe`, `_Projection` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_funcol.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_funcol.md) | 5 | `test_patch_installed`, `TestFuncolMovedim`, `test_all_gather_transposes_onto_dim_zero` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_scan_fsdp_shard_dim.md) | 33 | `Q235_STACKS`, `_fake_pg`, `_holder` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_guards.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_scan_guards.md) | 14 | `_model`, `_parallelism`, `_layer` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.md) | 40 | `_run`, `EXPERTS`, `_legacy_window` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_simple_fsdp_distributed.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_simple_fsdp_distributed.md) | 5 | `nonleading_shard_matches_dtensor`, `_on_devices`, `TestTpuSimpleFSDP` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.md) | 20 | `_split`, `fn`, `make_test_tensor` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_config.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_config.md) | 87 | `_qwen3_graph_config`, `_qwen3_graph_flops`, `flattened_for` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md), [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_distributed.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_distributed.md) | 10 | `_train_args`, `TpuGraphTrainerDistributedTest`, `_MODELS` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_graph_trainer_unit.md) | 19 | `config_manager`, `DummyModule`, `config` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.md) | 24 | `graph`, `_mm`, `_gm` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload_distributed.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload_distributed.md) | 12 | `_OFFLOAD`, `_RELOAD`, `_check_offload_engaged` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py`](torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.md) | 83 | `_MoEToy`, `_trace_toy`, `_splash_cores` |  |
| [`torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.py`](torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.md) | 18 | `_annotate_internal_donations`, `construct_tpu_pass_pipeline`, `tpu_backend_compile_pass` | [graph-trainer](../concepts/graph-trainer.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.py`](torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md) | 29 | `TpuGraphTrainer`, `compile`, `Config` | [graph-trainer](../concepts/graph-trainer.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.py`](torchtitan/experiments/tpu/graph_trainer/tpu_host_offload.md) | 14 | `offload_scan_activations`, `_SCAN_HOP`, `walk` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py`](torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md) | 28 | `select_saves`, `resolve_save_regions`, `SaveRegion` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/grouped_experts.py`](torchtitan/experiments/tpu/grouped_experts.md) | 46 | `TpuGroupedExperts`, `Config`, `TpuGroupedExpertsConverter` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/headtail.py`](torchtitan/experiments/tpu/headtail.md) | 7 | `headtail_positions`, `headtail_chunk_order`, `make_cp_segment_ids` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/jax_profiler.py`](torchtitan/experiments/tpu/jax_profiler.md) | 6 | `prof`, `logger`, `JaxProfiler` |  |
| [`torchtitan/experiments/tpu/kernels/expert_segment_matmul.py`](torchtitan/experiments/tpu/kernels/expert_segment_matmul.md) | 7 | `segment_matmul_pallas_2d`, `_grouped_mm_bwd`, `_tiling` |  |
| [`torchtitan/experiments/tpu/kernels/fill_indices.py`](torchtitan/experiments/tpu/kernels/fill_indices.md) | 5 | `fill_indices`, `fill_indices_jax`, `segment_body` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.py`](torchtitan/experiments/tpu/kernels/fp8_expert_segment_matmul.md) | 44 | `Tiling`, `FWD_DTYPE`, `fp8_segment_matmul_pallas_2d` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/fp8_scale.py`](torchtitan/experiments/tpu/kernels/fp8_scale.md) | 2 | `scale_from_amax`, `MIN_SCALE` |  |
| [`torchtitan/experiments/tpu/kernels/gmm.py`](torchtitan/experiments/tpu/kernels/gmm.md) | 9 | `grouped_matrix_multiply`, `_get_gmm_kernels`, `_gmm_fwd_cache` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.py`](torchtitan/experiments/tpu/kernels/linear_softmax_ce_softcap_kernel.md) | 49 | `Array`, `Real`, `Integer` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.py`](torchtitan/experiments/tpu/kernels/linear_softmax_cross_entropy_loss.md) | 14 | `_get_loss_op_names`, `_has_logit_transform`, `linear_softmax_cross_entropy_loss` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/paired_segment_matmul.py`](torchtitan/experiments/tpu/kernels/paired_segment_matmul.md) | 30 | `paired_segment_matmul_pallas_2d`, `_paired_grouped_mm_bwd`, `_metadata` |  |
| [`torchtitan/experiments/tpu/kernels/pallas_naming.py`](torchtitan/experiments/tpu/kernels/pallas_naming.md) | 2 | `call_named`, `__all__` |  |
| [`torchtitan/experiments/tpu/kernels/route_score.py`](torchtitan/experiments/tpu/kernels/route_score.md) | 3 | `route_score_grad`, `_route_score_grad_tpu`, `__all__` |  |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/base.py`](torchtitan/experiments/tpu/kernels/sbd_splash/base.md) | 9 | `SegmentIds`, `DEFAULT_MASK_VALUE`, `kv` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.py`](torchtitan/experiments/tpu/kernels/sbd_splash/mask_export.md) | 2 | `_mask_kernel`, `dropout_keep_mask` |  |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/mlc_guard.py`](torchtitan/experiments/tpu/kernels/sbd_splash/mlc_guard.md) | 4 | `DEFAULT_CONST`, `OVER_MARGIN`, `UNDER_MARGIN` |  |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.py`](torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_kernel.md) | 136 | `use_base2_exp`, `SplashConfig`, `partial` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.py`](torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask.md) | 67 | `Mask`, `shape`, `shape` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.py`](torchtitan/experiments/tpu/kernels/sbd_splash/splash_attention_mask_info.md) | 27 | `block_mask`, `num_active_blocks`, `partial_mask_blocks` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/segment_matmul.py`](torchtitan/experiments/tpu/kernels/segment_matmul.md) | 10 | `segment_matmul_pallas_2d`, `_get_ops`, `_build_ragged_dot_kernels` |  |
| [`torchtitan/experiments/tpu/kernels/splash_attention.py`](torchtitan/experiments/tpu/kernels/splash_attention.md) | 31 | `splash_sdpa`, `_make_mask`, `_maybe_document_aware_mask_info` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/splash_bias_dropout.py`](torchtitan/experiments/tpu/kernels/splash_bias_dropout.md) | 45 | `sbd_splash_attention`, `SbdConfig`, `update` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/tests/test_expert_segment_matmul.py`](torchtitan/experiments/tpu/kernels/tests/test_expert_segment_matmul.md) | 4 | `integers`, `ExpertSegmentMatmulTest`, `test_dweight_is_stored_in_the_weight_dtype_and_rounds_once` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_fill_indices.py`](torchtitan/experiments/tpu/kernels/tests/test_fill_indices.md) | 15 | `fill_indices_cpu_original`, `tpeg`, `siv` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.py`](torchtitan/experiments/tpu/kernels/tests/test_fp8_expert_segment_matmul.md) | 28 | `_rel_err`, `_GROUP_SIZES`, `_to_dev` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/tests/test_fp8_scale.py`](torchtitan/experiments/tpu/kernels/tests/test_fp8_scale.md) | 6 | `_E4M3`, `_E5M2`, `test_normal_scales_are_amax_over_fmax` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_gmm.py`](torchtitan/experiments/tpu/kernels/tests/test_gmm.md) | 9 | `manual_gmm_reference`, `func`, `GMMTest` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_kernel_name_determinism_distributed.py`](torchtitan/experiments/tpu/kernels/tests/test_kernel_name_determinism_distributed.md) | 6 | `_get_kernel_names_in_subprocess`, `_TIMEOUT_SECONDS`, `_run_worker` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_linear_softmax_ce_softcap.py`](torchtitan/experiments/tpu/kernels/tests/test_linear_softmax_ce_softcap.md) | 12 | `_CAP`, `_FP32_UNCAPPED`, `_FP32` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_linear_softmax_cross_entropy_loss.py`](torchtitan/experiments/tpu/kernels/tests/test_linear_softmax_cross_entropy_loss.md) | 6 | `run_custom`, `LinearSoftmaxCrossEntropyLossTest`, `test_parity` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.py`](torchtitan/experiments/tpu/kernels/tests/test_paired_segment_matmul.md) | 12 | `_paired_vs_unpaired`, `_bounded_values`, `bounded_values` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_pallas_naming.py`](torchtitan/experiments/tpu/kernels/tests/test_pallas_naming.md) | 10 | `_copy`, `x`, `_lowered_text` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_route_score.py`](torchtitan/experiments/tpu/kernels/tests/test_route_score.md) | 3 | `RouteScoreTest`, `test_matches_fp32_reference`, `test_rejects_unsupported_contracts` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_segment_matmul.py`](torchtitan/experiments/tpu/kernels/tests/test_segment_matmul.md) | 7 | `_manual_segment_matmul_reference`, `SegmentMatmulTest`, `test_backward_parity` |  |
| [`torchtitan/experiments/tpu/kernels/tests/test_splash_attention.py`](torchtitan/experiments/tpu/kernels/tests/test_splash_attention.md) | 22 | `check_forward_parity`, `make_packed_inputs`, `test_document_aware_block_skipping_is_optional` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.py`](torchtitan/experiments/tpu/kernels/tests/test_splash_bias_dropout.md) | 37 | `_qkv`, `_sdpa_ref`, `_segment_ids_case` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.py`](torchtitan/experiments/tpu/kernels/tests/test_tokamax_splash_attention.md) | 22 | `check_forward_parity`, `_CP_SHARD_CASES`, `_DOCUMENTS` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/kernels/tokamax_splash_attention.py`](torchtitan/experiments/tpu/kernels/tokamax_splash_attention.md) | 39 | `splash_sdpa`, `TokamaxConfig`, `_make_mask` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/layer_loop.py`](torchtitan/experiments/tpu/layer_loop.md) | 8 | `TpuLayerLoop`, `builds_layer_loop`, `tpu_model_class` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/llama3/__init__.py`](torchtitan/experiments/tpu/llama3/__init__.md) | 4 | `llama3_configs`, `_testmodel`, `_upstream_flavor` |  |
| [`torchtitan/experiments/tpu/llama3/config_registry.py`](torchtitan/experiments/tpu/llama3/config_registry.md) | 18 | `llama3_70b`, `_REAL_ROPE_OVERRIDE`, `llama3_405b` | [checkpointing](../concepts/checkpointing.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/llama3/infra/parallelize.py`](torchtitan/experiments/tpu/llama3/infra/parallelize.md) | 1 | `parallelize_llama` |  |
| [`torchtitan/experiments/tpu/llama3/infra/pipeline.py`](torchtitan/experiments/tpu/llama3/infra/pipeline.md) | 1 | `pipeline_llama` |  |
| [`torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py`](torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.md) | 19 | `_get_model_config`, `TEST_BATCH_SIZE`, `apply_fsdp_wrapper` |  |
| [`torchtitan/experiments/tpu/llama3/tests/test_llama3.py`](torchtitan/experiments/tpu/llama3/tests/test_llama3.md) | 10 | `_get_model_config`, `init_linear_weights`, `Llama3Test` |  |
| [`torchtitan/experiments/tpu/local_tpu_device.py`](torchtitan/experiments/tpu/local_tpu_device.md) | 31 | `Info`, `TpuChip`, `V7X` |  |
| [`torchtitan/experiments/tpu/loss.py`](torchtitan/experiments/tpu/loss.md) | 18 | `PallasCrossEntropyLoss`, `Config`, `pallas_cross_entropy_loss` |  |
| [`torchtitan/experiments/tpu/mfu_flops.py`](torchtitan/experiments/tpu/mfu_flops.md) | 1 | `get_maxtext_decoder_nparams_and_flops` | [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/model_annotator.py`](torchtitan/experiments/tpu/model_annotator.md) | 5 | `wrap_model`, `make_post_hook`, `make_pre_hook` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/__init__.py`](torchtitan/experiments/tpu/muse_glimmer/__init__.md) | 9 | `model_registry`, `use_tpu_attention`, `muse_glimmer_configs` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/attention.py`](torchtitan/experiments/tpu/muse_glimmer/attention.md) | 13 | `SlidingWindowScaledDotProductInnerAttention`, `Config`, `window_size` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/muse_glimmer/config_registry.py`](torchtitan/experiments/tpu/muse_glimmer/config_registry.md) | 13 | `muse_glimmer_debugmodel_fused_ce`, `muse_glimmer_debugmodel`, `_enable_pallas_cross_entropy` | [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.py`](torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.md) | 4 | `configure_muse_glimmer_simple_fsdp_shard_dims`, `parallelize_muse_glimmer`, `_validate_supported` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py`](torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.md) | 20 | `_get_model_config`, `_run`, `TEST_BATCH_SIZE` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py`](torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.md) | 21 | `_get_model_config`, `_setup_module_cpu_device_from_config`, `_is_tpu` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.py`](torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer_config.md) | 32 | `_get_model_config`, `_build_fused_ce_model`, `_build_attention` |  |
| [`torchtitan/experiments/tpu/muse_glimmer/tests/test_simple_fsdp_sharding.py`](torchtitan/experiments/tpu/muse_glimmer/tests/test_simple_fsdp_sharding.md) | 10 | `_parallel_dims`, `_model`, `test_rejects_context_parallelism` |  |
| [`torchtitan/experiments/tpu/numerical_validation.py`](torchtitan/experiments/tpu/numerical_validation.md) | 27 | `capture_local_state`, `history`, `in_context` |  |
| [`torchtitan/experiments/tpu/overrides/bf16_rope.py`](torchtitan/experiments/tpu/overrides/bf16_rope.md) | 5 | `TpuActivationDtypeCosSinRoPE`, `Config`, `tpu_activation_dtype_cossin_rope` |  |
| [`torchtitan/experiments/tpu/overrides/discarded_token_counter.py`](torchtitan/experiments/tpu/overrides/discarded_token_counter.md) | 5 | `TpuDiscardedTokenCounterMoE`, `tpu_discarded_token_counter`, `Config` |  |
| [`torchtitan/experiments/tpu/overrides/fused_loss.py`](torchtitan/experiments/tpu/overrides/fused_loss.md) | 12 | `FusedLossLinearWrapper`, `Config`, `fused_loss_lm_head` |  |
| [`torchtitan/experiments/tpu/overrides/real_rope.py`](torchtitan/experiments/tpu/overrides/real_rope.md) | 6 | `TpuRealArithmeticComplexRoPE`, `apply_rotary_emb`, `tpu_real_arithmetic_complex_rope` |  |
| [`torchtitan/experiments/tpu/profiler_workaround.py`](torchtitan/experiments/tpu/profiler_workaround.md) | 10 | `init`, `_global_job_config`, `_original_enter` |  |
| [`torchtitan/experiments/tpu/qkv.py`](torchtitan/experiments/tpu/qkv.md) | 27 | `TpuPackedQKVLinear`, `Config`, `TpuPackedQKVConverter` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/qwen3/__init__.py`](torchtitan/experiments/tpu/qwen3/__init__.md) | 8 | `model_registry`, `qwen3_configs`, `_8b_tpu` |  |
| [`torchtitan/experiments/tpu/qwen3/config_registry.py`](torchtitan/experiments/tpu/qwen3/config_registry.md) | 49 | `qwen3_8b`, `qwen3_moe_30b_fsdp_only_full_ac_benchmark`, `qwen3_moe_235b_scan` | [checkpointing](../concepts/checkpointing.md), [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md), [job-config](../concepts/job-config.md), [model-spec-protocols](../concepts/model-spec-protocols.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md) |
| [`torchtitan/experiments/tpu/qwen3/infra/parallelize.py`](torchtitan/experiments/tpu/qwen3/infra/parallelize.md) | 1 | `parallelize_qwen3` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/qwen3/model.py`](torchtitan/experiments/tpu/qwen3/model.md) | 3 | `MaxTextQwen3Config`, `from_qwen3`, `get_nparams_and_flops` |  |
| [`torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py`](torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.md) | 14 | `_get_qwen3_model_config`, `TEST_BATCH_SIZE`, `TEST_SEQ_LEN` |  |
| [`torchtitan/experiments/tpu/qwen3/tests/test_qwen3.py`](torchtitan/experiments/tpu/qwen3/tests/test_qwen3.md) | 12 | `_get_model_config`, `FULL_MODEL_TEST_CONFIGS`, `setUp` |  |
| [`torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py`](torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.md) | 17 | `_placed_235b`, `_FakeParallelDims`, `_mesh` |  |
| [`torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.py`](torchtitan/experiments/tpu/qwen3/tests/test_simple_fsdp_sharding.md) | 13 | `_model`, `_parallel_dims`, `_wrapped_model` |  |
| [`torchtitan/experiments/tpu/qwen3_5/__init__.py`](torchtitan/experiments/tpu/qwen3_5/__init__.md) | 4 | `model_registry`, `use_tpu_modules`, `_CONV1D_INIT` |  |
| [`torchtitan/experiments/tpu/qwen3_5/attn_gym_stub.py`](torchtitan/experiments/tpu/qwen3_5/attn_gym_stub.md) | 4 | `_module`, `_stub_op`, `_name` |  |
| [`torchtitan/experiments/tpu/qwen3_5/config_registry.py`](torchtitan/experiments/tpu/qwen3_5/config_registry.md) | 4 | `_TPU_MOE_CONVERTERS`, `qwen35_moe_35b`, `qwen35_debugmodel` | [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/qwen3_5/gated_delta.py`](torchtitan/experiments/tpu/qwen3_5/gated_delta.md) | 17 | `_causal_conv`, `chunked_gated_delta`, `TpuGatedDeltaNet` |  |
| [`torchtitan/experiments/tpu/qwen3_5/infra/parallelize.py`](torchtitan/experiments/tpu/qwen3_5/infra/parallelize.md) | 1 | `parallelize_qwen3_5` |  |
| [`torchtitan/experiments/tpu/qwen3_5/model.py`](torchtitan/experiments/tpu/qwen3_5/model.md) | 6 | `TpuQwen35Attention`, `TpuQwen35TransformerBlock`, `Config` |  |
| [`torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py`](torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.md) | 20 | `_is_tpu`, `_relative_l2_error`, `_packed_positions` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/qwen3_sharding.py`](torchtitan/experiments/tpu/qwen3_sharding.md) | 2 | `configure_qwen_simple_fsdp_shard_dims`, `__all__` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/remat_regions.py`](torchtitan/experiments/tpu/remat_regions.md) | 4 | `MOE_ROUTING`, `REMAT_REGION`, `annotate_region` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/rl_nc_ray/__init__.py`](torchtitan/experiments/tpu/rl_nc_ray/__init__.md) | 14 | `real_file`, `monarch_actor`, `monarch_spmd` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/actor.py`](torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/actor.md) | 11 | `RankProxy`, `current_rank`, `Actor` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/rdma.py`](torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/rdma.md) | 1 | `is_rdma_available` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/spmd.py`](torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/monarch/spmd.md) | 1 | `setup_torch_elastic_env_async` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/torchstore/__init__.py`](torchtitan/experiments/tpu/rl_nc_ray/dummy_modules/torchstore/__init__.md) | 4 | `LocalRankStrategy`, `get_state_dict`, `initialize` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/generator.py`](torchtitan/experiments/tpu/rl_nc_ray/generator.md) | 28 | `generator`, `logger`, `stop_profile` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/grpo.py`](torchtitan/experiments/tpu/rl_nc_ray/grpo.md) | 38 | `ray_generator`, `call`, `setup_async` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.py`](torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.md) | 6 | `patch_varlen_attention`, `padded_create_varlen_metadata`, `cpu_varlen_forward` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/scripts/plot_metrics_from_log.py`](torchtitan/experiments/tpu/rl_nc_ray/scripts/plot_metrics_from_log.md) | 4 | `parser`, `args`, `plot_metrics` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/tests/test_mini_rl.py`](torchtitan/experiments/tpu/rl_nc_ray/tests/test_mini_rl.md) | 20 | `rank`, `actors`, `model` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/tests/test_varlen_attn_tpu.py`](torchtitan/experiments/tpu/rl_nc_ray/tests/test_varlen_attn_tpu.md) | 2 | `compiled_varlen_attn`, `run_repro` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.py`](torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.md) | 13 | `GENERATOR_BASE_PORT`, `JAX_MEM_FRACTION`, `JAX_THREE_G_MEM_ALLOC_ON_FREE` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/trainer.py`](torchtitan/experiments/tpu/rl_nc_ray/trainer.md) | 15 | `profiler`, `RayTPUPolicyTrainer`, `_build_model` | [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py`](torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.md) | 14 | `vllm_codegen`, `e`, `vllm_compilation` |  |
| [`torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.py`](torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.md) | 11 | `get_clean_name`, `logger`, `load_weights_on_driver` |  |
| [`torchtitan/experiments/tpu/scan_backward_patch.py`](torchtitan/experiments/tpu/scan_backward_patch.md) | 26 | `apply_scan_reverse_backward_patch`, `_UPSTREAM_CALL_BACKWARD`, `_ReverseByIndex` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/spmd_utils.py`](torchtitan/experiments/tpu/spmd_utils.md) | 3 | `apply_spmd_safe`, `spmd_safe`, `e` |  |
| [`torchtitan/experiments/tpu/test_utils.py`](torchtitan/experiments/tpu/test_utils.md) | 15 | `check_equivalence`, `_skip_if_device`, `resolve_device_type` |  |
| [`torchtitan/experiments/tpu/tests/test_bf16_rope.py`](torchtitan/experiments/tpu/tests/test_bf16_rope.md) | 3 | `test_override_preserves_config_and_builds_tpu_rope`, `test_forward_matches_explicit_bf16_rotation`, `TpuActivationDtypeCosSinRoPETest` |  |
| [`torchtitan/experiments/tpu/tests/test_bld_layout.py`](torchtitan/experiments/tpu/tests/test_bld_layout.md) | 23 | `_build_pair`, `_HEAD_DIM`, `_DIM` |  |
| [`torchtitan/experiments/tpu/tests/test_checkpoint_verification_distributed.py`](torchtitan/experiments/tpu/tests/test_checkpoint_verification_distributed.md) | 8 | `patched_init`, `TrainCheckpointVerificationTest`, `StartTrainerWithLossCapture` |  |
| [`torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py`](torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.md) | 55 | `_check`, `_gke_env`, `_env` |  |
| [`torchtitan/experiments/tpu/tests/test_compiled_grad_norm_distributed.py`](torchtitan/experiments/tpu/tests/test_compiled_grad_norm_distributed.md) | 9 | `_run_clip_parity`, `CompiledGradNormDistributedTest`, `make_parameters` |  |
| [`torchtitan/experiments/tpu/tests/test_cp_attention.py`](torchtitan/experiments/tpu/tests/test_cp_attention.md) | 86 | `_config`, `rank`, `world_size` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/experiments/tpu/tests/test_datasets.py`](torchtitan/experiments/tpu/tests/test_datasets.md) | 5 | `test_c4_dataset_path_replaces_source_path`, `test_c4_keeps_upstream_source`, `test_c4_test_dataset_path_merges_kwargs` |  |
| [`torchtitan/experiments/tpu/tests/test_device_module.py`](torchtitan/experiments/tpu/tests/test_device_module.md) | 11 | `_set_accelerator`, `_fake_tpu_module`, `_fake_accelerator` |  |
| [`torchtitan/experiments/tpu/tests/test_discarded_token_counter.py`](torchtitan/experiments/tpu/tests/test_discarded_token_counter.md) | 10 | `_DIM`, `_moe_config`, `_TOKENS` |  |
| [`torchtitan/experiments/tpu/tests/test_dtensor_distributed.py`](torchtitan/experiments/tpu/tests/test_dtensor_distributed.md) | 57 | `HIDDEN_SIZE`, `SEQ_LEN`, `BATCH_SIZE` |  |
| [`torchtitan/experiments/tpu/tests/test_float8_converter.py`](torchtitan/experiments/tpu/tests/test_float8_converter.md) | 8 | `_converted`, `test_emulated_layer_matches_linear`, `test_converts_all_linears_except_filtered` |  |
| [`torchtitan/experiments/tpu/tests/test_layer_loop.py`](torchtitan/experiments/tpu/tests/test_layer_loop.md) | 33 | `_stock_config`, `_convert`, `_tpu_model` |  |
| [`torchtitan/experiments/tpu/tests/test_mfu_flops.py`](torchtitan/experiments/tpu/tests/test_mfu_flops.md) | 11 | `_build`, `test_maxtext_qwen3_config_reports_maxtext_flops`, `test_qwen3_model_config_reports_torchtitan_flops` |  |
| [`torchtitan/experiments/tpu/tests/test_model_distributed.py`](torchtitan/experiments/tpu/tests/test_model_distributed.md) | 4 | `_run_model_distributed`, `Qwen3DTensorParallelizeTest`, `setup_logger` |  |
| [`torchtitan/experiments/tpu/tests/test_profiler.py`](torchtitan/experiments/tpu/tests/test_profiler.md) | 2 | `ProfilerAcceleratorTest`, `test_profiler_runs_and_outputs_traces` |  |
| [`torchtitan/experiments/tpu/tests/test_real_rope.py`](torchtitan/experiments/tpu/tests/test_real_rope.md) | 14 | `rope_cache`, `_scan_rope_backward`, `query` |  |
| [`torchtitan/experiments/tpu/tests/test_scan_backward_patch.py`](torchtitan/experiments/tpu/tests/test_scan_backward_patch.md) | 29 | `_backward`, `_install_fake_bump`, `_SCAN_MODULE` |  |
| [`torchtitan/experiments/tpu/tests/test_token_dispatcher.py`](torchtitan/experiments/tpu/tests/test_token_dispatcher.md) | 24 | `dispatcher`, `run`, `step` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/tests/test_tpu_flags.py`](torchtitan/experiments/tpu/tests/test_tpu_flags.md) | 37 | `_FakeConfig`, `libtpu_init_flags`, `extra_libtpu_init_flags` |  |
| [`torchtitan/experiments/tpu/tests/test_train_distributed.py`](torchtitan/experiments/tpu/tests/test_train_distributed.md) | 2 | `TrainDistributedTest`, `test_train_distributed` |  |
| [`torchtitan/experiments/tpu/tests/test_train_minimal_distributed.py`](torchtitan/experiments/tpu/tests/test_train_minimal_distributed.md) | 2 | `TrainMinimalDistributedTest`, `test_train_minimal_distributed_parity` |  |
| [`torchtitan/experiments/tpu/tests/test_workarounds.py`](torchtitan/experiments/tpu/tests/test_workarounds.md) | 46 | `_tokamax_patch_fixture`, `fake_redistribute`, `attn` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/token_dispatcher.py`](torchtitan/experiments/tpu/token_dispatcher.md) | 34 | `TpuAllToAllTokenDispatcher`, `Config`, `TpuTokenDispatcherConverter` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/tpu_flags.py`](torchtitan/experiments/tpu/tpu_flags.md) | 24 | `FlagMap`, `merge_flags`, `apply_init_flags` | [jax-lane](../concepts/jax-lane.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/tpu_job_config.py`](torchtitan/experiments/tpu/tpu_job_config.md) | 75 | `TPUTrainerConfig`, `compile`, `splash_attention_kernel` | [jax-lane](../concepts/jax-lane.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/tpu/train.py`](torchtitan/experiments/tpu/train.md) | 10 | `start_trainer`, `TPUTrainer`, `_compiled_grad_norm` | [flux-diffusion-model](../concepts/flux-diffusion-model.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/tpu/train_minimal.py`](torchtitan/experiments/tpu/train_minimal.md) | 30 | `model`, `logger`, `parallel_dims` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/__init__.py`](torchtitan/experiments/tpu/transformers_modeling_backend/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.py`](torchtitan/experiments/tpu/transformers_modeling_backend/_meta_init.md) | 3 | `params_meta_buffers_real`, `register_parameter`, `to_empty_keep_buffers` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/_structure.py`](torchtitan/experiments/tpu/transformers_modeling_backend/_structure.md) | 23 | `_resolve`, `find_head`, `find_embedding` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/attention.py`](torchtitan/experiments/tpu/transformers_modeling_backend/attention.md) | 24 | `_segment_ids`, `_kernel_kwargs`, `_reported` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md) |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.py`](torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md) | 20 | `_tpu_hf_config`, `_DEFAULT_HF_MODEL`, `_TPU_FLAVORS` | [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/job_config.py`](torchtitan/experiments/tpu/transformers_modeling_backend/job_config.md) | 3 | `TPUTransformersBackendConfig`, `hf_model`, `hf_config_overrides` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/model.py`](torchtitan/experiments/tpu/transformers_modeling_backend/model.md) | 48 | `_added_lm_head`, `_part`, `TPUHFTransformerModel` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.py`](torchtitan/experiments/tpu/transformers_modeling_backend/parallelize.md) | 3 | `parallelize_hf_transformers_tpu`, `_defer_parametrization_during_init`, `init_states` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/lane_args.py`](torchtitan/experiments/tpu/transformers_modeling_backend/tests/lane_args.md) | 3 | `lane_config_args`, `MODULE`, `CPU_REFERENCE` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.py`](torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_attention_masks.md) | 22 | `_module`, `_POSITIONS`, `_ours` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_hf_backend_distributed.py`](torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_hf_backend_distributed.md) | 4 | `_PORTABLE_TOL`, `_KERNEL_TOL`, `HFBackendDistributedTest` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_hf_reference_parity.py`](torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_hf_reference_parity.md) | 8 | `one_step_vs_reference`, `setUp`, `HFReferenceParityTest` |  |
| [`torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_pallas_experts.py`](torchtitan/experiments/tpu/transformers_modeling_backend/tests/test_pallas_experts.md) | 10 | `PallasExpertsTest`, `TokenDispatcherTest`, `_rel_err` |  |
| [`torchtitan/experiments/tpu/unflatten_shim.py`](torchtitan/experiments/tpu/unflatten_shim.md) | 9 | `set_unflatten_seq_len`, `get_unflatten_seq_len`, `unflatten_tensor` |  |
| [`torchtitan/experiments/tpu/utils.py`](torchtitan/experiments/tpu/utils.md) | 2 | `ptd_checkpoint_wrapper_with_early_stop`, `__all__` |  |
| [`torchtitan/experiments/tpu/workarounds.py`](torchtitan/experiments/tpu/workarounds.md) | 31 | `use_cpu_safe_histc_patch`, `use_output_projection_patch`, `use_tokamax_splash_attention_patch` | [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md) |
| [`torchtitan/experiments/transformers_modeling_backend/__init__.py`](torchtitan/experiments/transformers_modeling_backend/__init__.md) | 27 | `model_registry`, `TitanMoeModelConfig`, `TitanModelConfig` |  |
| [`torchtitan/experiments/transformers_modeling_backend/config_registry.py`](torchtitan/experiments/transformers_modeling_backend/config_registry.md) | 10 | `TransformersBackendConfig`, `hf_model`, `transformers_modeling_backend_debugmodel` |  |
| [`torchtitan/experiments/transformers_modeling_backend/hf_sharding.py`](torchtitan/experiments/transformers_modeling_backend/hf_sharding.md) | 17 | `_hf_activation_placement`, `_hf_sequence_parallel_placement`, `CP` |  |
| [`torchtitan/experiments/transformers_modeling_backend/model.py`](torchtitan/experiments/transformers_modeling_backend/model.md) | 86 | `model`, `HFTransformerModel`, `Config` |  |
| [`torchtitan/experiments/transformers_modeling_backend/module_conversion.py`](torchtitan/experiments/transformers_modeling_backend/module_conversion.md) | 3 | `convert_hf_to_module`, `_make_module_class`, `_module_class_cache` |  |
| [`torchtitan/experiments/transformers_modeling_backend/moe_replacement.py`](torchtitan/experiments/transformers_modeling_backend/moe_replacement.md) | 16 | `_probe_hf_moe_block`, `_build_moe_config`, `_get_expert_param_info` |  |
| [`torchtitan/experiments/transformers_modeling_backend/parallelize.py`](torchtitan/experiments/transformers_modeling_backend/parallelize.md) | 6 | `parallelize_hf_transformers`, `apply_fsdp`, `_wrap_flex_kernel_cp` |  |
| [`torchtitan/experiments/transformers_modeling_backend/pipeline.py`](torchtitan/experiments/transformers_modeling_backend/pipeline.md) | 5 | `pipeline_hf_transformers`, `_build_stage_from_modules`, `pipeline_module_split` |  |
| [`torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.py`](torchtitan/experiments/transformers_modeling_backend/state_dict_adapter.md) | 12 | `_expert_names`, `_TITAN_EXPERTS_PREFIX`, `HFTransformerStateDictAdapter` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.py`](torchtitan/experiments/transformers_modeling_backend/tests/cp_pp_numerical.md) | 12 | `_run_case`, `_compare`, `_torchrun` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/integration_tests.py`](torchtitan/experiments/transformers_modeling_backend/tests/integration_tests.md) | 3 | `build_transformers_modeling_backend_test_list`, `_TEST_SUITES_FUNCTION`, `main` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/test_flex_attention.py`](torchtitan/experiments/transformers_modeling_backend/tests/test_flex_attention.md) | 4 | `test_block_causal_builds`, `test_packed_documents_do_not_leak`, `TestAttnMaskTypeValidation` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/test_flex_cp_numerical.py`](torchtitan/experiments/transformers_modeling_backend/tests/test_flex_cp_numerical.md) | 2 | `build_model`, `main` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/test_hf_build_forward_inputs.py`](torchtitan/experiments/transformers_modeling_backend/tests/test_hf_build_forward_inputs.md) | 6 | `_run`, `annotate`, `prepare` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py`](torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.md) | 37 | `_create_tiny_qwen3moe_model`, `_prepare_layers`, `_moe_buffer` |  |
| [`torchtitan/experiments/transformers_modeling_backend/tokenizer.py`](torchtitan/experiments/transformers_modeling_backend/tokenizer.md) | 8 | `HFBackendTokenizer`, `Config`, `apply_chat_template` |  |

## `torchtitan/hf_datasets`

Index: [`symbols/torchtitan-hf_datasets.tsv`](symbols/torchtitan-hf_datasets.tsv) (89 rows), [`edges/torchtitan-hf_datasets.tsv`](edges/torchtitan-hf_datasets.tsv) (244 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/hf_datasets/multimodal/mm_collator.py`](torchtitan/hf_datasets/multimodal/mm_collator.md) | 22 | `MultiModalCollator`, `Config`, `build_mrope_positions` | [hf-datasets](../concepts/hf-datasets.md) |
| [`torchtitan/hf_datasets/multimodal/mm_datasets.py`](torchtitan/hf_datasets/multimodal/mm_datasets.md) | 33 | `MM_DATASETS`, `MultiModalProcessor`, `Config` | [hf-datasets](../concepts/hf-datasets.md) |
| [`torchtitan/hf_datasets/multimodal/utils/image.py`](torchtitan/hf_datasets/multimodal/utils/image.md) | 7 | `resize_to_pixel_budget`, `resize_to_navit_patch_grid`, `process_image` | [hf-datasets](../concepts/hf-datasets.md) |
| [`torchtitan/hf_datasets/multimodal/utils/text.py`](torchtitan/hf_datasets/multimodal/utils/text.md) | 3 | `insert_vision_placeholders`, `pad_batch_dim`, `pad_seq_len` |  |
| [`torchtitan/hf_datasets/multimodal/utils/video.py`](torchtitan/hf_datasets/multimodal/utils/video.md) | 2 | `load_video`, `process_video` |  |
| [`torchtitan/hf_datasets/text_datasets.py`](torchtitan/hf_datasets/text_datasets.md) | 22 | `DATASETS`, `ChatProcessor`, `Config` | [hf-datasets](../concepts/hf-datasets.md) |

## `torchtitan/models`

Index: [`symbols/torchtitan-models.tsv`](symbols/torchtitan-models.tsv) (2682 rows), [`edges/torchtitan-models.tsv`](edges/torchtitan-models.tsv) (9586 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/models/__init__.py`](torchtitan/models/__init__.md) | 1 | `_supported_models` |  |
| [`torchtitan/models/common/__init__.py`](torchtitan/models/common/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/models/common/attention.py`](torchtitan/models/common/attention.md) | 108 | `FlexInnerAttention`, `AttentionMasksType`, `VarlenInnerAttention` | [deepseek-v4-model](../concepts/deepseek-v4-model.md), [gpt-oss-model](../concepts/gpt-oss-model.md), [model-building-blocks](../concepts/model-building-blocks.md), [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/models/common/aux_loss.py`](torchtitan/models/common/aux_loss.md) | 25 | `AuxLoss`, `set_step_denominator`, `coeff` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/config_utils.py`](torchtitan/models/common/config_utils.md) | 22 | `decoder_vocab_size`, `DEFAULT_DEBUG_MODEL_SEQ_LEN`, `TpGemmBackend` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/cp_attention.py`](torchtitan/models/common/cp_attention.md) | 16 | `KVAllGatherCPFlexInnerAttention`, `CPInnerAttention`, `UlyssesCPFlexInnerAttention` | [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) |
| [`torchtitan/models/common/decoder.py`](torchtitan/models/common/decoder.md) | 37 | `layers`, `tok_embeddings`, `lm_head` | [deepseek-v4-model](../concepts/deepseek-v4-model.md), [kimi-k2-7-model](../concepts/kimi-k2-7-model.md), [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/decoder_sharding.py`](torchtitan/models/common/decoder_sharding.md) | 19 | `dense_activation_placement`, `dense_param_placement`, `dense_sequence_parallel_placement` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/dist_gemm.py`](torchtitan/models/common/dist_gemm.md) | 15 | `_warn_once_unfused`, `DistGEMMFeedForward`, `_tp_group_from_context` |  |
| [`torchtitan/models/common/embedding.py`](torchtitan/models/common/embedding.md) | 9 | `Embedding`, `embedding_dim`, `Config` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/feed_forward.py`](torchtitan/models/common/feed_forward.md) | 18 | `FeedForward`, `Config`, `w1` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/linear.py`](torchtitan/models/common/linear.md) | 19 | `Linear`, `Config`, `out_features` | [config-overrides](../concepts/config-overrides.md), [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/moe.py`](torchtitan/models/common/moe.md) | 93 | `MoE`, `Config`, `hidden_dim` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/moe_sharding.py`](torchtitan/models/common/moe_sharding.md) | 16 | `set_moe_sharding_config`, `_tokens_per_expert_placement`, `CP` |  |
| [`torchtitan/models/common/multimodal.py`](torchtitan/models/common/multimodal.md) | 4 | `get_vision_positions`, `scatter_vision_embeds`, `gather_vision_embeds` |  |
| [`torchtitan/models/common/nn_modules.py`](torchtitan/models/common/nn_modules.md) | 48 | `RMSNorm`, `Config`, `normalized_shape` | [flux-diffusion-model](../concepts/flux-diffusion-model.md), [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/param_init.py`](torchtitan/models/common/param_init.md) | 2 | `depth_scaled_std`, `skip_param_init` |  |
| [`torchtitan/models/common/rope.py`](torchtitan/models/common/rope.md) | 40 | `dim`, `max_context_length`, `theta` | [config-overrides](../concepts/config-overrides.md), [deepseek-v3-model](../concepts/deepseek-v3-model.md), [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/common/token_dispatcher.py`](torchtitan/models/common/token_dispatcher.md) | 92 | `ep_mesh`, `AllToAllTokenDispatcher`, `num_experts` | [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md) |
| [`torchtitan/models/common/vision_encoder.py`](torchtitan/models/common/vision_encoder.md) | 43 | `VisionTransformerBlock`, `Config`, `attn` |  |
| [`torchtitan/models/common/vision_encoder_sharding.py`](torchtitan/models/common/vision_encoder_sharding.md) | 11 | `_vision_activation_placement`, `invariant_norm_config`, `vision_invariant_linear_config` | [model-building-blocks](../concepts/model-building-blocks.md) |
| [`torchtitan/models/deepseek_v3/__init__.py`](torchtitan/models/deepseek_v3/__init__.md) | 19 | `model_registry`, `_NORM_INIT`, `_build_dsv3_layers` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/config_registry.py`](torchtitan/models/deepseek_v3/config_registry.md) | 12 | `deepseek_v3_debugmodel`, `deepseek_v3_16b`, `deepseek_v3_671b` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/model.py`](torchtitan/models/deepseek_v3/model.md) | 58 | `DeepSeekV3Model`, `Config`, `dim` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/mtp.py`](torchtitan/models/deepseek_v3/mtp.md) | 34 | `mtp_layers`, `MTPDecoder`, `mtp_layers` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/parallelize.py`](torchtitan/models/deepseek_v3/parallelize.md) | 1 | `parallelize_deepseekv3` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/sharding.py`](torchtitan/models/deepseek_v3/sharding.md) | 4 | `_set_deepseek_v3_layer_sharding`, `set_deepseek_v3_sharding_config`, `_set_deepseek_v3_mtp_sharding` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v3/state_dict_adapter.py`](torchtitan/models/deepseek_v3/state_dict_adapter.md) | 9 | `DeepSeekV3StateDictAdapter`, `from_hf_map`, `from_hf` | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| [`torchtitan/models/deepseek_v4/__init__.py`](torchtitan/models/deepseek_v4/__init__.md) | 21 | `_NORM_INIT`, `_LINEAR_INIT`, `_HC_INIT` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/attention.py`](torchtitan/models/deepseek_v4/attention.md) | 83 | `DSV4FlexInnerAttention`, `Config`, `inner_attention` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/compressor.py`](torchtitan/models/deepseek_v4/compressor.md) | 43 | `Config`, `Compressor`, `Indexer` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/config_registry.py`](torchtitan/models/deepseek_v4/config_registry.md) | 4 | `deepseek_v4_debugmodel`, `deepseek_v4_flash`, `deepseek_v4_pro` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/mhc.py`](torchtitan/models/deepseek_v4/mhc.md) | 42 | `Config`, `HcHead`, `hc_mult` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/model.py`](torchtitan/models/deepseek_v4/model.md) | 41 | `DeepSeekV4TransformerBlock`, `DeepSeekV4Model`, `mtp_layers` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/moe.py`](torchtitan/models/deepseek_v4/moe.md) | 17 | `layer_id`, `hash`, `Config` |  |
| [`torchtitan/models/deepseek_v4/mtp.py`](torchtitan/models/deepseek_v4/mtp.md) | 17 | `Config`, `e_proj`, `enorm` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/sharding.py`](torchtitan/models/deepseek_v4/sharding.md) | 17 | `_dense_param_rep`, `_replicate_weight`, `set_compressor_sharding` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/deepseek_v4/state_dict_adapter.py`](torchtitan/models/deepseek_v4/state_dict_adapter.md) | 14 | `from_hf_map`, `_abstract_key`, `num_main_layers` | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| [`torchtitan/models/flux/__init__.py`](torchtitan/models/flux/__init__.md) | 15 | `model_registry`, `_XAVIER_LINEAR`, `_ZERO_LINEAR` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/config_registry.py`](torchtitan/models/flux/config_registry.md) | 7 | `_flux_dataset`, `_flux_seq_len`, `flux_debugmodel` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/configs.py`](torchtitan/models/flux/configs.md) | 15 | `SamplingConfig`, `classifier_free_guidance_scale`, `denoising_steps` |  |
| [`torchtitan/models/flux/flux_datasets.py`](torchtitan/models/flux/flux_datasets.md) | 36 | `dataset`, `FluxValidationDatasetConfig`, `Config` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/inference/infer.py`](torchtitan/models/flux/inference/infer.md) | 3 | `inference`, `config`, `config_manager` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/inference/sampling.py`](torchtitan/models/flux/inference/sampling.md) | 6 | `generate_image`, `save_image`, `denoise` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/model/autoencoder.py`](torchtitan/models/flux/model/autoencoder.md) | 112 | `AutoEncoder`, `out_channels`, `in_channels` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/model/hf_embedder.py`](torchtitan/models/flux/model/hf_embedder.md) | 12 | `FluxEmbedder`, `version`, `Config` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/model/layers.py`](torchtitan/models/flux/model/layers.md) | 131 | `Config`, `MLPEmbedder`, `hidden_size` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/model/model.py`](torchtitan/models/flux/model/model.md) | 42 | `FluxModel`, `Config`, `double_blocks` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/model/state_dict_adapter.py`](torchtitan/models/flux/model/state_dict_adapter.md) | 10 | `combination_plan`, `FluxStateDictAdapter`, `from_hf_map_direct` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/parallelize.py`](torchtitan/models/flux/parallelize.md) | 8 | `parallelize_flux`, `parallelize_encoders`, `apply_compile` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/precomputed_loader.py`](torchtitan/models/flux/precomputed_loader.md) | 8 | `files`, `max_steps`, `PrecomputedDataloader` |  |
| [`torchtitan/models/flux/random_loader.py`](torchtitan/models/flux/random_loader.md) | 12 | `batches`, `bsz`, `RandomDataloader` |  |
| [`torchtitan/models/flux/sharding.py`](torchtitan/models/flux/sharding.md) | 6 | `CP`, `DP`, `set_flux_sharding_config` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/tokenizer.py`](torchtitan/models/flux/tokenizer.md) | 30 | `FluxTokenizerContainer`, `encode`, `Config` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/trainer.py`](torchtitan/models/flux/trainer.md) | 13 | `FluxTrainer`, `Config`, `tokenizer` | [flux-diffusion-model](../concepts/flux-diffusion-model.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan/models/flux/utils.py`](torchtitan/models/flux/utils.md) | 9 | `PATCH_HEIGHT`, `PATCH_WIDTH`, `IMAGE_LATENT_SIZE_RATIO` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/flux/validate.py`](torchtitan/models/flux/validate.md) | 29 | `Config`, `dataloader`, `FluxValidator` | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| [`torchtitan/models/gpt_oss/__init__.py`](torchtitan/models/gpt_oss/__init__.md) | 13 | `model_registry`, `gptoss_configs`, `_NORM_INIT` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/config_registry.py`](torchtitan/models/gpt_oss/config_registry.md) | 5 | `gpt_oss_debugmodel`, `_gpt_oss_debugmodel`, `gpt_oss_debugmodel_flex` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/model.py`](torchtitan/models/gpt_oss/model.md) | 44 | `GptOssModel`, `Config`, `Attention` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/moe.py`](torchtitan/models/gpt_oss/moe.md) | 18 | `Config`, `GptOssGroupedExperts`, `GptOssMoE` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/parallelize.py`](torchtitan/models/gpt_oss/parallelize.md) | 3 | `parallelize_gptoss`, `_raise_dynamo_recompile_limit`, `_has_sliding_window_attention` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/sharding.py`](torchtitan/models/gpt_oss/sharding.md) | 4 | `_set_gpt_oss_layer_sharding`, `scaled_bias_rowwise_config`, `set_gpt_oss_sharding_config` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/gpt_oss/state_dict_adapter.py`](torchtitan/models/gpt_oss/state_dict_adapter.md) | 8 | `GptOssStateDictAdapter`, `_expert_bias_templates`, `from_hf_map` | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| [`torchtitan/models/kimi_k2_7/__init__.py`](torchtitan/models/kimi_k2_7/__init__.md) | 23 | `model_registry`, `_NORM_INIT`, `_vision_encoder_config` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/config_registry.py`](torchtitan/models/kimi_k2_7/config_registry.md) | 11 | `_dist_muon_optimizer`, `_KimiTrainerConfig`, `kimi_k2_5_debugmodel` | [flex-shard](../concepts/flex-shard.md), [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/model.py`](torchtitan/models/kimi_k2_7/model.md) | 10 | `KimiK25Model`, `Config`, `vision_encoder` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/parallelize.py`](torchtitan/models/kimi_k2_7/parallelize.md) | 1 | `parallelize_kimi_k2_5` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/qk_clip.py`](torchtitan/models/kimi_k2_7/qk_clip.md) | 14 | `QKClipFlexInnerAttention`, `Config`, `_clip_mla_weights` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/sharding.py`](torchtitan/models/kimi_k2_7/sharding.md) | 6 | `_shard_decoder_after_embedding_scatter`, `_set_vision_encoder_sharding`, `set_kimi_k2_5_sharding_config` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/state_dict_adapter.py`](torchtitan/models/kimi_k2_7/state_dict_adapter.md) | 8 | `vision_encoder`, `vision_from_hf_map`, `KimiK25StateDictAdapter` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k2_7/vision_encoder.py`](torchtitan/models/kimi_k2_7/vision_encoder.md) | 71 | `MoonViTEncoder`, `rotary_pos_emb`, `Config` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| [`torchtitan/models/kimi_k3/__init__.py`](torchtitan/models/kimi_k3/__init__.md) | 23 | `_linear`, `_norm`, `_NORM_INIT` | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md), [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/config_registry.py`](torchtitan/models/kimi_k3/config_registry.md) | 2 | `kimi_k3_debugmodel`, `_kimi_k3_multimodal_dataloader` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/kda.py`](torchtitan/models/kimi_k3/kda.md) | 62 | `num_heads`, `head_dim`, `Config` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/model.py`](torchtitan/models/kimi_k3/model.md) | 82 | `KimiK3Model`, `delta_attention`, `layers` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/moe.py`](torchtitan/models/kimi_k3/moe.md) | 27 | `Config`, `Config`, `KimiFeedForward` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/parallelize.py`](torchtitan/models/kimi_k3/parallelize.md) | 1 | `parallelize_kimi_k3` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/sharding.py`](torchtitan/models/kimi_k3/sharding.md) | 4 | `DP`, `_set_inner_kda_sharding`, `set_kimi_k3_sharding_config` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/state_dict_adapter.py`](torchtitan/models/kimi_k3/state_dict_adapter.md) | 10 | `kimi_config`, `from_hf_map`, `KimiK3StateDictAdapter` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/kimi_k3/vision_encoder.py`](torchtitan/models/kimi_k3/vision_encoder.md) | 20 | `KimiK3VisionEncoder`, `Config`, `Config` | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| [`torchtitan/models/llama3/__init__.py`](torchtitan/models/llama3/__init__.md) | 16 | `model_registry`, `llama3_configs`, `_build_llama3_layers` | [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/llama3/config_registry.py`](torchtitan/models/llama3/config_registry.md) | 17 | `llama3_debugmodel`, `llama3_8b`, `llama3_mxfp8_linear_converter_config` | [data-loading](../concepts/data-loading.md), [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md), [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/llama3/model.py`](torchtitan/models/llama3/model.md) | 14 | `Llama3Model`, `Config`, `dim` | [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/llama3/parallelize.py`](torchtitan/models/llama3/parallelize.md) | 1 | `parallelize_llama` | [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/llama3/sharding.py`](torchtitan/models/llama3/sharding.md) | 2 | `_set_llama3_layer_sharding`, `set_llama3_sharding_config` | [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/llama3/state_dict_adapter.py`](torchtitan/models/llama3/state_dict_adapter.md) | 9 | `Llama3StateDictAdapter`, `to_hf`, `model_config` | [llama3-model](../concepts/llama3-model.md) |
| [`torchtitan/models/muse_glimmer/__init__.py`](torchtitan/models/muse_glimmer/__init__.md) | 32 | `model_registry`, `_muse_glimmer_config`, `_NORM_EPS` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/config_registry.py`](torchtitan/models/muse_glimmer/config_registry.md) | 6 | `muse_glimmer_debugmodel`, `muse_glimmer_debugmodel_mm`, `_muse_glimmer_mm_dataloader` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/model.py`](torchtitan/models/muse_glimmer/model.md) | 68 | `MuseGlimmerModel`, `Config`, `SoftCappedLinear` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/parallelize.py`](torchtitan/models/muse_glimmer/parallelize.md) | 1 | `parallelize_muse_glimmer` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/sharding.py`](torchtitan/models/muse_glimmer/sharding.md) | 9 | `CP`, `DP`, `TP` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/state_dict_adapter.py`](torchtitan/models/muse_glimmer/state_dict_adapter.md) | 16 | `MuseGlimmerStateDictAdapter`, `_dtensor_safe`, `model_config` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/muse_glimmer/vision_encoder.py`](torchtitan/models/muse_glimmer/vision_encoder.md) | 74 | `Config`, `Config`, `MuseGlimmerVisionAdapter` | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| [`torchtitan/models/qwen3/__init__.py`](torchtitan/models/qwen3/__init__.md) | 28 | `model_registry`, `_LINEAR_INIT`, `_qwen3_norm` | [qwen3-model](../concepts/qwen3-model.md) |
| [`torchtitan/models/qwen3/config_registry.py`](torchtitan/models/qwen3/config_registry.md) | 17 | `qwen3_debugmodel`, `qwen3_moe_debug`, `qwen3_30b_a3b_global_aux` | [quantization](../concepts/quantization.md), [qwen3-model](../concepts/qwen3-model.md) |
| [`torchtitan/models/qwen3/model.py`](torchtitan/models/qwen3/model.md) | 16 | `Qwen3Model`, `Config`, `dim` | [qwen3-model](../concepts/qwen3-model.md), [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) |
| [`torchtitan/models/qwen3/parallelize.py`](torchtitan/models/qwen3/parallelize.md) | 1 | `parallelize_qwen3` | [qwen3-model](../concepts/qwen3-model.md) |
| [`torchtitan/models/qwen3/sharding.py`](torchtitan/models/qwen3/sharding.md) | 3 | `_set_qwen3_layer_sharding`, `set_qwen3_sharding_config`, `_GROUPED_EXPERTS_PARAM_LAYOUT` | [qwen3-model](../concepts/qwen3-model.md) |
| [`torchtitan/models/qwen3/state_dict_adapter.py`](torchtitan/models/qwen3/state_dict_adapter.md) | 5 | `Qwen3StateDictAdapter`, `from_hf_map`, `from_hf` | [qwen3-model](../concepts/qwen3-model.md) |
| [`torchtitan/models/qwen3_5/__init__.py`](torchtitan/models/qwen3_5/__init__.md) | 34 | `_offset_norm`, `model_registry`, `QWEN3_5_SPECIAL_TOKENS` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/config_registry.py`](torchtitan/models/qwen3_5/config_registry.md) | 12 | `_multimodal_collator_config`, `qwen35_debugmodel_moe`, `qwen35_debugmodel` | [model-building-blocks](../concepts/model-building-blocks.md), [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/gdn.py`](torchtitan/models/qwen3_5/gdn.md) | 60 | `GatedDeltaNet`, `Config`, `GatedDeltaKernel` |  |
| [`torchtitan/models/qwen3_5/model.py`](torchtitan/models/qwen3_5/model.md) | 70 | `Qwen35Model`, `vision_encoder`, `Config` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/parallelize.py`](torchtitan/models/qwen3_5/parallelize.md) | 1 | `parallelize_qwen3_5` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/rope.py`](torchtitan/models/qwen3_5/rope.md) | 6 | `Config`, `MRoPE`, `mrope_section` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/sharding.py`](torchtitan/models/qwen3_5/sharding.md) | 14 | `TP`, `DP`, `_set_deltanet_sharding` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/state_dict_adapter.py`](torchtitan/models/qwen3_5/state_dict_adapter.md) | 7 | `Qwen35StateDictAdapter`, `from_hf_map`, `to_hf` | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| [`torchtitan/models/qwen3_5/vision_encoder.py`](torchtitan/models/qwen3_5/vision_encoder.md) | 56 | `Qwen35VisionEncoder`, `Config`, `num_position_embeddings` |  |
| [`torchtitan/models/qwen3_6/__init__.py`](torchtitan/models/qwen3_6/__init__.md) | 4 | `model_registry`, `QWEN3_6_SPECIAL_TOKENS`, `qwen3_6_configs` |  |
| [`torchtitan/models/qwen3_6/config_registry.py`](torchtitan/models/qwen3_6/config_registry.md) | 6 | `_multimodal_collator_config`, `qwen36_debugmodel`, `qwen36_debugmodel_moe` |  |
| [`torchtitan/models/qwen3_8/__init__.py`](torchtitan/models/qwen3_8/__init__.md) | 5 | `model_registry`, `QWEN3_8_SPECIAL_TOKENS`, `_qwen3_8_2_4t_a95b` |  |
| [`torchtitan/models/qwen3_8/config_registry.py`](torchtitan/models/qwen3_8/config_registry.md) | 6 | `_multimodal_collator_config`, `qwen38_debugmodel`, `qwen38_debugmodel_moe` | [hf-datasets](../concepts/hf-datasets.md) |
| [`torchtitan/models/utils.py`](torchtitan/models/utils.md) | 17 | `validate_converter_order`, `quadratic_attention_flops_per_token`, `get_nparams_and_active_nparams` |  |

## `torchtitan/observability`

Index: [`symbols/torchtitan-observability.tsv`](symbols/torchtitan-observability.tsv) (149 rows), [`edges/torchtitan-observability.tsv`](edges/torchtitan-observability.tsv) (316 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/observability/sdc_replayer.py`](torchtitan/observability/sdc_replayer.md) | 66 | `SDCReplayer`, `Config`, `_ReplaySignature` | [observability](../concepts/observability.md) |
| [`torchtitan/observability/structured_logger/__init__.py`](torchtitan/observability/structured_logger/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/observability/structured_logger/gantt_generator.py`](torchtitan/observability/structured_logger/gantt_generator.md) | 6 | `_collect_paired_and_instants`, `_emit_chrome_events`, `_assign_tids_per_source` | [observability](../concepts/observability.md) |
| [`torchtitan/observability/structured_logger/jsonl_handler.py`](torchtitan/observability/structured_logger/jsonl_handler.md) | 16 | `_log_dict`, `_thread_local`, `_refresh_event_delta` | [observability](../concepts/observability.md) |
| [`torchtitan/observability/structured_logger/step_state.py`](torchtitan/observability/structured_logger/step_state.md) | 13 | `set_step`, `add_step_tag`, `get_step` | [observability](../concepts/observability.md) |
| [`torchtitan/observability/structured_logger/structured_logging.py`](torchtitan/observability/structured_logger/structured_logging.md) | 47 | `log_trace_span`, `_structured_logger`, `log_trace_instant` | [observability](../concepts/observability.md) |

## `torchtitan/ops`

Index: [`symbols/torchtitan-ops.tsv`](symbols/torchtitan-ops.tsv) (3 rows), [`edges/torchtitan-ops.tsv`](edges/torchtitan-ops.tsv) (3 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/ops/scatter_add.py`](torchtitan/ops/scatter_add.md) | 3 | `deterministic_scatter_add`, `_backward`, `_setup_context` |  |

## `torchtitan/overrides`

Index: [`symbols/torchtitan-overrides.tsv`](symbols/torchtitan-overrides.tsv) (142 rows), [`edges/torchtitan-overrides.tsv`](edges/torchtitan-overrides.tsv) (158 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/overrides/fused_mla.py`](torchtitan/overrides/fused_mla.md) | 28 | `_to_local`, `Config`, `FusedMLAAttention` | [config-overrides](../concepts/config-overrides.md) |
| [`torchtitan/overrides/fused_swiglu.py`](torchtitan/overrides/fused_swiglu.md) | 45 | `FusedSwiGLU`, `Config`, `silu_and_mul_op` | [config-overrides](../concepts/config-overrides.md) |
| [`torchtitan/overrides/helion_rope.py`](torchtitan/overrides/helion_rope.md) | 45 | `_config`, `_DEFAULT_CONFIG`, `_run_tuned` | [config-overrides](../concepts/config-overrides.md) |
| [`torchtitan/overrides/moe_token_dispatcher.py`](torchtitan/overrides/moe_token_dispatcher.md) | 2 | `deepep_override`, `hybridep_override` |  |
| [`torchtitan/overrides/offset_rmsnorm.py`](torchtitan/overrides/offset_rmsnorm.md) | 22 | `Config`, `TritonOffsetRMSNorm`, `_num_warps` | [config-overrides](../concepts/config-overrides.md) |

## `torchtitan/protocols`

Index: [`symbols/torchtitan-protocols.tsv`](symbols/torchtitan-protocols.tsv) (85 rows), [`edges/torchtitan-protocols.tsv`](edges/torchtitan-protocols.tsv) (2006 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/protocols/__init__.py`](torchtitan/protocols/__init__.md) | 1 | `__all__` |  |
| [`torchtitan/protocols/model.py`](torchtitan/protocols/model.md) | 10 | `ModelConfigConverter`, `BaseModel`, `Config` | [model-spec-protocols](../concepts/model-spec-protocols.md) |
| [`torchtitan/protocols/model_spec.py`](torchtitan/protocols/model_spec.md) | 14 | `model`, `max_context_length`, `parallelize_fn` | [llama3-model](../concepts/llama3-model.md), [model-spec-protocols](../concepts/model-spec-protocols.md) |
| [`torchtitan/protocols/module.py`](torchtitan/protocols/module.md) | 35 | `build`, `Module`, `param_init` | [config-overrides](../concepts/config-overrides.md), [model-spec-protocols](../concepts/model-spec-protocols.md) |
| [`torchtitan/protocols/sharding.py`](torchtitan/protocols/sharding.md) | 13 | `ShardingConfig`, `state_shardings`, `in_src_shardings` | [config-overrides](../concepts/config-overrides.md), [model-spec-protocols](../concepts/model-spec-protocols.md) |
| [`torchtitan/protocols/state_dict_adapter.py`](torchtitan/protocols/state_dict_adapter.md) | 12 | `fqn_to_index_mapping`, `StateDictAdapter`, `BaseStateDictAdapter` | [model-spec-protocols](../concepts/model-spec-protocols.md) |

## `torchtitan/tools`

Index: [`symbols/torchtitan-tools.tsv`](symbols/torchtitan-tools.tsv) (123 rows), [`edges/torchtitan-tools.tsv`](edges/torchtitan-tools.tsv) (682 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan/tools/filesystem.py`](torchtitan/tools/filesystem.md) | 8 | `join`, `is_remote`, `_resolve` | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |
| [`torchtitan/tools/logging.py`](torchtitan/tools/logging.md) | 4 | `logger`, `init_logger`, `warn_once` | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |
| [`torchtitan/tools/profiler.py`](torchtitan/tools/profiler.md) | 46 | `Profiler`, `Config`, `profile_freq` | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |
| [`torchtitan/tools/utils.py`](torchtitan/tools/utils.md) | 65 | `device_type`, `device_module`, `has_cuda_capability` | [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md) |

## `torchtitan_recipes/tests`

Index: [`symbols/torchtitan_recipes-tests.tsv`](symbols/torchtitan_recipes-tests.tsv) (102 rows), [`edges/torchtitan_recipes-tests.tsv`](edges/torchtitan_recipes-tests.tsv) (120 edges)

| Module | Symbols | Entry points | Cited by |
|---|---|---|---|
| [`torchtitan_recipes/tests/b200.py`](torchtitan_recipes/tests/b200.md) | 2 | `kimi_k3_debugmodel_mm_fsdp2`, `llama3_debugmodel_mxfp8_fsdp2` |  |
| [`torchtitan_recipes/tests/features.py`](torchtitan_recipes/tests/features.md) | 54 | `llama3_debugmodel_full_checkpoint_save`, `llama3_debugmodel_pp4_interleaved_1f1b`, `llama3_debugmodel_hsdp2x2` | [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) |
| [`torchtitan_recipes/tests/h100.py`](torchtitan_recipes/tests/h100.md) | 9 | `deepseek_v3_debugmodel_minimal_async_ep_fsdp2_tp2_cp2_ep8`, `llama3_debugmodel_float8_fsdp2_tp2_pp2_asynctp_compile`, `llama3_debugmodel_float8_hsdp2x2_cp2_compile` |  |
| [`torchtitan_recipes/tests/models.py`](torchtitan_recipes/tests/models.md) | 33 | `llama3_debugmodel_fsdp2_tp2_cp2`, `_configure_fsdp_numerics`, `qwen3_debugmodel_fsdp2_tp2_cp2` |  |
| [`torchtitan_recipes/tests/transformers_modeling_backend.py`](torchtitan_recipes/tests/transformers_modeling_backend.md) | 4 | `transformers_backend_dense_cp_pp`, `transformers_backend_dense_fsdp_tp_pp`, `transformers_backend_moe_fsdp_tp_ep_cp` |  |

