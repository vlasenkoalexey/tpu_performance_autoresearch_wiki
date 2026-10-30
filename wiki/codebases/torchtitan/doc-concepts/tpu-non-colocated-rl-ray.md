---
title: Non-colocated GRPO on TPU with Ray (separate trainer and vLLM generator slices)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/rl_nc_ray/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Non-colocated GRPO on TPU with Ray (separate trainer and vLLM generator slices)

## Definition
A decoupled RL (GRPO) layout where the policy trainer (TorchTitan) and the rollout generator (vLLM on
TorchTPU) run on **separate TPU slices**, so training weights/gradients and the vLLM KV cache never
compete for the same HBM. A Ray orchestrator on the head node launches remote trainer and generator
actors and moves the policy state dict between them through Ray's object store, replacing the
Monarch actors / torchstore of the upstream RL experiment.

## In torchtitan (grounded)
- Orchestrator: `rl_nc_ray/grpo.py` - [`RayController`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/grpo.md#RayController),
  proxies [`RayTrainerProxy`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/grpo.md#RayTrainerProxy) and
  [`RayInterGeneratorRouter`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/grpo.md#RayInterGeneratorRouter),
  entry [`main`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/grpo.md#main).
- Trainer actor: [`RayTPUPolicyTrainer`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/trainer.md#RayTPUPolicyTrainer),
  a `@ray.remote` subclass of upstream [`PolicyTrainer`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer);
  its device comes from `TORCHTITAN_DEVICE_TYPE` (default `cpu`, gloo PG), and it forces the optimizer
  to `foreach` ("TPU does not support fused AdamW natively").
- Generator actor: [`RayVLLMGenerator`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/generator.md#RayVLLMGenerator)
  with vLLM patches [`patch_vllm_for_tpu`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/generator.md#patch_vllm_for_tpu).
- Weight sync: [`prepare_trainer_state_dict`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.md#prepare_trainer_state_dict)
  replicates DTensors over ICI and concatenates parameters by dtype on device to reduce PCIe and
  object-store overhead; [`SYNC_LAYER_BY_LAYER`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.md#SYNC_LAYER_BY_LAYER)
  (True) syncs block by block because whole-model redistribution caused an HBM peak and OOM.
- Static shapes for the trainer: [`pad_train_batch_to_static`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.md#pad_train_batch_to_static)
  pads token ids / advantages / lengths to [`PAD_LEN`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/trainer.md#PAD_LEN)
  (4096) and [`MAX_SEQS`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/trainer.md#MAX_SEQS) (64) to
  avoid constant Dynamo recompiles from fluctuating batch layouts.
- Runtime env per process: [`build_trainer_env_vars`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.md#build_trainer_env_vars),
  [`build_generator_env_vars`](../catalog/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.md#build_generator_env_vars):
  PJRT preallocates ~90% of HBM by default, so the lane sets `XLA_PYTHON_CLIENT_PREALLOCATE=false`,
  memory fractions 0.45, and `--xla_tpu_use_enhanced_launch_barrier=false` (multiple runtimes per host).

### Scripts / launch
- `smoke_test_vm_tp1.sh` (CPU trainer + TPU generator, single slice), `smoke_test_vm_tp4.sh`
  (generator TP=4 on the `torchtpu-vllm` multi-process worker).
- `e2e_recipe_gke.sh {0.6b|1.7b|4b}` -> configs `rl_grpo_qwen3_{0_6b,1_7b,4b}_varlen`, submitted with
  `ray job submit` to a KubeRay cluster (`scripts/ray-v6e8-2.yaml`, GCS FUSE at `/data`, Workload
  Identity on `ray-ksa`); `plot_metrics_from_log.py` plots reward / loss / gen time / train time.

## Why it matters / when it applies
- Choose non-colocated when trainer state + KV cache do not fit one slice's HBM together; the cost is
  a per-step weight transfer, which is why the ICI replicate + dtype-concat + layer-by-layer sync path
  matters for step time.
- Generator throughput scales with vLLM TP (8 on the GKE recipe).

**Doc vs code:** the README says the GKE recipe uses "2D sharding (FSDP x DP) for the Policy
Trainer". `e2e_recipe_gke.sh` actually passes `--trainer.parallelism.tensor-parallel-degree 8
--trainer.parallelism.data_parallel_shard_degree 1` (TP=8, no FSDP split) and `--compile.no-enable`.
The trainer module docstring also says it "runs exclusively on CPU"; the code makes that the
*default* (`TORCHTITAN_DEVICE_TYPE` unset) with a TPU path selectable through the cluster layout.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [checkpointing](../concepts/checkpointing.md), [qwen3-model](../concepts/qwen3-model.md)
- Module catalogs: [rl_nc_ray/grpo](../catalog/torchtitan/experiments/tpu/rl_nc_ray/grpo.md),
  [rl_nc_ray/trainer](../catalog/torchtitan/experiments/tpu/rl_nc_ray/trainer.md),
  [rl_nc_ray/generator](../catalog/torchtitan/experiments/tpu/rl_nc_ray/generator.md),
  [rl_nc_ray/weight_transfer_utils](../catalog/torchtitan/experiments/tpu/rl_nc_ray/weight_transfer_utils.md),
  [rl_nc_ray/tpu_env_utils](../catalog/torchtitan/experiments/tpu/rl_nc_ray/tpu_env_utils.md),
  [rl_nc_ray/padding_packing_utils](../catalog/torchtitan/experiments/tpu/rl_nc_ray/padding_packing_utils.md)
- Related doc-concepts: [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md)

## Source
Extracted from `torchtitan/experiments/tpu/rl_nc_ray/README.md` (kept in place), cross-checked
against `rl_nc_ray/scripts/e2e_recipe_gke.sh`, `trainer.py`, `tpu_env_utils.py`.
