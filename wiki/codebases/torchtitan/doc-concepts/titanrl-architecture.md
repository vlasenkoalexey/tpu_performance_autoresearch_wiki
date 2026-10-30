---
title: TitanRL architecture (unified model, async rollout pipeline, Monarch actors)
type: doc-concept
provenance: doc
source: torchtitan/experiments/rl/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TitanRL architecture (unified model, async rollout pipeline, Monarch actors)

## Definition
TitanRL is the RL post-training library in `experiments/rl`. Its three selling points: (1) a **unified model definition** - (mostly) the same TorchTitan model runs inside the trainer and inside vLLM for generation (attention modules differ but share kernels), so a new model or kernel is written once; (2) an optional **batch-invariant mode** giving bitwise-identical log-probs between trainer and generator; (3) **one stack** from pretraining to post-training. The pipeline has three layers: experiment logic (a `Rollouter`), controller/dataflow (independent async loops joined by a bounded work buffer), and distributed execution (vLLM generator replicas behind a router, a trainer on its own TorchTitan mesh, weight publishing back to generators).

## In torchtitan (grounded)
- Controller: [`Controller`](../catalog/torchtitan/experiments/rl/controller.md#Controller) runs [`Controller._data_input_loop`](../catalog/torchtitan/experiments/rl/controller.md#Controller._data_input_loop), [`Controller._rollout_loop`](../catalog/torchtitan/experiments/rl/controller.md#Controller._rollout_loop), [`Controller._batcher_loop`](../catalog/torchtitan/experiments/rl/controller.md#Controller._batcher_loop) and [`Controller._trainer_loop`](../catalog/torchtitan/experiments/rl/controller.md#Controller._trainer_loop), configured by [`AsyncLoopConfig`](../catalog/torchtitan/experiments/rl/controller.md#AsyncLoopConfig). Loops meet at [`RolloutGroupWorkBuffer`](../catalog/torchtitan/experiments/rl/components/work_buffer.md#RolloutGroupWorkBuffer), which bounds policy lag (see [rl-windowed-fifo-scheduling](rl-windowed-fifo-scheduling.md)).
- Execution actors: [`PolicyTrainer`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer) (TorchTitan training on its own mesh; [`PolicyTrainer.forward_backward`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer.forward_backward), [`PolicyTrainer.push_model_state_dict`](../catalog/torchtitan/experiments/rl/actors/trainer.md#PolicyTrainer.push_model_state_dict)); [`VLLMGenerator`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator) (vLLM engine replica; [`VLLMGenerator.pull_model_state_dict`](../catalog/torchtitan/experiments/rl/actors/generator.md#VLLMGenerator.pull_model_state_dict)); routing by [`InterGeneratorRouter`](../catalog/torchtitan/experiments/rl/routing/inter_generator_router.md#InterGeneratorRouter); push/pull orchestration by [`WeightSyncManager`](../catalog/torchtitan/experiments/rl/components/weight_sync.md#WeightSyncManager). Host placement: [`PerHostProvisioner`](../catalog/torchtitan/experiments/rl/train.md#PerHostProvisioner) in [`main`](../catalog/torchtitan/experiments/rl/train.md#main).
- Unified model in vLLM: [`VLLMModelWrapper`](../catalog/torchtitan/experiments/rl/models/vllm_wrapper.md#VLLMModelWrapper) adapts a TorchTitan model to the vLLM V1 engine; [`VLLMAttentionWrapper`](../catalog/torchtitan/experiments/rl/models/attention.md#VLLMAttentionWrapper) and [`PyTorchVarlenInnerAttentionBackend`](../catalog/torchtitan/experiments/rl/models/attention.md#PyTorchVarlenInnerAttentionBackend) let vLLM call TorchTitan's [`VarlenInnerAttention`](../catalog/torchtitan/models/common/attention.md#VarlenInnerAttention); [`InferenceParallelismConfig`](../catalog/torchtitan/experiments/rl/models/vllm_registry.md#InferenceParallelismConfig) sizes generator DP/TP independently of the trainer.
- External components (no catalog symbols): Monarch as the actor controller over separate process meshes; TorchStore for trainer -> generator weight publishing (including direct GPU-to-GPU RDMA).

## Why it matters / when it applies
- Training and generation scale independently (e.g. the DAPO recipe: one TP=2 trainer + six TP=1 generators on 8 GPUs).
- The README is explicit that unified-model inference can trail native vLLM on inference-only workloads but can win end-to-end in some RL configurations; batch invariance trades throughput for exact numerics.
- **Monarch rule:** every actor endpoint (`PolicyTrainer`, `VLLMGenerator`, ...) uses `@concurrent_endpoint`, never plain `@endpoint`. A plain endpoint blocks the actor's queue - and on an actor mixing both kinds it blocks the concurrent ones too - so any future `@endpoint` must justify itself in its docstring.
- Observability has four views: structured-logger Gantt timelines, typed per-step metrics ([rl-typed-metrics-reduction](rl-typed-metrics-reduction.md)), vLLM engine health ([vllm-otel-engine-metrics](vllm-otel-engine-metrics.md)), and rollout samples via [`RolloutSampleRecorder`](../catalog/torchtitan/experiments/rl/rollout_recorder.md#RolloutSampleRecorder). `PolicyTrainer` does not yet support the core `Profiler.Config` (README TODO).
- **TPU relevance.** TitanRL is GPU-only at this commit (vLLM CUDA wheels, FA3/FA4, NCCL, Monarch GPU meshes). Its trainer side still reuses core TorchTitan parallelism, so trainer-side lessons transfer; generator-side ones do not.

**Doc vs code at this commit:** the README says "Set `max_offpolicy_steps=0` for synchronous execution". `max_offpolicy_steps` is a derived read-only property of `AsyncLoopConfig`. The settable knob is `target_offpolicy_steps`, and with the default `window_fraction=0.3` the derived bound can still be 1 at `target_offpolicy_steps=0`; use `window_fraction=None` too for strictly on-policy runs.

## Connections
- Code concepts: [rl-training](../concepts/rl-training.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md), [model-building-blocks](../concepts/model-building-blocks.md), [observability](../concepts/observability.md), [checkpointing](../concepts/checkpointing.md)
- Module catalogs: [rl/controller](../catalog/torchtitan/experiments/rl/controller.md), [rl/actors/trainer](../catalog/torchtitan/experiments/rl/actors/trainer.md), [rl/actors/generator](../catalog/torchtitan/experiments/rl/actors/generator.md), [rl/models/vllm_wrapper](../catalog/torchtitan/experiments/rl/models/vllm_wrapper.md), [rl/components/weight_sync](../catalog/torchtitan/experiments/rl/components/weight_sync.md)
- Related doc-concepts: [titanrl-rollouter-api](titanrl-rollouter-api.md), [rl-batch-invariance-bitwise-parity](rl-batch-invariance-bitwise-parity.md), [rl-windowed-fifo-scheduling](rl-windowed-fifo-scheduling.md), [rl-dapo-math-recipe](rl-dapo-math-recipe.md), [rl-search-r1-multiturn-tool-use](rl-search-r1-multiturn-tool-use.md), [rl-verifiers-integration](rl-verifiers-integration.md)

## Source
Extracted from `torchtitan/experiments/rl/README.md` (kept in place).
