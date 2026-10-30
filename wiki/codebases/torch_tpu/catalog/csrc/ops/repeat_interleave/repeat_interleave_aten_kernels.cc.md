---
title: 'Module: csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRepeatInterleave: AtenRepeatInterleave(43747c020ae61c12).
  AtenRepeatInterleaveSelfInt: AtenRepeatInterleaveSelfInt(154d8d9bd3bd39c).
  AtenRepeatInterleaveTensorOut: AtenRepeatInterleaveTensorOut(6d7f28e5dfb4bc19).
  AtenRepeatInterleaveTensor: AtenRepeatInterleaveTensor(23c51faffc967ed4).
  RepeatInterleaveBackwardKernel: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatInterleaveBackwardKernel(189d755593c50f01).'
  ValidateAndResolveRepeatInterleaveTensor: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/ValidateAndResolveRepeatInterleaveTensor(cdf0382d2d9ef7b5).'
  ValidateRepeatInterleaveSelfInt: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/ValidateRepeatInterleaveSelfInt(1540cfe31a39e932).'
  BuildRepeatInterleaveIndicesShlo: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/BuildRepeatInterleaveIndicesShlo(32e5625f5d56765e).'
  BuildRepeatInterleaveBackwardShlo: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/BuildRepeatInterleaveBackwardShlo(fea12b83d4a7a53c).'
  ComputeRepeatsSumAndMinOnHost: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/ComputeRepeatsSumAndMinOnHost(bd4fc38cf449acd5).'
  BuildRepeatInterleaveShlo: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/BuildRepeatInterleaveShlo(7581ace08ea737f).'
  BuildRepeatInterleaveTensorShlo: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/BuildRepeatInterleaveTensorShlo(32e5625f5d56765e).'
  AtenRepeatInterleaveSelfIntAutograd: AtenRepeatInterleaveSelfIntAutograd(154d8d9bd3bd39c).
  AtenRepeatInterleaveAutograd: AtenRepeatInterleaveAutograd(43747c020ae61c12).
  BuildUniformRepeatInterleaveShlo: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/BuildUniformRepeatInterleaveShlo(cb3859bc2e95d697).'
  TryExtractScalarRepeatCount: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/TryExtractScalarRepeatCount(83a99f295186f8a0).'
  RepeatsStats.min: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatsStats#min.'
  AtenRepeatInterleaveSelfIntAutogradNode: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/AtenRepeatInterleaveSelfIntAutogradNode#'
  AtenRepeatInterleaveSelfIntAutogradNode.backward: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/AtenRepeatInterleaveSelfIntAutogradNode#backward(305625f81d7e100).'
  AtenRepeatInterleaveSelfIntAutogradNode.forward: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/AtenRepeatInterleaveSelfIntAutogradNode#forward(402b8d85604fc314).'
  IsFakeOrFunctorchTensor: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/IsFakeOrFunctorchTensor(b580d0b7e29ca914).'
  RepeatsStats.sum: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatsStats#sum.'
  RepeatsStats: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatsStats#'
  DecomposeRepeatInterleaveSelfInt: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/DecomposeRepeatInterleaveSelfInt(154d8d9bd3bd39c).'
  RepeatInterleaveSelfIntValidation.resolved_output_size: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatInterleaveSelfIntValidation#resolved_output_size.'
  RepeatInterleaveSelfIntValidation: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatInterleaveSelfIntValidation#'
  RepeatInterleaveSelfIntValidation.resolved_dim: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatInterleaveSelfIntValidation#resolved_dim.'
  RepeatInterleaveSelfIntValidation.repeats_val: '`$anonymous_namespace_csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`/RepeatInterleaveSelfIntValidation#repeats_val.'
---
# Module: [`csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc)

## Classes
### <a id="AtenRepeatInterleaveSelfIntAutogradNode"></a>`AtenRepeatInterleaveSelfIntAutogradNode`  ·  implements/extends Function
- def: [`csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc:971`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L971)
- doc: Custom autograd node (`torch::autograd::Function`) for uniform
- signature: `struct AtenRepeatInterleaveSelfIntAutogradNode : public torch::autograd::Function< AtenRepeatInterleaveSelfIntAutogradNode>`
- members:
  - <a id="AtenRepeatInterleaveSelfIntAutogradNode.backward"></a>`backward(torch::autograd::AutogradContext* ctx, std::vector<at::Tensor> grad_outputs)` — [`L991`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L991)
  - `backward(torch::autograd::AutogradContext* ctx, std::vector<at::Tensor> grad_outputs)` — [`L991`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L991)
  - <a id="AtenRepeatInterleaveSelfIntAutogradNode.forward"></a>`forward(torch::autograd::AutogradContext* ctx, const at::Tensor& self, c10::SymInt repeats, std::optional<int64_t> dim, std::optional<c10::SymInt> output_size)` — [`L974`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L974)
- uses (calls/refs, reference-scoped): [`AtenRepeatInterleaveSelfInt`](repeat_interleave_aten_kernels.cc.md#AtenRepeatInterleaveSelfInt), [`RepeatInterleaveBackwardKernel`](repeat_interleave_aten_kernels.cc.md#RepeatInterleaveBackwardKernel)
- used by: [`AtenRepeatInterleaveSelfIntAutograd`](repeat_interleave_aten_kernels.cc.md#AtenRepeatInterleaveSelfIntAutograd)

### <a id="RepeatInterleaveSelfIntValidation"></a>`RepeatInterleaveSelfIntValidation`
- def: [`csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc:366`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L366)
- doc: Holds validated and canonicalized parameters for uniform `repeat_interleave`.
- signature: `struct RepeatInterleaveSelfIntValidation`
- members:
  - <a id="RepeatInterleaveSelfIntValidation.repeats_val"></a>`repeats_val` — [`L368`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L368) — Non-negative integer repeat count.
  - <a id="RepeatInterleaveSelfIntValidation.resolved_dim"></a>`resolved_dim` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L371) — Canonical non-negative dimension index in `[0, self.dim() - 1]`, or
  - <a id="RepeatInterleaveSelfIntValidation.resolved_output_size"></a>`resolved_output_size` — [`L373`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L373) — Total output extent along `resolved_dim` (`dim_size * repeats_val`).

### <a id="RepeatsStats"></a>`RepeatsStats`
- def: [`csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc:480`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L480)
- signature: `struct RepeatsStats`
- members:
  - <a id="RepeatsStats.min"></a>`min` — [`L482`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L482)
  - <a id="RepeatsStats.sum"></a>`sum` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L481)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenRepeatInterleave`](repeat_interleave_aten_kernels.cc.md#AtenRepeatInterleave), [`ValidateAndResolveRepeatInterleaveTensor`](repeat_interleave_aten_kernels.cc.md#ValidateAndResolveRepeatInterleaveTensor), [`ComputeRepeatsSumAndMinOnHost`](repeat_interleave_aten_kernels.cc.md#ComputeRepeatsSumAndMinOnHost), [`TryExtractScalarRepeatCount`](repeat_interleave_aten_kernels.cc.md#TryExtractScalarRepeatCount)

## Functions
- <a id="AtenRepeatInterleave"></a>`AtenRepeatInterleave(const at::Tensor& self, const at::Tensor& repeats, std::optional<int64_t> dim, std::optional<int64_t> output_size)` — [`L599`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L599) — Eager `PrivateUse1` kernel for `aten::repeat_interleave.self_Tensor`.
- <a id="AtenRepeatInterleaveAutograd"></a>`AtenRepeatInterleaveAutograd(const at::Tensor& self, const at::Tensor& repeats, std::optional<int64_t> dim, std::optional<int64_t> output_size)` — [`L1098`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L1098) — Entry point for `AutogradPrivateUse1` registration of
- <a id="AtenRepeatInterleaveSelfInt"></a>`AtenRepeatInterleaveSelfInt(const at::Tensor& self, c10::SymInt repeats, std::optional<int64_t> dim, std::optional<c10::SymInt> output_size)` — [`L534`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L534) — Eager `PrivateUse1` kernel for `aten::repeat_interleave.self_int`.
- <a id="AtenRepeatInterleaveSelfIntAutograd"></a>`AtenRepeatInterleaveSelfIntAutograd(const at::Tensor& self, c10::SymInt repeats, std::optional<int64_t> dim, std::optional<c10::SymInt> output_size)` — [`L1030`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L1030) — Entry point for `AutogradPrivateUse1` registration of
- <a id="AtenRepeatInterleaveTensor"></a>`AtenRepeatInterleaveTensor(const at::Tensor& repeats, const std::optional<c10::SymInt> output_size)` — [`L761`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L761) — Eager `PrivateUse1` kernel for `aten::repeat_interleave.Tensor`.
- <a id="AtenRepeatInterleaveTensorOut"></a>`AtenRepeatInterleaveTensorOut(const at::Tensor& repeats, const std::optional<c10::SymInt> output_size, at::Tensor& out)` — [`L797`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L797) — Eager `PrivateUse1` kernel for `aten::repeat_interleave.Tensor_out`.
- <a id="BuildRepeatInterleaveBackwardShlo"></a>`BuildRepeatInterleaveBackwardShlo(mlir::MlirOp grad_op, absl::Span<const int64_t> self_sizes, std::optional<int64_t> resolved_dim, int64_t repeats)` — [`L877`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L877) — Lowers the backward pass (Vector-Jacobian Product / VJP) of uniform
- <a id="BuildRepeatInterleaveIndicesShlo"></a>`BuildRepeatInterleaveIndicesShlo(mlir::MlirOp repeats, const int64_t output_size)` — [`L168`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L168) — Lowers variable-length `repeat_interleave` (`repeats` is a 1D tensor of
- <a id="BuildRepeatInterleaveShlo"></a>`BuildRepeatInterleaveShlo(mlir::MlirOp self, mlir::MlirOp repeats, const std::optional<int64_t> dim, const int64_t output_size)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L231)
- <a id="BuildRepeatInterleaveTensorShlo"></a>`BuildRepeatInterleaveTensorShlo(mlir::MlirOp input, const int64_t total)` — [`L740`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L740)
- <a id="BuildUniformRepeatInterleaveShlo"></a>`BuildUniformRepeatInterleaveShlo(mlir::MlirOp self, std::optional<int64_t> dim, int64_t repeats)` — [`L289`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L289) — Lowers `repeat_interleave` with uniform integer repeats (`repeats` is a
- <a id="ComputeRepeatsSumAndMinOnHost"></a>`ComputeRepeatsSumAndMinOnHost(const at::Tensor& repeats)` — [`L489`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L489) — Synchronizes `repeats` to host memory (if on TPU) via direct device-to-host
- <a id="DecomposeRepeatInterleaveSelfInt"></a>`DecomposeRepeatInterleaveSelfInt(const at::Tensor& self, c10::SymInt repeats, std::optional<int64_t> dim, std::optional<c10::SymInt> output_size)` — [`L433`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L433) — Decomposes uniform `repeat_interleave` into standard ATen view operations
- <a id="IsFakeOrFunctorchTensor"></a>`IsFakeOrFunctorchTensor(const at::Tensor& tensor)` — [`L470`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L470) — Returns true if `tensor` is a `FakeTensor`, `Meta` tensor, or wrapped inside
- <a id="RepeatInterleaveBackwardKernel"></a>`RepeatInterleaveBackwardKernel(const at::Tensor& grad_output, at::IntArrayRef self_sizes_ref, int64_t repeats_val, std::optional<int64_t> resolved_dim)` — [`L930`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L930) — Dispatches `BuildRepeatInterleaveBackwardShlo` as a native TPU eager kernel.
- <a id="TryExtractScalarRepeatCount"></a>`TryExtractScalarRepeatCount(const at::Tensor& self, const at::Tensor& repeats, std::optional<int64_t> dim, std::optional<int64_t> output_size, int64_t& repeats_val)` — [`L1048`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L1048) — Attempts to extract a scalar repeat count when `repeats` is a 1-element
- <a id="ValidateAndResolveRepeatInterleaveTensor"></a>`ValidateAndResolveRepeatInterleaveTensor(const at::Tensor& repeats, const std::optional<c10::SymInt>& output_size, const int64_t output_size_val)` — [`L710`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L710) — Validates `repeats` (1D, `int64` or `int32`, non-negative elements) and
- <a id="ValidateRepeatInterleaveSelfInt"></a>`ValidateRepeatInterleaveSelfInt(const at::Tensor& self, c10::SymInt repeats, std::optional<int64_t> dim, std::optional<c10::SymInt> output_size)` — [`L385`](../../../../../../../raw/code/torch_tpu/csrc/ops/repeat_interleave/repeat_interleave_aten_kernels.cc#L385) — Validates and canonicalizes arguments for `repeat_interleave.self_int`

