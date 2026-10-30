---
title: 'Module: csrc/ops/bernoulli/bernoulli_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/bernoulli/bernoulli_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenBernoulli_Float: AtenBernoulli_Float(a9bd7f7e9f511ac1).
  AtenBernoulliOut: AtenBernoulliOut(10160d7afafdb0ec).
  AtenBernoulli_Tensor: AtenBernoulli_Tensor(29ab3271b6ae7a63).
  BuildBernoulliShlo: '`$anonymous_namespace_csrc/ops/bernoulli/bernoulli_aten_kernels.cc`/BuildBernoulliShlo(314f0b7f28e8aa05).'
  DispatchBernoulliTensorRng: '`$anonymous_namespace_csrc/ops/bernoulli/bernoulli_aten_kernels.cc`/DispatchBernoulliTensorRng(effdb8400e98428b).'
  GetBernoulliFloatFunctional: '`$anonymous_namespace_csrc/ops/bernoulli/bernoulli_aten_kernels.cc`/GetBernoulliFloatFunctional(9caa4a07325230c6).'
  GetBernoulliTensorFunctional: '`$anonymous_namespace_csrc/ops/bernoulli/bernoulli_aten_kernels.cc`/GetBernoulliTensorFunctional(677eaa926852fd57).'
---
# Module: [`csrc/ops/bernoulli/bernoulli_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc)

## Functions
- <a id="AtenBernoulliOut"></a>`AtenBernoulliOut(const at::Tensor& self, std::optional<at::Generator> generator, at::Tensor& out)` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L131)
- <a id="AtenBernoulli_Float"></a>`AtenBernoulli_Float(at::Tensor& self, double p, std::optional<at::Generator> generator)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L157)
- <a id="AtenBernoulli_Tensor"></a>`AtenBernoulli_Tensor(at::Tensor& self, const at::Tensor& p, std::optional<at::Generator> generator)` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L189)
- <a id="BuildBernoulliShlo"></a>`BuildBernoulliShlo(mlir::MlirOp rng_input_state, mlir::MlirOp p_op, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L58) — Draws samples from a Bernoulli distribution with parameter `p`.
- `BuildBernoulliShlo(mlir::MlirOp rng_input_state, mlir::MlirOp p_op, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L58) — Draws samples from a Bernoulli distribution with parameter `p`.
- <a id="DispatchBernoulliTensorRng"></a>`DispatchBernoulliTensorRng(at::Tensor& dest, const at::Tensor& p_tensor, std::optional<at::Generator> generator, Dimensions dims, mlir::ElementType output_dtype, OpParamCacheKeys param_keys)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L111)
- <a id="GetBernoulliFloatFunctional"></a>`GetBernoulliFloatFunctional(Dimensions dims, mlir::ElementType output_dtype, double p)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L91)
- `GetBernoulliFloatFunctional(Dimensions dims, mlir::ElementType output_dtype, double p)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L91)
- <a id="GetBernoulliTensorFunctional"></a>`GetBernoulliTensorFunctional(Dimensions dims, mlir::ElementType output_dtype)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L103)
- `GetBernoulliTensorFunctional(Dimensions dims, mlir::ElementType output_dtype)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/ops/bernoulli/bernoulli_aten_kernels.cc#L103)

