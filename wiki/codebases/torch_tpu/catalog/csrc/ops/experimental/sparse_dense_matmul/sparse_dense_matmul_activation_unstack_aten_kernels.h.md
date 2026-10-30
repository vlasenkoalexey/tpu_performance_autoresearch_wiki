---
title: 'Module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AtenSparseDenseMatmulActivationUnstackAutograd#
symbols:
  AtenSparseDenseMatmulActivationUnstackAutograd: ''
---
# Module: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h)

## Classes
### <a id="AtenSparseDenseMatmulActivationUnstackAutograd"></a>`AtenSparseDenseMatmulActivationUnstackAutograd`  ·  implements/extends Function
- def: [`csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h:71`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/sparse_dense_matmul/sparse_dense_matmul_activation_unstack_aten_kernels.h#L71)
- doc: @brief Autograd function for sparse dense matmul activation unstack.
- signature: `struct AtenSparseDenseMatmulActivationUnstackAutograd : public torch::autograd::Function< AtenSparseDenseMatmulActivationUnstackAutograd>`
- uses (calls/refs, reference-scoped): [`forward`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstackAutograd.forward), [`backward`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstackAutograd.backward), [`backward`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstackAutograd.backward), [`forward`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstackAutograd.forward)
- used by: [`AtenSparseDenseMatmulActivationUnstack`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstack), [`TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12`](../../../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_init_tpu_AutogradPrivateUse1_12), [`forward`](sparse_dense_matmul_activation_unstack_aten_kernels.cc.md#AtenSparseDenseMatmulActivationUnstackAutograd.forward)

