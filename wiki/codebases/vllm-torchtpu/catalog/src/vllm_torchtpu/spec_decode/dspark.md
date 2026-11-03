---
title: 'Module: src/vllm_torchtpu/spec_decode/dspark.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/spec_decode/dspark.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.spec_decode.dspark`/
symbols:
  DSparkProposer._observe_draft_aux: DSparkProposer#_observe_draft_aux().
  DSparkProposer._draft_confidences: DSparkProposer#_draft_confidences.
  DSparkProposer.sample_from_anchor: DSparkProposer#sample_from_anchor.
  DSparkProposer._dflash_forward_and_sample: DSparkProposer#_dflash_forward_and_sample().
  logger: logger.
  DSparkProposer.load_model: DSparkProposer#load_model().
  DSparkProposer.take_draft_confidences: DSparkProposer#take_draft_confidences().
  DSparkProposer: DSparkProposer#
  DraftConfidences: DraftConfidences#
  DSparkProposer.__init__: DSparkProposer#__init__().
  DSparkProposer._query_block_size: DSparkProposer#_query_block_size().
  DSparkProposer.use_confidence_head: DSparkProposer#use_confidence_head.
  DraftConfidences.chunks: DraftConfidences#chunks.
  DraftConfidences.spans: DraftConfidences#spans.
  DSparkProposer._force_share_target_embeddings: DSparkProposer#_force_share_target_embeddings.
---
# Module: [`src/vllm_torchtpu/spec_decode/dspark.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py)

## Classes
### <a id="DSparkProposer"></a>`DSparkProposer`  ·  implements/extends DFlashProposer
- def: [`src/vllm_torchtpu/spec_decode/dspark.py:57`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L57)
- signature: `class DSparkProposer(DFlashProposer):`
- members:
  - <a id="DSparkProposer._dflash_forward_and_sample"></a>`_dflash_forward_and_sample(self, input_ids: torch.Tensor, positions: torch.Tensor, block_size: int)` — [`L158`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L158) — Backbone forward + sequential greedy Markov sampling, in-graph.
  - <a id="DSparkProposer.load_model"></a>`load_model(self, target_model)` — [`L124`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L124)
  - <a id="DSparkProposer.take_draft_confidences"></a>`take_draft_confidences(self)` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L152) — The last proposal's confidences; None once taken.
  - <a id="DSparkProposer.sample_from_anchor"></a>`sample_from_anchor` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L68)
  - <a id="DSparkProposer.use_confidence_head"></a>`use_confidence_head` — [`L88`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L88)
- protocol/private: <a id="DSparkProposer.__init__"></a>`__init__`[`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L58), <a id="DSparkProposer._draft_confidences"></a>`_draft_confidences`[`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L89), <a id="DSparkProposer._force_share_target_embeddings"></a>`_force_share_target_embeddings`[`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L116), <a id="DSparkProposer._observe_draft_aux"></a>`_observe_draft_aux`[`L140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L140), <a id="DSparkProposer._query_block_size"></a>`_query_block_size`[`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L118)
- uses (calls/refs, reference-scoped): [`load_model`](dflash.md#DFlashProposer.load_model), [`draft_model`](dflash.md#DFlashProposer.draft_model), [`DraftChunkInputs`](utils.md#DraftChunkInputs), [`block_size`](dflash.md#DFlashProposer.block_size), [`num_reqs`](utils.md#DraftChunkInputs.num_reqs), [`DFlashProposer`](dflash.md#DFlashProposer), [`speculative_config`](dflash.md#DFlashProposer.speculative_config), [`start_index`](utils.md#DraftChunkInputs.start_index), [`logger`](dspark.md#logger), [`__init__`](dflash.md#DFlashProposer.__init__), [`DraftConfidences`](dspark.md#DraftConfidences), [`chunks`](dspark.md#DraftConfidences.chunks), [`spans`](dspark.md#DraftConfidences.spans)
- used by: [`load_model`](dflash.md#DFlashProposer.load_model), [`_num_static_verify_reqs`](../runner/tpu_runner.md#TPUModelRunner._num_static_verify_reqs), [`DFlashProposer`](dflash.md#DFlashProposer), [`_dflash_forward_and_sample`](dflash.md#DFlashProposer._dflash_forward_and_sample), [`_observe_draft_aux`](dflash.md#DFlashProposer._observe_draft_aux), [`_query_block_size`](dflash.md#DFlashProposer._query_block_size)

### <a id="DraftConfidences"></a>`DraftConfidences`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/spec_decode/dspark.py:48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L48)
- doc: One proposal's per-chunk `[rows, K]` acceptance confidences at the
- signature: `class DraftConfidences(NamedTuple):`
- members:
  - <a id="DraftConfidences.chunks"></a>`chunks` — [`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L53)
  - <a id="DraftConfidences.spans"></a>`spans` — [`L54`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L54)
- used by: [`_observe_draft_aux`](dspark.md#DSparkProposer._observe_draft_aux), [`_draft_confidences`](dspark.md#DSparkProposer._draft_confidences), [`take_draft_confidences`](dspark.md#DSparkProposer.take_draft_confidences)

## Module values
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/spec_decode/dspark.py#L45)

