---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/moe.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/moe.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.moe`/
symbols:
  KimiMoE._forward_expert_parallel: KimiMoE#_forward_expert_parallel().
  KimiMoE.shared_group: KimiMoE#shared_group.
  KimiMoE.shared_experts: KimiMoE#shared_experts.
  KimiMoE.experts: KimiMoE#experts.
  KimiMoE.routed_expert_up_proj: KimiMoE#routed_expert_up_proj.
  KimiMoE.gate: KimiMoE#gate.
  KimiMoE.forward: KimiMoE#forward().
  KimiMoE.routed_expert_down_proj: KimiMoE#routed_expert_down_proj.
  KimiMoE.initialize_dummy_router: KimiMoE#initialize_dummy_router().
  KimiMoE.routed_expert_norm: KimiMoE#routed_expert_norm.
  KimiRoutedOutputTransform.forward: KimiRoutedOutputTransform#forward().
  KimiMoE: KimiMoE#
  KimiRoutedOutputTransform.norm: KimiRoutedOutputTransform#norm.
  KimiMoE.prefill_group: KimiMoE#prefill_group.
  KimiRoutedOutputTransform: KimiRoutedOutputTransform#
  KimiRoutedOutputTransform.up_proj: KimiRoutedOutputTransform#up_proj.
  KimiMoE.prefix: KimiMoE#prefix.
  KimiMoE.tp_size: KimiMoE#tp_size.
  KimiMoE.use_ep: KimiMoE#use_ep.
  KimiRoutedOutputTransform.__init__: KimiRoutedOutputTransform#__init__().
  KimiMoE.__init__: KimiMoE#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/moe.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py)

## Classes
### <a id="KimiMoE"></a>`KimiMoE`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/moe.py:67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L67)
- doc: Standard or latent Kimi MoE backed by the fused TPU GMM custom op.
- signature: `class KimiMoE(nn.Module):`
- members:
  - <a id="KimiMoE._forward_expert_parallel"></a>`_forward_expert_parallel(self, hidden_states: torch.Tensor, sequence_parallel: bool)` — [`L275`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L275) — Run EP experts with sharded or replicated tokens, then add shared experts. — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.forward"></a>`forward(self, hidden_states: torch.Tensor, sequence_parallel: bool = False)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L264) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.initialize_dummy_router"></a>`initialize_dummy_router(self)` — [`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L231) — Use fan-in random weights and fixed, distinct random layer biases.
  - <a id="KimiMoE.experts"></a>`experts` — [`L190`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L190) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.gate"></a>`gate` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L96) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.prefill_group"></a>`prefill_group` — [`L145`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L145)
  - <a id="KimiMoE.prefix"></a>`prefix` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L81)
  - <a id="KimiMoE.routed_expert_down_proj"></a>`routed_expert_down_proj` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L110)
  - <a id="KimiMoE.routed_expert_norm"></a>`routed_expert_norm` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L121)
  - <a id="KimiMoE.routed_expert_up_proj"></a>`routed_expert_up_proj` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L126) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.shared_experts"></a>`shared_experts` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L153) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMoE.shared_group"></a>`shared_group` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L146) — documented in [distributed-parallelism-and-meshes](../../../../../../concepts/distributed-parallelism-and-meshes.md)
  - <a id="KimiMoE.tp_size"></a>`tp_size` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L83)
  - <a id="KimiMoE.use_ep"></a>`use_ep` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L85)
- protocol/private: <a id="KimiMoE.__init__"></a>`__init__`[`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L70)
- uses (calls/refs, reference-scoped): [`get_intra_chip_group`](../../../distributed/intra_chip.md#get_intra_chip_group), [`apply_with_routing`](../../../layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod.apply_with_routing), [`hierarchical_moe_parallel_config`](../../../layers/adapter/moe_hierarchical.md#hierarchical_moe_parallel_config), [`route`](../../../layers/adapter/moe_routing.md#route), [`hierarchical_split_or_none`](../../../layers/adapter/moe_hierarchical.md#hierarchical_split_or_none), [`make_latent_projection`](../../../layers/adapter/latent_proj_intra_chip.md#make_latent_projection), [`FusedPrefillCollectives`](collective_ops.md#FusedPrefillCollectives), [`reduce_scatter`](collective_ops.md#FusedPrefillCollectives.reduce_scatter), [`KimiMLP`](layers.md#KimiMLP), [`gather_moe_inputs`](collective_ops.md#FusedPrefillCollectives.gather_moe_inputs), [`all_reduce`](collective_ops.md#FusedPrefillCollectives.all_reduce), [`TPU_K3_SP_PREFILL`](../../../envs.md#TPU_K3_SP_PREFILL), [`KimiRoutedOutputTransform`](moe.md#KimiRoutedOutputTransform)
- used by: [`process_weights_after_loading`](model.md#KimiLinearForCausalLM.process_weights_after_loading), [`block_sparse_moe`](model.md#KimiDecoderLayer.block_sparse_moe)

### <a id="KimiRoutedOutputTransform"></a>`KimiRoutedOutputTransform`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/moe.py:49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L49)
- signature: `class KimiRoutedOutputTransform(nn.Module):`
- members:
  - <a id="KimiRoutedOutputTransform.forward"></a>`forward(self, hidden_states: torch.Tensor)` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L60)
  - <a id="KimiRoutedOutputTransform.norm"></a>`norm` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L57)
  - <a id="KimiRoutedOutputTransform.up_proj"></a>`up_proj` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L58)
- protocol/private: <a id="KimiRoutedOutputTransform.__init__"></a>`__init__`[`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/moe.py#L50)
- used by: [`routed_expert_up_proj`](moe.md#KimiMoE.routed_expert_up_proj)

