---
title: JAX lane - Flax NNX trainer on TPU
type: doc-concept
provenance: doc
source: torchtitan/experiments/jax/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# JAX lane - Flax NNX trainer on TPU

## Definition
The `jax` experiment trains LLMs on TPU in **pure JAX with Flax NNX and optax** - no PyTorch in the training path. It is single-process, multi-device (JAX discovers all local TPU chips, no `torchrun`), uses scan-over-layers for a constant-size XLA graph, shards parameters over a named `(fsdp, tp)` mesh, and can swap in the Pallas splash-attention kernel. Model coverage is Llama 3 (8B, 70B, plus a debug model). It reuses the TPU lane's job-config schema, so it doubles as a JAX-native reference point for the torch-on-TPU lanes.

## In torchtitan (grounded)
- Entry point: [`main`](../catalog/torchtitan/experiments/jax/train_minimal.md#main) in `train_minimal.py` parses flags, builds the mesh and runs [`main_train_loop`](../catalog/torchtitan/experiments/jax/train_minimal.md#main_train_loop).
- Trainer: [`JaxTrainer`](../catalog/torchtitan/experiments/jax/trainer.md#JaxTrainer) - [`JaxTrainer.setup_model`](../catalog/torchtitan/experiments/jax/trainer.md#JaxTrainer.setup_model) (model build, AC policy, splash), [`JaxTrainer.setup_optimizer`](../catalog/torchtitan/experiments/jax/trainer.md#JaxTrainer.setup_optimizer) (optax `adamw` / `adam` / `sgd`), [`JaxTrainer.train`](../catalog/torchtitan/experiments/jax/trainer.md#JaxTrainer.train).
- Config: [`JaxJobConfig`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxJobConfig) extends the TPU lane's [`BaseTPUTrainerConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig) with [`JaxConfig`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig): [`use_scan`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.use_scan) (default True), [`tpu_megacore`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.tpu_megacore) (default True), [`tpu_num_slices`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.tpu_num_slices), [`model_layer_override`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.model_layer_override), [`adamw_bf16_state`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.adamw_bf16_state).
- Kernels and data: [`make_splash_attention_fn`](../catalog/torchtitan/experiments/jax/splash_attn.md#make_splash_attention_fn) / [`build_splash_attention_callable`](../catalog/torchtitan/experiments/jax/splash_attn.md#build_splash_attention_callable); [`torch_loader_to_jax`](../catalog/torchtitan/experiments/jax/data_utils.md#torch_loader_to_jax) bridges the torchtitan dataloader (or `--training.dataset=fake`).
- Metrics: [`JaxMetricsProcessor`](../catalog/torchtitan/experiments/jax/metrics.md#JaxMetricsProcessor) logs TPS, TFLOPs, MFU using [`get_peak_flops`](../catalog/torchtitan/experiments/jax/metrics.md#get_peak_flops). Profiling via [`maybe_enable_profiling`](../catalog/torchtitan/experiments/jax/jax_profiling.md#maybe_enable_profiling).

## Why it matters / when it applies
- **Reported performance (README):** Llama3 8B, scan + full AC, seq 2048, batch 4 on v6e-4 -> ~20% MFU after warmup. This is the lane's only published number; treat it as a baseline, not a ceiling.
- **Key flags:** `--jax_config.use_scan`, `--parallelism.tensor_parallel_degree`, `--activation_checkpoint.mode` (`full` / `selective` / none), `--jax_config.model_layer_override=2` for a 2-layer debug model.
- **Memory knob (code, undocumented in the README):** `--jax_config.adamw_bf16_state` stores both Adam moments in bf16 (upcast per-leaf inside the update, [`_scale_by_adam_bf16_state`](../catalog/torchtitan/experiments/jax/trainer.md#_scale_by_adam_bf16_state)); the docstring motivates it with Llama3 8B on v6e-4, where fp32 `nu` for the stacked MLP kernel alone is ~3.5 GiB/chip.
- **Flax 0.11+ NNX notes:** `nnx.Optimizer(model, tx, wrt=nnx.Param)` needs explicit `wrt`; `optimizer.update(model, grads)` takes the model explicitly; grads are filtered with `nnx.DiffState(0, nnx.Param)`.

**Doc vs code at this commit:**
- `tpu_megacore` is described as "Enable megacore (v4/v5p)". In code it is only read by `get_peak_flops`, where it doubles per-core peak FLOPs for v4/v5p in the MFU denominator; it does not change how the program runs.
- Splash attention is listed as a lane feature but is opt-in: it is used only when `--splash_attention_kernel.use_splash_attention_kernel` is set on TPU (default False, inherited from the TPU config), else attention falls back to the model's default path.
- The README says the lane is "parallel to `torchtitan/experiments/torchax/`"; there is no `torchax` experiment directory in this checkout.

## Connections
- Code concepts: [jax-lane](../concepts/jax-lane.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md), [llama3-model](../concepts/llama3-model.md), [observability](../concepts/observability.md)
- Module catalogs: [jax/trainer](../catalog/torchtitan/experiments/jax/trainer.md), [jax/train_minimal](../catalog/torchtitan/experiments/jax/train_minimal.md), [jax/jax_job_config](../catalog/torchtitan/experiments/jax/jax_job_config.md), [jax/splash_attn](../catalog/torchtitan/experiments/jax/splash_attn.md), [jax/metrics](../catalog/torchtitan/experiments/jax/metrics.md)
- Related doc-concepts: [jax-scan-over-layers](jax-scan-over-layers.md), [jax-fsdp-tp-mesh-sharding](jax-fsdp-tp-mesh-sharding.md), [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md), [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md), [experiments-contribution-contract](experiments-contribution-contract.md)

## Source
Extracted from `torchtitan/experiments/jax/README.md` (kept in place).
