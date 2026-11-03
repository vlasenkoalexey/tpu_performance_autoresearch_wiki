---
title: 'Module: src/vllm_torchtpu/gqa_head_padding.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/gqa_head_padding.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.gqa_head_padding`/
symbols:
  pad_qkv_weight: pad_qkv_weight().
  _pad_q_heads: _pad_q_heads().
  pad_gqa_tensor_along_dim: pad_gqa_tensor_along_dim().
  GqaPaddingSpec.head_dim: GqaPaddingSpec#head_dim.
  install_qkv_padded_loader: install_qkv_padded_loader().
  install_o_proj_padded_loader: install_o_proj_padded_loader().
  GqaPaddingSpec.orig_total_heads: GqaPaddingSpec#orig_total_heads().
  GqaPaddingSpec: GqaPaddingSpec#
  compute_padded_gqa_heads: compute_padded_gqa_heads().
  GqaPaddingSpec.padded_total_heads: GqaPaddingSpec#padded_total_heads().
  update_gqa_head_padding_config: update_gqa_head_padding_config().
  GqaPaddingSpec.num_kv_heads: GqaPaddingSpec#num_kv_heads.
  pad_o_proj_weight: pad_o_proj_weight().
  GqaPaddingSpec.orig_q_per_kv: GqaPaddingSpec#orig_q_per_kv.
  logger: logger.
  install_qkv_padded_loader._make_loader: install_qkv_padded_loader()._make_loader().
  install_qkv_padded_loader._make_loader._padded_loader: install_qkv_padded_loader()._make_loader()._padded_loader().
  install_o_proj_padded_loader._make_loader: install_o_proj_padded_loader()._make_loader().
  install_o_proj_padded_loader._make_loader._padded_loader: install_o_proj_padded_loader()._make_loader()._padded_loader().
  GqaPaddingSpec.padded_q_per_kv: GqaPaddingSpec#padded_q_per_kv.
  _spans_heads: _spans_heads().
  _unsupported_shape_error: _unsupported_shape_error().
  _wrap_layer_weight_loaders: _wrap_layer_weight_loaders().
---
# Module: [`src/vllm_torchtpu/gqa_head_padding.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py)

## Classes
### <a id="GqaPaddingSpec"></a>`GqaPaddingSpec`
- def: [`src/vllm_torchtpu/gqa_head_padding.py:36`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L36) — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- doc: Specification for per-KV-group query head zero-padding.
- signature: `class GqaPaddingSpec:`
- members:
  - <a id="GqaPaddingSpec.orig_total_heads"></a>`orig_total_heads(self)` — [`L45`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L45)
  - <a id="GqaPaddingSpec.padded_total_heads"></a>`padded_total_heads(self)` — [`L49`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L49)
  - <a id="GqaPaddingSpec.head_dim"></a>`head_dim` — [`L42`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L42)
  - <a id="GqaPaddingSpec.num_kv_heads"></a>`num_kv_heads` — [`L39`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L39)
  - <a id="GqaPaddingSpec.orig_q_per_kv"></a>`orig_q_per_kv` — [`L40`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L40)
  - <a id="GqaPaddingSpec.padded_q_per_kv"></a>`padded_q_per_kv` — [`L41`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L41)
- used by: [`__init__`](models/vllm/qwen2.md#TPUTPPaddedQwen2Attention.__init__), [`pad_qkv_weight`](gqa_head_padding.md#pad_qkv_weight), [`_pad_q_heads`](gqa_head_padding.md#_pad_q_heads), [`pad_gqa_tensor_along_dim`](gqa_head_padding.md#pad_gqa_tensor_along_dim), [`install_o_proj_padded_loader`](gqa_head_padding.md#install_o_proj_padded_loader), [`install_qkv_padded_loader`](gqa_head_padding.md#install_qkv_padded_loader), [`pad_o_proj_weight`](gqa_head_padding.md#pad_o_proj_weight)

## Functions
- <a id="install_qkv_padded_loader._make_loader"></a>`_make_loader(orig_fn: Callable[..., Any])` — [`L243`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L243)
- <a id="install_o_proj_padded_loader._make_loader"></a>`_make_loader(orig_fn: Callable[..., Any])` — [`L260`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L260)
- <a id="_pad_q_heads"></a>`_pad_q_heads(tensor: torch.Tensor, dim: int, spec: GqaPaddingSpec, name: str)` — [`L150`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L150) — Pads unpadded Q-head tensors; passes already-padded ones through.
- <a id="install_qkv_padded_loader._make_loader._padded_loader"></a>`_padded_loader(param: Any, loaded_weight: torch.Tensor, loaded_shard_id: str | None = None)` — [`L244`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L244)
- <a id="install_o_proj_padded_loader._make_loader._padded_loader"></a>`_padded_loader(param: Any, loaded_weight: torch.Tensor)` — [`L261`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L261)
- <a id="_spans_heads"></a>`_spans_heads(tensor: torch.Tensor, dim: int, num_heads: int, head_dim: int)` — [`L123`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L123) — Whether ``tensor`` has exactly ``num_heads * head_dim`` entries along ``dim``.
- <a id="_unsupported_shape_error"></a>`_unsupported_shape_error(name: str, tensor: torch.Tensor, dim: int, expected_heads: str, head_dim: int)` — [`L128`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L128)
- <a id="_wrap_layer_weight_loaders"></a>`_wrap_layer_weight_loaders(layer: Any, make_wrapped_loader: Callable[[Callable[..., Any]], Callable[..., Any]])` — [`L213`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L213) — Wraps ``weight_loader`` and ``weight_loader_v2`` on ``layer`` and params.
- <a id="compute_padded_gqa_heads"></a>`compute_padded_gqa_heads(total_num_heads: int, total_num_kv_heads: int, tp_size: int)` — [`L53`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L53) — Computes per-KV-group padded Q head counts when heads % tp_size != 0. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="install_o_proj_padded_loader"></a>`install_o_proj_padded_loader(layer: Any, spec: GqaPaddingSpec)` — [`L257`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L257) — Installs Q-head zero-padding weight loaders on ``RowParallelLinear``. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="install_qkv_padded_loader"></a>`install_qkv_padded_loader(layer: Any, spec: GqaPaddingSpec)` — [`L240`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L240) — Installs Q-head zero-padding weight loaders on ``QKVParallelLinear``. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="pad_gqa_tensor_along_dim"></a>`pad_gqa_tensor_along_dim(tensor: torch.Tensor, dim: int, spec: GqaPaddingSpec)` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L138) — Zero-pads a Q or O projection tensor per KV head group along ``dim``.
- <a id="pad_o_proj_weight"></a>`pad_o_proj_weight(param: Any, loaded_weight: torch.Tensor, spec: GqaPaddingSpec)` — [`L203`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L203) — Pads ``o_proj`` weights along ``input_dim`` when defined on ``param``.
- <a id="pad_qkv_weight"></a>`pad_qkv_weight(param: Any, loaded_weight: torch.Tensor, loaded_shard_id: str | None, spec: GqaPaddingSpec)` — [`L169`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L169) — Pads Q weights in sharded ('q') or fused (``loaded_shard_id=None``) form.
- <a id="update_gqa_head_padding_config"></a>`update_gqa_head_padding_config(model_config: Any, parallel_config: Any)` — [`L84`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L84) — Updates ``model_config.model_arch_config`` with the padded GQA head count.

## Module values
- <a id="logger"></a>`logger` — [`L32`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/gqa_head_padding.py#L32)

