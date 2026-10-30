---
title: 'Module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AtenRaggedAllToAllAutograd#
symbols:
  AtenRaggedAllToAllAutograd: ''
---
# Module: [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h)

## Classes
### <a id="AtenRaggedAllToAllAutograd"></a>`AtenRaggedAllToAllAutograd`  ·  implements/extends Function
- def: [`csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h:58`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_all_to_all/ragged_all_to_all_aten_kernels.h#L58) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- doc: Autograd function for ragged all-to-all collective operation.
- signature: `struct AtenRaggedAllToAllAutograd : public torch::autograd::Function<AtenRaggedAllToAllAutograd>`
- uses (calls/refs, reference-scoped): [`forward`](ragged_all_to_all_aten_kernels.cc.md#AtenRaggedAllToAllAutograd.forward), [`backward`](ragged_all_to_all_aten_kernels.cc.md#AtenRaggedAllToAllAutograd.backward)
- used by: [`AtenRaggedAllToAllOut`](ragged_all_to_all_aten_kernels.cc.md#AtenRaggedAllToAllOut), [`TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12`](../../../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12), [`forward`](ragged_all_to_all_aten_kernels.cc.md#AtenRaggedAllToAllAutograd.forward)

