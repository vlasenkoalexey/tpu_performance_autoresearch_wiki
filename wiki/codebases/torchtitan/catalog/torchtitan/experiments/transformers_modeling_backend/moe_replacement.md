---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/moe_replacement.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/moe_replacement.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.moe_replacement`/
symbols:
  _build_moe_config: _build_moe_config().
  build_and_swap_native_moe: build_and_swap_native_moe().
  _probe_hf_moe_block: _probe_hf_moe_block().
  _get_expert_param_info: _get_expert_param_info().
  prepare_native_moe_configs: prepare_native_moe_configs().
  _probe_layer_level_moe: _probe_layer_level_moe().
  _expert_param_info_cache._expert_param_info_cache: _expert_param_info_cache._expert_param_info_cache.
  _LINEAR_INIT: _LINEAR_INIT.
  _HFBatchedMoE: _HFBatchedMoE#
  _get_moe_block: _get_moe_block().
  _HFBatchedMoE.forward: _HFBatchedMoE#forward().
  _get_moe_attr_name: _get_moe_attr_name().
  _resolve_num_experts: _resolve_num_experts().
  _resolve_top_k: _resolve_top_k().
  _resolve_score_func: _resolve_score_func().
  _probe_shared_experts: _probe_shared_experts().
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/moe_replacement.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py)

## Classes
### <a id="_HFBatchedMoE"></a>`_HFBatchedMoE`  ·  implements/extends MoE
- def: [`torchtitan/experiments/transformers_modeling_backend/moe_replacement.py:50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L50)
- doc: Adapt HF's singleton batch to Titan MoE's flat token interface.
- signature: `class _HFBatchedMoE(MoE):`
- members:
  - <a id="_HFBatchedMoE.forward"></a>`forward(self, hidden_states: torch.Tensor)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L53)
- uses (calls/refs, reference-scoped): [`MoE`](../../models/common/moe.md#MoE), [`forward`](../../models/common/moe.md#MoE.forward)
- used by: [`MoE`](../../models/common/moe.md#MoE), [`build_and_swap_native_moe`](moe_replacement.md#build_and_swap_native_moe), [`forward`](../../models/common/moe.md#MoE.forward)

## Functions
- <a id="_build_moe_config"></a>`_build_moe_config(params: dict, config)` — [`L540`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L540) — Build a fully-specified MoE.Config from probed parameters.
- <a id="_get_expert_param_info"></a>`_get_expert_param_info()` — [`L502`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L502) — Discover GroupedExperts parameter names and their TP shard placements.
- <a id="_get_moe_attr_name"></a>`_get_moe_attr_name(layer: nn.Module)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L219) — Return the attribute name holding the MoE block on a decoder layer.
- <a id="_get_moe_block"></a>`_get_moe_block(layer: nn.Module)` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L231) — Return the MoE block module from a decoder layer.
- <a id="_probe_hf_moe_block"></a>`_probe_hf_moe_block(moe_block: nn.Module, config)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L241) — Extract MoE configuration from an HF MoE block.
- <a id="_probe_layer_level_moe"></a>`_probe_layer_level_moe(layer: nn.Module, config)` — [`L410`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L410) — Probe layer-level MoE (Gemma4) where router/experts are layer siblings.
- <a id="_probe_shared_experts"></a>`_probe_shared_experts(moe_block: nn.Module, config)` — [`L369`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L369) — Detect shared expert configuration from the HF MoE block.
- <a id="_resolve_num_experts"></a>`_resolve_num_experts(experts: nn.Module, gate: nn.Module | None, moe_block: nn.Module, config)` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L315) — Infer the total expert count from the HF MoE block or config.
- <a id="_resolve_score_func"></a>`_resolve_score_func(gate: nn.Module | None, config)` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L351) — Determine the router scoring function (softmax or sigmoid).
- <a id="_resolve_top_k"></a>`_resolve_top_k(moe_block: nn.Module, gate: nn.Module | None, config)` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L335) — Infer top-k routing from the HF MoE block or config.
- <a id="build_and_swap_native_moe"></a>`build_and_swap_native_moe(model: nn.Module, parallel_dims: ParallelDims)` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L92) — Build Titan MoE modules and swap them into the model.
- <a id="prepare_native_moe_configs"></a>`prepare_native_moe_configs(model: nn.Module, config)` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L62) — Probe each HF MoE layer and store a Titan ``MoE.Config`` for later build.

## Module values
- <a id="_LINEAR_INIT"></a>`_LINEAR_INIT` — [`L494`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L494)
- <a id="_expert_param_info_cache._expert_param_info_cache"></a>`_expert_param_info_cache` — [`L499`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/moe_replacement.py#L499)

