---
title: 'Module: torchtitan/experiments/tpu/tpu_job_config.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tpu_job_config.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tpu_job_config`/
symbols:
  TPUTrainerConfig: TPUTrainerConfig#
  TPUTrainerConfig.compile: TPUTrainerConfig#compile.
  BaseTPUTrainerConfig.splash_attention_kernel: BaseTPUTrainerConfig#splash_attention_kernel.
  TPUTrainerConfig.__post_init__: TPUTrainerConfig#__post_init__().
  TPUTrainerConfig.tpu_config: TPUTrainerConfig#tpu_config.
  BaseTPUTrainerConfig.__post_init__: BaseTPUTrainerConfig#__post_init__().
  TpuTrainerCompileConfig: TpuTrainerCompileConfig#
  TPUConfig: TPUConfig#
  BaseTPUTrainerConfig.libtpu_init_flags: BaseTPUTrainerConfig#libtpu_init_flags.
  SplashAttentionKernelConfig: SplashAttentionKernelConfig#
  SplashAttentionKernelConfig.use_splash_attention_kernel: SplashAttentionKernelConfig#use_splash_attention_kernel.
  SplashAttentionKernelConfig.sa_block_kv_compute: SplashAttentionKernelConfig#sa_block_kv_compute.
  SplashAttentionKernelConfig.sa_block_q_dkv: SplashAttentionKernelConfig#sa_block_q_dkv.
  SplashAttentionKernelConfig.sa_block_kv_dkv: SplashAttentionKernelConfig#sa_block_kv_dkv.
  BaseTPUTrainerConfig: BaseTPUTrainerConfig#
  TPUConfig.eager_mode: TPUConfig#eager_mode.
  SplashAttentionKernelConfig.sa_block_kv_dkv_compute: SplashAttentionKernelConfig#sa_block_kv_dkv_compute.
  SplashAttentionKernelConfig.sa_block_q: SplashAttentionKernelConfig#sa_block_q.
  SplashAttentionKernelConfig.sa_block_kv: SplashAttentionKernelConfig#sa_block_kv.
  SplashAttentionKernelConfig.use_tokamax_splash_attention_kernel: SplashAttentionKernelConfig#use_tokamax_splash_attention_kernel.
  SplashAttentionKernelConfig.sa_use_document_aware_block_skipping: SplashAttentionKernelConfig#sa_use_document_aware_block_skipping.
  SplashAttentionKernelConfig.sa_block_dkv: SplashAttentionKernelConfig#sa_block_dkv.
  SplashAttentionKernelConfig.sa_block_q_dq: SplashAttentionKernelConfig#sa_block_q_dq.
  SplashAttentionKernelConfig.sa_block_kv_dq: SplashAttentionKernelConfig#sa_block_kv_dq.
  SplashAttentionKernelConfig.sa_q_layout: SplashAttentionKernelConfig#sa_q_layout.
  SplashAttentionKernelConfig.sa_k_layout: SplashAttentionKernelConfig#sa_k_layout.
  BaseTPUTrainerConfig.loss_kernel: BaseTPUTrainerConfig#loss_kernel.
  TpuTrainerCompileConfig.compile_grad_norm: TpuTrainerCompileConfig#compile_grad_norm.
  LossKernelConfig: LossKernelConfig#
  TpuTrainerCompileConfig.mode: TpuTrainerCompileConfig#mode.
  BaseTPUTrainerConfig.xla_flags: BaseTPUTrainerConfig#xla_flags.
  TpuTrainerCompileConfig.materialize_forward_before_backward: TpuTrainerCompileConfig#materialize_forward_before_backward.
  SplashAttentionKernelConfig.use_vmap_bwd: SplashAttentionKernelConfig#use_vmap_bwd.
  TpuTrainerCompileConfig.optimizer_compile: TpuTrainerCompileConfig#optimizer_compile.
  BaseTPUTrainerConfig.conformer: BaseTPUTrainerConfig#conformer.
  BaseTPUTrainerConfig.flux: BaseTPUTrainerConfig#flux.
  TPUConfig.enable_amp: TPUConfig#enable_amp.
  SplashAttentionKernelConfig.sa_v_layout: SplashAttentionKernelConfig#sa_v_layout.
  LossKernelConfig.use_loss_kernel: LossKernelConfig#use_loss_kernel.
  TPUConfig.use_simple_fsdp: TPUConfig#use_simple_fsdp.
  ConformerConfig: ConformerConfig#
  TPUConfig.enable_mfu_benchmark: TPUConfig#enable_mfu_benchmark.
  BaseTPUTrainerConfig.derive_from: BaseTPUTrainerConfig#derive_from().
  BaseTPUTrainerConfig.extra_xla_flags: BaseTPUTrainerConfig#extra_xla_flags.
  BaseTPUTrainerConfig.extra_libtpu_init_flags: BaseTPUTrainerConfig#extra_libtpu_init_flags.
  BaseTPUTrainerConfig.qwen3: BaseTPUTrainerConfig#qwen3.
  BaseTPUTrainerConfig.lora: BaseTPUTrainerConfig#lora.
  TPUConfig.use_jax_profiler: TPUConfig#use_jax_profiler.
  TPUConfig.mfu_benchmark_start_step: TPUConfig#mfu_benchmark_start_step.
  ConformerConfig.use_ctc_loss: ConformerConfig#use_ctc_loss.
  Qwen3Config: Qwen3Config#
  FluxConfig: FluxConfig#
  LoRAConfig: LoRAConfig#
  TpuTrainerCompileMode: TpuTrainerCompileMode.
  TpuTrainerOptimizerCompileMode: TpuTrainerOptimizerCompileMode.
  ConformerConfig.use_jax_ctc_loss: ConformerConfig#use_jax_ctc_loss.
  FluxConfig.precomputed_dataset_path: FluxConfig#precomputed_dataset_path.
  FluxConfig.img_size: FluxConfig#img_size.
  LossKernelConfig.loss_b_block_size: LossKernelConfig#loss_b_block_size.
  LossKernelConfig.loss_h_block_size: LossKernelConfig#loss_h_block_size.
  LossKernelConfig.loss_v_block_size: LossKernelConfig#loss_v_block_size.
  LossKernelConfig.enable_pallas_loss_kernel: LossKernelConfig#enable_pallas_loss_kernel.
  TPUConfig.apply_rope_complex_workaround: TPUConfig#apply_rope_complex_workaround.
  TPUConfig.bld_block_layout: TPUConfig#bld_block_layout.
  TPUConfig.log_freq: TPUConfig#log_freq.
  ConformerConfig.ctc_loss_target_len: ConformerConfig#ctc_loss_target_len.
  Qwen3Config.use_gmm_kernel: Qwen3Config#use_gmm_kernel.
  Qwen3Config.use_fill_indices_kernel: Qwen3Config#use_fill_indices_kernel.
  FluxConfig.random_dataset: FluxConfig#random_dataset.
  LoRAConfig.use_lora: LoRAConfig#use_lora.
  LoRAConfig.lora_rank: LoRAConfig#lora_rank.
  LoRAConfig.lora_alpha: LoRAConfig#lora_alpha.
  LoRAConfig.lora_dtype: LoRAConfig#lora_dtype.
  LoRAConfig.force_lora_parameter_ddp: LoRAConfig#force_lora_parameter_ddp.
  SplashAttentionKernelConfig.sa_use_fused_bwd_kernel: SplashAttentionKernelConfig#sa_use_fused_bwd_kernel.
---
# Module: [`torchtitan/experiments/tpu/tpu_job_config.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py)

## Classes
### <a id="BaseTPUTrainerConfig"></a>`BaseTPUTrainerConfig`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:150`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L150) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- signature: `class BaseTPUTrainerConfig(torchtitan.trainer.Trainer.Config):`
- members:
  - <a id="BaseTPUTrainerConfig.derive_from"></a>`derive_from(cls, src, **overrides)` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L206) — Copy-construct a ``cls`` instance from a sibling ``BaseTPUTrainerConfig``
  - <a id="BaseTPUTrainerConfig.conformer"></a>`conformer` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L163)
  - <a id="BaseTPUTrainerConfig.extra_libtpu_init_flags"></a>`extra_libtpu_init_flags` — [`L160`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L160)
  - <a id="BaseTPUTrainerConfig.extra_xla_flags"></a>`extra_xla_flags` — [`L157`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L157)
  - <a id="BaseTPUTrainerConfig.flux"></a>`flux` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L167)
  - <a id="BaseTPUTrainerConfig.libtpu_init_flags"></a>`libtpu_init_flags` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L154)
  - <a id="BaseTPUTrainerConfig.lora"></a>`lora` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L168)
  - <a id="BaseTPUTrainerConfig.loss_kernel"></a>`loss_kernel` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L172)
  - <a id="BaseTPUTrainerConfig.qwen3"></a>`qwen3` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L166)
  - <a id="BaseTPUTrainerConfig.splash_attention_kernel"></a>`splash_attention_kernel` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L169)
  - <a id="BaseTPUTrainerConfig.xla_flags"></a>`xla_flags` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L151)
- protocol/private: <a id="BaseTPUTrainerConfig.__post_init__"></a>`__post_init__`[`L176`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L176)
- uses (calls/refs, reference-scoped): [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`training`](../../trainer.md#Trainer.Config.training), [`model_spec`](../../trainer.md#Trainer.Config.model_spec), [`Trainer`](../../trainer.md#Trainer), [`Config`](../../trainer.md#Trainer.Config), [`model`](../../protocols/model_spec.md#ModelSpec.model), [`TPUTrainerConfig`](tpu_job_config.md#TPUTrainerConfig), [`disable_cuda_graphs`](../../config/configs.md#TrainingConfig.disable_cuda_graphs), [`__post_init__`](../../trainer.md#Trainer.Config.__post_init__), [`context_parallel_degree`](../../config/configs.md#ParallelismConfig.context_parallel_degree), [`FlagMap`](tpu_flags.md#FlagMap), [`validate_tpu_context_parallel`](cp_attention.md#validate_tpu_context_parallel), [`SplashAttentionKernelConfig`](tpu_job_config.md#SplashAttentionKernelConfig), [`comm`](../../trainer.md#Trainer.Config.comm), [`JaxJobConfig`](../jax/jax_job_config.md#JaxJobConfig), [`LossKernelConfig`](tpu_job_config.md#LossKernelConfig), [`ConformerConfig`](tpu_job_config.md#ConformerConfig), [`trace_buf_size`](../../config/configs.md#CommConfig.trace_buf_size), [`FluxConfig`](tpu_job_config.md#FluxConfig), [`LoRAConfig`](tpu_job_config.md#LoRAConfig), [`Qwen3Config`](tpu_job_config.md#Qwen3Config)
- used by: [`sft_llama3_8b_metamath`](llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](qwen3/config_registry.md#qwen3_8b), [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](llama3/config_registry.md#llama3_70b), [`llama3_405b`](llama3/config_registry.md#llama3_405b), [`llama3_8b`](llama3/config_registry.md#llama3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`TPUTrainerConfig`](tpu_job_config.md#TPUTrainerConfig), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`conformer_test`](conformer/config_registry.md#conformer_test), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`parallelize_flux`](../../models/flux/parallelize.md#parallelize_flux), [`qwen3_32b`](qwen3/config_registry.md#qwen3_32b), [`_on_scan_lane`](llama3/config_registry.md#_on_scan_lane), [`_run_cpu_verification`](base_distributed_device_test.md#_run_cpu_verification), [`__post_init__`](tpu_job_config.md#TPUTrainerConfig.__post_init__), [`_dtype`](../../models/flux/trainer.md#FluxTrainer._dtype), [`_qwen3_moe_235b_fsdp_activation_offload`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_activation_offload), [`build_cross_entropy_loss`](loss.md#build_cross_entropy_loss), [`qwen3_8b_zero3`](qwen3/config_registry.md#qwen3_8b_zero3), [`_apply_flux_img_size`](train.md#_apply_flux_img_size), [`_legacy_pallas_loss_config`](loss.md#_legacy_pallas_loss_config), [`qwen3_moe_235b_fsdp_activation_offload_4x4x4`](qwen3/config_registry.md#qwen3_moe_235b_fsdp_activation_offload_4x4x4), [`llama3_debugmodel`](../jax/llama3/config_registry.md#llama3_debugmodel), [`update_from_config`](conformer/model.md#ConformerModelArgs.update_from_config), [`JaxJobConfig`](../jax/jax_job_config.md#JaxJobConfig)  (13 test-only)

### <a id="ConformerConfig"></a>`ConformerConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:64`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L64)
- signature: `class ConformerConfig:`
- members:
  - <a id="ConformerConfig.ctc_loss_target_len"></a>`ctc_loss_target_len` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L69)
  - <a id="ConformerConfig.use_ctc_loss"></a>`use_ctc_loss` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L65)
  - <a id="ConformerConfig.use_jax_ctc_loss"></a>`use_jax_ctc_loss` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L66)
- used by: [`start_trainer`](conformer/train_minimal.md#start_trainer), [`conformer_test`](conformer/config_registry.md#conformer_test), [`conformer`](tpu_job_config.md#BaseTPUTrainerConfig.conformer)

### <a id="FluxConfig"></a>`FluxConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L79)
- signature: `class FluxConfig:`
- members:
  - <a id="FluxConfig.img_size"></a>`img_size` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L84) — ---
  - <a id="FluxConfig.precomputed_dataset_path"></a>`precomputed_dataset_path` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L80) — ---
  - <a id="FluxConfig.random_dataset"></a>`random_dataset` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L82) — ---
- used by: [`_dtype`](../../models/flux/trainer.md#FluxTrainer._dtype), [`_apply_flux_img_size`](train.md#_apply_flux_img_size), [`flux`](tpu_job_config.md#BaseTPUTrainerConfig.flux)

### <a id="LoRAConfig"></a>`LoRAConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L93)
- signature: `class LoRAConfig:`
- members:
  - <a id="LoRAConfig.force_lora_parameter_ddp"></a>`force_lora_parameter_ddp` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L101)
  - <a id="LoRAConfig.lora_alpha"></a>`lora_alpha` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L97)
  - <a id="LoRAConfig.lora_dtype"></a>`lora_dtype` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L98)
  - <a id="LoRAConfig.lora_rank"></a>`lora_rank` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L96)
  - <a id="LoRAConfig.use_lora"></a>`use_lora` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L95)
- used by: [`lora`](tpu_job_config.md#BaseTPUTrainerConfig.lora)

### <a id="LossKernelConfig"></a>`LossKernelConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:135`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L135) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- signature: `class LossKernelConfig:`
- members:
  - <a id="LossKernelConfig.enable_pallas_loss_kernel"></a>`enable_pallas_loss_kernel` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L141)
  - <a id="LossKernelConfig.loss_b_block_size"></a>`loss_b_block_size` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L138)
  - <a id="LossKernelConfig.loss_h_block_size"></a>`loss_h_block_size` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L139)
  - <a id="LossKernelConfig.loss_v_block_size"></a>`loss_v_block_size` — [`L140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L140)
  - <a id="LossKernelConfig.use_loss_kernel"></a>`use_loss_kernel` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L136)
- used by: [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`_legacy_pallas_loss_config`](loss.md#_legacy_pallas_loss_config), [`loss_kernel`](tpu_job_config.md#BaseTPUTrainerConfig.loss_kernel)

### <a id="Qwen3Config"></a>`Qwen3Config`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L73)
- signature: `class Qwen3Config:`
- members:
  - <a id="Qwen3Config.use_fill_indices_kernel"></a>`use_fill_indices_kernel` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L75)
  - <a id="Qwen3Config.use_gmm_kernel"></a>`use_gmm_kernel` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L74)
- used by: [`qwen3`](tpu_job_config.md#BaseTPUTrainerConfig.qwen3)

### <a id="SplashAttentionKernelConfig"></a>`SplashAttentionKernelConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L105) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- signature: `class SplashAttentionKernelConfig:`
- members:
  - <a id="SplashAttentionKernelConfig.sa_block_dkv"></a>`sa_block_dkv` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L121)
  - <a id="SplashAttentionKernelConfig.sa_block_kv"></a>`sa_block_kv` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L120)
  - <a id="SplashAttentionKernelConfig.sa_block_kv_compute"></a>`sa_block_kv_compute` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L122)
  - <a id="SplashAttentionKernelConfig.sa_block_kv_dkv"></a>`sa_block_kv_dkv` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L124)
  - <a id="SplashAttentionKernelConfig.sa_block_kv_dkv_compute"></a>`sa_block_kv_dkv_compute` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L125)
  - <a id="SplashAttentionKernelConfig.sa_block_kv_dq"></a>`sa_block_kv_dq` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L127)
  - <a id="SplashAttentionKernelConfig.sa_block_q"></a>`sa_block_q` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L119)
  - <a id="SplashAttentionKernelConfig.sa_block_q_dkv"></a>`sa_block_q_dkv` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L123)
  - <a id="SplashAttentionKernelConfig.sa_block_q_dq"></a>`sa_block_q_dq` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L126)
  - <a id="SplashAttentionKernelConfig.sa_k_layout"></a>`sa_k_layout` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L130)
  - <a id="SplashAttentionKernelConfig.sa_q_layout"></a>`sa_q_layout` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L129)
  - <a id="SplashAttentionKernelConfig.sa_use_document_aware_block_skipping"></a>`sa_use_document_aware_block_skipping` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L117)
  - <a id="SplashAttentionKernelConfig.sa_use_fused_bwd_kernel"></a>`sa_use_fused_bwd_kernel` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L128)
  - <a id="SplashAttentionKernelConfig.sa_v_layout"></a>`sa_v_layout` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L131)
  - <a id="SplashAttentionKernelConfig.use_splash_attention_kernel"></a>`use_splash_attention_kernel` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L106)
  - <a id="SplashAttentionKernelConfig.use_tokamax_splash_attention_kernel"></a>`use_tokamax_splash_attention_kernel` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L107)
  - <a id="SplashAttentionKernelConfig.use_vmap_bwd"></a>`use_vmap_bwd` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L112)
- used by: [`sft_llama3_8b_metamath`](llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](qwen3/config_registry.md#qwen3_8b), [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](llama3/config_registry.md#llama3_70b), [`llama3_405b`](llama3/config_registry.md#llama3_405b), [`llama3_8b`](llama3/config_registry.md#llama3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`qwen3_moe_235b_scan`](qwen3/config_registry.md#qwen3_moe_235b_scan), [`conformer_test`](conformer/config_registry.md#conformer_test), [`_qwen3_moe_235b_fsdp_only`](qwen3/config_registry.md#_qwen3_moe_235b_fsdp_only), [`parallelize_flux`](../../models/flux/parallelize.md#parallelize_flux), [`splash_attention_kernel`](tpu_job_config.md#BaseTPUTrainerConfig.splash_attention_kernel), [`_run_cpu_verification`](base_distributed_device_test.md#_run_cpu_verification), [`qwen3_8b_zero3`](qwen3/config_registry.md#qwen3_8b_zero3), [`update_from_config`](conformer/model.md#ConformerModelArgs.update_from_config)  (12 test-only)

### <a id="TPUConfig"></a>`TPUConfig`
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L13) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- doc: TorchTPU runtime controls shared by the regular and graph trainers.
- signature: `class TPUConfig:`
- members:
  - <a id="TPUConfig.apply_rope_complex_workaround"></a>`apply_rope_complex_workaround` — [`L17`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L17)
  - <a id="TPUConfig.bld_block_layout"></a>`bld_block_layout` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L21)
  - <a id="TPUConfig.eager_mode"></a>`eager_mode` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L31)
  - <a id="TPUConfig.enable_amp"></a>`enable_amp` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L29)
  - <a id="TPUConfig.enable_mfu_benchmark"></a>`enable_mfu_benchmark` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L25)
  - <a id="TPUConfig.log_freq"></a>`log_freq` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L30)
  - <a id="TPUConfig.mfu_benchmark_start_step"></a>`mfu_benchmark_start_step` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L26)
  - <a id="TPUConfig.use_jax_profiler"></a>`use_jax_profiler` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L22)
  - <a id="TPUConfig.use_simple_fsdp"></a>`use_simple_fsdp` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L16)
- used by: [`sft_llama3_8b_metamath`](llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](llama3/config_registry.md#llama3_70b), [`llama3_405b`](llama3/config_registry.md#llama3_405b), [`llama3_8b`](llama3/config_registry.md#llama3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`flux_dev`](../../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../../models/flux/config_registry.md#flux_schnell), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen35_moe_35b`](qwen3_5/config_registry.md#qwen35_moe_35b), [`conformer_test`](conformer/config_registry.md#conformer_test), [`qwen35_debugmodel`](qwen3_5/config_registry.md#qwen35_debugmodel), [`parallelize_conformer`](conformer/infra/parallelize.md#parallelize_conformer), [`muse_glimmer_30b_full_logits`](muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits), [`_determine_parallel_strategy`](conformer/infra/parallelize.md#_determine_parallel_strategy), [`qwen3_moe_235b_fsdp_smoke`](qwen3/config_registry.md#qwen3_moe_235b_fsdp_smoke), [`tpu_config`](tpu_job_config.md#TPUTrainerConfig.tpu_config), [`qwen3_moe_30b_fsdp_only_full_ac_benchmark`](qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_benchmark), [`_compiled_grad_norm`](train.md#TPUTrainer._compiled_grad_norm), [`reg_trainer_muse_glimmer_30b_fused_ce`](muse_glimmer/config_registry.md#reg_trainer_muse_glimmer_30b_fused_ce), [`_mfu_benchmark`](graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._mfu_benchmark), [`_start_trainer`](gmain.md#_start_trainer)

### <a id="TPUTrainerConfig"></a>`TPUTrainerConfig`  ·  implements/extends BaseTPUTrainerConfig
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:248`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L248) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- signature: `class TPUTrainerConfig(BaseTPUTrainerConfig):`
- members:
  - <a id="TPUTrainerConfig.compile"></a>`compile` — [`L249`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L249)
  - <a id="TPUTrainerConfig.tpu_config"></a>`tpu_config` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L252)
- protocol/private: <a id="TPUTrainerConfig.__post_init__"></a>`__post_init__`[`L254`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L254)
- uses (calls/refs, reference-scoped): [`parallelism`](../../trainer.md#Trainer.Config.parallelism), [`enable`](../../config/configs.md#CompileConfig.enable), [`CompileConfig`](../../config/configs.md#CompileConfig), [`expert_parallel_degree`](../../config/configs.md#ParallelismConfig.expert_parallel_degree), [`Config`](graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config), [`components`](../../config/configs.md#CompileConfig.components), [`pipeline_parallel_degree`](../../config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`backend`](../../config/configs.md#CompileConfig.backend), [`__post_init__`](tpu_job_config.md#BaseTPUTrainerConfig.__post_init__), [`TpuTrainerCompileConfig`](tpu_job_config.md#TpuTrainerCompileConfig), [`dump_folder`](../../trainer.md#Trainer.Config.dump_folder), [`TPUConfig`](tpu_job_config.md#TPUConfig), [`TPUTransformersBackendConfig`](transformers_modeling_backend/job_config.md#TPUTransformersBackendConfig), [`BaseTPUTrainerConfig`](tpu_job_config.md#BaseTPUTrainerConfig), [`Config`](../../models/flux/trainer.md#FluxTrainer.Config), [`compile_grad_norm`](tpu_job_config.md#TpuTrainerCompileConfig.compile_grad_norm)
- used by: [`sft_llama3_8b_metamath`](llama3/config_registry.md#sft_llama3_8b_metamath), [`qwen3_8b`](qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](llama3/config_registry.md#llama3_70b), [`llama3_405b`](llama3/config_registry.md#llama3_405b), [`llama3_8b`](llama3/config_registry.md#llama3_8b), [`_qwen3_moe_30b_fsdp_only_full_ac`](qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`_muse_glimmer_30b_base`](muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../../models/flux/config_registry.md#flux_schnell), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`qwen35_moe_35b`](qwen3_5/config_registry.md#qwen35_moe_35b), [`qwen3_debugmodel`](qwen3/config_registry.md#qwen3_debugmodel), [`conformer_test`](conformer/config_registry.md#conformer_test), [`qwen35_debugmodel`](qwen3_5/config_registry.md#qwen35_debugmodel), [`llama3_debugmodel`](llama3/config_registry.md#llama3_debugmodel), [`llama3_1b`](llama3/config_registry.md#llama3_1b), [`start_trainer`](train.md#start_trainer), [`muse_glimmer_debugmodel`](muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`deepseek_v3_debugmodel`](deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`parallelize_conformer`](conformer/infra/parallelize.md#parallelize_conformer), [`parallelize_flux`](../../models/flux/parallelize.md#parallelize_flux), [`Config`](graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config), [`muse_glimmer_30b_full_logits`](muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits), [`_qwen3_cp`](qwen3/config_registry.md#_qwen3_cp), [`forward_backward_step`](train.md#TPUTrainer.forward_backward_step), [`qwen3_moe_testmodel`](qwen3/config_registry.md#qwen3_moe_testmodel), [`_on_scan_lane`](llama3/config_registry.md#_on_scan_lane), [`_test_train_distributed`](base_distributed_device_test.md#BaseDistributedDeviceTest._test_train_distributed), [`_determine_parallel_strategy`](conformer/infra/parallelize.md#_determine_parallel_strategy), [`qwen3_moe_235b_fsdp_smoke`](qwen3/config_registry.md#qwen3_moe_235b_fsdp_smoke), [`qwen3_moe_30b_fsdp_only_full_ac_benchmark`](qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_benchmark), [`build_cross_entropy_loss`](loss.md#build_cross_entropy_loss), [`_compiled_grad_norm`](train.md#TPUTrainer._compiled_grad_norm), [`flux_dev_mxfp8`](../../models/flux/config_registry.md#flux_dev_mxfp8), [`flux_schnell_mxfp8`](../../models/flux/config_registry.md#flux_schnell_mxfp8)  (+33 more; 31 test-only)

### <a id="TpuTrainerCompileConfig"></a>`TpuTrainerCompileConfig`  ·  implements/extends CompileConfig
- def: [`torchtitan/experiments/tpu/tpu_job_config.py:45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L45) — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)
- doc: Generic compile policy plus regular-Trainer TorchTPU controls.
- signature: `class TpuTrainerCompileConfig(torchtitan.config.CompileConfig):`
- members:
  - <a id="TpuTrainerCompileConfig.compile_grad_norm"></a>`compile_grad_norm` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L60)
  - <a id="TpuTrainerCompileConfig.materialize_forward_before_backward"></a>`materialize_forward_before_backward` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L55)
  - <a id="TpuTrainerCompileConfig.mode"></a>`mode` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L50)
  - <a id="TpuTrainerCompileConfig.optimizer_compile"></a>`optimizer_compile` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L58)
- uses (calls/refs, reference-scoped): [`CompileConfig`](../../config/configs.md#CompileConfig), [`TpuTrainerCompileMode`](tpu_job_config.md#TpuTrainerCompileMode), [`TpuTrainerOptimizerCompileMode`](tpu_job_config.md#TpuTrainerOptimizerCompileMode)
- used by: [`sft_llama3_8b_metamath`](llama3/config_registry.md#sft_llama3_8b_metamath), [`reg_trainer_qwen3_8b`](qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](llama3/config_registry.md#llama3_70b), [`llama3_405b`](llama3/config_registry.md#llama3_405b), [`llama3_8b`](llama3/config_registry.md#llama3_8b), [`_muse_glimmer_30b_base`](muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`_tpu_hf_config`](transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`CompileConfig`](../../config/configs.md#CompileConfig), [`qwen35_moe_35b`](qwen3_5/config_registry.md#qwen35_moe_35b), [`start_trainer`](train.md#start_trainer), [`parallelize_conformer`](conformer/infra/parallelize.md#parallelize_conformer), [`compile`](tpu_job_config.md#TPUTrainerConfig.compile), [`forward_backward_step`](train.md#TPUTrainer.forward_backward_step), [`__post_init__`](tpu_job_config.md#TPUTrainerConfig.__post_init__), [`_compiled_grad_norm`](train.md#TPUTrainer._compiled_grad_norm), [`reg_trainer_muse_glimmer_30b_fused_ce`](muse_glimmer/config_registry.md#reg_trainer_muse_glimmer_30b_fused_ce), [`apply_compile`](conformer/infra/parallelize.md#apply_compile), [`patched_parallelize`](train.md#start_trainer.patched_parallelize)  (6 test-only)

## Module values
- <a id="TpuTrainerCompileMode"></a>`TpuTrainerCompileMode` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L40)
- <a id="TpuTrainerOptimizerCompileMode"></a>`TpuTrainerOptimizerCompileMode` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tpu_job_config.py#L41)

