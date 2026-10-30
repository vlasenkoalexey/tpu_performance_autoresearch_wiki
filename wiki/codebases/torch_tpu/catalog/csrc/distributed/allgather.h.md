---
title: 'Module: csrc/distributed/allgather.h'
type: catalog
provenance: extracted
module: csrc/distributed/allgather.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AllGatherOutputMode#
symbols:
  AllGatherOutputMode.kStack: kStack.
  AllGatherOutputMode: ''
  AllGatherOutputMode.kConcat: kConcat.
  AllGatherOutputMode.kList: kList.
---
# Module: [`csrc/distributed/allgather.h`](../../../../../../raw/code/torch_tpu/csrc/distributed/allgather.h)

## Classes
### <a id="AllGatherOutputMode"></a>`AllGatherOutputMode`
- def: [`csrc/distributed/allgather.h:29`](../../../../../../raw/code/torch_tpu/csrc/distributed/allgather.h#L29)
- signature: `enum class AllGatherOutputMode`
- members:
  - <a id="AllGatherOutputMode.kConcat"></a>`kConcat` — [`L31`](../../../../../../raw/code/torch_tpu/csrc/distributed/allgather.h#L31) — Output a single tensor concatenated along the gather dim.
  - <a id="AllGatherOutputMode.kList"></a>`kList` — [`L30`](../../../../../../raw/code/torch_tpu/csrc/distributed/allgather.h#L30) — Output a list of tensors.
  - <a id="AllGatherOutputMode.kStack"></a>`kStack` — [`L32`](../../../../../../raw/code/torch_tpu/csrc/distributed/allgather.h#L32) — Output a single tensor stacked along the new dim 0.
- uses (calls/refs, reference-scoped): [`DeviceGroupList`](types.h.md#DeviceGroupList), [`BuildDistributedAllGatherShlo`](allgather.cc.md#BuildDistributedAllGatherShlo), [`BuildDistributedAllGatherShlo`](allgather.cc.md#BuildDistributedAllGatherShlo)
- used by: [`allgather`](process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`_allgather_base`](process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AllGatherDim`](../ops/experimental/collectives/collectives_aten_kernels.cc.md#AllGatherDim), [`BuildDistributedAllGatherShlo`](allgather.cc.md#BuildDistributedAllGatherShlo)

