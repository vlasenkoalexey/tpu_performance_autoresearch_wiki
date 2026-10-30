---
title: 'Module: csrc/common/utils.cc'
type: catalog
provenance: extracted
module: csrc/common/utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  LosslessToString: LosslessToString(ecc478f4b56c5f74).
  TensorHasTrivialLayout: TensorHasTrivialLayout(b580d0b7e29ca914).
  PercAsStr: PercAsStr(823807576f586005).
  LogLines: LogLines(c8024318075daf50).
  kMaxLogMessageSize: kMaxLogMessageSize.
---
# Module: [`csrc/common/utils.cc`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc)

## Functions
- <a id="LogLines"></a>`LogLines(std::string_view s)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L49) — Log a very long string as multiple lines. This is to work around ABSL_LOG's
- `LosslessToString(const c10::complex<double>& value)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L40)
- <a id="LosslessToString"></a>`LosslessToString(double value)` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L34) — TODO: b/441998432 - Use to_chars() once the OSS toolchain (currently clang
- <a id="PercAsStr"></a>`PercAsStr(uint64_t num, uint64_t den)` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L74) — Format percentage.
- <a id="TensorHasTrivialLayout"></a>`TensorHasTrivialLayout(const at::Tensor& tensor)` — [`L82`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L82) — Does the given tensor have a trivial and standard layout in memory.

## Module values
- <a id="kMaxLogMessageSize"></a>`kMaxLogMessageSize` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/common/utils.cc#L47) — To prevent the log system from truncating the log messages, each

