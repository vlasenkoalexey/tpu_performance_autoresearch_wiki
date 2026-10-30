---
title: 'Module: csrc/internal/env.cc'
type: catalog
provenance: extracted
module: csrc/internal/env.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TorchTpuPyBindInitModule_env: TorchTpuPyBindInitModule_env(d5b68cea704bb038).
  PyGetStringEnvOnce: '`$anonymous_namespace_csrc/internal/env.cc`/PyGetStringEnvOnce(547a07ec0ccefeeb).'
  PyGetIntegerEnvOnce: '`$anonymous_namespace_csrc/internal/env.cc`/PyGetIntegerEnvOnce(ab2227fbd85d4734).'
  PyGetBooleanEnvOnce: '`$anonymous_namespace_csrc/internal/env.cc`/PyGetBooleanEnvOnce(c5a27d577270f13b).'
  pybind11_exec_env: pybind11_exec_env(6642082b04e1bfd8).
  pybind11_init_env: pybind11_init_env(85901dfccbeca8c6).
---
# Module: [`csrc/internal/env.cc`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc)

## Functions
- <a id="PyGetBooleanEnvOnce"></a>`PyGetBooleanEnvOnce(std::string_view name, std::optional<bool> default_value)` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L40) — Returns the Boolean value of the environment variable `name`, or
- <a id="PyGetIntegerEnvOnce"></a>`PyGetIntegerEnvOnce(std::string_view name, std::optional<int64_t> default_value)` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L66) — Like PyGetBooleanEnvOnce(), but for integer environment variables.
- <a id="PyGetStringEnvOnce"></a>`PyGetStringEnvOnce(std::string_view name, std::optional<std::string> default_value)` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L100) — Like PyGetBooleanEnvOnce(), but for string environment variables. Unlike the
- <a id="TorchTpuPyBindInitModule_env"></a>`TorchTpuPyBindInitModule_env(env, m)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L132)
- <a id="pybind11_exec_env"></a>`pybind11_exec_env(env, m)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L132)
- <a id="pybind11_init_env"></a>`pybind11_init_env(env, m)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/internal/env.cc#L132)

