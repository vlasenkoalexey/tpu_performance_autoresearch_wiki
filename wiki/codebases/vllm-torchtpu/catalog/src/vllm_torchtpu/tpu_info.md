---
title: 'Module: src/vllm_torchtpu/tpu_info.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/tpu_info.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.tpu_info`/
symbols:
  get_libtpu_cache_key: get_libtpu_cache_key().
  get_tpu_metadata: get_tpu_metadata().
  get_chip_version: get_chip_version().
  get_tpu_type: get_tpu_type().
  get_tpu_library_path: get_tpu_library_path().
  get_num_chips: get_num_chips().
  logger: logger.
  get_node_name: get_node_name().
  get_node_worker_id: get_node_worker_id().
  get_num_cores_per_chip: get_num_cores_per_chip().
  get_libtpu_version: get_libtpu_version().
  GCE_TPU_ACCELERATOR_ENDPOINT: GCE_TPU_ACCELERATOR_ENDPOINT.
  GCE_TPU_HEADERS: GCE_TPU_HEADERS.
  _pip_libtpu_library_path: _pip_libtpu_library_path().
  _libtpu_file_fingerprint: _libtpu_file_fingerprint().
---
# Module: [`src/vllm_torchtpu/tpu_info.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py)

## Functions
- <a id="_libtpu_file_fingerprint"></a>`_libtpu_file_fingerprint(path: str, size: int, mtime_ns: int)` — [`L138`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L138)
- <a id="_pip_libtpu_library_path"></a>`_pip_libtpu_library_path()` — [`L103`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L103) — ``libtpu.so`` shipped by the pip ``libtpu`` package, if installed.
- <a id="get_chip_version"></a>`get_chip_version(accelerator_type: str | None = None)` — [`L65`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L65) — Resolves the TPU chip version without initializing a TPU client. — documented in [model-export-and-rust-launcher](../../../concepts/model-export-and-rust-launcher.md)
- <a id="get_libtpu_cache_key"></a>`get_libtpu_cache_key()` — [`L153`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L153) — Identify the libtpu build in use, for compilation and layout cache keys. — documented in [compilation-and-graph-capture](../../../concepts/compilation-and-graph-capture.md)
- <a id="get_libtpu_version"></a>`get_libtpu_version()` — [`L90`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L90) — Version of the pip ``libtpu`` package, or None if it is not installed.
- <a id="get_node_name"></a>`get_node_name()` — [`L172`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L172)
- <a id="get_node_worker_id"></a>`get_node_worker_id()` — [`L179`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L179) — For multi-host TPU VM, this returns the worker id for the current node.
- <a id="get_num_chips"></a>`get_num_chips()` — [`L196`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L196)
- <a id="get_num_cores_per_chip"></a>`get_num_cores_per_chip()` — [`L189`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L189)
- <a id="get_tpu_library_path"></a>`get_tpu_library_path()` — [`L115`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L115) — Custom ``libtpu.so`` from ``TPU_LIBRARY_PATH``, if one is in use.
- <a id="get_tpu_metadata"></a>`get_tpu_metadata(key: str = "")` — [`L35`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L35)
- <a id="get_tpu_type"></a>`get_tpu_type()` — [`L57`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L57)

## Module values
- <a id="GCE_TPU_ACCELERATOR_ENDPOINT"></a>`GCE_TPU_ACCELERATOR_ENDPOINT` — [`L29`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L29)
- <a id="GCE_TPU_HEADERS"></a>`GCE_TPU_HEADERS` — [`L32`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L32)
- <a id="logger"></a>`logger` — [`L27`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/tpu_info.py#L27)

