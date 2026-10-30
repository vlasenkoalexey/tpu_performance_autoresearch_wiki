---
title: 'Module: src/torch_tpu/_internal/utils/hardware.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/utils/hardware.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.utils.hardware`/
symbols:
  TpuVersion: TpuVersion#
  _HBM_BYTES_PER_CHIP._HBM_BYTES_PER_CHIP: _HBM_BYTES_PER_CHIP._HBM_BYTES_PER_CHIP.
  _BF16_FLOPS_PER_CHIP._BF16_FLOPS_PER_CHIP: _BF16_FLOPS_PER_CHIP._BF16_FLOPS_PER_CHIP.
  _TOPOLOGY_BY_TPU_PCI_DEVICE_ID._TOPOLOGY_BY_TPU_PCI_DEVICE_ID: _TOPOLOGY_BY_TPU_PCI_DEVICE_ID._TOPOLOGY_BY_TPU_PCI_DEVICE_ID.
  get_tpu_version: get_tpu_version().
  get_devices_per_chip: get_devices_per_chip().
  _DEVICES_PER_CHIP._DEVICES_PER_CHIP: _DEVICES_PER_CHIP._DEVICES_PER_CHIP.
  get_hbm_bytes_per_device: get_hbm_bytes_per_device().
  get_bf16_flops_per_device: get_bf16_flops_per_device().
  _scan_pci_tpus: _scan_pci_tpus().
  get_tpu_device_name: get_tpu_device_name().
  get_hbm_bytes_per_chip: get_hbm_bytes_per_chip().
  get_bf16_flops_per_chip: get_bf16_flops_per_chip().
  TpuVersion.V7: TpuVersion#V7.
  get_tpu_device_count: get_tpu_device_count().
  get_tpu_topology: get_tpu_topology().
  has_nvidia_gpu: has_nvidia_gpu().
  TpuVersion.V4: TpuVersion#V4.
  TpuVersion.V5P: TpuVersion#V5P.
  TpuVersion.V5E: TpuVersion#V5E.
  TpuVersion.V6E: TpuVersion#V6E.
  TpuVersion.UNKNOWN: TpuVersion#UNKNOWN.
  _GOOGLE_PCI_VENDOR_ID._GOOGLE_PCI_VENDOR_ID: _GOOGLE_PCI_VENDOR_ID._GOOGLE_PCI_VENDOR_ID.
  _PCI_DEVICE_ID_TO_NAME._PCI_DEVICE_ID_TO_NAME: _PCI_DEVICE_ID_TO_NAME._PCI_DEVICE_ID_TO_NAME.
  _V4_TOPOLOGY._V4_TOPOLOGY: _V4_TOPOLOGY._V4_TOPOLOGY.
  _V5P_TOPOLOGY._V5P_TOPOLOGY: _V5P_TOPOLOGY._V5P_TOPOLOGY.
  _V5E_TOPOLOGY._V5E_TOPOLOGY: _V5E_TOPOLOGY._V5E_TOPOLOGY.
  _V6E_TOPOLOGY._V6E_TOPOLOGY: _V6E_TOPOLOGY._V6E_TOPOLOGY.
  _V7_TOPOLOGY._V7_TOPOLOGY: _V7_TOPOLOGY._V7_TOPOLOGY.
  _NVIDIA_GPU_DEVICES._NVIDIA_GPU_DEVICES: _NVIDIA_GPU_DEVICES._NVIDIA_GPU_DEVICES.
---
# Module: [`src/torch_tpu/_internal/utils/hardware.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py)

## Classes
### <a id="TpuVersion"></a>`TpuVersion`  ·  implements/extends Enum
- def: [`src/torch_tpu/_internal/utils/hardware.py:109`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L109) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- signature: `class TpuVersion(enum.Enum):`
- members:
  - <a id="TpuVersion.UNKNOWN"></a>`UNKNOWN` — [`L116`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L116)
  - <a id="TpuVersion.V4"></a>`V4` — [`L110`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L110)
  - <a id="TpuVersion.V5E"></a>`V5E` — [`L112`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L112)
  - <a id="TpuVersion.V5P"></a>`V5P` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L111)
  - <a id="TpuVersion.V6E"></a>`V6E` — [`L113`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L113)
  - <a id="TpuVersion.V7"></a>`V7` — [`L114`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L114)
- used by: [`_BF16_FLOPS_PER_CHIP`](hardware.md#_BF16_FLOPS_PER_CHIP._BF16_FLOPS_PER_CHIP), [`_HBM_BYTES_PER_CHIP`](hardware.md#_HBM_BYTES_PER_CHIP._HBM_BYTES_PER_CHIP), [`get_tpu_version`](hardware.md#get_tpu_version), [`get_devices_per_chip`](hardware.md#get_devices_per_chip), [`_DEVICES_PER_CHIP`](hardware.md#_DEVICES_PER_CHIP._DEVICES_PER_CHIP)

## Functions
- <a id="_scan_pci_tpus"></a>`_scan_pci_tpus()` — [`L280`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L280) — Scans PCI bus for TPU devices. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_bf16_flops_per_chip"></a>`get_bf16_flops_per_chip()` — [`L232`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L232) — Peak dense bf16 compute per chip, in FLOP/s, for the attached TPU. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_bf16_flops_per_device"></a>`get_bf16_flops_per_device()` — [`L261`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L261) — Peak dense bf16 compute, in FLOP/s, for a single device. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_devices_per_chip"></a>`get_devices_per_chip()` — [`L216`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L216) — Number of separately-addressable devices the attached chip exposes. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_hbm_bytes_per_chip"></a>`get_hbm_bytes_per_chip()` — [`L176`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L176) — Physical HBM capacity per chip, in bytes, for the attached TPU.
- <a id="get_hbm_bytes_per_device"></a>`get_hbm_bytes_per_device()` — [`L242`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L242) — Physical HBM capacity, in bytes, visible to a single device. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_tpu_device_count"></a>`get_tpu_device_count()` — [`L322`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L322) — Returns the number of TPU devices found on the system.
- <a id="get_tpu_device_name"></a>`get_tpu_device_name()` — [`L119`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L119) — Returns a human-readable name for the attached TPU device. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="get_tpu_topology"></a>`get_tpu_topology(world_size: int | None = None)` — [`L332`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L332) — Returns the topology string and device count for attached TPU devices.
- <a id="get_tpu_version"></a>`get_tpu_version()` — [`L147`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L147) — Returns the TpuVersion enum of the attached TPU device. — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="has_nvidia_gpu"></a>`has_nvidia_gpu()` — [`L359`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L359) — True if there's a visible nvidia gpu available on device, False otherwise.

## Module values
- <a id="_BF16_FLOPS_PER_CHIP._BF16_FLOPS_PER_CHIP"></a>`_BF16_FLOPS_PER_CHIP` — [`L205`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L205) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_DEVICES_PER_CHIP._DEVICES_PER_CHIP"></a>`_DEVICES_PER_CHIP` — [`L195`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L195) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_GOOGLE_PCI_VENDOR_ID._GOOGLE_PCI_VENDOR_ID"></a>`_GOOGLE_PCI_VENDOR_ID` — [`L33`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L33)
- <a id="_HBM_BYTES_PER_CHIP._HBM_BYTES_PER_CHIP"></a>`_HBM_BYTES_PER_CHIP` — [`L165`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L165) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_NVIDIA_GPU_DEVICES._NVIDIA_GPU_DEVICES"></a>`_NVIDIA_GPU_DEVICES` — [`L102`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L102)
- <a id="_PCI_DEVICE_ID_TO_NAME._PCI_DEVICE_ID_TO_NAME"></a>`_PCI_DEVICE_ID_TO_NAME` — [`L92`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L92)
- <a id="_TOPOLOGY_BY_TPU_PCI_DEVICE_ID._TOPOLOGY_BY_TPU_PCI_DEVICE_ID"></a>`_TOPOLOGY_BY_TPU_PCI_DEVICE_ID` — [`L81`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L81) — documented in [hardware-introspection](../../../../../concepts/hardware-introspection.md)
- <a id="_V4_TOPOLOGY._V4_TOPOLOGY"></a>`_V4_TOPOLOGY` — [`L38`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L38)
- <a id="_V5E_TOPOLOGY._V5E_TOPOLOGY"></a>`_V5E_TOPOLOGY` — [`L52`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L52)
- <a id="_V5P_TOPOLOGY._V5P_TOPOLOGY"></a>`_V5P_TOPOLOGY` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L45)
- <a id="_V6E_TOPOLOGY._V6E_TOPOLOGY"></a>`_V6E_TOPOLOGY` — [`L66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L66)
- <a id="_V7_TOPOLOGY._V7_TOPOLOGY"></a>`_V7_TOPOLOGY` — [`L72`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/utils/hardware.py#L72)

