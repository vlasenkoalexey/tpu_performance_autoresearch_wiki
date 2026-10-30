---
title: 'Module: torchtitan/distributed/deepep/deepep.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/deepep/deepep.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.deepep.deepep`/
symbols:
  dispatch_tokens: dispatch_tokens().
  combine_tokens: combine_tokens().
  _buffer._buffer: _buffer._buffer.
  _dispatch_op_impl: _dispatch_op_impl().
  _combine_op_impl: _combine_op_impl().
  _lib: _lib.
  _pending_combine_event: _pending_combine_event.
  _handle_cache._handle_cache: _handle_cache._handle_cache.
  sync_combine: sync_combine().
  get_buffer: get_buffer().
  DispatchState: DispatchState#
  DispatchState.handle_id: DispatchState#handle_id.
  _get_next_handle_id: _get_next_handle_id().
  _resolve_dispatch_num_sms: _resolve_dispatch_num_sms().
  _dispatch_setup_context: _dispatch_setup_context().
  _dispatch_backward: _dispatch_backward().
  _combine_setup_context: _combine_setup_context().
  _combine_backward: _combine_backward().
  e: e.
  DispatchState.num_recv_tokens: DispatchState#num_recv_tokens.
  DispatchState.cudagraphable: DispatchState#cudagraphable.
  DispatchState.permuted_indices: DispatchState#permuted_indices.
  DispatchState.permuted_scores: DispatchState#permuted_scores.
  DispatchState.recv_scores: DispatchState#recv_scores.
  _handle_counter._handle_counter: _handle_counter._handle_counter.
  _DEEPEP_MULTINODE_NUM_SMS: _DEEPEP_MULTINODE_NUM_SMS.
  _permute_tokens: _permute_tokens().
  _unpermute_tokens: _unpermute_tokens().
  get_hidden_bytes: get_hidden_bytes().
---
# Module: [`torchtitan/distributed/deepep/deepep.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py)

## Classes
### <a id="DispatchState"></a>`DispatchState`
- def: [`torchtitan/distributed/deepep/deepep.py:441`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L441)
- doc: State from dispatch needed for combine.
- signature: `class DispatchState:`
- members:
  - <a id="DispatchState.cudagraphable"></a>`cudagraphable` — [`L446`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L446)
  - <a id="DispatchState.handle_id"></a>`handle_id` — [`L444`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L444)
  - <a id="DispatchState.num_recv_tokens"></a>`num_recv_tokens` — [`L445`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L445)
  - <a id="DispatchState.permuted_indices"></a>`permuted_indices` — [`L448`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L448)
  - <a id="DispatchState.permuted_scores"></a>`permuted_scores` — [`L449`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L449)
  - <a id="DispatchState.recv_scores"></a>`recv_scores` — [`L451`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L451)
- used by: [`dispatch_tokens`](deepep.md#dispatch_tokens), [`combine_tokens`](deepep.md#combine_tokens)

## Functions
- <a id="_combine_backward"></a>`_combine_backward(ctx, grad_combined)` — [`L282`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L282) — Backward for combine: a dispatch of the gradient (reuses the cached handle).
- <a id="_combine_op_impl"></a>`_combine_op_impl(x: torch.Tensor, handle_id: torch.Tensor, will_backward: bool)` — [`L246`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L246) — Execute DeepEP v2 combine (pure reduction; scores already applied upstream).
- <a id="_combine_setup_context"></a>`_combine_setup_context(ctx, inputs, output)` — [`L277`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L277)
- <a id="_dispatch_backward"></a>`_dispatch_backward(ctx, grad_recv_x, grad_recv_topk_idx, grad_recv_scores, grad_num_recv, grad_handle_id)` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L204) — Backward for dispatch: a combine of the gradients.
- <a id="_dispatch_op_impl"></a>`_dispatch_op_impl(x: torch.Tensor, topk_idx: torch.Tensor, topk_weights: torch.Tensor, num_experts: int, num_tokens_per_rank: int, cudagraphable: bool)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L130) — Execute DeepEP v2 dispatch.
- <a id="_dispatch_setup_context"></a>`_dispatch_setup_context(ctx, inputs, output)` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L197)
- <a id="_get_next_handle_id"></a>`_get_next_handle_id()` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L70) — Generate a unique handle_id tensor on CPU to avoid a GPU-CPU sync.
- <a id="_permute_tokens"></a>`_permute_tokens(hidden_states: torch.Tensor, dispatched_indices: torch.Tensor, dispatched_scores: torch.Tensor)` — [`L384`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L384) — Gather the compact (deduplicated) dispatch output into expert-major order.
- <a id="_resolve_dispatch_num_sms"></a>`_resolve_dispatch_num_sms(buffer, num_experts: int, num_topk: int)` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L112) — SM count for the dispatch kernel (also reused by combine via the handle).
- <a id="_unpermute_tokens"></a>`_unpermute_tokens(permuted_hidden_states: torch.Tensor, permuted_indices: torch.Tensor, num_tokens: int)` — [`L422`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L422) — Reverse ``_permute_tokens``: scatter-add expert outputs back to unique tokens.
- <a id="combine_tokens"></a>`combine_tokens(hidden_states: torch.Tensor, state: DispatchState)` — [`L560`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L560) — Combine expert outputs back to tokens via DeepEP v2.
- <a id="dispatch_tokens"></a>`dispatch_tokens(hidden_states: torch.Tensor, selected_experts_indices: torch.Tensor, top_scores: torch.Tensor, num_local_experts: int, num_experts: int, *, num_tokens_per_rank: int, cudagraphable: bool = False)` — [`L454`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L454) — Dispatch tokens to experts via DeepEP v2 ``ElasticBuffer``.
- <a id="get_buffer"></a>`get_buffer(group: ProcessGroup, *, hidden: int, num_max_tokens_per_rank: int, num_topk: int, use_fp8_dispatch: bool = False)` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L335) — Get or create the process-global DeepEP v2 ``ElasticBuffer``.
- <a id="get_hidden_bytes"></a>`get_hidden_bytes(x: torch.Tensor)` — [`L330`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L330) — Bytes for one token's hidden vector (>= 2 so fp8 and bf16 share a buffer).
- <a id="sync_combine"></a>`sync_combine()` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L315) — Wait the current CUDA stream on the pending async combine.

## Module values
- <a id="_DEEPEP_MULTINODE_NUM_SMS"></a>`_DEEPEP_MULTINODE_NUM_SMS` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L109)
- <a id="_buffer._buffer"></a>`_buffer` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L55)
- <a id="_handle_cache._handle_cache"></a>`_handle_cache` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L61)
- <a id="_handle_counter._handle_counter"></a>`_handle_counter` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L62)
- <a id="_lib"></a>`_lib` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L87)
- <a id="_pending_combine_event"></a>`_pending_combine_event` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L67)
- <a id="e"></a>`e` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/deepep/deepep.py#L46)

