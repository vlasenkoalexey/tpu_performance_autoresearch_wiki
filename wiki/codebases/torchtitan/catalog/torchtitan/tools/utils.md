---
title: 'Module: torchtitan/tools/utils.py'
type: catalog
provenance: extracted
module: torchtitan/tools/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.tools.utils`/
symbols:
  device_type: device_type.
  device_module: device_module.
  has_cuda_capability: has_cuda_capability().
  _patch_tpu_device_module: _patch_tpu_device_module().
  _patch_cpu_device_module: _patch_cpu_device_module().
  get_local_device: get_local_device().
  GarbageCollection: GarbageCollection#
  GarbageCollection.collect: GarbageCollection#collect().
  GarbageCollection.run: GarbageCollection#run().
  get_peak_flops: get_peak_flops().
  Color: Color#
  set_default_dtype: set_default_dtype().
  get_cuda_flash_attention_impl: get_cuda_flash_attention_impl().
  NoColor: NoColor#
  NoColor.turquoise: NoColor#turquoise.
  get_device_info: get_device_info().
  GarbageCollection.debug: GarbageCollection#debug.
  has_rocm_capability: has_rocm_capability().
  Color.red: Color#red.
  NoColor.green: NoColor#green.
  NoColor.blue: NoColor#blue.
  NoColor.reset: NoColor#reset.
  _TpuDeviceModule.__getattr__: _TpuDeviceModule#__getattr__().
  check_if_feature_in_pytorch: check_if_feature_in_pytorch().
  round_up: round_up().
  _TpuDeviceModule: _TpuDeviceModule#
  Color.reset: Color#reset.
  NoColor.red: NoColor#red.
  NoColor.yellow: NoColor#yellow.
  NoColor.magenta: NoColor#magenta.
  NoColor.cyan: NoColor#cyan.
  NoColor.orange: NoColor#orange.
  _patch_cpu_device_module.get_device_name: _patch_cpu_device_module().get_device_name().
  _patch_cpu_device_module.current_device: _patch_cpu_device_module().current_device().
  _patch_cpu_device_module.get_device_properties: _patch_cpu_device_module().get_device_properties().
  _patch_cpu_device_module.reset_peak_memory_stats: _patch_cpu_device_module().reset_peak_memory_stats().
  _patch_cpu_device_module.empty_cache: _patch_cpu_device_module().empty_cache().
  _patch_cpu_device_module.memory_stats: _patch_cpu_device_module().memory_stats().
  _use_accelerator_device_apis: _use_accelerator_device_apis().
  _TpuDeviceModule._tpu_module: _TpuDeviceModule#_tpu_module.
  _patch_tpu_device_module.reset_peak_memory_stats: _patch_tpu_device_module().reset_peak_memory_stats().
  _patch_tpu_device_module.empty_cache: _patch_tpu_device_module().empty_cache().
  _patch_tpu_device_module.memory_stats: _patch_tpu_device_module().memory_stats().
  _patch_tpu_device_module.is_triton_capable: _patch_tpu_device_module().is_triton_capable().
  GarbageCollection.gc_freq: GarbageCollection#gc_freq.
  Color.yellow: Color#yellow.
  _TpuDeviceModule.__init__: _TpuDeviceModule#__init__().
  _TpuDeviceModule.is_available: _TpuDeviceModule#is_available().
  _TpuDeviceModule.device_count: _TpuDeviceModule#device_count().
  _TpuDeviceModule.current_device: _TpuDeviceModule#current_device().
  _TpuDeviceModule.set_device: _TpuDeviceModule#set_device().
  _TpuDeviceModule.synchronize: _TpuDeviceModule#synchronize().
  _TpuDeviceModule.current_stream: _TpuDeviceModule#current_stream().
  _TpuDeviceModule.set_stream: _TpuDeviceModule#set_stream().
  GarbageCollection.__init__: GarbageCollection#__init__().
  Color.black: Color#black.
  Color.green: Color#green.
  Color.blue: Color#blue.
  Color.magenta: Color#magenta.
  Color.cyan: Color#cyan.
  Color.white: Color#white.
  Color.orange: Color#orange.
  Color.turquoise: Color#turquoise.
  NoColor.black: NoColor#black.
  NoColor.white: NoColor#white.
---
# Module: [`torchtitan/tools/utils.py`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py)

## Classes
### <a id="Color"></a>`Color`
- def: [`torchtitan/tools/utils.py:456`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L456) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- signature: `class Color:`
- members:
  - <a id="Color.black"></a>`black` — [`L457`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L457)
  - <a id="Color.blue"></a>`blue` — [`L461`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L461)
  - <a id="Color.cyan"></a>`cyan` — [`L463`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L463)
  - <a id="Color.green"></a>`green` — [`L459`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L459)
  - <a id="Color.magenta"></a>`magenta` — [`L462`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L462)
  - <a id="Color.orange"></a>`orange` — [`L466`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L466)
  - <a id="Color.red"></a>`red` — [`L458`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L458)
  - <a id="Color.reset"></a>`reset` — [`L465`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L465)
  - <a id="Color.turquoise"></a>`turquoise` — [`L467`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L467)
  - <a id="Color.white"></a>`white` — [`L464`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L464)
  - <a id="Color.yellow"></a>`yellow` — [`L460`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L460)
- used by: [`__init__`](../components/metrics.md#MetricsProcessor.__init__), [`log_to_console`](../experiments/rl/observability/metrics/console.md#log_to_console), [`ensure_pp_loss_visible`](../components/metrics.md#ensure_pp_loss_visible), [`color`](../components/metrics.md#MetricsProcessor.color), [`turquoise`](utils.md#NoColor.turquoise), [`color`](../experiments/jax/metrics.md#JaxMetricsProcessor.color), [`_COLOR_CYCLE`](../experiments/rl/observability/metrics/console.md#_COLOR_CYCLE)

### <a id="GarbageCollection"></a>`GarbageCollection`
- def: [`torchtitan/tools/utils.py:270`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L270) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- signature: `class GarbageCollection:`
- members:
  - <a id="GarbageCollection.collect"></a>`collect(reason: str, generation: int = 1)` — [`L301`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L301) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="GarbageCollection.run"></a>`run(self, step_count: int)` — [`L284`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L284) — Run a GC cycle if this step should collect. Returns True when a — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="GarbageCollection.debug"></a>`debug` — [`L274`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L274)
  - <a id="GarbageCollection.gc_freq"></a>`gc_freq` — [`L273`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L273)
- protocol/private: <a id="GarbageCollection.__init__"></a>`__init__`[`L271`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L271)
- uses (calls/refs, reference-scoped): [`logger`](logging.md#logger), [`log_trace_span`](../observability/structured_logger/structured_logging.md#log_trace_span), [`add_step_tag`](../observability/structured_logger/step_state.md#add_step_tag)
- used by: [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`train`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`train`](../trainer.md#Trainer.train), [`_save`](../components/checkpointer/dcp.md#CheckpointManager._save), [`load`](../components/checkpointer/base.md#BaseCheckpointManager.load), [`_save_last_step`](../components/checkpointer/torch_checkpointing.md#TorchCheckpointingManager._save_last_step), [`dcp_save`](../components/checkpointer/dcp.md#CheckpointManager.dcp_save), [`_ft_load`](../experiments/torchft/checkpoint.md#TorchFTCheckpointManager._ft_load), [`gc_handler`](../trainer.md#Trainer.gc_handler)

### <a id="NoColor"></a>`NoColor`
- def: [`torchtitan/tools/utils.py:471`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L471) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- signature: `class NoColor:`
- members:
  - <a id="NoColor.black"></a>`black` — [`L472`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L472)
  - <a id="NoColor.blue"></a>`blue` — [`L476`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L476)
  - <a id="NoColor.cyan"></a>`cyan` — [`L478`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L478)
  - <a id="NoColor.green"></a>`green` — [`L474`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L474)
  - <a id="NoColor.magenta"></a>`magenta` — [`L477`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L477)
  - <a id="NoColor.orange"></a>`orange` — [`L481`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L481)
  - <a id="NoColor.red"></a>`red` — [`L473`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L473)
  - <a id="NoColor.reset"></a>`reset` — [`L480`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L480)
  - <a id="NoColor.turquoise"></a>`turquoise` — [`L482`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L482) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="NoColor.white"></a>`white` — [`L479`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L479)
  - <a id="NoColor.yellow"></a>`yellow` — [`L475`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L475)
- uses (calls/refs, reference-scoped): [`Color`](utils.md#Color)
- used by: [`log`](../components/metrics.md#MetricsProcessor.log), [`__init__`](../components/metrics.md#MetricsProcessor.__init__), [`log_validation`](../components/metrics.md#MetricsProcessor.log_validation), [`_log_summary`](../experiments/jax/metrics.md#JaxMetricsProcessor._log_summary), [`log_to_console`](../experiments/rl/observability/metrics/console.md#log_to_console), [`ensure_pp_loss_visible`](../components/metrics.md#ensure_pp_loss_visible), [`color`](../components/metrics.md#MetricsProcessor.color), [`color`](../experiments/jax/metrics.md#JaxMetricsProcessor.color)

### <a id="_TpuDeviceModule"></a>`_TpuDeviceModule`  ·  implements/extends ModuleType
- def: [`torchtitan/tools/utils.py:103`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L103)
- doc: `torch.tpu` as torchtitan calls it, with torch.accelerator-backed APIs.
- signature: `class _TpuDeviceModule(ModuleType):`
- members:
  - <a id="_TpuDeviceModule.current_device"></a>`current_device()` — [`L134`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L134)
  - <a id="_TpuDeviceModule.current_stream"></a>`current_stream(device: int | str | torch.device | None = None)` — [`L156`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L156)
  - <a id="_TpuDeviceModule.device_count"></a>`device_count()` — [`L130`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L130)
  - <a id="_TpuDeviceModule.is_available"></a>`is_available()` — [`L126`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L126)
  - <a id="_TpuDeviceModule.set_device"></a>`set_device(device: int | str | torch.device)` — [`L138`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L138)
  - <a id="_TpuDeviceModule.set_stream"></a>`set_stream(stream)` — [`L160`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L160)
  - <a id="_TpuDeviceModule.synchronize"></a>`synchronize(device: int | str | torch.device | None = None)` — [`L152`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L152)
- protocol/private: <a id="_TpuDeviceModule.__getattr__"></a>`__getattr__`[`L122`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L122), <a id="_TpuDeviceModule.__init__"></a>`__init__`[`L118`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L118), <a id="_TpuDeviceModule._tpu_module"></a>`_tpu_module`[`L120`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L120)
- used by: [`_patch_tpu_device_module`](utils.md#_patch_tpu_device_module)  (1 test-only)

## Functions
- <a id="_patch_cpu_device_module"></a>`_patch_cpu_device_module(device_module: ModuleType)` — [`L59`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L59) — Adds the device-module functions torch.cpu does not provide. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="_patch_tpu_device_module"></a>`_patch_tpu_device_module(device_module: ModuleType)` — [`L164`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L164) — Adds the device-module functions torch_tpu does not provide. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="_use_accelerator_device_apis"></a>`_use_accelerator_device_apis()` — [`L91`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L91) — Whether torch.accelerator provides the device APIs _TpuDeviceModule calls.
- <a id="check_if_feature_in_pytorch"></a>`check_if_feature_in_pytorch(feature_name: str, pull_request: str, min_nightly_version: str | None = None)` — [`L490`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L490) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="_patch_cpu_device_module.current_device"></a>`current_device()` — [`L65`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L65)
- <a id="_patch_cpu_device_module.empty_cache"></a>`empty_cache()` — [`L77`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L77)
- <a id="_patch_tpu_device_module.empty_cache"></a>`empty_cache()` — [`L180`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L180)
- <a id="get_cuda_flash_attention_impl"></a>`get_cuda_flash_attention_impl()` — [`L38`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L38) — Return the FlashAttention implementation for the current CUDA architecture. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="get_device_info"></a>`get_device_info()` — [`L206`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L206) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="_patch_cpu_device_module.get_device_name"></a>`get_device_name(device=None)` — [`L62`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L62)
- <a id="_patch_cpu_device_module.get_device_properties"></a>`get_device_properties(device=None)` — [`L71`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L71)
- <a id="get_local_device"></a>`get_local_device()` — [`L222`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L222) — Return this process's device under LOCAL_RANK or visible-device launch. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="get_peak_flops"></a>`get_peak_flops(device_name: str)` — [`L309`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L309) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="has_cuda_capability"></a>`has_cuda_capability(major: int, minor: int)` — [`L29`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L29) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="has_rocm_capability"></a>`has_rocm_capability(major: int, minor: int)` — [`L51`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L51)
- <a id="_patch_tpu_device_module.is_triton_capable"></a>`is_triton_capable(*args, **kwargs)` — [`L193`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L193)
- <a id="_patch_cpu_device_module.memory_stats"></a>`memory_stats(device=None)` — [`L80`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L80)
- <a id="_patch_tpu_device_module.memory_stats"></a>`memory_stats(device=None)` — [`L183`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L183)
- <a id="_patch_cpu_device_module.reset_peak_memory_stats"></a>`reset_peak_memory_stats(device=None)` — [`L74`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L74)
- <a id="_patch_tpu_device_module.reset_peak_memory_stats"></a>`reset_peak_memory_stats(device=None)` — [`L177`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L177)
- <a id="round_up"></a>`round_up(value: int, multiple: int)` — [`L25`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L25)
- <a id="set_default_dtype"></a>`set_default_dtype(dtype: torch.dtype)` — [`L510`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L510) — Context manager to set torch's default dtype. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)

## Module values
- <a id="device_module"></a>`device_module` — [`L219`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L219) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- <a id="device_type"></a>`device_type` — [`L219`](../../../../../../raw/code/torchtitan/torchtitan/tools/utils.py#L219) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)

