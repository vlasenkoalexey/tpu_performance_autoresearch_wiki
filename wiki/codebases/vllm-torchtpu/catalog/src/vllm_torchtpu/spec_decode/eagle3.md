---
title: 'Module: src/vllm_torchtpu/spec_decode/eagle3.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/eagle3.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.eagle3`/
symbols:
  Eagle3Proposer._build_dp_dummy_draft: Eagle3Proposer#_build_dp_dummy_draft().
  Eagle3Proposer.propose: Eagle3Proposer#propose().
  Eagle3Proposer._build_draft_attn_metadata: Eagle3Proposer#_build_draft_attn_metadata().
  Eagle3Proposer._dp_dummy_draft_step: Eagle3Proposer#_dp_dummy_draft_step().
  Eagle3Proposer.load_model: Eagle3Proposer#load_model().
  Eagle3Proposer.draft_model: Eagle3Proposer#draft_model.
  Eagle3Proposer._prepare_draft_inputs: Eagle3Proposer#_prepare_draft_inputs().
  Eagle3Proposer._forward_draft: Eagle3Proposer#_forward_draft().
  Eagle3Proposer._build_mtp_fused_loop: Eagle3Proposer#_build_mtp_fused_loop().
  Eagle3Proposer._build_mtp_loop_model: Eagle3Proposer#_build_mtp_loop_model().
  Eagle3Proposer._load_draft_model: Eagle3Proposer#_load_draft_model().
  Eagle3Proposer._precompile_compute_logits: Eagle3Proposer#_precompile_compute_logits().
  Eagle3Proposer._init_mtp_index_sharing: Eagle3Proposer#_init_mtp_index_sharing().
  Eagle3Proposer._precompile_combine_hidden_states: Eagle3Proposer#_precompile_combine_hidden_states().
  Eagle3Proposer.speculative_config: Eagle3Proposer#speculative_config.
  Eagle3Proposer._run_mtp_fused_loop: Eagle3Proposer#_run_mtp_fused_loop().
  Eagle3Proposer.runner: Eagle3Proposer#runner.
  Eagle3Proposer._loop_step_attn_inputs: Eagle3Proposer#_loop_step_attn_inputs().
  Eagle3Proposer._precompile_draft_seed: Eagle3Proposer#_precompile_draft_seed().
  Eagle3Proposer._validate_dsa_draft: Eagle3Proposer#_validate_dsa_draft().
  Eagle3Proposer.draft_vllm_config: Eagle3Proposer#draft_vllm_config.
  Eagle3Proposer._loop_bucket: Eagle3Proposer#_loop_bucket().
  Eagle3Proposer._load_mtp_draft_sharing_head: Eagle3Proposer#_load_mtp_draft_sharing_head().
  Eagle3Proposer._target_draft_attn_metadata: Eagle3Proposer#_target_draft_attn_metadata().
  Eagle3Proposer.run_dp_dummy_draft: Eagle3Proposer#run_dp_dummy_draft().
  logger: logger.
  Eagle3Proposer._validate_kv_sharing_supported: Eagle3Proposer#_validate_kv_sharing_supported().
  Eagle3Proposer._dp_lockstep_sharded: Eagle3Proposer#_dp_lockstep_sharded().
  Eagle3Proposer.precompile: Eagle3Proposer#precompile().
  Eagle3Proposer._setup_gemma4_kv_sharing: Eagle3Proposer#_setup_gemma4_kv_sharing().
  Eagle3Proposer._draft_has_moe_cache: Eagle3Proposer#_draft_has_moe_cache.
  Eagle3Proposer._draft_combine_input_size: Eagle3Proposer#_draft_combine_input_size().
  Eagle3Proposer: Eagle3Proposer#
  Eagle3Proposer.vllm_config: Eagle3Proposer#vllm_config.
  Eagle3Proposer.run_draft_step: Eagle3Proposer#run_draft_step().
  Eagle3Proposer._share_mtp_indices: Eagle3Proposer#_share_mtp_indices.
  Eagle3Proposer._mtp_topk_buffers: Eagle3Proposer#_mtp_topk_buffers.
  Eagle3Proposer._draft_propose_token: Eagle3Proposer#_draft_propose_token().
  Eagle3Proposer._draft_hidden_size: Eagle3Proposer#_draft_hidden_size().
  Eagle3Proposer._draft_uses_aux_hidden_state: Eagle3Proposer#_draft_uses_aux_hidden_state().
  Eagle3Proposer._validate_mtp_layer_count: Eagle3Proposer#_validate_mtp_layer_count().
  Eagle3Proposer._draft_model_for_step: Eagle3Proposer#_draft_model_for_step().
  Eagle3Proposer._draft_moe_ctx: Eagle3Proposer#_draft_moe_ctx().
  Eagle3Proposer._draft_combine_hidden_states: Eagle3Proposer#_draft_combine_hidden_states().
  Eagle3Proposer._draft_attn_layer_names: Eagle3Proposer#_draft_attn_layer_names.
  Eagle3Proposer._draft_md_cache: Eagle3Proposer#_draft_md_cache.
  _static_shape_args: _static_shape_args().
  Eagle3Proposer.advance_draft_positions: Eagle3Proposer#advance_draft_positions().
  Eagle3Proposer._draft_replicated: Eagle3Proposer#_draft_replicated.
  Eagle3Proposer._mtp_fused_loop: Eagle3Proposer#_mtp_fused_loop.
  Eagle3Proposer._mtp_set_skip_topk: Eagle3Proposer#_mtp_set_skip_topk().
  Eagle3Proposer._mtp_compact_and_save: Eagle3Proposer#_mtp_compact_and_save().
  Eagle3Proposer._validate_prefill_only_draft_model: Eagle3Proposer#_validate_prefill_only_draft_model().
  Eagle3Proposer._draft_has_moe: Eagle3Proposer#_draft_has_moe().
  _DpDummyDraft.chunk: _DpDummyDraft#chunk.
  Eagle3Proposer._draft_seed_input_ids: Eagle3Proposer#_draft_seed_input_ids().
  Eagle3Proposer._draft_kv_shared: Eagle3Proposer#_draft_kv_shared.
  _draft_head_modules: _draft_head_modules().
  Eagle3Proposer.pad_dp_draft_step: Eagle3Proposer#pad_dp_draft_step().
  _maybe_pad_dim0: _maybe_pad_dim0().
  Eagle3Proposer._draft_tp_matches_target: Eagle3Proposer#_draft_tp_matches_target.
  Eagle3Proposer._mtp_loop_model: Eagle3Proposer#_mtp_loop_model.
  _static_shape_args.wrapper: _static_shape_args().wrapper().
  Eagle3Proposer.draft_chunks: Eagle3Proposer#draft_chunks.
  Eagle3Proposer._mtp_restore_topk: Eagle3Proposer#_mtp_restore_topk().
  Eagle3Proposer._draft_gather_carries: Eagle3Proposer#_draft_gather_carries().
  _DpDummyDraft: _DpDummyDraft#
  _DpDummyDraft.combine_aux: _DpDummyDraft#combine_aux.
  _DpDummyDraft.combine_plain: _DpDummyDraft#combine_plain.
  Eagle3Proposer._mtp_loop_model_warm: Eagle3Proposer#_mtp_loop_model_warm.
  Eagle3Proposer._mtp_fused_loop_warm: Eagle3Proposer#_mtp_fused_loop_warm.
  Eagle3Proposer.__init__: Eagle3Proposer#__init__().
  _static_shape_args.wrapper.unmark: _static_shape_args().wrapper().unmark().
  _DpDummyDraft.bucket: _DpDummyDraft#bucket.
  _DpDummyDraft.loop_bucket: _DpDummyDraft#loop_bucket.
  _DpDummyDraft.input_ids: _DpDummyDraft#input_ids.
  _DpDummyDraft.positions: _DpDummyDraft#positions.
  _DpDummyDraft.target_hidden_states: _DpDummyDraft#target_hidden_states.
  _DpDummyDraft.first_pass_carry: _DpDummyDraft#first_pass_carry.
  _DpDummyDraft.loop_input_ids: _DpDummyDraft#loop_input_ids.
  _DpDummyDraft.loop_positions: _DpDummyDraft#loop_positions.
  _DpDummyDraft.loop_hidden: _DpDummyDraft#loop_hidden.
  _DpDummyDraft.loop_query_start_loc: _DpDummyDraft#loop_query_start_loc.
  _DpDummyDraft.loop_request_distribution: _DpDummyDraft#loop_request_distribution.
  INVALID_TOKEN_ID: INVALID_TOKEN_ID.
  _maybe_pad_dim1: _maybe_pad_dim1().
  _collect_topk_indices_buffers: _collect_topk_indices_buffers().
  Eagle3Proposer.load_weights: Eagle3Proposer#load_weights().
  Eagle3Proposer._split_dsa_draft_layers: Eagle3Proposer#_split_dsa_draft_layers().
  Eagle3Proposer._unwrap_model_out: Eagle3Proposer#_unwrap_model_out().
---
# Module: [`src/vllm_torchtpu/spec_decode/eagle3.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py)

## Classes
### <a id="Eagle3Proposer"></a>`Eagle3Proposer`
- def: [`src/vllm_torchtpu/spec_decode/eagle3.py:193`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L193) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
- doc: Eagle3/MTP draft proposer for TPU.
- signature: `class Eagle3Proposer:`
- members:
  - <a id="Eagle3Proposer._build_dp_dummy_draft"></a>`_build_dp_dummy_draft(self)` — [`L2352`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2352) — Inputs for EP-DP padding chunks at the step's coordinated shapes, — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._build_draft_attn_metadata"></a>`_build_draft_attn_metadata(self, chunk: DraftChunkInputs, step_idx: int, seq_lens_delta: int, num_rejected_np: np.ndarray | None, num_tokens_padded: int | None = None, num_rejected_dev: torch.Tensor | None = None, loop_query_start_loc: torch.Tensor | None = None, loop_request_distribution: torch.Tensor | None = None)` — [`L1853`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1853) — Build draft attention metadata for one chunk. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._build_mtp_fused_loop"></a>`_build_mtp_fused_loop(self)` — [`L561`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L561) — Compile an MTP draft's loop steps 1..K-1 as one program, so the — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._build_mtp_loop_model"></a>`_build_mtp_loop_model(self)` — [`L499`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L499) — Give IndexShare's draft steps 1+ a compiled program of their own. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._dp_dummy_draft_step"></a>`_dp_dummy_draft_step(self, dummy: _DpDummyDraft, step: int)` — [`L2465`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2465) — Draft step `step` of one EP-DP padding chunk: the programs and — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._dp_lockstep_sharded"></a>`_dp_lockstep_sharded(self)` — [`L2216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2216) — True when the draft emits cross-DP collectives under EP-DP lockstep. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._draft_combine_input_size"></a>`_draft_combine_input_size(self)` — [`L2185`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2185) — Width of the per-token tensor that combine_hidden_states consumes.
  - <a id="Eagle3Proposer._draft_has_moe"></a>`_draft_has_moe(self)` — [`L2197`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2197) — Whether the draft model carries MoE layers.
  - <a id="Eagle3Proposer._draft_hidden_size"></a>`_draft_hidden_size(self)` — [`L2154`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2154) — Width of the hidden state the draft's lm_head consumes.
  - <a id="Eagle3Proposer._draft_model_for_step"></a>`_draft_model_for_step(self, step_idx: int)` — [`L677`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L677) — The compiled program draft step `step_idx` runs.
  - <a id="Eagle3Proposer._draft_moe_ctx"></a>`_draft_moe_ctx(self)` — [`L849`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L849) — The MoE collection chunking the draft forward runs under.
  - <a id="Eagle3Proposer._draft_uses_aux_hidden_state"></a>`_draft_uses_aux_hidden_state(self)` — [`L2176`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2176) — Whether this draft checkpoint feeds combine_hidden_states the
  - <a id="Eagle3Proposer._init_mtp_index_sharing"></a>`_init_mtp_index_sharing(self)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L417) — Enable IndexShare when a DSA MTP checkpoint asks for it.
  - <a id="Eagle3Proposer._load_mtp_draft_sharing_head"></a>`_load_mtp_draft_sharing_head(self, model_loader, draft_model_config, target_model: torch.nn.Module)` — [`L902`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L902) — Loads an MTP draft that borrows the target's embed_tokens and lm_head. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._loop_bucket"></a>`_loop_bucket(self, num_reqs: int)` — [`L2230`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2230) — Loop-phase token bucket p (carries, lm-head gathers, loop forwards). — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._loop_step_attn_inputs"></a>`_loop_step_attn_inputs(self, chunk: DraftChunkInputs, seq_lens_delta: int, num_rejected_np: np.ndarray | None, num_rejected_dev: torch.Tensor | None, loop_query_start_loc: torch.Tensor | None, loop_request_distribution: torch.Tensor | None)` — [`L1788`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1788) — seq_lens, query_start_loc and request_distribution of a loop step — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._mtp_compact_and_save"></a>`_mtp_compact_and_save(self, gather_indices: torch.Tensor)` — [`L698`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L698) — Compact step 0's per-token top-k rows to one row per request, then
  - <a id="Eagle3Proposer._mtp_restore_topk"></a>`_mtp_restore_topk(self, saved: list[torch.Tensor])` — [`L714`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L714) — Put this chunk's step-0 rows back at the front before its forward.
  - <a id="Eagle3Proposer._prepare_draft_inputs"></a>`_prepare_draft_inputs(self, chunk: DraftChunkInputs, sampled_token_ids: list[list[int]] | None, discard_sampled_tokens_req_indices: list[int], num_rejected_tokens_np: np.ndarray | None, scheduler_output, next_tokens_device: torch.Tensor | None = None, device_seed: torch.Tensor | None = None)` — [`L1508`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1508) — Build draft first-pass inputs for one chunk. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._run_mtp_fused_loop"></a>`_run_mtp_fused_loop(self, chunk: DraftChunkInputs, input_ids: torch.Tensor, positions: torch.Tensor, hidden_states: torch.Tensor, num_rejected_np: np.ndarray | None, num_rejected_dev: torch.Tensor | None, loop_query_start_loc: torch.Tensor, loop_request_distribution: torch.Tensor)` — [`L616`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L616) — Draft steps 1..K-1 of one chunk in one dispatch. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer._setup_gemma4_kv_sharing"></a>`_setup_gemma4_kv_sharing(self, target_model, target_attn_layer_names: set[str])` — [`L743`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L743) — Wire Q-only draft layers to read the target model's KV cache.
  - <a id="Eagle3Proposer._split_dsa_draft_layers"></a>`_split_dsa_draft_layers(all_attn_layers: dict[str, AttentionLayerBase], draft_attn_layer_names: set[str])` — [`L991`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L991) — Split a DSA draft's attention layers into (indexer K caches, MLA).
  - <a id="Eagle3Proposer._target_draft_attn_metadata"></a>`_target_draft_attn_metadata(self, chunk: DraftChunkInputs)` — [`L1751`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1751) — The draft layers' entries of the target forward's own metadata.
  - <a id="Eagle3Proposer._unwrap_model_out"></a>`_unwrap_model_out(out)` — [`L2054`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2054) — Normalise a draft-model forward result to (last_hidden, carry_hidden).
  - <a id="Eagle3Proposer._validate_dsa_draft"></a>`_validate_dsa_draft(self, all_attn_layers: dict[str, AttentionLayerBase], draft_attn_layer_names: set[str])` — [`L1022`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1022) — Prove a sparse-attention (DSA) draft's KV caches are usable.
  - <a id="Eagle3Proposer._validate_kv_sharing_supported"></a>`_validate_kv_sharing_supported(self)` — [`L719`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L719) — Fail closed on TPU paths that cannot honour `skip_kv_update`. — documented in [tpu-platform](../../../../concepts/tpu-platform.md)
  - <a id="Eagle3Proposer._validate_mtp_layer_count"></a>`_validate_mtp_layer_count(self)` — [`L369`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L369) — One nextn layer only: the proposer's per-step wiring assumes it.
  - <a id="Eagle3Proposer._validate_prefill_only_draft_model"></a>`_validate_prefill_only_draft_model(self, draft_attn_layer_names: set[str])` — [`L977`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L977) — Validate draft KV-cache capabilities known only after model load.
  - <a id="Eagle3Proposer.advance_draft_positions"></a>`advance_draft_positions(self)` — [`L286`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L286) — Whether each propose step advances the draft's positions/seq_lens.
  - <a id="Eagle3Proposer.load_model"></a>`load_model(self, target_model)` — [`L297`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L297) — Load the draft model and share embeddings/lm_head with target. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.load_weights"></a>`load_weights(weights: Iterable[tuple[str, torch.Tensor]])` — [`L954`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L954)
  - <a id="Eagle3Proposer.pad_dp_draft_step"></a>`pad_dp_draft_step(step: int)` — [`L1353`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1353)
  - <a id="Eagle3Proposer.precompile"></a>`precompile(self)` — [`L2137`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2137) — Precompile the draft-side @torch.compile wrapper subgraphs.
  - <a id="Eagle3Proposer.propose"></a>`propose(self, sampled_token_ids: list[list[int]] | None, discard_sampled_tokens_req_indices: list[int], num_rejected_tokens_np: np.ndarray | None, scheduler_output, return_device: bool = False, next_tokens_per_chunk: list[torch.Tensor] | None = None, device_seed: torch.Tensor | None = None)` — [`L1196`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1196) — Generate K draft tokens per request via the eagle3 draft model. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.run_dp_dummy_draft"></a>`run_dp_dummy_draft(self, num_chunks: int)` — [`L2325`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2325) — Replay a busy rank's DRAFT collective trace on an idle/padding rank,
  - <a id="Eagle3Proposer.run_draft_step"></a>`run_draft_step(ci: int, step: int)` — [`L1427`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1427) — One separate draft step for chunk `ci`: a draft forward
  - <a id="Eagle3Proposer.draft_chunks"></a>`draft_chunks` — [`L262`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L262)
  - <a id="Eagle3Proposer.draft_model"></a>`draft_model` — [`L247`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L247) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.draft_vllm_config"></a>`draft_vllm_config` — [`L248`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L248) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.runner"></a>`runner` — [`L214`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L214) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.speculative_config"></a>`speculative_config` — [`L218`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L218) — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="Eagle3Proposer.vllm_config"></a>`vllm_config` — [`L215`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L215)
- protocol/private: <a id="Eagle3Proposer.__init__"></a>`__init__`[`L209`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L209), <a id="Eagle3Proposer._draft_attn_layer_names"></a>`_draft_attn_layer_names`[`L252`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L252), <a id="Eagle3Proposer._draft_combine_hidden_states"></a>`_draft_combine_hidden_states`[`L1157`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1157), <a id="Eagle3Proposer._draft_gather_carries"></a>`_draft_gather_carries`[`L1132`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1132), <a id="Eagle3Proposer._draft_has_moe_cache"></a>`_draft_has_moe_cache`[`L240`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L240), <a id="Eagle3Proposer._draft_kv_shared"></a>`_draft_kv_shared`[`L258`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L258), <a id="Eagle3Proposer._draft_md_cache"></a>`_draft_md_cache`[`L269`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L269), <a id="Eagle3Proposer._draft_propose_token"></a>`_draft_propose_token`[`L1109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1109), <a id="Eagle3Proposer._draft_replicated"></a>`_draft_replicated`[`L236`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L236), <a id="Eagle3Proposer._draft_seed_input_ids"></a>`_draft_seed_input_ids`[`L1174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L1174), <a id="Eagle3Proposer._draft_tp_matches_target"></a>`_draft_tp_matches_target`[`L238`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L238), <a id="Eagle3Proposer._forward_draft"></a>`_forward_draft`[`L2074`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2074), <a id="Eagle3Proposer._load_draft_model"></a>`_load_draft_model`[`L861`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L861), <a id="Eagle3Proposer._mtp_fused_loop"></a>`_mtp_fused_loop`[`L282`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L282), <a id="Eagle3Proposer._mtp_fused_loop_warm"></a>`_mtp_fused_loop_warm`[`L283`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L283), <a id="Eagle3Proposer._mtp_loop_model"></a>`_mtp_loop_model`[`L276`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L276), <a id="Eagle3Proposer._mtp_loop_model_warm"></a>`_mtp_loop_model_warm`[`L278`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L278), <a id="Eagle3Proposer._mtp_set_skip_topk"></a>`_mtp_set_skip_topk`[`L693`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L693), <a id="Eagle3Proposer._mtp_topk_buffers"></a>`_mtp_topk_buffers`[`L273`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L273), <a id="Eagle3Proposer._precompile_combine_hidden_states"></a>`_precompile_combine_hidden_states`[`L2239`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2239), <a id="Eagle3Proposer._precompile_compute_logits"></a>`_precompile_compute_logits`[`L2293`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2293), <a id="Eagle3Proposer._precompile_draft_seed"></a>`_precompile_draft_seed`[`L2267`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L2267), <a id="Eagle3Proposer._share_mtp_indices"></a>`_share_mtp_indices`[`L271`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L271)
- uses (calls/refs, reference-scoped): [`device`](../runner/tpu_runner.md#TPUModelRunner.device), [`synchronize_tensors`](../utils.md#synchronize_tensors), [`_attn_metadata_builder_ctx`](../runner/tpu_runner.md#TPUModelRunner._attn_metadata_builder_ctx), [`num_reqs_most_model_len`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_most_model_len), [`num_tokens_paddings`](../runner/tpu_runner.md#TPUModelRunner.num_tokens_paddings), [`set_vllm_model_wrapper_context`](../models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`AttentionMetadata`](../layers/core/attention_metadata.md#AttentionMetadata), [`max_num_reqs`](../runner/tpu_runner.md#TPUModelRunner.max_num_reqs), [`num_reqs_max_model_len`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_max_model_len), [`from_vllm_config`](../platforms/pcp_validation.md#PcpStaticSupportValidator.from_vllm_config), [`_precompile_timed`](../runner/tpu_runner.md#TPUModelRunner._precompile_timed), [`_mtp_prefill_only`](../runner/tpu_runner.md#TPUModelRunner._mtp_prefill_only), [`DraftChunkInputs`](utils.md#DraftChunkInputs), [`num_reqs_paddings`](../runner/tpu_runner.md#TPUModelRunner.num_reqs_paddings), [`TPUModelRunner`](../runner/tpu_runner.md#TPUModelRunner), [`localize_token_tensor_and_gather_indices`](../layers/core/sequence_layout.md#SequenceLayoutPlan.localize_token_tensor_and_gather_indices), [`mesh`](../runner/tpu_runner.md#TPUModelRunner.mesh), [`_build_attention_metadata`](../runner/tpu_runner.md#TPUModelRunner._build_attention_metadata), [`_get_padded_token_len`](../runner/tpu_runner.md#_get_padded_token_len), [`attn_ctx`](utils.md#DraftChunkInputs.attn_ctx), [`num_reqs`](utils.md#DraftChunkInputs.num_reqs), [`maybe_share_lm_head`](utils.md#maybe_share_lm_head), [`_build_mamba_state_indices`](../runner/tpu_runner.md#TPUModelRunner._build_mamba_state_indices), [`logger`](eagle3.md#logger), [`_hidden_states_dtype`](../runner/tpu_runner.md#TPUModelRunner._hidden_states_dtype), [`aggregate_request_aligned_tensor`](../layers/core/sequence_layout.md#SequenceLayoutPlan.aggregate_request_aligned_tensor), [`AttentionMetadataBuilderContext`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext), [`_unified_kv_layout`](../runner/tpu_runner.md#TPUModelRunner._unified_kv_layout), [`_dp_num_tokens_across_dp`](../runner/tpu_runner.md#TPUModelRunner._dp_num_tokens_across_dp), [`seq_lens`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.seq_lens), [`use_max_model_len`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.use_max_model_len), [`_dp_lockstep_enabled`](../runner/tpu_runner.md#TPUModelRunner._dp_lockstep_enabled), [`get_kv_cache_spec`](../runner/tpu_runner.md#TPUModelRunner.get_kv_cache_spec), [`maybe_share_embeddings`](utils.md#maybe_share_embeddings), [`enforce_eager`](../runner/tpu_runner.md#TPUModelRunner.enforce_eager), [`position_ids_override`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.position_ids_override), [`sequence_layout_descriptor`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.sequence_layout_descriptor), [`mamba_state_indices`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.mamba_state_indices), [`query_start_loc`](../layers/core/attention_metadata.md#AttentionMetadataBuilderContext.query_start_loc), [`sequence_layout_plan`](utils.md#DraftChunkInputs.sequence_layout_plan)  (+47 more)
- used by: [`_admit_raiden_hybrid_kv_cache`](../distributed/kv_transfer/tpu_connector.md#TPURaidenConnectorWorker._admit_raiden_hybrid_kv_cache), [`_add_pipeline_chunk_buckets`](../runner/tpu_runner.md#TPUModelRunner._add_pipeline_chunk_buckets), [`_warmup_spec_decode_cleanup`](../runner/tpu_runner.md#TPUModelRunner._warmup_spec_decode_cleanup), [`drafter`](../runner/tpu_runner.md#TPUModelRunner.drafter), [`propose_draft_token_ids`](../runner/speculative_decoding_manager.md#SpeculativeDecodingManager.propose_draft_token_ids), [`_num_static_verify_reqs`](../runner/tpu_runner.md#TPUModelRunner._num_static_verify_reqs), [`_async_drafter`](../runner/tpu_runner.md#TPUModelRunner._async_drafter), [`_check_draft_buckets`](../runner/tpu_runner.md#TPUModelRunner._check_draft_buckets)

### <a id="_DpDummyDraft"></a>`_DpDummyDraft`
- def: [`src/vllm_torchtpu/spec_decode/eagle3.py:171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L171)
- doc: Inputs an EP-DP padding chunk replays the draft trace with.
- signature: `class _DpDummyDraft:`
- members:
  - <a id="_DpDummyDraft.bucket"></a>`bucket` — [`L176`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L176)
  - <a id="_DpDummyDraft.chunk"></a>`chunk` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L174)
  - <a id="_DpDummyDraft.combine_aux"></a>`combine_aux` — [`L189`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L189)
  - <a id="_DpDummyDraft.combine_plain"></a>`combine_plain` — [`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L190)
  - <a id="_DpDummyDraft.first_pass_carry"></a>`first_pass_carry` — [`L181`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L181)
  - <a id="_DpDummyDraft.input_ids"></a>`input_ids` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L178)
  - <a id="_DpDummyDraft.loop_bucket"></a>`loop_bucket` — [`L177`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L177)
  - <a id="_DpDummyDraft.loop_hidden"></a>`loop_hidden` — [`L184`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L184)
  - <a id="_DpDummyDraft.loop_input_ids"></a>`loop_input_ids` — [`L182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L182)
  - <a id="_DpDummyDraft.loop_positions"></a>`loop_positions` — [`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L183)
  - <a id="_DpDummyDraft.loop_query_start_loc"></a>`loop_query_start_loc` — [`L185`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L185)
  - <a id="_DpDummyDraft.loop_request_distribution"></a>`loop_request_distribution` — [`L186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L186)
  - <a id="_DpDummyDraft.positions"></a>`positions` — [`L179`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L179)
  - <a id="_DpDummyDraft.target_hidden_states"></a>`target_hidden_states` — [`L180`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L180)
- uses (calls/refs, reference-scoped): [`DraftChunkInputs`](utils.md#DraftChunkInputs)
- used by: [`_build_dp_dummy_draft`](eagle3.md#Eagle3Proposer._build_dp_dummy_draft), [`_dp_dummy_draft_step`](eagle3.md#Eagle3Proposer._dp_dummy_draft_step)

## Functions
- <a id="_collect_topk_indices_buffers"></a>`_collect_topk_indices_buffers(mtp_model)` — [`L134`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L134) — The distinct `topk_indices_buffer` tensors of a DSA MTP draft.
- <a id="_draft_head_modules"></a>`_draft_head_modules(model: torch.nn.Module)` — [`L154`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L154) — The draft's embedding and head modules, keyed by checkpoint-name fragment.
- <a id="_maybe_pad_dim0"></a>`_maybe_pad_dim0(t: torch.Tensor, target_len: int)` — [`L102`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L102) — Right-pad a 1-D or 2-D tensor along dim 0 to `target_len` with zeros.
- <a id="_maybe_pad_dim1"></a>`_maybe_pad_dim1(t: torch.Tensor, target_len: int)` — [`L120`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L120) — Pad the 2nd dimension (dim=1) of a 2D tensor up to target_len.
- <a id="_static_shape_args"></a>`_static_shape_args(fn)` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L61) — Strip dynamo dynamic-dim marks from a compiled region's tensor args.
- <a id="_static_shape_args.wrapper.unmark"></a>`unmark(a)` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L88)
- <a id="_static_shape_args.wrapper"></a>`wrapper(*args, **kwargs)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L87)

## Module values
- <a id="INVALID_TOKEN_ID"></a>`INVALID_TOKEN_ID` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L58)
- <a id="logger"></a>`logger` — [`L131`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/eagle3.py#L131)

