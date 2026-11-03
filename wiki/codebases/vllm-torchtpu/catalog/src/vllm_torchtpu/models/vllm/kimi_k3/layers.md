---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/layers.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/layers.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.layers`/
symbols:
  KimiMLP.forward: KimiMLP#forward().
  AttentionResidual.process_weights_after_loading: AttentionResidual#process_weights_after_loading().
  AttentionResidual.forward: AttentionResidual#forward().
  KimiMLP.act_fn: KimiMLP#act_fn.
  AttentionResidual._prefill_op: AttentionResidual#_prefill_op.
  _build_attention_residual_op: _build_attention_residual_op().
  KimiMLP: KimiMLP#
  KimiMLP.sp_group: KimiMLP#sp_group.
  SituAndMul.forward: SituAndMul#forward().
  AttentionResidual: AttentionResidual#
  KimiMLP.tp_group: KimiMLP#tp_group.
  AttentionResidual.eps: AttentionResidual#eps.
  _build_attention_residual_op.core: _build_attention_residual_op().core().
  SituAndMul.linear_beta: SituAndMul#linear_beta.
  KimiMLP.down_proj: KimiMLP#down_proj.
  SituAndMul.beta: SituAndMul#beta.
  AttentionResidual.folded_weight: AttentionResidual#folded_weight.
  SituAndMul: SituAndMul#
  KimiMLP.gate_up_proj: KimiMLP#gate_up_proj.
  AttentionResidual.norm: AttentionResidual#norm.
  AttentionResidual.proj: AttentionResidual#proj.
  SituAndMul.__init__: SituAndMul#__init__().
  KimiMLP.__init__: KimiMLP#__init__().
  AttentionResidual.__init__: AttentionResidual#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/layers.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py)

## Classes
### <a id="AttentionResidual"></a>`AttentionResidual`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/layers.py:165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L165)
- doc: K3 attention residual with a fused kernel for tiled prefill.
- signature: `class AttentionResidual(nn.Module):`
- members:
  - <a id="AttentionResidual.forward"></a>`forward(self, prefix_sum: torch.Tensor, block_residuals: torch.Tensor)` — [`L196`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L196)
  - <a id="AttentionResidual.process_weights_after_loading"></a>`process_weights_after_loading(self)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L185) — Fold the norm and projection weights into one [hidden] vector.
  - <a id="AttentionResidual.eps"></a>`eps` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L175)
  - <a id="AttentionResidual.folded_weight"></a>`folded_weight` — [`L191`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L191)
  - <a id="AttentionResidual.norm"></a>`norm` — [`L176`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L176)
  - <a id="AttentionResidual.proj"></a>`proj` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L177)
- protocol/private: <a id="AttentionResidual.__init__"></a>`__init__`[`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L168), <a id="AttentionResidual._prefill_op"></a>`_prefill_op`[`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L192)
- uses (calls/refs, reference-scoped): [`fresh_buffer`](../../../utils.md#fresh_buffer), [`_build_attention_residual_op`](layers.md#_build_attention_residual_op)
- used by: [`process_weights_after_loading`](model.md#KimiLinearForCausalLM.process_weights_after_loading), [`mlp_res`](model.md#KimiDecoderLayer.mlp_res), [`output_attn_res`](model.md#KimiModel.output_attn_res), [`self_attention_res`](model.md#KimiDecoderLayer.self_attention_res)

### <a id="KimiMLP"></a>`KimiMLP`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/layers.py:77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L77)
- doc: The standard vLLM merged-projection gated MLP.
- signature: `class KimiMLP(nn.Module):`
- members:
  - <a id="KimiMLP.forward"></a>`forward(self, hidden_states: torch.Tensor, sequence_parallel: bool = False)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L142)
  - <a id="KimiMLP.act_fn"></a>`act_fn` — [`L133`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L133)
  - <a id="KimiMLP.down_proj"></a>`down_proj` — [`L124`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L124)
  - <a id="KimiMLP.gate_up_proj"></a>`gate_up_proj` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L117)
  - <a id="KimiMLP.sp_group"></a>`sp_group` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L95)
  - <a id="KimiMLP.tp_group"></a>`tp_group` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L94)
- protocol/private: <a id="KimiMLP.__init__"></a>`__init__`[`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L80)
- uses (calls/refs, reference-scoped): [`all_gather`](collective_ops.md#TokenShardCollectives.all_gather), [`TPU_K3_SP_PREFILL`](../../../envs.md#TPU_K3_SP_PREFILL), [`TokenShardCollectives`](collective_ops.md#TokenShardCollectives), [`reduce_scatter`](collective_ops.md#TokenShardCollectives.reduce_scatter), [`SituAndMul`](layers.md#SituAndMul)
- used by: [`shared_experts`](moe.md#KimiMoE.shared_experts), [`mlp`](model.md#KimiDecoderLayer.mlp), [`mlp`](dspark.md#K3DSparkDecoderLayer.mlp)

### <a id="SituAndMul"></a>`SituAndMul`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/layers.py:57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L57)
- doc: Kimi's SITU gated activation.
- signature: `class SituAndMul(nn.Module):`
- members:
  - <a id="SituAndMul.forward"></a>`forward(self, x: torch.Tensor)` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L69)
  - <a id="SituAndMul.beta"></a>`beta` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L66)
  - <a id="SituAndMul.linear_beta"></a>`linear_beta` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L67)
- protocol/private: <a id="SituAndMul.__init__"></a>`__init__`[`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L64)
- used by: [`act_fn`](layers.md#KimiMLP.act_fn)

## Functions
- <a id="_build_attention_residual_op"></a>`_build_attention_residual_op(eps: float)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L43) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)
- <a id="_build_attention_residual_op.core"></a>`core(prefix: jax.Array, history: jax.Array, weight: jax.Array)` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/layers.py#L48) — documented in [kimi-k3-kernels](../../../../../../concepts/kimi-k3-kernels.md)

