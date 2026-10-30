---
title: 'Module: csrc/ops/precision_context.cc'
type: catalog
provenance: extracted
module: csrc/ops/precision_context.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetAndAddPrecisionTo: GetAndAddPrecisionTo(164574e34b85f590).
  PyUnsafeGetPrecision: PyUnsafeGetPrecision(b126dc7c1de90089).
  PyPopPrecision: PyPopPrecision(49f6e7a06ebc5aa8).
  PySetGlobalPrecision: PySetGlobalPrecision(7c8085fd1b1967ed).
  PyPushPrecision: PyPushPrecision(d4f767463ce0a6b3).
  PyGetGlobalPrecision: PyGetGlobalPrecision(e8d8a2ba6eeefc7a).
  g_global_precision: g_global_precision.
---
# Module: [`csrc/ops/precision_context.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc)

## Functions
- `GetAndAddPrecisionTo(OpParamCacheKeys& param_keys, const std::string_view param_name)` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L76) — Returns the current python thread's precision and adds it to the param_keys
- <a id="GetAndAddPrecisionTo"></a>`GetAndAddPrecisionTo(OpParamCacheKeys& param_keys, const std::string_view param_name)` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L76) — Returns the current python thread's precision and adds it to the param_keys — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- `PyGetGlobalPrecision()` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L41) — Returns the current global float32 matmul precision.
- <a id="PyGetGlobalPrecision"></a>`PyGetGlobalPrecision()` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L41) — Returns the current global float32 matmul precision. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- <a id="PyPopPrecision"></a>`PyPopPrecision()` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L49) — Pops the current precision context state from the stack. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- `PyPushPrecision(mlir::stablehlo::Precision precision)` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L45) — Pushes the given precision context state onto the stack.
- <a id="PyPushPrecision"></a>`PyPushPrecision(mlir::stablehlo::Precision precision)` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L45) — Pushes the given precision context state onto the stack. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- `PySetGlobalPrecision(mlir::stablehlo::Precision precision)` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L37) — Sets the global float32 matmul precision.
- <a id="PySetGlobalPrecision"></a>`PySetGlobalPrecision(mlir::stablehlo::Precision precision)` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L37) — Sets the global float32 matmul precision. — documented in [dtype-and-precision](../../../concepts/dtype-and-precision.md)
- <a id="PyUnsafeGetPrecision"></a>`PyUnsafeGetPrecision()` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L53) — Returns the current python thread's precision. It's unsafe in the sense that
- `PyUnsafeGetPrecision()` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L53) — Returns the current python thread's precision. It's unsafe in the sense that

## Module values
- <a id="g_global_precision"></a>`g_global_precision` — [`L34`](../../../../../../raw/code/torch_tpu/csrc/ops/precision_context.cc#L34)

