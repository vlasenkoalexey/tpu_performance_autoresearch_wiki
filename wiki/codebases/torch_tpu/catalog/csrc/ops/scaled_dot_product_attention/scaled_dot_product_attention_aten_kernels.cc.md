---
title: 'Module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFusedSdpChoice: AtenFusedSdpChoice(c686682968e160f4).
  AtenScaledDotProductFusedAttentionOverrideable: AtenScaledDotProductFusedAttentionOverrideable(16b3a8622b172982).
  AtenScaledDotProductFusedAttentionOverrideableBackward: AtenScaledDotProductFusedAttentionOverrideableBackward(89f96bf84625936c).
  AtenScaledDotProductFlashAttention: AtenScaledDotProductFlashAttention(747d9cd4f0111ba1).
  AtenScaledDotProductFlashAttentionBackward: AtenScaledDotProductFlashAttentionBackward(a0dca4ffe99c20d2).
  HasDynamicShape: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/HasDynamicShape(b580d0b7e29ca914).'
  IsSupportedFlashAttentionShape: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/IsSupportedFlashAttentionShape(4732fbc890694935).'
  AbslHashValue: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/AbslHashValue(cbddb36d90552fdc).'
  GenerateResults: GenerateResults(5fbe740109df92ca).
  SdpaKernelKey: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/SdpaKernelKey#'
  SdpaKernelKey.dtype: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/SdpaKernelKey#dtype.'
  SdpaKernelKey.operator: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/SdpaKernelKey#`operator==`(19721f1ff3d3e390).'
  SdpaKernelKey.is_causal: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`/SdpaKernelKey#is_causal.'
---
# Module: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc)

## Classes
### <a id="SdpaKernelKey"></a>`SdpaKernelKey`
- def: [`csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L53)
- signature: `struct SdpaKernelKey`
- members:
  - <a id="SdpaKernelKey.operator"></a>`operator==(const SdpaKernelKey& other)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L62)
  - <a id="SdpaKernelKey.dtype"></a>`dtype` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L54)
  - <a id="SdpaKernelKey.is_causal"></a>`is_causal` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L55)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AbslHashValue`](scaled_dot_product_attention_aten_kernels.cc.md#AbslHashValue)

## Functions
- <a id="AbslHashValue"></a>`AbslHashValue(H h, const SdpaKernelKey& k)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L58)
- <a id="AtenFusedSdpChoice"></a>`AtenFusedSdpChoice(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_mask, double dropout_p, bool is_causal, std::optional<double> scale, bool enable_gqa)` — [`L123`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L123) — Torch's extensibility is pretty gross here due to weird SDPA — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="AtenScaledDotProductFlashAttention"></a>`AtenScaledDotProductFlashAttention(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_bias, bool compute_log_sumexp, double dropout_p, bool is_causal, bool return_debug_mask, std::optional<double> scale)` — [`L319`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L319) — This function implements the interface of scaled_dot_product_cudnn_attention — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="AtenScaledDotProductFlashAttentionBackward"></a>`AtenScaledDotProductFlashAttentionBackward(const at::Tensor& grad_out, const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const at::Tensor& out, const at::Tensor& logsumexp, const at::Tensor& philox_seed, const at::Tensor& philox_offset, const at::Tensor& attn_bias, const at::Tensor& cum_seq_q, const at::Tensor& cum_seq_k, at::SymInt max_q, at::SymInt max_k, double dropout_p, bool is_causal, std::optional<double> scale)` — [`L353`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L353) — This function implements the interface of — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="AtenScaledDotProductFusedAttentionOverrideable"></a>`AtenScaledDotProductFusedAttentionOverrideable(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_bias, double dropout_p, bool is_causal, bool return_debug_mask, std::optional<double> scale)` — [`L249`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L249) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="AtenScaledDotProductFusedAttentionOverrideableBackward"></a>`AtenScaledDotProductFusedAttentionOverrideableBackward(const at::Tensor& grad_out, const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const at::Tensor& attn_bias, std::array<bool, 4> grad_input_mask, const at::Tensor& out, const at::Tensor& logsumexp, const at::Tensor& cum_seq_q, const at::Tensor& cum_seq_k, at::SymInt max_q, at::SymInt max_k, double dropout_p, bool is_causal, const at::Tensor& philox_seed, const at::Tensor& philox_offset, std::optional<double> scale)` — [`L276`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L276) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="GenerateResults"></a>`GenerateResults(at::Tensor out, at::Tensor logsumexp, at::Tensor philox_seed = at::Tensor(), at::Tensor philox_offset = at::Tensor())` — [`L229`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L229)
- <a id="HasDynamicShape"></a>`HasDynamicShape(const at::Tensor& tensor)` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L67) — Returns true if `tensor` has symbolic sizes (torch.compile dynamic shapes) or
- <a id="IsSupportedFlashAttentionShape"></a>`IsSupportedFlashAttentionShape(const at::Tensor& query, const at::Tensor& key, const at::Tensor& value, const std::optional<at::Tensor>& attn_mask = std::nullopt)` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc#L79)

