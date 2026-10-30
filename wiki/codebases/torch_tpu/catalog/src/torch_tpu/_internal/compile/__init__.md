---
title: 'Module: src/torch_tpu/_internal/compile/__init__.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/__init__.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile`/
symbols:
  _patch_flex_attention: _patch_flex_attention().
  _patch_flex_attention._flex_attention_tpu: _patch_flex_attention()._flex_attention_tpu().
  _patch_flex_attention._flex_attention_tpu.fold: _patch_flex_attention()._flex_attention_tpu().fold().
  _initialize_graphsafe_rng: _initialize_graphsafe_rng().
  _register_scan_operator: _register_scan_operator().
  _patch_flex_attention._validate_device: _patch_flex_attention()._validate_device().
  _patch_flex_attention._get_sdpa_attn_bias: _patch_flex_attention()._get_sdpa_attn_bias().
  _patch_flex_attention._sdpa_dense_backward: _patch_flex_attention()._sdpa_dense_backward().
  __all__: __all__.
---
# Module: [`src/torch_tpu/_internal/compile/__init__.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py)

## Functions
- <a id="_patch_flex_attention._flex_attention_tpu"></a>`_flex_attention_tpu(query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, score_mod=None, block_mask=None, scale=None, enable_gqa: bool = False, return_lse: bool = False, kernel_options=None, *, return_aux=None)` — [`L134`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L134)
- <a id="_patch_flex_attention._get_sdpa_attn_bias"></a>`_get_sdpa_attn_bias(block_mask: flex_attention.BlockMask, q_len: int, kv_len: int, dtype: torch.dtype, device: torch.device)` — [`L103`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L103)
- <a id="_initialize_graphsafe_rng"></a>`_initialize_graphsafe_rng()` — [`L32`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L32) — Initializes graphsafe RNG operations for TPU.
- <a id="_patch_flex_attention"></a>`_patch_flex_attention()` — [`L78`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L78) — Patches PyTorch flex_attention to support TPU tensors.
- <a id="_register_scan_operator"></a>`_register_scan_operator()` — [`L70`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L70) — Registers the custom scan operator implementation for TPU.
- <a id="_patch_flex_attention._sdpa_dense_backward"></a>`_sdpa_dense_backward(query, key, value, *args, **kwargs)` — [`L97`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L97)
- <a id="_patch_flex_attention._validate_device"></a>`_validate_device(query, key, value)` — [`L87`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L87)
- <a id="_patch_flex_attention._flex_attention_tpu.fold"></a>`fold(tensor: torch.Tensor)` — [`L189`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L189)

## Module values
- <a id="__all__"></a>`__all__` — [`L235`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/__init__.py#L235)

