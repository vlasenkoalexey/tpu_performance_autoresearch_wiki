---
title: 'Module: src/vllm_torchtpu/layers/adapter/fused_moe.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/fused_moe.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.fused_moe`/
symbols:
  fused_moe_gmm: fused_moe_gmm().
  _build_fused_moe_custom_op: _build_fused_moe_custom_op().
  prebuild_fused_moe_kernel: prebuild_fused_moe_kernel().
  TpuMoEActivationMixin: TpuMoEActivationMixin#
  load_kmajor_fp4: load_kmajor_fp4().
  TpuMoEActivationMixin._tpu_activation_str: TpuMoEActivationMixin#_tpu_activation_str.
  TpuMoEActivationMixin._set_tpu_activation: TpuMoEActivationMixin#_set_tpu_activation().
  requant_load_kmajor_fp4: requant_load_kmajor_fp4().
  TpuMoEActivationMixin._resolve_tpu_activation: TpuMoEActivationMixin#_resolve_tpu_activation().
  _get_fused_moe_custom_op: _get_fused_moe_custom_op().
  quantize_native_fp4_kmajor: quantize_native_fp4_kmajor().
  get_fused_moe_activation: get_fused_moe_activation().
  _load_kmajor_fp4_op: _load_kmajor_fp4_op.
  _allocate_kernel_instance_id: _allocate_kernel_instance_id().
  _kernel_instance_counter: _kernel_instance_counter.
  _fused_moe_kernel_cache._fused_moe_kernel_cache: _fused_moe_kernel_cache._fused_moe_kernel_cache.
  _requant_kmajor_fp4_ops._requant_kmajor_fp4_ops: _requant_kmajor_fp4_ops._requant_kmajor_fp4_ops.
  _quantize_native_fp4_kmajor_ops._quantize_native_fp4_kmajor_ops: _quantize_native_fp4_kmajor_ops._quantize_native_fp4_kmajor_ops.
  _resolve_activation_name: _resolve_activation_name().
  _build_fused_moe_custom_op._fake_fused_moe: _build_fused_moe_custom_op()._fake_fused_moe().
---
# Module: [`src/vllm_torchtpu/layers/adapter/fused_moe.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py)

## Classes
### <a id="TpuMoEActivationMixin"></a>`TpuMoEActivationMixin`
- def: [`src/vllm_torchtpu/layers/adapter/fused_moe.py:58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L58)
- doc: Holds the Pallas GMM kernel's activation string for one MoE layer.
- signature: `class TpuMoEActivationMixin:`
- members:
  - <a id="TpuMoEActivationMixin._resolve_tpu_activation"></a>`_resolve_tpu_activation(self, layer)` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L70) — Encode this layer's activation for the kernel.
  - <a id="TpuMoEActivationMixin._set_tpu_activation"></a>`_set_tpu_activation(self, layer)` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L78) — Resolve and store; returns it, since callers also use it locally.
- protocol/private: <a id="TpuMoEActivationMixin._tpu_activation_str"></a>`_tpu_activation_str`[`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L68)
- uses (calls/refs, reference-scoped): [`VllmCompressedTensorsW4ANMxfp4MoEMethod`](quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod), [`get_fused_moe_activation`](fused_moe.md#get_fused_moe_activation), [`_resolve_tpu_activation`](quantization/mxfp4.md#VllmMxfp4MoEMethod._resolve_tpu_activation), [`_resolve_tpu_activation`](quantization/nvfp4.md#VllmNvfp4MoEMethod._resolve_tpu_activation)
- used by: [`_admit`](moe_tp_decode.md#_admit), [`process_weights_after_loading`](quantization/nvfp4.md#VllmNvfp4MoEMethod.process_weights_after_loading), [`process_weights_after_loading`](quantization/fp8.md#VllmFp8MoEMethodTPU.process_weights_after_loading), [`apply_monolithic`](quantization/fp8.md#VllmFp8MoEMethodTPU.apply_monolithic), [`process_weights_after_loading`](quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod.process_weights_after_loading), [`process_weights_after_loading`](quantization/mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod.process_weights_after_loading), [`apply_monolithic`](quantization/nvfp4.md#VllmNvfp4MoEMethod.apply_monolithic), [`process_weights_after_loading`](quantization/mxfp4.md#VllmMxfp4MoEMethod.process_weights_after_loading), [`_forward_monolithic_tpu`](quantization/mxfp4.md#VllmMxfp4MoEMethod._forward_monolithic_tpu), [`process_weights_after_loading`](quantization/unquantized.md#VllmUnquantizedFusedMoEMethod.process_weights_after_loading), [`VllmUnquantizedFusedMoEMethod`](quantization/unquantized.md#VllmUnquantizedFusedMoEMethod), [`_forward_monolithic_tpu`](quantization/unquantized.md#VllmUnquantizedFusedMoEMethod._forward_monolithic_tpu), [`apply_with_routing`](quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod.apply_with_routing), [`VllmFp8MoEMethodTPU`](quantization/fp8.md#VllmFp8MoEMethodTPU), [`_admit`](fused_moe_decode.md#_admit), [`VllmCompressedTensorsW4ANMxfp4MoEMethod`](quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod), [`VllmMxfp4MoEMethod`](quantization/mxfp4.md#VllmMxfp4MoEMethod), [`VllmNvfp4MoEMethod`](quantization/nvfp4.md#VllmNvfp4MoEMethod), [`_resolve_tpu_activation`](quantization/nvfp4.md#VllmNvfp4MoEMethod._resolve_tpu_activation)

## Functions
- <a id="_allocate_kernel_instance_id"></a>`_allocate_kernel_instance_id()` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L146)
- <a id="_build_fused_moe_custom_op"></a>`_build_fused_moe_custom_op(*, topk: int, activation: str, use_ep: bool, skip_padded_tokens: bool, rhs_quant_dtype=None)` — [`L153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L153)
- <a id="_build_fused_moe_custom_op._fake_fused_moe"></a>`_fake_fused_moe(hidden_states, *args, **kwargs)` — [`L190`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L190)
- <a id="_get_fused_moe_custom_op"></a>`_get_fused_moe_custom_op(*, topk: int, activation: str, use_ep: bool, rhs_quant_dtype=None, skip_padded_tokens: bool | None = None)` — [`L200`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L200)
- <a id="_resolve_activation_name"></a>`_resolve_activation_name(activation: Any)` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L40)
- <a id="fused_moe_gmm"></a>`fused_moe_gmm(hidden_states: torch.Tensor, w1: torch.Tensor, w2: torch.Tensor, w1_scale: torch.Tensor | None, w2_scale: torch.Tensor | None, w1_bias: torch.Tensor | None, w2_bias: torch.Tensor | None, topk_weights: torch.Tensor, topk_ids: torch.Tensor, experts_start: torch.Tensor | None, topk: int, activation: str, rhs_quant_dtype=None, skip_padded_tokens: bool | None = None)` — [`L241`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L241) — Fused MoE forward pass with precomputed routing. — documented in [quantization-methods](../../../../../concepts/quantization-methods.md)
- <a id="get_fused_moe_activation"></a>`get_fused_moe_activation(activation, moe_config)` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L46) — Encode vLLM's activation config for the Pallas GMM kernel.
- <a id="load_kmajor_fp4"></a>`load_kmajor_fp4(w_u8: torch.Tensor)` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L84) — One-time load transform: packed uint8 ``[..., N, K//2]`` -> native
- <a id="prebuild_fused_moe_kernel"></a>`prebuild_fused_moe_kernel(*, topk: int, activation: str, use_ep: bool, rhs_quant_dtype=None, skip_padded_tokens: bool | None = None)` — [`L223`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L223) — Prebuild and cache fused MoE custom op outside compile-time tracing.
- <a id="quantize_native_fp4_kmajor"></a>`quantize_native_fp4_kmajor(w: torch.Tensor, block: int, pack: bool = True)` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L123) — Quantize an already-dequantized, K-major float weight to native FP4.
- <a id="requant_load_kmajor_fp4"></a>`requant_load_kmajor_fp4(w_u8: torch.Tensor, scale_f: torch.Tensor, block: int)` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L103) — W4A8 requant + K-major load in one JAX op (matches tpu-inference). Takes

## Module values
- <a id="_fused_moe_kernel_cache._fused_moe_kernel_cache"></a>`_fused_moe_kernel_cache` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L34)
- <a id="_kernel_instance_counter"></a>`_kernel_instance_counter` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L33)
- <a id="_load_kmajor_fp4_op"></a>`_load_kmajor_fp4_op` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L35)
- <a id="_quantize_native_fp4_kmajor_ops._quantize_native_fp4_kmajor_ops"></a>`_quantize_native_fp4_kmajor_ops` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L37)
- <a id="_requant_kmajor_fp4_ops._requant_kmajor_fp4_ops"></a>`_requant_kmajor_fp4_ops` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/fused_moe.py#L36)

