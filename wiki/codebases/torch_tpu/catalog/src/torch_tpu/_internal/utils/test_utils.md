---
title: 'Module: src/torch_tpu/_internal/utils/test_utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/test_utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.test_utils`/
symbols:
  _assert_tensor_close: _assert_tensor_close().
  _add_tolerance_suggestions: _add_tolerance_suggestions().
  _assert_tensor_close.strict_msg_handler: _assert_tensor_close().strict_msg_handler().
  assert_close: assert_close().
  CheckValueMode: CheckValueMode#
  _assert_tensor_close.msg_handler: _assert_tensor_close().msg_handler().
  compute_optimal_tolerances: compute_optimal_tolerances().
  _assert_tensor_close.refine_assert_close_message: _assert_tensor_close().refine_assert_close_message().
  _raw_assert_tensor_close: _raw_assert_tensor_close().
  CheckValueMode.LOOSE: CheckValueMode#LOOSE.
  _decode_sub_byte_tensor: _decode_sub_byte_tensor().
  _round_up_float: _round_up_float().
  _assert_tensor_close.get_indices: _assert_tensor_close().get_indices().
  CheckValueMode.STRICT: CheckValueMode#STRICT.
  _lookup_tolerances: _lookup_tolerances().
  Tolerance.Tolerance: Tolerance.Tolerance.
  _format_sci_ceil: _format_sci_ceil().
  _RE_INDEX_CAPTURE: _RE_INDEX_CAPTURE.
  _RE_STRICT_REL_FAILURE: _RE_STRICT_REL_FAILURE.
  _RE_SCALAR_COMP_FAILURE: _RE_SCALAR_COMP_FAILURE.
  _raw_assert_tensor_close._close: _raw_assert_tensor_close()._close().
  _SAFETY_FACTOR._SAFETY_FACTOR: _SAFETY_FACTOR._SAFETY_FACTOR.
  _FP4_E2M1_VALUES._FP4_E2M1_VALUES: _FP4_E2M1_VALUES._FP4_E2M1_VALUES.
  CheckValueMode.SKIP: CheckValueMode#SKIP.
  get_torch_version: get_torch_version.
  libtpu_version: libtpu_version.
  parse_version: parse_version.
---
# Module: [`src/torch_tpu/_internal/utils/test_utils.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py)

## Classes
### <a id="CheckValueMode"></a>`CheckValueMode`  ·  implements/extends Enum
- def: [`src/torch_tpu/_internal/utils/test_utils.py:51`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L51)
- doc: How to check the values when comparing tensors.
- signature: `class CheckValueMode(enum.Enum):`
- members:
  - <a id="CheckValueMode.LOOSE"></a>`LOOSE` — [`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L68)
  - <a id="CheckValueMode.SKIP"></a>`SKIP` — [`L67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L67)
  - <a id="CheckValueMode.STRICT"></a>`STRICT` — [`L69`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L69)
- used by: (5 test-only callers)

## Functions
- <a id="_add_tolerance_suggestions"></a>`_add_tolerance_suggestions(msg: str, check_mode: CheckValueMode, actual: Any, expected: Any)` — [`L433`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L433) — Augments the error message with tolerance suggestions.
- <a id="_assert_tensor_close"></a>`_assert_tensor_close(actual: torch.Tensor, expected: torch.Tensor, rtol: float | None = None, atol: Tolerance | None = None, preamble: str | None = None, check_value: CheckValueMode | None = None)` — [`L542`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L542) — Single-tensor assert_close implementation.
- <a id="_raw_assert_tensor_close._close"></a>`_close(actual_value: float, expected_value: float)` — [`L231`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L231) — Returns True if the values are close.
- <a id="_decode_sub_byte_tensor"></a>`_decode_sub_byte_tensor(t: torch.Tensor)` — [`L509`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L509) — Decodes a sub-byte dtype tensor for value comparison.
- <a id="_format_sci_ceil"></a>`_format_sci_ceil(val: float)` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L36) — Formats a float in scientific notation, rounded up to 1 decimal place.
- <a id="_lookup_tolerances"></a>`_lookup_tolerances(actual: torch.Tensor, expected: torch.Tensor, rtol: float | None, atol: float | None)` — [`L173`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L173) — Looks up the tolerances for comparing the given tensors.
- <a id="_raw_assert_tensor_close"></a>`_raw_assert_tensor_close(actual: torch.Tensor, expected: torch.Tensor, msg: Callable[[str], str], rtol: float | None = None, atol: Tolerance | None = None)` — [`L205`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L205) — Raw assert_close implementation.
- <a id="_round_up_float"></a>`_round_up_float(val: float)` — [`L267`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L267) — Rounds float upward towards +infinity to prevent truncation errors.
- <a id="assert_close"></a>`assert_close(actual: Any, expected: Any, rtol: float | None = None, atol: Tolerance | None = None, preamble: str | None = None, check_value: CheckValueMode | None = None, check_dtype: bool = True)` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L80) — Assert that `actual` and `expectec` are sufficiently close.
- <a id="compute_optimal_tolerances"></a>`compute_optimal_tolerances(actual: Any, expected: Any, safety_factor: float = _SAFETY_FACTOR)` — [`L275`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L275) — Computes optimal (atol, rtol) bounds for comparing actual and expected.
- <a id="_assert_tensor_close.get_indices"></a>`get_indices(msg: str)` — [`L636`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L636) — Returns the indices from the given message.
- <a id="_assert_tensor_close.msg_handler"></a>`msg_handler(msg: str)` — [`L717`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L717)
- <a id="_assert_tensor_close.refine_assert_close_message"></a>`refine_assert_close_message(msg: str)` — [`L663`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L663) — Refines the message from torch.testing.assert_close with more details.
- <a id="_assert_tensor_close.strict_msg_handler"></a>`strict_msg_handler(msg: str, is_relative: bool = False)` — [`L744`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L744)

## Module values
- <a id="Tolerance.Tolerance"></a>`Tolerance` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L31)
- <a id="_FP4_E2M1_VALUES._FP4_E2M1_VALUES"></a>`_FP4_E2M1_VALUES` — [`L500`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L500)
- <a id="_RE_INDEX_CAPTURE"></a>`_RE_INDEX_CAPTURE` — [`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L72)
- <a id="_RE_SCALAR_COMP_FAILURE"></a>`_RE_SCALAR_COMP_FAILURE` — [`L77`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L77)
- <a id="_RE_STRICT_REL_FAILURE"></a>`_RE_STRICT_REL_FAILURE` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L74)
- <a id="_SAFETY_FACTOR._SAFETY_FACTOR"></a>`_SAFETY_FACTOR` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L33)
- <a id="get_torch_version"></a>`get_torch_version` — [`L787`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L787)
- <a id="libtpu_version"></a>`libtpu_version` — [`L788`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L788)
- <a id="parse_version"></a>`parse_version` — [`L789`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/test_utils.py#L789)

