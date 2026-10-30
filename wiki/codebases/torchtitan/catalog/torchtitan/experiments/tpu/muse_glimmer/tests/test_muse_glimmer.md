---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.tests.test_muse_glimmer`/
symbols:
  MuseGlimmerTest.test_muse_glimmer_splash_attention_matches_sdpa: MuseGlimmerTest#test_muse_glimmer_splash_attention_matches_sdpa().
  MuseGlimmerTest.test_muse_glimmer_transformer_block_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_transformer_block_cpu_device_parity().
  MuseGlimmerTest.test_muse_glimmer_sliding_window_sdpa_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_sliding_window_sdpa_cpu_device_parity().
  MuseGlimmerTest.test_muse_glimmer_attention_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_attention_cpu_device_parity().
  MuseGlimmerTest.test_muse_glimmer_full_model_training_steps_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_full_model_training_steps_cpu_device_parity().
  MuseGlimmerTest.test_muse_glimmer_embedding_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_embedding_cpu_device_parity().
  MuseGlimmerTest.test_muse_glimmer_output_head_cpu_device_parity: MuseGlimmerTest#test_muse_glimmer_output_head_cpu_device_parity().
  _get_model_config: _get_model_config().
  MuseGlimmerTest._check_attention_parity: MuseGlimmerTest#_check_attention_parity().
  MuseGlimmerTest._is_tpu: MuseGlimmerTest#_is_tpu().
  MuseGlimmerTest._setup_module_cpu_device_from_config: MuseGlimmerTest#_setup_module_cpu_device_from_config().
  MuseGlimmerTest._check_relative_l2: MuseGlimmerTest#_check_relative_l2().
  MuseGlimmerTest._attn_tol: MuseGlimmerTest#_attn_tol().
  MuseGlimmerTest: MuseGlimmerTest#
  MuseGlimmerTest.setUp: MuseGlimmerTest#setUp().
  _naive_sliding_window_attention: _naive_sliding_window_attention().
  LAYER_TEST_CONFIGS: LAYER_TEST_CONFIGS.
  SDPA_TEST_CONFIGS: SDPA_TEST_CONFIGS.
  SPLASH_TEST_CONFIGS: SPLASH_TEST_CONFIGS.
  FULL_MODEL_TEST_CONFIGS: FULL_MODEL_TEST_CONFIGS.
  MuseGlimmerTest._perturb_gain_norms: MuseGlimmerTest#_perturb_gain_norms().
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py)

> **Collapsed catalog** (21 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="FULL_MODEL_TEST_CONFIGS"></a>`FULL_MODEL_TEST_CONFIGS` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L97)
- <a id="LAYER_TEST_CONFIGS"></a>`LAYER_TEST_CONFIGS` — [`L79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L79)
- <a id="MuseGlimmerTest"></a>`MuseGlimmerTest` — [`L115`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L115)
- <a id="MuseGlimmerTest._attn_tol"></a>`MuseGlimmerTest._attn_tol` — [`L133`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L133)
- <a id="MuseGlimmerTest._check_attention_parity"></a>`MuseGlimmerTest._check_attention_parity` — [`L190`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L190)
- <a id="MuseGlimmerTest._check_relative_l2"></a>`MuseGlimmerTest._check_relative_l2` — [`L170`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L170)
- <a id="MuseGlimmerTest._is_tpu"></a>`MuseGlimmerTest._is_tpu` — [`L130`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L130)
- <a id="MuseGlimmerTest._perturb_gain_norms"></a>`MuseGlimmerTest._perturb_gain_norms` — [`L217`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L217)
- <a id="MuseGlimmerTest._setup_module_cpu_device_from_config"></a>`MuseGlimmerTest._setup_module_cpu_device_from_config` — [`L151`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L151)
- <a id="MuseGlimmerTest.setUp"></a>`MuseGlimmerTest.setUp` — [`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L122)
- <a id="MuseGlimmerTest.test_muse_glimmer_attention_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_attention_cpu_device_parity` — [`L315`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L315)
- <a id="MuseGlimmerTest.test_muse_glimmer_embedding_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_embedding_cpu_device_parity` — [`L368`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L368)
- <a id="MuseGlimmerTest.test_muse_glimmer_full_model_training_steps_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_full_model_training_steps_cpu_device_parity` — [`L612`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L612)
- <a id="MuseGlimmerTest.test_muse_glimmer_output_head_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_output_head_cpu_device_parity` — [`L410`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L410)
- <a id="MuseGlimmerTest.test_muse_glimmer_sliding_window_sdpa_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_sliding_window_sdpa_cpu_device_parity` — [`L229`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L229)
- <a id="MuseGlimmerTest.test_muse_glimmer_splash_attention_matches_sdpa"></a>`MuseGlimmerTest.test_muse_glimmer_splash_attention_matches_sdpa` — [`L525`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L525)
- <a id="MuseGlimmerTest.test_muse_glimmer_transformer_block_cpu_device_parity"></a>`MuseGlimmerTest.test_muse_glimmer_transformer_block_cpu_device_parity` — [`L461`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L461)
- <a id="SDPA_TEST_CONFIGS"></a>`SDPA_TEST_CONFIGS` — [`L73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L73)
- <a id="SPLASH_TEST_CONFIGS"></a>`SPLASH_TEST_CONFIGS` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L87)
- <a id="_get_model_config"></a>`_get_model_config` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L30)
- <a id="_naive_sliding_window_attention"></a>`_naive_sliding_window_attention` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_muse_glimmer.py#L41)
