---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_chunked_loss`/
symbols:
  TestChunkedLossWrapperWithParamGrads.test_multi_output_matches_base_wrapper: TestChunkedLossWrapperWithParamGrads#test_multi_output_matches_base_wrapper().
  _make_model_and_loss: _make_model_and_loss().
  _FakeDecoder.output: _FakeDecoder#output.
  TestChunkedLossWrapperWithParamGrads.test_config_builds_param_grads_loss: TestChunkedLossWrapperWithParamGrads#test_config_builds_param_grads_loss().
  TestChunkedLossWrapperWithParamGrads.test_bitwise_equal_with_chunked_loss: TestChunkedLossWrapperWithParamGrads#test_bitwise_equal_with_chunked_loss().
  _WeightedTwoOutputLoss.__init__: _WeightedTwoOutputLoss#__init__().
  _WeightedTwoOutputLoss.Config: _WeightedTwoOutputLoss#Config#
  _WeightedTwoOutputLoss.__call__: _WeightedTwoOutputLoss#__call__().
  TestChunkedLossWrapperWithParamGrads.test_does_not_touch_dot_grad: TestChunkedLossWrapperWithParamGrads#test_does_not_touch_dot_grad().
  _chunked_loss_and_grads: _chunked_loss_and_grads().
  _WeightedTwoOutputLoss: _WeightedTwoOutputLoss#
  _WeightedTwoOutputLoss.auxiliary_weight: _WeightedTwoOutputLoss#auxiliary_weight.
  _FakeDecoder: _FakeDecoder#
  _FakeDecoder.forward: _FakeDecoder#forward().
  _WeightedTwoOutputLoss.Config.auxiliary_weight: _WeightedTwoOutputLoss#Config#auxiliary_weight.
  _FakeDecoder.__init__: _FakeDecoder#__init__().
  _FakeDecoder.layers: _FakeDecoder#layers.
  _FakeDecoder.tok_embeddings: _FakeDecoder#tok_embeddings.
  _FakeDecoder.norm: _FakeDecoder#norm.
  TestChunkedLossWrapperWithParamGrads: TestChunkedLossWrapperWithParamGrads#
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestChunkedLossWrapperWithParamGrads"></a>`TestChunkedLossWrapperWithParamGrads` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L90)
- <a id="TestChunkedLossWrapperWithParamGrads.test_bitwise_equal_with_chunked_loss"></a>`TestChunkedLossWrapperWithParamGrads.test_bitwise_equal_with_chunked_loss` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L96)
- <a id="TestChunkedLossWrapperWithParamGrads.test_config_builds_param_grads_loss"></a>`TestChunkedLossWrapperWithParamGrads.test_config_builds_param_grads_loss` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L91)
- <a id="TestChunkedLossWrapperWithParamGrads.test_does_not_touch_dot_grad"></a>`TestChunkedLossWrapperWithParamGrads.test_does_not_touch_dot_grad` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L122)
- <a id="TestChunkedLossWrapperWithParamGrads.test_multi_output_matches_base_wrapper"></a>`TestChunkedLossWrapperWithParamGrads.test_multi_output_matches_base_wrapper` — [`L135`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L135)
- <a id="_FakeDecoder"></a>`_FakeDecoder` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L25)
- <a id="_FakeDecoder.__init__"></a>`_FakeDecoder.__init__` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L28)
- <a id="_FakeDecoder.forward"></a>`_FakeDecoder.forward` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L35)
- <a id="_FakeDecoder.layers"></a>`_FakeDecoder.layers` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L31)
- <a id="_FakeDecoder.norm"></a>`_FakeDecoder.norm` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L33)
- <a id="_FakeDecoder.output"></a>`_FakeDecoder.output` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L30)
- <a id="_FakeDecoder.tok_embeddings"></a>`_FakeDecoder.tok_embeddings` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L32)
- <a id="_WeightedTwoOutputLoss"></a>`_WeightedTwoOutputLoss` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L41)
- <a id="_WeightedTwoOutputLoss.Config"></a>`_WeightedTwoOutputLoss.Config` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L43)
- <a id="_WeightedTwoOutputLoss.Config.auxiliary_weight"></a>`_WeightedTwoOutputLoss.Config.auxiliary_weight` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L44)
- <a id="_WeightedTwoOutputLoss.__call__"></a>`_WeightedTwoOutputLoss.__call__` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L51)
- <a id="_WeightedTwoOutputLoss.__init__"></a>`_WeightedTwoOutputLoss.__init__` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L46)
- <a id="_WeightedTwoOutputLoss.auxiliary_weight"></a>`_WeightedTwoOutputLoss.auxiliary_weight` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L49)
- <a id="_chunked_loss_and_grads"></a>`_chunked_loss_and_grads` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L78)
- <a id="_make_model_and_loss"></a>`_make_model_and_loss` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_chunked_loss.py#L68)
