---
title: 'Module: csrc/ops/ctc_loss/ctc_loss_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/ctc_loss/ctc_loss_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCtcLossTensorAutograd: AtenCtcLossTensorAutograd#
  AtenCtcLossAutograd: AtenCtcLossAutograd#
---
# Module: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.h)

## Classes
### <a id="AtenCtcLossAutograd"></a>`AtenCtcLossAutograd`  ·  implements/extends Function
- def: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.h:41`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.h#L41)
- signature: `struct AtenCtcLossAutograd : public torch::autograd::Function<AtenCtcLossAutograd>`
- uses (calls/refs, reference-scoped): [`backward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossAutograd.backward), [`forward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossAutograd.forward)
- used by: [`AtenCtcLossTensor`](ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`forward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossAutograd.forward), [`AtenCtcLossPublicAutograd`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublicAutograd)

### <a id="AtenCtcLossTensorAutograd"></a>`AtenCtcLossTensorAutograd`  ·  implements/extends Function
- def: [`csrc/ops/ctc_loss/ctc_loss_aten_kernels.h:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/ctc_loss/ctc_loss_aten_kernels.h#L55)
- signature: `struct AtenCtcLossTensorAutograd : public torch::autograd::Function<AtenCtcLossTensorAutograd>`
- uses (calls/refs, reference-scoped): [`AtenCtcLossBackwardTensor`](ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`backward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossTensorAutograd.backward), [`forward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossTensorAutograd.forward), [`AtenCtcLossPublic`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublic), [`AtenCtcLossBackward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossBackward), [`AtenCtcLossPublicTensor`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublicTensor), [`AtenCtcLossPublicAutograd`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublicAutograd), [`AtenCtcLossPublicTensorAutograd`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublicTensorAutograd)
- used by: [`backward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossAutograd.backward), [`forward`](ctc_loss_aten_kernels.cc.md#AtenCtcLossTensorAutograd.forward), [`AtenCtcLossPublicTensorAutograd`](ctc_loss_aten_kernels.cc.md#AtenCtcLossPublicTensorAutograd)

