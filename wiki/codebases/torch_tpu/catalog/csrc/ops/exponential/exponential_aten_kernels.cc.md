---
title: 'Module: csrc/ops/exponential/exponential_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/exponential/exponential_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenExponential_: AtenExponential_(a9bd7f7e9f511ac1).
  BuildExponentialShlo: '`$anonymous_namespace_csrc/ops/exponential/exponential_aten_kernels.cc`/BuildExponentialShlo(5c8af64d92073aa).'
  GetExponentialFunctional: '`$anonymous_namespace_csrc/ops/exponential/exponential_aten_kernels.cc`/GetExponentialFunctional(8d3d0df85d36236c).'
---
# Module: [`csrc/ops/exponential/exponential_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc)

## Functions
- <a id="AtenExponential_"></a>`AtenExponential_(at::Tensor& self, double lambd, std::optional<at::Generator> generator)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc#L91)
- <a id="BuildExponentialShlo"></a>`BuildExponentialShlo(mlir::MlirOp rng_input_state, mlir::MlirOp lambd_op, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc#L49)
- `BuildExponentialShlo(mlir::MlirOp rng_input_state, mlir::MlirOp lambd_op, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc#L49)
- <a id="GetExponentialFunctional"></a>`GetExponentialFunctional(Dimensions dims, mlir::ElementType output_dtype)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc#L80)
- `GetExponentialFunctional(Dimensions dims, mlir::ElementType output_dtype)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/exponential/exponential_aten_kernels.cc#L80)

