---
title: 'Module: csrc/mlir/instrumentation.h'
type: catalog
provenance: extracted
module: csrc/mlir/instrumentation.h
status: fresh
symbol_base: cxx . . $ torch_tpu/InstrumentationState#
symbols:
  InstrumentationState.dump_to_print: dump_to_print.
  InstrumentationState: ''
  InstrumentationState.ir_os: ir_os.
  InstrumentationState.timing_os: timing_os.
---
# Module: [`csrc/mlir/instrumentation.h`](../../../../../../raw/code/torch_tpu/csrc/mlir/instrumentation.h)

## Classes
### <a id="InstrumentationState"></a>`InstrumentationState`
- def: [`csrc/mlir/instrumentation.h:30`](../../../../../../raw/code/torch_tpu/csrc/mlir/instrumentation.h#L30) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- signature: `struct InstrumentationState`
- members:
  - <a id="InstrumentationState.dump_to_print"></a>`dump_to_print` — [`L33`](../../../../../../raw/code/torch_tpu/csrc/mlir/instrumentation.h#L33) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
  - <a id="InstrumentationState.ir_os"></a>`ir_os` — [`L31`](../../../../../../raw/code/torch_tpu/csrc/mlir/instrumentation.h#L31) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
  - <a id="InstrumentationState.timing_os"></a>`timing_os` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/mlir/instrumentation.h#L32) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- uses (calls/refs, reference-scoped): [`Apply`](instrumentation.cc.md#InstrumentationState.Apply), [`ConfigureInstrumentation`](instrumentation.cc.md#ConfigureInstrumentation)
- used by: [`ConfigureInstrumentation`](instrumentation.cc.md#ConfigureInstrumentation), [`Apply`](instrumentation.cc.md#InstrumentationState.Apply), [`NextModuleId`](instrumentation.cc.md#NextModuleId)

