---
title: 'Module: torchtitan/experiments/tpu/accelerator_device_type.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/accelerator_device_type.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.accelerator_device_type`/AcceleratorDeviceType#
symbols:
  AcceleratorDeviceType: ''
  AcceleratorDeviceType.CPU: CPU.
  AcceleratorDeviceType.TPU: TPU.
  AcceleratorDeviceType.CUDA: CUDA.
---
# Module: [`torchtitan/experiments/tpu/accelerator_device_type.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/accelerator_device_type.py)

## Classes
### <a id="AcceleratorDeviceType"></a>`AcceleratorDeviceType`  ·  implements/extends Enum
- def: [`torchtitan/experiments/tpu/accelerator_device_type.py:10`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/accelerator_device_type.py#L10)
- doc: Accelerator device type.
- signature: `class AcceleratorDeviceType(enum.Enum):`
- members:
  - <a id="AcceleratorDeviceType.CPU"></a>`CPU` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/accelerator_device_type.py#L14)
  - <a id="AcceleratorDeviceType.CUDA"></a>`CUDA` — [`L13`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/accelerator_device_type.py#L13)
  - <a id="AcceleratorDeviceType.TPU"></a>`TPU` — [`L12`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/accelerator_device_type.py#L12)
- used by: [`accelerator_device`](base_device_test.md#BaseAcceleratorDeviceTest.accelerator_device), [`accelerator_device_type`](base_distributed_device_test.md#BaseDistributedDeviceTest.accelerator_device_type), [`_test_train_distributed`](base_distributed_device_test.md#BaseDistributedDeviceTest._test_train_distributed), [`run_distributed`](distributed.md#run_distributed), [`accelerator_device_type`](base_device_test.md#BaseAcceleratorDeviceTest.accelerator_device_type), [`_run_trainer_distributed_parity_test`](base_distributed_device_test.md#BaseDistributedDeviceTest._run_trainer_distributed_parity_test), [`_run_in_gdist_worker`](distributed.md#_run_in_gdist_worker), [`_ensure_device_type_set`](distributed.md#_ensure_device_type_set)  (18 test-only)

