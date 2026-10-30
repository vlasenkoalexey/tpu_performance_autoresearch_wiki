---
title: 'Module: csrc/ops/index_utils.cc'
type: catalog
provenance: extracted
module: csrc/ops/index_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ResolveNegativeIndices: ResolveNegativeIndices(c219f49a61171495).
  ValidateIndexInputsAndGetDim: ValidateIndexInputsAndGetDim(77656466e213dbb6).
  ResolveAuxiliaryTensorDevice: '`$anonymous_namespace_csrc/ops/index_utils.cc`/ResolveAuxiliaryTensorDevice(cd958efedc17238).'
---
# Module: [`csrc/ops/index_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/index_utils.cc)

## Functions
- <a id="ResolveAuxiliaryTensorDevice"></a>`ResolveAuxiliaryTensorDevice(const at::Tensor& tensor)` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/ops/index_utils.cc#L54) — PyTorch's dispatcher bypasses backend device guards for index tensors
- `ResolveNegativeIndices(std::vector<at::Tensor>& indices, const at::IntArrayRef sizes, const Indices& dimensions)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/ops/index_utils.cc#L67) — Resolves negative indices by converting them to positive indices
- <a id="ResolveNegativeIndices"></a>`ResolveNegativeIndices(std::vector<at::Tensor>& indices, const at::IntArrayRef sizes, const Indices& dimensions)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/ops/index_utils.cc#L67) — Resolves negative indices by converting them to positive indices
- <a id="ValidateIndexInputsAndGetDim"></a>`ValidateIndexInputsAndGetDim(const at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& source)` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/ops/index_utils.cc#L173)

