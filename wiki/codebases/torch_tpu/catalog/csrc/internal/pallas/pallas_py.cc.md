---
title: 'Module: csrc/internal/pallas/pallas_py.cc'
type: catalog
provenance: extracted
module: csrc/internal/pallas/pallas_py.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PyCallCustomKernel: '`$anonymous_namespace_csrc/internal/pallas/pallas_py.cc`/PyCallCustomKernel(e5197ec62aedc840).'
  TorchTpuPyBindInitModule_tpu_torch_pallas: TorchTpuPyBindInitModule_tpu_torch_pallas(d5b68cea704bb038).
  pybind11_exec_tpu_torch_pallas: pybind11_exec_tpu_torch_pallas(6642082b04e1bfd8).
  pybind11_init_tpu_torch_pallas: pybind11_init_tpu_torch_pallas(85901dfccbeca8c6).
  PyLookupCustomKernel: '`$anonymous_namespace_csrc/internal/pallas/pallas_py.cc`/PyLookupCustomKernel(3c7df3f261a805ca).'
  PyRegisterCustomKernel: '`$anonymous_namespace_csrc/internal/pallas/pallas_py.cc`/PyRegisterCustomKernel(7be1541c555edf57).'
---
# Module: [`csrc/internal/pallas/pallas_py.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc)

## Functions
- <a id="PyCallCustomKernel"></a>`PyCallCustomKernel(block_size=128)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L129) — Dispatches a previously registered custom kernel (e.g., Pallas or XLA
- <a id="PyLookupCustomKernel"></a>`PyLookupCustomKernel(c10::string_view name, c10::string_view kernel_key)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L60)
- <a id="PyRegisterCustomKernel"></a>`PyRegisterCustomKernel(c10::string_view name, c10::string_view kernel_key, c10::string_view mlir_module_string)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L49)
- <a id="TorchTpuPyBindInitModule_tpu_torch_pallas"></a>`TorchTpuPyBindInitModule_tpu_torch_pallas(tpu_torch_pallas, m)` — [`L199`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L199)
- <a id="pybind11_exec_tpu_torch_pallas"></a>`pybind11_exec_tpu_torch_pallas(tpu_torch_pallas, m)` — [`L199`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L199)
- <a id="pybind11_init_tpu_torch_pallas"></a>`pybind11_init_tpu_torch_pallas(tpu_torch_pallas, m)` — [`L199`](../../../../../../../raw/code/torch_tpu/csrc/internal/pallas/pallas_py.cc#L199)

