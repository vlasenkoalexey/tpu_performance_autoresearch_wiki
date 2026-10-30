---
title: 'Module: torchtitan/distributed/tensor_parallel.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/tensor_parallel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.tensor_parallel`/NoParallel#
symbols:
  NoParallel._apply: _apply().
  NoParallel.input_layout: input_layout.
  NoParallel.output_layout: output_layout.
  NoParallel.desired_input_layout: desired_input_layout.
  NoParallel.use_local_output: use_local_output.
  NoParallel._prepare_input_fn: _prepare_input_fn().
  NoParallel._prepare_output_fn: _prepare_output_fn().
  NoParallel: ''
  NoParallel.__init__: __init__().
---
# Module: [`torchtitan/distributed/tensor_parallel.py`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py)

## Classes
### <a id="NoParallel"></a>`NoParallel`
- def: [`torchtitan/distributed/tensor_parallel.py:19`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L19)
- doc: Replicate computation on the TP mesh without sharding.
- signature: `class NoParallel(ParallelStyle):`
- members:
  - <a id="NoParallel.desired_input_layout"></a>`desired_input_layout` — [`L42`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L42)
  - <a id="NoParallel.input_layout"></a>`input_layout` — [`L40`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L40)
  - <a id="NoParallel.output_layout"></a>`output_layout` — [`L41`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L41)
  - <a id="NoParallel.use_local_output"></a>`use_local_output` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L43)
- protocol/private: <a id="NoParallel.__init__"></a>`__init__`[`L32`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L32), <a id="NoParallel._apply"></a>`_apply`[`L80`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L80), <a id="NoParallel._prepare_input_fn"></a>`_prepare_input_fn`[`L46`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L46), <a id="NoParallel._prepare_output_fn"></a>`_prepare_output_fn`[`L69`](../../../../../../raw/code/torchtitan/torchtitan/distributed/tensor_parallel.py#L69)

