---
title: 'Module: csrc/common/contain.cc'
type: catalog
provenance: extracted
module: csrc/common/contain.cc
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  FLAGS_torch_tpu_internal_enable_compilation_container: FLAGS_torch_tpu_internal_enable_compilation_container.
  ScopedMemMeasuringContainer.Impl: torch_tpu/ScopedMemMeasuringContainer#Impl#
  FLAGS_notorch_tpu_internal_enable_compilation_container: FLAGS_notorch_tpu_internal_enable_compilation_container.
  ScopedMemMeasuringContainer.ScopedMemMeasuringContainer: torch_tpu/ScopedMemMeasuringContainer#ScopedMemMeasuringContainer(49f6e7a06ebc5aa8).
  AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container: AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container#
  AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container: AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container#
  CleanUpContainer: torch_tpu/CleanUpContainer(49f6e7a06ebc5aa8).
  ScopedMemMeasuringContainer.-ScopedMemMeasuringContainer: torch_tpu/ScopedMemMeasuringContainer#`~ScopedMemMeasuringContainer`(ced63f7c635d850d).
  ContainerPeakHostMemoryBytes: torch_tpu/ContainerPeakHostMemoryBytes(eab097d057d15b4c).
  AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container.value: AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container#value.
  AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container.Value: AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container#Value(59d317b252f70f25).
  FLAGS_help_storage_torch_tpu_internal_enable_compilation_container: FLAGS_help_storage_torch_tpu_internal_enable_compilation_container.
  AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container.Gen: AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container#Gen(5d22bdacc48458e8).
  AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container.NonConst: AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container#NonConst(efd28698952f529a).
---
# Module: [`csrc/common/contain.cc`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc)

## Classes
### <a id="AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container"></a>`AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container`
- def: [`csrc/common/contain.cc:25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
- signature: `ABSL_FLAG(bool, torch_tpu_internal_enable_compilation_container, false, "Enable usage of gcontain for capturing peak memory during compilation.")`
- members:
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container.Gen"></a>`Gen(bool, torch_tpu_internal_enable_compilation_container, false, "Enable usage of gcontain for capturing peak memory during compilation.")` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_enable_compilation_container.value"></a>`value` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
- used by: [`FLAGS_notorch_tpu_internal_enable_compilation_container`](contain.cc.md#FLAGS_notorch_tpu_internal_enable_compilation_container)

### <a id="AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container"></a>`AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container`
- def: [`csrc/common/contain.cc:25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
- signature: `ABSL_FLAG(bool, torch_tpu_internal_enable_compilation_container, false, "Enable usage of gcontain for capturing peak memory during compilation.")`
- members:
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container.NonConst"></a>`NonConst(bool, torch_tpu_internal_enable_compilation_container, false, "Enable usage of gcontain for capturing peak memory during compilation.")` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_enable_compilation_container.Value"></a>`Value(bool, torch_tpu_internal_enable_compilation_container, false, "Enable usage of gcontain for capturing peak memory during compilation.")` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25) — long enough for NonConst to work correctly.
- used by: [`FLAGS_notorch_tpu_internal_enable_compilation_container`](contain.cc.md#FLAGS_notorch_tpu_internal_enable_compilation_container)

### <a id="ScopedMemMeasuringContainer.Impl"></a>`ScopedMemMeasuringContainer.Impl`
- def: [`csrc/common/contain.cc:31`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L31)
- signature: `struct ScopedMemMeasuringContainer::Impl`
- uses (calls/refs, reference-scoped): [`ScopedMemMeasuringContainer`](contain.h.md#ScopedMemMeasuringContainer)
- used by: [`ScopedMemMeasuringContainer`](contain.cc.md#ScopedMemMeasuringContainer.ScopedMemMeasuringContainer), [`operator=`](contain.h.md#ScopedMemMeasuringContainer.operator)

## Functions
- <a id="CleanUpContainer"></a>`CleanUpContainer()` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L42) — Destroys the container and resets the singleton state. Facilitates
- <a id="ContainerPeakHostMemoryBytes"></a>`ContainerPeakHostMemoryBytes()` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L40) — Returns peak memory usage in bytes inside the container. Work done by any

## Module values
- <a id="FLAGS_help_storage_torch_tpu_internal_enable_compilation_container"></a>`FLAGS_help_storage_torch_tpu_internal_enable_compilation_container` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
- <a id="FLAGS_notorch_tpu_internal_enable_compilation_container"></a>`FLAGS_notorch_tpu_internal_enable_compilation_container` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25)
- <a id="FLAGS_torch_tpu_internal_enable_compilation_container"></a>`FLAGS_torch_tpu_internal_enable_compilation_container` — [`L25`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L25) — second redeclaration is to allow applying attributes

## Other members
- <a id="ScopedMemMeasuringContainer.-ScopedMemMeasuringContainer"></a>`ScopedMemMeasuringContainer.-ScopedMemMeasuringContainer` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L38)
- <a id="ScopedMemMeasuringContainer.ScopedMemMeasuringContainer"></a>`ScopedMemMeasuringContainer.ScopedMemMeasuringContainer` — [`L35`](../../../../../../raw/code/torch_tpu/csrc/common/contain.cc#L35)

