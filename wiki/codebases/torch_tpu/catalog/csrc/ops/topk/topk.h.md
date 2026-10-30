---
title: 'Module: csrc/ops/topk/topk.h'
type: catalog
provenance: extracted
module: csrc/ops/topk/topk.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TopKStableMode.kUnstable: TopKStableMode#kUnstable.
  TopKOutputs: TopKOutputs#
  TopKMode: TopKMode#
  TopKStableMode: TopKStableMode#
  TopKOutputs.values: TopKOutputs#values.
  TopKMode.kSmallest: TopKMode#kSmallest.
  TopKOutputs.indices: TopKOutputs#indices.
  TopKMode.kLargest: TopKMode#kLargest.
  TopKStableMode.kStable: TopKStableMode#kStable.
---
# Module: [`csrc/ops/topk/topk.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h)

## Classes
### <a id="TopKMode"></a>`TopKMode`
- def: [`csrc/ops/topk/topk.h:33`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L33)
- signature: `enum class TopKMode`
- members:
  - <a id="TopKMode.kLargest"></a>`kLargest` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L34)
  - <a id="TopKMode.kSmallest"></a>`kSmallest` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L35)
- used by: [`AtenTopKValues`](topk_aten_kernels.cc.md#AtenTopKValues), [`BuildMultinomialShlo`](../multinomial/multinomial.cc.md#BuildMultinomialShlo), [`BuildTopKShlo`](topk.cc.md#BuildTopKShlo), [`kUnstable`](topk.h.md#TopKStableMode.kUnstable)

### <a id="TopKOutputs"></a>`TopKOutputs`
- def: [`csrc/ops/topk/topk.h:28`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L28)
- signature: `struct TopKOutputs`
- members:
  - <a id="TopKOutputs.indices"></a>`indices` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L30)
  - <a id="TopKOutputs.values"></a>`values` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L29)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenTopKValues`](topk_aten_kernels.cc.md#AtenTopKValues), [`BuildMultinomialShlo`](../multinomial/multinomial.cc.md#BuildMultinomialShlo), [`BuildTopKShlo`](topk.cc.md#BuildTopKShlo), [`kUnstable`](topk.h.md#TopKStableMode.kUnstable)

### <a id="TopKStableMode"></a>`TopKStableMode`
- def: [`csrc/ops/topk/topk.h:38`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L38)
- signature: `enum class TopKStableMode`
- members:
  - <a id="TopKStableMode.kStable"></a>`kStable` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L39)
  - <a id="TopKStableMode.kUnstable"></a>`kUnstable` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/topk/topk.h#L40)
- uses (calls/refs, reference-scoped): [`BuildTopKShlo`](topk.cc.md#BuildTopKShlo), [`TopKOutputs`](topk.h.md#TopKOutputs), [`TopKMode`](topk.h.md#TopKMode)
- used by: [`BuildTopKShlo`](topk.cc.md#BuildTopKShlo)

