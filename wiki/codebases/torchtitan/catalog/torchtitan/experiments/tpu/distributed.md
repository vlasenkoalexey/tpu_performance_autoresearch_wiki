---
title: 'Module: torchtitan/experiments/tpu/distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.distributed`/
symbols:
  run_distributed: run_distributed().
  _run_in_gdist_worker: _run_in_gdist_worker().
  _ensure_device_type_set: _ensure_device_type_set().
---
# Module: [`torchtitan/experiments/tpu/distributed.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/distributed.py)

## Functions
- <a id="_ensure_device_type_set"></a>`_ensure_device_type_set(accelerator_device_type: device_type.AcceleratorDeviceType)` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/distributed.py#L20) — Sets the device type for the current process.
- <a id="_run_in_gdist_worker"></a>`_run_in_gdist_worker(accelerator_device_type: device_type.AcceleratorDeviceType, func: Callable[[torch.device, int, int, ...], None], run_init_process_group: bool, *worker_args: Tuple[Any, ...])` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/distributed.py#L47) — Runs a function within a gdist worker process.
- <a id="run_distributed"></a>`run_distributed(num_devices: int, accelerator_device_type: device_type.AcceleratorDeviceType, func: Callable, *worker_args: Any, run_init_process_group: bool = True)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/distributed.py#L120) — Runs a function in a distributed manner across multiple devices. — documented in [tpu-trainer-and-job-config](../../../../concepts/tpu-trainer-and-job-config.md)

