---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.layers`/
symbols:
  DeepseekV4MLP.forward: DeepseekV4MLP#forward().
  DeepseekV4MLP.act_fn: DeepseekV4MLP#act_fn.
  mhc_collapse_head: mhc_collapse_head().
  DeepseekV4MLP: DeepseekV4MLP#
  DeepseekV4MLP.gate_up_proj: DeepseekV4MLP#gate_up_proj.
  DeepseekV4MLP.down_proj: DeepseekV4MLP#down_proj.
  DeepseekV4MLP.__init__: DeepseekV4MLP#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py)

## Classes
### <a id="DeepseekV4MLP"></a>`DeepseekV4MLP`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py:50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L50)
- doc: DeepSeek-V4 feed-forward layer for dense/shared expert projections.
- signature: `class DeepseekV4MLP(nn.Module):`
- members:
  - <a id="DeepseekV4MLP.forward"></a>`forward(self, x: torch.Tensor)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L91)
  - <a id="DeepseekV4MLP.act_fn"></a>`act_fn` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L87)
  - <a id="DeepseekV4MLP.down_proj"></a>`down_proj` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L73)
  - <a id="DeepseekV4MLP.gate_up_proj"></a>`gate_up_proj` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L65)
- protocol/private: <a id="DeepseekV4MLP.__init__"></a>`__init__`[`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L53)
- used by: [`shared_experts`](moe.md#DeepseekV4MoE.shared_experts)

## Functions
- <a id="mhc_collapse_head"></a>`mhc_collapse_head(hidden_states: torch.Tensor, hc_fn: torch.Tensor, hc_scale: torch.Tensor, hc_base: torch.Tensor, rms_norm_eps: float, hc_eps: float)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/layers.py#L30) — Collapse multi-stream residual manifold into a single vector before LM head.

