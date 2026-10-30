---
title: 'Module: csrc/ops/scaled_dot_product_attention/flash_attention_config.h'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/flash_attention_config.h
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  FlashAttnConfig: FlashAttnConfig#
  Tiling: Tiling#
  Tiling.kt: Tiling#kt.
  FlashAttnConfig.dropout_rate: FlashAttnConfig#dropout_rate.
  Tiling.qt: Tiling#qt.
  FlashAttnConfig.batch_size: FlashAttnConfig#batch_size.
  FlashAttnConfig.padded_q_sequence_length: FlashAttnConfig#padded_q_sequence_length.
  FlashAttnConfig.vo_head_dim: FlashAttnConfig#vo_head_dim.
  FlashAttnConfig.padded_kv_sequence_length: FlashAttnConfig#padded_kv_sequence_length.
  FlashAttnConfig.num_heads: FlashAttnConfig#num_heads.
  FlashAttnConfig.qk_head_dim: FlashAttnConfig#qk_head_dim.
  FlashAttnConfig.has_attn_bias: FlashAttnConfig#has_attn_bias.
  FlashAttnConfig.kv_num_heads: FlashAttnConfig#kv_num_heads.
  FlashAttnConfig.precision: FlashAttnConfig#precision.
  FlashAttnConfig.q_sequence_length: FlashAttnConfig#q_sequence_length.
  FlashAttnConfig.is_causal: FlashAttnConfig#is_causal.
  FlashAttnConfig.return_lse: FlashAttnConfig#return_lse.
  FlashAttnConfig.kv_sequence_length: FlashAttnConfig#kv_sequence_length.
  FlashAttnConfig.element_type: FlashAttnConfig#element_type.
  FlashAttnConfig.scale: FlashAttnConfig#scale.
  Tiling.kc: Tiling#kc.
  FlashAttnConfig.mask_broadcast_dims: FlashAttnConfig#mask_broadcast_dims.
  kLog2e: kLog2e.
  kDefaultKTileSize: kDefaultKTileSize.
  kDefaultQTileSize: kDefaultQTileSize.
---
# Module: [`csrc/ops/scaled_dot_product_attention/flash_attention_config.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h)

## Classes
### <a id="FlashAttnConfig"></a>`FlashAttnConfig`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_config.h:31`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L31) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- doc: Configuration for the flash attention kernel.
- signature: `struct FlashAttnConfig`
- members:
  - `batch_size` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L33)
  - <a id="FlashAttnConfig.batch_size"></a>`batch_size` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L33) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
  - `dropout_rate` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L49)
  - <a id="FlashAttnConfig.dropout_rate"></a>`dropout_rate` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L49) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
  - <a id="FlashAttnConfig.element_type"></a>`element_type` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L32)
  - `element_type` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L32)
  - `has_attn_bias` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L48)
  - <a id="FlashAttnConfig.has_attn_bias"></a>`has_attn_bias` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L48)
  - `is_causal` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L42)
  - <a id="FlashAttnConfig.is_causal"></a>`is_causal` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L42)
  - <a id="FlashAttnConfig.kv_num_heads"></a>`kv_num_heads` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L35)
  - `kv_num_heads` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L35)
  - <a id="FlashAttnConfig.kv_sequence_length"></a>`kv_sequence_length` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L39)
  - `kv_sequence_length` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L39)
  - <a id="FlashAttnConfig.mask_broadcast_dims"></a>`mask_broadcast_dims` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L45) — Broadcast dimensions of the mask.
  - `mask_broadcast_dims` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L45) — Broadcast dimensions of the mask.
  - <a id="FlashAttnConfig.num_heads"></a>`num_heads` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L34)
  - `num_heads` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L34)
  - `padded_kv_sequence_length` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L41)
  - <a id="FlashAttnConfig.padded_kv_sequence_length"></a>`padded_kv_sequence_length` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L41)
  - `padded_q_sequence_length` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L40)
  - <a id="FlashAttnConfig.padded_q_sequence_length"></a>`padded_q_sequence_length` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L40)
  - `precision` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L50)
  - <a id="FlashAttnConfig.precision"></a>`precision` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L50)
  - `q_sequence_length` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L38)
  - <a id="FlashAttnConfig.q_sequence_length"></a>`q_sequence_length` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L38)
  - <a id="FlashAttnConfig.qk_head_dim"></a>`qk_head_dim` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L36)
  - `qk_head_dim` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L36)
  - `return_lse` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L47) — Whether to return LSE (m and l) tensors.
  - <a id="FlashAttnConfig.return_lse"></a>`return_lse` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L47) — Whether to return LSE (m and l) tensors.
  - <a id="FlashAttnConfig.scale"></a>`scale` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L43)
  - `scale` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L43)
  - <a id="FlashAttnConfig.vo_head_dim"></a>`vo_head_dim` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L37)
  - `vo_head_dim` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L37)
- used by: [`CreateFlashAttentionBackwardKernel`](flash_attention_kernel_builder.cc.md#CreateFlashAttentionBackwardKernel), [`CreateFlashAttentionKernelImpl`](flash_attention_kernel_builder.cc.md#CreateFlashAttentionKernelImpl), [`buildModule`](flash_attention_kernel.cc.md#buildModule), [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`CreateFlashAttnConfig`](flash_attention_kernel_builder.cc.md#CreateFlashAttnConfig), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule), [`v_map`](util.h.md#KVWindowMaps.v_map), [`UpdateSoftmaxState`](flash_attention_kernel.cc.md#UpdateSoftmaxState), [`CreateKernel`](flash_attention_kernel.cc.md#CreateKernel), [`CreateBackwardDkvKernel`](flash_attention_backward_kernel.cc.md#CreateBackwardDkvKernel), [`CreateBackwardDqKernel`](flash_attention_backward_kernel.cc.md#CreateBackwardDqKernel), [`EmitGridStep`](flash_attention_kernel.cc.md#EmitGridStep), [`SetBackwardDkvKernelAttributes`](flash_attention_backward_kernel.cc.md#SetBackwardDkvKernelAttributes), [`LoadAndCastTiles`](flash_attention_backward_kernel.cc.md#LoadAndCastTiles), [`SetBackwardDqKernelAttributes`](flash_attention_backward_kernel.cc.md#SetBackwardDqKernelAttributes), [`StoreNormalizedOutput`](flash_attention_kernel.cc.md#StoreNormalizedOutput), [`SetKernelAttributes`](flash_attention_kernel.cc.md#SetKernelAttributes), [`ApplyDropoutToProbabilities`](flash_attention_kernel.cc.md#ApplyDropoutToProbabilities), [`ComputeSharedBackwardLogic`](flash_attention_backward_kernel.cc.md#ComputeSharedBackwardLogic), [`CreateKVWindowMaps`](util.cc.md#CreateKVWindowMaps), [`GetBwdArgIndices`](flash_attention_backward_kernel.cc.md#GetBwdArgIndices), [`BuildDropoutKeepMask`](util.cc.md#BuildDropoutKeepMask), [`SetScalarPrefetchAttr`](util.cc.md#SetScalarPrefetchAttr), [`PackPhiloxSeedAndOffsetTo4xI32`](flash_attention_kernel_builder.cc.md#PackPhiloxSeedAndOffsetTo4xI32), [`AppendScalarPrefetchTypes`](util.cc.md#AppendScalarPrefetchTypes)

### `Tiling`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_config.h:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L53)
- signature: `struct Tiling`
- members:
  - <a id="Tiling.kc"></a>`kc` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L61) — KV sub-block size the forward kernel computes on within a grid step. This
  - `kc` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L61) — KV sub-block size the forward kernel computes on within a grid step. This
  - `kt` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L56)
  - <a id="Tiling.kt"></a>`kt` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L56) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
  - `qt` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L55) — Q / KV block sizes that are DMA'd per grid step.
  - <a id="Tiling.qt"></a>`qt` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L55) — Q / KV block sizes that are DMA'd per grid step. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- used by: [`buildModule`](flash_attention_kernel.cc.md#buildModule), [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`CreateFlashAttnConfig`](flash_attention_kernel_builder.cc.md#CreateFlashAttnConfig), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule), [`UpdateSoftmaxState`](flash_attention_kernel.cc.md#UpdateSoftmaxState), [`CreateKernel`](flash_attention_kernel.cc.md#CreateKernel), [`CreateBackwardDkvKernel`](flash_attention_backward_kernel.cc.md#CreateBackwardDkvKernel), [`CreateBackwardDqKernel`](flash_attention_backward_kernel.cc.md#CreateBackwardDqKernel), [`EmitGridStep`](flash_attention_kernel.cc.md#EmitGridStep), [`SetBackwardDkvKernelAttributes`](flash_attention_backward_kernel.cc.md#SetBackwardDkvKernelAttributes), [`LoadAndCastTiles`](flash_attention_backward_kernel.cc.md#LoadAndCastTiles), [`SetBackwardDqKernelAttributes`](flash_attention_backward_kernel.cc.md#SetBackwardDqKernelAttributes), [`SetKernelAttributes`](flash_attention_kernel.cc.md#SetKernelAttributes), [`ApplyDropoutToProbabilities`](flash_attention_kernel.cc.md#ApplyDropoutToProbabilities), [`CreateKVWindowMaps`](util.cc.md#CreateKVWindowMaps)

## Module values
- <a id="kDefaultKTileSize"></a>`kDefaultKTileSize` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L65)
- `kDefaultKTileSize` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L65)
- <a id="kDefaultQTileSize"></a>`kDefaultQTileSize` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L64)
- `kDefaultQTileSize` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L64)
- `kLog2e` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L72) — The forward and backward kernels evaluate the softmax in the log2 domain:
- <a id="kLog2e"></a>`kLog2e` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_config.h#L72) — The forward and backward kernels evaluate the softmax in the log2 domain:

