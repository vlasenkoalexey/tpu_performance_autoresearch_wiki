---
title: 'Module: torchtitan/experiments/rl/tests/test_bitwise_parity.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_bitwise_parity.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_bitwise_parity`/
symbols:
  build_trainer_model: build_trainer_model().
  build_inference_engine: build_inference_engine().
  BitwiseParityTestBase.setUpClass: BitwiseParityTestBase#setUpClass().
  BitwiseParityTestBase.train_context: BitwiseParityTestBase#train_context.
  _flex_prefill_logprobs: _flex_prefill_logprobs().
  BitwiseParityTestBase.test_trainer_vs_vllm_prefill: BitwiseParityTestBase#test_trainer_vs_vllm_prefill().
  BitwiseParityTestBase: BitwiseParityTestBase#
  BitwiseParityTestBase.test_batch_invariance: BitwiseParityTestBase#test_batch_invariance().
  BitwiseParityTestBase.test_vllm_decode_vs_prefill: BitwiseParityTestBase#test_vllm_decode_vs_prefill().
  TestBitwiseParityQwen35DebugVarlen.test_vllm_prefill_and_decode_batch_invariance: TestBitwiseParityQwen35DebugVarlen#test_vllm_prefill_and_decode_batch_invariance().
  _qwen3_5_debug_bitwise_config: _qwen3_5_debug_bitwise_config().
  BitwiseParityTestBase.prompt_ids: BitwiseParityTestBase#prompt_ids.
  BitwiseParityTestBase.engine: BitwiseParityTestBase#engine.
  vllm_prefill: vllm_prefill().
  _sync_trainer_weights_to_vllm: _sync_trainer_weights_to_vllm().
  vllm_2nd_pass_prefill: vllm_2nd_pass_prefill().
  compute_trainer_prefill_logprobs: compute_trainer_prefill_logprobs().
  _varlen_prefill_logprobs: _varlen_prefill_logprobs().
  vllm_generate: vllm_generate().
  _make_prompt_tokens: _make_prompt_tokens().
  _run_engine: _run_engine().
  BitwiseParityTestBase.model: BitwiseParityTestBase#model.
  BitwiseParityTestBase.tearDownClass: BitwiseParityTestBase#tearDownClass().
  BitwiseParityTestBase._assert_logprobs_equal: BitwiseParityTestBase#_assert_logprobs_equal().
  BitwiseParityTestBase.config_fn: BitwiseParityTestBase#config_fn.
  BitwiseParityTestBase.attn_backend: BitwiseParityTestBase#attn_backend.
  BitwiseParityTestBase.device: BitwiseParityTestBase#device.
  TestBitwiseParityVarlen: TestBitwiseParityVarlen#
  TestBitwiseParityVarlen.config_fn: TestBitwiseParityVarlen#config_fn.
  TestBitwiseParityFlex: TestBitwiseParityFlex#
  TestBitwiseParityFlex.config_fn: TestBitwiseParityFlex#config_fn.
  TestBitwiseParityQwen35Varlen: TestBitwiseParityQwen35Varlen#
  TestBitwiseParityQwen35Varlen.config_fn: TestBitwiseParityQwen35Varlen#config_fn.
  TestBitwiseParityQwen35DebugVarlen: TestBitwiseParityQwen35DebugVarlen#
  TestBitwiseParityQwen35DebugVarlen.config_fn: TestBitwiseParityQwen35DebugVarlen#config_fn.
  TestBitwiseParityMoEEP: TestBitwiseParityMoEEP#
  TestBitwiseParityMoEEP.config_fn: TestBitwiseParityMoEEP#config_fn.
  TestBitwiseParityGptOssVarlen: TestBitwiseParityGptOssVarlen#
  TestBitwiseParityGptOssVarlen.config_fn: TestBitwiseParityGptOssVarlen#config_fn.
  _extract_logprobs_from_prompt: _extract_logprobs_from_prompt().
  _PREFILL_PARAMS: _PREFILL_PARAMS.
  BitwiseParityTestBase.min_world_size: BitwiseParityTestBase#min_world_size.
  BitwiseParityTestBase.sync_weights_from_trainer: BitwiseParityTestBase#sync_weights_from_trainer.
  TestBitwiseParityQwen35DebugVarlen.MAX_GEN_TOKENS: TestBitwiseParityQwen35DebugVarlen#MAX_GEN_TOKENS.
  logger: logger.
  _set_generator_determinism: _set_generator_determinism().
  _FILLER_TEXT: _FILLER_TEXT.
  BitwiseParityTestBase.BATCH_SIZE: BitwiseParityTestBase#BATCH_SIZE.
  BitwiseParityTestBase.PROMPT_LENGTH: BitwiseParityTestBase#PROMPT_LENGTH.
  BitwiseParityTestBase.MAX_GEN_TOKENS: BitwiseParityTestBase#MAX_GEN_TOKENS.
  BitwiseParityTestBase.hf_assets_env_var: BitwiseParityTestBase#hf_assets_env_var.
  BitwiseParityTestBase.dump_folder_env_var: BitwiseParityTestBase#dump_folder_env_var.
  BitwiseParityTestBase.__test__: BitwiseParityTestBase#__test__.
  TestBitwiseParityVarlen.__test__: TestBitwiseParityVarlen#__test__.
  TestBitwiseParityVarlen.attn_backend: TestBitwiseParityVarlen#attn_backend.
  TestBitwiseParityFlex.__test__: TestBitwiseParityFlex#__test__.
  TestBitwiseParityFlex.attn_backend: TestBitwiseParityFlex#attn_backend.
  TestBitwiseParityQwen35Varlen.__test__: TestBitwiseParityQwen35Varlen#__test__.
  TestBitwiseParityQwen35Varlen.attn_backend: TestBitwiseParityQwen35Varlen#attn_backend.
  TestBitwiseParityQwen35Varlen.min_world_size: TestBitwiseParityQwen35Varlen#min_world_size.
  TestBitwiseParityQwen35DebugVarlen.__test__: TestBitwiseParityQwen35DebugVarlen#__test__.
  TestBitwiseParityQwen35DebugVarlen.attn_backend: TestBitwiseParityQwen35DebugVarlen#attn_backend.
  TestBitwiseParityQwen35DebugVarlen.min_world_size: TestBitwiseParityQwen35DebugVarlen#min_world_size.
  TestBitwiseParityQwen35DebugVarlen.sync_weights_from_trainer: TestBitwiseParityQwen35DebugVarlen#sync_weights_from_trainer.
  TestBitwiseParityQwen35DebugVarlen.BATCH_SIZE: TestBitwiseParityQwen35DebugVarlen#BATCH_SIZE.
  TestBitwiseParityQwen35DebugVarlen.PROMPT_LENGTH: TestBitwiseParityQwen35DebugVarlen#PROMPT_LENGTH.
  TestBitwiseParityMoEEP.__test__: TestBitwiseParityMoEEP#__test__.
  TestBitwiseParityMoEEP.BATCH_SIZE: TestBitwiseParityMoEEP#BATCH_SIZE.
  TestBitwiseParityMoEEP.PROMPT_LENGTH: TestBitwiseParityMoEEP#PROMPT_LENGTH.
  TestBitwiseParityMoEEP.MAX_GEN_TOKENS: TestBitwiseParityMoEEP#MAX_GEN_TOKENS.
  TestBitwiseParityMoEEP.attn_backend: TestBitwiseParityMoEEP#attn_backend.
  TestBitwiseParityMoEEP.min_world_size: TestBitwiseParityMoEEP#min_world_size.
  TestBitwiseParityMoEEP.hf_assets_env_var: TestBitwiseParityMoEEP#hf_assets_env_var.
  TestBitwiseParityGptOssVarlen.__test__: TestBitwiseParityGptOssVarlen#__test__.
  TestBitwiseParityGptOssVarlen.attn_backend: TestBitwiseParityGptOssVarlen#attn_backend.
  TestBitwiseParityGptOssVarlen.sync_weights_from_trainer: TestBitwiseParityGptOssVarlen#sync_weights_from_trainer.
---
# Module: [`torchtitan/experiments/rl/tests/test_bitwise_parity.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py)

> **Collapsed catalog** (76 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BitwiseParityTestBase"></a>`BitwiseParityTestBase` — [`L589`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L589)
- <a id="BitwiseParityTestBase.BATCH_SIZE"></a>`BitwiseParityTestBase.BATCH_SIZE` — [`L594`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L594)
- <a id="BitwiseParityTestBase.MAX_GEN_TOKENS"></a>`BitwiseParityTestBase.MAX_GEN_TOKENS` — [`L596`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L596)
- <a id="BitwiseParityTestBase.PROMPT_LENGTH"></a>`BitwiseParityTestBase.PROMPT_LENGTH` — [`L595`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L595)
- <a id="BitwiseParityTestBase.__test__"></a>`BitwiseParityTestBase.__test__` — [`L592`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L592)
- <a id="BitwiseParityTestBase._assert_logprobs_equal"></a>`BitwiseParityTestBase._assert_logprobs_equal` — [`L713`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L713)
- <a id="BitwiseParityTestBase.attn_backend"></a>`BitwiseParityTestBase.attn_backend` — [`L599`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L599)
- <a id="BitwiseParityTestBase.config_fn"></a>`BitwiseParityTestBase.config_fn` — [`L598`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L598)
- <a id="BitwiseParityTestBase.device"></a>`BitwiseParityTestBase.device` — [`L685`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L685)
- <a id="BitwiseParityTestBase.dump_folder_env_var"></a>`BitwiseParityTestBase.dump_folder_env_var` — [`L605`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L605)
- <a id="BitwiseParityTestBase.engine"></a>`BitwiseParityTestBase.engine` — [`L612`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L612)
- <a id="BitwiseParityTestBase.hf_assets_env_var"></a>`BitwiseParityTestBase.hf_assets_env_var` — [`L601`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L601)
- <a id="BitwiseParityTestBase.min_world_size"></a>`BitwiseParityTestBase.min_world_size` — [`L600`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L600)
- <a id="BitwiseParityTestBase.model"></a>`BitwiseParityTestBase.model` — [`L611`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L611)
- <a id="BitwiseParityTestBase.prompt_ids"></a>`BitwiseParityTestBase.prompt_ids` — [`L613`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L613)
- <a id="BitwiseParityTestBase.setUpClass"></a>`BitwiseParityTestBase.setUpClass` — [`L616`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L616)
- <a id="BitwiseParityTestBase.sync_weights_from_trainer"></a>`BitwiseParityTestBase.sync_weights_from_trainer` — [`L608`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L608)
- <a id="BitwiseParityTestBase.tearDownClass"></a>`BitwiseParityTestBase.tearDownClass` — [`L696`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L696)
- <a id="BitwiseParityTestBase.test_batch_invariance"></a>`BitwiseParityTestBase.test_batch_invariance` — [`L744`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L744)
- <a id="BitwiseParityTestBase.test_trainer_vs_vllm_prefill"></a>`BitwiseParityTestBase.test_trainer_vs_vllm_prefill` — [`L780`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L780)
- <a id="BitwiseParityTestBase.test_vllm_decode_vs_prefill"></a>`BitwiseParityTestBase.test_vllm_decode_vs_prefill` — [`L806`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L806)
- <a id="BitwiseParityTestBase.train_context"></a>`BitwiseParityTestBase.train_context` — [`L685`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L685)
- <a id="TestBitwiseParityFlex"></a>`TestBitwiseParityFlex` — [`L838`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L838)
- <a id="TestBitwiseParityFlex.__test__"></a>`TestBitwiseParityFlex.__test__` — [`L841`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L841)
- <a id="TestBitwiseParityFlex.attn_backend"></a>`TestBitwiseParityFlex.attn_backend` — [`L843`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L843)
- <a id="TestBitwiseParityFlex.config_fn"></a>`TestBitwiseParityFlex.config_fn` — [`L842`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L842)
- <a id="TestBitwiseParityGptOssVarlen"></a>`TestBitwiseParityGptOssVarlen` — [`L938`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L938)
- <a id="TestBitwiseParityGptOssVarlen.__test__"></a>`TestBitwiseParityGptOssVarlen.__test__` — [`L941`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L941)
- <a id="TestBitwiseParityGptOssVarlen.attn_backend"></a>`TestBitwiseParityGptOssVarlen.attn_backend` — [`L943`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L943)
- <a id="TestBitwiseParityGptOssVarlen.config_fn"></a>`TestBitwiseParityGptOssVarlen.config_fn` — [`L942`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L942)
- <a id="TestBitwiseParityGptOssVarlen.sync_weights_from_trainer"></a>`TestBitwiseParityGptOssVarlen.sync_weights_from_trainer` — [`L944`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L944)
- <a id="TestBitwiseParityMoEEP"></a>`TestBitwiseParityMoEEP` — [`L916`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L916)
- <a id="TestBitwiseParityMoEEP.BATCH_SIZE"></a>`TestBitwiseParityMoEEP.BATCH_SIZE` — [`L928`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L928)
- <a id="TestBitwiseParityMoEEP.MAX_GEN_TOKENS"></a>`TestBitwiseParityMoEEP.MAX_GEN_TOKENS` — [`L930`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L930)
- <a id="TestBitwiseParityMoEEP.PROMPT_LENGTH"></a>`TestBitwiseParityMoEEP.PROMPT_LENGTH` — [`L929`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L929)
- <a id="TestBitwiseParityMoEEP.__test__"></a>`TestBitwiseParityMoEEP.__test__` — [`L926`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L926)
- <a id="TestBitwiseParityMoEEP.attn_backend"></a>`TestBitwiseParityMoEEP.attn_backend` — [`L933`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L933)
- <a id="TestBitwiseParityMoEEP.config_fn"></a>`TestBitwiseParityMoEEP.config_fn` — [`L932`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L932)
- <a id="TestBitwiseParityMoEEP.hf_assets_env_var"></a>`TestBitwiseParityMoEEP.hf_assets_env_var` — [`L935`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L935)
- <a id="TestBitwiseParityMoEEP.min_world_size"></a>`TestBitwiseParityMoEEP.min_world_size` — [`L934`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L934)
- <a id="TestBitwiseParityQwen35DebugVarlen"></a>`TestBitwiseParityQwen35DebugVarlen` — [`L868`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L868)
- <a id="TestBitwiseParityQwen35DebugVarlen.BATCH_SIZE"></a>`TestBitwiseParityQwen35DebugVarlen.BATCH_SIZE` — [`L876`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L876)
- <a id="TestBitwiseParityQwen35DebugVarlen.MAX_GEN_TOKENS"></a>`TestBitwiseParityQwen35DebugVarlen.MAX_GEN_TOKENS` — [`L878`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L878)
- <a id="TestBitwiseParityQwen35DebugVarlen.PROMPT_LENGTH"></a>`TestBitwiseParityQwen35DebugVarlen.PROMPT_LENGTH` — [`L877`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L877)
- <a id="TestBitwiseParityQwen35DebugVarlen.__test__"></a>`TestBitwiseParityQwen35DebugVarlen.__test__` — [`L871`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L871)
- <a id="TestBitwiseParityQwen35DebugVarlen.attn_backend"></a>`TestBitwiseParityQwen35DebugVarlen.attn_backend` — [`L873`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L873)
- <a id="TestBitwiseParityQwen35DebugVarlen.config_fn"></a>`TestBitwiseParityQwen35DebugVarlen.config_fn` — [`L872`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L872)
- <a id="TestBitwiseParityQwen35DebugVarlen.min_world_size"></a>`TestBitwiseParityQwen35DebugVarlen.min_world_size` — [`L874`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L874)
- <a id="TestBitwiseParityQwen35DebugVarlen.sync_weights_from_trainer"></a>`TestBitwiseParityQwen35DebugVarlen.sync_weights_from_trainer` — [`L875`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L875)
- <a id="TestBitwiseParityQwen35DebugVarlen.test_vllm_prefill_and_decode_batch_invariance"></a>`TestBitwiseParityQwen35DebugVarlen.test_vllm_prefill_and_decode_batch_invariance` — [`L880`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L880)
- <a id="TestBitwiseParityQwen35Varlen"></a>`TestBitwiseParityQwen35Varlen` — [`L846`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L846)
- <a id="TestBitwiseParityQwen35Varlen.__test__"></a>`TestBitwiseParityQwen35Varlen.__test__` — [`L849`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L849)
- <a id="TestBitwiseParityQwen35Varlen.attn_backend"></a>`TestBitwiseParityQwen35Varlen.attn_backend` — [`L851`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L851)
- <a id="TestBitwiseParityQwen35Varlen.config_fn"></a>`TestBitwiseParityQwen35Varlen.config_fn` — [`L850`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L850)
- <a id="TestBitwiseParityQwen35Varlen.min_world_size"></a>`TestBitwiseParityQwen35Varlen.min_world_size` — [`L852`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L852)
- <a id="TestBitwiseParityVarlen"></a>`TestBitwiseParityVarlen` — [`L830`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L830)
- <a id="TestBitwiseParityVarlen.__test__"></a>`TestBitwiseParityVarlen.__test__` — [`L833`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L833)
- <a id="TestBitwiseParityVarlen.attn_backend"></a>`TestBitwiseParityVarlen.attn_backend` — [`L835`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L835)
- <a id="TestBitwiseParityVarlen.config_fn"></a>`TestBitwiseParityVarlen.config_fn` — [`L834`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L834)
- <a id="_FILLER_TEXT"></a>`_FILLER_TEXT` — [`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L544)
- <a id="_PREFILL_PARAMS"></a>`_PREFILL_PARAMS` — [`L477`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L477)
- <a id="_extract_logprobs_from_prompt"></a>`_extract_logprobs_from_prompt` — [`L459`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L459)
- <a id="_flex_prefill_logprobs"></a>`_flex_prefill_logprobs` — [`L334`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L334)
- <a id="_make_prompt_tokens"></a>`_make_prompt_tokens` — [`L557`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L557)
- <a id="_qwen3_5_debug_bitwise_config"></a>`_qwen3_5_debug_bitwise_config` — [`L855`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L855)
- <a id="_run_engine"></a>`_run_engine` — [`L487`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L487)
- <a id="_set_generator_determinism"></a>`_set_generator_determinism` — [`L188`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L188)
- <a id="_sync_trainer_weights_to_vllm"></a>`_sync_trainer_weights_to_vllm` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L286)
- <a id="_varlen_prefill_logprobs"></a>`_varlen_prefill_logprobs` — [`L398`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L398)
- <a id="build_inference_engine"></a>`build_inference_engine` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L206) — documented in [rl-training](../../../../../concepts/rl-training.md)
- <a id="build_trainer_model"></a>`build_trainer_model` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L102) — documented in [rl-training](../../../../../concepts/rl-training.md)
- <a id="compute_trainer_prefill_logprobs"></a>`compute_trainer_prefill_logprobs` — [`L432`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L432)
- <a id="logger"></a>`logger` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L93)
- <a id="vllm_2nd_pass_prefill"></a>`vllm_2nd_pass_prefill` — [`L528`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L528)
- <a id="vllm_generate"></a>`vllm_generate` — [`L510`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L510)
- <a id="vllm_prefill"></a>`vllm_prefill` — [`L501`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_bitwise_parity.py#L501)
