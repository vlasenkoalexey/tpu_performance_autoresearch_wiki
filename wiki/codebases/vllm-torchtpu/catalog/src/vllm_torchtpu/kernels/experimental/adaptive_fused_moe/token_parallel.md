---
title: 'Module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.adaptive_fused_moe.token_parallel`/TokenReplicaLayout#
symbols:
  TokenReplicaLayout.split: split().
  TokenReplicaLayout.restore: restore().
  TokenReplicaLayout.groups: groups.
  TokenReplicaLayout.local_rows: local_rows.
  TokenReplicaLayout: ''
  TokenReplicaLayout.input_rows: input_rows.
  TokenReplicaLayout.slots: slots.
  TokenReplicaLayout.create: create().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py)

## Classes
### <a id="TokenReplicaLayout"></a>`TokenReplicaLayout`
- def: [`src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py:25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L25)
- doc: Groups are ordered mesh coordinates, independent of expert ownership.
- signature: `class TokenReplicaLayout:`
- members:
  - <a id="TokenReplicaLayout.create"></a>`create(cls, *, ep: int, input_rows: int, groups: tuple[tuple[int, ...], ...] | None = None, row_alignment: int = 1)` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L39)
  - <a id="TokenReplicaLayout.restore"></a>`restore(self, rows: jax.Array, axis: str)` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L92)
  - <a id="TokenReplicaLayout.split"></a>`split(self, rows: jax.Array, rank: jax.Array, *, fill_value: float = 0)` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L80) — documented in [adaptive-fused-moe-kernel](../../../../../../concepts/adaptive-fused-moe-kernel.md)
  - <a id="TokenReplicaLayout.groups"></a>`groups` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L33)
  - <a id="TokenReplicaLayout.input_rows"></a>`input_rows` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L35)
  - <a id="TokenReplicaLayout.local_rows"></a>`local_rows` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L36)
  - <a id="TokenReplicaLayout.slots"></a>`slots` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/adaptive_fused_moe/token_parallel.py#L34)
- used by: [`local_fn`](layer.md#adaptive_fused_moe.local_fn), [`adaptive_fused_moe`](layer.md#adaptive_fused_moe)

