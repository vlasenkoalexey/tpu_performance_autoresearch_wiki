---
title: 'Module: csrc/ops/isin/isin.h'
type: catalog
provenance: extracted
module: csrc/ops/isin/isin.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  IsInverted.kYes: IsInverted#kYes.
  IsInverted: IsInverted#
  IsUnique: IsUnique#
  IsUnique.kYes: IsUnique#kYes.
  IsInverted.kNo: IsInverted#kNo.
  IsUnique.kNo: IsUnique#kNo.
---
# Module: [`csrc/ops/isin/isin.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h)

## Classes
### <a id="IsInverted"></a>`IsInverted`
- def: [`csrc/ops/isin/isin.h:32`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L32)
- doc: Specifies whether matches should be inverted in the final predicate output.
- signature: `enum class IsInverted`
- members:
  - <a id="IsInverted.kNo"></a>`kNo` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L33)
  - <a id="IsInverted.kYes"></a>`kYes` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L34)
- uses (calls/refs, reference-scoped): [`BuildIsInShlo`](isin.cc.md#BuildIsInShlo), [`IsUnique`](isin.h.md#IsUnique)
- used by: [`AtenIsInHelper`](isin_aten_kernels.cc.md#AtenIsInHelper), [`BuildIsInShlo`](isin.cc.md#BuildIsInShlo), [`ToIsInverted`](isin_aten_kernels.cc.md#ToIsInverted), [`ToIsUnique`](isin_aten_kernels.cc.md#ToIsUnique)

### <a id="IsUnique"></a>`IsUnique`
- def: [`csrc/ops/isin/isin.h:26`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L26)
- doc: Specifies whether elements are assumed to be unique to optimize search.
- signature: `enum class IsUnique`
- members:
  - <a id="IsUnique.kNo"></a>`kNo` — [`L27`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L27)
  - <a id="IsUnique.kYes"></a>`kYes` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/isin/isin.h#L28)
- used by: [`AtenIsInHelper`](isin_aten_kernels.cc.md#AtenIsInHelper), [`BuildIsInShlo`](isin.cc.md#BuildIsInShlo), [`kYes`](isin.h.md#IsInverted.kYes), [`ToIsUnique`](isin_aten_kernels.cc.md#ToIsUnique)

