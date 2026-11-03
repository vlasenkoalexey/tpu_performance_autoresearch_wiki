---
title: 'Module: src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.fused_moe.v2.token_parallel`/
symbols:
  TokenReplicaLayout.split: TokenReplicaLayout#split().
  TokenReplicaLayout.groups: TokenReplicaLayout#groups.
  TokenReplicaLayout.restore: TokenReplicaLayout#restore().
  replica_wire_rows: replica_wire_rows().
  TokenReplicaLayout.local_rows: TokenReplicaLayout#local_rows.
  TokenReplicaLayout: TokenReplicaLayout#
  TokenReplicaLayout.input_rows: TokenReplicaLayout#input_rows.
  TokenReplicaLayout.slots: TokenReplicaLayout#slots.
  TokenReplicaLayout.create: TokenReplicaLayout#create().
---
# Module: [`src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py)

## Classes
### <a id="TokenReplicaLayout"></a>`TokenReplicaLayout`
- def: [`src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py:41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L41)
- doc: Groups are ordered mesh coordinates, independent of expert ownership.
- signature: `class TokenReplicaLayout:`
- members:
  - <a id="TokenReplicaLayout.create"></a>`create(cls, *, ep: int, input_rows: int, groups: tuple[tuple[int, ...], ...] | None = None, row_alignment: int = 1)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L55)
  - <a id="TokenReplicaLayout.restore"></a>`restore(self, rows: jax.Array, axis: str)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L108)
  - <a id="TokenReplicaLayout.split"></a>`split(self, rows: jax.Array, rank: jax.Array, *, fill_value: float = 0)` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L96) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
  - <a id="TokenReplicaLayout.groups"></a>`groups` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L49) — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)
  - <a id="TokenReplicaLayout.input_rows"></a>`input_rows` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L51)
  - <a id="TokenReplicaLayout.local_rows"></a>`local_rows` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L52)
  - <a id="TokenReplicaLayout.slots"></a>`slots` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L50)
- used by: [`compute_local`](layer.md#fused_ep_moe_v2.compute_local), [`fused_ep_moe_v2`](layer.md#fused_ep_moe_v2), [`quantize_local`](layer.md#fused_ep_moe_v2.quantize_local)

## Functions
- <a id="replica_wire_rows"></a>`replica_wire_rows(input_rows, width, row_alignment)` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/fused_moe/v2/token_parallel.py#L24) — An upper bound on `TokenReplicaLayout.local_rows`, in arithmetic alone. — documented in [fused-moe-kernels](../../../../../../concepts/fused-moe-kernels.md)

