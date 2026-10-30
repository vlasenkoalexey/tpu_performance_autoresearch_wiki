---
title: 'Module: torchtitan/experiments/tpu/tests/test_token_dispatcher.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_token_dispatcher.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_token_dispatcher`/
symbols:
  test_scale_before_down_proj_matches_scaling_the_output: test_scale_before_down_proj_matches_scaling_the_output().
  test_scale_before_down_proj_matches_scaling_the_output.run: test_scale_before_down_proj_matches_scaling_the_output().run().
  test_converter_preserves_fields_and_is_idempotent: test_converter_preserves_fields_and_is_idempotent().
  test_local_combine_matches_standard_dispatcher: test_local_combine_matches_standard_dispatcher().
  test_ep_combine_delegates_to_standard_dispatcher: test_ep_combine_delegates_to_standard_dispatcher().
  test_local_reorder_matches_reference_forward_and_backward: test_local_reorder_matches_reference_forward_and_backward().
  test_local_reorder_preserves_unused_gradients: test_local_reorder_preserves_unused_gradients().
  test_converter_preserves_fields_and_is_idempotent.RootConfig.__init__: test_converter_preserves_fields_and_is_idempotent().RootConfig#__init__().
  RootConfig.dispatcher: RootConfig#dispatcher.
  test_scale_route_weights_traces_forward_and_backward: test_scale_route_weights_traces_forward_and_backward().
  _SwiGLUExperts.forward: _SwiGLUExperts#forward().
  test_grouped_reduce_saves_only_row_index: test_grouped_reduce_saves_only_row_index().
  test_scale_route_weights_traces_forward_and_backward.step: test_scale_route_weights_traces_forward_and_backward().step().
  test_scale_route_weights_matches_native_autograd: test_scale_route_weights_matches_native_autograd().
  test_scale_route_weights_validates_shapes: test_scale_route_weights_validates_shapes().
  test_scale_route_weights_retains_native_dtype_fallback: test_scale_route_weights_retains_native_dtype_fallback().
  test_converter_preserves_fields_and_is_idempotent.RootConfig.traverse: test_converter_preserves_fields_and_is_idempotent().RootConfig#traverse().
  test_grouped_reduce_saves_only_row_index.pack: test_grouped_reduce_saves_only_row_index().pack().
  test_converter_preserves_fields_and_is_idempotent.RootConfig: test_converter_preserves_fields_and_is_idempotent().RootConfig#
  _SwiGLUExperts: _SwiGLUExperts#
  _SwiGLUExperts.w1_EDF: _SwiGLUExperts#w1_EDF.
  _SwiGLUExperts.w3_EDF: _SwiGLUExperts#w3_EDF.
  _SwiGLUExperts.w2_EFD: _SwiGLUExperts#w2_EFD.
  _SwiGLUExperts.__init__: _SwiGLUExperts#__init__().
---
# Module: [`torchtitan/experiments/tpu/tests/test_token_dispatcher.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py)

> **Collapsed catalog** (24 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="RootConfig.dispatcher"></a>`RootConfig.dispatcher` — [`L284`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L284)
- <a id="_SwiGLUExperts"></a>`_SwiGLUExperts` — [`L307`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L307)
- <a id="_SwiGLUExperts.__init__"></a>`_SwiGLUExperts.__init__` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L310)
- <a id="_SwiGLUExperts.forward"></a>`_SwiGLUExperts.forward` — [`L314`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L314)
- <a id="_SwiGLUExperts.w1_EDF"></a>`_SwiGLUExperts.w1_EDF` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L312)
- <a id="_SwiGLUExperts.w2_EFD"></a>`_SwiGLUExperts.w2_EFD` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L312)
- <a id="_SwiGLUExperts.w3_EDF"></a>`_SwiGLUExperts.w3_EDF` — [`L312`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L312)
- <a id="test_converter_preserves_fields_and_is_idempotent"></a>`test_converter_preserves_fields_and_is_idempotent` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L281) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="test_converter_preserves_fields_and_is_idempotent.RootConfig"></a>`test_converter_preserves_fields_and_is_idempotent.RootConfig` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L282)
- <a id="test_converter_preserves_fields_and_is_idempotent.RootConfig.__init__"></a>`test_converter_preserves_fields_and_is_idempotent.RootConfig.__init__` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L283)
- <a id="test_converter_preserves_fields_and_is_idempotent.RootConfig.traverse"></a>`test_converter_preserves_fields_and_is_idempotent.RootConfig.traverse` — [`L288`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L288)
- <a id="test_ep_combine_delegates_to_standard_dispatcher"></a>`test_ep_combine_delegates_to_standard_dispatcher` — [`L241`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L241)
- <a id="test_grouped_reduce_saves_only_row_index"></a>`test_grouped_reduce_saves_only_row_index` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L259)
- <a id="test_grouped_reduce_saves_only_row_index.pack"></a>`test_grouped_reduce_saves_only_row_index.pack` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L265)
- <a id="test_local_combine_matches_standard_dispatcher"></a>`test_local_combine_matches_standard_dispatcher` — [`L195`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L195)
- <a id="test_local_reorder_matches_reference_forward_and_backward"></a>`test_local_reorder_matches_reference_forward_and_backward` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L113)
- <a id="test_local_reorder_preserves_unused_gradients"></a>`test_local_reorder_preserves_unused_gradients` — [`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L155)
- <a id="test_scale_before_down_proj_matches_scaling_the_output"></a>`test_scale_before_down_proj_matches_scaling_the_output` — [`L326`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L326) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="test_scale_before_down_proj_matches_scaling_the_output.run"></a>`test_scale_before_down_proj_matches_scaling_the_output.run` — [`L338`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L338) — documented in [tpu-moe-dispatch-and-grouped-experts](../../../../../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- <a id="test_scale_route_weights_matches_native_autograd"></a>`test_scale_route_weights_matches_native_autograd` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L21)
- <a id="test_scale_route_weights_retains_native_dtype_fallback"></a>`test_scale_route_weights_retains_native_dtype_fallback` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L73)
- <a id="test_scale_route_weights_traces_forward_and_backward"></a>`test_scale_route_weights_traces_forward_and_backward` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L90)
- <a id="test_scale_route_weights_traces_forward_and_backward.step"></a>`test_scale_route_weights_traces_forward_and_backward.step` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L91)
- <a id="test_scale_route_weights_validates_shapes"></a>`test_scale_route_weights_validates_shapes` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_token_dispatcher.py#L66)
