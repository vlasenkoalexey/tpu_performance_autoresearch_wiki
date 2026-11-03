---
title: 'Module: src/vllm_torchtpu/layers/adapter/linear.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/linear.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.linear`/TpuRowParallelLinear#
symbols:
  TpuRowParallelLinear: ''
  TpuRowParallelLinear.forward: forward().
---
# Module: [`src/vllm_torchtpu/layers/adapter/linear.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear.py)

## Classes
### <a id="TpuRowParallelLinear"></a>`TpuRowParallelLinear`
- def: [`src/vllm_torchtpu/layers/adapter/linear.py:25`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear.py#L25)
- doc: RowParallelLinear that adds the bias after the TP all-reduce.
- signature: `class TpuRowParallelLinear(RowParallelLinear):`
- members:
  - <a id="TpuRowParallelLinear.forward"></a>`forward(self, input_)` — [`L38`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/linear.py#L38)

