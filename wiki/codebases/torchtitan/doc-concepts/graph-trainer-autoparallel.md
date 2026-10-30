---
title: GraphTrainer AutoParallel sharding
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer AutoParallel sharding

## Definition
AutoParallel is an experimental option in which an ILP-solver-based SPMD planner chooses the sharding placements for a supported model, instead of the hand-written TP/FSDP/EP plan. AutoParallel is **only responsible for producing the placed model**; GraphTrainer then captures and compiles that placed model through the normal `aot_fx_trace` flow, so every memory-policy, bucketing, overlap and Inductor option still applies.

## In torchtitan (grounded)
- Switch: [`GraphTrainerCompileConfig.enable_autoparallel`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.enable_autoparallel); [`validate_autoparallel_config`](../catalog/torchtitan/experiments/graph_trainer/configs.md#validate_autoparallel_config) rejects any mode other than `aot_fx_trace`.
- Wrapper: [`AutoParallelGraph`](../catalog/torchtitan/experiments/graph_trainer/autoparallel_api.md#AutoParallelGraph) (with [`AutoParallelGraph.apply_placement_for_fx_module`](../catalog/torchtitan/experiments/graph_trainer/autoparallel_api.md#AutoParallelGraph.apply_placement_for_fx_module)) and [`AutoParallelModelOutput`](../catalog/torchtitan/experiments/graph_trainer/autoparallel_api.md#AutoParallelModelOutput).
- Per-model entry points: [`parallelize_autoparallel_llama`](../catalog/torchtitan/experiments/graph_trainer/llama3/parallelize_autoparallel.md#parallelize_autoparallel_llama) and [`parallelize_autoparallel_deepseekv3`](../catalog/torchtitan/experiments/graph_trainer/deepseek_v3/parallelize_autoparallel.md#parallelize_autoparallel_deepseekv3).

## Why it matters / when it applies
- Supported today on the Llama 3 and DeepSeek-V3 debug models (README examples: Llama3 FSDP=2 x TP=2; DeepSeek-V3 FSDP=4 x EP=2).
- **Numerics:** AutoParallel may pick different shardings, collective schedules and operator lowerings than the manual plan, so its numerics tests require tight agreement with the eager baseline rather than bitwise-identical losses. Treat an AutoParallel speedup as needing a loss-parity check.
- **TPU relevance.** This is the PyTorch-side analogue of letting XLA/GSPMD propagate shardings from a few annotations. It is a useful reference point when deciding how much of the TPU lane's parallel plan to hand-write versus leave to the compiler (see [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) and [tpu-graph-trainer](../concepts/tpu-graph-trainer.md)).

**Doc vs code at this commit:** `torchtitan/experiments/__init__.py` still registers `autoparallel.llama3` / `autoparallel.local_map_deepseek_v3` module names although no standalone `experiments/autoparallel/` exists; AutoParallel is reached only through graph_trainer's `--compile.enable_autoparallel`.

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [llama3-model](../concepts/llama3-model.md), [deepseek-v3-model](../concepts/deepseek-v3-model.md)
- Module catalogs: [graph_trainer/autoparallel_api](../catalog/torchtitan/experiments/graph_trainer/autoparallel_api.md), [graph_trainer/configs](../catalog/torchtitan/experiments/graph_trainer/configs.md)
- Related doc-concepts: [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [experiments-contribution-contract](experiments-contribution-contract.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` (kept in place).
