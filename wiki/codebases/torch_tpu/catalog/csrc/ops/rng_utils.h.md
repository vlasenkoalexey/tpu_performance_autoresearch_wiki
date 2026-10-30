---
title: 'Module: csrc/ops/rng_utils.h'
type: catalog
provenance: extracted
module: csrc/ops/rng_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DispatchRngOpGeneral: DispatchRngOpGeneral(dca4cc2a97da0efa).
  DispatchRngOpAndReturnBuffer: DispatchRngOpAndReturnBuffer(4757735e21489d1f).
  DispatchRngOp: DispatchRngOp(a1ff451df0a2cb0e).
  DispatchRngOpOut: DispatchRngOpOut(eb2d610b6fe9a1fe).
  RngUsage: RngUsage#
  RngUsage.bit_width: RngUsage#bit_width.
  RngUsage.num_elements: RngUsage#num_elements.
---
# Module: [`csrc/ops/rng_utils.h`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h)

## Classes
### <a id="RngUsage"></a>`RngUsage`
- def: [`csrc/ops/rng_utils.h:40`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L40) — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- signature: `struct RngUsage`
- members:
  - <a id="RngUsage.bit_width"></a>`bit_width` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L42)
  - <a id="RngUsage.num_elements"></a>`num_elements` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L41)
- used by: [`AtenMultinomial`](multinomial/multinomial_aten_kernels.cc.md#AtenMultinomial), [`AtenMultinomialOut`](multinomial/multinomial_aten_kernels.cc.md#AtenMultinomialOut), [`AtenRandpermGeneratorOut`](randperm/randperm_aten_kernels.cc.md#AtenRandpermGeneratorOut), [`AtenLstmInputForward`](lstm/lstm_aten_kernels.cc.md#AtenLstmInputForward), [`AtenGruInputForwardCached`](gru/gru_aten_kernels.cc.md#AtenGruInputForwardCached), [`AtenLstmInputForwardCached`](lstm/lstm_aten_kernels.cc.md#AtenLstmInputForwardCached), [`AtenGruInputForward`](gru/gru_aten_kernels.cc.md#AtenGruInputForward), [`AtenDropoutCommonImpl`](dropout/dropout_aten_kernels.cc.md#AtenDropoutCommonImpl), [`ValidateInputs`](multinomial/multinomial_aten_kernels.cc.md#ValidateInputs), [`GetRngUsage`](multinomial/multinomial_aten_kernels.cc.md#GetRngUsage), [`DispatchRngOpGeneral`](rng_utils.h.md#DispatchRngOpGeneral), [`DispatchRngOpAndReturnBuffer`](rng_utils.h.md#DispatchRngOpAndReturnBuffer), [`DispatchRngOp`](rng_utils.h.md#DispatchRngOp), [`DispatchRngOpOut`](rng_utils.h.md#DispatchRngOpOut)

## Functions
- <a id="DispatchRngOp"></a>`DispatchRngOp(at::Tensor& result_tensor, c10::optional<at::Generator> generator, DispatchFunc dispatch_func, const std::optional<RngUsage>& usage = std::nullopt)` — [`L104`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L104) — Helper that wraps `DispatchRngOpAndReturnBuffer` and assigns the single — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="DispatchRngOpAndReturnBuffer"></a>`DispatchRngOpAndReturnBuffer(c10::optional<at::Generator> generator, DispatchFunc dispatch_func, const std::optional<RngUsage>& usage = std::nullopt)` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L89) — Helper that wraps `DispatchRngOpGeneral` and returns the single output buffer — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="DispatchRngOpGeneral"></a>`DispatchRngOpGeneral(c10::optional<at::Generator> generator, DispatchFunc dispatch_func, const std::optional<RngUsage>& usage = std::nullopt)` — [`L52`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L52) — Dispatches an RNG operation, handling locking, state retrieval, and — documented in [device-streams-generators-and-rng](../../../concepts/device-streams-generators-and-rng.md)
- <a id="DispatchRngOpOut"></a>`DispatchRngOpOut(at::Tensor& out, c10::optional<at::Generator> generator, mlir::ElementType out_dtype, DispatchFunc dispatch_func, const std::optional<RngUsage>& usage = std::nullopt)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/ops/rng_utils.h#L117) — Helper that executes an RNG op with out-tensor via `DispatchOpOut`, handling

