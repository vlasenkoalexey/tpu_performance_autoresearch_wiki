---
title: 'Module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h
status: fresh
symbol_base: cxx . . $ torch_tpu/FusedAttentionResults#
symbols:
  FusedAttentionResults.logsumexp: logsumexp.
  FusedAttentionResults: ''
  FusedAttentionResults.output: output.
---
# Module: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h)

## Classes
### <a id="FusedAttentionResults"></a>`FusedAttentionResults`
- def: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h:30`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h#L30)
- signature: `struct FusedAttentionResults`
- members:
  - <a id="FusedAttentionResults.logsumexp"></a>`logsumexp` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h#L32) — UNINITIALIZED_TENSOR_OK
  - <a id="FusedAttentionResults.output"></a>`output` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.h#L31) — UNINITIALIZED_TENSOR_OK
- uses (calls/refs, reference-scoped): [`OpParamCacheKeys`](../../common/cache_key.h.md#OpParamCacheKeys), [`ScaledDotProductFusedAttentionShlo`](scaled_dot_product_attention_shlo.cc.md#ScaledDotProductFusedAttentionShlo), [`ScaledDotProductFusedAttentionShloBackward`](scaled_dot_product_attention_shlo.cc.md#ScaledDotProductFusedAttentionShloBackward)
- used by: [`BuildScaledDotProductAttentionBackward`](scaled_dot_product_attention_shlo.cc.md#BuildScaledDotProductAttentionBackward), [`ScaledDotProductFusedAttentionShlo`](scaled_dot_product_attention_shlo.cc.md#ScaledDotProductFusedAttentionShlo)

