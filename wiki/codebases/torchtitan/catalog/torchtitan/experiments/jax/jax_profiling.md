---
title: 'Module: torchtitan/experiments/jax/jax_profiling.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/jax_profiling.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.jax_profiling`/
symbols:
  maybe_enable_profiling: maybe_enable_profiling().
  maybe_enable_profiling.JaxProfiler.step: maybe_enable_profiling().JaxProfiler#step().
  JaxProfiler.step_num: JaxProfiler#step_num.
  logger: logger.
  ProfilingConfig: ProfilingConfig.
  JaxProfiler.tracing: JaxProfiler#tracing.
  maybe_enable_profiling.JaxProfiler: maybe_enable_profiling().JaxProfiler#
  maybe_enable_profiling.JaxProfiler.__init__: maybe_enable_profiling().JaxProfiler#__init__().
---
# Module: [`torchtitan/experiments/jax/jax_profiling.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py)

## Classes
### <a id="maybe_enable_profiling.JaxProfiler"></a>`maybe_enable_profiling.JaxProfiler`
- def: [`torchtitan/experiments/jax/jax_profiling.py:52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L52)
- doc: Manages periodic JAX trace start/stop within a training loop.
- signature: `class JaxProfiler:`
- members:
  - <a id="maybe_enable_profiling.JaxProfiler.step"></a>`step(self)` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L59) — Advance the profiler by one step, starting or stopping a trace.
- protocol/private: <a id="maybe_enable_profiling.JaxProfiler.__init__"></a>`__init__`[`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L55)
- uses (calls/refs, reference-scoped): [`step_num`](jax_profiling.md#JaxProfiler.step_num), [`logger`](jax_profiling.md#logger), [`tracing`](jax_profiling.md#JaxProfiler.tracing)
- used by: [`train`](trainer.md#JaxTrainer.train), [`maybe_enable_profiling`](jax_profiling.md#maybe_enable_profiling)

## Functions
- <a id="maybe_enable_profiling"></a>`maybe_enable_profiling(profiling_config: ProfilingConfig, *, global_step: int = 0, base_folder: str = "")` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L28) — Context manager to conditionally enable JAX profiling based on config. — documented in [jax-lane](../../../../concepts/jax-lane.md)

## Module values
- <a id="ProfilingConfig"></a>`ProfilingConfig` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L23)
- <a id="logger"></a>`logger` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L24)

## Other members
- <a id="JaxProfiler.step_num"></a>`JaxProfiler.step_num` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L56)
- <a id="JaxProfiler.tracing"></a>`JaxProfiler.tracing` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/jax_profiling.py#L57)

