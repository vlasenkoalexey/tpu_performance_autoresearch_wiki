---
title: 'Module: torchtitan/experiments/tpu/jax_profiler.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/jax_profiler.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.jax_profiler`/
symbols:
  JaxProfiler.start: JaxProfiler#start().
  JaxProfiler.prof: JaxProfiler#prof.
  JaxProfiler.stop: JaxProfiler#stop().
  logger: logger.
  JaxProfiler.__init__: JaxProfiler#__init__().
  JaxProfiler: JaxProfiler#
---
# Module: [`torchtitan/experiments/tpu/jax_profiler.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py)

## Classes
### <a id="JaxProfiler"></a>`JaxProfiler`
- def: [`torchtitan/experiments/tpu/jax_profiler.py:14`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L14)
- doc: Wrapper for JAX profiler.
- signature: `class JaxProfiler:`
- members:
  - <a id="JaxProfiler.start"></a>`start(self)` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L20)
  - <a id="JaxProfiler.stop"></a>`stop(self)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L51)
  - <a id="JaxProfiler.prof"></a>`prof` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L18)
- protocol/private: <a id="JaxProfiler.__init__"></a>`__init__`[`L17`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L17)
- uses (calls/refs, reference-scoped): [`Profiler`](../../tools/profiler.md#Profiler), [`save_traces_folder`](../../tools/profiler.md#Profiler.Config.save_traces_folder), [`_base_folder`](../../tools/profiler.md#Profiler._base_folder), [`_config`](../../tools/profiler.md#Profiler._config), [`_leaf_folder`](../../tools/profiler.md#Profiler._leaf_folder), [`logger`](jax_profiler.md#logger)
- used by: [`custom_enter`](profiler_workaround.md#custom_enter)

## Module values
- <a id="logger"></a>`logger` — [`L11`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/jax_profiler.py#L11)

