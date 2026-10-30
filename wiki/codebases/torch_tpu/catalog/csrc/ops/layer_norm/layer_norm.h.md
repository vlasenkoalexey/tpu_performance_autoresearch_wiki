---
title: 'Module: csrc/ops/layer_norm/layer_norm.h'
type: catalog
provenance: extracted
module: csrc/ops/layer_norm/layer_norm.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  LayerNormBackwardShloResults.grad_bias: LayerNormBackwardShloResults#grad_bias.
  LayerNormShloResults: LayerNormShloResults#
  LayerNormShloResults.normalized_values: LayerNormShloResults#normalized_values.
  LayerNormBackwardShloResults: LayerNormBackwardShloResults#
  LayerNormBackwardShloResults.grad_input: LayerNormBackwardShloResults#grad_input.
  LayerNormShloResults.mean: LayerNormShloResults#mean.
  LayerNormBackwardShloResults.grad_weight: LayerNormBackwardShloResults#grad_weight.
  LayerNormShloResults.reciprocal_std: LayerNormShloResults#reciprocal_std.
---
# Module: [`csrc/ops/layer_norm/layer_norm.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h)

## Classes
### <a id="LayerNormBackwardShloResults"></a>`LayerNormBackwardShloResults`
- def: [`csrc/ops/layer_norm/layer_norm.h:34`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L34)
- signature: `struct LayerNormBackwardShloResults`
- members:
  - <a id="LayerNormBackwardShloResults.grad_bias"></a>`grad_bias` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L37)
  - <a id="LayerNormBackwardShloResults.grad_input"></a>`grad_input` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L35)
  - <a id="LayerNormBackwardShloResults.grad_weight"></a>`grad_weight` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L36)
- uses (calls/refs, reference-scoped): [`BuildLayerNormShlo`](layer_norm.cc.md#BuildLayerNormShlo), [`BuildLayerNormBackwardShlo`](layer_norm.cc.md#BuildLayerNormBackwardShlo), [`LayerNormShloResults`](layer_norm.h.md#LayerNormShloResults)
- used by: [`AtenLayerNormBackward`](layer_norm_aten_kernels.cc.md#AtenLayerNormBackward), [`BuildLayerNormShlo`](layer_norm.cc.md#BuildLayerNormShlo), [`BuildLayerNormBackwardShlo`](layer_norm.cc.md#BuildLayerNormBackwardShlo)

### <a id="LayerNormShloResults"></a>`LayerNormShloResults`
- def: [`csrc/ops/layer_norm/layer_norm.h:28`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L28)
- signature: `struct LayerNormShloResults`
- members:
  - <a id="LayerNormShloResults.mean"></a>`mean` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L30)
  - <a id="LayerNormShloResults.normalized_values"></a>`normalized_values` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L29)
  - <a id="LayerNormShloResults.reciprocal_std"></a>`reciprocal_std` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm.h#L31)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenRmsNorm`](../rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`AtenFusedRmsNorm`](../rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenNativeLayerNorm`](layer_norm_aten_kernels.cc.md#AtenNativeLayerNorm), [`AtenTransformerEncoderLayerFwd`](../transformer_encoder_layer_fwd/_transformer_encoder_layer_fwd_aten_kernels.cc.md#AtenTransformerEncoderLayerFwd), [`BuildLayerNormShlo`](layer_norm.cc.md#BuildLayerNormShlo), [`BuildRmsNormShlo`](../rms_norm/rms_norm.cc.md#BuildRmsNormShlo), [`ComputeTwoMoments`](layer_norm.cc.md#ComputeTwoMoments), [`grad_bias`](layer_norm.h.md#LayerNormBackwardShloResults.grad_bias)

