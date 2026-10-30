---
title: 'Module: csrc/internal/mosaic/kiln/core/index_map.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/index_map.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  IndexMap: IndexMap#
  IndexIndices: IndexIndices#
  IndexMap.IndexMap: IndexMap#IndexMap(4dedda5969c49de4).
  IndexMap.Invoke: IndexMap#Invoke(6f252a2777abb3dd).
  IndexMap.has_mapping: IndexMap#has_mapping(50ce9a9e25b4a850).
  IndexMap.IndexFn: IndexMap#IndexFn#
  IndexMap.mapping_: IndexMap#mapping_.
---
# Module: [`csrc/internal/mosaic/kiln/core/index_map.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h)

## Classes
### <a id="IndexIndices"></a>`IndexIndices`
- def: [`csrc/internal/mosaic/kiln/core/index_map.h:28`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L28)
- signature: `using IndexIndices = llvm::SmallVector<IndexArg, 4>`
- uses (calls/refs, reference-scoped): [`IndexArg`](index_arg.h.md#IndexArg)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`has_mapping`](index_map.h.md#IndexMap.has_mapping), [`IndexFn`](index_map.h.md#IndexMap.IndexFn)

### <a id="IndexMap"></a>`IndexMap`
- def: [`csrc/internal/mosaic/kiln/core/index_map.h:32`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L32)
- doc: Maps grid indices to block indices (Pallas `index_map`). Inside `IndexFn`,
- signature: `class IndexMap`
- members:
  - <a id="IndexMap.IndexMap"></a>`IndexMap(IndexFn fn)` — [`L37`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L37)
  - `IndexMap()` — [`L36`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L36)
  - <a id="IndexMap.Invoke"></a>`Invoke()` — [`L40`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L40)
  - <a id="IndexMap.has_mapping"></a>`has_mapping()` — [`L39`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L39)
  - <a id="IndexMap.mapping_"></a>`mapping_` — [`L43`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L43)
- uses (calls/refs, reference-scoped): [`IndexIndices`](index_map.h.md#IndexIndices), [`IndexFn`](index_map.h.md#IndexMap.IndexFn)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`dtype`](specs.h.md#BasicBlockSpec.dtype)

### <a id="IndexMap.IndexFn"></a>`IndexMap.IndexFn`
- def: [`csrc/internal/mosaic/kiln/core/index_map.h:34`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_map.h#L34)
- signature: `using IndexFn = std::function<IndexIndices()>`
- uses (calls/refs, reference-scoped): [`IndexIndices`](index_map.h.md#IndexIndices)
- used by: [`IndexMap`](index_map.h.md#IndexMap.IndexMap), [`Invoke`](index_map.h.md#IndexMap.Invoke)

