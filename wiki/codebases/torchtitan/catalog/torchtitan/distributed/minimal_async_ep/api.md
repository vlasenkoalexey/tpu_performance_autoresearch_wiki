---
title: 'Module: torchtitan/distributed/minimal_async_ep/api.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/minimal_async_ep/api.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.minimal_async_ep.api`/
symbols:
  init_buffer: init_buffer().
  _copy_rows_to_peers_and_wait_cuda: _copy_rows_to_peers_and_wait_cuda().
  maybe_update_minimal_async_ep_config: maybe_update_minimal_async_ep_config().
  _buffer_state._buffer_state: _buffer_state._buffer_state.
  _copy_all_counts_to_peers_and_wait_cuda: _copy_all_counts_to_peers_and_wait_cuda().
  _compute_direct_metadata: _compute_direct_metadata().
  dispatch_op: dispatch_op().
  _wait_counts_ready: _wait_counts_ready().
  combine_op: combine_op().
  combine_backward_op: combine_backward_op().
  dispatch_backward_op: dispatch_backward_op().
  _wait_hidden_ready: _wait_hidden_ready().
  _dispatch_metadata: _dispatch_metadata().
  _combine_to_origin: _combine_to_origin().
  _MinimalAsyncEPBufferState.group: _MinimalAsyncEPBufferState#group.
  MinimalAsyncEPDispatchMetadata: MinimalAsyncEPDispatchMetadata#
  _buffer_key._buffer_key: _buffer_key._buffer_key.
  _dispatch_to_experts: _dispatch_to_experts().
  dispatch_autograd_backward: dispatch_autograd_backward().
  combine_autograd_backward: combine_autograd_backward().
  _MinimalAsyncEPBufferState.num_max_tokens_per_rank: _MinimalAsyncEPBufferState#num_max_tokens_per_rank.
  _MinimalAsyncEPBufferState.hidden_recv_buffer_index: _MinimalAsyncEPBufferState#hidden_recv_buffer_index.
  dispatch_op_fake: dispatch_op_fake().
  combine_op_fake: combine_op_fake().
  dispatch_backward_op_fake: dispatch_backward_op_fake().
  combine_backward_op_fake: combine_backward_op_fake().
  _HIDDEN_RECV_BUFFER_COUNT: _HIDDEN_RECV_BUFFER_COUNT.
  _MinimalAsyncEPBufferState: _MinimalAsyncEPBufferState#
  _MinimalAsyncEPBufferState.hidden_recv_buffers: _MinimalAsyncEPBufferState#hidden_recv_buffers.
  _MinimalAsyncEPBufferState.hidden_recv_handles: _MinimalAsyncEPBufferState#hidden_recv_handles.
  _MinimalAsyncEPBufferState.hidden_recv_peer_buffers: _MinimalAsyncEPBufferState#hidden_recv_peer_buffers.
  _MinimalAsyncEPBufferState.hidden_recv_peer_ptrs: _MinimalAsyncEPBufferState#hidden_recv_peer_ptrs.
  _MinimalAsyncEPBufferState.counts_recv_buffer: _MinimalAsyncEPBufferState#counts_recv_buffer.
  _MinimalAsyncEPBufferState.counts_recv_handle: _MinimalAsyncEPBufferState#counts_recv_handle.
  _MinimalAsyncEPBufferState.counts_recv_peer_buffers: _MinimalAsyncEPBufferState#counts_recv_peer_buffers.
  _MinimalAsyncEPBufferState.counts_recv_peer_ptrs: _MinimalAsyncEPBufferState#counts_recv_peer_ptrs.
  MinimalAsyncEPDispatchMetadata.dispatch_dst_ranks: MinimalAsyncEPDispatchMetadata#dispatch_dst_ranks.
  MinimalAsyncEPDispatchMetadata.dispatch_dst_rows: MinimalAsyncEPDispatchMetadata#dispatch_dst_rows.
  MinimalAsyncEPDispatchMetadata.combine_dst_ranks: MinimalAsyncEPDispatchMetadata#combine_dst_ranks.
  MinimalAsyncEPDispatchMetadata.combine_dst_rows: MinimalAsyncEPDispatchMetadata#combine_dst_rows.
  MinimalAsyncEPDispatchMetadata.combine_num_valid_rows: MinimalAsyncEPDispatchMetadata#combine_num_valid_rows.
  MinimalAsyncEPDispatchMetadata.E_row_to_T_row: MinimalAsyncEPDispatchMetadata#E_row_to_T_row.
  MinimalAsyncEPDispatchMetadata.T_row_to_E_row: MinimalAsyncEPDispatchMetadata#T_row_to_E_row.
  MinimalAsyncEPDispatchMetadata.routed_scores: MinimalAsyncEPDispatchMetadata#routed_scores.
  MinimalAsyncEPDispatchMetadata.num_tokens: MinimalAsyncEPDispatchMetadata#num_tokens.
  MinimalAsyncEPDispatchMetadata.top_k: MinimalAsyncEPDispatchMetadata#top_k.
  _wait_ready: _wait_ready().
  _HIDDEN_READY_CHANNEL: _HIDDEN_READY_CHANNEL.
  _COUNTS_READY_CHANNEL: _COUNTS_READY_CHANNEL.
  dispatch_setup_context: dispatch_setup_context().
  combine_setup_context: combine_setup_context().
  __all__: __all__.
---
# Module: [`torchtitan/distributed/minimal_async_ep/api.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py)

## Classes
### <a id="MinimalAsyncEPDispatchMetadata"></a>`MinimalAsyncEPDispatchMetadata`
- def: [`torchtitan/distributed/minimal_async_ep/api.py:145`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L145)
- doc: MinimalAsyncEP metadata from dispatch needed for combine.
- signature: `class MinimalAsyncEPDispatchMetadata:`
- members:
  - <a id="MinimalAsyncEPDispatchMetadata.E_row_to_T_row"></a>`E_row_to_T_row` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L165)
  - <a id="MinimalAsyncEPDispatchMetadata.T_row_to_E_row"></a>`T_row_to_E_row` — [`L166`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L166)
  - <a id="MinimalAsyncEPDispatchMetadata.combine_dst_ranks"></a>`combine_dst_ranks` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L162)
  - <a id="MinimalAsyncEPDispatchMetadata.combine_dst_rows"></a>`combine_dst_rows` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L163)
  - <a id="MinimalAsyncEPDispatchMetadata.combine_num_valid_rows"></a>`combine_num_valid_rows` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L164)
  - <a id="MinimalAsyncEPDispatchMetadata.dispatch_dst_ranks"></a>`dispatch_dst_ranks` — [`L160`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L160)
  - <a id="MinimalAsyncEPDispatchMetadata.dispatch_dst_rows"></a>`dispatch_dst_rows` — [`L161`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L161)
  - <a id="MinimalAsyncEPDispatchMetadata.num_tokens"></a>`num_tokens` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L168)
  - <a id="MinimalAsyncEPDispatchMetadata.routed_scores"></a>`routed_scores` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L167)
  - <a id="MinimalAsyncEPDispatchMetadata.top_k"></a>`top_k` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L169)
- used by: [`dispatch`](../../models/common/token_dispatcher.md#MinimalAsyncEPTokenDispatcher.dispatch), [`combine`](../../models/common/token_dispatcher.md#MinimalAsyncEPTokenDispatcher.combine)

### <a id="_MinimalAsyncEPBufferState"></a>`_MinimalAsyncEPBufferState`
- def: [`torchtitan/distributed/minimal_async_ep/api.py:50`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L50)
- doc: Process-local symmetric-memory state initialized as one unit.
- signature: `class _MinimalAsyncEPBufferState:`
- members:
  - <a id="_MinimalAsyncEPBufferState.counts_recv_buffer"></a>`counts_recv_buffer` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L59)
  - <a id="_MinimalAsyncEPBufferState.counts_recv_handle"></a>`counts_recv_handle` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L60)
  - <a id="_MinimalAsyncEPBufferState.counts_recv_peer_buffers"></a>`counts_recv_peer_buffers` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L61)
  - <a id="_MinimalAsyncEPBufferState.counts_recv_peer_ptrs"></a>`counts_recv_peer_ptrs` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L62)
  - <a id="_MinimalAsyncEPBufferState.group"></a>`group` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L53)
  - <a id="_MinimalAsyncEPBufferState.hidden_recv_buffer_index"></a>`hidden_recv_buffer_index` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L63)
  - <a id="_MinimalAsyncEPBufferState.hidden_recv_buffers"></a>`hidden_recv_buffers` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L55)
  - <a id="_MinimalAsyncEPBufferState.hidden_recv_handles"></a>`hidden_recv_handles` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L56)
  - <a id="_MinimalAsyncEPBufferState.hidden_recv_peer_buffers"></a>`hidden_recv_peer_buffers` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L57)
  - <a id="_MinimalAsyncEPBufferState.hidden_recv_peer_ptrs"></a>`hidden_recv_peer_ptrs` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L58)
  - <a id="_MinimalAsyncEPBufferState.num_max_tokens_per_rank"></a>`num_max_tokens_per_rank` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L54)
- used by: [`init_buffer`](api.md#init_buffer), [`_copy_rows_to_peers_and_wait_cuda`](api.md#_copy_rows_to_peers_and_wait_cuda), [`_buffer_state`](api.md#_buffer_state._buffer_state), [`_copy_all_counts_to_peers_and_wait_cuda`](api.md#_copy_all_counts_to_peers_and_wait_cuda), [`_compute_direct_metadata`](api.md#_compute_direct_metadata), [`_wait_counts_ready`](api.md#_wait_counts_ready)

## Functions
- <a id="_combine_to_origin"></a>`_combine_to_origin(x_RD: torch.Tensor, combine_dst_ranks: torch.Tensor, combine_dst_rows: torch.Tensor, combine_num_valid_rows: torch.Tensor, num_routed_rows: int)` — [`L483`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L483) — Copy active local rows back to origin ranks as logical ``(N, D)`` rows.
- <a id="_compute_direct_metadata"></a>`_compute_direct_metadata(num_local_tokens_per_expert_E: torch.Tensor, all_tokens_per_expert_RE: torch.Tensor, num_routed_rows: int, receive_capacity: int, ep_size: int)` — [`L386`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L386)
- <a id="_copy_all_counts_to_peers_and_wait_cuda"></a>`_copy_all_counts_to_peers_and_wait_cuda(num_local_tokens_per_expert_E: torch.Tensor, ep_size: int)` — [`L366`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L366) — Copy this rank's expert counts to all peers and wait for peer counts.
- <a id="_copy_rows_to_peers_and_wait_cuda"></a>`_copy_rows_to_peers_and_wait_cuda(x: torch.Tensor, dst_ranks: torch.Tensor, dst_rows: torch.Tensor, num_rows: int, *, block_m: int = 1, num_warps: int = 4, src_rows: torch.Tensor | None = None, num_valid_rows: torch.Tensor | None = None)` — [`L296`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L296) — Copy rows through symmetric memory and wait before returning.
- <a id="_dispatch_metadata"></a>`_dispatch_metadata(num_local_tokens_per_expert_E: torch.Tensor, num_routed_rows: int, receive_capacity: int, ep_size: int)` — [`L505`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L505) — Exchange per-expert local counts and build dispatch/combine metadata.
- <a id="_dispatch_to_experts"></a>`_dispatch_to_experts(x_ND: torch.Tensor, dispatch_dst_ranks: torch.Tensor, dispatch_dst_rows: torch.Tensor, num_routed_rows: int)` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L466)
- <a id="_wait_counts_ready"></a>`_wait_counts_ready()` — [`L347`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L347)
- <a id="_wait_hidden_ready"></a>`_wait_hidden_ready(hidden_recv_handle: Any)` — [`L343`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L343)
- <a id="_wait_ready"></a>`_wait_ready(handle: Any, channel: int)` — [`L352`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L352) — EP-group barrier: ensure every peer has finished writing into this
- <a id="combine_autograd_backward"></a>`combine_autograd_backward(ctx, grad_out, grad_routed_output)` — [`L972`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L972)
- <a id="combine_backward_op"></a>`combine_backward_op(grad_out: torch.Tensor, dispatch_dst_ranks: torch.Tensor, dispatch_dst_rows: torch.Tensor, E_row_to_T_row_N: torch.Tensor, routed_scores_N: torch.Tensor, saved_routed_output_ND: torch.Tensor, top_k: int, receive_capacity: int)` — [`L829`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L829) — Expand combine gradients and dispatch them back to expert-owner ranks.
- <a id="combine_backward_op_fake"></a>`combine_backward_op_fake(grad_out: torch.Tensor, dispatch_dst_ranks: torch.Tensor, dispatch_dst_rows: torch.Tensor, E_row_to_T_row_N: torch.Tensor, routed_scores_N: torch.Tensor, saved_routed_output_ND: torch.Tensor, top_k: int, receive_capacity: int)` — [`L884`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L884)
- <a id="combine_op"></a>`combine_op(x: torch.Tensor, dispatch_dst_ranks: torch.Tensor, dispatch_dst_rows: torch.Tensor, combine_dst_ranks: torch.Tensor, combine_dst_rows: torch.Tensor, combine_num_valid_rows: torch.Tensor, T_row_to_E_row_N: torch.Tensor, E_row_to_T_row_N: torch.Tensor, routed_scores_N: torch.Tensor, num_tokens: int, top_k: int)` — [`L687`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L687) — Move expert outputs to origin ranks and reduce routed top-k rows.
- <a id="combine_op_fake"></a>`combine_op_fake(x: torch.Tensor, dispatch_dst_ranks: torch.Tensor, dispatch_dst_rows: torch.Tensor, combine_dst_ranks: torch.Tensor, combine_dst_rows: torch.Tensor, combine_num_valid_rows: torch.Tensor, T_row_to_E_row_N: torch.Tensor, E_row_to_T_row_N: torch.Tensor, routed_scores_N: torch.Tensor, num_tokens: int, top_k: int)` — [`L741`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L741)
- <a id="combine_setup_context"></a>`combine_setup_context(ctx, inputs, output)` — [`L946`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L946)
- <a id="dispatch_autograd_backward"></a>`dispatch_autograd_backward(ctx, grad_hidden, *unused_grads)` — [`L924`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L924)
- <a id="dispatch_backward_op"></a>`dispatch_backward_op(grad_hidden: torch.Tensor, combine_dst_ranks: torch.Tensor, combine_dst_rows: torch.Tensor, combine_num_valid_rows: torch.Tensor, T_row_to_E_row_N: torch.Tensor, num_routed_rows: int, num_tokens: int, top_k: int)` — [`L768`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L768) — Move dispatched activation gradients back and reduce routed top-k rows.
- <a id="dispatch_backward_op_fake"></a>`dispatch_backward_op_fake(grad_hidden: torch.Tensor, combine_dst_ranks: torch.Tensor, combine_dst_rows: torch.Tensor, combine_num_valid_rows: torch.Tensor, T_row_to_E_row_N: torch.Tensor, num_routed_rows: int, num_tokens: int, top_k: int)` — [`L811`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L811)
- <a id="dispatch_op"></a>`dispatch_op(dispatch_input: torch.Tensor, topk_expert_ids_TK: torch.Tensor, num_local_tokens_per_expert_E: torch.Tensor, receive_capacity: int, ep_size: int)` — [`L561`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L561) — Build MinimalAsyncEP metadata and dispatch rows to expert-owner ranks.
- <a id="dispatch_op_fake"></a>`dispatch_op_fake(dispatch_input: torch.Tensor, topk_expert_ids_TK: torch.Tensor, num_local_tokens_per_expert_E: torch.Tensor, receive_capacity: int, ep_size: int)` — [`L647`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L647)
- <a id="dispatch_setup_context"></a>`dispatch_setup_context(ctx, inputs, output)` — [`L900`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L900)
- <a id="init_buffer"></a>`init_buffer(group: dist.ProcessGroup, hidden_dim: int, num_max_tokens_per_rank: int, num_local_experts: int, top_k: int, dtype: torch.dtype, device: torch.device)` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L172) — Initialize or reuse the process-local MinimalAsyncEP communication buffer.
- <a id="maybe_update_minimal_async_ep_config"></a>`maybe_update_minimal_async_ep_config(model_config: Any, config: Any)` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L84) — Validate and fill MinimalAsyncEP dispatcher configs from runtime config. — documented in [parallel-dims-and-parallelization](../../../../concepts/parallel-dims-and-parallelization.md)

## Module values
- <a id="_COUNTS_READY_CHANNEL"></a>`_COUNTS_READY_CHANNEL` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L46)
- <a id="_HIDDEN_READY_CHANNEL"></a>`_HIDDEN_READY_CHANNEL` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L45)
- <a id="_HIDDEN_RECV_BUFFER_COUNT"></a>`_HIDDEN_RECV_BUFFER_COUNT` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L43)
- <a id="__all__"></a>`__all__` — [`L1015`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L1015)
- <a id="_buffer_key._buffer_key"></a>`_buffer_key` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L70)
- <a id="_buffer_state._buffer_state"></a>`_buffer_state` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/api.py#L66)

