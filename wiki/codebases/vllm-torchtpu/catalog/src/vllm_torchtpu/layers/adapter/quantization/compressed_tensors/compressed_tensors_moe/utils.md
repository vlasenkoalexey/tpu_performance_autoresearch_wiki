---
title: 'Module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.quantization.compressed_tensors.compressed_tensors_moe.utils`/
symbols:
  requantize_int4_to_fp4_weights: requantize_int4_to_fp4_weights().
  get_cpu_weight_loader_hook: get_cpu_weight_loader_hook().
  get_cpu_weight_loader_hook._cpu_weight_loader_hook: get_cpu_weight_loader_hook()._cpu_weight_loader_hook().
  release_memory_to_os: release_memory_to_os().
  requantize_int4_weights: requantize_int4_weights().
  requantize_and_transpose_int4_weights: requantize_and_transpose_int4_weights().
  requantize_and_transpose_int4_to_fp4_weights: requantize_and_transpose_int4_to_fp4_weights().
  StagedParameter: StagedParameter#
  StagedParameter._cpu_scratch: StagedParameter#_cpu_scratch.
  StagedParameter._orig_shape: StagedParameter#_orig_shape.
  quantize_to_fp4_e2m1_nibbles: quantize_to_fp4_e2m1_nibbles().
---
# Module: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py)

## Classes
### <a id="StagedParameter"></a>`StagedParameter`
- def: [`src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py:25`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L25)
- doc: Typing-only view of a parameter staged by the CPU weight loader.
- signature: `class StagedParameter(Parameter):`
- protocol/private: <a id="StagedParameter._cpu_scratch"></a>`_cpu_scratch`[`L28`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L28), <a id="StagedParameter._orig_shape"></a>`_orig_shape`[`L29`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L29)
- used by: [`create_weights`](compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod.create_weights), [`_cpu_weight_loader_hook`](utils.md#get_cpu_weight_loader_hook._cpu_weight_loader_hook)

## Functions
- <a id="get_cpu_weight_loader_hook._cpu_weight_loader_hook"></a>`_cpu_weight_loader_hook(param: StagedParameter, loaded_weight: torch.Tensor, weight_name: str, shard_id: str, expert_id: int, *args: Any, **kwargs: Any)` — [`L47`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L47)
- <a id="get_cpu_weight_loader_hook"></a>`get_cpu_weight_loader_hook(layer: RoutedExperts, orig_loader: Callable | None, tp_size: int, tp_rank: int, is_param_transposed: bool = True)` — [`L32`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L32) — Returns a custom weight loader hook for TPU to intercept specific Compressed Tensors
- <a id="quantize_to_fp4_e2m1_nibbles"></a>`quantize_to_fp4_e2m1_nibbles(tensor_scaled: torch.Tensor)` — [`L167`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L167) — Vectorized projection of scaled float values into 4-bit FP4 E2M1
- <a id="release_memory_to_os"></a>`release_memory_to_os()` — [`L157`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L157) — Forces Python GC and instructs the C allocator to return free memory
- <a id="requantize_and_transpose_int4_to_fp4_weights"></a>`requantize_and_transpose_int4_to_fp4_weights(w_packed: torch.Tensor, scale_f: torch.Tensor, requant_block_size: int, in_group_size: int)` — [`L341`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L341) — Requantizes INT4 weights to FP4 (torch.float8_e4m3fn carrier) and returns
- <a id="requantize_and_transpose_int4_weights"></a>`requantize_and_transpose_int4_weights(w_packed: torch.Tensor, scale_f: torch.Tensor, requant_block_size: int, sign_xor_val: int, in_group_size: int)` — [`L323`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L323) — Requantizes INT4 weights and returns transposed & XORed tensors matching
- <a id="requantize_int4_to_fp4_weights"></a>`requantize_int4_to_fp4_weights(w_packed: torch.Tensor, scale_f: torch.Tensor, requant_block_size: int, in_group_size: int)` — [`L247`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L247) — Requantizes INT4 weights [..., N, K/8] to FP4 (E2M1) packed into
- <a id="requantize_int4_weights"></a>`requantize_int4_weights(w_packed: torch.Tensor, scale_f: torch.Tensor, requant_block_size: int, in_group_size: int)` — [`L185`](../../../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/utils.py#L185) — INT4 MoE block-wise requantization on device:

