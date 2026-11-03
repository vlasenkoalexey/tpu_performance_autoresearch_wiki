---
title: 'Module: src/vllm_torchtpu/runner/tpu_runner_async_output.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/tpu_runner_async_output.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.tpu_runner_async_output`/
symbols:
  AsyncTPUModelRunnerOutput.get_output: AsyncTPUModelRunnerOutput#get_output().
  AsyncTPUCopyState.wait: AsyncTPUCopyState#wait().
  INVALID_TOKEN_ID: INVALID_TOKEN_ID.
  AsyncTPUCopyState.from_device_chunks: AsyncTPUCopyState#from_device_chunks().
  AsyncPreResults.wait_for_copy: AsyncPreResults#wait_for_copy().
  AsyncTPUCopyState.sampled_token_ids_cpu: AsyncTPUCopyState#sampled_token_ids_cpu().
  spec_logprobs_lists: spec_logprobs_lists().
  SpecLogprobsChunk: SpecLogprobsChunk#
  AsyncPreResults.req_id_to_index_copy: AsyncPreResults#req_id_to_index_copy.
  SpecLogprobsChunk.tensors: SpecLogprobsChunk#tensors.
  AsyncTPUModelRunnerOutput._model_runner_output: AsyncTPUModelRunnerOutput#_model_runner_output.
  AsyncPreResults.copy_state: AsyncPreResults#copy_state.
  AsyncPreResults.num_draft_per_req: AsyncPreResults#num_draft_per_req.
  AsyncTPUModelRunnerOutput: AsyncTPUModelRunnerOutput#
  SpecLogprobsChunk.row_starts: SpecLogprobsChunk#row_starts.
  AsyncTPUCopyState: AsyncTPUCopyState#
  AsyncPreResults.request_seq_lens: AsyncPreResults#request_seq_lens.
  AsyncTPUModelRunnerOutput.copy_state: AsyncTPUModelRunnerOutput#copy_state.
  AsyncTPUCopyState.spec_logprobs: AsyncTPUCopyState#spec_logprobs.
  assemble_spec_next_tokens: assemble_spec_next_tokens().
  compute_num_rejected: compute_num_rejected().
  AsyncTPUCopyState._sampled_token_ids_cpu: AsyncTPUCopyState#_sampled_token_ids_cpu.
  AsyncPreResults.next_tokens_tpu: AsyncPreResults#next_tokens_tpu.
  AsyncPreResults.spec_decode_num_rejected_tokens: AsyncPreResults#spec_decode_num_rejected_tokens.
  AsyncTPUCopyState.fence_pending_device_work: AsyncTPUCopyState#fence_pending_device_work().
  AsyncPreResults: AsyncPreResults#
  AsyncTPUModelRunnerOutput.__init__: AsyncTPUModelRunnerOutput#__init__().
  AsyncTPUCopyState.copy_ready_event: AsyncTPUCopyState#copy_ready_event.
  AsyncTPUCopyState.completed: AsyncTPUCopyState#completed.
  AsyncPreResults.req_ids: AsyncPreResults#req_ids.
  AsyncPreResults.discard_sampled_tokens_req_indices: AsyncPreResults#discard_sampled_tokens_req_indices.
  AsyncTPUModelRunnerOutput.discard_sampled_tokens_req_indices: AsyncTPUModelRunnerOutput#discard_sampled_tokens_req_indices.
  subtract_num_rejected_tokens: subtract_num_rejected_tokens().
  extract_draft_token_ids: extract_draft_token_ids().
  AsyncTPUCopyState.chunks_cpu: AsyncTPUCopyState#chunks_cpu.
  AsyncTPUCopyState.chunk_real_lens: AsyncTPUCopyState#chunk_real_lens.
  AsyncTPUCopyState.chunks_tpu: AsyncTPUCopyState#chunks_tpu.
  AsyncTPUCopyState._spec_logprobs_tpu: AsyncTPUCopyState#_spec_logprobs_tpu.
---
# Module: [`src/vllm_torchtpu/runner/tpu_runner_async_output.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py)

## Classes
### <a id="AsyncPreResults"></a>`AsyncPreResults`
- def: [`src/vllm_torchtpu/runner/tpu_runner_async_output.py:161`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L161)
- signature: `class AsyncPreResults:`
- members:
  - <a id="AsyncPreResults.wait_for_copy"></a>`wait_for_copy(self)` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L178)
  - <a id="AsyncPreResults.copy_state"></a>`copy_state` — [`L167`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L167)
  - <a id="AsyncPreResults.discard_sampled_tokens_req_indices"></a>`discard_sampled_tokens_req_indices` — [`L165`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L165)
  - <a id="AsyncPreResults.next_tokens_tpu"></a>`next_tokens_tpu` — [`L163`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L163)
  - <a id="AsyncPreResults.num_draft_per_req"></a>`num_draft_per_req` — [`L176`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L176)
  - <a id="AsyncPreResults.req_id_to_index_copy"></a>`req_id_to_index_copy` — [`L166`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L166)
  - <a id="AsyncPreResults.req_ids"></a>`req_ids` — [`L162`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L162)
  - <a id="AsyncPreResults.request_seq_lens"></a>`request_seq_lens` — [`L164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L164)
  - <a id="AsyncPreResults.spec_decode_num_rejected_tokens"></a>`spec_decode_num_rejected_tokens` — [`L171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L171)
- uses (calls/refs, reference-scoped): [`wait`](tpu_runner_async_output.md#AsyncTPUCopyState.wait), [`sampled_token_ids_cpu`](tpu_runner_async_output.md#AsyncTPUCopyState.sampled_token_ids_cpu), [`AsyncTPUCopyState`](tpu_runner_async_output.md#AsyncTPUCopyState)
- used by: [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`position_ids`](tpu_runner.md#TPUModelRunner.position_ids), [`_collect_mamba_state_seed_copies`](tpu_runner.md#TPUModelRunner._collect_mamba_state_seed_copies), [`_update_states`](tpu_runner.md#TPUModelRunner._update_states), [`_pre_async_results`](tpu_runner.md#TPUModelRunner._pre_async_results), [`_warmup_spec_decode_cleanup`](tpu_runner.md#TPUModelRunner._warmup_spec_decode_cleanup), [`_settle_draft_placeholders_for_min_tokens`](tpu_runner.md#TPUModelRunner._settle_draft_placeholders_for_min_tokens), [`_modify_prev_results`](tpu_runner.md#TPUModelRunner._modify_prev_results), [`_apply_async_token_substitution`](tpu_runner.md#TPUModelRunner._apply_async_token_substitution), [`_prepare_async_token_substitution_indices`](tpu_runner.md#TPUModelRunner._prepare_async_token_substitution_indices), [`_cached_pre_next_tokens_indices`](tpu_runner.md#TPUModelRunner._cached_pre_next_tokens_indices), [`_flush_disjoint_async_results`](tpu_runner.md#TPUModelRunner._flush_disjoint_async_results)

### <a id="AsyncTPUCopyState"></a>`AsyncTPUCopyState`
- def: [`src/vllm_torchtpu/runner/tpu_runner_async_output.py:79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L79)
- doc: Async D2H copy state for sampled tokens.
- signature: `class AsyncTPUCopyState:`
- members:
  - <a id="AsyncTPUCopyState.fence_pending_device_work"></a>`fence_pending_device_work(self)` — [`L127`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L127) — Re-arms the ready event behind everything enqueued on the device
  - <a id="AsyncTPUCopyState.from_device_chunks"></a>`from_device_chunks(cls, chunks_tpu: list[torch.Tensor], chunk_real_lens: list[int], spec_logprobs: list[SpecLogprobsChunk] | None = None)` — [`L101`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L101)
  - <a id="AsyncTPUCopyState.sampled_token_ids_cpu"></a>`sampled_token_ids_cpu(self)` — [`L145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L145) — Return the unpadded concatenated CPU tensor.
  - <a id="AsyncTPUCopyState.wait"></a>`wait(self)` — [`L136`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L136)
  - <a id="AsyncTPUCopyState.chunk_real_lens"></a>`chunk_real_lens` — [`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L89)
  - <a id="AsyncTPUCopyState.chunks_cpu"></a>`chunks_cpu` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L88)
  - <a id="AsyncTPUCopyState.chunks_tpu"></a>`chunks_tpu` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L91)
  - <a id="AsyncTPUCopyState.completed"></a>`completed` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L92)
  - <a id="AsyncTPUCopyState.copy_ready_event"></a>`copy_ready_event` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L90)
  - <a id="AsyncTPUCopyState.spec_logprobs"></a>`spec_logprobs` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L96)
- protocol/private: <a id="AsyncTPUCopyState._sampled_token_ids_cpu"></a>`_sampled_token_ids_cpu`[`L93`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L93), <a id="AsyncTPUCopyState._spec_logprobs_tpu"></a>`_spec_logprobs_tpu`[`L98`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L98)
- uses (calls/refs, reference-scoped): [`SpecLogprobsChunk`](tpu_runner_async_output.md#SpecLogprobsChunk), [`tensors`](tpu_runner_async_output.md#SpecLogprobsChunk.tensors), [`row_starts`](tpu_runner_async_output.md#SpecLogprobsChunk.row_starts)
- used by: [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`get_output`](tpu_runner_async_output.md#AsyncTPUModelRunnerOutput.get_output), [`wait_for_copy`](tpu_runner_async_output.md#AsyncPreResults.wait_for_copy), [`copy_state`](tpu_runner_async_output.md#AsyncPreResults.copy_state), [`__init__`](tpu_runner_async_output.md#AsyncTPUModelRunnerOutput.__init__)

### <a id="AsyncTPUModelRunnerOutput"></a>`AsyncTPUModelRunnerOutput`
- def: [`src/vllm_torchtpu/runner/tpu_runner_async_output.py:185`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L185)
- doc: Holds asynchronous model output specifically from a TPU runner.
- signature: `class AsyncTPUModelRunnerOutput(AsyncModelRunnerOutput):`
- members:
  - <a id="AsyncTPUModelRunnerOutput.get_output"></a>`get_output(self)` — [`L198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L198)
  - <a id="AsyncTPUModelRunnerOutput.copy_state"></a>`copy_state` — [`L195`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L195)
  - <a id="AsyncTPUModelRunnerOutput.discard_sampled_tokens_req_indices"></a>`discard_sampled_tokens_req_indices` — [`L196`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L196)
- protocol/private: <a id="AsyncTPUModelRunnerOutput.__init__"></a>`__init__`[`L188`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L188), <a id="AsyncTPUModelRunnerOutput._model_runner_output"></a>`_model_runner_output`[`L194`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L194)
- uses (calls/refs, reference-scoped): [`wait`](tpu_runner_async_output.md#AsyncTPUCopyState.wait), [`INVALID_TOKEN_ID`](tpu_runner_async_output.md#INVALID_TOKEN_ID), [`sampled_token_ids_cpu`](tpu_runner_async_output.md#AsyncTPUCopyState.sampled_token_ids_cpu), [`spec_logprobs_lists`](tpu_runner_async_output.md#spec_logprobs_lists), [`AsyncTPUCopyState`](tpu_runner_async_output.md#AsyncTPUCopyState), [`spec_logprobs`](tpu_runner_async_output.md#AsyncTPUCopyState.spec_logprobs)
- used by: [`execute_model`](tpu_runner.md#TPUModelRunner.execute_model), [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`get_execute_model_output`](../executors/ray_distributed_executor.md#RayWorkerWrapper.get_execute_model_output)

### <a id="SpecLogprobsChunk"></a>`SpecLogprobsChunk`
- def: [`src/vllm_torchtpu/runner/tpu_runner_async_output.py:30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L30)
- doc: One chunk's logprobs in a spec-decode step, one row per logits row.
- signature: `class SpecLogprobsChunk:`
- members:
  - <a id="SpecLogprobsChunk.row_starts"></a>`row_starts` — [`L44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L44)
  - <a id="SpecLogprobsChunk.tensors"></a>`tensors` — [`L42`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L42)
- used by: [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`from_device_chunks`](tpu_runner_async_output.md#AsyncTPUCopyState.from_device_chunks), [`spec_logprobs_lists`](tpu_runner_async_output.md#spec_logprobs_lists), [`spec_logprobs`](tpu_runner_async_output.md#AsyncTPUCopyState.spec_logprobs)

## Functions
- <a id="assemble_spec_next_tokens"></a>`assemble_spec_next_tokens(next_tokens: torch.Tensor, drafts: torch.Tensor, num_reqs: int | None = None)` — [`L233`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L233) — Async substitution source for speculative decoding.
- <a id="compute_num_rejected"></a>`compute_num_rejected(next_tokens: torch.Tensor, num_draft: torch.Tensor)` — [`L318`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L318) — Per-request rejected-draft count from the rejection output, on-device.
- <a id="extract_draft_token_ids"></a>`extract_draft_token_ids(input_ids: torch.Tensor, logits_indices: torch.Tensor, target_logits_indices: torch.Tensor)` — [`L307`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L307) — Gather the draft tokens the target just verified, from the (post-async-
- <a id="spec_logprobs_lists"></a>`spec_logprobs_lists(chunks: list[SpecLogprobsChunk], gen_lens: list[int])` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L47) — Keep each request's accepted rows, in request order.
- <a id="subtract_num_rejected_tokens"></a>`subtract_num_rejected_tokens(seq_lens: torch.Tensor, positions: torch.Tensor, num_rejected: torch.Tensor, seq_lens_subtract_indices: torch.Tensor, positions_subtract_indices: torch.Tensor)` — [`L264`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L264) — Remove the previous async step's per-request rejected-token over-count.

## Module values
- <a id="INVALID_TOKEN_ID"></a>`INVALID_TOKEN_ID` — [`L26`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_runner_async_output.py#L26)

