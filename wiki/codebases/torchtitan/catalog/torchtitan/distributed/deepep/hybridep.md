---
title: 'Module: torchtitan/distributed/deepep/hybridep.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/deepep/hybridep.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.deepep.hybridep`/
symbols:
  _buffer._buffer: _buffer._buffer.
  DispatchHandle: DispatchHandle#
  get_buffer: get_buffer().
  dispatch_tokens: dispatch_tokens().
  combine_tokens: combine_tokens().
  _dispatch_impl: _dispatch_impl().
  _combine_impl: _combine_impl().
  _dispatch_bwd_impl: _dispatch_bwd_impl().
  _combine_bwd_impl: _combine_bwd_impl().
  DispatchHandle.value: DispatchHandle#value.
  _dispatch_fake: _dispatch_fake().
  DispatchHandle.__eq__: DispatchHandle#__eq__().
  _combine_fake: _combine_fake().
  _dispatch_bwd_fake: _dispatch_bwd_fake().
  _combine_bwd_fake: _combine_bwd_fake().
  DispatchState.handle: DispatchState#handle.
  DispatchState: DispatchState#
  DispatchState.permuted_scores: DispatchState#permuted_scores.
  DispatchHandle.__hash__: DispatchHandle#__hash__().
  DispatchHandle.__fx_repr__: DispatchHandle#__fx_repr__().
  DispatchState.num_tokens: DispatchState#num_tokens.
  _num_permuted_tokens_for_non_blocking: _num_permuted_tokens_for_non_blocking().
  _dispatch_backward: _dispatch_backward().
  _dispatch_setup_context: _dispatch_setup_context().
  _combine_backward: _combine_backward().
  _combine_setup_context: _combine_setup_context().
  _NUM_SMS_DISPATCH: _NUM_SMS_DISPATCH.
  _NUM_SMS_COMBINE: _NUM_SMS_COMBINE.
  DispatchHandle.__init__: DispatchHandle#__init__().
  __all__: __all__.
---
# Module: [`torchtitan/distributed/deepep/hybridep.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py)

## Classes
### <a id="DispatchHandle"></a>`DispatchHandle`
- def: [`torchtitan/distributed/deepep/hybridep.py:34`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L34)
- doc: Opaque wrapper for HybridEP dispatch handle.
- signature: `class DispatchHandle(CustomClassBase):`
- members:
  - <a id="DispatchHandle.value"></a>`value` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L43)
- protocol/private: <a id="DispatchHandle.__eq__"></a>`__eq__`[`L45`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L45), <a id="DispatchHandle.__fx_repr__"></a>`__fx_repr__`[`L58`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L58), <a id="DispatchHandle.__hash__"></a>`__hash__`[`L50`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L50), <a id="DispatchHandle.__init__"></a>`__init__`[`L42`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L42)
- used by: [`_combine_impl`](hybridep.md#_combine_impl), [`_dispatch_impl`](hybridep.md#_dispatch_impl), [`_combine_bwd_impl`](hybridep.md#_combine_bwd_impl), [`_dispatch_bwd_impl`](hybridep.md#_dispatch_bwd_impl), [`_dispatch_fake`](hybridep.md#_dispatch_fake), [`_combine_bwd_fake`](hybridep.md#_combine_bwd_fake), [`_combine_fake`](hybridep.md#_combine_fake), [`_dispatch_bwd_fake`](hybridep.md#_dispatch_bwd_fake), [`handle`](hybridep.md#DispatchState.handle)

### <a id="DispatchState"></a>`DispatchState`
- def: [`torchtitan/distributed/deepep/hybridep.py:66`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L66)
- doc: State from dispatch needed for combine.
- signature: `class DispatchState:`
- members:
  - <a id="DispatchState.handle"></a>`handle` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L75)
  - <a id="DispatchState.num_tokens"></a>`num_tokens` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L77)
  - <a id="DispatchState.permuted_scores"></a>`permuted_scores` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L76)
- uses (calls/refs, reference-scoped): [`DispatchHandle`](hybridep.md#DispatchHandle)
- used by: [`dispatch_tokens`](hybridep.md#dispatch_tokens), [`combine_tokens`](hybridep.md#combine_tokens)

## Functions
- <a id="_combine_backward"></a>`_combine_backward(ctx, grad_combined)` — [`L367`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L367) — Backward: scatter gradients via dispatch_bwd op.
- <a id="_combine_bwd_fake"></a>`_combine_bwd_fake(grad_hidden: torch.Tensor, grad_scores: torch.Tensor, handle: DispatchHandle, num_tokens: int, num_experts: int)` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L315) — Fake combine_bwd for torch.compile tracing.
- <a id="_combine_bwd_impl"></a>`_combine_bwd_impl(grad_hidden: torch.Tensor, grad_scores: torch.Tensor, handle: DispatchHandle, num_tokens: int, num_experts: int)` — [`L290`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L290) — Backward of dispatch: gather gradients via combine_with_unpermute.
- <a id="_combine_fake"></a>`_combine_fake(x: torch.Tensor, handle: DispatchHandle, num_tokens: int, pad_multiple: int | None = None)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L241) — Fake combine for torch.compile tracing.
- <a id="_combine_impl"></a>`_combine_impl(x: torch.Tensor, handle: DispatchHandle, num_tokens: int, pad_multiple: int | None = None)` — [`L225`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L225) — CUDA combine: reverse dispatch permutation via opaque handle.
- <a id="_combine_setup_context"></a>`_combine_setup_context(ctx, inputs, output)` — [`L376`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L376) — Save context for combine backward.
- <a id="_dispatch_backward"></a>`_dispatch_backward(ctx, grad_hidden, grad_scores, grad_tpe, grad_handle)` — [`L334`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L334) — Backward: gather gradients via combine_bwd op.
- <a id="_dispatch_bwd_fake"></a>`_dispatch_bwd_fake(grad_combined: torch.Tensor, handle: DispatchHandle, num_permuted_tokens: int, pad_multiple: int | None = None)` — [`L279`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L279) — Fake dispatch_bwd for torch.compile tracing.
- <a id="_dispatch_bwd_impl"></a>`_dispatch_bwd_impl(grad_combined: torch.Tensor, handle: DispatchHandle, num_permuted_tokens: int, pad_multiple: int | None = None)` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L257) — Backward of combine: scatter gradients via dispatch_with_permute.
- <a id="_dispatch_fake"></a>`_dispatch_fake(x: torch.Tensor, topk_idx: torch.Tensor, topk_weights: torch.Tensor, num_experts: int, ep_size: int, group_name: str, non_blocking: bool = False, moe_expert_capacity_factor: float | None = None, pad_multiple: int | None = None)` — [`L194`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L194) — Fake dispatch for torch.compile tracing.
- <a id="_dispatch_impl"></a>`_dispatch_impl(x: torch.Tensor, topk_idx: torch.Tensor, topk_weights: torch.Tensor, num_experts: int, ep_size: int, group_name: str, non_blocking: bool = False, moe_expert_capacity_factor: float | None = None, pad_multiple: int | None = None)` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L116) — DeepEP's dispatch_with_permute needs to know the output buffer size
- <a id="_dispatch_setup_context"></a>`_dispatch_setup_context(ctx, inputs, output)` — [`L357`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L357) — Save context for dispatch backward.
- <a id="_num_permuted_tokens_for_non_blocking"></a>`_num_permuted_tokens_for_non_blocking(num_tokens: int, ep_size: int, num_local_experts: int, top_k: int, moe_expert_capacity_factor: float, pad_multiple: int | None = None)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L80) — Pre-allocated output buffer size for non-blocking dispatch.
- <a id="combine_tokens"></a>`combine_tokens(hidden_states: torch.Tensor, state: DispatchState, pad_multiple: int | None = None)` — [`L526`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L526) — Combine expert outputs back to original token order.
- <a id="dispatch_tokens"></a>`dispatch_tokens(hidden_states: torch.Tensor, selected_experts_indices: torch.Tensor, top_scores: torch.Tensor, num_local_experts: int, num_experts: int, group: dist.ProcessGroup, *, non_blocking_expert_capacity_factor: float | None = None, pad_multiple: int | None = None)` — [`L455`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L455) — Dispatch tokens to experts via HybridEP all-to-all.
- <a id="get_buffer"></a>`get_buffer(group: dist.ProcessGroup, hidden_dim: int, num_max_tokens_per_rank: int, num_local_experts: int, fp8_dispatch: bool = False)` — [`L394`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L394) — Ensure the global HybridEP buffer is initialized, reinitializing if config changed.

## Module values
- <a id="_NUM_SMS_COMBINE"></a>`_NUM_SMS_COMBINE` — [`L391`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L391)
- <a id="_NUM_SMS_DISPATCH"></a>`_NUM_SMS_DISPATCH` — [`L390`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L390)
- <a id="__all__"></a>`__all__` — [`L543`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L543)
- <a id="_buffer._buffer"></a>`_buffer` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/hybridep.py#L31)

