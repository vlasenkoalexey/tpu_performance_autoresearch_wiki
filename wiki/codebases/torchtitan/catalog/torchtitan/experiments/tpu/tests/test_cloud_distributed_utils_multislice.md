---
title: 'Module: torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_cloud_distributed_utils_multislice`/
symbols:
  ReplicateAxisValidationTest._check: ReplicateAxisValidationTest#_check().
  ReplicateAxisValidationTest.test_rejects_the_default_on_multi_slice: ReplicateAxisValidationTest#test_rejects_the_default_on_multi_slice().
  _gke_env: _gke_env().
  ReplicateAxisValidationTest.test_never_mutates: ReplicateAxisValidationTest#test_never_mutates().
  SliceCountTest.test_defaults_to_one_slice: SliceCountTest#test_defaults_to_one_slice().
  SliceCountTest.test_reads_megascale_num_slices: SliceCountTest#test_reads_megascale_num_slices().
  GkeMultiSliceInitTest.test_initializes_on_multi_slice: GkeMultiSliceInitTest#test_initializes_on_multi_slice().
  GkeMultiSliceInitTest.test_task_id_is_within_slice: GkeMultiSliceInitTest#test_task_id_is_within_slice().
  GkeMultiSliceInitTest.test_slicebuilder_addresses_cover_only_the_local_slice: GkeMultiSliceInitTest#test_slicebuilder_addresses_cover_only_the_local_slice().
  GkeMultiSliceInitTest.test_single_slice_task_id_is_the_global_rank: GkeMultiSliceInitTest#test_single_slice_task_id_is_the_global_rank().
  GkeMultiSliceInitTest.test_requires_the_megascale_client_on_multi_slice: GkeMultiSliceInitTest#test_requires_the_megascale_client_on_multi_slice().
  GkeMultiSliceInitTest.test_slice_id_is_not_required_in_the_environment: GkeMultiSliceInitTest#test_slice_id_is_not_required_in_the_environment().
  GkeMultiSliceInitTest.test_rejects_world_size_not_divisible_by_slices: GkeMultiSliceInitTest#test_rejects_world_size_not_divisible_by_slices().
  GkeMultiSliceInitTest.test_bails_out_on_inconsistent_bounds: GkeMultiSliceInitTest#test_bails_out_on_inconsistent_bounds().
  ReplicateAxisValidationTest.test_noop_on_single_slice: ReplicateAxisValidationTest#test_noop_on_single_slice().
  PinnedHostMemoryTest.test_disables_pinning_and_is_idempotent: PinnedHostMemoryTest#test_disables_pinning_and_is_idempotent().
  NodeRankTest.test_nodes_per_slice_is_the_host_list_length: NodeRankTest#test_nodes_per_slice_is_the_host_list_length().
  NodeRankTest.test_global_node_rank_is_slice_major: NodeRankTest#test_global_node_rank_is_slice_major().
  NodeRankTest.test_independent_of_chips_per_host: NodeRankTest#test_independent_of_chips_per_host().
  NodeRankTest.test_four_slices: NodeRankTest#test_four_slices().
  NodeRankTest.test_returns_none_rather_than_guessing: NodeRankTest#test_returns_none_rather_than_guessing().
  NodeRankTest._env: NodeRankTest#_env().
  SliceCountTest.test_slice_id_defaults_to_zero: SliceCountTest#test_slice_id_defaults_to_zero().
  SliceCountTest.test_pod_hostname_is_not_used: SliceCountTest#test_pod_hostname_is_not_used().
  SliceCountTest.test_slice_id_is_derived_from_the_rank: SliceCountTest#test_slice_id_is_derived_from_the_rank().
  SliceCountTest.test_slice_id_derivation_handles_four_slices: SliceCountTest#test_slice_id_derivation_handles_four_slices().
  SliceCountTest.test_explicit_slice_id_is_cross_checked_against_the_rank: SliceCountTest#test_explicit_slice_id_is_cross_checked_against_the_rank().
  SliceCountTest.test_rejects_non_positive_and_garbage: SliceCountTest#test_rejects_non_positive_and_garbage().
  ReplicateAxisValidationTest.test_accepts_replicate_equal_to_slice_count: ReplicateAxisValidationTest#test_accepts_replicate_equal_to_slice_count().
  ReplicateAxisValidationTest.test_accepts_a_multiple_of_the_slice_count: ReplicateAxisValidationTest#test_accepts_a_multiple_of_the_slice_count().
  ReplicateAxisValidationTest.test_leaves_an_indivisible_replicate_degree_to_torch_tpu: ReplicateAxisValidationTest#test_leaves_an_indivisible_replicate_degree_to_torch_tpu().
  ReplicateAxisValidationTest.test_allows_pipeline_stages_across_slices: ReplicateAxisValidationTest#test_allows_pipeline_stages_across_slices().
  ReplicateAxisValidationTest.test_allows_pipeline_and_replicate_together: ReplicateAxisValidationTest#test_allows_pipeline_and_replicate_together().
  ReplicateAxisValidationTest.test_error_names_the_flag_to_pass: ReplicateAxisValidationTest#test_error_names_the_flag_to_pass().
  NodeRankTest.test_ignores_empty_entries: NodeRankTest#test_ignores_empty_entries().
  NodeRankTest.test_none_when_multi_slice_has_no_slice_index: NodeRankTest#test_none_when_multi_slice_has_no_slice_index().
  SliceIdFromWorkerHostnamesTest.test_recovers_each_slice_index: SliceIdFromWorkerHostnamesTest#test_recovers_each_slice_index().
  SliceIdFromWorkerHostnamesTest.test_single_slice_job_is_slice_zero: SliceIdFromWorkerHostnamesTest#test_single_slice_job_is_slice_zero().
  SliceIdFromWorkerHostnamesTest.test_bare_hostnames_without_subdomain_still_parse: SliceIdFromWorkerHostnamesTest#test_bare_hostnames_without_subdomain_still_parse().
  SliceIdFromWorkerHostnamesTest.test_node_names_are_rejected: SliceIdFromWorkerHostnamesTest#test_node_names_are_rejected().
  SliceIdFromWorkerHostnamesTest.test_disagreeing_job_indices_are_rejected: SliceIdFromWorkerHostnamesTest#test_disagreeing_job_indices_are_rejected().
  SliceIdFromWorkerHostnamesTest.test_non_contiguous_pod_indices_are_rejected: SliceIdFromWorkerHostnamesTest#test_non_contiguous_pod_indices_are_rejected().
  SliceIdFromWorkerHostnamesTest.test_slice_index_beyond_the_slice_count_is_rejected: SliceIdFromWorkerHostnamesTest#test_slice_index_beyond_the_slice_count_is_rejected().
  SliceIdFromWorkerHostnamesTest.test_missing_host_list_is_none: SliceIdFromWorkerHostnamesTest#test_missing_host_list_is_none().
  SliceIdFromWorkerHostnamesTest.test_get_slice_id_uses_it_without_the_variable: SliceIdFromWorkerHostnamesTest#test_get_slice_id_uses_it_without_the_variable().
  SliceIdFromWorkerHostnamesTest.test_get_slice_id_prefers_hostnames_over_the_rank: SliceIdFromWorkerHostnamesTest#test_get_slice_id_prefers_hostnames_over_the_rank().
  SliceIdFromWorkerHostnamesTest.test_declared_variable_disagreeing_with_hostnames_raises: SliceIdFromWorkerHostnamesTest#test_declared_variable_disagreeing_with_hostnames_raises().
  SliceIdFromWorkerHostnamesTest.test_global_node_rank_without_the_variable: SliceIdFromWorkerHostnamesTest#test_global_node_rank_without_the_variable().
  SliceIdFromWorkerHostnamesTest.test_global_node_rank_none_when_nothing_carries_the_slice: SliceIdFromWorkerHostnamesTest#test_global_node_rank_none_when_nothing_carries_the_slice().
  SliceCountTest: SliceCountTest#
  GkeMultiSliceInitTest: GkeMultiSliceInitTest#
  ReplicateAxisValidationTest: ReplicateAxisValidationTest#
  PinnedHostMemoryTest: PinnedHostMemoryTest#
  NodeRankTest: NodeRankTest#
  SliceIdFromWorkerHostnamesTest: SliceIdFromWorkerHostnamesTest#
---
# Module: [`torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py)

> **Collapsed catalog** (55 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="GkeMultiSliceInitTest"></a>`GkeMultiSliceInitTest` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L108)
- <a id="GkeMultiSliceInitTest.test_bails_out_on_inconsistent_bounds"></a>`GkeMultiSliceInitTest.test_bails_out_on_inconsistent_bounds` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L161)
- <a id="GkeMultiSliceInitTest.test_initializes_on_multi_slice"></a>`GkeMultiSliceInitTest.test_initializes_on_multi_slice` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L110)
- <a id="GkeMultiSliceInitTest.test_rejects_world_size_not_divisible_by_slices"></a>`GkeMultiSliceInitTest.test_rejects_world_size_not_divisible_by_slices` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L157)
- <a id="GkeMultiSliceInitTest.test_requires_the_megascale_client_on_multi_slice"></a>`GkeMultiSliceInitTest.test_requires_the_megascale_client_on_multi_slice` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L144)
- <a id="GkeMultiSliceInitTest.test_single_slice_task_id_is_the_global_rank"></a>`GkeMultiSliceInitTest.test_single_slice_task_id_is_the_global_rank` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L132)
- <a id="GkeMultiSliceInitTest.test_slice_id_is_not_required_in_the_environment"></a>`GkeMultiSliceInitTest.test_slice_id_is_not_required_in_the_environment` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L151)
- <a id="GkeMultiSliceInitTest.test_slicebuilder_addresses_cover_only_the_local_slice"></a>`GkeMultiSliceInitTest.test_slicebuilder_addresses_cover_only_the_local_slice` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L123)
- <a id="GkeMultiSliceInitTest.test_task_id_is_within_slice"></a>`GkeMultiSliceInitTest.test_task_id_is_within_slice` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L116)
- <a id="NodeRankTest"></a>`NodeRankTest` — [`L254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L254)
- <a id="NodeRankTest._env"></a>`NodeRankTest._env` — [`L257`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L257)
- <a id="NodeRankTest.test_four_slices"></a>`NodeRankTest.test_four_slices` — [`L293`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L293)
- <a id="NodeRankTest.test_global_node_rank_is_slice_major"></a>`NodeRankTest.test_global_node_rank_is_slice_major` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L281)
- <a id="NodeRankTest.test_ignores_empty_entries"></a>`NodeRankTest.test_ignores_empty_entries` — [`L273`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L273)
- <a id="NodeRankTest.test_independent_of_chips_per_host"></a>`NodeRankTest.test_independent_of_chips_per_host` — [`L288`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L288)
- <a id="NodeRankTest.test_nodes_per_slice_is_the_host_list_length"></a>`NodeRankTest.test_nodes_per_slice_is_the_host_list_length` — [`L267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L267)
- <a id="NodeRankTest.test_none_when_multi_slice_has_no_slice_index"></a>`NodeRankTest.test_none_when_multi_slice_has_no_slice_index` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L303)
- <a id="NodeRankTest.test_returns_none_rather_than_guessing"></a>`NodeRankTest.test_returns_none_rather_than_guessing` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L297)
- <a id="PinnedHostMemoryTest"></a>`PinnedHostMemoryTest` — [`L229`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L229)
- <a id="PinnedHostMemoryTest.test_disables_pinning_and_is_idempotent"></a>`PinnedHostMemoryTest.test_disables_pinning_and_is_idempotent` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L239)
- <a id="ReplicateAxisValidationTest"></a>`ReplicateAxisValidationTest` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L168)
- <a id="ReplicateAxisValidationTest._check"></a>`ReplicateAxisValidationTest._check` — [`L179`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L179)
- <a id="ReplicateAxisValidationTest.test_accepts_a_multiple_of_the_slice_count"></a>`ReplicateAxisValidationTest.test_accepts_a_multiple_of_the_slice_count` — [`L189`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L189)
- <a id="ReplicateAxisValidationTest.test_accepts_replicate_equal_to_slice_count"></a>`ReplicateAxisValidationTest.test_accepts_replicate_equal_to_slice_count` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L185)
- <a id="ReplicateAxisValidationTest.test_allows_pipeline_and_replicate_together"></a>`ReplicateAxisValidationTest.test_allows_pipeline_and_replicate_together` — [`L208`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L208)
- <a id="ReplicateAxisValidationTest.test_allows_pipeline_stages_across_slices"></a>`ReplicateAxisValidationTest.test_allows_pipeline_stages_across_slices` — [`L203`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L203)
- <a id="ReplicateAxisValidationTest.test_error_names_the_flag_to_pass"></a>`ReplicateAxisValidationTest.test_error_names_the_flag_to_pass` — [`L212`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L212)
- <a id="ReplicateAxisValidationTest.test_leaves_an_indivisible_replicate_degree_to_torch_tpu"></a>`ReplicateAxisValidationTest.test_leaves_an_indivisible_replicate_degree_to_torch_tpu` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L199)
- <a id="ReplicateAxisValidationTest.test_never_mutates"></a>`ReplicateAxisValidationTest.test_never_mutates` — [`L218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L218)
- <a id="ReplicateAxisValidationTest.test_noop_on_single_slice"></a>`ReplicateAxisValidationTest.test_noop_on_single_slice` — [`L223`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L223)
- <a id="ReplicateAxisValidationTest.test_rejects_the_default_on_multi_slice"></a>`ReplicateAxisValidationTest.test_rejects_the_default_on_multi_slice` — [`L192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L192)
- <a id="SliceCountTest"></a>`SliceCountTest` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L52)
- <a id="SliceCountTest.test_defaults_to_one_slice"></a>`SliceCountTest.test_defaults_to_one_slice` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L54)
- <a id="SliceCountTest.test_explicit_slice_id_is_cross_checked_against_the_rank"></a>`SliceCountTest.test_explicit_slice_id_is_cross_checked_against_the_rank` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L94)
- <a id="SliceCountTest.test_pod_hostname_is_not_used"></a>`SliceCountTest.test_pod_hostname_is_not_used` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L65)
- <a id="SliceCountTest.test_reads_megascale_num_slices"></a>`SliceCountTest.test_reads_megascale_num_slices` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L58)
- <a id="SliceCountTest.test_rejects_non_positive_and_garbage"></a>`SliceCountTest.test_rejects_non_positive_and_garbage` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L101)
- <a id="SliceCountTest.test_slice_id_defaults_to_zero"></a>`SliceCountTest.test_slice_id_defaults_to_zero` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L62)
- <a id="SliceCountTest.test_slice_id_derivation_handles_four_slices"></a>`SliceCountTest.test_slice_id_derivation_handles_four_slices` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L86)
- <a id="SliceCountTest.test_slice_id_is_derived_from_the_rank"></a>`SliceCountTest.test_slice_id_is_derived_from_the_rank` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L79)
- <a id="SliceIdFromWorkerHostnamesTest"></a>`SliceIdFromWorkerHostnamesTest` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L316)
- <a id="SliceIdFromWorkerHostnamesTest.test_bare_hostnames_without_subdomain_still_parse"></a>`SliceIdFromWorkerHostnamesTest.test_bare_hostnames_without_subdomain_still_parse` — [`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L348)
- <a id="SliceIdFromWorkerHostnamesTest.test_declared_variable_disagreeing_with_hostnames_raises"></a>`SliceIdFromWorkerHostnamesTest.test_declared_variable_disagreeing_with_hostnames_raises` — [`L419`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L419)
- <a id="SliceIdFromWorkerHostnamesTest.test_disagreeing_job_indices_are_rejected"></a>`SliceIdFromWorkerHostnamesTest.test_disagreeing_job_indices_are_rejected` — [`L367`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L367)
- <a id="SliceIdFromWorkerHostnamesTest.test_get_slice_id_prefers_hostnames_over_the_rank"></a>`SliceIdFromWorkerHostnamesTest.test_get_slice_id_prefers_hostnames_over_the_rank` — [`L409`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L409)
- <a id="SliceIdFromWorkerHostnamesTest.test_get_slice_id_uses_it_without_the_variable"></a>`SliceIdFromWorkerHostnamesTest.test_get_slice_id_uses_it_without_the_variable` — [`L401`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L401)
- <a id="SliceIdFromWorkerHostnamesTest.test_global_node_rank_none_when_nothing_carries_the_slice"></a>`SliceIdFromWorkerHostnamesTest.test_global_node_rank_none_when_nothing_carries_the_slice` — [`L436`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L436)
- <a id="SliceIdFromWorkerHostnamesTest.test_global_node_rank_without_the_variable"></a>`SliceIdFromWorkerHostnamesTest.test_global_node_rank_without_the_variable` — [`L428`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L428)
- <a id="SliceIdFromWorkerHostnamesTest.test_missing_host_list_is_none"></a>`SliceIdFromWorkerHostnamesTest.test_missing_host_list_is_none` — [`L394`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L394)
- <a id="SliceIdFromWorkerHostnamesTest.test_node_names_are_rejected"></a>`SliceIdFromWorkerHostnamesTest.test_node_names_are_rejected` — [`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L357)
- <a id="SliceIdFromWorkerHostnamesTest.test_non_contiguous_pod_indices_are_rejected"></a>`SliceIdFromWorkerHostnamesTest.test_non_contiguous_pod_indices_are_rejected` — [`L376`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L376)
- <a id="SliceIdFromWorkerHostnamesTest.test_recovers_each_slice_index"></a>`SliceIdFromWorkerHostnamesTest.test_recovers_each_slice_index` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L325)
- <a id="SliceIdFromWorkerHostnamesTest.test_single_slice_job_is_slice_zero"></a>`SliceIdFromWorkerHostnamesTest.test_single_slice_job_is_slice_zero` — [`L339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L339)
- <a id="SliceIdFromWorkerHostnamesTest.test_slice_index_beyond_the_slice_count_is_rejected"></a>`SliceIdFromWorkerHostnamesTest.test_slice_index_beyond_the_slice_count_is_rejected` — [`L385`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L385)
- <a id="_gke_env"></a>`_gke_env` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cloud_distributed_utils_multislice.py#L27)
