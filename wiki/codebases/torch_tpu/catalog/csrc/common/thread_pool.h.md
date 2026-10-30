---
title: 'Module: csrc/common/thread_pool.h'
type: catalog
provenance: extracted
module: csrc/common/thread_pool.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ThreadPool#
symbols:
  ThreadPool: ''
  ThreadPool.Schedule: Schedule(fe7a8a4d1eddb70).
  ThreadPool.NumThreads: NumThreads(455f465bc33b4cdf).
  ThreadPool.pool_: pool_.
  ThreadPool.ThreadPool: ThreadPool(4aa74c421218e55).
  ThreadPool.operator: '`operator=`(9c3f56cc15443660).'
---
# Module: [`csrc/common/thread_pool.h`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h)

## Classes
### <a id="ThreadPool"></a>`ThreadPool`
- def: [`csrc/common/thread_pool.h:26`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L26)
- signature: `class ThreadPool`
- members:
  - <a id="ThreadPool.NumThreads"></a>`NumThreads()` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L50)
  - <a id="ThreadPool.Schedule"></a>`Schedule(F&& f)` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L44) — Schedules f() for execution in the pool of threads. Function object f
  - <a id="ThreadPool.ThreadPool"></a>`ThreadPool(ThreadPool&&)` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L38)
  - `ThreadPool(const ThreadPool&)` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L36) — This class is neither copyable nor movable.
  - <a id="ThreadPool.operator"></a>`operator=(ThreadPool&&)` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L39)
  - `operator=(const ThreadPool&)` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L37)
  - <a id="ThreadPool.pool_"></a>`pool_` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/common/thread_pool.h#L53)
- uses (calls/refs, reference-scoped): [`ThreadPool`](thread_pool.cc.md#ThreadPool.ThreadPool)
- used by: [`GetFromTier3OrCompile`](compilation_cache.cc.md#CompilationCache.GetFromTier3OrCompile), [`cache_mutex_`](compilation_cache.h.md#CompilationCache.cache_mutex_), [`ScheduleAsyncAssertionCheck`](../ops/assertion_aten_kernels.cc.md#ScheduleAsyncAssertionCheck), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`EnsureInitialized`](compilation_cache.cc.md#CompilationCache.EnsureInitialized), [`ThreadPool`](thread_pool.cc.md#ThreadPool.ThreadPool), [`compilation_pool_`](compilation_cache.h.md#CompilationCache.compilation_pool_), [`GetAssertionThreadPool`](../ops/assertion_aten_kernels.cc.md#GetAssertionThreadPool)

