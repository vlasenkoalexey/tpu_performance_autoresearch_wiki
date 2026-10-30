---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_cpu_offload`/TestCpuOffloadPass#
symbols:
  TestCpuOffloadPass._make_fake_val: _make_fake_val().
  TestCpuOffloadPass._build_joint_graph: _build_joint_graph().
  TestCpuOffloadPass.test_prefetch_moves_reloads_earlier: test_prefetch_moves_reloads_earlier().
  TestCpuOffloadPass.test_prefetch_via_apply_pass: test_prefetch_via_apply_pass().
  TestCpuOffloadPass.test_prefetch_n_layers_2: test_prefetch_n_layers_2().
  TestCpuOffloadPass.test_wait_after_last_forward_consumer: test_wait_after_last_forward_consumer().
  TestCpuOffloadPass.test_wait_dep_points_to_last_forward_consumer: test_wait_dep_points_to_last_forward_consumer().
  TestCpuOffloadPass.test_offload_reload_ops_inserted: test_offload_reload_ops_inserted().
  TestCpuOffloadPass.test_view_chain_offloaded_with_replay: test_view_chain_offloaded_with_replay().
  TestCpuOffloadPass.test_view_replay_multi_view_same_consumer: test_view_replay_multi_view_same_consumer().
  TestCpuOffloadPass.test_tag_all_offloadable_activations_basic: test_tag_all_offloadable_activations_basic().
  TestCpuOffloadPass.test_must_save_sym_int_not_offloaded: test_must_save_sym_int_not_offloaded().
  TestCpuOffloadPass.test_tag_no_backward_consumers: test_tag_no_backward_consumers().
  TestCpuOffloadPass.test_offload_pass_noop_when_no_tags: test_offload_pass_noop_when_no_tags().
  TestCpuOffloadPass.test_view_ops_not_tagged: test_view_ops_not_tagged().
  TestCpuOffloadPass.test_small_tensors_not_tagged: test_small_tensors_not_tagged().
  TestCpuOffloadPass.test_prefetch_noop_without_offloads: test_prefetch_noop_without_offloads().
  TestCpuOffloadPass.test_saved_view_boundary_offloads_its_base: test_saved_view_boundary_offloads_its_base().
  TestCpuOffloadPass.test_wait_dep_follows_view_chain: test_wait_dep_follows_view_chain().
  TestCpuOffloadPass.test_wait_dep_non_tensor_consumer: test_wait_dep_non_tensor_consumer().
  TestCpuOffloadPass.test_single_layer_tagged: test_single_layer_tagged().
  TestCpuOffloadPass._build_view_chain_graph: _build_view_chain_graph().
  TestCpuOffloadPass._reload_positions: _reload_positions().
  TestCpuOffloadPass: ''
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py)

> **Collapsed catalog** (24 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestCpuOffloadPass"></a>`TestCpuOffloadPass` — [`L12`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L12)
- <a id="TestCpuOffloadPass._build_joint_graph"></a>`TestCpuOffloadPass._build_joint_graph` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L28)
- <a id="TestCpuOffloadPass._build_view_chain_graph"></a>`TestCpuOffloadPass._build_view_chain_graph` — [`L533`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L533)
- <a id="TestCpuOffloadPass._make_fake_val"></a>`TestCpuOffloadPass._make_fake_val` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L20)
- <a id="TestCpuOffloadPass._reload_positions"></a>`TestCpuOffloadPass._reload_positions` — [`L428`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L428)
- <a id="TestCpuOffloadPass.test_must_save_sym_int_not_offloaded"></a>`TestCpuOffloadPass.test_must_save_sym_int_not_offloaded` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L114)
- <a id="TestCpuOffloadPass.test_offload_pass_noop_when_no_tags"></a>`TestCpuOffloadPass.test_offload_pass_noop_when_no_tags` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L207)
- <a id="TestCpuOffloadPass.test_offload_reload_ops_inserted"></a>`TestCpuOffloadPass.test_offload_reload_ops_inserted` — [`L229`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L229)
- <a id="TestCpuOffloadPass.test_prefetch_moves_reloads_earlier"></a>`TestCpuOffloadPass.test_prefetch_moves_reloads_earlier` — [`L365`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L365)
- <a id="TestCpuOffloadPass.test_prefetch_n_layers_2"></a>`TestCpuOffloadPass.test_prefetch_n_layers_2` — [`L456`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L456)
- <a id="TestCpuOffloadPass.test_prefetch_noop_without_offloads"></a>`TestCpuOffloadPass.test_prefetch_noop_without_offloads` — [`L411`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L411)
- <a id="TestCpuOffloadPass.test_prefetch_via_apply_pass"></a>`TestCpuOffloadPass.test_prefetch_via_apply_pass` — [`L421`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L421)
- <a id="TestCpuOffloadPass.test_saved_view_boundary_offloads_its_base"></a>`TestCpuOffloadPass.test_saved_view_boundary_offloads_its_base` — [`L619`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L619)
- <a id="TestCpuOffloadPass.test_single_layer_tagged"></a>`TestCpuOffloadPass.test_single_layer_tagged` — [`L907`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L907)
- <a id="TestCpuOffloadPass.test_small_tensors_not_tagged"></a>`TestCpuOffloadPass.test_small_tensors_not_tagged` — [`L326`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L326)
- <a id="TestCpuOffloadPass.test_tag_all_offloadable_activations_basic"></a>`TestCpuOffloadPass.test_tag_all_offloadable_activations_basic` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L89)
- <a id="TestCpuOffloadPass.test_tag_no_backward_consumers"></a>`TestCpuOffloadPass.test_tag_no_backward_consumers` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L172)
- <a id="TestCpuOffloadPass.test_view_chain_offloaded_with_replay"></a>`TestCpuOffloadPass.test_view_chain_offloaded_with_replay` — [`L571`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L571)
- <a id="TestCpuOffloadPass.test_view_ops_not_tagged"></a>`TestCpuOffloadPass.test_view_ops_not_tagged` — [`L275`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L275)
- <a id="TestCpuOffloadPass.test_view_replay_multi_view_same_consumer"></a>`TestCpuOffloadPass.test_view_replay_multi_view_same_consumer` — [`L830`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L830)
- <a id="TestCpuOffloadPass.test_wait_after_last_forward_consumer"></a>`TestCpuOffloadPass.test_wait_after_last_forward_consumer` — [`L490`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L490)
- <a id="TestCpuOffloadPass.test_wait_dep_follows_view_chain"></a>`TestCpuOffloadPass.test_wait_dep_follows_view_chain` — [`L685`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L685)
- <a id="TestCpuOffloadPass.test_wait_dep_non_tensor_consumer"></a>`TestCpuOffloadPass.test_wait_dep_non_tensor_consumer` — [`L754`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L754)
- <a id="TestCpuOffloadPass.test_wait_dep_points_to_last_forward_consumer"></a>`TestCpuOffloadPass.test_wait_dep_points_to_last_forward_consumer` — [`L636`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_cpu_offload.py#L636)
