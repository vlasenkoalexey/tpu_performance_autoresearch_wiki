---
title: 'Module: src/vllm_torchtpu/spec_decode/dflash.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/dflash.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.dflash`/
symbols:
  DFlashProposer.load_model: DFlashProposer#load_model().
  DFlashProposer.draft_model: DFlashProposer#draft_model.
  DFlashProposer.precompile: DFlashProposer#precompile().
  DFlashProposer._prepare_dflash_inputs: DFlashProposer#_prepare_dflash_inputs().
  DFlashProposer.propose: DFlashProposer#propose().
  DFlashProposer._build_attn_metadata_for_draft: DFlashProposer#_build_attn_metadata_for_draft().
  DFlashProposer._dummy_kv_update_inputs: DFlashProposer#_dummy_kv_update_inputs().
  DFlashProposer._dummy_draft_forward: DFlashProposer#_dummy_draft_forward().
  DFlashProposer._update_draft_kv_cache_from_target: DFlashProposer#_update_draft_kv_cache_from_target().
  DFlashProposer._dummy_precompute_and_update_kv_cache: DFlashProposer#_dummy_precompute_and_update_kv_cache().
  DFlashProposer._load_draft_model: DFlashProposer#_load_draft_model().
  DFlashProposer._build_draft_attn_metadata: DFlashProposer#_build_draft_attn_metadata().
  DFlashProposer.runner: DFlashProposer#runner.
  DFlashProposer._update_context_kv: DFlashProposer#_update_context_kv().
  DFlashProposer._dp_lockstep_sharded: DFlashProposer#_dp_lockstep_sharded().
  DFlashProposer.block_size: DFlashProposer#block_size().
  DFlashProposer: DFlashProposer#
  DFlashProposer._dp_draft_bucket: DFlashProposer#_dp_draft_bucket().
  DFlashProposer._dp_dummy_kv_update: DFlashProposer#_dp_dummy_kv_update().
  DFlashProposer._zero_draft_lengths: DFlashProposer#_zero_draft_lengths().
  DFlashProposer.vllm_config: DFlashProposer#vllm_config.
  DFlashProposer._target_layer_ids: DFlashProposer#_target_layer_ids.
  DFlashProposer._draft_token_paddings: DFlashProposer#_draft_token_paddings().
  DFlashProposer._get_static_attn_tensors: DFlashProposer#_get_static_attn_tensors().
  DFlashProposer.run_dp_dummy_draft: DFlashProposer#run_dp_dummy_draft().
  DFlashProposer.speculative_config: DFlashProposer#speculative_config.
  DFlashProposer._max_chunk_reqs: DFlashProposer#_max_chunk_reqs().
  DFlashProposer.run_dp_dummy_context: DFlashProposer#run_dp_dummy_context().
  DFlashProposer._chunk_num_reqs_device: DFlashProposer#_chunk_num_reqs_device().
  DFlashProposer.prepare_prefill_handoff: DFlashProposer#prepare_prefill_handoff().
  DFlashProposer._tpu_build_dflash_inputs_next_tokens: DFlashProposer#_tpu_build_dflash_inputs_next_tokens().
  DFlashProposer._tpu_build_dflash_inputs_seed: DFlashProposer#_tpu_build_dflash_inputs_seed().
  DFlashProposer._draft_tp_matches_target: DFlashProposer#_draft_tp_matches_target.
  DFlashProposer._require_aux_hidden_states: DFlashProposer#_require_aux_hidden_states().
  DFlashProposer._dp_dummy_forward: DFlashProposer#_dp_dummy_forward().
  DFlashProposer._tpu_precompute_and_update_kv_cache: DFlashProposer#_tpu_precompute_and_update_kv_cache().
  DFlashProposer._dflash_forward_and_sample: DFlashProposer#_dflash_forward_and_sample().
  DFlashProposer.draft_chunks: DFlashProposer#draft_chunks.
  logger: logger.
  DFlashProposer._observe_draft_aux: DFlashProposer#_observe_draft_aux().
  DFlashProposer._build_draft_layer_metadata: DFlashProposer#_build_draft_layer_metadata().
  DFlashProposer._get_padded_len: DFlashProposer#_get_padded_len().
  DFlashProposer.dflash_config: DFlashProposer#dflash_config.
  DFlashProposer.mask_token_id: DFlashProposer#mask_token_id.
  DFlashProposer._dummy_kv_input_cache: DFlashProposer#_dummy_kv_input_cache.
  DFlashProposer._layout_draft_block: DFlashProposer#_layout_draft_block().
  DFlashProposer._draft_replicated: DFlashProposer#_draft_replicated.
  DFlashProposer.__init__: DFlashProposer#__init__().
  DFlashProposer._query_block_size: DFlashProposer#_query_block_size().
  DFlashProposer._draft_has_moe_cache: DFlashProposer#_draft_has_moe_cache.
  DFlashProposer._draft_attn_layer_names: DFlashProposer#_draft_attn_layer_names.
  DFlashProposer._static_attn_tensors_cache: DFlashProposer#_static_attn_tensors_cache.
  DFlashProposer._max_model_len: DFlashProposer#_max_model_len.
  DFlashProposer._zero_draft_lengths_cache: DFlashProposer#_zero_draft_lengths_cache.
  DFlashProposer._force_share_target_embeddings: DFlashProposer#_force_share_target_embeddings.
  DFlashProposer._request_window_bounds: DFlashProposer#_request_window_bounds().
  _draft_has_moe_layers: _draft_has_moe_layers().
  DFlashProposer.bucketed_drafts: DFlashProposer#bucketed_drafts.
---
# Module: [`src/vllm_torchtpu/spec_decode/dflash.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py)

## Classes
### <a id="DFlashProposer"></a>`DFlashProposer`
- def: [`src/vllm_torchtpu/spec_decode/dflash.py:71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L71) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
- doc: DFlash draft proposer for TPU.
- signature: `class DFlashProposer:`
- members:
  - <a id="DFlashProposer._build_attn_metadata_for_draft"></a>`_build_attn_metadata_for_draft(self, *, num_reqs: int, start_index: int, use_max_model_len: bool, seq_lens: torch.Tensor, query_start_loc: torch.Tensor, request_distribution: torch.Tensor, position_ids_override: torch.Tensor | None, padded_num_reqs: int)` — [`L331`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L331) — Build the draft layers' attention metadata. The real path and — documented in [attention-and-layer-core](../../../../concepts/attention-and-layer-core.md)
  - <a id="DFlashProposer._build_draft_attn_metadata"></a>`_build_draft_attn_metadata(self, chunk: DraftChunkInputs, num_tokens_padded: int, seq_lens: torch.Tensor)` — [`L370`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L370) — Construct attention metadata for DFlash draft forward. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer._build_draft_layer_metadata"></a>`_build_draft_layer_metadata(self, attn_metadata: dict[str, AttentionMetadata])` — [`L495`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L495) — Per-layer metadata for the draft's KV write, in layer order.
  - <a id="DFlashProposer._chunk_num_reqs_device"></a>`_chunk_num_reqs_device(chunk: DraftChunkInputs)` — [`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L177) — The chunk's live request count as a device scalar (int32, 0-d).
  - <a id="DFlashProposer._dflash_forward_and_sample"></a>`_dflash_forward_and_sample(self, input_ids: torch.Tensor, positions: torch.Tensor, block_size: int)` — [`L1079`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L1079) — Compiled XLA graph for DFlash backbone forward pass and greedy sampling.
  - <a id="DFlashProposer._dp_draft_bucket"></a>`_dp_draft_bucket(self, local_num_reqs: int = 0)` — [`L899`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L899) — Draft-forward token bucket every lockstep rank runs this step.
  - <a id="DFlashProposer._dp_dummy_forward"></a>`_dp_dummy_forward(self)` — [`L919`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L919) — One padding draft forward at the step's coordinated draft bucket.
  - <a id="DFlashProposer._dp_dummy_kv_update"></a>`_dp_dummy_kv_update(self)` — [`L905`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L905) — One padding KV-update pass at the DP-coordinated target bucket.
  - <a id="DFlashProposer._dp_lockstep_sharded"></a>`_dp_lockstep_sharded(self)` — [`L925`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L925) — True when the draft emits cross-DP collectives under EP-DP
  - <a id="DFlashProposer._draft_token_paddings"></a>`_draft_token_paddings(self)` — [`L302`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L302) — Draft-forward buckets: the runner's token buckets, doubled past
  - <a id="DFlashProposer._dummy_draft_forward"></a>`_dummy_draft_forward(self, num_tokens: int, use_max_model_len: bool, sync: bool)` — [`L828`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L828) — One draft forward on constant dummies; `sync` as in
  - <a id="DFlashProposer._dummy_kv_update_inputs"></a>`_dummy_kv_update_inputs(self, num_tokens: int, num_reqs: int, num_blocks: int)` — [`L748`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L748) — Cached `(aux hidden list, metadata)` for one KV-update shape; — documented in [attention-and-layer-core](../../../../concepts/attention-and-layer-core.md)
  - <a id="DFlashProposer._dummy_precompute_and_update_kv_cache"></a>`_dummy_precompute_and_update_kv_cache(self, num_tokens: int, num_reqs: int, num_blocks: int, sync: bool)` — [`L802`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L802) — One KV-update pass on constant dummies; `sync` waits on the host
  - <a id="DFlashProposer._get_static_attn_tensors"></a>`_get_static_attn_tensors(self, padded_num_reqs: int)` — [`L150`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L150) — Fetch or create persistent static TPU tensors for draft
  - <a id="DFlashProposer._layout_draft_block"></a>`_layout_draft_block(self, base_tokens: torch.Tensor, base_pos: torch.Tensor, block_size: int, padded_len: int, mask_token_id: int)` — [`L1143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L1143) — Lay out `[base, MASK x K]` per request from `base_tokens`
  - <a id="DFlashProposer._max_chunk_reqs"></a>`_max_chunk_reqs(self)` — [`L292`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L292) — Most requests one draft chunk holds.
  - <a id="DFlashProposer._observe_draft_aux"></a>`_observe_draft_aux(self, aux: torch.Tensor, chunk_index: int, chunk: DraftChunkInputs)` — [`L192`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L192) — Receives the second output of a chunk's
  - <a id="DFlashProposer._prepare_dflash_inputs"></a>`_prepare_dflash_inputs(self, chunk: DraftChunkInputs, next_tokens_device: torch.Tensor | None = None, device_seed: torch.Tensor | None = None)` — [`L401`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L401) — Prepares input_ids and positions tensors for DFlash draft execution. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer._query_block_size"></a>`_query_block_size(self, K: int)` — [`L187`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L187) — Query tokens per request: 1 anchor + K mask slots. DSpark's dense
  - <a id="DFlashProposer._request_window_bounds"></a>`_request_window_bounds(self, query_start_loc: torch.Tensor, position_ids: torch.Tensor, num_reqs: torch.Tensor, padded_num_reqs: int)` — [`L1117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L1117) — Per padded request row: the clamped request index, a
  - <a id="DFlashProposer._tpu_build_dflash_inputs_next_tokens"></a>`_tpu_build_dflash_inputs_next_tokens(self, next_tokens_device: torch.Tensor, query_start_loc: torch.Tensor, position_ids: torch.Tensor, draft_lengths: torch.Tensor, num_reqs: torch.Tensor, block_size: int, padded_len: int, mask_token_id: int, invalid_token_id: int)` — [`L1189`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L1189) — Compiled XLA graph that builds the drafter's inputs directly from the target
  - <a id="DFlashProposer._tpu_build_dflash_inputs_seed"></a>`_tpu_build_dflash_inputs_seed(self, device_seed: torch.Tensor, query_start_loc: torch.Tensor, position_ids: torch.Tensor, num_reqs: torch.Tensor, block_size: int, padded_len: int, mask_token_id: int)` — [`L1272`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L1272) — Compiled XLA graph that builds the drafter's inputs from a
  - <a id="DFlashProposer._tpu_precompute_and_update_kv_cache"></a>`_tpu_precompute_and_update_kv_cache(self, hidden_states: tuple[torch.Tensor, ...] | list[torch.Tensor] | torch.Tensor, positions: torch.Tensor, draft_md_tuple: tuple[AttentionMetadata, ...])` — [`L967`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L967) — Projects target model hidden states directly into the draft model's KV space.
  - <a id="DFlashProposer._update_context_kv"></a>`_update_context_kv(self, chunks: list[DraftChunkInputs])` — [`L564`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L564) — Update all context chunks before any draft forward (DP lockstep). — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer._update_draft_kv_cache_from_target"></a>`_update_draft_kv_cache_from_target(self, chunk: DraftChunkInputs)` — [`L536`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L536) — Projects the target model's hidden states into the draft model's KV cache. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer._zero_draft_lengths"></a>`_zero_draft_lengths(self, num_reqs: int)` — [`L477`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L477) — Cached all-zero `draft_lengths` for a chunk without spec
  - <a id="DFlashProposer.block_size"></a>`block_size(self)` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L146) — Tokens per request in a draft forward (see _query_block_size). — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.load_model"></a>`load_model(self, target_model)` — [`L198`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L198) — Load the draft model, share embeddings, and tag target layers. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.precompile"></a>`precompile(self)` — [`L697`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L697) — Warm up the DFlash draft model across all padding buckets. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.prepare_prefill_handoff"></a>`prepare_prefill_handoff(self)` — [`L578`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L578) — Build draft context without proposing tokens on a PD producer.
  - <a id="DFlashProposer.propose"></a>`propose(self, sampled_token_ids: list[list[int]] | None, discard_sampled_tokens_req_indices: list[int], num_rejected_tokens_np: np.ndarray | None, scheduler_output, return_device: bool = False, next_tokens_per_chunk: list[torch.Tensor] | None = None, device_seed: list[torch.Tensor] | None = None)` — [`L597`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L597) — Main execution step to propose draft tokens. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.run_dp_dummy_context"></a>`run_dp_dummy_context(self, num_chunks: int)` — [`L942`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L942) — Pair context-only producer updates without proposing draft tokens.
  - <a id="DFlashProposer.run_dp_dummy_draft"></a>`run_dp_dummy_draft(self, num_chunks: int)` — [`L952`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L952) — Replay a busy rank's draft collectives on an idle/padding rank
  - <a id="DFlashProposer.bucketed_drafts"></a>`bucketed_drafts` — [`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L169)
  - <a id="DFlashProposer.dflash_config"></a>`dflash_config` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L90)
  - <a id="DFlashProposer.draft_chunks"></a>`draft_chunks` — [`L132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L132) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.draft_model"></a>`draft_model` — [`L129`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L129) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DFlashProposer.mask_token_id"></a>`mask_token_id` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L91)
  - <a id="DFlashProposer.runner"></a>`runner` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L82)
  - <a id="DFlashProposer.speculative_config"></a>`speculative_config` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L86)
  - <a id="DFlashProposer.vllm_config"></a>`vllm_config` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L83)
- protocol/private: <a id="DFlashProposer.__init__"></a>`__init__`[`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L77), <a id="DFlashProposer._draft_attn_layer_names"></a>`_draft_attn_layer_names`[`L131`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L131), <a id="DFlashProposer._draft_has_moe_cache"></a>`_draft_has_moe_cache`[`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L130), <a id="DFlashProposer._draft_replicated"></a>`_draft_replicated`[`L119`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L119), <a id="DFlashProposer._draft_tp_matches_target"></a>`_draft_tp_matches_target`[`L121`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L121), <a id="DFlashProposer._dummy_kv_input_cache"></a>`_dummy_kv_input_cache`[`L138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L138), <a id="DFlashProposer._force_share_target_embeddings"></a>`_force_share_target_embeddings`[`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L174), <a id="DFlashProposer._get_padded_len"></a>`_get_padded_len`[`L319`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L319), <a id="DFlashProposer._load_draft_model"></a>`_load_draft_model`[`L272`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L272), <a id="DFlashProposer._max_model_len"></a>`_max_model_len`[`L128`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L128), <a id="DFlashProposer._require_aux_hidden_states"></a>`_require_aux_hidden_states`[`L528`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L528), <a id="DFlashProposer._static_attn_tensors_cache"></a>`_static_attn_tensors_cache`[`L133`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L133), <a id="DFlashProposer._target_layer_ids"></a>`_target_layer_ids`[`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L92), <a id="DFlashProposer._zero_draft_lengths_cache"></a>`_zero_draft_lengths_cache`[`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L143)
- uses (calls/refs, reference-scoped): [`device`](../runner/tpu_runner.md#TPUModelRunner.device), [`synchronize_tensors`](../utils.md#synchronize_tensors), [`_attn_metadata_builder_ctx`](../runner/tpu_runner.md#TPUModelRunner._attn_metadata_builder_ctx), [`num_reqs_most_model_len`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_most_model_len), [`initialize_kernel`](../layers/adapter/attention.md#PallasAttentionBackendImpl.initialize_kernel), [`num_tokens_paddings`](../runner/tpu_runner.md#TPUModelRunner.num_tokens_paddings), [`set_vllm_model_wrapper_context`](../models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`AttentionMetadata`](../layers/core/attention_metadata.md#AttentionMetadata), [`max_num_reqs`](../runner/tpu_runner.md#TPUModelRunner.max_num_reqs), [`num_reqs_max_model_len`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_max_model_len), [`_precompile_timed`](../runner/tpu_runner.md#TPUModelRunner._precompile_timed), [`DraftChunkInputs`](utils.md#DraftChunkInputs), [`most_model_len`](../runner/tpu_runner.md#TPUModelRunner.most_model_len), [`TPUModelRunner`](../runner/tpu_runner.md#TPUModelRunner), [`PallasAttentionBackendImpl`](../layers/adapter/attention.md#PallasAttentionBackendImpl), [`_observe_draft_aux`](dspark.md#DSparkProposer._observe_draft_aux), [`max_num_blocks_per_req`](../runner/tpu_runner.md#TPUModelRunner.max_num_blocks_per_req), [`build_attention_metadata_for_layers`](../runner/tpu_runner.md#TPUModelRunner.build_attention_metadata_for_layers), [`mesh`](../runner/tpu_runner.md#TPUModelRunner.mesh), [`request_distribution`](../layers/core/attention_metadata.md#AttentionMetadata.request_distribution), [`query_start_loc`](../layers/core/attention_metadata.md#AttentionMetadata.query_start_loc), [`seq_lens`](../layers/core/attention_metadata.md#AttentionMetadata.seq_lens), [`attn_ctx`](utils.md#DraftChunkInputs.attn_ctx), [`block_tables`](../layers/core/attention_metadata.md#AttentionMetadata.block_tables), [`num_reqs`](utils.md#DraftChunkInputs.num_reqs), [`maybe_share_lm_head`](utils.md#maybe_share_lm_head), [`AttentionMetadataBuilderContext`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext), [`num_blocks_per_most_len_req`](../runner/tpu_runner.md#TPUModelRunner.num_blocks_per_most_len_req), [`INVALID_TOKEN_ID`](../runner/tpu_runner_async_output.md#INVALID_TOKEN_ID), [`_dp_num_tokens_across_dp`](../runner/tpu_runner.md#TPUModelRunner._dp_num_tokens_across_dp), [`seq_lens`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.seq_lens), [`use_max_model_len`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.use_max_model_len), [`_dp_lockstep_enabled`](../runner/tpu_runner.md#TPUModelRunner._dp_lockstep_enabled), [`maybe_share_embeddings`](utils.md#maybe_share_embeddings), [`normalize_draft_config`](utils.md#normalize_draft_config), [`position_ids_override`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.position_ids_override), [`_get_padded_num_reqs_with_upper_limit`](../runner/tpu_runner.md#_get_padded_num_reqs_with_upper_limit), [`input_positions`](../layers/core/attention_metadata.md#AttentionMetadata.input_positions), [`query_start_loc`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.query_start_loc), [`_dflash_forward_and_sample`](dspark.md#DSparkProposer._dflash_forward_and_sample)  (+22 more)
- used by: [`device`](../runner/tpu_runner.md#TPUModelRunner.device), [`sample_tokens`](../runner/tpu_runner.md#TPUModelRunner.sample_tokens), [`encoder_cudagraph_manager`](../runner/tpu_runner.md#TPUModelRunner.encoder_cudagraph_manager), [`_warmup_spec_decode_cleanup`](../runner/tpu_runner.md#TPUModelRunner._warmup_spec_decode_cleanup), [`_run_dp_idle_pairing`](../runner/tpu_runner.md#TPUModelRunner._run_dp_idle_pairing), [`drafter`](../runner/tpu_runner.md#TPUModelRunner.drafter), [`propose_draft_token_ids`](../runner/speculative_decoding_manager.md#SpeculativeDecodingManager.propose_draft_token_ids), [`_num_static_verify_reqs`](../runner/tpu_runner.md#TPUModelRunner._num_static_verify_reqs), [`_async_drafter`](../runner/tpu_runner.md#TPUModelRunner._async_drafter), [`_draft_confidences`](dspark.md#DSparkProposer._draft_confidences), [`sample_from_anchor`](dspark.md#DSparkProposer.sample_from_anchor), [`_dflash_forward_and_sample`](dspark.md#DSparkProposer._dflash_forward_and_sample), [`load_model`](dspark.md#DSparkProposer.load_model), [`DSparkProposer`](dspark.md#DSparkProposer), [`__init__`](dspark.md#DSparkProposer.__init__)

## Functions
- <a id="_draft_has_moe_layers"></a>`_draft_has_moe_layers(draft_model: torch.nn.Module)` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L57) — Whether a draft carries MoE layers, i.e. emits EP collectives.

## Module values
- <a id="logger"></a>`logger` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dflash.py#L54)

