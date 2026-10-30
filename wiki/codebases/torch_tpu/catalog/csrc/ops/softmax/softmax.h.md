---
title: 'Module: csrc/ops/softmax/softmax.h'
type: catalog
provenance: extracted
module: csrc/ops/softmax/softmax.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SoftmaxMode: SoftmaxMode#
  EncodeParamCacheKey: EncodeParamCacheKey(346731dd550b6674).
  SoftmaxMode.kSoftmax: SoftmaxMode#kSoftmax.
  SoftmaxMode.kLogSoftmax: SoftmaxMode#kLogSoftmax.
---
# Module: [`csrc/ops/softmax/softmax.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.h)

## Classes
### <a id="SoftmaxMode"></a>`SoftmaxMode`
- def: [`csrc/ops/softmax/softmax.h:30`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.h#L30)
- signature: `enum class SoftmaxMode`
- members:
  - <a id="SoftmaxMode.kLogSoftmax"></a>`kLogSoftmax` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.h#L30)
  - <a id="SoftmaxMode.kSoftmax"></a>`kSoftmax` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.h#L30)
- used by: [`SoftmaxBackwardDataInternalOut`](softmax_aten_kernels.cc.md#SoftmaxBackwardDataInternalOut), [`AtenLogSoftmaxBackwardDataOut`](softmax_aten_kernels.cc.md#AtenLogSoftmaxBackwardDataOut), [`AtenLogSoftmaxOut`](softmax_aten_kernels.cc.md#AtenLogSoftmaxOut), [`AtenSoftmaxBackwardDataOut`](softmax_aten_kernels.cc.md#AtenSoftmaxBackwardDataOut), [`AtenSoftmaxOut`](softmax_aten_kernels.cc.md#AtenSoftmaxOut), [`BuildSoftmaxBackwardDataShlo`](softmax.cc.md#BuildSoftmaxBackwardDataShlo), [`SoftmaxInternalOut`](softmax_aten_kernels.cc.md#SoftmaxInternalOut), [`BuildSoftmaxShlo`](softmax.cc.md#BuildSoftmaxShlo), [`BuildMhaCore`](../native_multi_head_attention/native_multi_head_attention_aten_kernels.cc.md#BuildMhaCore), [`BuildCrossEntropyLossBackwardShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyLossBackwardShlo), [`BuildCrossEntropyLossBackwardTargetShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyLossBackwardTargetShlo), [`BuildCrossEntropyProbTargetBackwardShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyProbTargetBackwardShlo), [`BuildCrossEntropyLossShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyLossShlo), [`BuildMaskedSoftmaxShlo`](softmax.cc.md#BuildMaskedSoftmaxShlo), [`BuildMaskedSoftmaxBackwardDataShlo`](softmax.cc.md#BuildMaskedSoftmaxBackwardDataShlo), [`BuildMultiheadAttentionShlo`](../transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc.md#BuildMultiheadAttentionShlo), [`EncodeParamCacheKey`](softmax.h.md#EncodeParamCacheKey), [`GetSoftmaxBackwardDataFunctional`](softmax_aten_kernels.cc.md#GetSoftmaxBackwardDataFunctional), [`GetSoftmaxFunctional`](softmax_aten_kernels.cc.md#GetSoftmaxFunctional)

## Functions
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const SoftmaxMode softmax_mode)` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax.h#L33) — Encodes a SoftmaxMode enum as a parameter cache key string. — documented in [compilation-cache-key](../../../../concepts/compilation-cache-key.md)

