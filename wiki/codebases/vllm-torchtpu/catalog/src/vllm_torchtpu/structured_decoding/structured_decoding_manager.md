---
title: 'Module: src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.structured_decoding.structured_decoding_manager`/StructuredDecodingManager#
symbols:
  StructuredDecodingManager.device_dummy_bitmask: device_dummy_bitmask.
  StructuredDecodingManager.prepare_structured_decoding_input: prepare_structured_decoding_input().
  StructuredDecodingManager.prepare_spec_structured_decoding_input: prepare_spec_structured_decoding_input().
  StructuredDecodingManager.vocab_size: vocab_size.
  StructuredDecodingManager.grammar_bitmask_cpu: grammar_bitmask_cpu.
  StructuredDecodingManager.require_structured_out_cpu: require_structured_out_cpu.
  StructuredDecodingManager.mask_spec_logits: mask_spec_logits().
  StructuredDecodingManager.mask_logits: mask_logits().
  StructuredDecodingManager.structured_decode: structured_decode().
  StructuredDecodingManager.structured_decode_arange: structured_decode_arange.
  StructuredDecodingManager.device: device.
  StructuredDecodingManager.device_all_false_require: device_all_false_require.
  StructuredDecodingManager.target_grammar_bitmask_cpu: target_grammar_bitmask_cpu.
  StructuredDecodingManager.device_all_true_require: device_all_true_require.
  StructuredDecodingManager.require_structured_out_target_cpu: require_structured_out_target_cpu.
  StructuredDecodingManager._structured_decode: _structured_decode().
  StructuredDecodingManager.apply_grammar_bitmask: apply_grammar_bitmask().
  StructuredDecodingManager: ''
  StructuredDecodingManager.__init__: __init__().
  StructuredDecodingManager.runner: runner.
---
# Module: [`src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py)

## Classes
### <a id="StructuredDecodingManager"></a>`StructuredDecodingManager`
- def: [`src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py:32`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L32)
- signature: `class StructuredDecodingManager:`
- members:
  - <a id="StructuredDecodingManager.apply_grammar_bitmask"></a>`apply_grammar_bitmask(self, logits: torch.Tensor, grammar_bitmask: torch.Tensor, arange: torch.Tensor)` — [`L354`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L354)
  - <a id="StructuredDecodingManager.mask_logits"></a>`mask_logits(self, logits: torch.Tensor, grammar_output: GrammarOutput, cur_start_idx: int, cur_end_idx: int)` — [`L244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L244) — Applies the grammar bitmask to one non-spec chunk's logits. — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="StructuredDecodingManager.mask_spec_logits"></a>`mask_spec_logits(self, target_logits: torch.Tensor | None, bonus_logits: torch.Tensor, grammar_output: GrammarOutput, scheduled_spec_decode_tokens: Mapping[str, Sequence[int]], draft_lengths_cpu: np.ndarray | None, cur_start_idx: int, cur_end_idx: int)` — [`L273`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L273) — Applies the grammar bitmask to both bonus and target(if not None). — documented in [tracing-annotations](../../../../concepts/tracing-annotations.md)
  - <a id="StructuredDecodingManager.prepare_spec_structured_decoding_input"></a>`prepare_spec_structured_decoding_input(self, target_logits: torch.Tensor | None, bonus_logits: torch.Tensor, grammar_output: GrammarOutput, scheduled_spec_decode_tokens: Mapping[str, Sequence[int]], draft_lengths_cpu: np.ndarray | None, cur_start_idx: int, cur_end_idx: int)` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L152) — Builds the `structured_decode` inputs for one spec decoding chunk.
  - <a id="StructuredDecodingManager.prepare_structured_decoding_input"></a>`prepare_structured_decoding_input(self, logits: torch.Tensor, grammar_output: GrammarOutput, cur_start_idx: int, cur_end_idx: int)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L92) — Builds the device inputs for `structured_decode` for one chunk.
  - <a id="StructuredDecodingManager.structured_decode"></a>`structured_decode(self, require_struct_decoding: torch.Tensor, grammar_bitmask: torch.Tensor, logits: torch.Tensor, arange: torch.Tensor)` — [`L330`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L330)
  - <a id="StructuredDecodingManager.device"></a>`device` — [`L49`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L49)
  - <a id="StructuredDecodingManager.device_all_false_require"></a>`device_all_false_require` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L58)
  - <a id="StructuredDecodingManager.device_all_true_require"></a>`device_all_true_require` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L55)
  - <a id="StructuredDecodingManager.device_dummy_bitmask"></a>`device_dummy_bitmask` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L61)
  - <a id="StructuredDecodingManager.grammar_bitmask_cpu"></a>`grammar_bitmask_cpu` — [`L37`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L37)
  - <a id="StructuredDecodingManager.require_structured_out_cpu"></a>`require_structured_out_cpu` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L43)
  - <a id="StructuredDecodingManager.require_structured_out_target_cpu"></a>`require_structured_out_target_cpu` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L85)
  - <a id="StructuredDecodingManager.runner"></a>`runner` — [`L34`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L34)
  - <a id="StructuredDecodingManager.structured_decode_arange"></a>`structured_decode_arange` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L52)
  - <a id="StructuredDecodingManager.target_grammar_bitmask_cpu"></a>`target_grammar_bitmask_cpu` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L79)
  - <a id="StructuredDecodingManager.vocab_size"></a>`vocab_size` — [`L35`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L35)
- protocol/private: <a id="StructuredDecodingManager.__init__"></a>`__init__`[`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L33), <a id="StructuredDecodingManager._structured_decode"></a>`_structured_decode`[`L341`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/structured_decoding/structured_decoding_manager.py#L341)
- uses (calls/refs, reference-scoped): [`device`](../runner/tpu_runner.md#TPUModelRunner.device), [`speculative_config`](../runner/tpu_runner.md#TPUModelRunner.speculative_config), [`num_tokens_paddings`](../runner/tpu_runner.md#TPUModelRunner.num_tokens_paddings), [`max_num_reqs`](../runner/tpu_runner.md#TPUModelRunner.max_num_reqs), [`TraceAnnotation`](../tracing/annotation.md#TraceAnnotation), [`_mtp_prefill_only`](../runner/tpu_runner.md#TPUModelRunner._mtp_prefill_only), [`TPUModelRunner`](../runner/tpu_runner.md#TPUModelRunner), [`_get_padded_token_len`](../runner/tpu_runner.md#_get_padded_token_len), [`vocab_size`](../runner/tpu_runner.md#TPUModelRunner.vocab_size)
- used by: [`sample_tokens`](../runner/tpu_runner.md#TPUModelRunner.sample_tokens), [`_sample_spec_verify_chunk`](../runner/tpu_runner.md#TPUModelRunner._sample_spec_verify_chunk), [`_precompile_structured_decoding`](../runner/tpu_runner.md#TPUModelRunner._precompile_structured_decoding), [`_verify_logits_paddings`](../runner/tpu_runner.md#TPUModelRunner._verify_logits_paddings), [`structured_decoding_manager`](../runner/tpu_runner.md#TPUModelRunner.structured_decoding_manager)

