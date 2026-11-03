---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/attention.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/attention.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.attention`/
symbols:
  KimiDeltaAttention.forward: KimiDeltaAttention#forward().
  KimiDeltaAttention._core_attention_pooled: KimiDeltaAttention#_core_attention_pooled().
  MultiHeadLatentAttention.q_b_proj: MultiHeadLatentAttention#q_b_proj.
  MultiHeadLatentAttention.prefill_group: MultiHeadLatentAttention#prefill_group.
  KimiDeltaAttention.packed_prefill_weight: KimiDeltaAttention#packed_prefill_weight.
  MultiHeadLatentAttention.prepare_sp_mla_gate: MultiHeadLatentAttention#prepare_sp_mla_gate().
  MultiHeadLatentAttention.mla_attn: MultiHeadLatentAttention#mla_attn.
  KimiDeltaAttention.process_weights_after_loading: KimiDeltaAttention#process_weights_after_loading().
  KimiDeltaAttention.g_proj: KimiDeltaAttention#g_proj.
  MultiHeadLatentAttention.forward: MultiHeadLatentAttention#forward().
  KimiDeltaAttention.head_dim: KimiDeltaAttention#head_dim.
  KimiDeltaAttention.v_conv1d: KimiDeltaAttention#v_conv1d.
  KimiDeltaAttention.num_heads: KimiDeltaAttention#num_heads.
  KimiDeltaAttention.projection_size: KimiDeltaAttention#projection_size.
  KimiDeltaAttention.dt_bias: KimiDeltaAttention#dt_bias.
  MultiHeadLatentAttention.kv_a_proj_with_mqa: MultiHeadLatentAttention#kv_a_proj_with_mqa.
  CausalDepthwiseConv1d.weight: CausalDepthwiseConv1d#weight.
  KimiDeltaAttention.g_b_proj: KimiDeltaAttention#g_b_proj.
  KimiDeltaAttention.get_state_shape: KimiDeltaAttention#get_state_shape().
  MixedParallelMergedLinear._slice_loaded_weight: MixedParallelMergedLinear#_slice_loaded_weight().
  KimiDeltaAttention.fused_qkvb_proj: KimiDeltaAttention#fused_qkvb_proj.
  KimiDeltaAttention.total_heads: KimiDeltaAttention#total_heads.
  KimiDeltaAttention.local_projection_size: KimiDeltaAttention#local_projection_size.
  MultiHeadLatentAttention.kv_b_proj: MultiHeadLatentAttention#kv_b_proj.
  KimiDeltaAttention.q_conv1d: KimiDeltaAttention#q_conv1d.
  KimiDeltaAttention.k_conv1d: KimiDeltaAttention#k_conv1d.
  KimiDeltaAttention.f_b_proj: KimiDeltaAttention#f_b_proj.
  KimiDeltaAttention.dispatched_kda_op: KimiDeltaAttention#dispatched_kda_op.
  KimiDeltaAttention.pooled_kda_op: KimiDeltaAttention#pooled_kda_op.
  MultiHeadLatentAttention.mla_gate_is_fused: MultiHeadLatentAttention#mla_gate_is_fused.
  KimiDeltaAttention.f_a_proj: KimiDeltaAttention#f_a_proj.
  MultiHeadLatentAttention: MultiHeadLatentAttention#
  MultiHeadLatentAttention.q_lora_rank: MultiHeadLatentAttention#q_lora_rank.
  MultiHeadLatentAttention.g_proj: MultiHeadLatentAttention#g_proj.
  MultiHeadLatentAttention.o_proj: MultiHeadLatentAttention#o_proj.
  KimiDeltaAttention.conv_size: KimiDeltaAttention#conv_size.
  KimiDeltaAttention.prefill_group: KimiDeltaAttention#prefill_group.
  KimiDeltaAttention._metadata: KimiDeltaAttention#_metadata().
  KimiDeltaAttention.A_log: KimiDeltaAttention#A_log.
  MultiHeadLatentAttention.kv_lora_rank: MultiHeadLatentAttention#kv_lora_rank.
  MultiHeadLatentAttention.v_head_dim: MultiHeadLatentAttention#v_head_dim.
  KimiDeltaAttention.use_full_rank_gate: KimiDeltaAttention#use_full_rank_gate.
  KimiDeltaAttention.kv_cache: KimiDeltaAttention#kv_cache.
  KimiDeltaAttention.get_state_dtype: KimiDeltaAttention#get_state_dtype().
  MultiHeadLatentAttention.q_proj: MultiHeadLatentAttention#q_proj.
  MultiHeadLatentAttention.kv_a_layernorm: MultiHeadLatentAttention#kv_a_layernorm.
  KimiDeltaAttention.o_norm: KimiDeltaAttention#o_norm.
  KimiDeltaAttention.o_proj: KimiDeltaAttention#o_proj.
  KimiDeltaAttention.conv_weight_fused: KimiDeltaAttention#conv_weight_fused.
  MultiHeadLatentAttention.qk_rope_head_dim: MultiHeadLatentAttention#qk_rope_head_dim.
  MultiHeadLatentAttention.fused_qkv_a_proj: MultiHeadLatentAttention#fused_qkv_a_proj.
  MultiHeadLatentAttention.q_a_layernorm: MultiHeadLatentAttention#q_a_layernorm.
  kda_state_dtype: kda_state_dtype().
  MixedParallelMergedLinear.mixed_tp_size: MixedParallelMergedLinear#mixed_tp_size.
  CausalDepthwiseConv1d: CausalDepthwiseConv1d#
  KimiDeltaAttention: KimiDeltaAttention#
  KimiDeltaAttention.fused_fa_ga_proj: KimiDeltaAttention#fused_fa_ga_proj.
  logger: logger.
  MixedParallelMergedLinear.weight_loader: MixedParallelMergedLinear#weight_loader().
  MixedParallelMergedLinear.weight_loader_v2: MixedParallelMergedLinear#weight_loader_v2().
  MultiHeadLatentAttention.qk_nope_head_dim: MultiHeadLatentAttention#qk_nope_head_dim.
  MultiHeadLatentAttention.qk_head_dim: MultiHeadLatentAttention#qk_head_dim.
  KimiDeltaAttention.tp_size: KimiDeltaAttention#tp_size.
  KimiDeltaAttention.num_spec_tokens: KimiDeltaAttention#num_spec_tokens.
  KimiDeltaAttention.gate_lower_bound: KimiDeltaAttention#gate_lower_bound.
  _load_a_log: _load_a_log().
  MixedParallelMergedLinear: MixedParallelMergedLinear#
  MixedParallelMergedLinear.mixed_tp_rank: MixedParallelMergedLinear#mixed_tp_rank.
  MixedParallelMergedLinear.replicate_outputs: MixedParallelMergedLinear#replicate_outputs.
  CausalDepthwiseConv1d.channels: CausalDepthwiseConv1d#channels.
  CausalDepthwiseConv1d.weight_loader: CausalDepthwiseConv1d#weight_loader().
  KimiDeltaAttention.prefix: KimiDeltaAttention#prefix.
  KimiDeltaAttention.vllm_config: KimiDeltaAttention#vllm_config.
  KimiDeltaAttention._pack_prefill_projection: KimiDeltaAttention#_pack_prefill_projection().
  MixedParallelMergedLinear.__init__: MixedParallelMergedLinear#__init__().
  MixedParallelMergedLinear.global_output_sizes: MixedParallelMergedLinear#global_output_sizes.
  MultiHeadLatentAttention.__init__: MultiHeadLatentAttention#__init__().
  CausalDepthwiseConv1d.__init__: CausalDepthwiseConv1d#__init__().
  CausalDepthwiseConv1d.kernel_size: CausalDepthwiseConv1d#kernel_size.
  KimiDeltaAttention.supports_dcp: KimiDeltaAttention#supports_dcp.
  KimiDeltaAttention.__init__: KimiDeltaAttention#__init__().
  KimiDeltaAttention.mamba_type: KimiDeltaAttention#mamba_type().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/attention.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py)

## Classes
### <a id="CausalDepthwiseConv1d"></a>`CausalDepthwiseConv1d`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/attention.py:430`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L430)
- doc: Checkpoint-compatible depthwise-convolution weight container.
- signature: `class CausalDepthwiseConv1d(nn.Module):`
- members:
  - <a id="CausalDepthwiseConv1d.weight_loader"></a>`weight_loader(self, parameter: nn.Parameter, loaded_weight: torch.Tensor)` — [`L443`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L443)
  - <a id="CausalDepthwiseConv1d.channels"></a>`channels` — [`L438`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L438)
  - <a id="CausalDepthwiseConv1d.kernel_size"></a>`kernel_size` — [`L439`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L439)
  - <a id="CausalDepthwiseConv1d.weight"></a>`weight` — [`L440`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L440) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
- protocol/private: <a id="CausalDepthwiseConv1d.__init__"></a>`__init__`[`L433`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L433)
- used by: [`process_weights_after_loading`](attention.md#KimiDeltaAttention.process_weights_after_loading), [`v_conv1d`](attention.md#KimiDeltaAttention.v_conv1d), [`k_conv1d`](attention.md#KimiDeltaAttention.k_conv1d), [`q_conv1d`](attention.md#KimiDeltaAttention.q_conv1d)

### <a id="KimiDeltaAttention"></a>`KimiDeltaAttention`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/attention.py:457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L457)
- doc: KDA registered with vLLM and executed by TPU Pallas custom ops.
- signature: `class KimiDeltaAttention(nn.Module, MambaBase):`
- members:
  - <a id="KimiDeltaAttention._core_attention_pooled"></a>`_core_attention_pooled(self, mixed_qkv: torch.Tensor, raw_gate: torch.Tensor, beta: torch.Tensor, output_gate: torch.Tensor, pool: torch.Tensor, metadata: AttentionMetadata)` — [`L801`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L801) — KDA over the unified pool: conv and recurrent state live in the — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention._pack_prefill_projection"></a>`_pack_prefill_projection(self)` — [`L664`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L664) — Cache BF16 KDA input weights after the normal checkpoint loaders.
  - <a id="KimiDeltaAttention.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor, sequence_parallel: bool = False)` — [`L695`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L695) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.get_state_dtype"></a>`get_state_dtype(self)` — [`L614`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L614)
  - <a id="KimiDeltaAttention.get_state_shape"></a>`get_state_shape(self)` — [`L617`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L617)
  - <a id="KimiDeltaAttention.mamba_type"></a>`mamba_type(self)` — [`L611`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L611)
  - <a id="KimiDeltaAttention.process_weights_after_loading"></a>`process_weights_after_loading(self, act_dtype: torch.dtype)` — [`L636`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L636) — Fold the three depthwise conv weights into the kernels' layout. — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.A_log"></a>`A_log` — [`L559`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L559)
  - <a id="KimiDeltaAttention.conv_size"></a>`conv_size` — [`L483`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L483)
  - <a id="KimiDeltaAttention.conv_weight_fused"></a>`conv_weight_fused` — [`L661`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L661)
  - <a id="KimiDeltaAttention.dispatched_kda_op"></a>`dispatched_kda_op` — [`L582`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L582) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="KimiDeltaAttention.dt_bias"></a>`dt_bias` — [`L560`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L560) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.f_a_proj"></a>`f_a_proj` — [`L502`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L502)
  - <a id="KimiDeltaAttention.f_b_proj"></a>`f_b_proj` — [`L541`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L541) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.fused_fa_ga_proj"></a>`fused_fa_ga_proj` — [`L501`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L501)
  - <a id="KimiDeltaAttention.fused_qkvb_proj"></a>`fused_qkvb_proj` — [`L493`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L493) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.g_b_proj"></a>`g_b_proj` — [`L549`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L549) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.g_proj"></a>`g_proj` — [`L509`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L509) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.gate_lower_bound"></a>`gate_lower_bound` — [`L489`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L489)
  - <a id="KimiDeltaAttention.head_dim"></a>`head_dim` — [`L476`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L476) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.k_conv1d"></a>`k_conv1d` — [`L528`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L528) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.kv_cache"></a>`kv_cache` — [`L578`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L578)
  - <a id="KimiDeltaAttention.local_projection_size"></a>`local_projection_size` — [`L482`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L482) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.num_heads"></a>`num_heads` — [`L480`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L480) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.num_spec_tokens"></a>`num_spec_tokens` — [`L484`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L484)
  - <a id="KimiDeltaAttention.o_norm"></a>`o_norm` — [`L565`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L565)
  - <a id="KimiDeltaAttention.o_proj"></a>`o_proj` — [`L566`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L566)
  - <a id="KimiDeltaAttention.packed_prefill_weight"></a>`packed_prefill_weight` — [`L666`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L666) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.pooled_kda_op"></a>`pooled_kda_op` — [`L597`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L597) — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="KimiDeltaAttention.prefill_group"></a>`prefill_group` — [`L574`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L574)
  - <a id="KimiDeltaAttention.prefix"></a>`prefix` — [`L473`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L473)
  - <a id="KimiDeltaAttention.projection_size"></a>`projection_size` — [`L481`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L481) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.q_conv1d"></a>`q_conv1d` — [`L527`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L527) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.supports_dcp"></a>`supports_dcp` — [`L460`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L460)
  - <a id="KimiDeltaAttention.total_heads"></a>`total_heads` — [`L477`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L477)
  - <a id="KimiDeltaAttention.tp_size"></a>`tp_size` — [`L475`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L475)
  - <a id="KimiDeltaAttention.use_full_rank_gate"></a>`use_full_rank_gate` — [`L490`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L490)
  - <a id="KimiDeltaAttention.v_conv1d"></a>`v_conv1d` — [`L529`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L529) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDeltaAttention.vllm_config"></a>`vllm_config` — [`L474`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L474)
- protocol/private: <a id="KimiDeltaAttention.__init__"></a>`__init__`[`L462`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L462), <a id="KimiDeltaAttention._metadata"></a>`_metadata`[`L625`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L625)
- uses (calls/refs, reference-scoped): [`fresh_buffer`](../../../utils.md#fresh_buffer), [`AttentionMetadata`](../../../layers/core/attention_metadata.md#AttentionMetadata), [`build_kimi_pooled_kda_op`](../../../layers/adapter/custom_ops/kda_attention_op.md#build_kimi_pooled_kda_op), [`request_distribution`](../../../layers/core/attention_metadata.md#AttentionMetadata.request_distribution), [`is_pcp_streaming_attention_metadata`](../../../layers/core/sequence_layout.md#is_pcp_streaming_attention_metadata), [`query_start_loc`](../../../layers/core/attention_metadata.md#AttentionMetadata.query_start_loc), [`seq_lens`](../../../layers/core/attention_metadata.md#AttentionMetadata.seq_lens), [`WEIGHT_FLIPPED_ATTR`](../../../layers/adapter/linear_common.md#WEIGHT_FLIPPED_ATTR), [`build_kimi_dispatched_kda_op`](../../../layers/adapter/custom_ops/kda_attention_op.md#build_kimi_dispatched_kda_op), [`weight`](attention.md#CausalDepthwiseConv1d.weight), [`FusedPrefillCollectives`](collective_ops.md#FusedPrefillCollectives), [`all_gather`](collective_ops.md#FusedPrefillCollectives.all_gather), [`reduce_scatter`](collective_ops.md#FusedPrefillCollectives.reduce_scatter), [`project_reduce_scatter`](collective_ops.md#FusedPrefillCollectives.project_reduce_scatter), [`all_reduce`](collective_ops.md#FusedPrefillCollectives.all_reduce), [`TPU_K3_SP_PREFILL`](../../../envs.md#TPU_K3_SP_PREFILL), [`mamba_state_indices`](../../../layers/core/attention_metadata.md#AttentionMetadata.mamba_state_indices), [`mamba_request_distribution`](../../../layers/core/attention_metadata.md#AttentionMetadata.mamba_request_distribution), [`mamba_slot_read_offsets`](../../../layers/core/attention_metadata.md#AttentionMetadata.mamba_slot_read_offsets), [`gather_project`](collective_ops.md#FusedPrefillCollectives.gather_project), [`CausalDepthwiseConv1d`](attention.md#CausalDepthwiseConv1d), [`kda_state_dtype`](attention.md#kda_state_dtype), [`mamba_ckpt_indices`](../../../layers/core/attention_metadata.md#AttentionMetadata.mamba_ckpt_indices), [`_load_a_log`](attention.md#_load_a_log)
- used by: [`self_attn`](model.md#KimiDecoderLayer.self_attn)

### <a id="MixedParallelMergedLinear"></a>`MixedParallelMergedLinear`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/attention.py:99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L99)
- doc: One local matmul containing replicated and TP-column weight slices.
- signature: `class MixedParallelMergedLinear(MergedColumnParallelLinear):`
- members:
  - <a id="MixedParallelMergedLinear.weight_loader"></a>`weight_loader(self, param: nn.Parameter, loaded_weight: torch.Tensor, loaded_shard_id: tuple[int, ...] | int | None = None)` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L171)
  - <a id="MixedParallelMergedLinear.weight_loader_v2"></a>`weight_loader_v2(self, param: BasevLLMParameter, loaded_weight: torch.Tensor, loaded_shard_id: tuple[int, ...] | int | None = None)` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L184)
  - <a id="MixedParallelMergedLinear.global_output_sizes"></a>`global_output_sizes` — [`L128`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L128)
  - <a id="MixedParallelMergedLinear.mixed_tp_rank"></a>`mixed_tp_rank` — [`L127`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L127)
  - <a id="MixedParallelMergedLinear.mixed_tp_size"></a>`mixed_tp_size` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L126)
  - <a id="MixedParallelMergedLinear.replicate_outputs"></a>`replicate_outputs` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L129)
- protocol/private: <a id="MixedParallelMergedLinear.__init__"></a>`__init__`[`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L108), <a id="MixedParallelMergedLinear._slice_loaded_weight"></a>`_slice_loaded_weight`[`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L143)
- used by: [`q_b_proj`](attention.md#MultiHeadLatentAttention.q_b_proj)

### <a id="MultiHeadLatentAttention"></a>`MultiHeadLatentAttention`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/attention.py:198`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L198)
- doc: NoPE MLA dispatched through the TPU Pallas MLA custom op.
- signature: `class MultiHeadLatentAttention(nn.Module):`
- members:
  - <a id="MultiHeadLatentAttention.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor, sequence_parallel: bool = False)` — [`L407`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L407)
  - <a id="MultiHeadLatentAttention.prepare_sp_mla_gate"></a>`prepare_sp_mla_gate(self)` — [`L380`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L380) — Refresh the TP2 MLA gate buffer after checkpoint loading or reload. — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="MultiHeadLatentAttention.fused_qkv_a_proj"></a>`fused_qkv_a_proj` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L249)
  - <a id="MultiHeadLatentAttention.g_proj"></a>`g_proj` — [`L303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L303)
  - <a id="MultiHeadLatentAttention.kv_a_layernorm"></a>`kv_a_layernorm` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L295)
  - <a id="MultiHeadLatentAttention.kv_a_proj_with_mqa"></a>`kv_a_proj_with_mqa` — [`L286`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L286)
  - <a id="MultiHeadLatentAttention.kv_b_proj"></a>`kv_b_proj` — [`L296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L296)
  - <a id="MultiHeadLatentAttention.kv_lora_rank"></a>`kv_lora_rank` — [`L234`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L234)
  - <a id="MultiHeadLatentAttention.mla_attn"></a>`mla_attn` — [`L363`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L363) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="MultiHeadLatentAttention.mla_gate_is_fused"></a>`mla_gate_is_fused` — [`L240`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L240)
  - <a id="MultiHeadLatentAttention.o_proj"></a>`o_proj` — [`L314`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L314)
  - <a id="MultiHeadLatentAttention.prefill_group"></a>`prefill_group` — [`L345`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L345) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="MultiHeadLatentAttention.q_a_layernorm"></a>`q_a_layernorm` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L250)
  - <a id="MultiHeadLatentAttention.q_b_proj"></a>`q_b_proj` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L251) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="MultiHeadLatentAttention.q_lora_rank"></a>`q_lora_rank` — [`L233`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L233)
  - <a id="MultiHeadLatentAttention.q_proj"></a>`q_proj` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L242)
  - <a id="MultiHeadLatentAttention.qk_head_dim"></a>`qk_head_dim` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L238)
  - <a id="MultiHeadLatentAttention.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L235)
  - <a id="MultiHeadLatentAttention.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L236)
  - <a id="MultiHeadLatentAttention.v_head_dim"></a>`v_head_dim` — [`L237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L237)
- protocol/private: <a id="MultiHeadLatentAttention.__init__"></a>`__init__`[`L201`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L201)
- uses (calls/refs, reference-scoped): [`WEIGHT_FLIPPED_ATTR`](../../../layers/adapter/linear_common.md#WEIGHT_FLIPPED_ATTR), [`mla_ops`](collective_ops.md#FusedPrefillCollectives.mla_ops), [`FusedPrefillCollectives`](collective_ops.md#FusedPrefillCollectives), [`all_gather`](collective_ops.md#FusedPrefillCollectives.all_gather), [`reduce_scatter`](collective_ops.md#FusedPrefillCollectives.reduce_scatter), [`all_reduce`](collective_ops.md#FusedPrefillCollectives.all_reduce), [`TPU_K3_SP_PREFILL`](../../../envs.md#TPU_K3_SP_PREFILL), [`MixedParallelMergedLinear`](attention.md#MixedParallelMergedLinear)
- used by: [`precompute_and_store_context_kv`](dspark.md#K3DSparkModel.precompute_and_store_context_kv), [`process_weights_after_loading`](model.md#KimiLinearForCausalLM.process_weights_after_loading), [`self_attn`](model.md#KimiDecoderLayer.self_attn), [`get_draft_kv_cache_layer_names`](dspark.md#K3DSparkForCausalLM.get_draft_kv_cache_layer_names), [`self_attn`](dspark.md#K3DSparkDecoderLayer.self_attn)

## Functions
- <a id="_load_a_log"></a>`_load_a_log(parameter: torch.Tensor, loaded_weight: torch.Tensor)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L88) — Load either the old ``[1, 1, H, 1]`` or current ``[H]`` layout.
- <a id="kda_state_dtype"></a>`kda_state_dtype(vllm_config: VllmConfig)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L71) — Storage dtypes for one KDA layer's conv and recurrent state.

## Module values
- <a id="logger"></a>`logger` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/attention.py#L68)

