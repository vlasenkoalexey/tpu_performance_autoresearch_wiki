---
title: GraphTrainer pre-compile (compile-on-one-rank)
type: doc-concept
provenance: doc
source: torchtitan/experiments/graph_trainer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# GraphTrainer pre-compile (compile-on-one-rank)

## Definition
Pre-compile compiles the AOT train-step graph **once, on a single process/GPU**, serializes it, and loads the same artifact on every rank at training time, skipping compilation entirely. It relies on compile-on-one-rank (CooR) to make the artifact rank-agnostic: rank-specific values are computed at run time instead of being baked into the graph.

## In torchtitan (grounded)
- Switch: [`GraphTrainerCompileConfig.precompile_artifact_dir`](../catalog/torchtitan/experiments/graph_trainer/configs.md#GraphTrainerCompileConfig.precompile_artifact_dir) - setting it enables precompile in both steps.
- Step 1 (save): [`main`](../catalog/torchtitan/experiments/graph_trainer/precompile_main.md#main) in `precompile_main.py`, which traces and then calls [`precompile_fx_trace_save`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#precompile_fx_trace_save); fake SPMD meshes come from [`get_spmd_precompile_meshes`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#get_spmd_precompile_meshes).
- Artifact: [`PrecompiledFxTraceArtifact`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#PrecompiledFxTraceArtifact) (serialized graph module + flat-input/output layout), built with [`PrecompiledFxTraceArtifact.from_traced_result`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#PrecompiledFxTraceArtifact.from_traced_result).
- Staleness: [`compute_config_fingerprint`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#compute_config_fingerprint) / [`ConfigFingerprint`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#ConfigFingerprint) - a mismatch raises at load time.
- Step 2 (load): [`GraphTrainer._load_precompiled_fx_trace`](../catalog/torchtitan/experiments/graph_trainer/trainer.md#GraphTrainer._load_precompiled_fx_trace) via [`precompile_fx_trace_load`](../catalog/torchtitan/experiments/graph_trainer/precompile.md#precompile_fx_trace_load). When an artifact is present, [`construct_default_graph_passes`](../catalog/torchtitan/experiments/graph_trainer/passes.md#construct_default_graph_passes) returns only the CUDA-graph pass, because the compile-time passes were baked in during precompile.
- Launch: `run_train_precompile.sh` passes `--virtual-local-rank` to torchrun so every worker sees `LOCAL_RANK=0` / `cuda:0`, matching the single-process artifact.

## Why it matters / when it applies
- Removes per-rank compile time from job start-up (and from every restart) at scale; for multi-node runs the artifact directory must be on a shared filesystem.
- Works with any pass that produces serializable output, including full and regional Inductor.
- **Artifacts are ephemeral:** tied to the exact PyTorch version, CUDA version, model architecture and parallelism configuration; regenerate after any change.
- Limitations: GraphPP does not load precompile artifacts yet; the composability table still marks pre-compile as in progress; `enable_inplace_graph_gradient_accumulation` lists precompile as a TODO.
- **TPU relevance.** The precompile artifact is GPU-specific (Triton kernels, `cuda:0` targeting), and the TPU graph lane does not use it. Compile cold-start on TPU is a separate concern of the TPU backend (no precompile/cache code lives in `experiments/tpu` at this commit); the transferable idea is fingerprinting the config and rejecting stale artifacts. See [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md).

## Connections
- Code concepts: [graph-trainer](../concepts/graph-trainer.md), [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [checkpointing](../concepts/checkpointing.md)
- Module catalogs: [graph_trainer/precompile](../catalog/torchtitan/experiments/graph_trainer/precompile.md), [graph_trainer/precompile_main](../catalog/torchtitan/experiments/graph_trainer/precompile_main.md), [graph_trainer/trainer](../catalog/torchtitan/experiments/graph_trainer/trainer.md)
- Related doc-concepts: [graph-trainer-pass-pipeline](graph-trainer-pass-pipeline.md), [graph-trainer-full-step-graph-capture](graph-trainer-full-step-graph-capture.md), [graph-pp-pipeline-parallelism](graph-pp-pipeline-parallelism.md)

## Source
Extracted from `torchtitan/experiments/graph_trainer/README.md` (kept in place).
