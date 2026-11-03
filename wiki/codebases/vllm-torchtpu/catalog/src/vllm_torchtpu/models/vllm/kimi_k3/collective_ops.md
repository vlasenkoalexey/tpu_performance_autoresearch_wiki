---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.collective_ops`/
symbols:
  _build_mla_ops: _build_mla_ops().
  _OPS._OPS: _OPS._OPS.
  _build_token_op: _build_token_op().
  _mesh_and_tables: _mesh_and_tables().
  _build_op: _build_op().
  _build_moe_gather_op: _build_moe_gather_op().
  _build_project_op: _build_project_op().
  _build_gather_project_op: _build_gather_project_op().
  FusedPrefillCollectives.mla_ops: FusedPrefillCollectives#mla_ops().
  FusedPrefillCollectives: FusedPrefillCollectives#
  FusedPrefillCollectives.all_gather: FusedPrefillCollectives#all_gather().
  FusedPrefillCollectives.reduce_scatter: FusedPrefillCollectives#reduce_scatter().
  FusedPrefillCollectives.project_reduce_scatter: FusedPrefillCollectives#project_reduce_scatter().
  TokenShardCollectives.ag: TokenShardCollectives#ag.
  TokenShardCollectives.rs: TokenShardCollectives#rs.
  FusedPrefillCollectives.gather_moe_inputs: FusedPrefillCollectives#gather_moe_inputs().
  TokenShardCollectives.all_gather: TokenShardCollectives#all_gather().
  FusedPrefillCollectives.base: FusedPrefillCollectives#base.
  FusedPrefillCollectives.all_reduce: FusedPrefillCollectives#all_reduce().
  TokenShardCollectives: TokenShardCollectives#
  TokenShardCollectives.world_size: TokenShardCollectives#world_size.
  FusedPrefillCollectives.gather_project: FusedPrefillCollectives#gather_project.
  _build_mla_ops.pack: _build_mla_ops().pack().
  _build_mla_ops.preprocess: _build_mla_ops().preprocess().
  _build_moe_gather_op.gather: _build_moe_gather_op().gather().
  _build_op.collective: _build_op().collective().
  _build_project_op.project: _build_project_op().project().
  _build_gather_project_op.project: _build_gather_project_op().project().
  _build_token_op.collective: _build_token_op().collective().
  TokenShardCollectives.reduce_scatter: TokenShardCollectives#reduce_scatter().
  FusedPrefillCollectives.ag: FusedPrefillCollectives#ag.
  FusedPrefillCollectives.rs: FusedPrefillCollectives#rs.
  FusedPrefillCollectives.project_rs: FusedPrefillCollectives#project_rs.
  FusedPrefillCollectives._moe_gather_op: FusedPrefillCollectives#_moe_gather_op.
  _build_mla_ops.fake: _build_mla_ops().fake().
  _build_moe_gather_op.fake: _build_moe_gather_op().fake().
  _build_op.fake: _build_op().fake().
  _build_project_op.fake: _build_project_op().fake().
  _build_gather_project_op.fake: _build_gather_project_op().fake().
  _build_token_op.collective.local: _build_token_op().collective().local().
  _build_token_op.fake: _build_token_op().fake().
  TokenShardCollectives.rank_in_group: TokenShardCollectives#rank_in_group.
  FusedPrefillCollectives.layer: FusedPrefillCollectives#layer.
  TokenShardCollectives.__init__: TokenShardCollectives#__init__().
  FusedPrefillCollectives.__init__: FusedPrefillCollectives#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py)

## Classes
### <a id="FusedPrefillCollectives"></a>`FusedPrefillCollectives`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py:321`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L321) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
- doc: Fused prefill projections and MoE collectives, with standard fallbacks.
- signature: `class FusedPrefillCollectives:`
- members:
  - <a id="FusedPrefillCollectives.all_gather"></a>`all_gather(self, x, dim)` — [`L348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L348) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="FusedPrefillCollectives.all_reduce"></a>`all_reduce(self, x)` — [`L388`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L388)
  - <a id="FusedPrefillCollectives.gather_moe_inputs"></a>`gather_moe_inputs(self, latent, weights, ids, *, num_experts)` — [`L337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L337) — Gather token activations and routes, packing compatible BF16 inputs.
  - <a id="FusedPrefillCollectives.mla_ops"></a>`mla_ops(self, eps)` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L344) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="FusedPrefillCollectives.project_reduce_scatter"></a>`project_reduce_scatter(self, x, projection)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L371) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="FusedPrefillCollectives.reduce_scatter"></a>`reduce_scatter(self, x, dim)` — [`L359`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L359) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="FusedPrefillCollectives.ag"></a>`ag` — [`L331`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L331)
  - <a id="FusedPrefillCollectives.base"></a>`base` — [`L325`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L325)
  - <a id="FusedPrefillCollectives.gather_project"></a>`gather_project` — [`L334`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L334)
  - <a id="FusedPrefillCollectives.layer"></a>`layer` — [`L330`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L330)
  - <a id="FusedPrefillCollectives.project_rs"></a>`project_rs` — [`L333`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L333)
  - <a id="FusedPrefillCollectives.rs"></a>`rs` — [`L332`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L332)
- protocol/private: <a id="FusedPrefillCollectives.__init__"></a>`__init__`[`L324`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L324), <a id="FusedPrefillCollectives._moe_gather_op"></a>`_moe_gather_op`[`L335`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L335)
- uses (calls/refs, reference-scoped): [`_build_mla_ops`](collective_ops.md#_build_mla_ops), [`WEIGHT_FLIPPED_ATTR`](../../../layers/adapter/linear_common.md#WEIGHT_FLIPPED_ATTR), [`_mesh_and_tables`](collective_ops.md#_mesh_and_tables), [`_build_op`](collective_ops.md#_build_op), [`ep_rank_order`](../../../distributed/ep_mesh.md#ep_rank_order), [`_build_gather_project_op`](collective_ops.md#_build_gather_project_op), [`_build_moe_gather_op`](collective_ops.md#_build_moe_gather_op), [`_build_project_op`](collective_ops.md#_build_project_op)
- used by: [`forward`](attention.md#KimiDeltaAttention.forward), [`_forward_expert_parallel`](moe.md#KimiMoE._forward_expert_parallel), [`prefill_group`](attention.md#MultiHeadLatentAttention.prefill_group), [`packed_prefill_weight`](attention.md#KimiDeltaAttention.packed_prefill_weight), [`prepare_sp_mla_gate`](attention.md#MultiHeadLatentAttention.prepare_sp_mla_gate), [`shared_group`](moe.md#KimiMoE.shared_group), [`forward`](attention.md#MultiHeadLatentAttention.forward), [`prefill_group`](attention.md#KimiDeltaAttention.prefill_group)

### <a id="TokenShardCollectives"></a>`TokenShardCollectives`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py:303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L303)
- doc: Gather/scatter token shards over TP2 or TP32 without concrete allocations.
- signature: `class TokenShardCollectives:`
- members:
  - <a id="TokenShardCollectives.all_gather"></a>`all_gather(self, x, dim)` — [`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L312)
  - <a id="TokenShardCollectives.reduce_scatter"></a>`reduce_scatter(self, x, dim)` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L316)
  - <a id="TokenShardCollectives.ag"></a>`ag` — [`L309`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L309)
  - <a id="TokenShardCollectives.rank_in_group"></a>`rank_in_group` — [`L308`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L308)
  - <a id="TokenShardCollectives.rs"></a>`rs` — [`L310`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L310)
  - <a id="TokenShardCollectives.world_size"></a>`world_size` — [`L307`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L307)
- protocol/private: <a id="TokenShardCollectives.__init__"></a>`__init__`[`L306`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L306)
- uses (calls/refs, reference-scoped): [`_build_token_op`](collective_ops.md#_build_token_op)
- used by: [`forward`](model.md#KimiModel.forward), [`forward`](layers.md#KimiMLP.forward), [`sp_group`](model.md#KimiModel.sp_group), [`sp_group`](layers.md#KimiMLP.sp_group)

## Functions
- <a id="_build_gather_project_op"></a>`_build_gather_project_op(mesh, tables, collective_id)` — [`L212`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L212)
- <a id="_build_mla_ops"></a>`_build_mla_ops(mesh, owners, layer, eps)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L42) — documented in [distributed-parallelism-and-meshes](../../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_build_moe_gather_op"></a>`_build_moe_gather_op(mesh, tables, collective_id)` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L103)
- <a id="_build_op"></a>`_build_op(mesh, tables, gather, collective_id)` — [`L138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L138) — documented in [distributed-parallelism-and-meshes](../../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_build_project_op"></a>`_build_project_op(mesh, tables, collective_id)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L175)
- <a id="_build_token_op"></a>`_build_token_op(world_size, gather)` — [`L259`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L259) — documented in [distributed-parallelism-and-meshes](../../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_mesh_and_tables"></a>`_mesh_and_tables()` — [`L247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L247) — documented in [distributed-parallelism-and-meshes](../../../../../../concepts/distributed-parallelism-and-meshes.md)
- <a id="_build_op.collective"></a>`collective(x: jax.Array)` — [`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L148)
- <a id="_build_token_op.collective"></a>`collective(x: jax.Array)` — [`L269`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L269)
- <a id="_build_mla_ops.fake"></a>`fake(x, weight, packed_gate, qnorm, kvnorm, sequence_parallel)` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L94)
- <a id="_build_moe_gather_op.fake"></a>`fake(x, weights, ids)` — [`L128`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L128)
- <a id="_build_op.fake"></a>`fake(x)` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L166)
- <a id="_build_project_op.fake"></a>`fake(x, w)` — [`L202`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L202)
- <a id="_build_gather_project_op.fake"></a>`fake(x, w)` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L236)
- <a id="_build_token_op.fake"></a>`fake(x)` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L295)
- <a id="_build_moe_gather_op.gather"></a>`gather(x: jax.Array, weights: jax.Array, ids: jax.Array)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L113)
- <a id="_build_token_op.collective.local"></a>`local(part)` — [`L270`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L270)
- <a id="_build_mla_ops.pack"></a>`pack(weight: jax.Array)` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L54)
- <a id="_build_mla_ops.preprocess"></a>`preprocess(x: jax.Array, weight: jax.Array, packed_gate: jax.Array, qnorm: jax.Array, kvnorm: jax.Array, sequence_parallel: bool)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L66)
- <a id="_build_project_op.project"></a>`project(x: jax.Array, w: jax.Array)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L185)
- <a id="_build_gather_project_op.project"></a>`project(x: jax.Array, w: jax.Array)` — [`L222`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L222)

## Module values
- <a id="_OPS._OPS"></a>`_OPS` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/collective_ops.py#L39)

