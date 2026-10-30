---
title: 'Module: csrc/ops/reductions/reduction_utils.cc'
type: catalog
provenance: extracted
module: csrc/ops/reductions/reduction_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ValidateFloatOrComplex: ValidateFloatOrComplex(90723f725b74ed91).
  CanonicalizeDims: CanonicalizeDims(be3aed9dc487c92c).
  GetReductionFactor: GetReductionFactor(b36433b3062b1f56).
  ApplySumReduction: ApplySumReduction(2efca8662e33e5d5).
  GetSizesAfterReduction: GetSizesAfterReduction(c47a1cd37488d98c).
  ApplySumReductionOut: ApplySumReductionOut(928500735b116d16).
  MakeSumCacheKeys: '`$anonymous_namespace_csrc/ops/reductions/reduction_utils.cc`/MakeSumCacheKeys(29e3bff57e48777b).'
  OutputSizesArrayDiscardDim: '`$anonymous_namespace_csrc/ops/reductions/reduction_utils.cc`/OutputSizesArrayDiscardDim(a2b69fe0ae9d8693).'
  GetSumFunctional: '`$anonymous_namespace_csrc/ops/reductions/reduction_utils.cc`/GetSumFunctional(399bfcad39b508ca).'
  OutputSizesArrayKeepDim: '`$anonymous_namespace_csrc/ops/reductions/reduction_utils.cc`/OutputSizesArrayKeepDim(a2b69fe0ae9d8693).'
---
# Module: [`csrc/ops/reductions/reduction_utils.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc)

## Functions
- <a id="ApplySumReduction"></a>`ApplySumReduction(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, ReductionMode reduction_mode, c10::ScalarType out_dtype)` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L191) — Reduces the provided tensor by applying sum. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="ApplySumReductionOut"></a>`ApplySumReductionOut(const at::Tensor& self, at::Tensor& out, c10::OptionalArrayRef<int64_t> dim, ReductionMode reduction_mode, c10::ScalarType out_dtype, OpParamCacheKeys param_keys)` — [`L214`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L214) — Like ApplySumReduction but results are written to the provided `out` tensor. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="CanonicalizeDims"></a>`CanonicalizeDims(const at::Tensor& tensor, c10::OptionalArrayRef<int64_t> dim)` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L119) — Converts provided dimensions to canonical dimensions. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="GetReductionFactor"></a>`GetReductionFactor(const at::Tensor& input_tensor, c10::OptionalArrayRef<int64_t> dim)` — [`L172`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L172) — Returns the input:output ratio for the provided reduction. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="GetSizesAfterReduction"></a>`GetSizesAfterReduction(at::IntArrayRef self_size, ReductionMode reduction_mode, at::IntArrayRef canonicalized_dims)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L101) — Returns the size array after a reduction is applied. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="GetSumFunctional"></a>`GetSumFunctional(Dimensions dim, ReductionMode reduction_mode, mlir::ElementType mlir_type)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L57) — documented in [reductions](../../../../concepts/reductions.md)
- <a id="MakeSumCacheKeys"></a>`MakeSumCacheKeys(absl::Span<const int64_t> dims, ReductionMode reduction_mode)` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L93) — documented in [reductions](../../../../concepts/reductions.md)
- <a id="OutputSizesArrayDiscardDim"></a>`OutputSizesArrayDiscardDim(at::IntArrayRef self_size, absl::Span<const int64_t> canonicalized_dims)` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L79) — All reduced dimensions are removed. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="OutputSizesArrayKeepDim"></a>`OutputSizesArrayKeepDim(at::IntArrayRef self_size, absl::Span<const int64_t> canonicalized_dims)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L69) — All reduced dimensions are set to size 1. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="ValidateFloatOrComplex"></a>`ValidateFloatOrComplex(c10::ScalarType scalar_type)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/reduction_utils.cc#L109) — Checks that the provided dtype is either floating point or complex. — documented in [reductions](../../../../concepts/reductions.md)

