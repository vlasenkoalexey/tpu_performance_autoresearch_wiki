---
title: 'Module: torchtitan/experiments/tpu/examples/dilated_conv.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/dilated_conv.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.dilated_conv`/DilatedGroupCausalConv#
symbols:
  DilatedGroupCausalConv.forward: forward().
  DilatedGroupCausalConv.max_pad: max_pad.
  DilatedGroupCausalConv.max_dilation: max_dilation.
  DilatedGroupCausalConv.convs: convs.
  DilatedGroupCausalConv: ''
  DilatedGroupCausalConv.gs: gs.
  DilatedGroupCausalConv.ng: ng.
  DilatedGroupCausalConv.K: K.
  DilatedGroupCausalConv.__init__: __init__().
---
# Module: [`torchtitan/experiments/tpu/examples/dilated_conv.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py)

## Classes
### <a id="DilatedGroupCausalConv"></a>`DilatedGroupCausalConv`
- def: [`torchtitan/experiments/tpu/examples/dilated_conv.py:5`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L5)
- doc: TorchTPU / XLA Optimized Dilated Grouped Causal Conv.
- signature: `class DilatedGroupCausalConv(nn.Module):`
- members:
  - <a id="DilatedGroupCausalConv.forward"></a>`forward(self, x)` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L26)
  - <a id="DilatedGroupCausalConv.K"></a>`K` — [`L14`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L14)
  - <a id="DilatedGroupCausalConv.convs"></a>`convs` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L20)
  - <a id="DilatedGroupCausalConv.gs"></a>`gs` — [`L14`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L14)
  - <a id="DilatedGroupCausalConv.max_dilation"></a>`max_dilation` — [`L17`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L17)
  - <a id="DilatedGroupCausalConv.max_pad"></a>`max_pad` — [`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L18)
  - <a id="DilatedGroupCausalConv.ng"></a>`ng` — [`L14`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L14)
- protocol/private: <a id="DilatedGroupCausalConv.__init__"></a>`__init__`[`L11`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/dilated_conv.py#L11)
- used by: (1 test-only callers)

