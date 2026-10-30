---
title: 'Module: csrc/eager/eager_mode.cc'
type: catalog
provenance: extracted
module: csrc/eager/eager_mode.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetEagerMode: GetEagerMode(72e64654b4e721f3).
  SetEagerMode: SetEagerMode(5ca8227ae1906c8).
  GetDefaultEagerMode: GetDefaultEagerMode(72e64654b4e721f3).
  IsInplaceBufferDonationEnabled: IsInplaceBufferDonationEnabled(c9857a73d68e59ba).
  EnableInplaceBufferDonation: EnableInplaceBufferDonation(b45ddcbc8423892c).
  GetMutableGlobalEagerMode: GetMutableGlobalEagerMode(f68bb98b798a4981).
  GetDefaultInplaceBufferDonation: GetDefaultInplaceBufferDonation(c9857a73d68e59ba).
  GetMutableGlobalInplaceBufferDonation: GetMutableGlobalInplaceBufferDonation(4f1842f07fc06118).
---
# Module: [`csrc/eager/eager_mode.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc)

## Functions
- <a id="EnableInplaceBufferDonation"></a>`EnableInplaceBufferDonation(bool enabled)` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L81) — Controls whether input buffer donation for in-place ATen operations in — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="GetDefaultEagerMode"></a>`GetDefaultEagerMode()` — [`L28`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L28)
- <a id="GetDefaultInplaceBufferDonation"></a>`GetDefaultInplaceBufferDonation()` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L61)
- <a id="GetEagerMode"></a>`GetEagerMode()` — [`L51`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L51) — Returns the active eager mode for the current Python thread. Thread-safe. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="GetMutableGlobalEagerMode"></a>`GetMutableGlobalEagerMode()` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L46) — Returns the global base eager mode.
- <a id="GetMutableGlobalInplaceBufferDonation"></a>`GetMutableGlobalInplaceBufferDonation()` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L72) — Returns the global base in-place buffer donation setting.
- <a id="IsInplaceBufferDonationEnabled"></a>`IsInplaceBufferDonationEnabled()` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L77) — Returns whether input buffer donation for in-place ATen operations in — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="SetEagerMode"></a>`SetEagerMode(EagerMode mode)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/eager/eager_mode.cc#L56) — Sets the global default eager mode. Thread-safe. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)

