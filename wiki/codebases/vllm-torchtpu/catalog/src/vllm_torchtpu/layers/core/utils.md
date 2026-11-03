---
title: 'Module: src/vllm_torchtpu/layers/core/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.utils`/
symbols:
  reorder_concatenated_tensor_for_sharding: reorder_concatenated_tensor_for_sharding().
  inverse_reorder_for_sharding: inverse_reorder_for_sharding().
  slice_sharded_tensor_for_concatenation: slice_sharded_tensor_for_concatenation().
---
# Module: [`src/vllm_torchtpu/layers/core/utils.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/utils.py)

## Functions
- <a id="inverse_reorder_for_sharding"></a>`inverse_reorder_for_sharding(reordered_tensor: jax.Array, split_sizes: list[int], n_shards: int, dim: int)` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/utils.py#L60) — Inverse of reorder_concatenated_tensor_for_sharding.
- <a id="reorder_concatenated_tensor_for_sharding"></a>`reorder_concatenated_tensor_for_sharding(concatenated_tensor: jax.Array, split_sizes: list[int], n_shards: int, dim: int)` — [`L19`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/utils.py#L19) — Reorder a replicated concatenated tensor such that when sharded on multiple chips,
- <a id="slice_sharded_tensor_for_concatenation"></a>`slice_sharded_tensor_for_concatenation(sharded_tensor: jax.Array, split_sizes: list[int], n_shards: int)` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/utils.py#L92) — Slice the input tensor which is sharded on multiple chips (on the last dim) into

