---
title: 'Module: csrc/common/error_utils.cc'
type: catalog
provenance: extracted
module: csrc/common/error_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TranslateToC10ErrorAndThrow: TranslateToC10ErrorAndThrow(37625dab65a739d3).
  TtError.TtError: TtError#TtError(eed07011c2dc91d6).
  SafeWrapDim: SafeWrapDim(f0457be0504a4a8).
  AdaptExternalErrorMessage: AdaptExternalErrorMessage(6ccff4770ff7ddc3).
  NumElements: NumElements(29997028681ee8c2).
  GetStickyError: GetStickyError(c8a92d17d58c956f).
  SafeMultiply: SafeMultiply(f0457be0504a4a8).
  GetEnableDebugChecks: GetEnableDebugChecks(c9857a73d68e59ba).
  AdaptXlaError: AdaptXlaError(1b2dfccf5020845a).
  AdaptVfioDeviceCollisionError: internal/AdaptVfioDeviceCollisionError(942748e557ec07ce).
  SyncAndCheckStickyError: SyncAndCheckStickyError(49f6e7a06ebc5aa8).
  SafeAdd: SafeAdd(f0457be0504a4a8).
  SetStickyError: SetStickyError(2814731695a089b8).
  ClearStickyError: ClearStickyError(49f6e7a06ebc5aa8).
  WaitForPendingAssertionChecks: WaitForPendingAssertionChecks(49f6e7a06ebc5aa8).
  CheckDeviceIsTpu: CheckDeviceIsTpu(3dac8a611a162a84).
  DecrementPendingAssertionChecks: DecrementPendingAssertionChecks(49f6e7a06ebc5aa8).
  IncrementPendingAssertionChecks: IncrementPendingAssertionChecks(49f6e7a06ebc5aa8).
  g_has_sticky_error: internal/g_has_sticky_error.
  IsXlaOomError: IsXlaOomError(4f113b8b49399b0a).
  MakeErrorMessage: MakeErrorMessage(6e57f2f39f67660e).
  FormatVfioCollisionMessage: '`$anonymous_namespace_csrc/common/error_utils.cc`/FormatVfioCollisionMessage(cf2bb20406cb4ef8).'
  FindProcessesHoldingDevice: '`$anonymous_namespace_csrc/common/error_utils.cc`/FindProcessesHoldingDevice(22731a89093ea261).'
  g_sticky_error: '`$anonymous_namespace_csrc/common/error_utils.cc`/g_sticky_error.'
  g_pending_assertions: '`$anonymous_namespace_csrc/common/error_utils.cc`/g_pending_assertions.'
  g_assertion_mutex: '`$anonymous_namespace_csrc/common/error_utils.cc`/g_assertion_mutex.'
  g_sticky_error_mutex: '`$anonymous_namespace_csrc/common/error_utils.cc`/g_sticky_error_mutex.'
  IsVfioDeviceCollisionError: '`$anonymous_namespace_csrc/common/error_utils.cc`/IsVfioDeviceCollisionError(4f113b8b49399b0a).'
  StartsWithAllowedWord: '`$anonymous_namespace_csrc/common/error_utils.cc`/StartsWithAllowedWord(622bf5f99ebeb951).'
  ReadProcessName: '`$anonymous_namespace_csrc/common/error_utils.cc`/ReadProcessName(9d1d804ca2daf246).'
  DeviceHolder: '`$anonymous_namespace_csrc/common/error_utils.cc`/DeviceHolder#'
  DeviceHolder.name: '`$anonymous_namespace_csrc/common/error_utils.cc`/DeviceHolder#name.'
  ExceptionType: ExceptionType#
  ExtractVfioDevicePath: '`$anonymous_namespace_csrc/common/error_utils.cc`/ExtractVfioDevicePath(904f61f3a16c5694).'
  ExceptionType.kTtError: ExceptionType#kTtError.
  g_assertion_cv: '`$anonymous_namespace_csrc/common/error_utils.cc`/g_assertion_cv.'
  MatchVfioCollisionMessage: '`$anonymous_namespace_csrc/common/error_utils.cc`/MatchVfioCollisionMessage(99b3db28d45a9d54).'
  ExceptionType.kC10Error: ExceptionType#kC10Error.
  CanonicalizeDevicePath: '`$anonymous_namespace_csrc/common/error_utils.cc`/CanonicalizeDevicePath(6ccff4770ff7ddc3).'
  DeviceHolder.pid: '`$anonymous_namespace_csrc/common/error_utils.cc`/DeviceHolder#pid.'
  kMaxProcessNameLen: '`$anonymous_namespace_csrc/common/error_utils.cc`/kMaxProcessNameLen.'
  kAllowedStartingWords: '`$anonymous_namespace_csrc/common/error_utils.cc`/kAllowedStartingWords.'
---
# Module: [`csrc/common/error_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc)

## Classes
### <a id="DeviceHolder"></a>`DeviceHolder`
- def: [`csrc/common/error_utils.cc:1060`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1060)
- doc: Information about a process holding a device node open.
- signature: `struct DeviceHolder`
- members:
  - <a id="DeviceHolder.name"></a>`name` — [`L1062`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1062)
  - <a id="DeviceHolder.pid"></a>`pid` — [`L1061`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1061)
- used by: [`AdaptVfioDeviceCollisionError`](error_utils.cc.md#AdaptVfioDeviceCollisionError), [`FormatVfioCollisionMessage`](error_utils.cc.md#FormatVfioCollisionMessage), [`FindProcessesHoldingDevice`](error_utils.cc.md#FindProcessesHoldingDevice)

### <a id="ExceptionType"></a>`ExceptionType`
- def: [`csrc/common/error_utils.cc:1159`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1159)
- signature: `enum class ExceptionType`
- members:
  - <a id="ExceptionType.kC10Error"></a>`kC10Error` — [`L1161`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1161)
  - <a id="ExceptionType.kTtError"></a>`kTtError` — [`L1160`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1160)
- used by: [`TranslateToC10ErrorAndThrow`](error_utils.cc.md#TranslateToC10ErrorAndThrow), [`TtError`](error_utils.cc.md#TtError.TtError), [`MakeErrorMessage`](error_utils.cc.md#MakeErrorMessage)

## Functions
- <a id="AdaptExternalErrorMessage"></a>`AdaptExternalErrorMessage(const std::string_view message)` — [`L786`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L786) — Adapts an external error message (e.g., from PyTorch or OpenXLA) to conform
- `AdaptVfioDeviceCollisionError(absl::Status status)` — [`L1155`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1155) — Rewrites a VFIO device-collision error into an actionable message instructing
- <a id="AdaptVfioDeviceCollisionError"></a>`AdaptVfioDeviceCollisionError(absl::Status status, std::string_view proc_root)` — [`L1140`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1140) — Like AdaptVfioDeviceCollisionError, but scans `proc_root` instead of
- <a id="AdaptXlaError"></a>`AdaptXlaError(const absl::Status& status, const std::string_view context)` — [`L986`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L986) — Adapts an external error from OpenXLA to comply to TorchTPU error guidelines. — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="CanonicalizeDevicePath"></a>`CanonicalizeDevicePath(std::string_view path)` — [`L1039`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1039) — Resolves symlinks in `path`, returning `path` unchanged on failure.
- <a id="CheckDeviceIsTpu"></a>`CheckDeviceIsTpu(const c10::optional<at::Device> device_opt, const std::string_view op_name)` — [`L904`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L904) — Checks that `device_opt` is TPU (PrivateUse1), or crashes if it is not. — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="ClearStickyError"></a>`ClearStickyError()` — [`L979`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L979) — Clears the global sticky error state. Used for testing. — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="DecrementPendingAssertionChecks"></a>`DecrementPendingAssertionChecks()` — [`L956`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L956) — Decrements the count of pending asynchronous assertion checks.
- <a id="ExtractVfioDevicePath"></a>`ExtractVfioDevicePath(std::string_view message)` — [`L1050`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1050) — Extracts the device node path (e.g. "/dev/vfio/0") from `message`, or
- <a id="FindProcessesHoldingDevice"></a>`FindProcessesHoldingDevice(std::string_view device_path, std::string_view proc_root)` — [`L1066`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1066) — Returns processes under `proc_root` holding `device_path` open.
- `FindProcessesHoldingDevice(std::string_view device_path, std::string_view proc_root)` — [`L1066`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1066) — Returns processes under `proc_root` holding `device_path` open.
- <a id="FormatVfioCollisionMessage"></a>`FormatVfioCollisionMessage(std::optional<std::string_view> device_path, absl::Span<const DeviceHolder> holders)` — [`L1108`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1108) — Formats the user-facing device-collision error message with colliding
- <a id="GetEnableDebugChecks"></a>`GetEnableDebugChecks()` — [`L811`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L811) — Returns true if debug checks are enabled via the
- <a id="GetStickyError"></a>`GetStickyError()` — [`L946`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L946) — Gets the global sticky error state. — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="IncrementPendingAssertionChecks"></a>`IncrementPendingAssertionChecks()` — [`L951`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L951) — Increments the count of pending asynchronous assertion checks.
- <a id="IsVfioDeviceCollisionError"></a>`IsVfioDeviceCollisionError(const absl::Status& status)` — [`L1014`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1014) — Returns true if `status` is a VFIO device-collision error, i.e. libtpu
- <a id="IsXlaOomError"></a>`IsXlaOomError(const absl::Status& status)` — [`L911`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L911) — Returns true if the status is an XLA OOM error. This is a heuristic that
- <a id="MakeErrorMessage"></a>`MakeErrorMessage(const absl::Status& status, const c10::SourceLocation& thrown_from, const ExceptionType exception_type)` — [`L1169`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1169) — Returns the error message for a Status error.
- <a id="MatchVfioCollisionMessage"></a>`MatchVfioCollisionMessage(std::string_view message, std::string* device_path)` — [`L1002`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1002) — Returns true if `message` indicates a VFIO collision. If a device node is
- <a id="NumElements"></a>`NumElements(absl::Span<const int64_t> dims)` — [`L854`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L854) — Returns the number of elements in a tensor with the given dimensions.
- `NumElements(const at::Tensor& tensor)` — [`L867`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L867)
- <a id="ReadProcessName"></a>`ReadProcessName(std::string_view proc_root, int pid)` — [`L1025`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1025) — Returns the command line for `pid` read from <proc_root>/<pid>/cmdline, or
- <a id="SafeAdd"></a>`SafeAdd(const int64_t x, const int64_t y)` — [`L821`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L821) — Returns the sum of x and y, or returns an error if the sum overflows or
- <a id="SafeMultiply"></a>`SafeMultiply(const int64_t x, const int64_t y)` — [`L837`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L837) — Returns the product of two numbers, or returns an error if the product
- `SafeMultiply(const uint64_t x, const uint64_t y)` — [`L845`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L845)
- <a id="SafeWrapDim"></a>`SafeWrapDim(int64_t dim, int64_t dim_bound)` — [`L871`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L871) — Safely wraps a dimension index.
- <a id="SetStickyError"></a>`SetStickyError(absl::Status status)` — [`L935`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L935) — Sets the global sticky error state. Subsequent ops should fail if this is — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="StartsWithAllowedWord"></a>`StartsWithAllowedWord(const std::string_view message)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L84) — Helper to check if a message starts with any of the allowed words.
- <a id="SyncAndCheckStickyError"></a>`SyncAndCheckStickyError()` — [`L972`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L972) — Blocks until all pending asynchronous assertion checks have completed, and — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="TranslateToC10ErrorAndThrow"></a>`TranslateToC10ErrorAndThrow(const TtError& e)` — [`L1223`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1223) — Translates a TtError to a c10::Error or one of its subclasses and throws it. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="WaitForPendingAssertionChecks"></a>`WaitForPendingAssertionChecks()` — [`L965`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L965) — Blocks until all pending asynchronous assertion checks have completed.

## Module values
- <a id="g_assertion_cv"></a>`g_assertion_cv` — [`L931`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L931)
- <a id="g_assertion_mutex"></a>`g_assertion_mutex` — [`L930`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L930)
- <a id="g_has_sticky_error"></a>`g_has_sticky_error` — [`L922`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L922) — Aligned to 64 bytes (cache-line size) to prevent false sharing with other
- <a id="g_pending_assertions"></a>`g_pending_assertions` — [`L932`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L932)
- <a id="g_sticky_error"></a>`g_sticky_error` — [`L927`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L927)
- <a id="g_sticky_error_mutex"></a>`g_sticky_error_mutex` — [`L926`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L926)
- <a id="kAllowedStartingWords"></a>`kAllowedStartingWords` — [`L80`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L80) — Words that are allowed to start an error message with an uppercase letter.
- <a id="kMaxProcessNameLen"></a>`kMaxProcessNameLen` — [`L1021`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1021) — Upper bound on the process cmdline included in error messages.

## Other members
- <a id="TtError.TtError"></a>`TtError.TtError` — [`L1211`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.cc#L1211) — documented in [error-handling](../../../concepts/error-handling.md)

