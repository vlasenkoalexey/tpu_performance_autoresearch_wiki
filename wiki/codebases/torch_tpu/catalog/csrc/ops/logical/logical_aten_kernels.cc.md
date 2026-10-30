---
title: 'Module: csrc/ops/logical/logical_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/logical/logical_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLogicalAndOut: AtenLogicalAndOut(dcc870e438d8791).
  AtenLogicalNotOut: AtenLogicalNotOut(4655895dd4ef7692).
  AtenLogicalOrOut: AtenLogicalOrOut(dcc870e438d8791).
  AtenLogicalXorOut: AtenLogicalXorOut(dcc870e438d8791).
  LogicalBinaryOutImpl: '`$anonymous_namespace_csrc/ops/logical/logical_aten_kernels.cc`/LogicalBinaryOutImpl(45e142bd473b440b).'
  LogicalUnaryOutImpl: '`$anonymous_namespace_csrc/ops/logical/logical_aten_kernels.cc`/LogicalUnaryOutImpl(7a9ac0ae4395728b).'
---
# Module: [`csrc/ops/logical/logical_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc)

## Functions
- <a id="AtenLogicalAndOut"></a>`AtenLogicalAndOut(const at::Tensor& self, const at::Tensor& other, at::Tensor& out)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L65)
- <a id="AtenLogicalNotOut"></a>`AtenLogicalNotOut(const at::Tensor& self, at::Tensor& out)` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L92)
- <a id="AtenLogicalOrOut"></a>`AtenLogicalOrOut(const at::Tensor& self, const at::Tensor& other, at::Tensor& out)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L74)
- <a id="AtenLogicalXorOut"></a>`AtenLogicalXorOut(const at::Tensor& self, const at::Tensor& other, at::Tensor& out)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L83)
- <a id="LogicalBinaryOutImpl"></a>`LogicalBinaryOutImpl(const at::Tensor& self, const at::Tensor& other, at::Tensor& out, MlirBinaryOpBuilder core_op_builder)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L41) — This helper function for binary logical operations validates output dtype
- <a id="LogicalUnaryOutImpl"></a>`LogicalUnaryOutImpl(const at::Tensor& self, at::Tensor& out, MlirUnaryOpBuilder core_op_builder)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/logical/logical_aten_kernels.cc#L53) — This helper function for unary logical operations validates output dtype

