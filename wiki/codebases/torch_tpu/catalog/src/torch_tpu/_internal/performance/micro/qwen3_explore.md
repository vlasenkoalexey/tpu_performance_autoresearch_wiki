---
title: 'Module: src/torch_tpu/_internal/performance/micro/qwen3_explore.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/performance/micro/qwen3_explore.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.performance.micro.qwen3_explore`/
symbols:
  main: main().
  FeedForward.forward: FeedForward#forward().
  configs: configs.
  _MODEL: _MODEL.
  _ITERS: _ITERS.
  FeedForward: FeedForward#
  FeedForward.fc1: FeedForward#fc1.
  FeedForward.fc2: FeedForward#fc2.
  FeedForward.fc3: FeedForward#fc3.
  FeedForward.__init__: FeedForward#__init__().
---
# Module: [`src/torch_tpu/_internal/performance/micro/qwen3_explore.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py)

## Classes
### <a id="FeedForward"></a>`FeedForward`
- def: [`src/torch_tpu/_internal/performance/micro/qwen3_explore.py:81`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L81)
- doc: Traditional feed forward layer with 2 FC's, a silu, and a final FC.
- signature: `class FeedForward(nn.Module):`
- members:
  - <a id="FeedForward.forward"></a>`forward(self, x)` — [`L96`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L96)
  - <a id="FeedForward.fc1"></a>`fc1` — [`L86`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L86)
  - <a id="FeedForward.fc2"></a>`fc2` — [`L89`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L89)
  - <a id="FeedForward.fc3"></a>`fc3` — [`L92`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L92)
- protocol/private: <a id="FeedForward.__init__"></a>`__init__`[`L84`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L84)
- used by: [`main`](qwen3_explore.md#main)

## Functions
- <a id="main"></a>`main(argv)` — [`L103`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L103)

## Module values
- <a id="_ITERS"></a>`_ITERS` — [`L76`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L76)
- <a id="_MODEL"></a>`_MODEL` — [`L71`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L71)
- <a id="configs"></a>`configs` — [`L33`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/performance/micro/qwen3_explore.py#L33)

