---
title: 'Module: torchtitan/experiments/jax/distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.distributed`/
symbols:
  _match_path: _match_path().
  apply_sharding_to_state.shard_leaf: apply_sharding_to_state().shard_leaf().
  shard_input: shard_input().
  sharded_device_put: sharded_device_put().
  _process_sharding_name: _process_sharding_name().
  logger: logger.
  apply_sharding_to_state: apply_sharding_to_state().
  P: P.
  _is_integer: _is_integer().
---
# Module: [`torchtitan/experiments/jax/distributed.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py)

## Functions
- <a id="_is_integer"></a>`_is_integer(token: str)` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L55)
- <a id="_match_path"></a>`_match_path(path_str: str, sharding_map: dict)` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L79) — Return the partition spec for ``path_str`` from ``sharding_map``. — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="_process_sharding_name"></a>`_process_sharding_name(name: str)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L63) — Replace integer path segments with '*'.
- <a id="apply_sharding_to_state"></a>`apply_sharding_to_state(state: nnx.State, sharding_map: dict, mesh: jax.sharding.Mesh)` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L103) — Apply JAX sharding to every leaf in an NNX state pytree. — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="shard_input"></a>`shard_input(x, mesh: jax.sharding.Mesh, num_global_devices: int, num_local_devices: int)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L165) — Shard a batch input tensor across the FSDP axis (batch dimension). — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="apply_sharding_to_state.shard_leaf"></a>`shard_leaf(path, array)` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L117) — documented in [jax-lane](../../../../concepts/jax-lane.md)
- <a id="sharded_device_put"></a>`sharded_device_put(array, sharding, num_global_devices: int, num_local_devices: int)` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L25) — Place an array (or tuple of arrays) on devices with the given sharding. — documented in [jax-lane](../../../../concepts/jax-lane.md)

## Module values
- <a id="P"></a>`P` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L22)
- <a id="logger"></a>`logger` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/distributed.py#L20)

