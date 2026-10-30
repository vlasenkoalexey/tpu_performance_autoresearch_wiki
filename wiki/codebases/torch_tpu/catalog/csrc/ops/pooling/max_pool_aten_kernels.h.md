---
title: 'Module: csrc/ops/pooling/max_pool_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/pooling/max_pool_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TpuMaxPool2dAutograd: TpuMaxPool2dAutograd#
  TpuMaxPool3dAutograd: TpuMaxPool3dAutograd#
  TpuMaxPool1dAutograd: TpuMaxPool1dAutograd#
---
# Module: [`csrc/ops/pooling/max_pool_aten_kernels.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.h)

## Classes
### <a id="TpuMaxPool1dAutograd"></a>`TpuMaxPool1dAutograd`  ·  implements/extends Function
- def: [`csrc/ops/pooling/max_pool_aten_kernels.h:56`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.h#L56)
- doc: Autograd function for MaxPool1D that routes to tpu::_max_pool1d during
- signature: `struct TpuMaxPool1dAutograd : public torch::autograd::Function<TpuMaxPool1dAutograd>`
- uses (calls/refs, reference-scoped): [`AtenMaxPool2dWithIndicesOut`](max_pool_aten_kernels.cc.md#AtenMaxPool2dWithIndicesOut), [`TpuMaxPool2d`](max_pool_aten_kernels.cc.md#TpuMaxPool2d), [`TpuMaxPool2dBackward`](max_pool_aten_kernels.cc.md#TpuMaxPool2dBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool1dAutograd.forward), [`backward`](max_pool_aten_kernels.cc.md#TpuMaxPool1dAutograd.backward), [`AtenMaxPool2d`](max_pool_aten_kernels.cc.md#AtenMaxPool2d)
- used by: [`TpuMaxPool1dBackward`](max_pool_aten_kernels.cc.md#TpuMaxPool1dBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool1dAutograd.forward), [`AtenMaxPool1d`](max_pool_aten_kernels.cc.md#AtenMaxPool1d)

### <a id="TpuMaxPool2dAutograd"></a>`TpuMaxPool2dAutograd`  ·  implements/extends Function
- def: [`csrc/ops/pooling/max_pool_aten_kernels.h:104`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.h#L104)
- doc: Autograd function for MaxPool2D that routes to tpu::_max_pool2d during
- signature: `struct TpuMaxPool2dAutograd : public torch::autograd::Function<TpuMaxPool2dAutograd>`
- uses (calls/refs, reference-scoped): [`AtenMaxPool2dWithIndicesBackwardGradInput`](max_pool_aten_kernels.cc.md#AtenMaxPool2dWithIndicesBackwardGradInput), [`TpuMaxPool3d`](max_pool_aten_kernels.cc.md#TpuMaxPool3d), [`TpuMaxPool3dBackward`](max_pool_aten_kernels.cc.md#TpuMaxPool3dBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool2dAutograd.forward), [`backward`](max_pool_aten_kernels.cc.md#TpuMaxPool2dAutograd.backward), [`AtenMaxPool3d`](max_pool_aten_kernels.cc.md#AtenMaxPool3d)
- used by: [`TpuMaxPool2dBackward`](max_pool_aten_kernels.cc.md#TpuMaxPool2dBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool2dAutograd.forward), [`AtenMaxPool2d`](max_pool_aten_kernels.cc.md#AtenMaxPool2d)

### <a id="TpuMaxPool3dAutograd"></a>`TpuMaxPool3dAutograd`  ·  implements/extends Function
- def: [`csrc/ops/pooling/max_pool_aten_kernels.h:152`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.h#L152)
- doc: Autograd function for MaxPool3D that routes to tpu::_max_pool3d during
- signature: `struct TpuMaxPool3dAutograd : public torch::autograd::Function<TpuMaxPool3dAutograd>`
- uses (calls/refs, reference-scoped): [`AtenMaxPool3dWithIndicesOut`](max_pool_aten_kernels.cc.md#AtenMaxPool3dWithIndicesOut), [`AtenMaxPool3dWithIndicesBackwardGradInput`](max_pool_aten_kernels.cc.md#AtenMaxPool3dWithIndicesBackwardGradInput), [`AtenMaxPool3dWithIndices`](max_pool_aten_kernels.cc.md#AtenMaxPool3dWithIndices), [`AtenMaxPool3dWithIndicesBackward`](max_pool_aten_kernels.cc.md#AtenMaxPool3dWithIndicesBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool3dAutograd.forward), [`backward`](max_pool_aten_kernels.cc.md#TpuMaxPool3dAutograd.backward)
- used by: [`TpuMaxPool3dBackward`](max_pool_aten_kernels.cc.md#TpuMaxPool3dBackward), [`forward`](max_pool_aten_kernels.cc.md#TpuMaxPool3dAutograd.forward), [`AtenMaxPool3d`](max_pool_aten_kernels.cc.md#AtenMaxPool3d)

