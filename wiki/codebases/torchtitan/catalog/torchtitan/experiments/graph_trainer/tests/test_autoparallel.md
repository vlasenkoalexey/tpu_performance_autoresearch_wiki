---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_autoparallel.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_autoparallel.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_autoparallel`/
symbols:
  test_model_autoparallel_uses_fx_module_path_and_resolved_policy: test_model_autoparallel_uses_fx_module_path_and_resolved_policy().
  test_autoparallel_graph_pass_selection_uses_regular_memory_policy: test_autoparallel_graph_pass_selection_uses_regular_memory_policy().
  _training_config: _training_config().
  test_autoparallel_config_validation: test_autoparallel_config_validation().
  test_autoparallel_integration_matrix: test_autoparallel_integration_matrix().
  _FakeAutoParallelGraph.used_fx_path: _FakeAutoParallelGraph#used_fx_path.
  _FakeParallelDims.get_optional_mesh: _FakeParallelDims#get_optional_mesh().
  _FakeAutoParallelGraph: _FakeAutoParallelGraph#
  _FakeMesh: _FakeMesh#
  _FakeAutoParallelGraph.instances: _FakeAutoParallelGraph#instances.
  _FakeMesh.ndim: _FakeMesh#ndim.
  _FakeMesh.size: _FakeMesh#size().
  _FakeParallelDims.__init__: _FakeParallelDims#__init__().
  _FakeParallelDims.get_mesh: _FakeParallelDims#get_mesh().
  _FakeAutoParallelGraph.apply_placement_for_fx_module: _FakeAutoParallelGraph#apply_placement_for_fx_module().
  _FakeParallelDims: _FakeParallelDims#
  _FakeMesh.mesh_dim_names: _FakeMesh#mesh_dim_names.
  _FakeMesh._size: _FakeMesh#_size.
  _FakeParallelDims.tp_enabled: _FakeParallelDims#tp_enabled.
  _FakeParallelDims.sparse: _FakeParallelDims#sparse.
  test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model: test_model_autoparallel_uses_fx_module_path_and_resolved_policy().FakeDeepSeekV3Model#
  _FakeMesh.__init__: _FakeMesh#__init__().
  _FakeParallelDims.dp_replicate_enabled: _FakeParallelDims#dp_replicate_enabled.
  _FakeParallelDims.cp_enabled: _FakeParallelDims#cp_enabled.
  _FakeParallelDims.pp_enabled: _FakeParallelDims#pp_enabled.
  _FakeParallelDims.dp_replicate: _FakeParallelDims#dp_replicate.
  _FakeParallelDims.dp_shard: _FakeParallelDims#dp_shard.
  _FakeAutoParallelGraph.__init__: _FakeAutoParallelGraph#__init__().
  _FakeAutoParallelGraph.model: _FakeAutoParallelGraph#model.
  _FakeAutoParallelGraph.kwargs: _FakeAutoParallelGraph#kwargs.
  _FakeAutoParallelGraph.__enter__: _FakeAutoParallelGraph#__enter__().
  _FakeAutoParallelGraph.__exit__: _FakeAutoParallelGraph#__exit__().
  _FakeAutoParallelGraph.add_parameter_memory_constraint: _FakeAutoParallelGraph#add_parameter_memory_constraint().
  _FakeAutoParallelGraph.add_input_constraints: _FakeAutoParallelGraph#add_input_constraints().
  _FakeAutoParallelGraph.add_output_constraints: _FakeAutoParallelGraph#add_output_constraints().
  _FakeAutoParallelGraph.optimize_placement: _FakeAutoParallelGraph#optimize_placement().
  _FakeAutoParallelGraph.apply_kwargs: _FakeAutoParallelGraph#apply_kwargs.
  test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model.__init__: test_model_autoparallel_uses_fx_module_path_and_resolved_policy().FakeDeepSeekV3Model#__init__().
  FakeDeepSeekV3Model.model_args: FakeDeepSeekV3Model#model_args.
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_autoparallel.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py)

> **Collapsed catalog** (39 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="FakeDeepSeekV3Model.model_args"></a>`FakeDeepSeekV3Model.model_args` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L181)
- <a id="_FakeAutoParallelGraph"></a>`_FakeAutoParallelGraph` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L53)
- <a id="_FakeAutoParallelGraph.__enter__"></a>`_FakeAutoParallelGraph.__enter__` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L62)
- <a id="_FakeAutoParallelGraph.__exit__"></a>`_FakeAutoParallelGraph.__exit__` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L65)
- <a id="_FakeAutoParallelGraph.__init__"></a>`_FakeAutoParallelGraph.__init__` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L56)
- <a id="_FakeAutoParallelGraph.add_input_constraints"></a>`_FakeAutoParallelGraph.add_input_constraints` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L71)
- <a id="_FakeAutoParallelGraph.add_output_constraints"></a>`_FakeAutoParallelGraph.add_output_constraints` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L74)
- <a id="_FakeAutoParallelGraph.add_parameter_memory_constraint"></a>`_FakeAutoParallelGraph.add_parameter_memory_constraint` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L68)
- <a id="_FakeAutoParallelGraph.apply_kwargs"></a>`_FakeAutoParallelGraph.apply_kwargs` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L82)
- <a id="_FakeAutoParallelGraph.apply_placement_for_fx_module"></a>`_FakeAutoParallelGraph.apply_placement_for_fx_module` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L80)
- <a id="_FakeAutoParallelGraph.instances"></a>`_FakeAutoParallelGraph.instances` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L54)
- <a id="_FakeAutoParallelGraph.kwargs"></a>`_FakeAutoParallelGraph.kwargs` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L58)
- <a id="_FakeAutoParallelGraph.model"></a>`_FakeAutoParallelGraph.model` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L57)
- <a id="_FakeAutoParallelGraph.optimize_placement"></a>`_FakeAutoParallelGraph.optimize_placement` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L77)
- <a id="_FakeAutoParallelGraph.used_fx_path"></a>`_FakeAutoParallelGraph.used_fx_path` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L59)
- <a id="_FakeMesh"></a>`_FakeMesh` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L21)
- <a id="_FakeMesh.__init__"></a>`_FakeMesh.__init__` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L22)
- <a id="_FakeMesh._size"></a>`_FakeMesh._size` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L25)
- <a id="_FakeMesh.mesh_dim_names"></a>`_FakeMesh.mesh_dim_names` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L23)
- <a id="_FakeMesh.ndim"></a>`_FakeMesh.ndim` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L24)
- <a id="_FakeMesh.size"></a>`_FakeMesh.size` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L27)
- <a id="_FakeParallelDims"></a>`_FakeParallelDims` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L31)
- <a id="_FakeParallelDims.__init__"></a>`_FakeParallelDims.__init__` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L39)
- <a id="_FakeParallelDims.cp_enabled"></a>`_FakeParallelDims.cp_enabled` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L33)
- <a id="_FakeParallelDims.dp_replicate"></a>`_FakeParallelDims.dp_replicate` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L36)
- <a id="_FakeParallelDims.dp_replicate_enabled"></a>`_FakeParallelDims.dp_replicate_enabled` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L32)
- <a id="_FakeParallelDims.dp_shard"></a>`_FakeParallelDims.dp_shard` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L37)
- <a id="_FakeParallelDims.get_mesh"></a>`_FakeParallelDims.get_mesh` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L47)
- <a id="_FakeParallelDims.get_optional_mesh"></a>`_FakeParallelDims.get_optional_mesh` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L43)
- <a id="_FakeParallelDims.pp_enabled"></a>`_FakeParallelDims.pp_enabled` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L34)
- <a id="_FakeParallelDims.sparse"></a>`_FakeParallelDims.sparse` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L40)
- <a id="_FakeParallelDims.tp_enabled"></a>`_FakeParallelDims.tp_enabled` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L35)
- <a id="_training_config"></a>`_training_config` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L86)
- <a id="test_autoparallel_config_validation"></a>`test_autoparallel_config_validation` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L115)
- <a id="test_autoparallel_graph_pass_selection_uses_regular_memory_policy"></a>`test_autoparallel_graph_pass_selection_uses_regular_memory_policy` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L131)
- <a id="test_autoparallel_integration_matrix"></a>`test_autoparallel_integration_matrix` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L95)
- <a id="test_model_autoparallel_uses_fx_module_path_and_resolved_policy"></a>`test_model_autoparallel_uses_fx_module_path_and_resolved_policy` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L172)
- <a id="test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model"></a>`test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L178)
- <a id="test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model.__init__"></a>`test_model_autoparallel_uses_fx_module_path_and_resolved_policy.FakeDeepSeekV3Model.__init__` — [`L179`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_autoparallel.py#L179)
