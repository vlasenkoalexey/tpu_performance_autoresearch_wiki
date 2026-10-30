---
title: 'Module: torchtitan/distributed/context_parallel/api.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/context_parallel/api.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.context_parallel.api`/
symbols:
  prepare_context_parallel_input: prepare_context_parallel_input().
  _cp_shard_dims: _cp_shard_dims().
  cp_shard: cp_shard().
---
# Module: [`torchtitan/distributed/context_parallel/api.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/context_parallel/api.py)

## Functions
- <a id="_cp_shard_dims"></a>`_cp_shard_dims(input_sharding: dict[str, SpmdType])` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/context_parallel/api.py#L25) — Derive ``{name: seq_dim}`` for inputs whose CP mesh axis is a Shard.
- <a id="cp_shard"></a>`cp_shard(cp_mesh: DeviceMesh, inputs: tuple[torch.Tensor, ...], attention_masks: AttentionMasksType | None, load_balancer_type: str | None = "headtail", input_seq_dims: int | tuple[int, ...] = 0, ptrr_mask_key: str | None = None)` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/context_parallel/api.py#L110) — Shard inputs and attention masks across the context parallel mesh.
- <a id="prepare_context_parallel_input"></a>`prepare_context_parallel_input(input_dict: dict[str, Any], input_shardings: dict[str, SpmdType] | None, cp_mesh: DeviceMesh, load_balancer_type: str | None = "headtail", ptrr_mask_key: str | None = None)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/context_parallel/api.py#L39) — Shard named tensors and attention masks for Context Parallel.

