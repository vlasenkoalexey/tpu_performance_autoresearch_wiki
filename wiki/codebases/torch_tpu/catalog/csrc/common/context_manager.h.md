---
title: 'Module: csrc/common/context_manager.h'
type: catalog
provenance: extracted
module: csrc/common/context_manager.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetContextState: GetContextState(4865679c0ba3ac33).
  PopContextState: PopContextState(49f6e7a06ebc5aa8).
  PushContextState: PushContextState(9b289cee16747614).
  ContextManagerState: ContextManagerState#
  ContextManagerNode: ContextManagerNode#
  ContextManagerNode.ContextManagerNode: ContextManagerNode#ContextManagerNode(3e235d7578564969).
  is_alternative_v: internal/is_alternative_v.
  ContextManagerNode.parent: ContextManagerNode#parent(5a61c3d5e38d959d).
  ContextManagerNode.state: ContextManagerNode#state(ec45a031f4e09d1e).
  ContextManagerNode.operator: ContextManagerNode#`operator=`(159a536bed234550).
  ContextManagerNode.state_: ContextManagerNode#state_.
  kTpuContextSlot: internal/kTpuContextSlot.
  ContextManagerNode.parent_: ContextManagerNode#parent_.
---
# Module: [`csrc/common/context_manager.h`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h)

## Classes
### <a id="ContextManagerNode"></a>`ContextManagerNode`  ·  implements/extends DebugInfoBase
- def: [`csrc/common/context_manager.h:75`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L75) — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- doc: A persistent stack node for TorchTPU context managers. Each node contains a
- signature: `class ContextManagerNode : public c10::DebugInfoBase`
- members:
  - `ContextManagerNode(ContextManagerState state, const ContextManagerNode* absl_nullable parent)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L78) — Creates a node from the given state (delta) and parent node.
  - `ContextManagerNode(const ContextManagerNode&)` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L83) — This class is neither copyable nor movable.
  - `ContextManagerNode(ContextManagerNode&&)` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L85)
  - <a id="ContextManagerNode.ContextManagerNode"></a>`ContextManagerNode(ContextManagerState state, const ContextManagerNode* absl_nullable parent)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L78) — Creates a node from the given state (delta) and parent node. — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
  - <a id="ContextManagerNode.operator"></a>`operator=(ContextManagerNode&&)` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L86)
  - `operator=(const ContextManagerNode&)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L84)
  - <a id="ContextManagerNode.parent"></a>`parent()` — [`L90`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L90)
  - <a id="ContextManagerNode.state"></a>`state()` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L89) — Accessors.
  - `state()` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L89) — Accessors.
  - <a id="ContextManagerNode.parent_"></a>`parent_` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L94) — Not owned.
  - <a id="ContextManagerNode.state_"></a>`state_` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L93)
- uses (calls/refs, reference-scoped): [`ContextManagerState`](context_manager.h.md#ContextManagerState)
- used by: [`GetContextState`](context_manager.h.md#GetContextState), [`PopContextState`](context_manager.h.md#PopContextState), [`PopContextStateUntyped`](context_manager.cc.md#PopContextStateUntyped), [`PushContextStateUntyped`](context_manager.cc.md#PushContextStateUntyped)

### <a id="ContextManagerState"></a>`ContextManagerState`
- def: [`csrc/common/context_manager.h:61`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L61)
- doc: The state for different types of context managers respectively.
- signature: `using ContextManagerState = std::variant< CustomCompilerOptionsContextState, EagerModeContextState, EnableTracebacksContextState, IsSpmdSafeContextState, LayoutContextState, PrecisionContextState, ProfileContextState >`
- uses (calls/refs, reference-scoped): [`EagerModeContextState`](context_states.h.md#EagerModeContextState), [`EnableTracebacksContextState`](context_states.h.md#EnableTracebacksContextState), [`CustomCompilerOptionsContextState`](context_states.h.md#CustomCompilerOptionsContextState), [`ProfileContextState`](context_states.h.md#ProfileContextState), [`PrecisionContextState`](context_states.h.md#PrecisionContextState), [`IsSpmdSafeContextState`](context_states.h.md#IsSpmdSafeContextState), [`LayoutContextState`](context_states.h.md#LayoutContextState)
- used by: [`GetContextState`](context_manager.h.md#GetContextState), [`PopContextState`](context_manager.h.md#PopContextState), [`PushContextState`](context_manager.h.md#PushContextState), [`PushContextStateUntyped`](context_manager.cc.md#PushContextStateUntyped), [`ContextManagerNode`](context_manager.h.md#ContextManagerNode.ContextManagerNode), [`parent`](context_manager.h.md#ContextManagerNode.parent), [`operator=`](context_manager.h.md#ContextManagerNode.operator)

## Functions
- <a id="GetContextState"></a>`GetContextState()` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L101) — Returns the context state of the given type from the current python — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- `GetContextState(GetDefaultStateT get_default_state)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L132) — Returns the context state of the given type from the current python
- <a id="PopContextState"></a>`PopContextState()` — [`L165`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L165) — Pops the current python thread's context state stack, and returns the — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)
- <a id="PushContextState"></a>`PushContextState(T state)` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L153) — Pushes the given context state of the specified type T onto the current — documented in [context-states-and-execution-modes](../../../concepts/context-states-and-execution-modes.md)

## Module values
- <a id="is_alternative_v"></a>`is_alternative_v` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L43) — Trait that indicates whether T is one of the options for an std::variant
- <a id="kTpuContextSlot"></a>`kTpuContextSlot` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/context_manager.h#L38) — The ThreadLocalDebugInfo slot to use for TorchTPU context states. For now, we

