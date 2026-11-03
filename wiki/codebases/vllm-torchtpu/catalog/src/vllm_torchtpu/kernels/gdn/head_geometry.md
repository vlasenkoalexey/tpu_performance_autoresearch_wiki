---
title: 'Module: src/vllm_torchtpu/kernels/gdn/head_geometry.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/gdn/head_geometry.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.gdn.head_geometry`/
symbols:
  derive_gdn_head_geometry: derive_gdn_head_geometry().
  GdnHeadGeometry.parallel_size: GdnHeadGeometry#parallel_size.
  GdnHeadGeometry.local_num_kq_heads: GdnHeadGeometry#local_num_kq_heads.
  GdnHeadGeometry: GdnHeadGeometry#
  GdnHeadGeometry.local_num_v_heads: GdnHeadGeometry#local_num_v_heads.
  GdnHeadGeometry.kq_replication_factor: GdnHeadGeometry#kq_replication_factor.
  GdnHeadGeometry.kq_shard_index: GdnHeadGeometry#kq_shard_index().
  GdnHeadGeometry.local_conv_dim: GdnHeadGeometry#local_conv_dim().
  GdnHeadGeometry.local_state_shapes: GdnHeadGeometry#local_state_shapes().
  GdnHeadGeometry.num_kq_heads: GdnHeadGeometry#num_kq_heads.
  GdnHeadGeometry.num_v_heads: GdnHeadGeometry#num_v_heads.
  GdnHeadGeometry.num_unique_kq_shards: GdnHeadGeometry#num_unique_kq_shards.
---
# Module: [`src/vllm_torchtpu/kernels/gdn/head_geometry.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py)

## Classes
### <a id="GdnHeadGeometry"></a>`GdnHeadGeometry`
- def: [`src/vllm_torchtpu/kernels/gdn/head_geometry.py:20`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L20) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
- doc: Validated rank-local GDN head geometry.
- signature: `class GdnHeadGeometry:`
- members:
  - <a id="GdnHeadGeometry.kq_shard_index"></a>`kq_shard_index(self, rank: int)` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L36) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.local_conv_dim"></a>`local_conv_dim(self, d_k: int, d_v: int)` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L41) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.local_state_shapes"></a>`local_state_shapes(self, shapes: tuple[tuple[int, ...], ...], d_k: int, d_v: int, *, conv_dim_axis: int = -1)` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L48) — Apply head ownership, preserving tap/speculation and layout axes. — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.kq_replication_factor"></a>`kq_replication_factor` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L34) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.local_num_kq_heads"></a>`local_num_kq_heads` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L32) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.local_num_v_heads"></a>`local_num_v_heads` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L33) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.num_kq_heads"></a>`num_kq_heads` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L28) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
  - <a id="GdnHeadGeometry.num_unique_kq_shards"></a>`num_unique_kq_shards` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L31)
  - <a id="GdnHeadGeometry.num_v_heads"></a>`num_v_heads` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L29)
  - <a id="GdnHeadGeometry.parallel_size"></a>`parallel_size` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L30) — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)
- used by: [`fused_qkvz_projection_pcp_gdn`](../experimental/gdn_pcp_fused/pcp_wrapper.md#fused_qkvz_projection_pcp_gdn), [`_admit_raiden_hybrid_kv_cache`](../../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`lower_gdn_state_fanout_spans_sol`](../../distributed/kv_transfer/raiden/seq_on_lane.md#lower_gdn_state_fanout_spans_sol), [`forward`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.forward), [`_build_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_gdn_op), [`_build_pooled_pcp_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_pooled_pcp_gdn_op), [`derive_gdn_head_geometry`](head_geometry.md#derive_gdn_head_geometry), [`_build_pooled_gdn_op`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention._build_pooled_gdn_op), [`_hybrid_mamba_state_layout`](../../platforms/tpu_block_size_utils.md#_hybrid_mamba_state_layout), [`_validate_gdn_transfer_geometry`](../../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._validate_gdn_transfer_geometry), [`_reorder_gdn_qkv_for_pcp`](../../layers/core/gdn_attention.md#_reorder_gdn_qkv_for_pcp), [`weight_loader`](../../layers/adapter/gdn_linear.md#GdnInterleavedColumnParallelLinear.weight_loader), [`run_jax_gdn_attention_pcp_tp_prefill`](../../layers/core/gdn_attention.md#run_jax_gdn_attention_pcp_tp_prefill), [`run_jax_gdn_attention_pooled_pcp_prefill_projection`](../../layers/core/gdn_attention.md#run_jax_gdn_attention_pooled_pcp_prefill_projection), [`tp_head_geometry`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.tp_head_geometry), [`run_jax_gdn_attention_pooled_pcp_prefill`](../../layers/core/gdn_attention.md#run_jax_gdn_attention_pooled_pcp_prefill), [`_gdn_head_geometry`](../../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._gdn_head_geometry), [`get_kv_cache_spec`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.get_kv_cache_spec), [`local_group_sizes`](../../layers/adapter/gdn_linear.md#GdnInterleavedColumnParallelLinear.local_group_sizes), [`_localize_gdn_state_shapes_for_pcp`](../../platforms/tpu_block_size_utils.md#_localize_gdn_state_shapes_for_pcp), [`replication_factors`](../../layers/adapter/gdn_linear.md#GdnColumnParallelLinear.replication_factors), [`checkpoint_sizes`](../../layers/adapter/gdn_linear.md#GdnColumnParallelLinear.checkpoint_sizes), [`_localize_gdn_mamba_spec_for_pcp`](../../layers/adapter/custom_ops/gdn_attention_op.md#_localize_gdn_mamba_spec_for_pcp), [`get_state_shape`](../../layers/adapter/custom_ops/gdn_attention_op.md#VllmGatedDeltaNetAttention.get_state_shape), [`__init__`](../../layers/adapter/gdn_linear.md#GdnColumnParallelLinear.__init__), [`__init__`](../../layers/adapter/gdn_linear.md#GdnInterleavedColumnParallelLinear.__init__)

## Functions
- <a id="derive_gdn_head_geometry"></a>`derive_gdn_head_geometry(num_kq_heads: int, num_v_heads: int, parallel_size: int)` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/gdn/head_geometry.py#L63) — Derive the native sharding/replication relationship for GDN TP and PCP. — documented in [gated-deltanet-kernels](../../../../../concepts/gated-deltanet-kernels.md)

