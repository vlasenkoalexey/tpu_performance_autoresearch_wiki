---
title: 'Module: src/vllm_torchtpu/spec_decode/utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.utils`/
symbols:
  DraftChunkInputs: DraftChunkInputs#
  DraftChunkInputs.attn_ctx: DraftChunkInputs#attn_ctx.
  logger: logger.
  DraftChunkInputs.num_reqs: DraftChunkInputs#num_reqs.
  maybe_share_lm_head: maybe_share_lm_head().
  populate_draft_lm_head_from_target: populate_draft_lm_head_from_target().
  maybe_share_embeddings: maybe_share_embeddings().
  normalize_draft_config: normalize_draft_config().
  populate_draft_embed_from_target: populate_draft_embed_from_target().
  DraftChunkInputs.sequence_layout_plan: DraftChunkInputs#sequence_layout_plan.
  fit_rows: fit_rows().
  DraftChunkInputs.start_index: DraftChunkInputs#start_index.
  _DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN: _DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN.
  DraftChunkInputs.aux_hidden_states: DraftChunkInputs#aux_hidden_states.
  DraftChunkInputs.position_ids: DraftChunkInputs#position_ids.
  iter_mtp_shared_heads: iter_mtp_shared_heads().
  dp_lockstep_num_reqs: dp_lockstep_num_reqs().
  DraftChunkInputs.input_ids: DraftChunkInputs#input_ids.
  DraftChunkInputs.query_start_loc_np: DraftChunkInputs#query_start_loc_np.
  DraftChunkInputs.draft_lengths: DraftChunkInputs#draft_lengths.
  DraftChunkInputs.hidden_states: DraftChunkInputs#hidden_states.
  _force_draft_tp1: _force_draft_tp1().
  gather_sharded_weight: gather_sharded_weight().
  DraftChunkInputs.attn_metadata: DraftChunkInputs#attn_metadata.
  handoff_seed_tokens: handoff_seed_tokens().
  _NOISE_TOKEN_KEYS: _NOISE_TOKEN_KEYS.
  resolve_draft_logits_processor: resolve_draft_logits_processor().
  _resolve_target_layer_ids: _resolve_target_layer_ids().
---
# Module: [`src/vllm_torchtpu/spec_decode/utils.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py)

## Classes
### <a id="DraftChunkInputs"></a>`DraftChunkInputs`
- def: [`src/vllm_torchtpu/spec_decode/utils.py:80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L80) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
- signature: `class DraftChunkInputs:`
- members:
  - <a id="DraftChunkInputs.attn_ctx"></a>`attn_ctx` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L91) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DraftChunkInputs.attn_metadata"></a>`attn_metadata` — [`L112`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L112)
  - <a id="DraftChunkInputs.aux_hidden_states"></a>`aux_hidden_states` — [`L99`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L99)
  - <a id="DraftChunkInputs.draft_lengths"></a>`draft_lengths` — [`L107`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L107)
  - <a id="DraftChunkInputs.hidden_states"></a>`hidden_states` — [`L110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L110)
  - <a id="DraftChunkInputs.input_ids"></a>`input_ids` — [`L83`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L83)
  - <a id="DraftChunkInputs.num_reqs"></a>`num_reqs` — [`L95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L95) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="DraftChunkInputs.position_ids"></a>`position_ids` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L85)
  - <a id="DraftChunkInputs.query_start_loc_np"></a>`query_start_loc_np` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L87)
  - <a id="DraftChunkInputs.sequence_layout_plan"></a>`sequence_layout_plan` — [`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L102)
  - <a id="DraftChunkInputs.start_index"></a>`start_index` — [`L93`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L93)
- uses (calls/refs, reference-scoped): [`SequenceLayoutPlan`](../layers/core/sequence_layout.md#SequenceLayoutPlan), [`AttentionMetadataBuilderContext`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext), [`_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN`](utils.md#_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN)
- used by: [`execute_model`](../runner/tpu_runner.md#TPUModelRunner.execute_model), [`_build_dp_dummy_draft`](eagle3.md#Eagle3Proposer._build_dp_dummy_draft), [`propose`](eagle3.md#Eagle3Proposer.propose), [`_build_draft_attn_metadata`](eagle3.md#Eagle3Proposer._build_draft_attn_metadata), [`_prepare_draft_inputs`](eagle3.md#Eagle3Proposer._prepare_draft_inputs), [`_prepare_dflash_inputs`](dflash.md#DFlashProposer._prepare_dflash_inputs), [`propose`](dflash.md#DFlashProposer.propose), [`_forward_draft`](eagle3.md#Eagle3Proposer._forward_draft), [`_update_draft_kv_cache_from_target`](dflash.md#DFlashProposer._update_draft_kv_cache_from_target), [`_run_mtp_fused_loop`](eagle3.md#Eagle3Proposer._run_mtp_fused_loop), [`_loop_step_attn_inputs`](eagle3.md#Eagle3Proposer._loop_step_attn_inputs), [`_build_draft_attn_metadata`](dflash.md#DFlashProposer._build_draft_attn_metadata), [`_observe_draft_aux`](dspark.md#DSparkProposer._observe_draft_aux), [`_update_context_kv`](dflash.md#DFlashProposer._update_context_kv), [`_target_draft_attn_metadata`](eagle3.md#Eagle3Proposer._target_draft_attn_metadata), [`_chunk_num_reqs_device`](dflash.md#DFlashProposer._chunk_num_reqs_device), [`prepare_prefill_handoff`](dflash.md#DFlashProposer.prepare_prefill_handoff), [`_require_aux_hidden_states`](dflash.md#DFlashProposer._require_aux_hidden_states), [`draft_chunks`](dflash.md#DFlashProposer.draft_chunks), [`_observe_draft_aux`](dflash.md#DFlashProposer._observe_draft_aux), [`chunk`](eagle3.md#_DpDummyDraft.chunk), [`draft_chunks`](../runner/tpu_runner.md#ExecuteModelState.draft_chunks), [`draft_chunks`](eagle3.md#Eagle3Proposer.draft_chunks)

## Functions
- <a id="_force_draft_tp1"></a>`_force_draft_tp1()` — [`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L116) — Collapse the TP group to world_size=1 / rank=0 for the duration of draft
- <a id="_resolve_target_layer_ids"></a>`_resolve_target_layer_ids(hf_dict: dict)` — [`L471`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L471) — Target layer indices whose hidden states feed the drafter.
- <a id="dp_lockstep_num_reqs"></a>`dp_lockstep_num_reqs(dp_step_max_reqs: int, local_num_reqs: int)` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L68) — Per-chunk request count all EP-DP lockstep ranks size the draft to: the
- <a id="fit_rows"></a>`fit_rows(t: torch.Tensor, rows: int, value: int = 0)` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L53) — `t` with its leading dim sliced or padded (with `value`) to `rows`. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
- <a id="gather_sharded_weight"></a>`gather_sharded_weight(sharded_module: VocabParallelEmbedding)` — [`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L175) — Gathers a sharded weight tensor across TP into a full replicated tensor.
- <a id="handoff_seed_tokens"></a>`handoff_seed_tokens(device_seed: torch.Tensor, req_ids: list[str], metadata: Any)` — [`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L143) — Seeds a prefill-only draft's boundary row with the consumer's token.
- <a id="iter_mtp_shared_heads"></a>`iter_mtp_shared_heads(draft_model: torch.nn.Module)` — [`L298`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L298) — Yield the per-layer ``shared_head`` modules of a DeepSeek-style MTP draft.
- <a id="maybe_share_embeddings"></a>`maybe_share_embeddings(draft_model: torch.nn.Module, target_model: torch.nn.Module, tp_layout_matches: bool, force_share: bool = False)` — [`L232`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L232)
- <a id="maybe_share_lm_head"></a>`maybe_share_lm_head(draft_model: torch.nn.Module, target_model: torch.nn.Module, draft_replicated: bool, tp_layout_matches: bool, force_share: bool = False, materialize_if_mismatched: bool = True)` — [`L375`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L375) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
- <a id="normalize_draft_config"></a>`normalize_draft_config(hf_config)` — [`L488`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L488) — Resolve parallel draft config spellings into ``dflash_config``. Idempotent.
- <a id="populate_draft_embed_from_target"></a>`populate_draft_embed_from_target(draft_model: torch.nn.Module, target_embed: VocabParallelEmbedding)` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L203) — Fill the draft's own (tp=1, full-vocab) embed_tokens with the
- <a id="populate_draft_lm_head_from_target"></a>`populate_draft_lm_head_from_target(draft_model: torch.nn.Module, target_lm_head: VocabParallelEmbedding)` — [`L332`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L332)
- <a id="resolve_draft_logits_processor"></a>`resolve_draft_logits_processor(draft_model: torch.nn.Module)` — [`L318`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L318) — The draft's `LogitsProcessor`, wherever the draft class keeps it.

## Module values
- <a id="_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN"></a>`_DEFAULT_DRAFT_SEQUENCE_LAYOUT_PLAN` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L46)
- <a id="_NOISE_TOKEN_KEYS"></a>`_NOISE_TOKEN_KEYS` — [`L463`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L463)
- <a id="logger"></a>`logger` — [`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/utils.py#L37)

