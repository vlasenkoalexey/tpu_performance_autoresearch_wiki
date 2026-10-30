---
title: 'Module: torchtitan/experiments/tpu/cloud_distributed_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/cloud_distributed_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.cloud_distributed_utils`/
symbols:
  get_global_node_rank: get_global_node_rank().
  get_slice_id: get_slice_id().
  _maybe_init_distributed_on_gke: _maybe_init_distributed_on_gke().
  get_slice_id_from_worker_hostnames: get_slice_id_from_worker_hostnames().
  _TPU_CHIP_TO_HOST_BOUNDS: _TPU_CHIP_TO_HOST_BOUNDS.
  _maybe_init_distributed_on_tpu_vm: _maybe_init_distributed_on_tpu_vm().
  get_num_slices: get_num_slices().
  maybe_validate_multislice_parallelism: maybe_validate_multislice_parallelism().
  get_nodes_per_slice: get_nodes_per_slice().
  maybe_init_distributed: maybe_init_distributed().
  is_multi_slice: is_multi_slice().
  _POD_INDEX_RE: _POD_INDEX_RE.
---
# Module: [`torchtitan/experiments/tpu/cloud_distributed_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py)

## Functions
- <a id="_maybe_init_distributed_on_gke"></a>`_maybe_init_distributed_on_gke(slicebuilder_first_worker_port: int = 10000, environ: dict[str, str] | None = None)` — [`L260`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L260) — Initializes environment variables for distributed TPU training on GKE.
- <a id="_maybe_init_distributed_on_tpu_vm"></a>`_maybe_init_distributed_on_tpu_vm()` — [`L415`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L415) — Initializes environment variables for distributed TPU training on a TPU VM.
- <a id="get_global_node_rank"></a>`get_global_node_rank(environ: dict[str, str] | None = None)` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L161) — Returns this worker's node rank across the whole job, or None.
- <a id="get_nodes_per_slice"></a>`get_nodes_per_slice(environ: dict[str, str] | None = None)` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L79) — Returns the number of hosts in one slice, or None if GKE has not said.
- <a id="get_num_slices"></a>`get_num_slices(environ: dict[str, str] | None = None)` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L46) — Returns the number of TPU slices this job spans.
- <a id="get_slice_id"></a>`get_slice_id(environ: dict[str, str] | None = None)` — [`L193`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L193) — Returns this process's slice index, 0 on a single-slice job.
- <a id="get_slice_id_from_worker_hostnames"></a>`get_slice_id_from_worker_hostnames(environ: dict[str, str] | None = None)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L108) — Returns this slice's index, read out of ``TPU_WORKER_HOSTNAMES``, or None.
- <a id="is_multi_slice"></a>`is_multi_slice(environ: dict[str, str] | None = None)` — [`L255`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L255) — Whether this job spans more than one TPU slice.
- <a id="maybe_init_distributed"></a>`maybe_init_distributed()` — [`L531`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L531) — Initializes environment variables for distributed TPU training.
- <a id="maybe_validate_multislice_parallelism"></a>`maybe_validate_multislice_parallelism(parallelism_config)` — [`L473`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L473) — Rejects the one multi-slice layout torch_tpu cannot detect.

## Module values
- <a id="_POD_INDEX_RE"></a>`_POD_INDEX_RE` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L28)
- <a id="_TPU_CHIP_TO_HOST_BOUNDS"></a>`_TPU_CHIP_TO_HOST_BOUNDS` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/cloud_distributed_utils.py#L30)

