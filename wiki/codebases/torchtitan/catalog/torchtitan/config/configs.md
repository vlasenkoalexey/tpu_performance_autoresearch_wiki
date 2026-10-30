---
title: 'Module: torchtitan/config/configs.py'
type: catalog
provenance: extracted
module: torchtitan/config/configs.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.configs`/
symbols:
  ParallelismConfig: ParallelismConfig#
  TrainingConfig: TrainingConfig#
  TrainingConfig.max_context_length: TrainingConfig#max_context_length.
  TrainingConfig.num_tokens_per_microbatch_per_dp_rank: TrainingConfig#num_tokens_per_microbatch_per_dp_rank.
  CompileConfig.enable: CompileConfig#enable.
  CompileConfig: CompileConfig#
  TrainingConfig.steps: TrainingConfig#steps.
  ParallelismConfig.data_parallel_shard_degree: ParallelismConfig#data_parallel_shard_degree.
  ParallelismConfig.tensor_parallel_degree: ParallelismConfig#tensor_parallel_degree.
  ParallelismConfig.expert_parallel_degree: ParallelismConfig#expert_parallel_degree.
  ParallelismConfig.spmd_backend: ParallelismConfig#spmd_backend.
  TrainingConfig.disable_cuda_graphs: TrainingConfig#disable_cuda_graphs.
  CompileConfig.components: CompileConfig#components.
  ParallelismConfig.context_parallel_degree: ParallelismConfig#context_parallel_degree.
  ParallelismConfig.pipeline_parallel_degree: ParallelismConfig#pipeline_parallel_degree.
  TrainingConfig.mixed_precision_reduce: TrainingConfig#mixed_precision_reduce.
  ParallelismConfig.pipeline_parallel_schedule: ParallelismConfig#pipeline_parallel_schedule.
  TrainingConfig.mixed_precision_param: TrainingConfig#mixed_precision_param.
  ParallelismConfig.fsdp_reshard_after_forward: ParallelismConfig#fsdp_reshard_after_forward.
  CompileConfig.backend: CompileConfig#backend.
  TrainingConfig.enable_cpu_offload: TrainingConfig#enable_cpu_offload.
  ParallelismConfig.data_parallel_replicate_degree: ParallelismConfig#data_parallel_replicate_degree.
  ParallelismConfig.use_simple_fsdp: ParallelismConfig#use_simple_fsdp.
  ParallelismConfig.num_pp_microbatches: ParallelismConfig#num_pp_microbatches.
  DebugConfig: DebugConfig#
  TrainingConfig.num_tokens_per_train_step: TrainingConfig#num_tokens_per_train_step.
  ParallelismConfig.context_parallel_load_balancer: ParallelismConfig#context_parallel_load_balancer.
  TrainingConfig.dtype: TrainingConfig#dtype.
  DebugConfig.seed: DebugConfig#seed.
  ParallelismConfig.enable_fsdp_symm_mem: ParallelismConfig#enable_fsdp_symm_mem.
  ParallelismConfig.enable_sequence_parallel: ParallelismConfig#enable_sequence_parallel.
  CommConfig: CommConfig#
  DebugConfig.deterministic: DebugConfig#deterministic.
  TrainingConfig.max_norm: TrainingConfig#max_norm.
  DebugConfig.batch_invariant: DebugConfig#batch_invariant.
  ParallelismConfig.enable_tpu_topo_mesh: ParallelismConfig#enable_tpu_topo_mesh.
  TrainingConfig.__post_init__: TrainingConfig#__post_init__().
  ParallelismConfig.__post_init__: ParallelismConfig#__post_init__().
  CompileConfig.__post_init__: CompileConfig#__post_init__().
  CompileConfig.enable_async_tensor_parallel: CompileConfig#enable_async_tensor_parallel.
  ParallelismConfig.context_parallel_ptrr_mask_key: ParallelismConfig#context_parallel_ptrr_mask_key.
  DebugConfig.spmd_typechecking: DebugConfig#spmd_typechecking.
  DebugConfig.print_config: DebugConfig#print_config.
  ParallelismConfig.module_fqns_per_model_part: ParallelismConfig#module_fqns_per_model_part.
  ParallelismConfig.pipeline_parallel_layers_per_stage: ParallelismConfig#pipeline_parallel_layers_per_stage.
  CommConfig.train_timeout_seconds: CommConfig#train_timeout_seconds.
  DebugConfig.enable_structured_logging: DebugConfig#enable_structured_logging.
  ParallelismConfig.pipeline_parallel_schedule_csv: ParallelismConfig#pipeline_parallel_schedule_csv.
  CommConfig.trace_buf_size: CommConfig#trace_buf_size.
  DebugConfig.deterministic_warn_only: DebugConfig#deterministic_warn_only.
  TrainingConfig.gc_freq: TrainingConfig#gc_freq.
  TrainingConfig.gc_debug: TrainingConfig#gc_debug.
  ParallelismConfig.pipeline_parallel_first_stage_less_layers: ParallelismConfig#pipeline_parallel_first_stage_less_layers.
  ParallelismConfig.pipeline_parallel_last_stage_less_layers: ParallelismConfig#pipeline_parallel_last_stage_less_layers.
  CommConfig.mode: CommConfig#mode.
  DebugConfig.save_config_file: DebugConfig#save_config_file.
  ParallelismConfig.enable_min_cost_redistribute: ParallelismConfig#enable_min_cost_redistribute.
  CommConfig.init_timeout_seconds: CommConfig#init_timeout_seconds.
  CommConfig.save_traces_folder: CommConfig#save_traces_folder.
  CommConfig.save_traces_file_prefix: CommConfig#save_traces_file_prefix.
  DebugConfig.moe_force_load_balance: DebugConfig#moe_force_load_balance.
  DebugConfig.detect_anomaly: DebugConfig#detect_anomaly.
---
# Module: [`torchtitan/config/configs.py`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py)

## Classes
### <a id="CommConfig"></a>`CommConfig`
- def: [`torchtitan/config/configs.py:368`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L368)
- signature: `class CommConfig:`
- members:
  - <a id="CommConfig.init_timeout_seconds"></a>`init_timeout_seconds` — [`L369`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L369) — ---
  - <a id="CommConfig.mode"></a>`mode` — [`L387`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L387) — ---
  - <a id="CommConfig.save_traces_file_prefix"></a>`save_traces_file_prefix` — [`L384`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L384) — ---
  - <a id="CommConfig.save_traces_folder"></a>`save_traces_folder` — [`L381`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L381) — ---
  - <a id="CommConfig.trace_buf_size"></a>`trace_buf_size` — [`L378`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L378) — ---
  - <a id="CommConfig.train_timeout_seconds"></a>`train_timeout_seconds` — [`L372`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L372) — ---
- used by: [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`train`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`train`](../trainer.md#Trainer.train), [`init_distributed`](../distributed/utils.md#init_distributed), [`__post_init__`](../experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.__post_init__), [`comm`](../trainer.md#Trainer.Config.comm), [`comm`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.comm)  (2 test-only)

### <a id="CompileConfig"></a>`CompileConfig`
- def: [`torchtitan/config/configs.py:338`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L338) — documented in [job-config](../../../concepts/job-config.md)
- signature: `class CompileConfig:`
- members:
  - <a id="CompileConfig.backend"></a>`backend` — [`L348`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L348) — documented in [job-config](../../../concepts/job-config.md)
  - <a id="CompileConfig.components"></a>`components` — [`L345`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L345) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="CompileConfig.enable"></a>`enable` — [`L339`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L339) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="CompileConfig.enable_async_tensor_parallel"></a>`enable_async_tensor_parallel` — [`L342`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L342) — ---
- protocol/private: <a id="CompileConfig.__post_init__"></a>`__post_init__`[`L350`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L350)
- uses (calls/refs, reference-scoped): [`GraphTrainerCompileConfig`](../experiments/graph_trainer/configs.md#GraphTrainerCompileConfig), [`TpuTrainerCompileConfig`](../experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig)
- used by: [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`deepseek_v3_16b`](../models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test), [`qwen35_debugmodel`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_debugmodel), [`GraphTrainerCompileConfig`](../experiments/graph_trainer/configs.md#GraphTrainerCompileConfig), [`compile`](../trainer.md#Trainer.Config.compile), [`parallelize_conformer`](../experiments/tpu/conformer/infra/parallelize.md#parallelize_conformer), [`parallelize_gptoss`](../models/gpt_oss/parallelize.md#parallelize_gptoss), [`parallelize_flux`](../models/flux/parallelize.md#parallelize_flux), [`parallelize_kimi_k3`](../models/kimi_k3/parallelize.md#parallelize_kimi_k3), [`parallelize_hf_transformers`](../experiments/transformers_modeling_backend/parallelize.md#parallelize_hf_transformers), [`parallelize_deepseekv3`](../models/deepseek_v3/parallelize.md#parallelize_deepseekv3), [`parallelize_qwen3_5`](../models/qwen3_5/parallelize.md#parallelize_qwen3_5), [`parallelize_qwen3`](../models/qwen3/parallelize.md#parallelize_qwen3), [`parallelize_kimi_k2_5`](../models/kimi_k2_7/parallelize.md#parallelize_kimi_k2_5), [`_multi_node`](../experiments/tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`parallelize_muse_glimmer`](../models/muse_glimmer/parallelize.md#parallelize_muse_glimmer), [`parallelize_llama`](../models/llama3/parallelize.md#parallelize_llama), [`parallelize_muse_glimmer`](../experiments/tpu/muse_glimmer/infra/parallelize.md#parallelize_muse_glimmer), [`pipeline_llm`](../distributed/pipeline_parallel.md#pipeline_llm)  (+74 more; 67 test-only)

### <a id="DebugConfig"></a>`DebugConfig`
- def: [`torchtitan/config/configs.py:398`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L398) — documented in [job-config](../../../concepts/job-config.md)
- signature: `class DebugConfig:`
- members:
  - <a id="DebugConfig.batch_invariant"></a>`batch_invariant` — [`L418`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L418) — ---
  - <a id="DebugConfig.detect_anomaly"></a>`detect_anomaly` — [`L414`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L414) — ---
  - <a id="DebugConfig.deterministic"></a>`deterministic` — [`L405`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L405) — ---
  - <a id="DebugConfig.deterministic_warn_only"></a>`deterministic_warn_only` — [`L408`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L408) — ---
  - <a id="DebugConfig.enable_structured_logging"></a>`enable_structured_logging` — [`L428`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L428) — ---
  - <a id="DebugConfig.moe_force_load_balance"></a>`moe_force_load_balance` — [`L411`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L411) — ---
  - <a id="DebugConfig.print_config"></a>`print_config` — [`L422`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L422) — ---
  - <a id="DebugConfig.save_config_file"></a>`save_config_file` — [`L425`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L425) — ---
  - <a id="DebugConfig.seed"></a>`seed` — [`L399`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L399) — ---
  - <a id="DebugConfig.spmd_typechecking"></a>`spmd_typechecking` — [`L402`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L402) — ---
- used by: [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`transformers_modeling_backend_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full), [`transformers_modeling_backend_full_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full_moe), [`start_trainer`](../experiments/tpu/train.md#start_trainer), [`model_path`](../experiments/rl/actors/generator.md#VLLMGenerator.model_path), [`main`](../experiments/rl/train.md#main), [`__post_init__`](../trainer.md#Trainer.Config.__post_init__), [`update_from_config`](../models/common/decoder.md#Decoder.Config.update_from_config), [`_tp_rank`](../experiments/rl/actors/generator.md#VLLMGenerator._tp_rank), [`__post_init__`](../experiments/rl/controller.md#Controller.Config.__post_init__), [`set_determinism`](../distributed/utils.md#set_determinism), [`debug`](../trainer.md#Trainer.Config.debug), [`loss_mesh`](../experiments/tpu/train_minimal.md#TrainerMinimal.loss_mesh), [`graph_trainer_llama3_debugmodel_sdc_replay`](../experiments/graph_trainer/llama3/config_registry.md#graph_trainer_llama3_debugmodel_sdc_replay), [`__init__`](../experiments/rl/actors/trainer.md#PolicyTrainer.__init__), [`device`](../experiments/rl/actors/trainer.md#PolicyTrainer.device), [`__init__`](../experiments/rl/actors/generator.md#VLLMGenerator.__init__), [`__post_init__`](../experiments/rl/actors/generator.md#VLLMGenerator.Config.__post_init__), [`maybe_log`](../trainer.md#Trainer.Config.maybe_log), [`_validate_sdc_replay`](../trainer.md#Trainer.Config._validate_sdc_replay), [`debug`](../experiments/rl/actors/generator.md#VLLMGenerator.Config.debug), [`_sampling`](../experiments/rl/controller.md#Controller._sampling), [`debug`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.debug), [`_set_determinism`](../experiments/rl/actors/generator.md#VLLMGenerator._set_determinism)  (14 test-only)

### <a id="ParallelismConfig"></a>`ParallelismConfig`
- def: [`torchtitan/config/configs.py:123`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L123) — documented in [job-config](../../../concepts/job-config.md)
- signature: `class ParallelismConfig:`
- members:
  - <a id="ParallelismConfig.context_parallel_degree"></a>`context_parallel_degree` — [`L266`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L266) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.context_parallel_load_balancer"></a>`context_parallel_load_balancer` — [`L269`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L269) — ---
  - <a id="ParallelismConfig.context_parallel_ptrr_mask_key"></a>`context_parallel_ptrr_mask_key` — [`L277`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L277) — ---
  - <a id="ParallelismConfig.data_parallel_replicate_degree"></a>`data_parallel_replicate_degree` — [`L149`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L149) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.data_parallel_shard_degree"></a>`data_parallel_shard_degree` — [`L160`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L160) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.enable_fsdp_symm_mem"></a>`enable_fsdp_symm_mem` — [`L187`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L187) — ---
  - <a id="ParallelismConfig.enable_min_cost_redistribute"></a>`enable_min_cost_redistribute` — [`L132`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L132) — ---
  - <a id="ParallelismConfig.enable_sequence_parallel"></a>`enable_sequence_parallel` — [`L196`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L196) — ---
  - <a id="ParallelismConfig.enable_tpu_topo_mesh"></a>`enable_tpu_topo_mesh` — [`L127`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L127) — ---
  - <a id="ParallelismConfig.expert_parallel_degree"></a>`expert_parallel_degree` — [`L326`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L326) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.fsdp_reshard_after_forward"></a>`fsdp_reshard_after_forward` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L172) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.module_fqns_per_model_part"></a>`module_fqns_per_model_part` — [`L214`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L214) — ---
  - <a id="ParallelismConfig.num_pp_microbatches"></a>`num_pp_microbatches` — [`L259`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L259) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.pipeline_parallel_degree"></a>`pipeline_parallel_degree` — [`L207`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L207) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.pipeline_parallel_first_stage_less_layers"></a>`pipeline_parallel_first_stage_less_layers` — [`L224`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L224) — ---
  - <a id="ParallelismConfig.pipeline_parallel_last_stage_less_layers"></a>`pipeline_parallel_last_stage_less_layers` — [`L230`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L230) — ---
  - <a id="ParallelismConfig.pipeline_parallel_layers_per_stage"></a>`pipeline_parallel_layers_per_stage` — [`L236`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L236) — ---
  - <a id="ParallelismConfig.pipeline_parallel_schedule"></a>`pipeline_parallel_schedule` — [`L243`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L243) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.pipeline_parallel_schedule_csv"></a>`pipeline_parallel_schedule_csv` — [`L252`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L252) — ---
  - <a id="ParallelismConfig.spmd_backend"></a>`spmd_backend` — [`L199`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L199) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.tensor_parallel_degree"></a>`tensor_parallel_degree` — [`L193`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L193) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="ParallelismConfig.use_simple_fsdp"></a>`use_simple_fsdp` — [`L124`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L124) — --- — documented in [job-config](../../../concepts/job-config.md)
- protocol/private: <a id="ParallelismConfig.__post_init__"></a>`__post_init__`[`L286`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L286)
- used by: [`parallelism`](../trainer.md#Trainer.Config.parallelism), [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_build_stage_graphs`](../experiments/graph_trainer/graph_pp/graph_builder.md#_build_stage_graphs), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5)  (+132 more; 160 test-only)

### <a id="TrainingConfig"></a>`TrainingConfig`
- def: [`torchtitan/config/configs.py:36`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L36) — documented in [flux-diffusion-model](../../../concepts/flux-diffusion-model.md)
- signature: `class TrainingConfig:`
- members:
  - <a id="TrainingConfig.disable_cuda_graphs"></a>`disable_cuda_graphs` — [`L77`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L77) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="TrainingConfig.dtype"></a>`dtype` — [`L89`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L89) — ---
  - <a id="TrainingConfig.enable_cpu_offload"></a>`enable_cpu_offload` — [`L72`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L72) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="TrainingConfig.gc_debug"></a>`gc_debug` — [`L113`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L113) — ---
  - <a id="TrainingConfig.gc_freq"></a>`gc_freq` — [`L110`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L110) — ---
  - <a id="TrainingConfig.max_context_length"></a>`max_context_length` — [`L51`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L51) — --- — documented in [flux-diffusion-model](../../../concepts/flux-diffusion-model.md)
  - <a id="TrainingConfig.max_norm"></a>`max_norm` — [`L66`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L66) — ---
  - <a id="TrainingConfig.mixed_precision_param"></a>`mixed_precision_param` — [`L96`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L96) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="TrainingConfig.mixed_precision_reduce"></a>`mixed_precision_reduce` — [`L104`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L104) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="TrainingConfig.num_tokens_per_microbatch_per_dp_rank"></a>`num_tokens_per_microbatch_per_dp_rank` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L37) — --- — documented in [job-config](../../../concepts/job-config.md)
  - <a id="TrainingConfig.num_tokens_per_train_step"></a>`num_tokens_per_train_step` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L43) — ---
  - <a id="TrainingConfig.steps"></a>`steps` — [`L69`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L69) — --- — documented in [job-config](../../../concepts/job-config.md)
- protocol/private: <a id="TrainingConfig.__post_init__"></a>`__post_init__`[`L54`](../../../../../../raw/code/torchtitan/torchtitan/config/configs.py#L54)
- used by: [`training`](../trainer.md#Trainer.Config.training), [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`transformers_modeling_backend_sft_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP)  (+151 more; 122 test-only)

