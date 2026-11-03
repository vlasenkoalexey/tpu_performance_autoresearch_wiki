---
title: 'Module: src/vllm_torchtpu/runner/speculative_decoding_manager.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/speculative_decoding_manager.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.speculative_decoding_manager`/
symbols:
  SpeculativeDecodingManager.get_spec_decode_metadata: SpeculativeDecodingManager#get_spec_decode_metadata().
  SpeculativeDecodingManager.propose_draft_token_ids: SpeculativeDecodingManager#propose_draft_token_ids().
  SpeculativeDecodingManager.runner: SpeculativeDecodingManager#runner.
  SpeculativeDecodingManager._meta_cache: SpeculativeDecodingManager#_meta_cache.
  SpecDecodeMetadata.draft_token_ids: SpecDecodeMetadata#draft_token_ids.
  SpecDecodeMetadata.segment_ids: SpecDecodeMetadata#segment_ids.
  SpeculativeDecodingManager.take_draft_token_ids: SpeculativeDecodingManager#take_draft_token_ids().
  SpecDecodeMetadata.draft_lengths: SpecDecodeMetadata#draft_lengths.
  SpecDecodeMetadata: SpecDecodeMetadata#
  SpecDecodeMetadata.draft_lengths_cpu: SpecDecodeMetadata#draft_lengths_cpu.
  SpecDecodeMetadata.target_logits_indices: SpecDecodeMetadata#target_logits_indices.
  SpecDecodeMetadata.bonus_logits_indices: SpecDecodeMetadata#bonus_logits_indices.
  SpecDecodeMetadata.final_logits_indices: SpecDecodeMetadata#final_logits_indices.
  SpecDecodeMetadata.group_indices: SpecDecodeMetadata#group_indices.
  SpeculativeDecodingManager.stage_draft_token_ids_for_host: SpeculativeDecodingManager#stage_draft_token_ids_for_host().
  SpeculativeDecodingManager._draft_token_ids: SpeculativeDecodingManager#_draft_token_ids.
  SpecDecodeMetadata.deferred_draft_token_ids_cpu: SpecDecodeMetadata#deferred_draft_token_ids_cpu.
  SpeculativeDecodingManager._staged_draft_copy: SpeculativeDecodingManager#_staged_draft_copy.
  SpecDecodeMetadata.upload_deferred_draft_token_ids: SpecDecodeMetadata#upload_deferred_draft_token_ids().
  SpeculativeDecodingManager._meta_cache_np: SpeculativeDecodingManager#_meta_cache_np.
  SpeculativeDecodingManager.__init__: SpeculativeDecodingManager#__init__().
  SpeculativeDecodingManager: SpeculativeDecodingManager#
  SpeculativeDecodingManager._meta_cache_key: SpeculativeDecodingManager#_meta_cache_key.
  SpeculativeDecodingManager.spec_token_ids: SpeculativeDecodingManager#spec_token_ids.
---
# Module: [`src/vllm_torchtpu/runner/speculative_decoding_manager.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py)

## Classes
### <a id="SpecDecodeMetadata"></a>`SpecDecodeMetadata`
- def: [`src/vllm_torchtpu/runner/speculative_decoding_manager.py:31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L31)
- doc: Metadata for speculative decoding on Torch/TPU, containing all
- signature: `class SpecDecodeMetadata:`
- members:
  - <a id="SpecDecodeMetadata.upload_deferred_draft_token_ids"></a>`upload_deferred_draft_token_ids(self, device: torch.device)` — [`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L63)
  - <a id="SpecDecodeMetadata.bonus_logits_indices"></a>`bonus_logits_indices` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L49)
  - <a id="SpecDecodeMetadata.deferred_draft_token_ids_cpu"></a>`deferred_draft_token_ids_cpu` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L61)
  - <a id="SpecDecodeMetadata.draft_lengths"></a>`draft_lengths` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L41)
  - <a id="SpecDecodeMetadata.draft_lengths_cpu"></a>`draft_lengths_cpu` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L43)
  - <a id="SpecDecodeMetadata.draft_token_ids"></a>`draft_token_ids` — [`L39`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L39)
  - <a id="SpecDecodeMetadata.final_logits_indices"></a>`final_logits_indices` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L52)
  - <a id="SpecDecodeMetadata.group_indices"></a>`group_indices` — [`L57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L57)
  - <a id="SpecDecodeMetadata.segment_ids"></a>`segment_ids` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L55)
  - <a id="SpecDecodeMetadata.target_logits_indices"></a>`target_logits_indices` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L46)
- used by: [`execute_model`](tpu_runner.md#TPUModelRunner.execute_model), [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`position_ids`](tpu_runner.md#TPUModelRunner.position_ids), [`_sample_spec_verify_chunk`](tpu_runner.md#TPUModelRunner._sample_spec_verify_chunk), [`get_spec_decode_metadata`](speculative_decoding_manager.md#SpeculativeDecodingManager.get_spec_decode_metadata), [`_meta_cache`](speculative_decoding_manager.md#SpeculativeDecodingManager._meta_cache), [`spec_decode_metadata_list`](tpu_runner.md#ExecuteModelState.spec_decode_metadata_list)

### <a id="SpeculativeDecodingManager"></a>`SpeculativeDecodingManager`
- def: [`src/vllm_torchtpu/runner/speculative_decoding_manager.py:70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L70)
- doc: Manages speculative decoding operations, including draft proposal and
- signature: `class SpeculativeDecodingManager:`
- members:
  - <a id="SpeculativeDecodingManager.get_spec_decode_metadata"></a>`get_spec_decode_metadata(self, num_draft_tokens: np.ndarray, cu_num_scheduled_tokens: np.ndarray, padded_num_reqs: int, defer_draft_token_ids: bool = False)` — [`L268`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L268) — Calculates indices for speculative decoding forward pass and — documented in [tpu-model-runner](../../../../concepts/tpu-model-runner.md)
  - <a id="SpeculativeDecodingManager.propose_draft_token_ids"></a>`propose_draft_token_ids(self, sampled_token_ids: list[list[int]] | None, discard_sampled_tokens_req_indices: list[int] | None = None, num_rejected_tokens_np: np.ndarray | None = None, scheduler_output=None, return_device: bool = False, next_tokens_per_chunk: list[torch.Tensor] | None = None, device_seed: torch.Tensor | list[torch.Tensor] | None = None)` — [`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L155) — Proposes draft token IDs based on the speculative decoding method. — documented in [speculative-decoding](../../../../concepts/speculative-decoding.md)
  - <a id="SpeculativeDecodingManager.stage_draft_token_ids_for_host"></a>`stage_draft_token_ids_for_host(self, drafts: torch.Tensor | list[torch.Tensor], real_lens: list[int] | None = None)` — [`L117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L117) — Starts a non-blocking D2H copy of drafts on device.
  - <a id="SpeculativeDecodingManager.take_draft_token_ids"></a>`take_draft_token_ids(self)` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L96)
  - <a id="SpeculativeDecodingManager.runner"></a>`runner` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L76)
  - <a id="SpeculativeDecodingManager.spec_token_ids"></a>`spec_token_ids` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L85)
- protocol/private: <a id="SpeculativeDecodingManager.__init__"></a>`__init__`[`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L75), <a id="SpeculativeDecodingManager._draft_token_ids"></a>`_draft_token_ids`[`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L78), <a id="SpeculativeDecodingManager._meta_cache"></a>`_meta_cache`[`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L91), <a id="SpeculativeDecodingManager._meta_cache_key"></a>`_meta_cache_key`[`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L90), <a id="SpeculativeDecodingManager._meta_cache_np"></a>`_meta_cache_np`[`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L94), <a id="SpeculativeDecodingManager._staged_draft_copy"></a>`_staged_draft_copy`[`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/speculative_decoding_manager.py#L82)
- uses (calls/refs, reference-scoped): [`device`](tpu_runner.md#TPUModelRunner.device), [`propose`](../spec_decode/eagle3.md#Eagle3Proposer.propose), [`speculative_config`](tpu_runner.md#TPUModelRunner.speculative_config), [`num_tokens_paddings`](tpu_runner.md#TPUModelRunner.num_tokens_paddings), [`propose`](../spec_decode/dflash.md#DFlashProposer.propose), [`drafter`](tpu_runner.md#TPUModelRunner.drafter), [`TPUModelRunner`](tpu_runner.md#TPUModelRunner), [`_is_async_drafter`](tpu_runner.md#TPUModelRunner._is_async_drafter), [`_get_padded_token_len`](tpu_runner.md#_get_padded_token_len), [`DFlashProposer`](../spec_decode/dflash.md#DFlashProposer), [`_async_drafter`](tpu_runner.md#TPUModelRunner._async_drafter), [`draft_token_ids`](speculative_decoding_manager.md#SpecDecodeMetadata.draft_token_ids), [`input_ids_cpu`](tpu_runner.md#TPUModelRunner.input_ids_cpu), [`segment_ids`](speculative_decoding_manager.md#SpecDecodeMetadata.segment_ids), [`draft_lengths`](speculative_decoding_manager.md#SpecDecodeMetadata.draft_lengths), [`SpecDecodeMetadata`](speculative_decoding_manager.md#SpecDecodeMetadata), [`bonus_logits_indices`](speculative_decoding_manager.md#SpecDecodeMetadata.bonus_logits_indices), [`draft_lengths_cpu`](speculative_decoding_manager.md#SpecDecodeMetadata.draft_lengths_cpu), [`target_logits_indices`](speculative_decoding_manager.md#SpecDecodeMetadata.target_logits_indices), [`arange_np`](tpu_runner.md#TPUModelRunner.arange_np), [`final_logits_indices`](speculative_decoding_manager.md#SpecDecodeMetadata.final_logits_indices), [`group_indices`](speculative_decoding_manager.md#SpecDecodeMetadata.group_indices), [`deferred_draft_token_ids_cpu`](speculative_decoding_manager.md#SpecDecodeMetadata.deferred_draft_token_ids_cpu)
- used by: [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`position_ids`](tpu_runner.md#TPUModelRunner.position_ids), [`spec_decode_manager`](tpu_runner.md#TPUModelRunner.spec_decode_manager), [`take_draft_token_ids`](tpu_runner.md#TPUModelRunner.take_draft_token_ids)

