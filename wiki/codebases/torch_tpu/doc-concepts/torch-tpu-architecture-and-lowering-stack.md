---
title: TorchTPU architecture - design principles and the dispatcher-to-PjRt lowering stack
type: doc-concept
provenance: doc
source: docs/markdown/intro_to_torchtpu.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# TorchTPU architecture - design principles and the dispatcher-to-PjRt lowering stack

## Definition
TorchTPU is a native PyTorch backend for Cloud TPUs (Google + Meta) with **no JAX runtime dependency**. The intro doc frames it around three principles: *native PyTorch citizenship* (standard view and in-place mutation semantics, one process per device, `torch.compile` via TorchDynamo), *out-of-the-box usability* (port by changing `device="cuda"` -> `"tpu"` and `backend="nccl"` -> `"tpu_dist"`), and *production-scale performance* (deferred-fusion eager, a Dynamo-to-XLA compiler, bounded dynamism, custom-kernel APIs). The README's feature list is the same surface in brief: ATen kernels for TPU, a compilation cache, DP/TP distributed training, `torch.compile` integration, and debug/benchmark utilities.

The doc's four-stage software lowering pipeline:
1. PyTorch's dispatcher intercepts tensor and collective ops on the `"tpu"` device.
2. Strided views and in-place writes are turned into functional ops by **view decomposition** and **view inversion**.
3. ATen and `c10d` ops are lowered to **StableHLO** (or **Mosaic** for Pallas kernels).
4. A C++ **PjRt client** compiles the module with XLA, caches the executable, and dispatches it asynchronously.

## In torch_tpu (grounded)
- Stage 1 (dispatch): ATen kernels enter through [`DispatchOp`](../catalog/csrc/eager/op_dispatcher.h.md#DispatchOp) / [`DispatchOpOut`](../catalog/csrc/eager/op_dispatcher.h.md#DispatchOpOut) in `csrc/eager`; collectives through [`ProcessGroupTpu`](../catalog/csrc/distributed/process_group_tpu.h.md#ProcessGroupTpu) (the `tpu_dist` c10d backend).
- Stage 2 (views): [`DecomposeIntoViewSequence`](../catalog/csrc/ops/view_decomposition/decomposition.cc.md#DecomposeIntoViewSequence) rewrites an arbitrary `(sizes, strides, offset)` view into a sequence of primitive view ops, and [`InverseViewSequenceShlo`](../catalog/csrc/ops/view_decomposition/inversion.cc.md#InverseViewSequenceShlo) / [`ComputeInverseViewOperation`](../catalog/csrc/ops/view_decomposition/inversion.cc.md#ComputeInverseViewOperation) emit the scatter-back needed when a view is written in place.
- Stage 3 (StableHLO): kernels build MLIR with the op-builder helpers; the compiled module is named by [`BuildModuleNameFromPyContext`](../catalog/csrc/ops/op_builder_utils.cc.md#BuildModuleNameFromPyContext) (`tt_jit_<file>_L<line>C<col>_<func>_<op>`), which is how these modules show up in dumps and profiles ([hlo-and-llo-compilation-dumps.md](hlo-and-llo-compilation-dumps.md)).
- Stage 4 (compile/cache/execute): [`Compile`](../catalog/csrc/common/compilation.cc.md#Compile) produces a [`LoadedExecutableWithMetadata`](../catalog/csrc/common/compilation.h.md#LoadedExecutableWithMetadata); [`CompilationCache`](../catalog/csrc/common/compilation_cache.h.md#CompilationCache) fronts it ([multi-tier-compilation-cache.md](multi-tier-compilation-cache.md)); the process-wide PjRt client is [`PjrtBackend`](../catalog/csrc/pjrt/pjrt_state.h.md#PjrtBackend) ([`PjrtBackend.GetInstance`](../catalog/csrc/pjrt/pjrt_state.cc.md#PjrtBackend.GetInstance), [`PjrtBackend.GetClient`](../catalog/csrc/pjrt/pjrt_state.cc.md#PjrtBackend.GetClient)).
- Graph mode: the `"tpu"` Dynamo backend is [`TpuBackend`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend), registered under that name in `src/torch_tpu/_internal/compile/__init__.py`.
- Hardware hooks the doc names: a `torch.tpu.Stream(pinned="sparse")` pins a stream to the SparseCore so collectives overlap TensorCore math - see [`TpuStream.pinned`](../catalog/src/torch_tpu/_internal/stream/streams.md#TpuStream.pinned); the internal flag [`kTorchTpuInternalSkinnyScOffloadEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalSkinnyScOffloadEnvVar) auto-pins traversals that contain exactly one collective.

## Why it matters / when it applies
- The hardware model the doc gives sets the perf priorities: MXUs multiply bf16 and accumulate fp32 (see [dtype-and-precision](../concepts/dtype-and-precision.md)); HBM is the shared bottleneck that fusion avoids; SparseCores handle gather/scatter/embeddings and collectives; ICI links chips inside a slice (3D torus / twisted torus) while DCN links slices.
- View decomposition is why TorchTPU can keep PyTorch's aliasing semantics on a functional compiler - and also why heavily strided in-place code turns into extra slice/scatter work in the HLO.
- Every op ultimately pays StableHLO build + cache lookup + (on miss) XLA compile; the eager modes, the cache tiers, and `torch.compile` are all strategies to amortize stage 4.
- Coverage claims in the doc (~450 core ATen ops forward+backward, ~5,000 Hugging Face models validated) describe the eager path; three eager modes and `torch.compile` are detailed in [eager-execution-modes.md](eager-execution-modes.md) and [torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md).

## Connections
- Code concepts: [eager-op-dispatch](../concepts/eager-op-dispatch.md), [view-decomposition](../concepts/view-decomposition.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md), [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [compilation-cache](../concepts/compilation-cache.md), [pjrt-client](../concepts/pjrt-client.md), [process-group-and-collectives](../concepts/process-group-and-collectives.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [device-streams-generators-and-rng](../concepts/device-streams-generators-and-rng.md), [hardware-introspection](../concepts/hardware-introspection.md), [dtype-and-precision](../concepts/dtype-and-precision.md)
- Module catalogs: [csrc/eager/op_dispatcher.h](../catalog/csrc/eager/op_dispatcher.h.md), [csrc/ops/view_decomposition/decomposition.cc](../catalog/csrc/ops/view_decomposition/decomposition.cc.md), [csrc/ops/view_decomposition/inversion.cc](../catalog/csrc/ops/view_decomposition/inversion.cc.md), [csrc/common/compilation.cc](../catalog/csrc/common/compilation.cc.md), [csrc/pjrt/pjrt_state.h](../catalog/csrc/pjrt/pjrt_state.h.md), [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md)
- Related doc-concepts: [tpu-device-backend-initialization.md](tpu-device-backend-initialization.md), [aten-and-c10d-ops-as-ir.md](aten-and-c10d-ops-as-ir.md), [xla-lowering-stablehlo-hlo-llo.md](xla-lowering-stablehlo-hlo-llo.md), [eager-execution-modes.md](eager-execution-modes.md), [multi-tier-compilation-cache.md](multi-tier-compilation-cache.md), [optimized-wheel-build.md](optimized-wheel-build.md)

## Source
Extracted from `docs/markdown/intro_to_torchtpu.md` (byte-identical copy: `docs/markdown/1_basics_1_intro_to_torchtpu.md`) and the Description/Features sections of `README.md` (kept in place).
