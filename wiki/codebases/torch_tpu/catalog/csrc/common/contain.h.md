---
title: 'Module: csrc/common/contain.h'
type: catalog
provenance: extracted
module: csrc/common/contain.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ScopedMemMeasuringContainer#
symbols:
  ScopedMemMeasuringContainer: ''
  ScopedMemMeasuringContainer.impl_: impl_.
  ScopedMemMeasuringContainer.operator: '`operator=`(195205cd287401f5).'
  ScopedMemMeasuringContainer.ScopedMemMeasuringContainer: ScopedMemMeasuringContainer(5262942d43a75abb).
---
# Module: [`csrc/common/contain.h`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h)

## Classes
### <a id="ScopedMemMeasuringContainer"></a>`ScopedMemMeasuringContainer`
- def: [`csrc/common/contain.h:49`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L49)
- doc: Dynamic container for tracking memory usage.
- signature: `class ScopedMemMeasuringContainer`
- members:
  - <a id="ScopedMemMeasuringContainer.ScopedMemMeasuringContainer"></a>`ScopedMemMeasuringContainer(const ScopedMemMeasuringContainer&)` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L54)
  - `ScopedMemMeasuringContainer(ScopedMemMeasuringContainer&&)` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L57)
  - <a id="ScopedMemMeasuringContainer.operator"></a>`operator=(ScopedMemMeasuringContainer&&)` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L58)
  - `operator=(const ScopedMemMeasuringContainer&)` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L55)
  - <a id="ScopedMemMeasuringContainer.impl_"></a>`impl_` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/contain.h#L63)
- uses (calls/refs, reference-scoped): [`Impl`](contain.cc.md#ScopedMemMeasuringContainer.Impl), [`ScopedMemMeasuringContainer`](contain.cc.md#ScopedMemMeasuringContainer.ScopedMemMeasuringContainer), [`CleanUpContainer`](contain.cc.md#CleanUpContainer), [`~ScopedMemMeasuringContainer`](contain.cc.md#ScopedMemMeasuringContainer.-ScopedMemMeasuringContainer), [`ContainerPeakHostMemoryBytes`](contain.cc.md#ContainerPeakHostMemoryBytes)
- used by: [`InitializeInternal`](../pjrt/pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`EnqueueCompilation`](compilation_cache.cc.md#CompilationCache.EnqueueCompilation), [`EnsureInitialized`](compilation_cache.cc.md#CompilationCache.EnsureInitialized), [`Impl`](contain.cc.md#ScopedMemMeasuringContainer.Impl), [`ScopedMemMeasuringContainer`](contain.cc.md#ScopedMemMeasuringContainer.ScopedMemMeasuringContainer), [`~ScopedMemMeasuringContainer`](contain.cc.md#ScopedMemMeasuringContainer.-ScopedMemMeasuringContainer)

