---
title: GraphTrainer full train-step graph capture
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer full train-step graph capture

## Definition
GraphTrainer captures the **entire training step** - forward, loss, backward, and optionally `optimizer.step` - as one flat FX graph, then transforms and optimizes that graph before execution. The default `aot_fx_trace` mode traces with a `make_fx`-based tracer **without AOTAutograd partitioning**, so every backward op is explicit in the same graph as the forward. The Manifesto frames this as a bet that distributed training at scale needs a compiler: eager composability (FSDP2 + AC + compile + CUDA graphs) is fragile, and scheduling via hooks/`autograd.Function` is too coarse.

## In torchtitan (grounded)
- Tracer: [`minimal_fx_tracer`](../catalog/torchtitan/experiments/graph_trainer/make_fx_tracer.md#minimal_fx_tracer) produces a [`TracedResult`](../catalog/torchtitan/experiments/graph_trainer/make_fx_tracer.md#TracedResult) (graph module, flat-input layout, subclass layouts, optimizer-state input counts); [`run_traced`](../catalog/torchtitan/experiments/graph_trainer/make_fx_tracer.md#run_traced) executes it.
- Trainer: [`GraphTrainer`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#GraphTrainer) subclasses core `Trainer`; [`GraphTrainer._make_fx_forward_backward_step`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#GraphTrainer._make_fx_forward_backward_step) builds the traced step from [`make_fwd_bwd_step`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#make_fwd_bwd_step), and [`GraphRunner`](../catalog/torchtitan/experiments/graph_trainer/runner.md#GraphRunner) runs the compiled callable.
- Mode selection: [`GraphTrainerCompileConfig.mode`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.mode) (`aot_fx_trace` default; `jit` deprecated, routed through [`apply_compile`](../catalog/torchtitan/experiments/graph_trainer/compile.md#apply_compile)). Configs are lifted from a core config by [`to_graph_trainer_config`](../catalog/torchtitan/experiments/graph_trainer/configs.md#to_graph_trainer_config).
- Model entry points: `graph_trainer.llama3`, `graph_trainer.deepseek_v3`, `graph_trainer.qwen3` (plus `graph_trainer.muse_glimmer`), each with its own parallelize function, e.g. [`parallelize_deepseekv3`](../catalog/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize.md#parallelize_deepseekv3).

## Why it matters / when it applies
- **Every optimization becomes a graph pass** (AC, CUDA graphs, CPU offload, comm overlap, fusion) on one shared representation; passes compose instead of threading hooks through the stack. See [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md).
- **TPU relevance.** The Manifesto's "hardware heterogeneity" point - non-GPU accelerators such as TPUs assume a graph and do better with a full graph to optimize - is realized in this fork by [`TpuGraphTrainer`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer), a `GraphTrainer` subclass that registers a `tpu` pass pipeline ([`construct_tpu_transform_passes`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_backend_pass.md#construct_tpu_transform_passes)) and can fold the optimizer into the graph. See [tpu-graph-trainer](../concepts/tpu-graph-trainer.md).
- The graph is also the substrate for agentic optimization (see [graph-trainer-autoresearch-harness](graph-trainer-autoresearch-harness.md)) and is dumpable/diffable for debugging (tlparse integration).
- Requires the latest PyTorch nightly.

**Composability status (README table, `aot_fx_trace`):** supported - meta init, activation checkpointing, mixed precision, TP, CP, distributed checkpointing, CUDA graphs, EP. In progress - activation offloading, Float8/MXFP8, EP+AC, EP+PP, graph-based PP, micro-batch overlap, pre-compile.

**Doc vs code at this commit:** the README's collapsed "legacy modes" section names an AOT mode (`--compile.mode aot`) and a JIT mode. In code `GraphTrainerCompileConfig.mode` is `Literal["jit", "aot_fx_trace"]` - the old `aot` value no longer exists; only `jit` remains as the deprecated alternative. The table marks "Activation Offloading" as in progress even though an offload memory policy (`sac_and_offload`) is implemented (see [graph-trainer-memory-policy](graph-trainer-memory-policy.md)).

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [trainer-and-train-loop](../concepts/trainer-and-train-loop.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md)
- Module catalogs: [graph_trainer/make_fx_tracer](../catalog/torchtitan/experiments/graph_trainer/make_fx_tracer.md), [graph_trainer/trainer](../catalog/torchtitan/experiments/graph_trainer/trainer.md), [graph_trainer/configs](../catalog/torchtitan/experiments/graph_trainer/configs.md), [graph_trainer/runner](../catalog/torchtitan/experiments/graph_trainer/runner.md)
- Related doc-concepts: [simple-fsdp](simple-fsdp.md), [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [graph-trainer-memory-policy](graph-trainer-memory-policy.md), [graph-pp-pipeline-parallelism](graph-pp-pipeline-parallelism.md), [graph-trainer-ep-overlap](graph-trainer-ep-overlap.md), [graph-trainer-autoparallel](graph-trainer-autoparallel.md), [graph-trainer-precompile](graph-trainer-precompile.md), [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md) (TPU GraphTrainer)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` and `torchtitan/experiments/graph_trainer/MANIFESTO.md` (kept in place).
