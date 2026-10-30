---
title: 'Module: csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AtenSparseGatherAutograd#
symbols:
  AtenSparseGatherAutograd: ''
---
# Module: [`csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h)

## Classes
### <a id="AtenSparseGatherAutograd"></a>`AtenSparseGatherAutograd`  ·  implements/extends Function
- def: [`csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h:88`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_gather/sparse_gather_aten_kernels.h#L88)
- doc: @brief Autograd function for sparse gather.
- signature: `struct AtenSparseGatherAutograd : public torch::autograd::Function<AtenSparseGatherAutograd>`
- uses (calls/refs, reference-scoped): [`forward`](sparse_gather_aten_kernels.cc.md#AtenSparseGatherAutograd.forward), [`backward`](sparse_gather_aten_kernels.cc.md#AtenSparseGatherAutograd.backward)
- used by: [`AtenSparseGatherBackward`](sparse_gather_aten_kernels.cc.md#AtenSparseGatherBackward), [`TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12`](../../../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12), [`forward`](sparse_gather_aten_kernels.cc.md#AtenSparseGatherAutograd.forward)

