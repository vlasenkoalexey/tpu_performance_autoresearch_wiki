---
title: 'Module: csrc/ops/macros/kernel.cc'
type: catalog
provenance: extracted
module: csrc/ops/macros/kernel.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/internal/
symbols:
  CheckTensorsUsed: CheckTensorsUsed(794bbbca577513a2).
  AppendPromotedScalarPointers: AppendPromotedScalarPointers(80d4a4c6ee3e1fa0).
---
# Module: [`csrc/ops/macros/kernel.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.cc)

## Functions
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const std::vector<PromotedScalar>& arg)` — [`L26`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.cc#L26) — Case: std::vector<PromotedScalar>
- <a id="AppendPromotedScalarPointers"></a>`AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const std::vector<PromotedScalar>& arg)` — [`L26`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.cc#L26) — Case: std::vector<PromotedScalar>
- `CheckTensorsUsed(const PromotedTensorStates& promoted_scalars)` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.cc#L33) — Crashes if any of the given PromotedScalars was not used in the kernel.
- <a id="CheckTensorsUsed"></a>`CheckTensorsUsed(const PromotedTensorStates& promoted_scalars)` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.cc#L33) — Crashes if any of the given PromotedScalars was not used in the kernel. — documented in [aten-kernel-authoring](../../../../concepts/aten-kernel-authoring.md)

