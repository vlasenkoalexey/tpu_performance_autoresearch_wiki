---
title: 'Module: torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3_5.tests.test_qwen3_5`/
symbols:
  Qwen35Test.test_flavors_and_registry: Qwen35Test#test_flavors_and_registry().
  Qwen35Test.test_qwen3_5_hf_reference_parity: Qwen35Test#test_qwen3_5_hf_reference_parity().
  Qwen35Test.test_35b_recipe: Qwen35Test#test_35b_recipe().
  Qwen35Test.test_model_isolates_packed_documents: Qwen35Test#test_model_isolates_packed_documents().
  Qwen35Test._is_tpu: Qwen35Test#_is_tpu().
  Qwen35Test.test_chunked_gated_delta_resets_at_documents: Qwen35Test#test_chunked_gated_delta_resets_at_documents().
  Qwen35Test.test_gated_delta_net_isolates_packed_documents: Qwen35Test#test_gated_delta_net_isolates_packed_documents().
  Qwen35Test.test_chunked_gated_delta_matches_recurrent: Qwen35Test#test_chunked_gated_delta_matches_recurrent().
  Qwen35Test.test_causal_conv_resets_at_documents: Qwen35Test#test_causal_conv_resets_at_documents().
  Qwen35Test.test_gated_delta_net_isolates_batch_sequences: Qwen35Test#test_gated_delta_net_isolates_batch_sequences().
  Qwen35Test.test_attention_isolates_packed_documents: Qwen35Test#test_attention_isolates_packed_documents().
  _relative_l2_error: _relative_l2_error().
  Qwen35Test.forward_backward: Qwen35Test#forward_backward().
  Qwen35Test.setUp: Qwen35Test#setUp().
  Qwen35Test.run: Qwen35Test#run().
  Qwen35Test.test_causal_conv_adds_bf16_taps_in_fp32: Qwen35Test#test_causal_conv_adds_bf16_taps_in_fp32().
  _recurrent_gated_delta_reference: _recurrent_gated_delta_reference().
  _packed_positions: _packed_positions().
  Qwen35Test: Qwen35Test#
  Qwen35Test._build_hf_reference: Qwen35Test#_build_hf_reference().
---
# Module: [`torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Qwen35Test"></a>`Qwen35Test` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L98)
- <a id="Qwen35Test._build_hf_reference"></a>`Qwen35Test._build_hf_reference` — [`L111`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L111)
- <a id="Qwen35Test._is_tpu"></a>`Qwen35Test._is_tpu` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L108)
- <a id="Qwen35Test.forward_backward"></a>`Qwen35Test.forward_backward` — [`L681`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L681)
- <a id="Qwen35Test.run"></a>`Qwen35Test.run` — [`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L359)
- <a id="Qwen35Test.setUp"></a>`Qwen35Test.setUp` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L101)
- <a id="Qwen35Test.test_35b_recipe"></a>`Qwen35Test.test_35b_recipe` — [`L857`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L857)
- <a id="Qwen35Test.test_attention_isolates_packed_documents"></a>`Qwen35Test.test_attention_isolates_packed_documents` — [`L749`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L749)
- <a id="Qwen35Test.test_causal_conv_adds_bf16_taps_in_fp32"></a>`Qwen35Test.test_causal_conv_adds_bf16_taps_in_fp32` — [`L513`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L513)
- <a id="Qwen35Test.test_causal_conv_resets_at_documents"></a>`Qwen35Test.test_causal_conv_resets_at_documents` — [`L459`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L459)
- <a id="Qwen35Test.test_chunked_gated_delta_matches_recurrent"></a>`Qwen35Test.test_chunked_gated_delta_matches_recurrent` — [`L335`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L335)
- <a id="Qwen35Test.test_chunked_gated_delta_resets_at_documents"></a>`Qwen35Test.test_chunked_gated_delta_resets_at_documents` — [`L394`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L394)
- <a id="Qwen35Test.test_flavors_and_registry"></a>`Qwen35Test.test_flavors_and_registry` — [`L803`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L803)
- <a id="Qwen35Test.test_gated_delta_net_isolates_batch_sequences"></a>`Qwen35Test.test_gated_delta_net_isolates_batch_sequences` — [`L545`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L545)
- <a id="Qwen35Test.test_gated_delta_net_isolates_packed_documents"></a>`Qwen35Test.test_gated_delta_net_isolates_packed_documents` — [`L588`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L588)
- <a id="Qwen35Test.test_model_isolates_packed_documents"></a>`Qwen35Test.test_model_isolates_packed_documents` — [`L644`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L644)
- <a id="Qwen35Test.test_qwen3_5_hf_reference_parity"></a>`Qwen35Test.test_qwen3_5_hf_reference_parity` — [`L180`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L180) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="_packed_positions"></a>`_packed_positions` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L86)
- <a id="_recurrent_gated_delta_reference"></a>`_recurrent_gated_delta_reference` — [`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L49)
- <a id="_relative_l2_error"></a>`_relative_l2_error` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3_5/tests/test_qwen3_5.py#L91)
