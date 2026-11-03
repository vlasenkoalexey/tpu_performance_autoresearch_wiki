---
title: 'Module: src/vllm_torchtpu/experimental/export/trace.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/trace.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.trace`/
symbols:
  trace: trace#
  trace.__call__: trace#__call__().
  trace.__enter__: trace#__enter__().
  trace.name: trace#name.
  trace.__exit__: trace#__exit__().
  _emit: _emit().
  _pid: _pid().
  _F: _F.
  _HOST: _HOST.
  trace.__init__: trace#__init__().
---
# Module: [`src/vllm_torchtpu/experimental/export/trace.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py)

## Classes
### <a id="trace"></a>`trace`  ·  implements/extends ContextDecorator
- def: [`src/vllm_torchtpu/experimental/export/trace.py:50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L50) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: Logs a span around a block (`with trace("x"):`) or a function (`@trace()`).
- signature: `class trace(contextlib.ContextDecorator):`
- members:
  - <a id="trace.name"></a>`name` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L61)
- protocol/private: <a id="trace.__call__"></a>`__call__`[`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L63), <a id="trace.__enter__"></a>`__enter__`[`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L68), <a id="trace.__exit__"></a>`__exit__`[`L74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L74), <a id="trace.__init__"></a>`__init__`[`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L58)
- uses (calls/refs, reference-scoped): [`_emit`](trace.md#_emit), [`_F`](trace.md#_F)
- used by: [`build_export_config_from_vllm`](universal_adapter.md#build_export_config_from_vllm), [`export`](exporter.md#export), [`run_export_from_args`](cli.md#run_export_from_args), [`_params_read_by_forward`](exporter.md#_params_read_by_forward), [`fit_num_blocks_to_hbm`](universal_adapter.md#UniversalVllmExportableLLM.fit_num_blocks_to_hbm), [`lower_torch_callable_to_mlir`](tpu_lowering.md#lower_torch_callable_to_mlir), [`save_model_checkpoint`](checkpoint.md#save_model_checkpoint), [`_launch_workers`](cli.md#_launch_workers), [`create_export_vllm_config`](universal_adapter.md#create_export_vllm_config), [`run_model_loader`](universal_adapter.md#run_model_loader)

## Functions
- <a id="_emit"></a>`_emit(kind: str, name: str)` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L42)
- <a id="_pid"></a>`_pid()` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L36)

## Module values
- <a id="_F"></a>`_F` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L32)
- <a id="_HOST"></a>`_HOST` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/trace.py#L33)

