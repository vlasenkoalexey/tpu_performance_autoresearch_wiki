---
title: TorchTPU user-guide map (docs index -> code concepts)
type: doc-concept
provenance: doc
source: docs/markdown/index.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TorchTPU user-guide map (docs index -> code concepts)

## Definition
`docs/markdown/index.md` is the table of contents for the TorchTPU user guide. It is organized as a learning ladder: **Basics** (intro, VM and GKE setup, running upstream PyTorch examples, distributed on GKE), **In depth** (how TorchTPU works, known limitations, memory model and views, execution modes), **Practical examples** (LLM inference and training, FSDP best practices, Pallas kernels and distributed Pallas, bounded dynamism), **Debugging and performance analysis** (numerical precision, XProf, error information, compilation artifacts), a **FLUX case study**, and a **Reference** shelf (supported features, `torch.tpu` API, XProf reference, environment variables). This page maps each section to the code that implements it, through the lens of TPU performance.

## In torch_tpu (grounded)
| Guide section | What it covers | Code concepts | Doc-concepts |
|---|---|---|---|
| Basics: get started (VM / GKE) | `"tpu"` device, `.to`/`.cpu`, GKE Job manifests | [hardware-introspection](../concepts/hardware-introspection.md), [host-device-copy](../concepts/host-device-copy.md) | [tpu-device-backend-initialization](tpu-device-backend-initialization.md), [gke-single-device-workload-topology](gke-single-device-workload-topology.md) |
| Basics: distributed on GKE | launchers, multi-host env | [distributed-launchers-and-spmd](../concepts/distributed-launchers-and-spmd.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md) | [gke-single-device-workload-topology](gke-single-device-workload-topology.md) |
| In depth: how TorchTPU works | ATen -> StableHLO -> XLA | [eager-op-dispatch](../concepts/eager-op-dispatch.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [compilation-cache](../concepts/compilation-cache.md) | [torch-tpu-architecture-and-lowering-stack](torch-tpu-architecture-and-lowering-stack.md), [multi-tier-compilation-cache](multi-tier-compilation-cache.md) |
| In depth: execution modes | strict / deferred / fused eager, compiled | [context-states-and-execution-modes](../concepts/context-states-and-execution-modes.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [compiled-mode](../concepts/compiled-mode.md) | [eager-execution-modes](eager-execution-modes.md), [defer-and-fuse-materialization](defer-and-fuse-materialization.md) |
| In depth: memory model | views on TPU | [view-decomposition](../concepts/view-decomposition.md) | - |
| Practical: LLM train / infer, porting | training loops, attention | [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md), [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md) | [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [sdpa-backend-selection-when-porting](sdpa-backend-selection-when-porting.md) |
| Practical: Pallas kernels | custom and distributed kernels | [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md), [mosaic-matmul](../concepts/mosaic-matmul.md) | [pallas-jax-op-bridge](pallas-jax-op-bridge.md), [pallas-register-level-fusion](pallas-register-level-fusion.md) |
| Practical: bounded dynamism | dynamic shapes | [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), [dynamic-shape-ops](../concepts/dynamic-shape-ops.md) | [torch-compile-static-shapes-and-bounded-dynamism](torch-compile-static-shapes-and-bounded-dynamism.md) |
| Debugging: numerical precision | matmul precision, excess precision | [dtype-and-precision](../concepts/dtype-and-precision.md) | [excess-precision](excess-precision.md), [matmul-precision-modes](matmul-precision-modes.md), [tpu-cpu-numerical-parity](tpu-cpu-numerical-parity.md) |
| Debugging: XProf | profiling | [profiler](../concepts/profiler.md) | [xprof-profiling-workflow](xprof-profiling-workflow.md), [trace-red-flags](trace-red-flags.md) |
| Debugging: errors, compilation artifacts | error anatomy, dumps | [error-handling](../concepts/error-handling.md), [op-names-and-python-context](../concepts/op-names-and-python-context.md), [mlir-optimization-passes](../concepts/mlir-optimization-passes.md) | [tpu-error-anatomy](tpu-error-anatomy.md) |
| Reference: torch.tpu API, env vars | public surface, knobs | [python-ops](../concepts/python-ops.md) | [public-api-paths-and-module-structure](public-api-paths-and-module-structure.md), [global-and-local-knobs](global-and-local-knobs.md), [api-lifecycle-stages](api-lifecycle-stages.md) |

The public surface the Reference section documents is generated from the declarative table in [`public_api`](../catalog/src/torch_tpu/_internal/public_api.md) and installed by [`install`](../catalog/src/torch_tpu/_internal/public_api.md#install).

## Why it matters / when it applies
- For an optimization pass, the perf-bearing chapters are **execution modes**, **memory model**, **bounded dynamism**, **numerical precision**, **XProf**, **compilation artifacts**, **FSDP best practices** and the **FLUX case study** (a worked multi-optimization example). The Basics chapters only set up the environment.
- The guide files carry a `torch_tpu_version: 0.1.1.dev...` front-matter stamp that predates v0.2.0. Where a doc and the code disagree (e.g. the GKE manifest's `TPU_LAUNCH_BLOCKING`, or the design guide's `ReadFlagOnce()`), trust the code at the pinned SHA.

## Connections
- Code concepts: listed per row above; entry points are [eager-op-dispatch](../concepts/eager-op-dispatch.md) and [compilation-pipeline](../concepts/compilation-pipeline.md).
- Module catalogs: [src/torch_tpu/_internal/public_api](../catalog/src/torch_tpu/_internal/public_api.md)
- Related doc-concepts: all pages in the table.

## Source
Extracted from `docs/markdown/index.md` (kept in place).
