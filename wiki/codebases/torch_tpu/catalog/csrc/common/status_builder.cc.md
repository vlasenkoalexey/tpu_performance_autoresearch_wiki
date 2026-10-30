---
title: 'Module: csrc/common/status_builder.cc'
type: catalog
provenance: extracted
module: csrc/common/status_builder.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  MaybeAddCppSourceLoc: internal/MaybeAddCppSourceLoc(d1a8344382e811db).
  SetRootOpNamePayload: internal/SetRootOpNamePayload(942748e557ec07ce).
  StatusBuilder.StatusBuilder: StatusBuilder#StatusBuilder(607516e9740bbeaf).
  StatusBuilder.JoinMessageToStatus: StatusBuilder#JoinMessageToStatus(6ce32a2124d1a670).
  StatusBuilder.CreateStatus: StatusBuilder#CreateStatus(1b6f9d1eb9692235).
  TorchShowCppStacktraces: TorchShowCppStacktraces(d957277c84f0858b).
  CppStackTracesEnabled: CppStackTracesEnabled(c9857a73d68e59ba).
  StatusBuilderWithMessage.operator-Status: StatusBuilderWithMessage#`operator Status`(1b6f9d1eb9692235).
  StatusBuilder.Rep.Rep: StatusBuilder#Rep#Rep(7fdfbc69d4012d7c).
  GetMessageWithCppErrorTrace: internal/GetMessageWithCppErrorTrace(481c591cc328ef24).
  GetRootOpNamePayload: internal/GetRootOpNamePayload(481c591cc328ef24).
  StatusBuilder.Rep.InitStream: StatusBuilder#Rep#InitStream(49f6e7a06ebc5aa8).
  StatusBuilder.Rep.-Rep: StatusBuilder#Rep#`~Rep`(ced63f7c635d850d).
  StatusBuilder.-StatusBuilder: StatusBuilder#`~StatusBuilder`(ced63f7c635d850d).
---
# Module: [`csrc/common/status_builder.cc`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc)

## Functions
- <a id="CppStackTracesEnabled"></a>`CppStackTracesEnabled()` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L50) — Returns true if C++ stack traces are enabled. This is controlled by the
- <a id="GetMessageWithCppErrorTrace"></a>`GetMessageWithCppErrorTrace(const absl::Status& status)` — [`L162`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L162) — Returns the message of the given status, with the C++ error trace in its
- <a id="GetRootOpNamePayload"></a>`GetRootOpNamePayload(const absl::Status& status)` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L142) — Returns the root op name in the absl::Status payload.
- <a id="MaybeAddCppSourceLoc"></a>`MaybeAddCppSourceLoc(absl::Status status, const std::string_view file, const int line, const std::string_view function)` — [`L148`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L148) — Appends the given C++ source location to the absl::Status payload if — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="SetRootOpNamePayload"></a>`SetRootOpNamePayload(absl::Status status, std::string_view root_op_name)` — [`L136`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L136) — Sets the root op name in the absl::Status payload. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="TorchShowCppStacktraces"></a>`TorchShowCppStacktraces()` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L34) — Returns the state of the TORCH_SHOW_CPP_STACKTRACES environment variable:

## Other members
- `StatusBuilder` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L58)
- `StatusBuilder` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L62)
- `Rep` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L73)
- `Rep` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L74)
- <a id="StatusBuilder.-StatusBuilder"></a>`StatusBuilder.-StatusBuilder` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L60)
- <a id="StatusBuilder.CreateStatus"></a>`StatusBuilder.CreateStatus` — [`L120`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L120)
- <a id="StatusBuilder.JoinMessageToStatus"></a>`StatusBuilder.JoinMessageToStatus` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L88)
- <a id="StatusBuilder.Rep.-Rep"></a>`StatusBuilder.Rep.-Rep` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L75)
- <a id="StatusBuilder.Rep.InitStream"></a>`StatusBuilder.Rep.InitStream` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L86)
- <a id="StatusBuilder.Rep.Rep"></a>`StatusBuilder.Rep.Rep` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L77)
- <a id="StatusBuilder.StatusBuilder"></a>`StatusBuilder.StatusBuilder` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L65) — documented in [error-handling](../../../concepts/error-handling.md)
- <a id="StatusBuilderWithMessage.operator-Status"></a>`StatusBuilderWithMessage.operator-Status` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.cc#L68)

