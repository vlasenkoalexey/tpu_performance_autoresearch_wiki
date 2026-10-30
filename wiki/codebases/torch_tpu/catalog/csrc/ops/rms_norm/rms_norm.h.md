---
title: 'Module: csrc/ops/rms_norm/rms_norm.h'
type: catalog
provenance: extracted
module: csrc/ops/rms_norm/rms_norm.h
status: fresh
symbol_base: cxx . . $ torch_tpu/RmsNormBackwardShloResults#
symbols:
  RmsNormBackwardShloResults.grad_weight: grad_weight.
  RmsNormBackwardShloResults: ''
  RmsNormBackwardShloResults.grad_input: grad_input.
---
# Module: [`csrc/ops/rms_norm/rms_norm.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.h)

## Classes
### <a id="RmsNormBackwardShloResults"></a>`RmsNormBackwardShloResults`
- def: [`csrc/ops/rms_norm/rms_norm.h:34`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.h#L34)
- signature: `struct RmsNormBackwardShloResults`
- members:
  - <a id="RmsNormBackwardShloResults.grad_input"></a>`grad_input` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.h#L35)
  - <a id="RmsNormBackwardShloResults.grad_weight"></a>`grad_weight` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm.h#L36)
- uses (calls/refs, reference-scoped): [`BuildRmsNormBackwardShlo`](rms_norm.cc.md#BuildRmsNormBackwardShlo)
- used by: [`AtenFusedRmsNormBackward`](rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`BuildRmsNormBackwardShlo`](rms_norm.cc.md#BuildRmsNormBackwardShlo), [`BuildRmsNormDx`](rms_norm.cc.md#BuildRmsNormDx)

