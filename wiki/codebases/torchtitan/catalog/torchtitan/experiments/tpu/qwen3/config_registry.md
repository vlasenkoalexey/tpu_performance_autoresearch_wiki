---
title: 'Module: torchtitan/experiments/tpu/qwen3/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.config_registry`/
symbols:
  qwen3_8b: qwen3_8b().
  reg_trainer_qwen3_8b: reg_trainer_qwen3_8b().
  qwen3_1_7b: qwen3_1_7b().
  _qwen3_moe_30b_fsdp_only_full_ac: _qwen3_moe_30b_fsdp_only_full_ac().
  qwen3_moe_30b: qwen3_moe_30b().
  qwen3_debugmodel: qwen3_debugmodel().
  qwen3_moe_235b_scan: qwen3_moe_235b_scan().
  _qwen3_moe_235b_fsdp_only: _qwen3_moe_235b_fsdp_only().
  qwen3_32b: qwen3_32b().
  _qwen3_cp: _qwen3_cp().
  qwen3_moe_testmodel: qwen3_moe_testmodel().
  qwen3_moe_235b_fsdp_smoke: qwen3_moe_235b_fsdp_smoke().
  qwen3_moe_30b_fsdp_only_full_ac_benchmark: qwen3_moe_30b_fsdp_only_full_ac_benchmark().
  _qwen3_moe_235b_fsdp_activation_offload: _qwen3_moe_235b_fsdp_activation_offload().
  qwen3_8b_zero3: qwen3_8b_zero3().
  qwen3_moe_235b_scan_proxy: qwen3_moe_235b_scan_proxy().
  qwen3_moe_30b_fsdp_only_full_ac_profile: qwen3_moe_30b_fsdp_only_full_ac_profile().
  qwen3_moe_235b_fsdp_activation_offload_maxtext: qwen3_moe_235b_fsdp_activation_offload_maxtext().
  _qwen3_dense_model_spec: _qwen3_dense_model_spec().
  qwen3_moe_235b_scan_maxtext: qwen3_moe_235b_scan_maxtext().
  graph_trainer_qwen3_debugmodel: graph_trainer_qwen3_debugmodel().
  _use_maxtext_flops: _use_maxtext_flops().
  qwen3_moe_235b_fsdp_activation_offload_4x4x4: qwen3_moe_235b_fsdp_activation_offload_4x4x4().
  qwen3_moe_235b_scan_torchao_float8: qwen3_moe_235b_scan_torchao_float8().
  qwen3_8b_maxtext_parity: qwen3_8b_maxtext_parity().
  qwen3_32b_4x8x8: qwen3_32b_4x8x8().
  qwen3_32b_maxtext_parity: qwen3_32b_maxtext_parity().
  qwen3_debugmodel_allgather_cp2: qwen3_debugmodel_allgather_cp2().
  _configure_qwen3_moe_235b_fsdp_128: _configure_qwen3_moe_235b_fsdp_128().
  qwen3_moe_30b_proxy: qwen3_moe_30b_proxy().
  _enable_pallas_cross_entropy: _enable_pallas_cross_entropy().
  _use_global_batch_aux_loss: _use_global_batch_aux_loss().
  _Q235_SCAN_FLAGS: _Q235_SCAN_FLAGS.
  qwen3_moe_30b_fsdp_only_attention_parity_benchmark: qwen3_moe_30b_fsdp_only_attention_parity_benchmark().
  _scale_routes_before_down_proj: _scale_routes_before_down_proj().
  _qwen3_1_7b_32k: _qwen3_1_7b_32k().
  qwen3_moe_30b_fsdp_only_maxtext_benchmark: qwen3_moe_30b_fsdp_only_maxtext_benchmark().
  _without_splash_saves: _without_splash_saves().
  qwen3_moe_235b_fsdp_activation_offload_maxtext_4x4x4: qwen3_moe_235b_fsdp_activation_offload_maxtext_4x4x4().
  _Q235_COMPILED_OFFLOAD_FLAGS: _Q235_COMPILED_OFFLOAD_FLAGS.
  _QWEN3_DENSE_4X4X4_FLAGS: _QWEN3_DENSE_4X4X4_FLAGS.
  qwen3_debugmodel_ulysses_cp2: qwen3_debugmodel_ulysses_cp2().
  qwen3_moe_235b_hsdp_activation_offload_maxtext: qwen3_moe_235b_hsdp_activation_offload_maxtext().
  qwen3_1_7b_allgather_cp4: qwen3_1_7b_allgather_cp4().
  qwen3_1_7b_ulysses_cp4: qwen3_1_7b_ulysses_cp4().
  _Q235_SHARED_FLAGS: _Q235_SHARED_FLAGS.
  _BF16_ROPE_OVERRIDE: _BF16_ROPE_OVERRIDE.
  _FUSED_LOSS_OVERRIDE: _FUSED_LOSS_OVERRIDE.
  _DISCARDED_TOKEN_COUNTER_OVERRIDE: _DISCARDED_TOKEN_COUNTER_OVERRIDE.
---
# Module: [`torchtitan/experiments/tpu/qwen3/config_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py)

## Functions
- <a id="_configure_qwen3_moe_235b_fsdp_128"></a>`_configure_qwen3_moe_235b_fsdp_128(cfg: TpuGraphTrainer.Config, *, replicate_degree: int)` — [`L1065`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1065) — Configure an FSDP-128 mesh and its matching global batch size.
- <a id="_enable_pallas_cross_entropy"></a>`_enable_pallas_cross_entropy(config: TPUTrainerConfig)` — [`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L166) — Select the fused loss and its pre-construction LM-head override together.
- <a id="_qwen3_1_7b_32k"></a>`_qwen3_1_7b_32k()` — [`L463`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L463) — Qwen3 1.7B at 32k context, one sequence per data-parallel rank.
- <a id="_qwen3_cp"></a>`_qwen3_cp(config: TPUTrainerConfig, *, strategy: Literal["ulysses", "all_gather"], cp_degree: int)` — [`L418`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L418) — Enables TPU context parallelism, following pattern set by upstream torchtitan_recipes/muse_glimmer.py for CUDA.
- <a id="_qwen3_dense_model_spec"></a>`_qwen3_dense_model_spec(flavor: str)` — [`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L544)
- <a id="_qwen3_moe_235b_fsdp_activation_offload"></a>`_qwen3_moe_235b_fsdp_activation_offload()` — [`L1017`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1017) — Add the common Q235 activation-offload execution policy.
- <a id="_qwen3_moe_235b_fsdp_only"></a>`_qwen3_moe_235b_fsdp_only()` — [`L942`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L942) — Build the common Qwen3 235B-A22B FSDP configuration. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="_qwen3_moe_30b_fsdp_only_full_ac"></a>`_qwen3_moe_30b_fsdp_only_full_ac()` — [`L797`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L797) — Batch-6 FSDP128 baseline with local dropless expert dispatch. — documented in [debug-and-profiling-tools](../../../../../concepts/debug-and-profiling-tools.md)
- <a id="_scale_routes_before_down_proj"></a>`_scale_routes_before_down_proj(cfg: TPUTrainerConfig)` — [`L932`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L932) — Apply routing scores before W2 so remat does not replay the W2 forward.
- <a id="_use_global_batch_aux_loss"></a>`_use_global_batch_aux_loss(config: TPUTrainerConfig)` — [`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L173) — Use Qwen's global auxiliary load-balancing loss for every MoE layer.
- <a id="_use_maxtext_flops"></a>`_use_maxtext_flops(config: TPUTrainerConfig)` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L151) — Report MaxText FLOPs and MFU instead of upstream torchtitan's.
- <a id="_without_splash_saves"></a>`_without_splash_saves(cfg: TpuGraphTrainer.Config)` — [`L1048`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1048) — Fall back to plain offload; the Splash saves were measured only at w512.
- <a id="graph_trainer_qwen3_debugmodel"></a>`graph_trainer_qwen3_debugmodel()` — [`L230`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L230) — Qwen3 debug model using TPU GraphTrainer.
- <a id="qwen3_1_7b"></a>`qwen3_1_7b()` — [`L272`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L272) — Qwen3 1.7B model configuration for TPU. — documented in [model-spec-protocols](../../../../../concepts/model-spec-protocols.md)
- <a id="qwen3_1_7b_allgather_cp4"></a>`qwen3_1_7b_allgather_cp4()` — [`L471`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L471) — Qwen3 1.7B at 32k context with load-balanced KV all-gather CP degree 4.
- <a id="qwen3_1_7b_ulysses_cp4"></a>`qwen3_1_7b_ulysses_cp4()` — [`L476`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L476) — Qwen3 1.7B at 32k context with Ulysses (all-to-all) CP degree 4.
- <a id="qwen3_32b"></a>`qwen3_32b()` — [`L677`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L677) — Qwen3 32B recipe for a tpu7x-4x4x4 slice. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="qwen3_32b_4x8x8"></a>`qwen3_32b_4x8x8()` — [`L704`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L704) — Qwen3 32B recipe for a tpu7x-4x8x8 slice (512 devices).
- <a id="qwen3_32b_maxtext_parity"></a>`qwen3_32b_maxtext_parity()` — [`L726`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L726) — Qwen3 32B recipe with MaxText's BF16 reductions and BF16 RoPE.
- <a id="qwen3_8b"></a>`qwen3_8b()` — [`L555`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L555) — Qwen3 8B model configuration for TPU. — documented in [checkpointing](../../../../../concepts/checkpointing.md)
- <a id="qwen3_8b_maxtext_parity"></a>`qwen3_8b_maxtext_parity()` — [`L652`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L652) — Qwen3 8B recipe matching currently available MaxText policies.
- <a id="qwen3_8b_zero3"></a>`qwen3_8b_zero3()` — [`L640`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L640) — Qwen3 8B GraphTrainer recipe retaining sharded parameters after forward.
- <a id="qwen3_debugmodel"></a>`qwen3_debugmodel()` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L183) — Qwen3 debug model configuration for TPU.
- <a id="qwen3_debugmodel_allgather_cp2"></a>`qwen3_debugmodel_allgather_cp2()` — [`L445`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L445) — Qwen3 debug model with load-balanced KV all-gather CP degree 2.
- <a id="qwen3_debugmodel_ulysses_cp2"></a>`qwen3_debugmodel_ulysses_cp2()` — [`L458`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L458) — Qwen3 debug model with Ulysses (all-to-all) CP degree 2.
- <a id="qwen3_moe_235b_fsdp_activation_offload_4x4x4"></a>`qwen3_moe_235b_fsdp_activation_offload_4x4x4()` — [`L1093`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1093) — FP32-reduction Q235 offload recipe for a 4x4x4 TPU7x slice.
- <a id="qwen3_moe_235b_fsdp_activation_offload_maxtext"></a>`qwen3_moe_235b_fsdp_activation_offload_maxtext()` — [`L1054`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1054) — MaxText-numerics variant of the Q235 activation-offload recipe.
- <a id="qwen3_moe_235b_fsdp_activation_offload_maxtext_4x4x4"></a>`qwen3_moe_235b_fsdp_activation_offload_maxtext_4x4x4()` — [`L1112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1112) — MaxText-numerics Q235 offload recipe for a 4x4x4 TPU7x slice.
- <a id="qwen3_moe_235b_fsdp_smoke"></a>`qwen3_moe_235b_fsdp_smoke()` — [`L1120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1120) — Four-layer FSDP512 smoke for the production 235B execution path.
- <a id="qwen3_moe_235b_hsdp_activation_offload_maxtext"></a>`qwen3_moe_235b_hsdp_activation_offload_maxtext()` — [`L1082`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1082) — MaxText-numerics Q235 offload recipe using 4x128 HSDP.
- <a id="qwen3_moe_235b_scan"></a>`qwen3_moe_235b_scan()` — [`L1141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1141) — Qwen3 235B-A22B on the graph trainer with its 94 layers scanned. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="qwen3_moe_235b_scan_maxtext"></a>`qwen3_moe_235b_scan_maxtext()` — [`L1267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1267) — `qwen3_moe_235b_scan` with MaxText's numerics instead of torchtitan's.
- <a id="qwen3_moe_235b_scan_proxy"></a>`qwen3_moe_235b_scan_proxy()` — [`L1249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1249) — `qwen3_moe_235b_scan` cut to 12 of its 94 layers, so it fits a 32-chip slice.
- <a id="qwen3_moe_235b_scan_torchao_float8"></a>`qwen3_moe_235b_scan_torchao_float8()` — [`L1223`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1223) — `qwen3_moe_235b_scan` with torchao rowwise float8 dense linears.
- <a id="qwen3_moe_30b"></a>`qwen3_moe_30b()` — [`L735`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L735) — TPU specialization of the global-aux Qwen3 30B recipe. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="qwen3_moe_30b_fsdp_only_attention_parity_benchmark"></a>`qwen3_moe_30b_fsdp_only_attention_parity_benchmark()` — [`L902`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L902) — Q30 benchmark adding MaxText's BF16 RoPE numerical policy.
- <a id="qwen3_moe_30b_fsdp_only_full_ac_benchmark"></a>`qwen3_moe_30b_fsdp_only_full_ac_benchmark()` — [`L892`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L892) — Profiler-free bracket for the batch-6 FSDP128 comparison.
- <a id="qwen3_moe_30b_fsdp_only_full_ac_profile"></a>`qwen3_moe_30b_fsdp_only_full_ac_profile()` — [`L880`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L880) — Profile the batch-6 FSDP128 baseline on rank zero.
- <a id="qwen3_moe_30b_fsdp_only_maxtext_benchmark"></a>`qwen3_moe_30b_fsdp_only_maxtext_benchmark()` — [`L919`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L919) — Q30 benchmark with MaxText's numerics and FLOP accounting.
- <a id="qwen3_moe_30b_proxy"></a>`qwen3_moe_30b_proxy()` — [`L1282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L1282) — Proxy model for Qwen3 30B MoE (4 layers instead of 48) for testing/iterations.
- <a id="qwen3_moe_testmodel"></a>`qwen3_moe_testmodel()` — [`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L242) — Qwen3 MoE test model configuration for TPU.
- <a id="reg_trainer_qwen3_8b"></a>`reg_trainer_qwen3_8b()` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L344) — Qwen3 8B model configuration for TPU (regular trainer). — documented in [job-config](../../../../../concepts/job-config.md)

## Module values
- <a id="_BF16_ROPE_OVERRIDE"></a>`_BF16_ROPE_OVERRIDE` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L76)
- <a id="_DISCARDED_TOKEN_COUNTER_OVERRIDE"></a>`_DISCARDED_TOKEN_COUNTER_OVERRIDE` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L80)
- <a id="_FUSED_LOSS_OVERRIDE"></a>`_FUSED_LOSS_OVERRIDE` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L73)
- <a id="_Q235_COMPILED_OFFLOAD_FLAGS"></a>`_Q235_COMPILED_OFFLOAD_FLAGS` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L110)
- <a id="_Q235_SCAN_FLAGS"></a>`_Q235_SCAN_FLAGS` — [`L126`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L126)
- <a id="_Q235_SHARED_FLAGS"></a>`_Q235_SHARED_FLAGS` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L87)
- <a id="_QWEN3_DENSE_4X4X4_FLAGS"></a>`_QWEN3_DENSE_4X4X4_FLAGS` — [`L669`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/config_registry.py#L669)

