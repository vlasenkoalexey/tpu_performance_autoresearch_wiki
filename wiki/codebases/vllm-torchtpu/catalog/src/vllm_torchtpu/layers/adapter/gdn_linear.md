---
title: 'Module: src/vllm_torchtpu/layers/adapter/gdn_linear.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/gdn_linear.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.gdn_linear`/
symbols:
  GdnInterleavedColumnParallelLinear.weight_loader: GdnInterleavedColumnParallelLinear#weight_loader().
  GdnColumnParallelLinear.weight_loader: GdnColumnParallelLinear#weight_loader().
  GdnInterleavedColumnParallelLinear.local_group_sizes: GdnInterleavedColumnParallelLinear#local_group_sizes.
  GdnColumnParallelLinear.replication_factors: GdnColumnParallelLinear#replication_factors.
  GdnColumnParallelLinear.weight: GdnColumnParallelLinear#weight.
  GdnColumnParallelLinear.checkpoint_sizes: GdnColumnParallelLinear#checkpoint_sizes.
  GdnInterleavedColumnParallelLinear: GdnInterleavedColumnParallelLinear#
  GdnColumnParallelLinear: GdnColumnParallelLinear#
  GdnColumnParallelLinear.__init__: GdnColumnParallelLinear#__init__().
  GdnColumnParallelLinear.weight_loader_v2: GdnColumnParallelLinear#weight_loader_v2.
  GdnInterleavedColumnParallelLinear.__init__: GdnInterleavedColumnParallelLinear#__init__().
  GdnColumnParallelLinear._parameter_slice: GdnColumnParallelLinear#_parameter_slice().
  GdnInterleavedColumnParallelLinear.geometry: GdnInterleavedColumnParallelLinear#geometry.
  GdnInterleavedColumnParallelLinear.group_sizes: GdnInterleavedColumnParallelLinear#group_sizes.
  GdnInterleavedColumnParallelLinear.replicated_segments: GdnInterleavedColumnParallelLinear#replicated_segments.
  GdnInterleavedColumnParallelLinear.weight_loader_v2: GdnInterleavedColumnParallelLinear#weight_loader_v2.
---
# Module: [`src/vllm_torchtpu/layers/adapter/gdn_linear.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py)

## Classes
### <a id="GdnColumnParallelLinear"></a>`GdnColumnParallelLinear`
- def: [`src/vllm_torchtpu/layers/adapter/gdn_linear.py:39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L39)
- doc: Merged Q/K/V\[/Z\] projection using the same loader for every TP size.
- signature: `class GdnColumnParallelLinear(MergedColumnParallelLinear):`
- members:
  - <a id="GdnColumnParallelLinear._parameter_slice"></a>`_parameter_slice(self, param: BasevLLMParameter, size: int, offset: int)` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L83) — Translate output-channel coordinates to this parameter's storage.
  - <a id="GdnColumnParallelLinear.weight_loader"></a>`weight_loader(self, param: BasevLLMParameter, loaded_weight: torch.Tensor, loaded_shard_id: tuple[int, ...] | int | None = None)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L91)
  - <a id="GdnColumnParallelLinear.checkpoint_sizes"></a>`checkpoint_sizes` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L63)
  - <a id="GdnColumnParallelLinear.replication_factors"></a>`replication_factors` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L66)
  - <a id="GdnColumnParallelLinear.weight"></a>`weight` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L49)
  - <a id="GdnColumnParallelLinear.weight_loader_v2"></a>`weight_loader_v2` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L139)
- protocol/private: <a id="GdnColumnParallelLinear.__init__"></a>`__init__`[`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L51)
- uses (calls/refs, reference-scoped): [`GdnHeadGeometry`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry), [`kq_replication_factor`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.kq_replication_factor), [`num_kq_heads`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.num_kq_heads), [`num_v_heads`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.num_v_heads)
- used by: [`forward`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.forward), [`_forward_fused_pooled_pcp`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._forward_fused_pooled_pcp), [`conv1d`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.conv1d), [`_create_conv1d`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._create_conv1d), [`create_qkvz_proj`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.create_qkvz_proj), [`process_weights_after_loading`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.process_weights_after_loading)

### <a id="GdnInterleavedColumnParallelLinear"></a>`GdnInterleavedColumnParallelLinear`
- def: [`src/vllm_torchtpu/layers/adapter/gdn_linear.py:142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L142)
- doc: Shard checkpoint groups while keeping complete shared Q/K heads.
- signature: `class GdnInterleavedColumnParallelLinear(MergedColumnParallelLinear):`
- members:
  - <a id="GdnInterleavedColumnParallelLinear.weight_loader"></a>`weight_loader(self, param: BasevLLMParameter, loaded_weight: torch.Tensor, loaded_shard_id: tuple[int, ...] | int | None = None)` — [`L180`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L180)
  - <a id="GdnInterleavedColumnParallelLinear.geometry"></a>`geometry` — [`L161`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L161)
  - <a id="GdnInterleavedColumnParallelLinear.group_sizes"></a>`group_sizes` — [`L162`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L162)
  - <a id="GdnInterleavedColumnParallelLinear.local_group_sizes"></a>`local_group_sizes` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L164)
  - <a id="GdnInterleavedColumnParallelLinear.replicated_segments"></a>`replicated_segments` — [`L163`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L163)
  - <a id="GdnInterleavedColumnParallelLinear.weight_loader_v2"></a>`weight_loader_v2` — [`L224`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L224)
- protocol/private: <a id="GdnInterleavedColumnParallelLinear.__init__"></a>`__init__`[`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/gdn_linear.py#L151)
- uses (calls/refs, reference-scoped): [`local_num_kq_heads`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.local_num_kq_heads), [`parallel_size`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.parallel_size), [`GdnHeadGeometry`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry), [`kq_replication_factor`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.kq_replication_factor), [`kq_shard_index`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.kq_shard_index), [`num_kq_heads`](../../kernels/gdn/head_geometry.md#GdnHeadGeometry.num_kq_heads)
- used by: [`create_qkvz_proj`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.create_qkvz_proj), [`create_ba_proj`](custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.create_ba_proj)

