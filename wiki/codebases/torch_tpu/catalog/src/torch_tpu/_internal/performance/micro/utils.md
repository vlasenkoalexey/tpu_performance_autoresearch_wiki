---
title: 'Module: src/torch_tpu/_internal/performance/micro/utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/performance/micro/utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.performance.micro.utils`/
symbols:
  run_model_cpu_acc: run_model_cpu_acc().
  _get_device: _get_device().
  _ACC: _ACC.
  _run_and_time_model: _run_and_time_model().
---
# Module: [`src/torch_tpu/_internal/performance/micro/utils.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/utils.py)

## Functions
- <a id="_get_device"></a>`_get_device()` — [`L32`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/utils.py#L32) — Initialize and return the accelerator runtime.
- <a id="_run_and_time_model"></a>`_run_and_time_model(model: torch.nn.Module = None, input_tensor: torch.Tensor | None = None, warmup: int = 1, iterations: int = 1)` — [`L43`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/utils.py#L43) — Run and time the model.
- <a id="run_model_cpu_acc"></a>`run_model_cpu_acc(cfg, model: torch.nn.Module, input_tensor: torch.Tensor, warmup: int = 1, iterations: int = 10, desc: str | None = None)` — [`L74`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/utils.py#L74) — Run the model on CPU and accelerator device.

## Module values
- <a id="_ACC"></a>`_ACC` — [`L23`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/utils.py#L23)

