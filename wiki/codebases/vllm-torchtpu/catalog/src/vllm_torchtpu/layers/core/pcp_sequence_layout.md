---
title: 'Module: src/vllm_torchtpu/layers/core/pcp_sequence_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/pcp_sequence_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.pcp_sequence_layout`/
symbols:
  prepare_pcp_sequence_layout: prepare_pcp_sequence_layout().
  PcpSequenceLayoutPlanner.prepare_real: PcpSequenceLayoutPlanner#prepare_real().
  PcpSequenceLayoutEligibility._evaluate_streaming_query: PcpSequenceLayoutEligibility#_evaluate_streaming_query().
  PcpSequenceLayoutEligibility.evaluate_runner_chunk: PcpSequenceLayoutEligibility#evaluate_runner_chunk().
  PcpSequenceLayoutPlanner.prepare_dummy: PcpSequenceLayoutPlanner#prepare_dummy().
  PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR: PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR.
  PcpSequenceLayoutPlanner.padded_num_tokens: PcpSequenceLayoutPlanner#padded_num_tokens().
  PcpSequenceLayoutEligibility._build_request_spans: PcpSequenceLayoutEligibility#_build_request_spans().
  PcpSequenceLayoutPlanner.enabled: PcpSequenceLayoutPlanner#enabled().
  PcpSequenceLayoutPlanner.maybe_select_logits_hidden_states: PcpSequenceLayoutPlanner#maybe_select_logits_hidden_states().
  PcpSequenceLayoutDecision.mode: PcpSequenceLayoutDecision#mode.
  PcpSequenceLayoutPlanner._decide: PcpSequenceLayoutPlanner#_decide().
  PcpRequestSpan.crosses_prompt_boundary: PcpRequestSpan#crosses_prompt_boundary().
  PcpSequenceLayoutEligibility.require_mode: PcpSequenceLayoutEligibility#require_mode().
  PcpSequenceLayoutPlanner.from_vllm_config: PcpSequenceLayoutPlanner#from_vllm_config().
  PcpSequenceLayoutMode: PcpSequenceLayoutMode#
  PcpSequenceLayoutEligibility.pcp_size: PcpSequenceLayoutEligibility#pcp_size.
  PcpSequenceLayoutDecision.enabled: PcpSequenceLayoutDecision#enabled().
  PcpSequenceLayoutPlanner.finalize_hidden_states: PcpSequenceLayoutPlanner#finalize_hidden_states().
  PcpSequenceLayoutDecision: PcpSequenceLayoutDecision#
  PcpRequestSpan.scheduled_tokens: PcpRequestSpan#scheduled_tokens.
  PcpSequenceLayoutEligibility.interleave_size: PcpSequenceLayoutEligibility#interleave_size.
  PcpSequenceLayoutEligibility._validate_execution_support: PcpSequenceLayoutEligibility#_validate_execution_support().
  PcpRequestSpan: PcpRequestSpan#
  PcpSequenceLayoutEligibility: PcpSequenceLayoutEligibility#
  PcpSequenceLayoutPlanner.__init__: PcpSequenceLayoutPlanner#__init__().
  PcpSequenceLayoutPlanner.eligibility: PcpSequenceLayoutPlanner#eligibility.
  PcpSequenceLayoutPlanner.backend_preinit_world_size: PcpSequenceLayoutPlanner#backend_preinit_world_size().
  PcpSequenceLayoutPlanner.reserve_host_token_capacity: PcpSequenceLayoutPlanner#reserve_host_token_capacity().
  PcpSequenceLayoutDecision.spans: PcpSequenceLayoutDecision#spans.
  PcpSequenceLayoutEligibility.from_vllm_config: PcpSequenceLayoutEligibility#from_vllm_config().
  PcpSequenceLayoutEligibility.enabled: PcpSequenceLayoutEligibility#enabled().
  PcpSequenceLayoutMode.DISABLED: PcpSequenceLayoutMode#DISABLED.
  PcpSequenceLayoutDecision.local_padded_tokens: PcpSequenceLayoutDecision#local_padded_tokens.
  logger: logger.
  _get_pcp_streaming_q_block_size: _get_pcp_streaming_q_block_size().
  PcpRequestSpan.computed_tokens: PcpRequestSpan#computed_tokens.
  PcpRequestSpan.prompt_tokens: PcpRequestSpan#prompt_tokens.
  PcpSequenceLayoutDecision.pcp_size: PcpSequenceLayoutDecision#pcp_size.
  PcpSequenceLayoutDecision.interleave_size: PcpSequenceLayoutDecision#interleave_size.
  PcpSequenceLayoutPlanner: PcpSequenceLayoutPlanner#
  PcpSequenceLayoutPlanner._all_planner: PcpSequenceLayoutPlanner#_all_planner.
  PcpSequenceLayoutPlanner.requires_backend_preinit: PcpSequenceLayoutPlanner#requires_backend_preinit().
  PcpSequenceLayoutPlanner.uses_selected_logits_hidden_states: PcpSequenceLayoutPlanner#uses_selected_logits_hidden_states().
  PcpSequenceLayoutMode.STREAMING: PcpSequenceLayoutMode#STREAMING.
  PcpRequestSpan.absolute_query_start: PcpRequestSpan#absolute_query_start.
  PcpSequenceLayoutDecision.absolute_query_start_offsets_per_req: PcpSequenceLayoutDecision#absolute_query_start_offsets_per_req.
  PcpSequenceLayoutDecision.token_owner_start_offsets_per_req: PcpSequenceLayoutDecision#token_owner_start_offsets_per_req.
  PcpSequenceLayoutDecision.local_token_counts: PcpSequenceLayoutDecision#local_token_counts.
  PcpSequenceLayoutDecision.global_padded_tokens: PcpSequenceLayoutDecision#global_padded_tokens.
  PcpPreparedBatch: PcpPreparedBatch#
  PcpPreparedBatch.local_token_slice: PcpPreparedBatch#local_token_slice.
  PcpPreparedBatch.padded_total_num_scheduled_tokens: PcpPreparedBatch#padded_total_num_scheduled_tokens.
  PcpPreparedBatch.local_total_num_scheduled_tokens: PcpPreparedBatch#local_total_num_scheduled_tokens.
  PcpPreparedBatch.local_padded_total_num_scheduled_tokens: PcpPreparedBatch#local_padded_total_num_scheduled_tokens.
  PcpPreparedBatch.logits_indices_cpu: PcpPreparedBatch#logits_indices_cpu.
  PcpPreparedBatch.logits_local_indices_cpu: PcpPreparedBatch#logits_local_indices_cpu.
  PcpPreparedBatch.logits_owner_mask_cpu: PcpPreparedBatch#logits_owner_mask_cpu.
  PcpPreparedBatch.packed_to_request_major_token_indices: PcpPreparedBatch#packed_to_request_major_token_indices.
  PcpPreparedBatch.request_major_to_packed_token_indices: PcpPreparedBatch#request_major_to_packed_token_indices.
  _ensure_host_token_buffer_capacity: _ensure_host_token_buffer_capacity().
  PcpSequenceLayoutDecision.pcp_alignment: PcpSequenceLayoutDecision#pcp_alignment.
  PcpSequenceLayoutDecision.local_required_tokens: PcpSequenceLayoutDecision#local_required_tokens.
  PcpSequenceLayoutEligibility._BOUNDARY_MESSAGE: PcpSequenceLayoutEligibility#_BOUNDARY_MESSAGE.
  PcpSequenceLayoutEligibility.dcp_size: PcpSequenceLayoutEligibility#dcp_size.
  _debug_pcp_layout_window: _debug_pcp_layout_window().
  PcpSequenceLayoutEligibility.__init__: PcpSequenceLayoutEligibility#__init__().
  PcpSequenceLayoutEligibility.pipeline_parallel_size: PcpSequenceLayoutEligibility#pipeline_parallel_size.
  PcpSequenceLayoutEligibility.async_scheduling: PcpSequenceLayoutEligibility#async_scheduling.
---
# Module: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py)

## Classes
### <a id="PcpPreparedBatch"></a>`PcpPreparedBatch`
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:339`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L339)
- signature: `class PcpPreparedBatch:`
- members:
  - <a id="PcpPreparedBatch.local_padded_total_num_scheduled_tokens"></a>`local_padded_total_num_scheduled_tokens` — [`L343`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L343)
  - <a id="PcpPreparedBatch.local_token_slice"></a>`local_token_slice` — [`L340`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L340)
  - <a id="PcpPreparedBatch.local_total_num_scheduled_tokens"></a>`local_total_num_scheduled_tokens` — [`L342`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L342)
  - <a id="PcpPreparedBatch.logits_indices_cpu"></a>`logits_indices_cpu` — [`L344`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L344)
  - <a id="PcpPreparedBatch.logits_local_indices_cpu"></a>`logits_local_indices_cpu` — [`L345`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L345)
  - <a id="PcpPreparedBatch.logits_owner_mask_cpu"></a>`logits_owner_mask_cpu` — [`L346`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L346)
  - <a id="PcpPreparedBatch.packed_to_request_major_token_indices"></a>`packed_to_request_major_token_indices` — [`L347`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L347)
  - <a id="PcpPreparedBatch.padded_total_num_scheduled_tokens"></a>`padded_total_num_scheduled_tokens` — [`L341`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L341)
  - <a id="PcpPreparedBatch.request_major_to_packed_token_indices"></a>`request_major_to_packed_token_indices` — [`L348`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L348)
- used by: [`prepare_pcp_sequence_layout`](pcp_sequence_layout.md#prepare_pcp_sequence_layout), [`prepare_real`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_real)

### <a id="PcpRequestSpan"></a>`PcpRequestSpan`
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:74`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L74)
- signature: `class PcpRequestSpan:`
- members:
  - <a id="PcpRequestSpan.crosses_prompt_boundary"></a>`crosses_prompt_boundary(self)` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L81)
  - <a id="PcpRequestSpan.absolute_query_start"></a>`absolute_query_start` — [`L78`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L78)
  - <a id="PcpRequestSpan.computed_tokens"></a>`computed_tokens` — [`L75`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L75)
  - <a id="PcpRequestSpan.prompt_tokens"></a>`prompt_tokens` — [`L77`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L77)
  - <a id="PcpRequestSpan.scheduled_tokens"></a>`scheduled_tokens` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L76)
- used by: [`_evaluate_streaming_query`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility._evaluate_streaming_query), [`evaluate_runner_chunk`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.evaluate_runner_chunk), [`_build_request_spans`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility._build_request_spans), [`spans`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.spans)

### <a id="PcpSequenceLayoutDecision"></a>`PcpSequenceLayoutDecision`
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L90)
- signature: `class PcpSequenceLayoutDecision:`
- members:
  - <a id="PcpSequenceLayoutDecision.enabled"></a>`enabled(self)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L104)
  - <a id="PcpSequenceLayoutDecision.absolute_query_start_offsets_per_req"></a>`absolute_query_start_offsets_per_req` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L96)
  - <a id="PcpSequenceLayoutDecision.global_padded_tokens"></a>`global_padded_tokens` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L101)
  - <a id="PcpSequenceLayoutDecision.interleave_size"></a>`interleave_size` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L94)
  - <a id="PcpSequenceLayoutDecision.local_padded_tokens"></a>`local_padded_tokens` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L100)
  - <a id="PcpSequenceLayoutDecision.local_required_tokens"></a>`local_required_tokens` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L99)
  - <a id="PcpSequenceLayoutDecision.local_token_counts"></a>`local_token_counts` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L98)
  - <a id="PcpSequenceLayoutDecision.mode"></a>`mode` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L91)
  - <a id="PcpSequenceLayoutDecision.pcp_alignment"></a>`pcp_alignment` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L95)
  - <a id="PcpSequenceLayoutDecision.pcp_size"></a>`pcp_size` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L93)
  - <a id="PcpSequenceLayoutDecision.spans"></a>`spans` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L92)
  - <a id="PcpSequenceLayoutDecision.token_owner_start_offsets_per_req"></a>`token_owner_start_offsets_per_req` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L97)
- uses (calls/refs, reference-scoped): [`PcpSequenceLayoutMode`](pcp_sequence_layout.md#PcpSequenceLayoutMode), [`PcpRequestSpan`](pcp_sequence_layout.md#PcpRequestSpan), [`DISABLED`](pcp_sequence_layout.md#PcpSequenceLayoutMode.DISABLED)
- used by: [`prepare_pcp_sequence_layout`](pcp_sequence_layout.md#prepare_pcp_sequence_layout), [`prepare_real`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_real), [`_evaluate_streaming_query`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility._evaluate_streaming_query), [`evaluate_runner_chunk`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.evaluate_runner_chunk), [`padded_num_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.padded_num_tokens), [`_decide`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner._decide), [`require_mode`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.require_mode)

### <a id="PcpSequenceLayoutEligibility"></a>`PcpSequenceLayoutEligibility`
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L108)
- signature: `class PcpSequenceLayoutEligibility:`
- members:
  - <a id="PcpSequenceLayoutEligibility.enabled"></a>`enabled(self)` — [`L146`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L146)
  - <a id="PcpSequenceLayoutEligibility.evaluate_runner_chunk"></a>`evaluate_runner_chunk(self, *, input_batch: Any, scheduler_output: Any, start_index: int, num_reqs: int, num_scheduled_tokens_per_req: np.ndarray, absolute_query_start_offsets_per_req: np.ndarray | None = None, num_tokens_paddings: Sequence[int] | None = None, max_num_tokens: int | None = None, dp_target_bucket: int | None = None)` — [`L149`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L149) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="PcpSequenceLayoutEligibility.from_vllm_config"></a>`from_vllm_config(cls, vllm_config: Any)` — [`L130`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L130)
  - <a id="PcpSequenceLayoutEligibility.require_mode"></a>`require_mode(decision: PcpSequenceLayoutDecision, expected: PcpSequenceLayoutMode)` — [`L191`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L191)
  - <a id="PcpSequenceLayoutEligibility.async_scheduling"></a>`async_scheduling` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L127)
  - <a id="PcpSequenceLayoutEligibility.dcp_size"></a>`dcp_size` — [`L125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L125)
  - <a id="PcpSequenceLayoutEligibility.interleave_size"></a>`interleave_size` — [`L124`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L124)
  - <a id="PcpSequenceLayoutEligibility.pcp_size"></a>`pcp_size` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L123)
  - <a id="PcpSequenceLayoutEligibility.pipeline_parallel_size"></a>`pipeline_parallel_size` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L126)
- protocol/private: <a id="PcpSequenceLayoutEligibility._BOUNDARY_MESSAGE"></a>`_BOUNDARY_MESSAGE`[`L109`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L109), <a id="PcpSequenceLayoutEligibility.__init__"></a>`__init__`[`L114`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L114), <a id="PcpSequenceLayoutEligibility._build_request_spans"></a>`_build_request_spans`[`L201`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L201), <a id="PcpSequenceLayoutEligibility._evaluate_streaming_query"></a>`_evaluate_streaming_query`[`L266`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L266), <a id="PcpSequenceLayoutEligibility._validate_execution_support"></a>`_validate_execution_support`[`L256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L256)
- uses (calls/refs, reference-scoped): [`mode`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.mode), [`crosses_prompt_boundary`](pcp_sequence_layout.md#PcpRequestSpan.crosses_prompt_boundary), [`PcpSequenceLayoutMode`](pcp_sequence_layout.md#PcpSequenceLayoutMode), [`PcpSequenceLayoutDecision`](pcp_sequence_layout.md#PcpSequenceLayoutDecision), [`pcp_local_token_counts`](../../kernels/experimental/pcp_streaming_rpa/pcp_layout.md#pcp_local_token_counts), [`scheduled_tokens`](pcp_sequence_layout.md#PcpRequestSpan.scheduled_tokens), [`PcpRequestSpan`](pcp_sequence_layout.md#PcpRequestSpan), [`spans`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.spans), [`DISABLED`](pcp_sequence_layout.md#PcpSequenceLayoutMode.DISABLED), [`local_padded_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.local_padded_tokens), [`_get_pcp_streaming_q_block_size`](pcp_sequence_layout.md#_get_pcp_streaming_q_block_size), [`_first_ge`](sequence_layout.md#_first_ge), [`computed_tokens`](pcp_sequence_layout.md#PcpRequestSpan.computed_tokens), [`interleave_size`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.interleave_size), [`pcp_size`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.pcp_size), [`prompt_tokens`](pcp_sequence_layout.md#PcpRequestSpan.prompt_tokens), [`STREAMING`](pcp_sequence_layout.md#PcpSequenceLayoutMode.STREAMING), [`absolute_query_start`](pcp_sequence_layout.md#PcpRequestSpan.absolute_query_start), [`absolute_query_start_offsets_per_req`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.absolute_query_start_offsets_per_req), [`global_padded_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.global_padded_tokens), [`local_token_counts`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.local_token_counts), [`token_owner_start_offsets_per_req`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.token_owner_start_offsets_per_req), [`local_required_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.local_required_tokens), [`pcp_alignment`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.pcp_alignment)
- used by: [`prepare_pcp_sequence_layout`](pcp_sequence_layout.md#prepare_pcp_sequence_layout), [`prepare_dummy`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_dummy), [`enabled`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.enabled), [`_decide`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner._decide), [`from_vllm_config`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.from_vllm_config), [`__init__`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.__init__), [`backend_preinit_world_size`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.backend_preinit_world_size)

### <a id="PcpSequenceLayoutMode"></a>`PcpSequenceLayoutMode`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L68)
- signature: `class PcpSequenceLayoutMode(Enum):`
- members:
  - <a id="PcpSequenceLayoutMode.DISABLED"></a>`DISABLED` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L69)
  - <a id="PcpSequenceLayoutMode.STREAMING"></a>`STREAMING` — [`L70`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L70)
- used by: [`prepare_pcp_sequence_layout`](pcp_sequence_layout.md#prepare_pcp_sequence_layout), [`prepare_real`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.prepare_real), [`_evaluate_streaming_query`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility._evaluate_streaming_query), [`evaluate_runner_chunk`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.evaluate_runner_chunk), [`padded_num_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutPlanner.padded_num_tokens), [`mode`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.mode), [`require_mode`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.require_mode), [`enabled`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.enabled)

### <a id="PcpSequenceLayoutPlanner"></a>`PcpSequenceLayoutPlanner`
- def: [`src/vllm_torchtpu/layers/core/pcp_sequence_layout.py:351`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L351)
- signature: `class PcpSequenceLayoutPlanner:`
- members:
  - <a id="PcpSequenceLayoutPlanner.backend_preinit_world_size"></a>`backend_preinit_world_size(self)` — [`L369`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L369)
  - <a id="PcpSequenceLayoutPlanner.enabled"></a>`enabled(self)` — [`L361`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L361)
  - <a id="PcpSequenceLayoutPlanner.finalize_hidden_states"></a>`finalize_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None)` — [`L516`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L516)
  - <a id="PcpSequenceLayoutPlanner.from_vllm_config"></a>`from_vllm_config(cls, vllm_config: Any)` — [`L357`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L357)
  - <a id="PcpSequenceLayoutPlanner.maybe_select_logits_hidden_states"></a>`maybe_select_logits_hidden_states(self, hidden_states: torch.Tensor, plan: SequenceLayoutPlan | None, logits_indices: torch.Tensor)` — [`L525`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L525)
  - <a id="PcpSequenceLayoutPlanner.padded_num_tokens"></a>`padded_num_tokens(self, *, runner: Any, scheduler_output: Any, start_index: int, num_scheduled_tokens_per_req: np.ndarray)` — [`L464`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L464) — The ``local_padded_num_tokens`` of the plan ``prepare_real``
  - <a id="PcpSequenceLayoutPlanner.prepare_dummy"></a>`prepare_dummy(self, *, num_tokens: int, num_reqs: int, kv_cache_initialized: bool)` — [`L491`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L491)
  - <a id="PcpSequenceLayoutPlanner.prepare_real"></a>`prepare_real(self, *, runner: Any, scheduler_output: Any, start_index: int, num_reqs: int, num_scheduled_tokens_per_req: np.ndarray, total_num_scheduled_tokens: int, use_max_model_len: bool, target_num_reqs: int, padded_num_reqs: int)` — [`L382`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L382) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
  - <a id="PcpSequenceLayoutPlanner.requires_backend_preinit"></a>`requires_backend_preinit(self)` — [`L365`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L365)
  - <a id="PcpSequenceLayoutPlanner.reserve_host_token_capacity"></a>`reserve_host_token_capacity(self, runner: Any, required_num_tokens: int)` — [`L376`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L376)
  - <a id="PcpSequenceLayoutPlanner.uses_selected_logits_hidden_states"></a>`uses_selected_logits_hidden_states(self)` — [`L373`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L373)
  - <a id="PcpSequenceLayoutPlanner.eligibility"></a>`eligibility` — [`L353`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L353)
- protocol/private: <a id="PcpSequenceLayoutPlanner.__init__"></a>`__init__`[`L352`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L352), <a id="PcpSequenceLayoutPlanner._all_planner"></a>`_all_planner`[`L354`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L354), <a id="PcpSequenceLayoutPlanner._decide"></a>`_decide`[`L445`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L445)
- uses (calls/refs, reference-scoped): [`prepare_pcp_sequence_layout`](pcp_sequence_layout.md#prepare_pcp_sequence_layout), [`evaluate_runner_chunk`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.evaluate_runner_chunk), [`prepare_real`](sequence_layout.md#AllSequenceLayoutPlanner.prepare_real), [`prepare_dummy`](sequence_layout.md#AllSequenceLayoutPlanner.prepare_dummy), [`SequenceLayoutPlan`](sequence_layout.md#SequenceLayoutPlan), [`PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR`](pcp_sequence_layout.md#PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR), [`token_slice`](sequence_layout.md#SequenceLayoutPlan.token_slice), [`mode`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.mode), [`descriptor`](sequence_layout.md#SequenceLayoutPlan.descriptor), [`PcpSequenceLayoutMode`](pcp_sequence_layout.md#PcpSequenceLayoutMode), [`global_padded_num_tokens`](sequence_layout.md#SequenceLayoutPlan.global_padded_num_tokens), [`pcp_size`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.pcp_size), [`PcpSequenceLayoutDecision`](pcp_sequence_layout.md#PcpSequenceLayoutDecision), [`all_reduce_sum`](../../distributed/pcp.md#all_reduce_sum), [`AllSequenceLayoutPlanner`](sequence_layout.md#AllSequenceLayoutPlanner), [`PcpSequenceLayoutEligibility`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility), [`all_gather_equal_tokens`](../../distributed/pcp.md#all_gather_equal_tokens), [`enabled`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.enabled), [`from_vllm_config`](pcp_sequence_layout.md#PcpSequenceLayoutEligibility.from_vllm_config), [`DISABLED`](pcp_sequence_layout.md#PcpSequenceLayoutMode.DISABLED), [`global_num_tokens`](sequence_layout.md#SequenceLayoutPlan.global_num_tokens), [`local_num_tokens`](sequence_layout.md#SequenceLayoutPlan.local_num_tokens), [`local_padded_num_tokens`](sequence_layout.md#SequenceLayoutPlan.local_padded_num_tokens), [`local_padded_tokens`](pcp_sequence_layout.md#PcpSequenceLayoutDecision.local_padded_tokens), [`padded_num_tokens`](sequence_layout.md#AllSequenceLayoutPlanner.padded_num_tokens), [`_packed_to_request_major_token_indices`](sequence_layout.md#SequenceLayoutPlan._packed_to_request_major_token_indices), [`_request_major_to_packed_token_indices`](sequence_layout.md#SequenceLayoutPlan._request_major_to_packed_token_indices), [`logits_local_indices_cpu`](sequence_layout.md#SequenceLayoutPlan.logits_local_indices_cpu), [`logits_owner_mask_cpu`](sequence_layout.md#SequenceLayoutPlan.logits_owner_mask_cpu), [`requires_hidden_state_gather`](sequence_layout.md#SequenceLayoutPlan.requires_hidden_state_gather), [`_ensure_host_token_buffer_capacity`](pcp_sequence_layout.md#_ensure_host_token_buffer_capacity), [`local_padded_total_num_scheduled_tokens`](pcp_sequence_layout.md#PcpPreparedBatch.local_padded_total_num_scheduled_tokens), [`local_token_slice`](pcp_sequence_layout.md#PcpPreparedBatch.local_token_slice), [`local_total_num_scheduled_tokens`](pcp_sequence_layout.md#PcpPreparedBatch.local_total_num_scheduled_tokens), [`logits_indices_cpu`](pcp_sequence_layout.md#PcpPreparedBatch.logits_indices_cpu), [`logits_local_indices_cpu`](pcp_sequence_layout.md#PcpPreparedBatch.logits_local_indices_cpu), [`logits_owner_mask_cpu`](pcp_sequence_layout.md#PcpPreparedBatch.logits_owner_mask_cpu), [`packed_to_request_major_token_indices`](pcp_sequence_layout.md#PcpPreparedBatch.packed_to_request_major_token_indices), [`padded_total_num_scheduled_tokens`](pcp_sequence_layout.md#PcpPreparedBatch.padded_total_num_scheduled_tokens), [`request_major_to_packed_token_indices`](pcp_sequence_layout.md#PcpPreparedBatch.request_major_to_packed_token_indices)  (+1 more)
- used by: [`create_sequence_layout_planner`](sequence_layout.md#create_sequence_layout_planner)

## Functions
- <a id="_debug_pcp_layout_window"></a>`_debug_pcp_layout_window(runner: Any, *, pcp_rank: int, local_token_slice: slice, local_padded_tokens: int, logits_indices: np.ndarray)` — [`L603`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L603)
- <a id="_ensure_host_token_buffer_capacity"></a>`_ensure_host_token_buffer_capacity(runner: Any, required_num_tokens: int)` — [`L550`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L550) — Grow CPU-only token staging buffers for partial sequence layouts.
- <a id="_get_pcp_streaming_q_block_size"></a>`_get_pcp_streaming_q_block_size()` — [`L60`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L60)
- <a id="prepare_pcp_sequence_layout"></a>`prepare_pcp_sequence_layout(runner: Any, scheduler_output: Any, start_index: int, num_reqs: int, num_scheduled_tokens_per_req: np.ndarray, total_num_scheduled_tokens: int, use_max_model_len: bool, target_num_reqs: int, padded_num_reqs: int, get_native_pcp_rank: Any | None = None, get_native_pcp_world_size: Any | None = None, decision: PcpSequenceLayoutDecision | None = None)` — [`L638`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L638) — Prepare native PCP streaming host state for a real request. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)

## Module values
- <a id="PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR"></a>`PCP_STREAMING_SEQUENCE_LAYOUT_DESCRIPTOR` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L53) — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="logger"></a>`logger` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/pcp_sequence_layout.py#L51)

