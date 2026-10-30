---
title: 'Module: src/torch_tpu/_internal/distributed/distributed_test.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/distributed/distributed_test.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.distributed.distributed_test`/
symbols:
  _mock_env: _mock_env().
  _coords_process: _coords_process().
  EnvironmentTest.test_set_tpu_launch_env_initializes_multiprocessing_spawn: EnvironmentTest#test_set_tpu_launch_env_initializes_multiprocessing_spawn().
  EnvironmentTest.test_print_launch_env_multihost_with_coordinates: EnvironmentTest#test_print_launch_env_multihost_with_coordinates().
  TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates: TopologicalNodeRankTest#test_set_tpu_launch_env_with_coordinates().
  TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates_and_no_job_completion_index: TopologicalNodeRankTest#test_set_tpu_launch_env_with_coordinates_and_no_job_completion_index().
  TopologicalNodeRankTest.test_set_tpu_launch_env_empty_coordinates_fallback: TopologicalNodeRankTest#test_set_tpu_launch_env_empty_coordinates_fallback().
  TopologicalNodeRankTest.test_set_tpu_launch_env_out_of_bounds_coordinates_fallback: TopologicalNodeRankTest#test_set_tpu_launch_env_out_of_bounds_coordinates_fallback().
  QueryLocalDeviceCoordsTest.test_runs_this_module_in_child_process: QueryLocalDeviceCoordsTest#test_runs_this_module_in_child_process().
  QueryLocalDeviceCoordsTest.test_ignores_other_stdout_lines: QueryLocalDeviceCoordsTest#test_ignores_other_stdout_lines().
  EnvironmentTest.test_singlehost_auto_detection: EnvironmentTest#test_singlehost_auto_detection().
  EnvironmentTest.test_single_worker_hostname_inferred_as_singlehost: EnvironmentTest#test_single_worker_hostname_inferred_as_singlehost().
  EnvironmentTest.test_single_worker_hostname_with_job_completion_index_uses_multihost: EnvironmentTest#test_single_worker_hostname_with_job_completion_index_uses_multihost().
  EnvironmentTest.test_multihost_auto_detection_from_env: EnvironmentTest#test_multihost_auto_detection_from_env().
  EnvironmentTest.test_multihost_keeps_pinned_env_without_worker_hostnames: EnvironmentTest#test_multihost_keeps_pinned_env_without_worker_hostnames().
  EnvironmentTest.test_print_launch_env_singlehost: EnvironmentTest#test_print_launch_env_singlehost().
  EnvironmentTest.test_print_launch_env_always_prints_node_rank: EnvironmentTest#test_print_launch_env_always_prints_node_rank().
  TopologicalNodeRankTest.test_set_tpu_launch_env_coordinate_lookup_failure_fallback: TopologicalNodeRankTest#test_set_tpu_launch_env_coordinate_lookup_failure_fallback().
  TopologicalNodeRankTest.test_set_tpu_launch_env_without_tpu_devices_skips_query: TopologicalNodeRankTest#test_set_tpu_launch_env_without_tpu_devices_skips_query().
  TopologicalNodeRankTest.test_set_tpu_launch_env_without_topology_skips_query: TopologicalNodeRankTest#test_set_tpu_launch_env_without_topology_skips_query().
  TopologicalNodeRankTest.test_set_tpu_launch_env_ignores_auto_detected_topology: TopologicalNodeRankTest#test_set_tpu_launch_env_ignores_auto_detected_topology().
  TopologicalNodeRankTest.test_set_tpu_launch_env_keeps_pinned_node_rank: TopologicalNodeRankTest#test_set_tpu_launch_env_keeps_pinned_node_rank().
  TopologicalNodeRankTest.test_set_tpu_launch_env_singlehost_skips_query: TopologicalNodeRankTest#test_set_tpu_launch_env_singlehost_skips_query().
  QueryLocalDeviceCoordsTest.test_without_tpu_devices_returns_none: QueryLocalDeviceCoordsTest#test_without_tpu_devices_returns_none().
  QueryLocalDeviceCoordsTest.test_child_failure_returns_none: QueryLocalDeviceCoordsTest#test_child_failure_returns_none().
  QueryLocalDeviceCoordsTest.test_missing_coordinates_line_returns_none: QueryLocalDeviceCoordsTest#test_missing_coordinates_line_returns_none().
  QueryLocalDeviceCoordsTest.test_malformed_coordinates_line_returns_none: QueryLocalDeviceCoordsTest#test_malformed_coordinates_line_returns_none().
  _mock_env.get_str_env_once: _mock_env().get_str_env_once().
  _mock_env.get_int_env_once: _mock_env().get_int_env_once().
  _spawn_worker: _spawn_worker().
  EnvironmentTest: EnvironmentTest#
  TopologyTest: TopologyTest#
  TopologyTest.test_parse_topology: TopologyTest#test_parse_topology().
  TopologyTest.test_get_slice_host_coordinates_1d: TopologyTest#test_get_slice_host_coordinates_1d().
  TopologyTest.test_get_slice_host_coordinates_2d: TopologyTest#test_get_slice_host_coordinates_2d().
  TopologyTest.test_get_slice_host_coordinates_3d: TopologyTest#test_get_slice_host_coordinates_3d().
  TopologyTest.test_get_slice_host_coordinates_3d_single_host: TopologyTest#test_get_slice_host_coordinates_3d_single_host().
  TopologyTest.test_get_slice_host_coordinates_4d: TopologyTest#test_get_slice_host_coordinates_4d().
  TopologyTest.test_calculate_topological_node_rank_linearization_3d: TopologyTest#test_calculate_topological_node_rank_linearization_3d().
  TopologyTest.test_calculate_topological_node_rank_various_topologies: TopologyTest#test_calculate_topological_node_rank_various_topologies().
  TopologyTest.test_calculate_topological_node_rank_fallback: TopologyTest#test_calculate_topological_node_rank_fallback().
  TopologyTest.test_calculate_topological_node_rank_out_of_bounds_fallback: TopologyTest#test_calculate_topological_node_rank_out_of_bounds_fallback().
  TopologyTest.test_calculate_topological_node_rank_invalid_topology_fallback: TopologyTest#test_calculate_topological_node_rank_invalid_topology_fallback().
  TopologicalNodeRankTest: TopologicalNodeRankTest#
  TopologicalNodeRankTest.setUp: TopologicalNodeRankTest#setUp().
  QueryLocalDeviceCoordsTest: QueryLocalDeviceCoordsTest#
  QueryLocalDeviceCoordsTest.setUp: QueryLocalDeviceCoordsTest#setUp().
  QueryLocalDeviceCoordsTest.test_print_local_device_coords: QueryLocalDeviceCoordsTest#test_print_local_device_coords().
---
# Module: [`src/torch_tpu/_internal/distributed/distributed_test.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py)

> **Collapsed catalog** (48 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="EnvironmentTest"></a>`EnvironmentTest` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L80)
- <a id="EnvironmentTest.test_multihost_auto_detection_from_env"></a>`EnvironmentTest.test_multihost_auto_detection_from_env` — [`L153`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L153)
- <a id="EnvironmentTest.test_multihost_keeps_pinned_env_without_worker_hostnames"></a>`EnvironmentTest.test_multihost_keeps_pinned_env_without_worker_hostnames` — [`L168`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L168)
- <a id="EnvironmentTest.test_print_launch_env_always_prints_node_rank"></a>`EnvironmentTest.test_print_launch_env_always_prints_node_rank` — [`L201`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L201)
- <a id="EnvironmentTest.test_print_launch_env_multihost_with_coordinates"></a>`EnvironmentTest.test_print_launch_env_multihost_with_coordinates` — [`L212`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L212)
- <a id="EnvironmentTest.test_print_launch_env_singlehost"></a>`EnvironmentTest.test_print_launch_env_singlehost` — [`L184`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L184)
- <a id="EnvironmentTest.test_set_tpu_launch_env_initializes_multiprocessing_spawn"></a>`EnvironmentTest.test_set_tpu_launch_env_initializes_multiprocessing_spawn` — [`L82`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L82)
- <a id="EnvironmentTest.test_single_worker_hostname_inferred_as_singlehost"></a>`EnvironmentTest.test_single_worker_hostname_inferred_as_singlehost` — [`L121`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L121)
- <a id="EnvironmentTest.test_single_worker_hostname_with_job_completion_index_uses_multihost"></a>`EnvironmentTest.test_single_worker_hostname_with_job_completion_index_uses_multihost` — [`L136`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L136)
- <a id="EnvironmentTest.test_singlehost_auto_detection"></a>`EnvironmentTest.test_singlehost_auto_detection` — [`L107`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L107)
- <a id="QueryLocalDeviceCoordsTest"></a>`QueryLocalDeviceCoordsTest` — [`L553`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L553)
- <a id="QueryLocalDeviceCoordsTest.setUp"></a>`QueryLocalDeviceCoordsTest.setUp` — [`L555`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L555)
- <a id="QueryLocalDeviceCoordsTest.test_child_failure_returns_none"></a>`QueryLocalDeviceCoordsTest.test_child_failure_returns_none` — [`L611`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L611)
- <a id="QueryLocalDeviceCoordsTest.test_ignores_other_stdout_lines"></a>`QueryLocalDeviceCoordsTest.test_ignores_other_stdout_lines` — [`L598`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L598)
- <a id="QueryLocalDeviceCoordsTest.test_malformed_coordinates_line_returns_none"></a>`QueryLocalDeviceCoordsTest.test_malformed_coordinates_line_returns_none` — [`L633`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L633)
- <a id="QueryLocalDeviceCoordsTest.test_missing_coordinates_line_returns_none"></a>`QueryLocalDeviceCoordsTest.test_missing_coordinates_line_returns_none` — [`L622`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L622)
- <a id="QueryLocalDeviceCoordsTest.test_print_local_device_coords"></a>`QueryLocalDeviceCoordsTest.test_print_local_device_coords` — [`L647`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L647)
- <a id="QueryLocalDeviceCoordsTest.test_runs_this_module_in_child_process"></a>`QueryLocalDeviceCoordsTest.test_runs_this_module_in_child_process` — [`L570`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L570)
- <a id="QueryLocalDeviceCoordsTest.test_without_tpu_devices_returns_none"></a>`QueryLocalDeviceCoordsTest.test_without_tpu_devices_returns_none` — [`L561`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L561)
- <a id="TopologicalNodeRankTest"></a>`TopologicalNodeRankTest` — [`L416`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L416)
- <a id="TopologicalNodeRankTest.setUp"></a>`TopologicalNodeRankTest.setUp` — [`L418`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L418)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_coordinate_lookup_failure_fallback"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_coordinate_lookup_failure_fallback` — [`L449`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L449)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_empty_coordinates_fallback"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_empty_coordinates_fallback` — [`L463`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L463)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_ignores_auto_detected_topology"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_ignores_auto_detected_topology` — [`L511`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L511)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_keeps_pinned_node_rank"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_keeps_pinned_node_rank` — [`L529`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L529)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_out_of_bounds_coordinates_fallback"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_out_of_bounds_coordinates_fallback` — [`L475`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L475)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_singlehost_skips_query"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_singlehost_skips_query` — [`L540`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L540)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates` — [`L424`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L424)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates_and_no_job_completion_index"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_with_coordinates_and_no_job_completion_index` — [`L436`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L436)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_without_topology_skips_query"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_without_topology_skips_query` — [`L501`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L501)
- <a id="TopologicalNodeRankTest.test_set_tpu_launch_env_without_tpu_devices_skips_query"></a>`TopologicalNodeRankTest.test_set_tpu_launch_env_without_tpu_devices_skips_query` — [`L487`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L487)
- <a id="TopologyTest"></a>`TopologyTest` — [`L237`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L237)
- <a id="TopologyTest.test_calculate_topological_node_rank_fallback"></a>`TopologyTest.test_calculate_topological_node_rank_fallback` — [`L352`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L352)
- <a id="TopologyTest.test_calculate_topological_node_rank_invalid_topology_fallback"></a>`TopologyTest.test_calculate_topological_node_rank_invalid_topology_fallback` — [`L401`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L401)
- <a id="TopologyTest.test_calculate_topological_node_rank_linearization_3d"></a>`TopologyTest.test_calculate_topological_node_rank_linearization_3d` — [`L300`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L300)
- <a id="TopologyTest.test_calculate_topological_node_rank_out_of_bounds_fallback"></a>`TopologyTest.test_calculate_topological_node_rank_out_of_bounds_fallback` — [`L378`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L378)
- <a id="TopologyTest.test_calculate_topological_node_rank_various_topologies"></a>`TopologyTest.test_calculate_topological_node_rank_various_topologies` — [`L321`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L321)
- <a id="TopologyTest.test_get_slice_host_coordinates_1d"></a>`TopologyTest.test_get_slice_host_coordinates_1d` — [`L247`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L247)
- <a id="TopologyTest.test_get_slice_host_coordinates_2d"></a>`TopologyTest.test_get_slice_host_coordinates_2d` — [`L253`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L253)
- <a id="TopologyTest.test_get_slice_host_coordinates_3d"></a>`TopologyTest.test_get_slice_host_coordinates_3d` — [`L259`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L259)
- <a id="TopologyTest.test_get_slice_host_coordinates_3d_single_host"></a>`TopologyTest.test_get_slice_host_coordinates_3d_single_host` — [`L285`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L285)
- <a id="TopologyTest.test_get_slice_host_coordinates_4d"></a>`TopologyTest.test_get_slice_host_coordinates_4d` — [`L290`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L290)
- <a id="TopologyTest.test_parse_topology"></a>`TopologyTest.test_parse_topology` — [`L239`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L239)
- <a id="_coords_process"></a>`_coords_process` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L62)
- <a id="_mock_env"></a>`_mock_env` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L39)
- <a id="_mock_env.get_int_env_once"></a>`_mock_env.get_int_env_once` — [`L45`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L45)
- <a id="_mock_env.get_str_env_once"></a>`_mock_env.get_str_env_once` — [`L42`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L42)
- <a id="_spawn_worker"></a>`_spawn_worker` — [`L74`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/distributed/distributed_test.py#L74)
