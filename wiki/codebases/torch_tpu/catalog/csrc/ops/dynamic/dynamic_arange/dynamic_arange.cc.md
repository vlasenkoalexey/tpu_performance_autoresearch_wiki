---
title: 'Module: csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc'
type: catalog
provenance: extracted
module: csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DynamicArange: DynamicArange(503383d081c62f23).
  BuildDynamicArange: BuildDynamicArange(9c3dfc64620aa438).
---
# Module: [`csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc)

## Functions
- <a id="BuildDynamicArange"></a>`BuildDynamicArange(mlir::MlirBuilder& builder, mlir::MlirOp start_op, mlir::MlirOp end_op, mlir::MlirOp step_op, mlir::ElementType element_type, int64_t max_length)` — [`L46`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc#L46) — documented in [dynamic-shape-ops](../../../../../concepts/dynamic-shape-ops.md)
- <a id="DynamicArange"></a>`DynamicArange(const at::Tensor& start, const at::Tensor& end, const at::Tensor& step, int64_t max_length, at::ScalarType dtype)` — [`L120`](../../../../../../../../raw/code/torch_tpu/csrc/ops/dynamic/dynamic_arange/dynamic_arange.cc#L120) — This op is a torch_tpu custom op for use in torch.compile() mode to handle — documented in [dynamic-shape-ops](../../../../../concepts/dynamic-shape-ops.md)

