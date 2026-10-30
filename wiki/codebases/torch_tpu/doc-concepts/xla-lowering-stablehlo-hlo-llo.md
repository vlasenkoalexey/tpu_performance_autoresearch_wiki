---
title: The XLA lowering path on TPU - ATen -> StableHLO -> HLO -> LLO
type: doc-concept
provenance: doc
source: docs/markdown/background_on_torch_compile_on_tpus_via_xla.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# The XLA lowering path on TPU - ATen -> StableHLO -> HLO -> LLO

## Definition
TorchTPU compiles PyTorch with **XLA**, not Inductor. The doc's seven-step path from Python to TPU machine code:
1. user code changes minimally (device `"tpu"`);
2. PyTorch's dispatcher lowers Python to ATen and c10d ops (unchanged from GPU);
3. **TorchTPU** lowers ATen/c10d to **StableHLO**, a device-agnostic MLIR dialect;
4. XLA lowers StableHLO to **HLO**;
5. XLA optimizes HLO over many passes (this is where fusion happens);
6. XLA lowers HLO to device-specific **LLO** (low-level ops);
7. XLA optimizes LLO for the specific TPU generation.

Its conclusion: "the heart of creating highly optimized custom TPU kernels is gainful control of this final outputted LLO", whether the kernel is written as StableHLO, JAX-level ops, or Pallas.

## In torch_tpu (grounded)
- Only step 3 is TorchTPU code; steps 4-7 run inside the XLA/libtpu compiler invoked through PjRt. TorchTPU's boundary is the StableHLO module it hands to [`Compile`](../catalog/csrc/common/compilation.cc.md#Compile), created in an MLIR context from [`MakeMlirContext`](../catalog/csrc/common/compilation.cc.md#MakeMlirContext) and returned as a [`LoadedExecutableWithMetadata`](../catalog/csrc/common/compilation.h.md#LoadedExecutableWithMetadata).
- Step 3 is per-op in eager (each ATen kernel builds StableHLO via the op-builder layer, e.g. [`UnaryOp`](../catalog/csrc/ops/unary_aten_kernels.cc.md#UnaryOp), [`BinaryOp`](../catalog/csrc/ops/binary_aten_kernels.h.md#BinaryOp)) and per-FX-graph under `torch.compile` ([`TpuBackend`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend)); in both cases the same ATen kernels emit the StableHLO.
- Before XLA sees it, TorchTPU runs its own MLIR passes on the StableHLO; two env-var knobs that matter for perf are [`kTorchTpuInternalEnableMlirCseEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalEnableMlirCseEnvVar) (CSE, off by default because it regressed vLLM prefill) and [`kTorchTpuInternalDumpMlirPassesToEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalDumpMlirPassesToEnvVar) (dump IR per pass).
- XLA option overrides reach steps 4-7 via `XLA_FLAGS`, `LIBTPU_INIT_ARGS` ([`kLibtpuInitArgsEnvVar`](../catalog/csrc/common/env_vars.h.md#kLibtpuInitArgsEnvVar)) and the internal [`kTorchTpuInternalXlaOptionsEnvVar`](../catalog/csrc/common/env_vars.h.md#kTorchTpuInternalXlaOptionsEnvVar) (`key=value` pairs applied to `xla::CompileOptions`, taking precedence over `XLA_FLAGS`). Programmatic overrides go on a per-thread compiler-option stack via [`PushCompilerOptionOverrides`](../catalog/csrc/common/compilation.cc.md#PushCompilerOptionOverrides).
- Pallas kernels bypass steps 4-5 for their body: they are lowered to **Mosaic** and appear in HLO as a custom call ([pallas-custom-kernels](../concepts/pallas-custom-kernels.md)).

## Why it matters / when it applies
- Each layer has its own dump and its own question: StableHLO (did TorchTPU emit what I expect?), HLO before/after optimization (did XLA fuse it?), LLO (is the VPU/MXU actually busy, are DMAs overlapped?). How to get them: [hlo-and-llo-compilation-dumps.md](hlo-and-llo-compilation-dumps.md).
- Because fusion happens in step 5, eager DeferAndFuse and `torch.compile` both rely on handing XLA the largest possible graph ([op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md)).
- When XLA's output LLO is not good enough, the escalation is a custom kernel (Pallas / Mosaic) that controls the LLO directly.

## Connections
- Code concepts: [compilation-pipeline](../concepts/compilation-pipeline.md), [stablehlo-op-builder](../concepts/stablehlo-op-builder.md), [mlir-optimization-passes](../concepts/mlir-optimization-passes.md), [aten-kernel-authoring](../concepts/aten-kernel-authoring.md), [torch-compile-backend](../concepts/torch-compile-backend.md), [pjrt-client](../concepts/pjrt-client.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [kiln-kernel-dsl](../concepts/kiln-kernel-dsl.md), [mosaic-matmul](../concepts/mosaic-matmul.md)
- Module catalogs: [csrc/common/compilation.cc](../catalog/csrc/common/compilation.cc.md), [csrc/common/compilation.h](../catalog/csrc/common/compilation.h.md), [csrc/common/env_vars.h](../catalog/csrc/common/env_vars.h.md), [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md)
- Related doc-concepts: [hlo-and-llo-compilation-dumps.md](hlo-and-llo-compilation-dumps.md), [op-fusion-and-hbm-traffic.md](op-fusion-and-hbm-traffic.md), [aten-and-c10d-ops-as-ir.md](aten-and-c10d-ops-as-ir.md), [torch-tpu-architecture-and-lowering-stack.md](torch-tpu-architecture-and-lowering-stack.md), [pallas-register-level-fusion.md](pallas-register-level-fusion.md), [pytorch-extension-ladder.md](pytorch-extension-ladder.md)

## Source
Extracted from `docs/markdown/background_on_torch_compile_on_tpus_via_xla.md` (byte-identical copy: `docs/markdown/4_debugging_and_performance_analysis_4_viewing_compilation_artifacts.md`), intro and conclusion (kept in place).
