---
title: 'Module: torchtitan/experiments/graph_trainer/chunked_loss.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/chunked_loss.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.chunked_loss`/
symbols:
  ChunkedLossWrapperWithParamGrads: ChunkedLossWrapperWithParamGrads#
  ChunkedLossWrapperWithParamGrads.Config: ChunkedLossWrapperWithParamGrads#Config#
  ChunkedLossWrapperWithParamGrads._gradient_backprop: ChunkedLossWrapperWithParamGrads#_gradient_backprop().
  _ChunkedLossWrapperWithParamGrads: _ChunkedLossWrapperWithParamGrads#
  _ChunkedLossWrapperWithParamGrads.forward: _ChunkedLossWrapperWithParamGrads#forward().
  _ChunkedLossWrapperWithParamGrads.backward: _ChunkedLossWrapperWithParamGrads#backward().
---
# Module: [`torchtitan/experiments/graph_trainer/chunked_loss.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py)

## Classes
### <a id="ChunkedLossWrapperWithParamGrads"></a>`ChunkedLossWrapperWithParamGrads`  ·  implements/extends ChunkedLossWrapper
- def: [`torchtitan/experiments/graph_trainer/chunked_loss.py:15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L15) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: ChunkedLossWrapper variant that exposes sharded lm_head param grads as
- signature: `class ChunkedLossWrapperWithParamGrads(ChunkedLossWrapper):`
- protocol/private: <a id="ChunkedLossWrapperWithParamGrads._gradient_backprop"></a>`_gradient_backprop`[`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L31)
- uses (calls/refs, reference-scoped): [`ChunkedLossWrapper`](../../components/loss.md#ChunkedLossWrapper), [`lm_head`](../../components/loss.md#ChunkedLossWrapper.lm_head), [`_ChunkedLossWrapperWithParamGrads`](chunked_loss.md#_ChunkedLossWrapperWithParamGrads)
- used by: [`ChunkedLossWrapper`](../../components/loss.md#ChunkedLossWrapper), [`to_graph_trainer_config`](configs.md#to_graph_trainer_config), [`_gradient_backprop`](../../components/loss.md#ChunkedLossWrapper._gradient_backprop)  (7 test-only)

### <a id="ChunkedLossWrapperWithParamGrads.Config"></a>`ChunkedLossWrapperWithParamGrads.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/graph_trainer/chunked_loss.py:28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L28)
- signature: `class Config(ChunkedLossWrapper.Config):`
- uses (calls/refs, reference-scoped): [`ChunkedLossWrapper`](../../components/loss.md#ChunkedLossWrapper), [`Config`](../../components/loss.md#ChunkedLossWrapper.Config)
- used by: [`to_graph_trainer_config`](configs.md#to_graph_trainer_config)  (6 test-only)

### <a id="_ChunkedLossWrapperWithParamGrads"></a>`_ChunkedLossWrapperWithParamGrads`
- def: [`torchtitan/experiments/graph_trainer/chunked_loss.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L53)
- members:
  - <a id="_ChunkedLossWrapperWithParamGrads.backward"></a>`backward(ctx, grad_output: torch.Tensor)` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L110)
  - <a id="_ChunkedLossWrapperWithParamGrads.forward"></a>`forward(ctx, num_predictions: int, *args: Any)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/chunked_loss.py#L74)
- used by: [`_gradient_backprop`](chunked_loss.md#ChunkedLossWrapperWithParamGrads._gradient_backprop)

