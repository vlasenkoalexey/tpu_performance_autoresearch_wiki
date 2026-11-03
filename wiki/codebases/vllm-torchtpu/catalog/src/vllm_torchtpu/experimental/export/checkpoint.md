---
title: 'Module: src/vllm_torchtpu/experimental/export/checkpoint.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/checkpoint.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.checkpoint`/
symbols:
  run_cpu_load_worker: run_cpu_load_worker().
  save_model_checkpoint: save_model_checkpoint().
  iter_checkpoint_shards: iter_checkpoint_shards().
  _save_checkpoint: _save_checkpoint().
  check_replicas: check_replicas().
  _has_replicas: _has_replicas().
  launch_cpu_workers: launch_cpu_workers().
  export_checkpoint: export_checkpoint().
  _AXIS_NAMES: _AXIS_NAMES.
  local_tensors: local_tensors().
  init_jax: init_jax().
  JAX_COORDINATOR_FLAG: JAX_COORDINATOR_FLAG.
  CHECKPOINT_DATA_DIR: CHECKPOINT_DATA_DIR.
  host_tensors: host_tensors().
  save_checkpoint: save_checkpoint().
  checkpoint_shards: checkpoint_shards().
  DATA_DIR_FLAG: DATA_DIR_FLAG.
  _sharded_axes: _sharded_axes().
  CPU_ENV: CPU_ENV.
  abstract_params_inputs: abstract_params_inputs().
  mesh_axis_sizes: mesh_axis_sizes().
  shard_shape: shard_shape().
  to_numpy: to_numpy().
---
# Module: [`src/vllm_torchtpu/experimental/export/checkpoint.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py)

## Functions
- <a id="_has_replicas"></a>`_has_replicas(spec: Mapping[str, Any], axis_sizes: Mapping[str, int])` — [`L246`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L246) — Whether more than one process holds a copy of the same shard of `spec`.
- <a id="_save_checkpoint"></a>`_save_checkpoint(inputs: Sequence[Mapping[str, Any]], shards: Iterable[Any], axis_sizes: Mapping[str, int], data_dir: str)` — [`L196`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L196)
- <a id="_sharded_axes"></a>`_sharded_axes(spec: Mapping[str, Any])` — [`L238`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L238)
- <a id="abstract_params_inputs"></a>`abstract_params_inputs(artifact_dir: str)` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L57) — The `abstract_params` inputs of the artifact, in argument order.
- <a id="check_replicas"></a>`check_replicas(inputs: Sequence[Mapping[str, Any]], digests: Any, axis_sizes: Mapping[str, int])` — [`L252`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L252) — Fails if processes holding copies of one shard saved different values.
- <a id="checkpoint_shards"></a>`checkpoint_shards(inputs: Sequence[Mapping[str, Any]], tensors: Mapping[str, Any], axis_sizes: Mapping[str, int])` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L164) — This rank's shard of every `abstract_params` input (`iter_checkpoint_shards`).
- <a id="export_checkpoint"></a>`export_checkpoint(argv: Sequence[str], tp_size: int, output_dir: str)` — [`L387`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L387) — `checkpoint` mode: fills the existing artifact in `output_dir` on CPU.
- <a id="host_tensors"></a>`host_tensors(model: Any)` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L97) — CPU copies of `local_tensors(model)`; tied names keep sharing one copy.
- <a id="init_jax"></a>`init_jax(rank: int, world_size: int, coordinator: str | None)` — [`L290`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L290) — Joins this rank to the launcher's JAX distributed runtime at `coordinator`.
- <a id="iter_checkpoint_shards"></a>`iter_checkpoint_shards(inputs: Sequence[Mapping[str, Any]], tensors: Mapping[str, Any], axis_sizes: Mapping[str, int])` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L127) — Yields this rank's shard of every `abstract_params` input as a numpy array.
- <a id="launch_cpu_workers"></a>`launch_cpu_workers(argv: Sequence[str], tp_size: int, worker_flag: str)` — [`L355`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L355) — Runs `python -m vllm_torchtpu.experimental.export` once per rank on CPU.
- <a id="local_tensors"></a>`local_tensors(model: Any)` — [`L84`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L84) — The model's parameters and buffers by name.
- <a id="mesh_axis_sizes"></a>`mesh_axis_sizes(artifact_dir: str)` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L65) — Size of each mesh axis of the artifact.
- <a id="run_cpu_load_worker"></a>`run_cpu_load_worker(args: argparse.Namespace)` — [`L318`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L318) — `checkpoint` mode: loads this rank's weights on CPU and saves its shards.
- <a id="save_checkpoint"></a>`save_checkpoint(inputs: Sequence[Mapping[str, Any]], shards: Iterable[Any], axis_sizes: Mapping[str, int], data_dir: str)` — [`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L173) — Saves the global arrays assembled from every process's `shards` with Orbax.
- <a id="save_model_checkpoint"></a>`save_model_checkpoint(tensors: Mapping[str, Any], artifact_dir: str, data_dir: str)` — [`L308`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L308) — Saves this rank's `tensors`, by name, for the artifact in `artifact_dir`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="shard_shape"></a>`shard_shape(spec: Mapping[str, Any], axis_sizes: Mapping[str, int])` — [`L72`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L72) — Shape of one device's shard of the global tensor `spec`.
- <a id="to_numpy"></a>`to_numpy(tensor: Any)` — [`L110`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L110) — A CPU numpy view of `tensor`, with `ml_dtypes` types for bf16 and FP8.

## Module values
- <a id="CHECKPOINT_DATA_DIR"></a>`CHECKPOINT_DATA_DIR` — [`L54`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L54)
- <a id="CPU_ENV"></a>`CPU_ENV` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L46)
- <a id="DATA_DIR_FLAG"></a>`DATA_DIR_FLAG` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L51)
- <a id="JAX_COORDINATOR_FLAG"></a>`JAX_COORDINATOR_FLAG` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L50)
- <a id="_AXIS_NAMES"></a>`_AXIS_NAMES` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/checkpoint.py#L52)

