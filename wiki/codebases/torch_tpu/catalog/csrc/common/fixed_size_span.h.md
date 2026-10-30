---
title: 'Module: csrc/common/fixed_size_span.h'
type: catalog
provenance: extracted
module: csrc/common/fixed_size_span.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  FixedSizeSpan: torch_tpu/FixedSizeSpan#
  tuple_size: std/tuple_size#
  FixedSizeSpan.FixedSizeSpan-T-kSize: torch_tpu/FixedSizeSpan#`FixedSizeSpan<T, kSize>`(ed733b9a10096646).
  MoveToStdArray: torch_tpu/MoveToStdArray(e6e6f5ab4bf74e5c).
  tuple_element: std/tuple_element#
  get: torch_tpu/get(73c25e1684228f8c).
  tuple_element.type: std/tuple_element#type#
---
# Module: [`csrc/common/fixed_size_span.h`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h)

## Classes
### <a id="FixedSizeSpan"></a>`FixedSizeSpan`  ·  implements/extends Span
- def: [`csrc/common/fixed_size_span.h:34`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L34)
- doc: Like absl::Span, but with a fixed size determined at compile time.
- signature: `template <typename T, int kSize> class FixedSizeSpan : public absl::Span<T>`
- members:
  - `FixedSizeSpan<T, kSize>(const std::array<U, kSize>& array)` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L53) — Constructs from an std::array of the expected size.
  - <a id="FixedSizeSpan.FixedSizeSpan-T-kSize"></a>`FixedSizeSpan<T, kSize>(const absl::Span<T> span)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L40) — Constructs from an absl::Span. Requires that the span has the expected
  - `FixedSizeSpan<T, kSize>(const std::initializer_list<T> list)` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L48) — Constructs from an initializer list. Requires that the initializer list
- uses (calls/refs, reference-scoped): [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator)
- used by: [`DispatchOp`](../eager/op_dispatcher.h.md#DispatchOp), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenArangeStartOut`](../ops/arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenGridSampler3dBackward`](../ops/grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenCdistBackward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistForward), [`AtenLinspaceOut`](../ops/linspace/linspace_aten_kernels.cc.md#AtenLinspaceOut), [`AtenSelectScatterOut`](../ops/select_scatter/select_scatter_aten_kernels.cc.md#AtenSelectScatterOut), [`AtenSliceScatterOut`](../ops/slice_scatter/slice_scatter_aten_kernels.cc.md#AtenSliceScatterOut), [`AtenConstantPadNd`](../ops/constant_pad/constant_pad_aten_kernels.cc.md#AtenConstantPadNd), [`AtenPdistBackward`](../ops/distance/dist_aten_kernels.cc.md#AtenPdistBackward), [`AtenLogitBackwardGradInput`](../ops/logit/logit_aten_kernels.cc.md#AtenLogitBackwardGradInput), [`AtenSelectScatter`](../ops/select_scatter/select_scatter_aten_kernels.cc.md#AtenSelectScatter), [`AtenSliceScatter`](../ops/slice_scatter/slice_scatter_aten_kernels.cc.md#AtenSliceScatter), [`AtenSoftplusBackwardGradInput`](../ops/softplus/softplus_aten_kernels.cc.md#AtenSoftplusBackwardGradInput), [`AtenSoftplusOut`](../ops/softplus/softplus_aten_kernels.cc.md#AtenSoftplusOut), [`AtenAddcmulOut`](../ops/addcmul/addcmul_aten_kernels.cc.md#AtenAddcmulOut), [`AtenEmbeddingRenorm_`](../ops/embedding/embedding_aten_kernels.cc.md#AtenEmbeddingRenorm_), [`AtenGeluBackwardGradInput`](../ops/gelu/gelu_aten_kernels.cc.md#AtenGeluBackwardGradInput), [`AtenMseLossBackward`](../ops/mse_loss/mse_loss_aten_kernels.cc.md#AtenMseLossBackward), [`AtenMseLossOut`](../ops/mse_loss/mse_loss_aten_kernels.cc.md#AtenMseLossOut), [`AtenSigmoidBackwardGradInput`](../ops/sigmoid/sigmoid_aten_kernels.cc.md#AtenSigmoidBackwardGradInput), [`AtenToDenseSparse`](../ops/sparse_coo/sparse_coo_aten_kernels.cc.md#AtenToDenseSparse), [`AllToAllBaseUnevenSplits`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.AllToAllBaseUnevenSplits), [`AtenHardswishBackward`](../ops/hardswish/hardswish_aten_kernels.cc.md#AtenHardswishBackward), [`AtenXlogyOutTensor`](../ops/xlogy/xlogy_aten_kernels.cc.md#AtenXlogyOutTensor), [`DynamicArange`](../ops/dynamic/dynamic_arange/dynamic_arange.cc.md#DynamicArange), [`SetDimensionLogicalSize`](../ops/dynamic/set_dimension_logical_size/set_dimension_logical_size.cc.md#SetDimensionLogicalSize), [`AtenGridSampler2d`](../ops/grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler2d), [`AtenHardsigmoidBackwardGradInput`](../ops/hardsigmoid/hardsigmoid_aten_kernels.cc.md#AtenHardsigmoidBackwardGradInput), [`AtenIndexFillIntTensor_`](../ops/index_fill/index_fill_aten_kernels.cc.md#AtenIndexFillIntTensor_), [`AtenUpsampleNearest1dOut`](../ops/upsample/upsample_aten_kernels.cc.md#AtenUpsampleNearest1dOut), [`AtenUpsampleNearest2dOut`](../ops/upsample/upsample_aten_kernels.cc.md#AtenUpsampleNearest2dOut)  (+130 more)

### <a id="tuple_element"></a>`tuple_element`
- def: [`csrc/common/fixed_size_span.h:140`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L140)
- doc: 2. Specialization of `std::tuple_element`
- signature: `template <std::size_t I, typename T, std::size_t N> struct std::tuple_element<I, torch_tpu::FixedSizeSpan<T, N>>`
- uses (calls/refs, reference-scoped): [`FixedSizeSpan`](fixed_size_span.h.md#FixedSizeSpan)

### <a id="tuple_element.type"></a>`tuple_element.type`
- def: [`csrc/common/fixed_size_span.h:141`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L141)
- signature: `using type = T`

### <a id="tuple_size"></a>`tuple_size`
- def: [`csrc/common/fixed_size_span.h:135`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L135)
- doc: 1. Specialization of `std::tuple_size`
- signature: `template <typename T, std::size_t N> struct std::tuple_size<torch_tpu::FixedSizeSpan<T, N>> : std::integral_constant<std::size_t, N>`
- uses (calls/refs, reference-scoped): [`FixedSizeSpan`](fixed_size_span.h.md#FixedSizeSpan)
- used by: [`gtest_BroadcastTestsBroadcastTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_BroadcastTestsBroadcastTest_dummy_), [`gtest_ConvolutionLikeBoundedTestsConvolutionLikeBoundedTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_ConvolutionLikeBoundedTestsConvolutionLikeBoundedTest_dummy_), [`gtest_ConvolutionLikeUnsupportedTestsConvolutionLikeUnsupportedTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_ConvolutionLikeUnsupportedTestsConvolutionLikeUnsupportedTest_dummy_), [`gtest_DynamicBroadcastTestsDynamicBroadcastTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_DynamicBroadcastTestsDynamicBroadcastTest_dummy_), [`gtest_DynamicReshapeFromStaticDimensionsTestsDynamicReshapeFromStaticDimensionsTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_DynamicReshapeFromStaticDimensionsTestsDynamicReshapeFromStaticDimensionsTest_dummy_), [`gtest_DispatchScanTestDispatchScanNumScanInputsTest_dummy_`](../internal/compile/dispatch_scan_test.cc.md#gtest_DispatchScanTestDispatchScanNumScanInputsTest_dummy_), [`gtest_IotaOutOfBoundsTestsIotaOutOfBoundsTest_dummy_`](../ops/op_builder_utils_test.cc.md#gtest_IotaOutOfBoundsTestsIotaOutOfBoundsTest_dummy_), [`gtest_ScanLoweringMultiScanBuilderTest_dummy_`](../ops/scan_builder_test.cc.md#gtest_ScanLoweringMultiScanBuilderTest_dummy_), [`gtest_ScanLoweringScanBuilderTest_dummy_`](../ops/scan_builder_test.cc.md#gtest_ScanLoweringScanBuilderTest_dummy_)

## Functions
- <a id="MoveToStdArray"></a>`MoveToStdArray(torch_tpu::FixedSizeSpan<T, 4> span)` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L100)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 5> span)` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L105)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 0> span)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L84) — Move elements from a FixedSizeSpan to an std::array of the same size.
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 8> span)` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L121)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 1> span)` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L88)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 7> span)` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L115)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 3> span)` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L96)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 2> span)` — [`L92`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L92)
- `MoveToStdArray(torch_tpu::FixedSizeSpan<T, 6> span)` — [`L110`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L110)
- <a id="get"></a>`get(FixedSizeSpan<T, N>& span)` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L61) — For supporting structured bindings in lambdas.
- `get(const FixedSizeSpan<T, N>& span)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L67)
- `get(FixedSizeSpan<T, N>&& span)` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/fixed_size_span.h#L73)

