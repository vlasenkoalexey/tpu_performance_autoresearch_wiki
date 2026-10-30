---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_tpu_backend_pass`/PartitionDonationTest#
symbols:
  PartitionDonationTest.test_missing_alias_metadata_disables_donation: test_missing_alias_metadata_disables_donation().
  PartitionDonationTest._split: _split().
  PartitionDonationTest.fn: fn().
  PartitionDonationTest.test_missing_tensor_value_disables_donation: test_missing_tensor_value_disables_donation().
  PartitionDonationTest.test_donates_internal_boundary_at_last_use: test_donates_internal_boundary_at_last_use().
  PartitionDonationTest.test_forced_donation_does_not_require_internal_inference: test_forced_donation_does_not_require_internal_inference().
  PartitionDonationTest.test_does_not_donate_view_of_parent_input: test_does_not_donate_view_of_parent_input().
  PartitionDonationTest.test_does_not_donate_escaping_output: test_does_not_donate_escaping_output().
  PartitionDonationTest.test_does_not_donate_aliased_producer_outputs: test_does_not_donate_aliased_producer_outputs().
  PartitionDonationTest.test_review_is_not_donated_before_sibling_alias_use: test_review_is_not_donated_before_sibling_alias_use().
  PartitionDonationTest.test_review_is_not_donated_when_sibling_alias_escapes: test_review_is_not_donated_when_sibling_alias_escapes().
  PartitionDonationTest.test_review_is_donated_after_last_sibling_alias_use: test_review_is_donated_after_last_sibling_alias_use().
  PartitionDonationTest.test_duplicate_getitem_keeps_storage_live: test_duplicate_getitem_keeps_storage_live().
  PartitionDonationTest.test_direct_compile_restores_pinned_host_reload_input: test_direct_compile_restores_pinned_host_reload_input().
  PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled: test_legacy_static_compiler_works_when_donation_is_disabled().
  PartitionDonationTest.test_maps_argument_positions_to_tensor_indices: test_maps_argument_positions_to_tensor_indices().
  PartitionDonationTest.make_test_tensor: make_test_tensor().
  PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler: test_legacy_static_compiler_works_when_donation_is_disabled().LegacyStaticCompiler#
  PartitionDonationTest: ''
  PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler.__call__: test_legacy_static_compiler_works_when_donation_is_disabled().LegacyStaticCompiler#__call__().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="PartitionDonationTest"></a>`PartitionDonationTest` — [`L13`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L13)
- <a id="PartitionDonationTest._split"></a>`PartitionDonationTest._split` — [`L15`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L15)
- <a id="PartitionDonationTest.fn"></a>`PartitionDonationTest.fn` — [`L25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L25)
- <a id="PartitionDonationTest.make_test_tensor"></a>`PartitionDonationTest.make_test_tensor` — [`L329`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L329)
- <a id="PartitionDonationTest.test_direct_compile_restores_pinned_host_reload_input"></a>`PartitionDonationTest.test_direct_compile_restores_pinned_host_reload_input` — [`L312`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L312)
- <a id="PartitionDonationTest.test_does_not_donate_aliased_producer_outputs"></a>`PartitionDonationTest.test_does_not_donate_aliased_producer_outputs` — [`L110`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L110)
- <a id="PartitionDonationTest.test_does_not_donate_escaping_output"></a>`PartitionDonationTest.test_does_not_donate_escaping_output` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L94)
- <a id="PartitionDonationTest.test_does_not_donate_view_of_parent_input"></a>`PartitionDonationTest.test_does_not_donate_view_of_parent_input` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L78)
- <a id="PartitionDonationTest.test_donates_internal_boundary_at_last_use"></a>`PartitionDonationTest.test_donates_internal_boundary_at_last_use` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L24)
- <a id="PartitionDonationTest.test_duplicate_getitem_keeps_storage_live"></a>`PartitionDonationTest.test_duplicate_getitem_keeps_storage_live` — [`L198`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L198)
- <a id="PartitionDonationTest.test_forced_donation_does_not_require_internal_inference"></a>`PartitionDonationTest.test_forced_donation_does_not_require_internal_inference` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L48)
- <a id="PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled"></a>`PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled` — [`L358`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L358)
- <a id="PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler"></a>`PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler` — [`L362`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L362)
- <a id="PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler.__call__"></a>`PartitionDonationTest.test_legacy_static_compiler_works_when_donation_is_disabled.LegacyStaticCompiler.__call__` — [`L364`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L364)
- <a id="PartitionDonationTest.test_maps_argument_positions_to_tensor_indices"></a>`PartitionDonationTest.test_maps_argument_positions_to_tensor_indices` — [`L291`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L291)
- <a id="PartitionDonationTest.test_missing_alias_metadata_disables_donation"></a>`PartitionDonationTest.test_missing_alias_metadata_disables_donation` — [`L254`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L254)
- <a id="PartitionDonationTest.test_missing_tensor_value_disables_donation"></a>`PartitionDonationTest.test_missing_tensor_value_disables_donation` — [`L233`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L233)
- <a id="PartitionDonationTest.test_review_is_donated_after_last_sibling_alias_use"></a>`PartitionDonationTest.test_review_is_donated_after_last_sibling_alias_use` — [`L172`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L172)
- <a id="PartitionDonationTest.test_review_is_not_donated_before_sibling_alias_use"></a>`PartitionDonationTest.test_review_is_not_donated_before_sibling_alias_use` — [`L127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L127)
- <a id="PartitionDonationTest.test_review_is_not_donated_when_sibling_alias_escapes"></a>`PartitionDonationTest.test_review_is_not_donated_when_sibling_alias_escapes` — [`L154`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_backend_pass.py#L154)
