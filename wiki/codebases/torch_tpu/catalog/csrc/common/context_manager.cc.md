---
title: 'Module: csrc/common/context_manager.cc'
type: catalog
provenance: extracted
module: csrc/common/context_manager.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DisallowThisThreadToAccessContextState: DisallowThisThreadToAccessContextState(49f6e7a06ebc5aa8).
  CrashIfContextStateAccessIsDisallowed: internal/CrashIfContextStateAccessIsDisallowed(49f6e7a06ebc5aa8).
  PopContextStateUntyped: internal/PopContextStateUntyped(12823fd0495830c1).
  PushContextStateUntyped: internal/PushContextStateUntyped(313a88a3555d794).
  allow_context_state_access: allow_context_state_access.
---
# Module: [`csrc/common/context_manager.cc`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc)

## Functions
- <a id="CrashIfContextStateAccessIsDisallowed"></a>`CrashIfContextStateAccessIsDisallowed()` — [`L36`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L36) — Crashes if the current thread is not allowed to access context states. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="DisallowThisThreadToAccessContextState"></a>`DisallowThisThreadToAccessContextState()` — [`L30`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L30) — One-way flip to disallow the current thread to access thread-local context — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="PopContextStateUntyped"></a>`PopContextStateUntyped()` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L56) — Type-erased implementation that pops and returns a node from the underlying — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- `PushContextStateUntyped(ContextManagerState state)` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L44) — Type-erased implementation that pushes a context state variant onto the
- <a id="PushContextStateUntyped"></a>`PushContextStateUntyped(ContextManagerState state)` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L44) — Type-erased implementation that pushes a context state variant onto the — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)

## Module values
- <a id="allow_context_state_access"></a>`allow_context_state_access` — [`L28`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.cc#L28)

