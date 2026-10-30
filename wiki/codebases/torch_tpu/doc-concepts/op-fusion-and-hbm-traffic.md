---
title: Op fusion and HBM traffic (Inductor/Triton on GPU vs XLA on TPU)
type: doc-concept
provenance: doc
source: docs/markdown/background_on_torch_compile.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Op fusion and HBM traffic (Inductor/Triton on GPU vs XLA on TPU)

## Definition
Without fusion, `relu(add(x, y))` reads inputs from HBM, computes, writes the sum back to HBM, then reads it again for the ReLU and writes again - serial, memory-bound round-trips. **Fusion** loads the data once, applies both ops in registers, and writes once. The `torch.compile` background doc shows the GPU version: Inductor emits a single Triton kernel `triton_poi_fused_add_relu_0` (visible with `TORCH_LOGS="output_code"`) that `tl.load`s both inputs, adds, takes `maximum` with 0, and `tl.store`s the result, with no intermediate HBM write. It also notes Inductor usually does *not* fuse matmuls, deferring to cuBLAS. The companion XLA doc shows the TPU equivalent: XLA fuses the same pair into one `kLoop` fusion (`add_maximum_fusion`) whose LLO is `vadd.f32` then `vmax.f32` on VMEM-resident data.

## In torch_tpu (grounded)
- TorchTPU does not implement fusion itself; it maximizes the graph XLA sees and lets XLA's HLO passes fuse. The three ways to give XLA a multi-op graph:
  - `torch.compile(backend="tpu")` - whole FX graphs through [`TpuBackend`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend) ([torch-compile-static-shapes-and-bounded-dynamism.md](torch-compile-static-shapes-and-bounded-dynamism.md));
  - DeferAndFuse eager - the deferred op queue flushed at [`Materialize`](../catalog/csrc/eager/materialize.h.md#Materialize) ([defer-and-fuse-materialization.md](defer-and-fuse-materialization.md));
  - multi-op kernels written as one StableHLO program, e.g. the fused optimizer kernels ([fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md)).
- In Strict eager each ATen op is its own executable, so every intermediate goes through HBM - the "no fusion" baseline the doc describes.
- Where XLA's fusion is not enough (e.g. matmul + epilogue, or quantize+pack at register level), the escalation is a Pallas/Mosaic custom kernel ([pallas-register-level-fusion.md](pallas-register-level-fusion.md)).

## Why it matters / when it applies
- Most of a transformer step outside matmul/attention is elementwise or reduction work that is HBM-bandwidth-bound; fusion is what turns those into near-free epilogues. On TPU this is the main reason fused eager and `torch.compile` beat Strict eager.
- Anything that cuts the graph - Dynamo graph breaks ([graph-breaks-on-tpu.md](graph-breaks-on-tpu.md)), eager materialization triggers, backend splits at collectives - is a fusion boundary and reintroduces the round-trip.
- To check whether fusion happened, look for a single `fusion(...)` in the after-optimization HLO dump ([hlo-and-llo-compilation-dumps.md](hlo-and-llo-compilation-dumps.md)) rather than inferring it from timing.

## Connections
- Code concepts: [compilation-pipeline](../concepts/compilation-pipeline.md), [deferred-execution-and-materialization](../concepts/deferred-execution-and-materialization.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [fused-optimizer-kernels](../concepts/fused-optimizer-kernels.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [mlir-optimization-passes](../concepts/mlir-optimization-passes.md)
- Module catalogs: [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md), [csrc/eager/materialize.h](../catalog/csrc/eager/materialize.h.md)
- Related doc-concepts: [defer-and-fuse-materialization.md](defer-and-fuse-materialization.md), [eager-execution-modes.md](eager-execution-modes.md), [xla-lowering-stablehlo-hlo-llo.md](xla-lowering-stablehlo-hlo-llo.md), [hlo-and-llo-compilation-dumps.md](hlo-and-llo-compilation-dumps.md), [graph-breaks-on-tpu.md](graph-breaks-on-tpu.md), [pallas-register-level-fusion.md](pallas-register-level-fusion.md)

## Source
Extracted from `docs/markdown/background_on_torch_compile.md`, with the TPU side from `docs/markdown/background_on_torch_compile_on_tpus_via_xla.md` (= `docs/markdown/4_debugging_and_performance_analysis_4_viewing_compilation_artifacts.md`) sections 3-4 (kept in place).
