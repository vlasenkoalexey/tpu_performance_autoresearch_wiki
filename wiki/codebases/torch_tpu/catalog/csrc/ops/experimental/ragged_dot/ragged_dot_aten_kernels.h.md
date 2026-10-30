---
title: 'Module: csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AtenRaggedDotAutograd#
symbols:
  AtenRaggedDotAutograd: ''
---
# Module: [`csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h)

## Classes
### <a id="AtenRaggedDotAutograd"></a>`AtenRaggedDotAutograd`  ·  implements/extends Function
- def: [`csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h:96`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.h#L96)
- doc: Autograd function for ragged dot product.
- signature: `struct AtenRaggedDotAutograd : public torch::autograd::Function<AtenRaggedDotAutograd>`
- uses (calls/refs, reference-scoped): [`forward`](ragged_dot_aten_kernels.cc.md#AtenRaggedDotAutograd.forward), [`backward`](ragged_dot_aten_kernels.cc.md#AtenRaggedDotAutograd.backward)
- used by: [`AtenRaggedDotWeightGrad`](ragged_dot_aten_kernels.cc.md#AtenRaggedDotWeightGrad), [`TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12`](../../../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12), [`forward`](ragged_dot_aten_kernels.cc.md#AtenRaggedDotAutograd.forward)

