---
title: 'Module: torchtitan/experiments/tpu/local_tpu_device.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/local_tpu_device.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.local_tpu_device`/
symbols:
  get_chips: get_chips().
  TpuChip: TpuChip#
  TpuChip.from_pci_device_id: TpuChip#from_pci_device_id().
  chip_path: chip_path().
  TpuChip.Info: TpuChip#Info#
  TpuChip.V7X: TpuChip#V7X.
  get_local_chips: get_local_chips().
  ChipInfo.cores: ChipInfo#cores.
  _chip_sort_key: _chip_sort_key().
  TpuChip.V5E: TpuChip#V5E.
  TpuChip.V5P: TpuChip#V5P.
  TpuChip.V6E: TpuChip#V6E.
  ChipInfo: ChipInfo#
  TpuChip.V2: TpuChip#V2.
  TpuChip.V3: TpuChip#V3.
  TpuChip.V4: TpuChip#V4.
  CoreInfo.vfio_path: CoreInfo#vfio_path.
  _identity: _identity().
  GOOGLE_PCI_VENDOR_ID: GOOGLE_PCI_VENDOR_ID.
  _T: _T.
  CoreInfo: CoreInfo#
  nonmember: nonmember.
  CoreInfo.core_index: CoreInfo#core_index.
  CoreInfo.device_id: CoreInfo#device_id.
  CoreInfo.full_addr: CoreInfo#full_addr.
  ChipInfo.base_addr: ChipInfo#base_addr.
  TpuChip.Info.name: TpuChip#Info#name.
  TpuChip.Info.hbm_gib: TpuChip#Info#hbm_gib.
  TpuChip.Info.devices_per_chip: TpuChip#Info#devices_per_chip.
  TpuChip.__str__: TpuChip#__str__().
  get_chip_owners: get_chip_owners().
---
# Module: [`torchtitan/experiments/tpu/local_tpu_device.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py)

## Classes
### <a id="ChipInfo"></a>`ChipInfo`
- def: [`torchtitan/experiments/tpu/local_tpu_device.py:91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L91)
- doc: Information about a TPU chip.
- signature: `class ChipInfo:`
- members:
  - <a id="ChipInfo.base_addr"></a>`base_addr` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L93)
  - <a id="ChipInfo.cores"></a>`cores` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L95)
- uses (calls/refs, reference-scoped): [`CoreInfo`](local_tpu_device.md#CoreInfo)
- used by: [`get_chips`](local_tpu_device.md#get_chips), [`_chip_sort_key`](local_tpu_device.md#_chip_sort_key)

### <a id="CoreInfo"></a>`CoreInfo`
- def: [`torchtitan/experiments/tpu/local_tpu_device.py:82`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L82)
- doc: Information about a TPU core.
- signature: `class CoreInfo:`
- members:
  - <a id="CoreInfo.core_index"></a>`core_index` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L84)
  - <a id="CoreInfo.device_id"></a>`device_id` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L85)
  - <a id="CoreInfo.full_addr"></a>`full_addr` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L87)
  - <a id="CoreInfo.vfio_path"></a>`vfio_path` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L86)
- used by: [`get_chips`](local_tpu_device.md#get_chips), [`_chip_sort_key`](local_tpu_device.md#_chip_sort_key), [`cores`](local_tpu_device.md#ChipInfo.cores)

### <a id="TpuChip"></a>`TpuChip`  ·  implements/extends Enum
- def: [`torchtitan/experiments/tpu/local_tpu_device.py:29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L29)
- doc: TPU chip versions and basic specs.
- signature: `class TpuChip(enum.Enum):`
- members:
  - <a id="TpuChip.__str__"></a>`__str__(self)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L72) — Human-readable name of TPU chip type.
  - <a id="TpuChip.from_pci_device_id"></a>`from_pci_device_id(cls, device_id: str, subsystem_id: str)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L51) — Returns TPU chip type for given PCI IDs, or None if not a TPU device.
  - <a id="TpuChip.V2"></a>`V2` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L42)
  - <a id="TpuChip.V3"></a>`V3` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L43)
  - <a id="TpuChip.V4"></a>`V4` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L44)
  - <a id="TpuChip.V5E"></a>`V5E` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L45)
  - <a id="TpuChip.V5P"></a>`V5P` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L46)
  - <a id="TpuChip.V6E"></a>`V6E` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L47)
  - <a id="TpuChip.V7X"></a>`V7X` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L48)
- uses (calls/refs, reference-scoped): [`Info`](local_tpu_device.md#TpuChip.Info)
- used by: [`_TPU_CHIP_TO_HOST_BOUNDS`](cloud_distributed_utils.md#_TPU_CHIP_TO_HOST_BOUNDS), [`_maybe_init_distributed_on_tpu_vm`](cloud_distributed_utils.md#_maybe_init_distributed_on_tpu_vm), [`chip_path`](local_tpu_device.md#chip_path), [`get_local_chips`](local_tpu_device.md#get_local_chips)  (1 test-only)

### <a id="TpuChip.Info"></a>`TpuChip.Info`  ·  implements/extends Generic
- def: [`torchtitan/experiments/tpu/local_tpu_device.py:35`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L35)
- doc: Specs for a specific TPU chip version.
- signature: `class Info(typing.NamedTuple):`
- members:
  - <a id="TpuChip.Info.devices_per_chip"></a>`devices_per_chip` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L40)
  - <a id="TpuChip.Info.hbm_gib"></a>`hbm_gib` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L39)
  - <a id="TpuChip.Info.name"></a>`name` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L38)
- uses (calls/refs, reference-scoped): [`nonmember`](local_tpu_device.md#nonmember)
- used by: [`V7X`](local_tpu_device.md#TpuChip.V7X), [`V5E`](local_tpu_device.md#TpuChip.V5E), [`V5P`](local_tpu_device.md#TpuChip.V5P), [`V6E`](local_tpu_device.md#TpuChip.V6E), [`V2`](local_tpu_device.md#TpuChip.V2), [`V3`](local_tpu_device.md#TpuChip.V3), [`V4`](local_tpu_device.md#TpuChip.V4)

## Functions
- <a id="_chip_sort_key"></a>`_chip_sort_key(chip: ChipInfo)` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L98) — Returns a sort key for a chip based on zero-indexed core's vfio path.
- <a id="_identity"></a>`_identity(item: _T)` — [`L19`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L19)
- <a id="chip_path"></a>`chip_path(chip_type: TpuChip, index: int)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L199) — Returns the expected `/dev` path for a given TPU device type.
- <a id="get_chip_owners"></a>`get_chip_owners()` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L207) — Returns a mapping of device paths to PIDs of processes using that device.
- <a id="get_chips"></a>`get_chips()` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L116) — Returns the list of information about chips with core information.
- <a id="get_local_chips"></a>`get_local_chips()` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L177) — Returns the type and number of TPU chips available.

## Module values
- <a id="GOOGLE_PCI_VENDOR_ID"></a>`GOOGLE_PCI_VENDOR_ID` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L14)
- <a id="_T"></a>`_T` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L16)
- <a id="nonmember"></a>`nonmember` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/local_tpu_device.py#L25)

