---
title: 'Module: csrc/ops/masked_select/masked_select_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/masked_select/masked_select_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMaskedSelect: AtenMaskedSelect(91c7cc726c97ea99).
  AtenMaskedSelectOut: AtenMaskedSelectOut(dcc870e438d8791).
  PrepareOutTensor: '`$anonymous_namespace_csrc/ops/masked_select/masked_select_aten_kernels.cc`/PrepareOutTensor(27a803b2289b6b46).'
  ValidateMaskTensorIsBool: '`$anonymous_namespace_csrc/ops/masked_select/masked_select_aten_kernels.cc`/ValidateMaskTensorIsBool(fd0458bfc68bb174).'
  MaskedSelectFlat: '`$anonymous_namespace_csrc/ops/masked_select/masked_select_aten_kernels.cc`/MaskedSelectFlat(91c7cc726c97ea99).'
---
# Module: [`csrc/ops/masked_select/masked_select_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc)

## Functions
- <a id="AtenMaskedSelect"></a>`AtenMaskedSelect(const at::Tensor& self, const at::Tensor& mask)` — [`L98`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc#L98) — AtenMaskedSelect implements torch.masked_select by delegating to the nonzero
- <a id="AtenMaskedSelectOut"></a>`AtenMaskedSelectOut(const at::Tensor& self, const at::Tensor& mask, at::Tensor& out)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc#L112) — AtenMaskedSelectOut implements torch.masked_select.out by computing the
- <a id="MaskedSelectFlat"></a>`MaskedSelectFlat(const at::Tensor& self, const at::Tensor& mask)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc#L46) — MaskedSelectFlat implements masked_select by flattening the input tensors,
- <a id="PrepareOutTensor"></a>`PrepareOutTensor(const at::Tensor& result, at::Tensor& out)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc#L69) — PrepareOutTensor validates that the out tensor is on TPU, resizes it to match
- <a id="ValidateMaskTensorIsBool"></a>`ValidateMaskTensorIsBool(const at::Tensor& mask)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/masked_select/masked_select_aten_kernels.cc#L87) — ValidateMaskTensorIsBool verifies that the mask tensor has boolean scalar

