---
title: 'Module: src/vllm_torchtpu/layers/core/sequence_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/sequence_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.sequence_layout`/
symbols:
  AllSequenceLayoutPlanner.prepare_real: AllSequenceLayoutPlanner#prepare_real().
  AllSequenceLayoutPlanner.prepare_dummy: AllSequenceLayoutPlanner#prepare_dummy().
  SequenceLayoutPlan: SequenceLayoutPlan#
  SequenceLayoutPlan.localize_token_tensor_and_gather_indices: SequenceLayoutPlan#localize_token_tensor_and_gather_indices().
  SequenceLayoutKind: SequenceLayoutKind#
  is_pcp_streaming_attention_metadata: is_pcp_streaming_attention_metadata().
  create_sequence_layout_planner: create_sequence_layout_planner().
  is_pcp_streaming_sequence_layout_descriptor: is_pcp_streaming_sequence_layout_descriptor().
  SequenceLayoutPlan.aggregate_request_aligned_tensor: SequenceLayoutPlan#aggregate_request_aligned_tensor().
  SequenceLayoutPlan.token_slice: SequenceLayoutPlan#token_slice.
  SequenceLayoutDescriptor.cache_key: SequenceLayoutDescriptor#cache_key().
  SequenceLayoutKind.ALL: SequenceLayoutKind#ALL.
  SequenceLayoutPlan.descriptor: SequenceLayoutPlan#descriptor.
  SequenceLayoutPlan.kind: SequenceLayoutPlan#kind().
  is_pcp_streaming_sequence_layout: is_pcp_streaming_sequence_layout().
  SequenceLayoutDescriptor.kind: SequenceLayoutDescriptor#kind.
  SequenceLayoutPlan.global_padded_num_tokens: SequenceLayoutPlan#global_padded_num_tokens.
  DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR: DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR.
  SequenceLayoutDescriptor: SequenceLayoutDescriptor#
  SequenceLayoutPlan.local_index_for_request_major_token: SequenceLayoutPlan#local_index_for_request_major_token().
  AllSequenceLayoutPlanner: AllSequenceLayoutPlanner#
  SequenceLayoutDescriptor.protocol: SequenceLayoutDescriptor#protocol.
  _all_padded_num_tokens: _all_padded_num_tokens().
  DEFAULT_SEQUENCE_LAYOUT_PROTOCOL: DEFAULT_SEQUENCE_LAYOUT_PROTOCOL.
  PCP_STREAMING_SEQUENCE_LAYOUT_PROTOCOL: PCP_STREAMING_SEQUENCE_LAYOUT_PROTOCOL.
  SequenceLayoutPlan.global_num_tokens: SequenceLayoutPlan#global_num_tokens.
  SequenceLayoutPlan.local_num_tokens: SequenceLayoutPlan#local_num_tokens.
  SequenceLayoutPlan.local_padded_num_tokens: SequenceLayoutPlan#local_padded_num_tokens.
  AllSequenceLayoutPlanner.padded_num_tokens: AllSequenceLayoutPlanner#padded_num_tokens().
  SequenceLayoutKind.PARTIAL: SequenceLayoutKind#PARTIAL.
  SequenceLayoutPlan.logits_local_indices_cpu: SequenceLayoutPlan#logits_local_indices_cpu.
  SequenceLayoutPlan.logits_owner_mask_cpu: SequenceLayoutPlan#logits_owner_mask_cpu.
  SequenceLayoutPlan.requires_hidden_state_gather: SequenceLayoutPlan#requires_hidden_state_gather.
  SequenceLayoutPlan._packed_to_request_major_token_indices: SequenceLayoutPlan#_packed_to_request_major_token_indices.
  SequenceLayoutPlan._request_major_to_packed_token_indices: SequenceLayoutPlan#_request_major_to_packed_token_indices.
  _first_ge: _first_ge().
  SequenceLayoutPlanner.prepare_real: SequenceLayoutPlanner#prepare_real().
  SequenceLayoutPlanner.prepare_dummy: SequenceLayoutPlanner#prepare_dummy().
  SequenceLayoutPlanner.finalize_hidden_states: SequenceLayoutPlanner#finalize_hidden_states().
  SequenceLayoutPlanner.maybe_select_logits_hidden_states: SequenceLayoutPlanner#maybe_select_logits_hidden_states().
  AllSequenceLayoutPlanner.finalize_hidden_states: AllSequenceLayoutPlanner#finalize_hidden_states().
  AllSequenceLayoutPlanner.maybe_select_logits_hidden_states: AllSequenceLayoutPlanner#maybe_select_logits_hidden_states().
  SequenceLayoutDescriptor.version: SequenceLayoutDescriptor#version.
  SequenceLayoutPlan.logits_indices_cpu: SequenceLayoutPlan#logits_indices_cpu.
  _localize_token_tensor_and_gather_indices: _localize_token_tensor_and_gather_indices().
  SequenceLayoutPlanner: SequenceLayoutPlanner#
  SequenceLayoutPlanner.requires_backend_preinit: SequenceLayoutPlanner#requires_backend_preinit().
  SequenceLayoutPlanner.backend_preinit_world_size: SequenceLayoutPlanner#backend_preinit_world_size().
  SequenceLayoutPlanner.uses_selected_logits_hidden_states: SequenceLayoutPlanner#uses_selected_logits_hidden_states().
  SequenceLayoutPlanner.reserve_host_token_capacity: SequenceLayoutPlanner#reserve_host_token_capacity().
  SequenceLayoutPlanner.padded_num_tokens: SequenceLayoutPlanner#padded_num_tokens().
  AllSequenceLayoutPlanner.requires_backend_preinit: AllSequenceLayoutPlanner#requires_backend_preinit().
  AllSequenceLayoutPlanner.backend_preinit_world_size: AllSequenceLayoutPlanner#backend_preinit_world_size().
  AllSequenceLayoutPlanner.uses_selected_logits_hidden_states: AllSequenceLayoutPlanner#uses_selected_logits_hidden_states().
  AllSequenceLayoutPlanner.reserve_host_token_capacity: AllSequenceLayoutPlanner#reserve_host_token_capacity().
---
# Module: [`src/vllm_torchtpu/layers/core/sequence_layout.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py)

## Classes
### <a id="AllSequenceLayoutPlanner"></a>`AllSequenceLayoutPlanner`
- def: [`src/vllm_torchtpu/layers/core/sequence_layout.py:311`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L311)
- signature: `class AllSequenceLayoutPlanner:`
- members:
  - <a id="AllSequenceLayoutPlanner.backend_preinit_world_size"></a>`backend_preinit_world_size(self)` — [`L317`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L317)
  - <a id="AllSequenceLayoutPlanner.finalize_hidden_states"></a>`finalize_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None)` — [`L396`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L396)
  - <a id="AllSequenceLayoutPlanner.maybe_select_logits_hidden_states"></a>`maybe_select_logits_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None, logits_indices: torch.Tensor)` — [`L404`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L404)
  - <a id="AllSequenceLayoutPlanner.padded_num_tokens"></a>`padded_num_tokens(self, *, runner: Any, scheduler_output: Any, start_index: int, num_scheduled_tokens_per_req: Any)` — [`L365`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L365) — The ``local_padded_num_tokens`` of the plan ``prepare_real``
  - <a id="AllSequenceLayoutPlanner.prepare_dummy"></a>`prepare_dummy(self, *, num_tokens: int, num_reqs: int, kv_cache_initialized: bool)` — [`L378`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L378) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AllSequenceLayoutPlanner.prepare_real"></a>`prepare_real(self, *, runner: Any, scheduler_output: Any, start_index: int, num_reqs: int, num_scheduled_tokens_per_req: Any, total_num_scheduled_tokens: int, use_max_model_len: bool, target_num_reqs: int, padded_num_reqs: int)` — [`L329`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L329) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="AllSequenceLayoutPlanner.requires_backend_preinit"></a>`requires_backend_preinit(self)` — [`L313`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L313)
  - <a id="AllSequenceLayoutPlanner.reserve_host_token_capacity"></a>`reserve_host_token_capacity(self, runner: Any, required_num_tokens: int)` — [`L324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L324)
  - <a id="AllSequenceLayoutPlanner.uses_selected_logits_hidden_states"></a>`uses_selected_logits_hidden_states(self)` — [`L321`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L321)
- uses (calls/refs, reference-scoped): [`SequenceLayoutPlan`](sequence_layout.md#SequenceLayoutPlan), [`token_slice`](sequence_layout.md#SequenceLayoutPlan.token_slice), [`descriptor`](sequence_layout.md#SequenceLayoutPlan.descriptor), [`global_padded_num_tokens`](sequence_layout.md#SequenceLayoutPlan.global_padded_num_tokens), [`DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR), [`_all_padded_num_tokens`](sequence_layout.md#_all_padded_num_tokens), [`global_num_tokens`](sequence_layout.md#SequenceLayoutPlan.global_num_tokens), [`local_num_tokens`](sequence_layout.md#SequenceLayoutPlan.local_num_tokens), [`local_padded_num_tokens`](sequence_layout.md#SequenceLayoutPlan.local_padded_num_tokens)
- used by: [`prepare_real`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_real), [`prepare_dummy`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_dummy), [`padded_num_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.padded_num_tokens), [`create_sequence_layout_planner`](sequence_layout.md#create_sequence_layout_planner), [`_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN`](../../spec_decode/utils.md#_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN), [`__init__`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.__init__)

### <a id="SequenceLayoutDescriptor"></a>`SequenceLayoutDescriptor`
- def: [`src/vllm_torchtpu/layers/core/sequence_layout.py:36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L36)
- signature: `class SequenceLayoutDescriptor:`
- members:
  - <a id="SequenceLayoutDescriptor.cache_key"></a>`cache_key(self)` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L42)
  - <a id="SequenceLayoutDescriptor.kind"></a>`kind` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L37)
  - <a id="SequenceLayoutDescriptor.protocol"></a>`protocol` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L38)
  - <a id="SequenceLayoutDescriptor.version"></a>`version` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L39)
- uses (calls/refs, reference-scoped): [`SequenceLayoutKind`](sequence_layout.md#SequenceLayoutKind), [`ALL`](sequence_layout.md#SequenceLayoutKind.ALL), [`DEFAULT_SEQUENCE_LAYOUT_PROTOCOL`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_PROTOCOL)
- used by: [`PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR`](pcp_sequence_layout.md#PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR), [`aggregate_request_aligned_tensor`](sequence_layout.md#SequenceLayoutPlan.aggregate_request_aligned_tensor), [`is_pcp_streaming_sequence_layout_descriptor`](sequence_layout.md#is_pcp_streaming_sequence_layout_descriptor), [`sequence_layout_descriptor`](attention_metadata.md#AttentionMetadataBuilderContext.sequence_layout_descriptor), [`descriptor`](sequence_layout.md#SequenceLayoutPlan.descriptor), [`kind`](sequence_layout.md#SequenceLayoutPlan.kind), [`DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR)

### <a id="SequenceLayoutKind"></a>`SequenceLayoutKind`  ·  implements/extends Enum, str
- def: [`src/vllm_torchtpu/layers/core/sequence_layout.py:26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L26) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- signature: `class SequenceLayoutKind(str, Enum):`
- members:
  - <a id="SequenceLayoutKind.ALL"></a>`ALL` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L27)
  - <a id="SequenceLayoutKind.PARTIAL"></a>`PARTIAL` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L28)
- used by: [`_prepare_inputs`](../../runner/tpu_runner.md#TPUModelRunner._prepare_inputs), [`_pool_chunk`](../../runner/tpu_runner.md#TPUModelRunner._pool_chunk), [`localize_token_tensor_and_gather_indices`](sequence_layout.md#SequenceLayoutPlan.localize_token_tensor_and_gather_indices), [`PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR`](pcp_sequence_layout.md#PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR), [`is_pcp_streaming_attention_metadata`](sequence_layout.md#is_pcp_streaming_attention_metadata), [`is_pcp_streaming_sequence_layout_descriptor`](sequence_layout.md#is_pcp_streaming_sequence_layout_descriptor), [`_token_padding_update`](../../runner/tpu_runner.md#TPUModelRunner._token_padding_update), [`is_pcp_streaming_sequence_layout`](sequence_layout.md#is_pcp_streaming_sequence_layout), [`kind`](sequence_layout.md#SequenceLayoutPlan.kind), [`kind`](sequence_layout.md#SequenceLayoutDescriptor.kind), [`sequence_layout_kind`](attention_metadata.md#AttentionMetadata.sequence_layout_kind)

### <a id="SequenceLayoutPlan"></a>`SequenceLayoutPlan`
- def: [`src/vllm_torchtpu/layers/core/sequence_layout.py:60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L60) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- signature: `class SequenceLayoutPlan:`
- members:
  - <a id="SequenceLayoutPlan.aggregate_request_aligned_tensor"></a>`aggregate_request_aligned_tensor(self, local_tensor: torch.Tensor, owner_mask: torch.Tensor)` — [`L164`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L164) — Aggregate request-aligned owner rows for this sequence layout.
  - <a id="SequenceLayoutPlan.kind"></a>`kind(self)` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L80)
  - <a id="SequenceLayoutPlan.local_index_for_request_major_token"></a>`local_index_for_request_major_token(self, request_major_index: int)` — [`L83`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L83) — Map a runner chunk token index to this rank's local input index.
  - <a id="SequenceLayoutPlan.localize_token_tensor_and_gather_indices"></a>`localize_token_tensor_and_gather_indices(self, request_major_token_tensor: torch.Tensor, request_major_gather_indices: torch.Tensor, *, num_valid_gathers: int)` — [`L117`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L117) — Localize request-major tokens and request-aligned gather values. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="SequenceLayoutPlan.descriptor"></a>`descriptor` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L61)
  - <a id="SequenceLayoutPlan.global_num_tokens"></a>`global_num_tokens` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L63)
  - <a id="SequenceLayoutPlan.global_padded_num_tokens"></a>`global_padded_num_tokens` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L64)
  - <a id="SequenceLayoutPlan.local_num_tokens"></a>`local_num_tokens` — [`L65`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L65)
  - <a id="SequenceLayoutPlan.local_padded_num_tokens"></a>`local_padded_num_tokens` — [`L66`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L66)
  - <a id="SequenceLayoutPlan.logits_indices_cpu"></a>`logits_indices_cpu` — [`L67`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L67)
  - <a id="SequenceLayoutPlan.logits_local_indices_cpu"></a>`logits_local_indices_cpu` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L68)
  - <a id="SequenceLayoutPlan.logits_owner_mask_cpu"></a>`logits_owner_mask_cpu` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L69)
  - <a id="SequenceLayoutPlan.requires_hidden_state_gather"></a>`requires_hidden_state_gather` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L70)
  - <a id="SequenceLayoutPlan.token_slice"></a>`token_slice` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L62) — documented in [kv-transfer-and-disaggregated-serving](../../../../../concepts/kv-transfer-and-disaggregated-serving.md)
- protocol/private: <a id="SequenceLayoutPlan._packed_to_request_major_token_indices"></a>`_packed_to_request_major_token_indices`[`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L73), <a id="SequenceLayoutPlan._request_major_to_packed_token_indices"></a>`_request_major_to_packed_token_indices`[`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L77)
- uses (calls/refs, reference-scoped): [`SequenceLayoutKind`](sequence_layout.md#SequenceLayoutKind), [`is_pcp_streaming_sequence_layout_descriptor`](sequence_layout.md#is_pcp_streaming_sequence_layout_descriptor), [`cache_key`](sequence_layout.md#SequenceLayoutDescriptor.cache_key), [`ALL`](sequence_layout.md#SequenceLayoutKind.ALL), [`kind`](sequence_layout.md#SequenceLayoutDescriptor.kind), [`DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR`](sequence_layout.md#DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR), [`SequenceLayoutDescriptor`](sequence_layout.md#SequenceLayoutDescriptor), [`all_reduce_sum`](../../distributed/pcp.md#all_reduce_sum), [`_localize_token_tensor_and_gather_indices`](sequence_layout.md#_localize_token_tensor_and_gather_indices)
- used by: [`propose`](../../spec_decode/eagle3.md#Eagle3Proposer.propose), [`prepare_real`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_real), [`_prepare_draft_inputs`](../../spec_decode/eagle3.md#Eagle3Proposer._prepare_draft_inputs), [`prepare_dummy`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_dummy), [`prepare_real`](sequence_layout.md#AllSequenceLayoutPlanner.prepare_real), [`prepare_dummy`](sequence_layout.md#AllSequenceLayoutPlanner.prepare_dummy), [`record`](../../distributed/kv_transfer/kv_save_nan_check.md#KVSaveNanCheck.record), [`maybe_select_logits_hidden_states`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.maybe_select_logits_hidden_states), [`sequence_layout_plan`](../../spec_decode/utils.md#DraftChunkInputs.sequence_layout_plan), [`finalize_hidden_states`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.finalize_hidden_states), [`finalize_hidden_states`](sequence_layout.md#AllSequenceLayoutPlanner.finalize_hidden_states), [`finalize_hidden_states`](sequence_layout.md#SequenceLayoutPlanner.finalize_hidden_states), [`maybe_select_logits_hidden_states`](sequence_layout.md#AllSequenceLayoutPlanner.maybe_select_logits_hidden_states), [`maybe_select_logits_hidden_states`](sequence_layout.md#SequenceLayoutPlanner.maybe_select_logits_hidden_states), [`prepare_dummy`](sequence_layout.md#SequenceLayoutPlanner.prepare_dummy), [`prepare_real`](sequence_layout.md#SequenceLayoutPlanner.prepare_real)

### <a id="SequenceLayoutPlanner"></a>`SequenceLayoutPlanner`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/layers/core/sequence_layout.py:229`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L229)
- signature: `class SequenceLayoutPlanner(Protocol):`
- members:
  - <a id="SequenceLayoutPlanner.backend_preinit_world_size"></a>`backend_preinit_world_size(self)` — [`L234`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L234)
  - <a id="SequenceLayoutPlanner.finalize_hidden_states"></a>`finalize_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None)` — [`L274`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L274)
  - <a id="SequenceLayoutPlanner.maybe_select_logits_hidden_states"></a>`maybe_select_logits_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None, logits_indices: torch.Tensor)` — [`L280`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L280)
  - <a id="SequenceLayoutPlanner.padded_num_tokens"></a>`padded_num_tokens(self, *, runner: Any, scheduler_output: Any, start_index: int, num_scheduled_tokens_per_req: Any)` — [`L257`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L257)
  - <a id="SequenceLayoutPlanner.prepare_dummy"></a>`prepare_dummy(self, *, num_tokens: int, num_reqs: int, kv_cache_initialized: bool)` — [`L266`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L266)
  - <a id="SequenceLayoutPlanner.prepare_real"></a>`prepare_real(self, *, runner: Any, scheduler_output: Any, start_index: int, num_reqs: int, num_scheduled_tokens_per_req: Any, total_num_scheduled_tokens: int, use_max_model_len: bool, target_num_reqs: int, padded_num_reqs: int)` — [`L243`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L243)
  - <a id="SequenceLayoutPlanner.requires_backend_preinit"></a>`requires_backend_preinit(self)` — [`L231`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L231)
  - <a id="SequenceLayoutPlanner.reserve_host_token_capacity"></a>`reserve_host_token_capacity(self, runner: Any, required_num_tokens: int)` — [`L239`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L239)
  - <a id="SequenceLayoutPlanner.uses_selected_logits_hidden_states"></a>`uses_selected_logits_hidden_states(self)` — [`L237`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L237)
- uses (calls/refs, reference-scoped): [`SequenceLayoutPlan`](sequence_layout.md#SequenceLayoutPlan)
- used by: [`_mtp_prefill_only`](../../runner/tpu_runner.md#TPUModelRunner._mtp_prefill_only), [`create_sequence_layout_planner`](sequence_layout.md#create_sequence_layout_planner)

## Functions
- <a id="_all_padded_num_tokens"></a>`_all_padded_num_tokens(runner: Any, total_num_scheduled_tokens: int)` — [`L299`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L299) — The token bucket of a chunk every device holds whole, raised to the
- <a id="_first_ge"></a>`_first_ge(paddings: list[int] | tuple[int, ...], value: int)` — [`L288`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L288)
- <a id="_localize_token_tensor_and_gather_indices"></a>`_localize_token_tensor_and_gather_indices(request_major_token_tensor: torch.Tensor, request_major_gather_indices: torch.Tensor, local_packed_to_request: np.ndarray, request_to_packed: np.ndarray, local_start: int, local_end: int)` — [`L183`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L183) — Pure tensor transform shared by all partial sequence layout plans.
- <a id="create_sequence_layout_planner"></a>`create_sequence_layout_planner(vllm_config: Any)` — [`L414`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L414)
- <a id="is_pcp_streaming_attention_metadata"></a>`is_pcp_streaming_attention_metadata(attn_metadata: Any)` — [`L435`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L435) — documented in [kimi-k3-model](../../../../../concepts/kimi-k3-model.md)
- <a id="is_pcp_streaming_sequence_layout"></a>`is_pcp_streaming_sequence_layout(*, kind: str | SequenceLayoutKind, protocol: str)` — [`L423`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L423)
- <a id="is_pcp_streaming_sequence_layout_descriptor"></a>`is_pcp_streaming_sequence_layout_descriptor(descriptor: SequenceLayoutDescriptor)` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L49)

## Module values
- <a id="DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR"></a>`DEFAULT_SEQUENCE_LAYOUT_DESCRIPTOR` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L46)
- <a id="DEFAULT_SEQUENCE_LAYOUT_PROTOCOL"></a>`DEFAULT_SEQUENCE_LAYOUT_PROTOCOL` — [`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L31)
- <a id="PCP_STREAMING_SEQUENCE_LAYOUT_PROTOCOL"></a>`PCP_STREAMING_SEQUENCE_LAYOUT_PROTOCOL` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/sequence_layout.py#L32)

