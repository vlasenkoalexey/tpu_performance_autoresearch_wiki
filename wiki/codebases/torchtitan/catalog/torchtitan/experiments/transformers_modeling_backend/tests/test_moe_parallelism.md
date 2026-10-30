---
title: 'Module: torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.transformers_modeling_backend.tests.test_moe_parallelism`/
symbols:
  TestNativeMoeLoadBalancing.test_optimizer_hook_updates_expert_bias: TestNativeMoeLoadBalancing#test_optimizer_hook_updates_expert_bias().
  TestPrepareNativeMoeConfigs.test_moe_config_build: TestPrepareNativeMoeConfigs#test_moe_config_build().
  TestNativeMoeBuildAndSwap.test_build_produces_native_moe: TestNativeMoeBuildAndSwap#test_build_produces_native_moe().
  TestNativeMoeBuildAndSwap.test_init_states_materializes_params: TestNativeMoeBuildAndSwap#test_init_states_materializes_params().
  TestNativeMoeBuildAndSwap.test_native_moe_backward: TestNativeMoeBuildAndSwap#test_native_moe_backward().
  TestNativeMoeLoadBalancing.test_native_moe_exposes_load_balance_attrs: TestNativeMoeLoadBalancing#test_native_moe_exposes_load_balance_attrs().
  TestNativeMoeLoadBalancing.test_forward_accumulates_tokens_per_expert: TestNativeMoeLoadBalancing#test_forward_accumulates_tokens_per_expert().
  _prepare_layers: _prepare_layers().
  TestNativeMoeBuildAndSwap.test_native_moe_forward: TestNativeMoeBuildAndSwap#test_native_moe_forward().
  _create_tiny_qwen3moe_model: _create_tiny_qwen3moe_model().
  TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy.layers: TestPrepareNativeMoeConfigs#test_prepare_stores_config_on_layers()._ModelProxy#layers.
  TestPrepareNativeMoeConfigs.test_qwen3_moe_config_probing: TestPrepareNativeMoeConfigs#test_qwen3_moe_config_probing().
  TestPrepareNativeMoeConfigs.test_deepseek_v3_config_probing: TestPrepareNativeMoeConfigs#test_deepseek_v3_config_probing().
  TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers: TestPrepareNativeMoeConfigs#test_prepare_stores_config_on_layers().
  _moe_buffer: _moe_buffer().
  _expert_weights: _expert_weights().
  _FakeParallelDims.__init__: _FakeParallelDims#__init__().
  _FakeParallelDims._meshes: _FakeParallelDims#_meshes.
  _HAS_DTENSOR_TEST: _HAS_DTENSOR_TEST.
  _FakeParallelDims.get_optional_mesh: _FakeParallelDims#get_optional_mesh().
  _FakeParallelDims.get_mesh: _FakeParallelDims#get_mesh().
  _FakeParallelDims.resolve_mesh: _FakeParallelDims#resolve_mesh().
  _FakeParallelDims.seq_len_divisor: _FakeParallelDims#seq_len_divisor().
  TestMoeDetection.test_moe_enabled_all_moe: TestMoeDetection#test_moe_enabled_all_moe().
  TestMoeDetection.test_moe_enabled_mixed: TestMoeDetection#test_moe_enabled_mixed().
  _FakeParallelDims.tp: _FakeParallelDims#tp.
  _create_tiny_deepseek_v3_model: _create_tiny_deepseek_v3_model().
  _FakeParallelDims: _FakeParallelDims#
  _FakeParallelDims.tp_enabled: _FakeParallelDims#tp_enabled.
  _FakeParallelDims.ep_enabled: _FakeParallelDims#ep_enabled.
  TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy: TestPrepareNativeMoeConfigs#test_prepare_stores_config_on_layers()._ModelProxy#
  _FakeParallelDims.spmd_backend: _FakeParallelDims#spmd_backend.
  _FakeParallelDims.ep: _FakeParallelDims#ep.
  TestPrepareNativeMoeConfigs: TestPrepareNativeMoeConfigs#
  TestNativeMoeBuildAndSwap: TestNativeMoeBuildAndSwap#
  TestNativeMoeLoadBalancing: TestNativeMoeLoadBalancing#
  TestMoeDetection: TestMoeDetection#
---
# Module: [`torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py)

> **Collapsed catalog** (37 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestMoeDetection"></a>`TestMoeDetection` — [`L562`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L562)
- <a id="TestMoeDetection.test_moe_enabled_all_moe"></a>`TestMoeDetection.test_moe_enabled_all_moe` — [`L565`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L565)
- <a id="TestMoeDetection.test_moe_enabled_mixed"></a>`TestMoeDetection.test_moe_enabled_mixed` — [`L574`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L574)
- <a id="TestNativeMoeBuildAndSwap"></a>`TestNativeMoeBuildAndSwap` — [`L308`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L308)
- <a id="TestNativeMoeBuildAndSwap.test_build_produces_native_moe"></a>`TestNativeMoeBuildAndSwap.test_build_produces_native_moe` — [`L311`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L311)
- <a id="TestNativeMoeBuildAndSwap.test_init_states_materializes_params"></a>`TestNativeMoeBuildAndSwap.test_init_states_materializes_params` — [`L338`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L338)
- <a id="TestNativeMoeBuildAndSwap.test_native_moe_backward"></a>`TestNativeMoeBuildAndSwap.test_native_moe_backward` — [`L405`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L405)
- <a id="TestNativeMoeBuildAndSwap.test_native_moe_forward"></a>`TestNativeMoeBuildAndSwap.test_native_moe_forward` — [`L376`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L376)
- <a id="TestNativeMoeLoadBalancing"></a>`TestNativeMoeLoadBalancing` — [`L443`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L443)
- <a id="TestNativeMoeLoadBalancing.test_forward_accumulates_tokens_per_expert"></a>`TestNativeMoeLoadBalancing.test_forward_accumulates_tokens_per_expert` — [`L473`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L473)
- <a id="TestNativeMoeLoadBalancing.test_native_moe_exposes_load_balance_attrs"></a>`TestNativeMoeLoadBalancing.test_native_moe_exposes_load_balance_attrs` — [`L446`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L446)
- <a id="TestNativeMoeLoadBalancing.test_optimizer_hook_updates_expert_bias"></a>`TestNativeMoeLoadBalancing.test_optimizer_hook_updates_expert_bias` — [`L503`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L503)
- <a id="TestPrepareNativeMoeConfigs"></a>`TestPrepareNativeMoeConfigs` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L217)
- <a id="TestPrepareNativeMoeConfigs.test_deepseek_v3_config_probing"></a>`TestPrepareNativeMoeConfigs.test_deepseek_v3_config_probing` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L239)
- <a id="TestPrepareNativeMoeConfigs.test_moe_config_build"></a>`TestPrepareNativeMoeConfigs.test_moe_config_build` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L258)
- <a id="TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers"></a>`TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L276)
- <a id="TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy"></a>`TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy` — [`L292`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L292)
- <a id="TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy.layers"></a>`TestPrepareNativeMoeConfigs.test_prepare_stores_config_on_layers._ModelProxy.layers` — [`L293`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L293)
- <a id="TestPrepareNativeMoeConfigs.test_qwen3_moe_config_probing"></a>`TestPrepareNativeMoeConfigs.test_qwen3_moe_config_probing` — [`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L220)
- <a id="_FakeParallelDims"></a>`_FakeParallelDims` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L172)
- <a id="_FakeParallelDims.__init__"></a>`_FakeParallelDims.__init__` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L181)
- <a id="_FakeParallelDims._meshes"></a>`_FakeParallelDims._meshes` — [`L182`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L182)
- <a id="_FakeParallelDims.ep"></a>`_FakeParallelDims.ep` — [`L179`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L179)
- <a id="_FakeParallelDims.ep_enabled"></a>`_FakeParallelDims.ep_enabled` — [`L177`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L177)
- <a id="_FakeParallelDims.get_mesh"></a>`_FakeParallelDims.get_mesh` — [`L194`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L194)
- <a id="_FakeParallelDims.get_optional_mesh"></a>`_FakeParallelDims.get_optional_mesh` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L186)
- <a id="_FakeParallelDims.resolve_mesh"></a>`_FakeParallelDims.resolve_mesh` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L200)
- <a id="_FakeParallelDims.seq_len_divisor"></a>`_FakeParallelDims.seq_len_divisor` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L208)
- <a id="_FakeParallelDims.spmd_backend"></a>`_FakeParallelDims.spmd_backend` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L175)
- <a id="_FakeParallelDims.tp"></a>`_FakeParallelDims.tp` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L178)
- <a id="_FakeParallelDims.tp_enabled"></a>`_FakeParallelDims.tp_enabled` — [`L176`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L176)
- <a id="_HAS_DTENSOR_TEST"></a>`_HAS_DTENSOR_TEST` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L65)
- <a id="_create_tiny_deepseek_v3_model"></a>`_create_tiny_deepseek_v3_model` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L115)
- <a id="_create_tiny_qwen3moe_model"></a>`_create_tiny_qwen3moe_model` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L79)
- <a id="_expert_weights"></a>`_expert_weights` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L27)
- <a id="_moe_buffer"></a>`_moe_buffer` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L46)
- <a id="_prepare_layers"></a>`_prepare_layers` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/transformers_modeling_backend/tests/test_moe_parallelism.py#L158)
