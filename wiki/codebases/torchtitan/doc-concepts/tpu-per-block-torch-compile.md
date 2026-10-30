---
title: Per-block torch.compile on TorchTPU (and compiling the glue)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Per-block torch.compile on TorchTPU (and compiling the glue)

## Definition
`torch.compile(backend="tpu")` fuses the ops inside a captured region into one XLA program,
collapsing many eager dispatches into a few. The guide calls it **mandatory** for any performance
run (typically a "solid double-digit-percent speedup" on its own) and prescribes **transformer-block
granularity** with static shapes: fuse within each block, keep activation checkpointing between
blocks so memory stays bounded. Whole-model compile is discouraged; the residual glue (loss,
optimizer step, grad norm) has its own compile switches, and whole-step capture belongs to
GraphTrainer.

## In torchtitan (grounded)
- **Knobs** on [`TpuTrainerCompileConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig)
  (extends core [`CompileConfig`](../catalog/torchtitan/config/configs.md#CompileConfig): `enable`,
  `backend`, `components`):
  - [`mode`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.mode):
    `"layer"` (default, per block), `"fullgraph"`, `"whole"`, `"block"` - support differs by model
    family (Llama/Qwen: layer/fullgraph).
  - [`optimizer_compile`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.optimizer_compile):
    `"eager"` or `"separate_graph"` (AdamW step captured as one FX graph via
    [`apply_compiled_optimizer`](../catalog/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.md#apply_compiled_optimizer)).
  - [`compile_grad_norm`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.compile_grad_norm):
    global grad norm as a static graph ([`CompiledGradNorm`](../catalog/torchtitan/experiments/tpu/grad_norm.md#CompiledGradNorm));
    the in-place clip stays eager. Rejected with EP > 1 or PP > 1
    ([`TPUTrainerConfig.__post_init__`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUTrainerConfig.__post_init__)).
  - [`materialize_forward_before_backward`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TpuTrainerCompileConfig.materialize_forward_before_backward):
    [`TPUTrainer.forward_backward_step`](../catalog/torchtitan/experiments/tpu/train.md#TPUTrainer.forward_backward_step)
    calls torch_tpu `synchronize(loss, wait=False)` between forward+loss and backward, splitting one
    lazy XLA graph into two and cutting first-step compile time (skipped under PP). This is one runtime
    boundary, not GraphTrainer's multi-executable splitter.
  - `"loss"` in `compile.components` compiles the loss function.
- **Per-block path.** Llama3 on TPU ([`parallelize_llama`](../catalog/torchtitan/experiments/tpu/llama3/infra/parallelize.md#parallelize_llama))
  forwards to the core model parallelizer, which calls core
  [`apply_compile`](../catalog/torchtitan/distributed/compile.md#apply_compile): each block gets
  `transformer_block.compile(backend=..., fullgraph=True)`. With `mode="fullgraph"` it instead disables
  per-layer compile and wraps the whole model in `torch.compile(model, fullgraph=True, backend="tpu")`;
  [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer) logs a warning that
  the optimizer step is still outside the graph.
- [`raise_dynamo_recompile_limits`](../catalog/torchtitan/experiments/tpu/workarounds.md#raise_dynamo_recompile_limits)
  raises Dynamo's recompile limit to `max(64, 2 x n_layers + 16)`: SimpleFSDP parametrization / AC
  wrapping gives each layer its own module class, so the shared checkpoint wrapper re-guards per layer
  and the default limit of 8 fails hard at 52/80 layers.

## Why it matters / when it applies
- **Static shapes.** Training runs at fixed batch x sequence; the guide says always pass
  `dynamic=False` - dynamic shapes force padding and recompiles and defeat fusion, and leaving
  `dynamic=None` lets Dynamo silently flip a region to dynamic after a recompile.
- **Why not whole-model compile** (no TPU recipe uses it): without in-graph checkpointing all layers'
  activations are live (compile/runtime OOM); `checkpoint(preserve_rng_state=True)` RNG fork/restore
  does not trace cleanly on TorchTPU (the conformer recipe uses `preserve_rng_state=False`); token
  embedding backward can bind incorrectly when compiled (keep it eager); lazily created buffers such
  as RoPE cos/sin must be materialized before tracing; and it still leaves loss and optimizer as
  separate programs, so it does not remove the whole-step idle.
- **Shrinking the eager surface:** combine per-block compile with `optimizer_compile="separate_graph"`,
  `compile_grad_norm=True` and a compiled loss; each turns a chain of eager ops into one program, but
  dispatches between programs remain. Remove them entirely with
  [GraphTrainer](tpu-graph-trainer-memory-policies.md).
- Recipes that use the glue switches: Qwen3 and Muse Glimmer recipes set
  `materialize_forward_before_backward=True` and `compile_grad_norm=True` in several configs.

**Doc vs code:** the guide says to always compile with `dynamic=False` and that TorchTitan's
`apply_compile` "does exactly this". At this commit the core `apply_compile` used by the Llama3/Qwen3
TPU paths calls `transformer_block.compile(backend=backend, fullgraph=True)` **without** a `dynamic`
argument (only the Gemma4 example and the conformer TPU parallelizer pass `dynamic=False`). Static
shapes there rely on the training shapes staying fixed rather than on an explicit flag.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md),
  [llama3-model](../concepts/llama3-model.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md)
- Module catalogs: [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [train (tpu)](../catalog/torchtitan/experiments/tpu/train.md),
  [distributed/compile](../catalog/torchtitan/distributed/compile.md),
  [compiled_optimizers/separate_graph](../catalog/torchtitan/experiments/tpu/compiled_optimizers/separate_graph.md),
  [grad_norm](../catalog/torchtitan/experiments/tpu/grad_norm.md),
  [workarounds](../catalog/torchtitan/experiments/tpu/workarounds.md)
- Related doc-concepts: [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md),
  [tpu-defer-and-fuse-eager-mode](tpu-defer-and-fuse-eager-mode.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md),
  [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (sections 4 and 7; kept
in place).
