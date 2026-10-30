---
title: 'Module: torchtitan/experiments/tpu/tests/test_layer_loop.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_layer_loop.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_layer_loop`/
symbols:
  ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert: ConfigRewriteTest#test_rewrite_rejects_what_it_cannot_convert().
  ForwardParityTest.test_gradients_match_upstream: ForwardParityTest#test_gradients_match_upstream().
  ForwardStructureTest.test_forward_is_upstream_forward_modulo_the_loop: ForwardStructureTest#test_forward_is_upstream_forward_modulo_the_loop().
  _stock_config: _stock_config().
  ForwardParityTest.test_forward_matches_upstream: ForwardParityTest#test_forward_matches_upstream().
  ConfigRewriteTest.test_rewrite_swaps_the_model_class_and_keeps_every_field: ConfigRewriteTest#test_rewrite_swaps_the_model_class_and_keeps_every_field().
  ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement: ConfigRewriteTest#test_rewrite_keeps_an_earlier_root_config_replacement().
  _convert: _convert().
  _tokens: _tokens().
  CONTAINERS: CONTAINERS.
  _tpu_model: _tpu_model().
  TOKENS: TOKENS.
  ForwardParityTest.test_layerless_pipeline_stage_is_a_passthrough: ForwardParityTest#test_layerless_pipeline_stage_is_a_passthrough().
  ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig: ConfigRewriteTest#test_rewrite_keeps_an_earlier_root_config_replacement().CustomFlopsConfig#
  ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.Config: ConfigRewriteTest#test_rewrite_rejects_what_it_cannot_convert().ForwardOwningModel#Config#
  ConfigRewriteTest.test_state_dict_keys_are_unchanged: ConfigRewriteTest#test_state_dict_keys_are_unchanged().
  _ScanLikeLoop: _ScanLikeLoop#
  _is_tpu_dispatch: _is_tpu_dispatch().
  ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel: ConfigRewriteTest#test_rewrite_rejects_what_it_cannot_convert().ForwardOwningModel#
  _ScanLikeLoop.forward: _ScanLikeLoop#forward().
  _recast: _recast().
  ForwardParityTest.grads: ForwardParityTest#grads().
  _is_upstream_loop: _is_upstream_loop().
  _blank_the_loop: _blank_the_loop().
  BATCH: BATCH.
  SEQ: SEQ.
  _ScanLikeLoop.calls: _ScanLikeLoop#calls.
  _ScanLikeLoop.__init__: _ScanLikeLoop#__init__().
  ForwardParityTest: ForwardParityTest#
  ForwardStructureTest: ForwardStructureTest#
  ConfigRewriteTest: ConfigRewriteTest#
  ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig.get_nparams_and_flops: ConfigRewriteTest#test_rewrite_keeps_an_earlier_root_config_replacement().CustomFlopsConfig#get_nparams_and_flops().
  ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.forward: ConfigRewriteTest#test_rewrite_rejects_what_it_cannot_convert().ForwardOwningModel#forward().
---
# Module: [`torchtitan/experiments/tpu/tests/test_layer_loop.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py)

> **Collapsed catalog** (33 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BATCH"></a>`BATCH` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L35)
- <a id="CONTAINERS"></a>`CONTAINERS` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L107)
- <a id="ConfigRewriteTest"></a>`ConfigRewriteTest` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L228)
- <a id="ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement"></a>`ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L248)
- <a id="ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig"></a>`ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L252)
- <a id="ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig.get_nparams_and_flops"></a>`ConfigRewriteTest.test_rewrite_keeps_an_earlier_root_config_replacement.CustomFlopsConfig.get_nparams_and_flops` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L254)
- <a id="ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert"></a>`ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L271)
- <a id="ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel"></a>`ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L276)
- <a id="ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.Config"></a>`ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.Config` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L279)
- <a id="ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.forward"></a>`ConfigRewriteTest.test_rewrite_rejects_what_it_cannot_convert.ForwardOwningModel.forward` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L282)
- <a id="ConfigRewriteTest.test_rewrite_swaps_the_model_class_and_keeps_every_field"></a>`ConfigRewriteTest.test_rewrite_swaps_the_model_class_and_keeps_every_field` — [`L230`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L230)
- <a id="ConfigRewriteTest.test_state_dict_keys_are_unchanged"></a>`ConfigRewriteTest.test_state_dict_keys_are_unchanged` — [`L263`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L263)
- <a id="ForwardParityTest"></a>`ForwardParityTest` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L115)
- <a id="ForwardParityTest.grads"></a>`ForwardParityTest.grads` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L153)
- <a id="ForwardParityTest.test_forward_matches_upstream"></a>`ForwardParityTest.test_forward_matches_upstream` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L120)
- <a id="ForwardParityTest.test_gradients_match_upstream"></a>`ForwardParityTest.test_gradients_match_upstream` — [`L148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L148)
- <a id="ForwardParityTest.test_layerless_pipeline_stage_is_a_passthrough"></a>`ForwardParityTest.test_layerless_pipeline_stage_is_a_passthrough` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L136)
- <a id="ForwardStructureTest"></a>`ForwardStructureTest` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L208)
- <a id="ForwardStructureTest.test_forward_is_upstream_forward_modulo_the_loop"></a>`ForwardStructureTest.test_forward_is_upstream_forward_modulo_the_loop` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L210)
- <a id="SEQ"></a>`SEQ` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L35)
- <a id="TOKENS"></a>`TOKENS` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L37)
- <a id="_ScanLikeLoop"></a>`_ScanLikeLoop` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L93)
- <a id="_ScanLikeLoop.__init__"></a>`_ScanLikeLoop.__init__` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L96)
- <a id="_ScanLikeLoop.calls"></a>`_ScanLikeLoop.calls` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L98)
- <a id="_ScanLikeLoop.forward"></a>`_ScanLikeLoop.forward` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L100)
- <a id="_blank_the_loop"></a>`_blank_the_loop` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L184)
- <a id="_convert"></a>`_convert` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L62)
- <a id="_is_tpu_dispatch"></a>`_is_tpu_dispatch` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L174)
- <a id="_is_upstream_loop"></a>`_is_upstream_loop` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L164)
- <a id="_recast"></a>`_recast` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L67)
- <a id="_stock_config"></a>`_stock_config` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L40)
- <a id="_tokens"></a>`_tokens` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L82)
- <a id="_tpu_model"></a>`_tpu_model` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_layer_loop.py#L74)
