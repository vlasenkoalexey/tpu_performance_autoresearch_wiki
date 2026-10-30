---
title: 'Module: torchtitan/experiments/tpu/tests/test_bld_layout.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_bld_layout.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_bld_layout`/
symbols:
  _llama3_block: _llama3_block().
  _cossin_rope: _cossin_rope().
  BLDLayoutTest.test_block_matches_upstream: BLDLayoutTest#test_block_matches_upstream().
  BLDLayoutTest.test_cossin_rotate_is_bit_exact: BLDLayoutTest#test_cossin_rotate_is_bit_exact().
  BLDLayoutTest.test_qkv_subclass_swapped_later: BLDLayoutTest#test_qkv_subclass_swapped_later().
  _BLOCKS: _BLOCKS.
  _qwen3_block: _qwen3_block().
  _packed_qwen3_block: _packed_qwen3_block().
  _HEAD_DIM: _HEAD_DIM.
  _build_pair: _build_pair().
  BLDLayoutTest.test_ineligible_block_is_untouched: BLDLayoutTest#test_ineligible_block_is_untouched().
  _SEQ_LEN: _SEQ_LEN.
  BLDLayoutTest.test_idempotent: BLDLayoutTest#test_idempotent().
  BLDLayoutTest.test_instance_forward_wrapper_is_untouched: BLDLayoutTest#test_instance_forward_wrapper_is_untouched().
  BLDLayoutTest.test_generated_classes_pickle: BLDLayoutTest#test_generated_classes_pickle().
  _DIM: _DIM.
  _BATCH: _BATCH.
  BLDSkipReasonTest.test_skip_reason: BLDSkipReasonTest#test_skip_reason().
  _MAX_LEN: _MAX_LEN.
  BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE: BLDLayoutTest#test_ineligible_block_is_untouched().CustomRoPE#
  BLDLayoutTest: BLDLayoutTest#
  BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE.forward: BLDLayoutTest#test_ineligible_block_is_untouched().CustomRoPE#forward().
  BLDSkipReasonTest: BLDSkipReasonTest#
---
# Module: [`torchtitan/experiments/tpu/tests/test_bld_layout.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py)

> **Collapsed catalog** (23 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BLDLayoutTest"></a>`BLDLayoutTest` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L94)
- <a id="BLDLayoutTest.test_block_matches_upstream"></a>`BLDLayoutTest.test_block_matches_upstream` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L115)
- <a id="BLDLayoutTest.test_cossin_rotate_is_bit_exact"></a>`BLDLayoutTest.test_cossin_rotate_is_bit_exact` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L96)
- <a id="BLDLayoutTest.test_generated_classes_pickle"></a>`BLDLayoutTest.test_generated_classes_pickle` — [`L192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L192)
- <a id="BLDLayoutTest.test_idempotent"></a>`BLDLayoutTest.test_idempotent` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L142)
- <a id="BLDLayoutTest.test_ineligible_block_is_untouched"></a>`BLDLayoutTest.test_ineligible_block_is_untouched` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L150)
- <a id="BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE"></a>`BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L153)
- <a id="BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE.forward"></a>`BLDLayoutTest.test_ineligible_block_is_untouched.CustomRoPE.forward` — [`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L155)
- <a id="BLDLayoutTest.test_instance_forward_wrapper_is_untouched"></a>`BLDLayoutTest.test_instance_forward_wrapper_is_untouched` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L183)
- <a id="BLDLayoutTest.test_qkv_subclass_swapped_later"></a>`BLDLayoutTest.test_qkv_subclass_swapped_later` — [`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L166)
- <a id="BLDSkipReasonTest"></a>`BLDSkipReasonTest` — [`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L201)
- <a id="BLDSkipReasonTest.test_skip_reason"></a>`BLDSkipReasonTest.test_skip_reason` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L208)
- <a id="_BATCH"></a>`_BATCH` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L27)
- <a id="_BLOCKS"></a>`_BLOCKS` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L72)
- <a id="_DIM"></a>`_DIM` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L23)
- <a id="_HEAD_DIM"></a>`_HEAD_DIM` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L24)
- <a id="_MAX_LEN"></a>`_MAX_LEN` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L25)
- <a id="_SEQ_LEN"></a>`_SEQ_LEN` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L26)
- <a id="_build_pair"></a>`_build_pair` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L85)
- <a id="_cossin_rope"></a>`_cossin_rope` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L30)
- <a id="_llama3_block"></a>`_llama3_block` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L50)
- <a id="_packed_qwen3_block"></a>`_packed_qwen3_block` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L68)
- <a id="_qwen3_block"></a>`_qwen3_block` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_bld_layout.py#L36)
