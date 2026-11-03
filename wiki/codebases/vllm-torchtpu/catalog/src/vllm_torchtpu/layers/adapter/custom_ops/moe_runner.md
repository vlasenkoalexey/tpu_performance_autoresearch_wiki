---
title: 'Module: src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.custom_ops.moe_runner`/
symbols:
  VllmMoERunner._fused_output_is_reduced: VllmMoERunner#_fused_output_is_reduced().
  VllmMoERunner._fused_ep_owns_pcp_collectives: VllmMoERunner#_fused_ep_owns_pcp_collectives().
  _upstream_fused_output_is_reduced: _upstream_fused_output_is_reduced.
  VllmMoERunner._take_over_moe_quant_config_init: VllmMoERunner#_take_over_moe_quant_config_init().
  VllmMoERunner.__init__: VllmMoERunner#__init__().
  VllmMoERunner._maybe_dispatch: VllmMoERunner#_maybe_dispatch().
  VllmMoERunner._maybe_combine: VllmMoERunner#_maybe_combine().
  VllmMoERunner.ensure_moe_quant_config_init: VllmMoERunner#ensure_moe_quant_config_init().
  VllmMoERunner: VllmMoERunner#
  VllmMoERunner._select_forward: VllmMoERunner#_select_forward().
---
# Module: [`src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py)

## Classes
### <a id="VllmMoERunner"></a>`VllmMoERunner`
- def: [`src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py:37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L37)
- doc: vLLM builds every MoE layer's runner as `MoERunner(...)` unless a
- signature: `class VllmMoERunner(MoERunner):`
- members:
  - <a id="VllmMoERunner.ensure_moe_quant_config_init"></a>`ensure_moe_quant_config_init()` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L55)
- protocol/private: <a id="VllmMoERunner.__init__"></a>`__init__`[`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L47), <a id="VllmMoERunner._fused_ep_owns_pcp_collectives"></a>`_fused_ep_owns_pcp_collectives`[`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L129), <a id="VllmMoERunner._fused_output_is_reduced"></a>`_fused_output_is_reduced`[`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L81), <a id="VllmMoERunner._maybe_combine"></a>`_maybe_combine`[`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L148), <a id="VllmMoERunner._maybe_dispatch"></a>`_maybe_dispatch`[`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L140), <a id="VllmMoERunner._select_forward"></a>`_select_forward`[`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L69), <a id="VllmMoERunner._take_over_moe_quant_config_init"></a>`_take_over_moe_quant_config_init`[`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L51)
- uses (calls/refs, reference-scoped): [`fused_moe_ep_supported`](../fused_moe_ep.md#fused_moe_ep_supported), [`adaptive_fused_moe_supported`](../../../kernels/experimental/adaptive_fused_moe/vllm_adapter.md#adaptive_fused_moe_supported), [`moe_tp_decode_supported`](../moe_tp_decode.md#moe_tp_decode_supported), [`USE_MOE_FUSED_EP_KERNEL`](../../../envs.md#USE_MOE_FUSED_EP_KERNEL), [`_upstream_fused_output_is_reduced`](moe_runner.md#_upstream_fused_output_is_reduced)

## Module values
- <a id="_upstream_fused_output_is_reduced"></a>`_upstream_fused_output_is_reduced` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/custom_ops/moe_runner.py#L32)

