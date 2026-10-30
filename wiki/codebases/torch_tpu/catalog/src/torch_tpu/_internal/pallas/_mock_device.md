---
title: 'Module: src/torch_tpu/_internal/pallas/_mock_device.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/pallas/_mock_device.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.pallas._mock_device`/
symbols:
  _PallasDevice.__eq__: _PallasDevice#__eq__().
  _PallasDevice.__repr__: _PallasDevice#__repr__().
  _PallasDevice.__hash__: _PallasDevice#__hash__().
  _PallasDevice.device_kind: _PallasDevice#device_kind.
  _PallasDevice.platform: _PallasDevice#platform.
  _PallasDevice.id: _PallasDevice#id.
  _MOCK_CLIENT: _MOCK_CLIENT.
  _PallasDevice: _PallasDevice#
  _PallasDevice.client: _PallasDevice#client.
  _PallasMockClient: _PallasMockClient#
  _PallasMockClient.platform: _PallasMockClient#platform.
  _PallasMockClient.platform_version: _PallasMockClient#platform_version.
  _PallasMockClient.runtime_type: _PallasMockClient#runtime_type.
  _PallasMockClient.process_index: _PallasMockClient#process_index().
  _PallasMockClient.device_count: _PallasMockClient#device_count().
  _PallasMockClient.devices: _PallasMockClient#devices().
  _PallasMockClient.local_devices: _PallasMockClient#local_devices().
  _PallasDevice.__init__: _PallasDevice#__init__().
  _PallasDevice.num_cores: _PallasDevice#num_cores.
  _PallasDevice.process_index: _PallasDevice#process_index.
---
# Module: [`src/torch_tpu/_internal/pallas/_mock_device.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py)

## Classes
### <a id="_PallasDevice"></a>`_PallasDevice`
- def: [`src/torch_tpu/_internal/pallas/_mock_device.py:46`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L46)
- doc: Compile-only abstract device compatible with JAX mesh/sharding inspection without jax.devices().
- signature: `class _PallasDevice:`
- members:
  - <a id="_PallasDevice.client"></a>`client` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L62)
  - <a id="_PallasDevice.device_kind"></a>`device_kind` — [`L57`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L57)
  - <a id="_PallasDevice.id"></a>`id` — [`L60`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L60)
  - <a id="_PallasDevice.num_cores"></a>`num_cores` — [`L58`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L58)
  - <a id="_PallasDevice.platform"></a>`platform` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L59)
  - <a id="_PallasDevice.process_index"></a>`process_index` — [`L61`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L61)
- protocol/private: <a id="_PallasDevice.__eq__"></a>`__eq__`[`L70`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L70), <a id="_PallasDevice.__hash__"></a>`__hash__`[`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L79), <a id="_PallasDevice.__init__"></a>`__init__`[`L49`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L49), <a id="_PallasDevice.__repr__"></a>`__repr__`[`L64`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L64)
- uses (calls/refs, reference-scoped): [`_MOCK_CLIENT`](_mock_device.md#_MOCK_CLIENT)
- used by: [`_get_pallas_mesh`](pallas.md#_get_pallas_mesh)

### <a id="_PallasMockClient"></a>`_PallasMockClient`
- def: [`src/torch_tpu/_internal/pallas/_mock_device.py:21`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L21)
- doc: Mock PJRT client for abstract compilation devices.
- signature: `class _PallasMockClient:`
- members:
  - <a id="_PallasMockClient.device_count"></a>`device_count(self)` — [`L31`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L31)
  - <a id="_PallasMockClient.devices"></a>`devices(self)` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L36)
  - <a id="_PallasMockClient.local_devices"></a>`local_devices(self)` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L39)
  - <a id="_PallasMockClient.process_index"></a>`process_index(self)` — [`L28`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L28)
  - <a id="_PallasMockClient.platform"></a>`platform` — [`L24`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L24)
  - <a id="_PallasMockClient.platform_version"></a>`platform_version` — [`L25`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L25)
  - <a id="_PallasMockClient.runtime_type"></a>`runtime_type` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L26)
- used by: [`_MOCK_CLIENT`](_mock_device.md#_MOCK_CLIENT)

## Module values
- <a id="_MOCK_CLIENT"></a>`_MOCK_CLIENT` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pallas/_mock_device.py#L43)

