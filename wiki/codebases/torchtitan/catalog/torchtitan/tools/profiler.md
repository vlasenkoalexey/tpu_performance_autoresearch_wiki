---
title: 'Module: torchtitan/tools/profiler.py'
type: catalog
provenance: extracted
module: torchtitan/tools/profiler.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.tools.profiler`/
symbols:
  Profiler: Profiler#
  Profiler.build_torch_profiler: Profiler#build_torch_profiler().
  MemoryProfiler.step: MemoryProfiler#step().
  Profiler.Config: Profiler#Config#
  Profiler.Config.profile_freq: Profiler#Config#profile_freq.
  Profiler.__enter__: Profiler#__enter__().
  Profiler.build_memory_profiler: Profiler#build_memory_profiler().
  Profiler.Config.enable_profiling: Profiler#Config#enable_profiling.
  Profiler.step: Profiler#step().
  Profiler.Config.profiler_warmup: Profiler#Config#profiler_warmup.
  Profiler.trace_handler: Profiler#trace_handler().
  Profiler.Config.profiler_active: Profiler#Config#profiler_active.
  Profiler.memory_profiler: Profiler#memory_profiler.
  Profiler.__exit__: Profiler#__exit__().
  Profiler.Config.__post_init__: Profiler#Config#__post_init__().
  Profiler.active: Profiler#active().
  Profiler.Config.save_traces_folder: Profiler#Config#save_traces_folder.
  Profiler.torch_profiler: Profiler#torch_profiler.
  Profiler._global_step: Profiler#_global_step.
  Profiler._config: Profiler#_config.
  Profiler._base_folder: Profiler#_base_folder.
  Profiler._leaf_folder: Profiler#_leaf_folder.
  Profiler.__init__: Profiler#__init__().
  MemoryProfiler.step_num: MemoryProfiler#step_num.
  Profiler.Config.save_memory_snapshot_folder: Profiler#Config#save_memory_snapshot_folder.
  _EXPORT_SUPPORTS_ANNOTATIONS: _EXPORT_SUPPORTS_ANNOTATIONS.
  MemoryProfiler.__init__: MemoryProfiler#__init__().
  Profiler.Config.memory_snapshot_freq: Profiler#Config#memory_snapshot_freq.
  PROFILE_DIR: PROFILE_DIR.
  PROFILE_ITER_DIR: PROFILE_ITER_DIR.
  PROFILE_FILE: PROFILE_FILE.
  MEMORY_DIR: MEMORY_DIR.
  MEMORY_STEP_DIR: MEMORY_STEP_DIR.
  MEMORY_EXIT_DIR: MEMORY_EXIT_DIR.
  MEMORY_FILE: MEMORY_FILE.
  MemoryProfiler: MemoryProfiler#
  MemoryProfiler.freq: MemoryProfiler#freq.
  MemoryProfiler._snapshot_dir: MemoryProfiler#_snapshot_dir.
  MemoryProfiler._leaf_folder: MemoryProfiler#_leaf_folder.
  MemoryProfiler._rank: MemoryProfiler#_rank.
  Profiler.Config.profiler_repeat: Profiler#Config#profiler_repeat.
  Profiler.Config.profiler_skip_first: Profiler#Config#profiler_skip_first.
  Profiler.Config.profiler_skip_first_wait: Profiler#Config#profiler_skip_first_wait.
  Profiler.Config.enable_memory_snapshot: Profiler#Config#enable_memory_snapshot.
  Profiler.Config.memory_snapshot_max_entries: Profiler#Config#memory_snapshot_max_entries.
  Profiler.caused_by_oom: Profiler#caused_by_oom().
---
# Module: [`torchtitan/tools/profiler.py`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py)

## Classes
### <a id="MemoryProfiler"></a>`MemoryProfiler`
- def: [`torchtitan/tools/profiler.py:45`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L45)
- doc: Records periodic memory snapshots during training.
- signature: `class MemoryProfiler:`
- members:
  - <a id="MemoryProfiler.step"></a>`step(self, exit_ctx: bool = False)` — [`L77`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L77) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="MemoryProfiler.freq"></a>`freq` — [`L72`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L72)
  - <a id="MemoryProfiler.step_num"></a>`step_num` — [`L71`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L71)
- protocol/private: <a id="MemoryProfiler.__init__"></a>`__init__`[`L53`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L53), <a id="MemoryProfiler._leaf_folder"></a>`_leaf_folder`[`L74`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L74), <a id="MemoryProfiler._rank"></a>`_rank`[`L75`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L75), <a id="MemoryProfiler._snapshot_dir"></a>`_snapshot_dir`[`L73`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L73)
- uses (calls/refs, reference-scoped): [`logger`](logging.md#logger), [`device_module`](utils.md#device_module), [`MEMORY_EXIT_DIR`](profiler.md#MEMORY_EXIT_DIR), [`MEMORY_FILE`](profiler.md#MEMORY_FILE), [`MEMORY_STEP_DIR`](profiler.md#MEMORY_STEP_DIR)
- used by: [`build_memory_profiler`](profiler.md#Profiler.build_memory_profiler), [`custom_step`](../experiments/tpu/profiler_workaround.md#custom_step), [`step`](profiler.md#Profiler.step), [`__exit__`](profiler.md#Profiler.__exit__), [`custom_exit`](../experiments/tpu/profiler_workaround.md#custom_exit)

### <a id="Profiler"></a>`Profiler`  ·  implements/extends Configurable
- def: [`torchtitan/tools/profiler.py:106`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L106) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- doc: Owns profiling and memory snapshot lifecycle for a training run.
- signature: `class Profiler(Configurable):`
- members:
  - <a id="Profiler.active"></a>`active(self, *, global_step: int = 0, base_folder: str = "", leaf_folder: str = "")` — [`L217`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L217) — Update runtime args and return self for use as a context manager. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.build_memory_profiler"></a>`build_memory_profiler(self, *, global_step: int, base_folder: str, leaf_folder: str)` — [`L388`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L388) — Create and return a :class:`MemoryProfiler`, or ``None`` if disabled. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.build_torch_profiler"></a>`build_torch_profiler(self, *, global_step: int, base_folder: str, leaf_folder: str)` — [`L286`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L286) — Create, start, and return the torch profiler, or ``None`` if disabled. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.caused_by_oom"></a>`caused_by_oom(exc: BaseException | None)` — [`L253`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L253) — Whether an OutOfMemoryError appears anywhere in the cause chain.
  - <a id="Profiler.step"></a>`step(self)` — [`L276`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L276) — Advance all active profilers by one training step. — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.trace_handler"></a>`trace_handler(prof)` — [`L311`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L311) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.memory_profiler"></a>`memory_profiler` — [`L215`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L215) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.torch_profiler"></a>`torch_profiler` — [`L214`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L214) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- protocol/private: <a id="Profiler.__enter__"></a>`__enter__`[`L239`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L239), <a id="Profiler.__exit__"></a>`__exit__`[`L252`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L252), <a id="Profiler.__init__"></a>`__init__`[`L202`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L202), <a id="Profiler._base_folder"></a>`_base_folder`[`L212`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L212), <a id="Profiler._config"></a>`_config`[`L210`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L210), <a id="Profiler._global_step"></a>`_global_step`[`L211`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L211), <a id="Profiler._leaf_folder"></a>`_leaf_folder`[`L213`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L213)
- uses (calls/refs, reference-scoped): [`logger`](logging.md#logger), [`Configurable`](../config/configurable.md#Configurable), [`log_trace_span`](../observability/structured_logger/structured_logging.md#log_trace_span), [`device_type`](utils.md#device_type), [`Config`](profiler.md#Profiler.Config), [`step`](profiler.md#MemoryProfiler.step), [`profile_freq`](profiler.md#Profiler.Config.profile_freq), [`enable_profiling`](profiler.md#Profiler.Config.enable_profiling), [`profiler_warmup`](profiler.md#Profiler.Config.profiler_warmup), [`profiler_active`](profiler.md#Profiler.Config.profiler_active), [`get_cudagraph_annotations`](../distributed/cudagraph.md#get_cudagraph_annotations), [`save_traces_folder`](profiler.md#Profiler.Config.save_traces_folder), [`save_memory_snapshot_folder`](profiler.md#Profiler.Config.save_memory_snapshot_folder), [`_EXPORT_SUPPORTS_ANNOTATIONS`](profiler.md#_EXPORT_SUPPORTS_ANNOTATIONS), [`memory_snapshot_freq`](profiler.md#Profiler.Config.memory_snapshot_freq), [`MemoryProfiler`](profiler.md#MemoryProfiler), [`PROFILE_FILE`](profiler.md#PROFILE_FILE), [`PROFILE_ITER_DIR`](profiler.md#PROFILE_ITER_DIR), [`enable_memory_snapshot`](profiler.md#Profiler.Config.enable_memory_snapshot), [`memory_snapshot_max_entries`](profiler.md#Profiler.Config.memory_snapshot_max_entries), [`profiler_repeat`](profiler.md#Profiler.Config.profiler_repeat), [`profiler_skip_first`](profiler.md#Profiler.Config.profiler_skip_first), [`profiler_skip_first_wait`](profiler.md#Profiler.Config.profiler_skip_first_wait)
- used by: [`Configurable`](../config/configurable.md#Configurable), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`transformers_modeling_backend_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full), [`transformers_modeling_backend_full_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full_moe), [`train`](../experiments/tpu/train_minimal.md#TrainerMinimal.train), [`custom_enter`](../experiments/tpu/profiler_workaround.md#custom_enter), [`qwen3_moe_30b_fsdp_only_full_ac_profile`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_profile), [`profiler`](../trainer.md#Trainer.Config.profiler), [`custom_step`](../experiments/tpu/profiler_workaround.md#custom_step), [`start`](../experiments/tpu/jax_profiler.md#JaxProfiler.start), [`custom_exit`](../experiments/tpu/profiler_workaround.md#custom_exit), [`custom_init`](../experiments/tpu/profiler_workaround.md#custom_init), [`_original_enter`](../experiments/tpu/profiler_workaround.md#_original_enter), [`ProfilingConfig`](../experiments/jax/jax_profiling.md#ProfilingConfig), [`_original_exit`](../experiments/tpu/profiler_workaround.md#_original_exit), [`_original_init`](../experiments/tpu/profiler_workaround.md#_original_init), [`_original_step`](../experiments/tpu/profiler_workaround.md#_original_step), [`profiler`](../experiments/rl/actors/generator.md#VLLMGenerator.Config.profiler), [`profiler`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.profiler), [`__init__`](../experiments/tpu/jax_profiler.md#JaxProfiler.__init__)  (2 test-only)

### <a id="Profiler.Config"></a>`Profiler.Config`  ·  implements/extends Config
- def: [`torchtitan/tools/profiler.py:129`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L129) — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Profiler.Config.enable_memory_snapshot"></a>`enable_memory_snapshot` — [`L174`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L174) — ---
  - <a id="Profiler.Config.enable_profiling"></a>`enable_profiling` — [`L130`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L130) — --- — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.Config.memory_snapshot_freq"></a>`memory_snapshot_freq` — [`L177`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L177) — ---
  - <a id="Profiler.Config.memory_snapshot_max_entries"></a>`memory_snapshot_max_entries` — [`L186`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L186) — ---
  - <a id="Profiler.Config.profile_freq"></a>`profile_freq` — [`L136`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L136) — --- — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.Config.profiler_active"></a>`profiler_active` — [`L160`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L160) — --- — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.Config.profiler_repeat"></a>`profiler_repeat` — [`L139`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L139) — ---
  - <a id="Profiler.Config.profiler_skip_first"></a>`profiler_skip_first` — [`L146`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L146) — ---
  - <a id="Profiler.Config.profiler_skip_first_wait"></a>`profiler_skip_first_wait` — [`L153`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L153) — ---
  - <a id="Profiler.Config.profiler_warmup"></a>`profiler_warmup` — [`L167`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L167) — --- — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
  - <a id="Profiler.Config.save_memory_snapshot_folder"></a>`save_memory_snapshot_folder` — [`L183`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L183) — ---
  - <a id="Profiler.Config.save_traces_folder"></a>`save_traces_folder` — [`L133`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L133) — --- — documented in [debug-and-profiling-tools](../../../concepts/debug-and-profiling-tools.md)
- protocol/private: <a id="Profiler.Config.__post_init__"></a>`__post_init__`[`L193`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L193)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config), [`MEMORY_DIR`](profiler.md#MEMORY_DIR), [`PROFILE_DIR`](profiler.md#PROFILE_DIR)
- used by: [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`transformers_modeling_backend_debugmodel`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`transformers_modeling_backend_full`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full), [`transformers_modeling_backend_full_moe`](../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full_moe), [`_multi_node`](../experiments/tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`custom_enter`](../experiments/tpu/profiler_workaround.md#custom_enter), [`build_torch_profiler`](profiler.md#Profiler.build_torch_profiler), [`qwen3_moe_30b_fsdp_only_full_ac_profile`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_profile), [`profiler`](../trainer.md#Trainer.Config.profiler), [`maybe_enable_profiling`](../experiments/jax/jax_profiling.md#maybe_enable_profiling), [`build_memory_profiler`](profiler.md#Profiler.build_memory_profiler), [`custom_step`](../experiments/tpu/profiler_workaround.md#custom_step), [`start`](../experiments/tpu/jax_profiler.md#JaxProfiler.start), [`ProfilingConfig`](../experiments/jax/jax_profiling.md#ProfilingConfig), [`profiler`](../experiments/rl/actors/generator.md#VLLMGenerator.Config.profiler), [`profiler`](../experiments/rl/actors/trainer.md#PolicyTrainer.Config.profiler), [`__init__`](profiler.md#Profiler.__init__)  (3 test-only)

## Module values
- <a id="MEMORY_DIR"></a>`MEMORY_DIR` — [`L35`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L35)
- <a id="MEMORY_EXIT_DIR"></a>`MEMORY_EXIT_DIR` — [`L39`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L39)
- <a id="MEMORY_FILE"></a>`MEMORY_FILE` — [`L40`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L40)
- <a id="MEMORY_STEP_DIR"></a>`MEMORY_STEP_DIR` — [`L38`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L38)
- <a id="PROFILE_DIR"></a>`PROFILE_DIR` — [`L31`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L31)
- <a id="PROFILE_FILE"></a>`PROFILE_FILE` — [`L33`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L33)
- <a id="PROFILE_ITER_DIR"></a>`PROFILE_ITER_DIR` — [`L32`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L32)
- <a id="_EXPORT_SUPPORTS_ANNOTATIONS"></a>`_EXPORT_SUPPORTS_ANNOTATIONS` — [`L25`](../../../../../../raw/code/torchtitan/torchtitan/tools/profiler.py#L25)

