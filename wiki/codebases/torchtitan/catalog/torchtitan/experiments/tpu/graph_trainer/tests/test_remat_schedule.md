---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_remat_schedule`/
symbols:
  TestTpuRematSchedule.test_traced_two_layer_schedule: TestTpuRematSchedule#test_traced_two_layer_schedule().
  TestTpuFsdpRematSchedule.test_rs_deadline_reuses_all_gather_barriers: TestTpuFsdpRematSchedule#test_rs_deadline_reuses_all_gather_barriers().
  _trace_simple_fsdp_remat_graph: _trace_simple_fsdp_remat_graph().
  TestTpuFsdpRematSchedule.test_all_gather_barrier_uses_configured_layer_distance: TestTpuFsdpRematSchedule#test_all_gather_barrier_uses_configured_layer_distance().
  TestTpuFsdpRematSchedule.test_all_gather_barrier_requires_positive_prefetch_distance: TestTpuFsdpRematSchedule#test_all_gather_barrier_requires_positive_prefetch_distance().
  _describe_barriers: _describe_barriers().
  _Block.moe: _Block#moe.
  _ToyModel.forward: _ToyModel#forward().
  TestTpuFsdpRematSchedule.test_all_gather_barrier_ignores_activation_collectives: TestTpuFsdpRematSchedule#test_all_gather_barrier_ignores_activation_collectives().
  _Block.forward: _Block#forward().
  TestScanRecomputePolicy.test_a_scan_over_the_layers_is_never_recomputed: TestScanRecomputePolicy#test_a_scan_over_the_layers_is_never_recomputed().
  _Block.attention: _Block#attention.
  _ToyModel.layers: _ToyModel#layers.
  _ToyModel.norm: _ToyModel#norm.
  _trace_simple_fsdp_remat_graph.step: _trace_simple_fsdp_remat_graph().step().
  _nearest_parameter_fqns: _nearest_parameter_fqns().
  TestTpuRematSchedule.step: TestTpuRematSchedule#step().
  _set_tensor_meta: _set_tensor_meta().
  _Projection.forward: _Projection#forward().
  _Projection: _Projection#
  _ToyModel: _ToyModel#
  _Projection.weight: _Projection#weight.
  _Block: _Block#
  _Epilogue: _Epilogue#
  _ToyModel.masked: _ToyModel#masked.
  _Projection.__init__: _Projection#__init__().
  _Block.__init__: _Block#__init__().
  _Epilogue.forward: _Epilogue#forward().
  _ToyModel.__init__: _ToyModel#__init__().
  TestTpuFsdpRematSchedule: TestTpuFsdpRematSchedule#
  TestTpuRematSchedule: TestTpuRematSchedule#
  TestScanRecomputePolicy: TestScanRecomputePolicy#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py)

> **Collapsed catalog** (32 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestScanRecomputePolicy"></a>`TestScanRecomputePolicy` — [`L541`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L541)
- <a id="TestScanRecomputePolicy.test_a_scan_over_the_layers_is_never_recomputed"></a>`TestScanRecomputePolicy.test_a_scan_over_the_layers_is_never_recomputed` — [`L543`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L543)
- <a id="TestTpuFsdpRematSchedule"></a>`TestTpuFsdpRematSchedule` — [`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L185)
- <a id="TestTpuFsdpRematSchedule.test_all_gather_barrier_ignores_activation_collectives"></a>`TestTpuFsdpRematSchedule.test_all_gather_barrier_ignores_activation_collectives` — [`L260`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L260)
- <a id="TestTpuFsdpRematSchedule.test_all_gather_barrier_requires_positive_prefetch_distance"></a>`TestTpuFsdpRematSchedule.test_all_gather_barrier_requires_positive_prefetch_distance` — [`L249`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L249)
- <a id="TestTpuFsdpRematSchedule.test_all_gather_barrier_uses_configured_layer_distance"></a>`TestTpuFsdpRematSchedule.test_all_gather_barrier_uses_configured_layer_distance` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L186)
- <a id="TestTpuFsdpRematSchedule.test_rs_deadline_reuses_all_gather_barriers"></a>`TestTpuFsdpRematSchedule.test_rs_deadline_reuses_all_gather_barriers` — [`L286`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L286)
- <a id="TestTpuRematSchedule"></a>`TestTpuRematSchedule` — [`L430`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L430)
- <a id="TestTpuRematSchedule.step"></a>`TestTpuRematSchedule.step` — [`L445`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L445)
- <a id="TestTpuRematSchedule.test_traced_two_layer_schedule"></a>`TestTpuRematSchedule.test_traced_two_layer_schedule` — [`L431`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L431) — documented in [tpu-graph-trainer](../../../../../../concepts/tpu-graph-trainer.md)
- <a id="_Block"></a>`_Block` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L91)
- <a id="_Block.__init__"></a>`_Block.__init__` — [`L92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L92)
- <a id="_Block.attention"></a>`_Block.attention` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L101)
- <a id="_Block.forward"></a>`_Block.forward` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L103)
- <a id="_Block.moe"></a>`_Block.moe` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L98)
- <a id="_Epilogue"></a>`_Epilogue` — [`L110`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L110)
- <a id="_Epilogue.forward"></a>`_Epilogue.forward` — [`L111`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L111)
- <a id="_Projection"></a>`_Projection` — [`L79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L79)
- <a id="_Projection.__init__"></a>`_Projection.__init__` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L80)
- <a id="_Projection.forward"></a>`_Projection.forward` — [`L84`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L84)
- <a id="_Projection.weight"></a>`_Projection.weight` — [`L82`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L82)
- <a id="_ToyModel"></a>`_ToyModel` — [`L115`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L115)
- <a id="_ToyModel.__init__"></a>`_ToyModel.__init__` — [`L116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L116)
- <a id="_ToyModel.forward"></a>`_ToyModel.forward` — [`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L124)
- <a id="_ToyModel.layers"></a>`_ToyModel.layers` — [`L120`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L120)
- <a id="_ToyModel.masked"></a>`_ToyModel.masked` — [`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L122)
- <a id="_ToyModel.norm"></a>`_ToyModel.norm` — [`L121`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L121)
- <a id="_describe_barriers"></a>`_describe_barriers` — [`L387`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L387)
- <a id="_nearest_parameter_fqns"></a>`_nearest_parameter_fqns` — [`L364`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L364)
- <a id="_set_tensor_meta"></a>`_set_tensor_meta` — [`L62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L62)
- <a id="_trace_simple_fsdp_remat_graph"></a>`_trace_simple_fsdp_remat_graph` — [`L133`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L133)
- <a id="_trace_simple_fsdp_remat_graph.step"></a>`_trace_simple_fsdp_remat_graph.step` — [`L152`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_remat_schedule.py#L152)
