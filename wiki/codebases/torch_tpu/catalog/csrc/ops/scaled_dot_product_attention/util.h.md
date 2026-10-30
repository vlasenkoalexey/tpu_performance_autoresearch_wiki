---
title: 'Module: csrc/ops/scaled_dot_product_attention/util.h'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/util.h
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/KVWindowMaps#
symbols:
  KVWindowMaps.v_map: v_map.
  KVWindowMaps: ''
  KVWindowMaps.k_map: k_map.
---
# Module: [`csrc/ops/scaled_dot_product_attention/util.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.h)

## Classes
### <a id="KVWindowMaps"></a>`KVWindowMaps`
- def: [`csrc/ops/scaled_dot_product_attention/util.h:41`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.h#L41)
- signature: `struct KVWindowMaps`
- members:
  - <a id="KVWindowMaps.k_map"></a>`k_map` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.h#L42)
  - <a id="KVWindowMaps.v_map"></a>`v_map` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/util.h#L43) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- uses (calls/refs, reference-scoped): [`ScaleValue`](util.cc.md#ScaleValue), [`CreateKVWindowMaps`](util.cc.md#CreateKVWindowMaps), [`StoreTile`](util.cc.md#StoreTile), [`ConvertElementType`](util.cc.md#ConvertElementType), [`StoreTileSlice`](util.cc.md#StoreTileSlice), [`LoadTile`](util.cc.md#LoadTile), [`FlashAttnConfig`](flash_attention_config.h.md#FlashAttnConfig), [`BuildDropoutKeepMask`](util.cc.md#BuildDropoutKeepMask), [`SplatConstant`](util.cc.md#SplatConstant), [`NormalizeLaneDim`](util.cc.md#NormalizeLaneDim), [`Tiling`](flash_attention_config.h.md#Tiling), [`SplatNegInf`](util.cc.md#SplatNegInf), [`CreateSymbolTransformIndicesAttr`](util.cc.md#CreateSymbolTransformIndicesAttr), [`GetOpString`](util.cc.md#GetOpString), [`AppendScalarPrefetchTypes`](util.cc.md#AppendScalarPrefetchTypes), [`ApplyStructuredMask`](util.cc.md#ApplyStructuredMask), [`LoadTileSlice`](util.cc.md#LoadTileSlice), [`ZeroTile`](util.cc.md#ZeroTile), [`SetScalarPrefetchAttr`](util.cc.md#SetScalarPrefetchAttr), [`NInfTile`](util.cc.md#NInfTile), [`CreateBelowOrOnDiagCondition`](util.cc.md#CreateBelowOrOnDiagCondition), [`SplatConstant`](util.cc.md#SplatConstant), [`CreateCausalIfOp`](util.cc.md#CreateCausalIfOp), [`ClampMinFinite`](util.cc.md#ClampMinFinite), [`CreateIntersectsDiagCondition`](util.cc.md#CreateIntersectsDiagCondition), [`NeedsPadMask`](util.cc.md#NeedsPadMask), [`AppendScalarPrefetchTypes`](util.cc.md#AppendScalarPrefetchTypes), [`ReduceBroadcastLane`](util.cc.md#ReduceBroadcastLane), [`CreateLog2`](util.cc.md#CreateLog2), [`CreateKVWindowMaps`](util.cc.md#CreateKVWindowMaps), [`LoadTileSlice`](util.cc.md#LoadTileSlice), [`ReduceBroadcastLane`](util.cc.md#ReduceBroadcastLane), [`CreateCausalIfOp`](util.cc.md#CreateCausalIfOp), [`LoadTile`](util.cc.md#LoadTile), [`SplatConstant`](util.cc.md#SplatConstant), [`BuildDropoutKeepMask`](util.cc.md#BuildDropoutKeepMask), [`SetScalarPrefetchAttr`](util.cc.md#SetScalarPrefetchAttr)
- used by: [`SetScalarPrefetchAttr`](util.cc.md#SetScalarPrefetchAttr)

