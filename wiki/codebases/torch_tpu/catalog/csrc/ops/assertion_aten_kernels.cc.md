---
title: 'Module: csrc/ops/assertion_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/assertion_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAssertAsyncMsg: AtenAssertAsyncMsg(da71742833b00b67).
  ScheduleAsyncAssertionCheck: '`$anonymous_namespace_csrc/ops/assertion_aten_kernels.cc`/ScheduleAsyncAssertionCheck(da71742833b00b67).'
  ValidateAssertionInput: '`$anonymous_namespace_csrc/ops/assertion_aten_kernels.cc`/ValidateAssertionInput(45982de3b0bc1087).'
  ShouldScheduleAsyncCheck: '`$anonymous_namespace_csrc/ops/assertion_aten_kernels.cc`/ShouldScheduleAsyncCheck(b580d0b7e29ca914).'
  AtenAssertAsync: AtenAssertAsync(45982de3b0bc1087).
  GetAssertionThreadPool: '`$anonymous_namespace_csrc/ops/assertion_aten_kernels.cc`/GetAssertionThreadPool(9eeca9d7cbd706f2).'
---
# Module: [`csrc/ops/assertion_aten_kernels.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc)

## Functions
- <a id="AtenAssertAsync"></a>`AtenAssertAsync(const at::Tensor& self)` — [`L179`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L179) — aten::_assert_async(Tensor self) -> ()
- <a id="AtenAssertAsyncMsg"></a>`AtenAssertAsyncMsg(const at::Tensor& self, std::string_view assert_msg)` — [`L184`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L184) — aten::_assert_async.msg(Tensor self, str assert_msg) -> ()
- <a id="GetAssertionThreadPool"></a>`GetAssertionThreadPool()` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L51) — Returns the background thread pool for evaluating asynchronous assertion
- <a id="ScheduleAsyncAssertionCheck"></a>`ScheduleAsyncAssertionCheck(const at::Tensor& self, const std::string_view assert_msg)` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L88) — Schedules an asynchronous assertion check for `self` on the background thread
- <a id="ShouldScheduleAsyncCheck"></a>`ShouldScheduleAsyncCheck(const at::Tensor& self)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L71) — Determines whether the assertion check should be scheduled asynchronously on
- <a id="ValidateAssertionInput"></a>`ValidateAssertionInput(const at::Tensor& self)` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/ops/assertion_aten_kernels.cc#L59) — Validates that the assertion condition tensor is a single-element scalar.

