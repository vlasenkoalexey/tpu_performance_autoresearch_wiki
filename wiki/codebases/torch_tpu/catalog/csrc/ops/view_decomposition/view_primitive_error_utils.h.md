---
title: 'Module: csrc/ops/view_decomposition/view_primitive_error_utils.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/view_primitive_error_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetViewPrimitiveErrorSuffix: GetViewPrimitiveErrorSuffix(6e4e4912803e00f0).
  GetUpdateLayoutBugSuffix: GetUpdateLayoutBugSuffix(475744e32cae6b3a).
  GetViewPrimitiveShloErrorSuffix: GetViewPrimitiveShloErrorSuffix(a860c7ff9eca7903).
  ViewPrimitiveBugSuffix: ViewPrimitiveBugSuffix#
  ViewPrimitiveBugSuffix.kHide: ViewPrimitiveBugSuffix#kHide.
  ViewPrimitiveErrorOptions.bug_suffix: ViewPrimitiveErrorOptions#bug_suffix.
  ShouldAppendBugSuffix: ShouldAppendBugSuffix(4a9c8c2eeedf43d).
  ViewPrimitiveErrorOptions.leading_semicolon: ViewPrimitiveErrorOptions#leading_semicolon.
  ViewPrimitiveBugSuffix.kAppend: ViewPrimitiveBugSuffix#kAppend.
  ViewPrimitiveErrorOptions: ViewPrimitiveErrorOptions#
---
# Module: [`csrc/ops/view_decomposition/view_primitive_error_utils.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h)

## Classes
### <a id="ViewPrimitiveBugSuffix"></a>`ViewPrimitiveBugSuffix`
- def: [`csrc/ops/view_decomposition/view_primitive_error_utils.h:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L55)
- doc: Settings for controlling the bug suffix.
- signature: `enum class ViewPrimitiveBugSuffix`
- members:
  - <a id="ViewPrimitiveBugSuffix.kAppend"></a>`kAppend` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L57)
  - <a id="ViewPrimitiveBugSuffix.kHide"></a>`kHide` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L56)
- used by: [`ViewPrimitiveShlo`](bitcast_primitive.cc.md#ViewPrimitiveShlo), [`GetViewPrimitiveShloErrorSuffix`](view_primitive_error_utils.h.md#GetViewPrimitiveShloErrorSuffix), [`TestBody`](view_primitive_error_utils_test.cc.md#ViewPrimitiveErrorUtilsTest_GetViewPrimitiveShloErrorSuffix_Test.TestBody), [`TestBody`](view_primitive_error_utils_test.cc.md#ViewPrimitiveErrorUtilsTest_GetViewPrimitiveErrorSuffix_Test.TestBody), [`ShouldAppendBugSuffix`](view_primitive_error_utils.h.md#ShouldAppendBugSuffix), [`bug_suffix`](view_primitive_error_utils.h.md#ViewPrimitiveErrorOptions.bug_suffix), [`leading_semicolon`](view_primitive_error_utils.h.md#ViewPrimitiveErrorOptions.leading_semicolon)

### <a id="ViewPrimitiveErrorOptions"></a>`ViewPrimitiveErrorOptions`
- def: [`csrc/ops/view_decomposition/view_primitive_error_utils.h:61`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L61)
- doc: Options to the `GetViewPrimitiveErrorSuffix()` function.
- signature: `struct ViewPrimitiveErrorOptions`
- members:
  - <a id="ViewPrimitiveErrorOptions.bug_suffix"></a>`bug_suffix` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L66) — Appends the bug suffix at the end of the error message.
  - <a id="ViewPrimitiveErrorOptions.leading_semicolon"></a>`leading_semicolon` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L63) — Adds a "; " before the error message.
- uses (calls/refs, reference-scoped): [`ViewPrimitiveBugSuffix`](view_primitive_error_utils.h.md#ViewPrimitiveBugSuffix), [`kAppend`](view_primitive_error_utils.h.md#ViewPrimitiveBugSuffix.kAppend)
- used by: [`GetViewPrimitiveErrorSuffix`](view_primitive_error_utils.h.md#GetViewPrimitiveErrorSuffix)

## Functions
- <a id="GetUpdateLayoutBugSuffix"></a>`GetUpdateLayoutBugSuffix(const ViewPrimitiveT& view_primitive, const StridedLayout& layout)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L98) — Returns a string to be appended to checks in the view decomposition logic,
- <a id="GetViewPrimitiveErrorSuffix"></a>`GetViewPrimitiveErrorSuffix` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L78) — Returns a string to be appended to checks in the view decomposition logic,
- <a id="GetViewPrimitiveShloErrorSuffix"></a>`GetViewPrimitiveShloErrorSuffix(const ViewPrimitiveT& view_primitive, const absl::Span<const int64_t> shape, const ViewPrimitiveBugSuffix bug_suffix = ViewPrimitiveBugSuffix::kAppend)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L118) — Returns a string to be appended to checks in the view decomposition logic,
- <a id="ShouldAppendBugSuffix"></a>`ShouldAppendBugSuffix(const ViewPrimitiveBugSuffix bug_suffix)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_primitive_error_utils.h#L69)

