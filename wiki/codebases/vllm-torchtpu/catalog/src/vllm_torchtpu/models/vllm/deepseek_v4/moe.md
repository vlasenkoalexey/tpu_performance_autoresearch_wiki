---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.moe`/DeepseekV4MoE#
symbols:
  DeepseekV4MoE.experts: experts.
  DeepseekV4MoE.gate: gate.
  DeepseekV4MoE.shared_experts: shared_experts.
  DeepseekV4MoE.hash_indices_dtype: hash_indices_dtype.
  DeepseekV4MoE.forward: forward().
  DeepseekV4MoE.routes_dp_gathered_tokens: routes_dp_gathered_tokens().
  DeepseekV4MoE.tp_rank: tp_rank.
  DeepseekV4MoE: ''
  DeepseekV4MoE.swiglu_limit: swiglu_limit.
  DeepseekV4MoE.tp_size: tp_size.
  DeepseekV4MoE.routed_scaling_factor: routed_scaling_factor.
  DeepseekV4MoE.scoring_func: scoring_func.
  DeepseekV4MoE.__init__: __init__().
  DeepseekV4MoE.prefix: prefix.
  DeepseekV4MoE.hidden_size: hidden_size.
  DeepseekV4MoE.n_routed_experts: n_routed_experts.
  DeepseekV4MoE.renormalize: renormalize.
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py)

## Classes
### <a id="DeepseekV4MoE"></a>`DeepseekV4MoE`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py:32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L32)
- doc: DeepSeek-V4 MoE layer with dynamic hash routing and fused routed experts.
- signature: `class DeepseekV4MoE(nn.Module):`
- members:
  - <a id="DeepseekV4MoE.forward"></a>`forward(self, hidden_states: torch.Tensor, input_ids: torch.Tensor | None = None)` — [`L144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L144) — Forward pass executing router gate and fused expert computation.
  - <a id="DeepseekV4MoE.routes_dp_gathered_tokens"></a>`routes_dp_gathered_tokens(self)` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L132) — Whether the experts see the DP-gathered batch or this rank's rows.
  - <a id="DeepseekV4MoE.experts"></a>`experts` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L98) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4MoE.gate"></a>`gate` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L53) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4MoE.hash_indices_dtype"></a>`hash_indices_dtype` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L64)
  - <a id="DeepseekV4MoE.hidden_size"></a>`hidden_size` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L47)
  - <a id="DeepseekV4MoE.n_routed_experts"></a>`n_routed_experts` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L48)
  - <a id="DeepseekV4MoE.prefix"></a>`prefix` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L44)
  - <a id="DeepseekV4MoE.renormalize"></a>`renormalize` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L50)
  - <a id="DeepseekV4MoE.routed_scaling_factor"></a>`routed_scaling_factor` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L46)
  - <a id="DeepseekV4MoE.scoring_func"></a>`scoring_func` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L51)
  - <a id="DeepseekV4MoE.shared_experts"></a>`shared_experts` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L82) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4MoE.swiglu_limit"></a>`swiglu_limit` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L49)
  - <a id="DeepseekV4MoE.tp_rank"></a>`tp_rank` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L95)
  - <a id="DeepseekV4MoE.tp_size"></a>`tp_size` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L41)
- protocol/private: <a id="DeepseekV4MoE.__init__"></a>`__init__`[`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/moe.py#L35)
- uses (calls/refs, reference-scoped): [`DeepseekV4MLP`](layers.md#DeepseekV4MLP)
- used by: [`_dp_gather_hash_moe_input_ids`](model.md#DeepseekV4Model._dp_gather_hash_moe_input_ids), [`ffn`](model.md#DeepseekV4DecoderLayer.ffn)

