---
title: 'Module: torchtitan/experiments/tpu/tests/test_cp_attention.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_cp_attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_cp_attention`/
symbols:
  CPAttentionParityTest._run: CPAttentionParityTest#_run().
  CompiledCPCollectivesTest.test_ulysses_waits_each_all_to_all_once: CompiledCPCollectivesTest#test_ulysses_waits_each_all_to_all_once().
  CPShardTest.test_cp_shard_precomputes_full_segment_ids_once_per_step: CPShardTest#test_cp_shard_precomputes_full_segment_ids_once_per_step().
  CPValidationTest.test_rejects_non_causal_kv_all_gather: CPValidationTest#test_rejects_non_causal_kv_all_gather().
  CPShardTest.test_kv_all_gather_cp_shard_respects_input_shardings: CPShardTest#test_kv_all_gather_cp_shard_respects_input_shardings().
  CPShardTest.test_cp_rank_cache_device_normalization: CPShardTest#test_cp_rank_cache_device_normalization().
  CompiledCPCollectivesTest.test_kv_all_gather_waits_each_collective_once: CompiledCPCollectivesTest#test_kv_all_gather_waits_each_collective_once().
  CPValidationTest.test_rejects_splash_blocks_that_do_not_tile_the_shards: CPValidationTest#test_rejects_splash_blocks_that_do_not_tile_the_shards().
  CPValidationTest.test_accepts_splash_blocks_capped_at_the_shard_length: CPValidationTest#test_accepts_splash_blocks_capped_at_the_shard_length().
  CPValidationTest.test_out_transform_is_rejected: CPValidationTest#test_out_transform_is_rejected().
  CPValidationTest._config: CPValidationTest#_config().
  _emulated_cp_group: _emulated_cp_group().
  CPAttentionParityTest.test_kv_all_gather_matches_dense_attention: CPAttentionParityTest#test_kv_all_gather_matches_dense_attention().
  CPShardTest.test_kv_all_gather_cp_shard_layout: CPShardTest#test_kv_all_gather_cp_shard_layout().
  CPValidationTest.test_rejects_pipeline_parallelism: CPValidationTest#test_rejects_pipeline_parallelism().
  CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits: CompiledCPCollectivesTest#test_tpu_selective_ac_recomputes_collectives_with_their_waits().
  CPValidationTest.test_rejects_unshardable_sequence_lengths: CPValidationTest#test_rejects_unshardable_sequence_lengths().
  CPValidationTest.test_accepts_shardable_sequence_lengths: CPValidationTest#test_accepts_shardable_sequence_lengths().
  InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once: InstallTPUCPPatchesTest#test_flattens_dp_shard_and_cp_once().
  _all_to_all: _all_to_all().
  CPAttentionParityTest.make_attn: CPAttentionParityTest#make_attn().
  _Ranks.exchange: _Ranks#exchange().
  CPAttentionParityTest.test_ulysses_matches_dense_attention: CPAttentionParityTest#test_ulysses_matches_dense_attention().
  CPValidationTest.test_rejects_tokamax_diag_skip_with_head_tail_cp: CPValidationTest#test_rejects_tokamax_diag_skip_with_head_tail_cp().
  CPValidationTest.test_kv_all_gather_rejects_masks_it_cannot_apply: CPValidationTest#test_kv_all_gather_rejects_masks_it_cannot_apply().
  CPAttentionParityTest._check: CPAttentionParityTest#_check().
  CompiledCPCollectivesTest.waits_on_saved_tensors: CompiledCPCollectivesTest#waits_on_saved_tensors().
  _emulated_cp_group.reduce_scatter_tensor: _emulated_cp_group().reduce_scatter_tensor().
  _shard: _shard().
  CPValidationTest.test_ulysses_sdpa_rejects_sliding_windows_without_a_kernel: CPValidationTest#test_ulysses_sdpa_rejects_sliding_windows_without_a_kernel().
  _dense_local_attention: _dense_local_attention().
  _SEQ_LEN: _SEQ_LEN.
  CompiledCPCollectivesTest._assert_waits_pair_with_collectives: CompiledCPCollectivesTest#_assert_waits_pair_with_collectives().
  _Ranks.rank: _Ranks#rank().
  _Ranks.group: _Ranks#group().
  _Ranks.run: _Ranks#run().
  _Ranks.run_rank: _Ranks#run_rank().
  CPAttentionParityTest.run_rank: CPAttentionParityTest#run_rank().
  _COLLECTIVES: _COLLECTIVES.
  CPShardTest.prepare: CPShardTest#prepare().
  CompiledCPCollectivesTest._graphs: CompiledCPCollectivesTest#_graphs().
  InstallTPUCPPatchesTest.resolve: InstallTPUCPPatchesTest#resolve().
  _Ranks.world_size: _Ranks#world_size.
  _WAIT: _WAIT.
  CPAttentionParityTest.kwargs_fn: CPAttentionParityTest#kwargs_fn().
  _C10D: _C10D.
  _emulated_cp_group.all_to_all_single: _emulated_cp_group().all_to_all_single().
  _emulated_cp_group.all_gather_tensor: _emulated_cp_group().all_gather_tensor().
  _emulated_cp_group.redistribute: _emulated_cp_group().redistribute().
  _unshard: _unshard().
  _Ranks: _Ranks#
  _Ranks._barrier: _Ranks#_barrier.
  InstallTPUCPPatchesTest.dims: InstallTPUCPPatchesTest#dims().
  _AllToAll.forward: _AllToAll#forward().
  _AllToAll.backward: _AllToAll#backward().
  CPAttentionParityTest.setUp: CPAttentionParityTest#setUp().
  CPShardTest.setUp: CPShardTest#setUp().
  CPShardTest.test_headtail_order_matches_torch_load_balancer: CPShardTest#test_headtail_order_matches_torch_load_balancer().
  CompiledCPCollectivesTest.setUp: CompiledCPCollectivesTest#setUp().
  CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.forward: CompiledCPCollectivesTest#test_tpu_selective_ac_recomputes_collectives_with_their_waits().Block#forward().
  _Ranks._slots: _Ranks#_slots.
  _Ranks._local: _Ranks#_local.
  _dense_attention: _dense_attention().
  _DOCS: _DOCS.
  CompiledCPCollectivesTest.capture: CompiledCPCollectivesTest#capture().
  CompiledCPCollectivesTest._inputs: CompiledCPCollectivesTest#_inputs().
  CompiledCPCollectivesTest.fn: CompiledCPCollectivesTest#fn().
  Block.w: Block#w.
  InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh: InstallTPUCPPatchesTest#test_flattens_dp_shard_and_cp_once().FakeMesh#
  _AllToAll: _AllToAll#
  _Redistribute: _Redistribute#
  _packed_positions: _packed_positions().
  CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block: CompiledCPCollectivesTest#test_tpu_selective_ac_recomputes_collectives_with_their_waits().Block#
  _Ranks.__init__: _Ranks#__init__().
  _Redistribute.forward: _Redistribute#forward().
  _Redistribute.backward: _Redistribute#backward().
  CPAttentionParityTest: CPAttentionParityTest#
  CPShardTest: CPShardTest#
  CompiledCPCollectivesTest: CompiledCPCollectivesTest#
  CompiledCPCollectivesTest.setUpClass: CompiledCPCollectivesTest#setUpClass().
  CompiledCPCollectivesTest.tearDownClass: CompiledCPCollectivesTest#tearDownClass().
  CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.__init__: CompiledCPCollectivesTest#test_tpu_selective_ac_recomputes_collectives_with_their_waits().Block#__init__().
  CPValidationTest: CPValidationTest#
  CPValidationTest.test_qwen3_1_7b_cp_recipes_build_and_validate: CPValidationTest#test_qwen3_1_7b_cp_recipes_build_and_validate().
  InstallTPUCPPatchesTest: InstallTPUCPPatchesTest#
  InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh.__getitem__: InstallTPUCPPatchesTest#test_flattens_dp_shard_and_cp_once().FakeMesh#__getitem__().
---
# Module: [`torchtitan/experiments/tpu/tests/test_cp_attention.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py)

> **Collapsed catalog** (86 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Block.w"></a>`Block.w` — [`L692`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L692)
- <a id="CPAttentionParityTest"></a>`CPAttentionParityTest` — [`L256`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L256)
- <a id="CPAttentionParityTest._check"></a>`CPAttentionParityTest._check` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L295)
- <a id="CPAttentionParityTest._run"></a>`CPAttentionParityTest._run` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L265)
- <a id="CPAttentionParityTest.kwargs_fn"></a>`CPAttentionParityTest.kwargs_fn` — [`L317`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L317)
- <a id="CPAttentionParityTest.make_attn"></a>`CPAttentionParityTest.make_attn` — [`L340`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L340)
- <a id="CPAttentionParityTest.run_rank"></a>`CPAttentionParityTest.run_rank` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L277)
- <a id="CPAttentionParityTest.setUp"></a>`CPAttentionParityTest.setUp` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L259)
- <a id="CPAttentionParityTest.test_kv_all_gather_matches_dense_attention"></a>`CPAttentionParityTest.test_kv_all_gather_matches_dense_attention` — [`L309`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L309)
- <a id="CPAttentionParityTest.test_ulysses_matches_dense_attention"></a>`CPAttentionParityTest.test_ulysses_matches_dense_attention` — [`L336`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L336)
- <a id="CPShardTest"></a>`CPShardTest` — [`L362`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L362)
- <a id="CPShardTest.prepare"></a>`CPShardTest.prepare` — [`L377`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L377)
- <a id="CPShardTest.setUp"></a>`CPShardTest.setUp` — [`L365`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L365)
- <a id="CPShardTest.test_cp_rank_cache_device_normalization"></a>`CPShardTest.test_cp_rank_cache_device_normalization` — [`L467`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L467)
- <a id="CPShardTest.test_cp_shard_precomputes_full_segment_ids_once_per_step"></a>`CPShardTest.test_cp_shard_precomputes_full_segment_ids_once_per_step` — [`L498`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L498) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="CPShardTest.test_headtail_order_matches_torch_load_balancer"></a>`CPShardTest.test_headtail_order_matches_torch_load_balancer` — [`L552`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L552) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="CPShardTest.test_kv_all_gather_cp_shard_layout"></a>`CPShardTest.test_kv_all_gather_cp_shard_layout` — [`L371`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L371) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="CPShardTest.test_kv_all_gather_cp_shard_respects_input_shardings"></a>`CPShardTest.test_kv_all_gather_cp_shard_respects_input_shardings` — [`L413`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L413) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="CPValidationTest"></a>`CPValidationTest` — [`L715`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L715)
- <a id="CPValidationTest._config"></a>`CPValidationTest._config` — [`L718`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L718)
- <a id="CPValidationTest.test_accepts_shardable_sequence_lengths"></a>`CPValidationTest.test_accepts_shardable_sequence_lengths` — [`L763`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L763)
- <a id="CPValidationTest.test_accepts_splash_blocks_capped_at_the_shard_length"></a>`CPValidationTest.test_accepts_splash_blocks_capped_at_the_shard_length` — [`L800`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L800)
- <a id="CPValidationTest.test_kv_all_gather_rejects_masks_it_cannot_apply"></a>`CPValidationTest.test_kv_all_gather_rejects_masks_it_cannot_apply` — [`L864`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L864)
- <a id="CPValidationTest.test_out_transform_is_rejected"></a>`CPValidationTest.test_out_transform_is_rejected` — [`L842`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L842)
- <a id="CPValidationTest.test_qwen3_1_7b_cp_recipes_build_and_validate"></a>`CPValidationTest.test_qwen3_1_7b_cp_recipes_build_and_validate` — [`L880`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L880)
- <a id="CPValidationTest.test_rejects_non_causal_kv_all_gather"></a>`CPValidationTest.test_rejects_non_causal_kv_all_gather` — [`L817`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L817)
- <a id="CPValidationTest.test_rejects_pipeline_parallelism"></a>`CPValidationTest.test_rejects_pipeline_parallelism` — [`L728`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L728)
- <a id="CPValidationTest.test_rejects_splash_blocks_that_do_not_tile_the_shards"></a>`CPValidationTest.test_rejects_splash_blocks_that_do_not_tile_the_shards` — [`L788`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L788)
- <a id="CPValidationTest.test_rejects_tokamax_diag_skip_with_head_tail_cp"></a>`CPValidationTest.test_rejects_tokamax_diag_skip_with_head_tail_cp` — [`L807`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L807)
- <a id="CPValidationTest.test_rejects_unshardable_sequence_lengths"></a>`CPValidationTest.test_rejects_unshardable_sequence_lengths` — [`L754`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L754)
- <a id="CPValidationTest.test_ulysses_sdpa_rejects_sliding_windows_without_a_kernel"></a>`CPValidationTest.test_ulysses_sdpa_rejects_sliding_windows_without_a_kernel` — [`L834`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L834)
- <a id="CompiledCPCollectivesTest"></a>`CompiledCPCollectivesTest` — [`L562`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L562)
- <a id="CompiledCPCollectivesTest._assert_waits_pair_with_collectives"></a>`CompiledCPCollectivesTest._assert_waits_pair_with_collectives` — [`L616`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L616)
- <a id="CompiledCPCollectivesTest._graphs"></a>`CompiledCPCollectivesTest._graphs` — [`L596`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L596)
- <a id="CompiledCPCollectivesTest._inputs"></a>`CompiledCPCollectivesTest._inputs` — [`L636`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L636)
- <a id="CompiledCPCollectivesTest.capture"></a>`CompiledCPCollectivesTest.capture` — [`L603`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L603)
- <a id="CompiledCPCollectivesTest.fn"></a>`CompiledCPCollectivesTest.fn` — [`L651`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L651)
- <a id="CompiledCPCollectivesTest.setUp"></a>`CompiledCPCollectivesTest.setUp` — [`L584`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L584)
- <a id="CompiledCPCollectivesTest.setUpClass"></a>`CompiledCPCollectivesTest.setUpClass` — [`L571`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L571)
- <a id="CompiledCPCollectivesTest.tearDownClass"></a>`CompiledCPCollectivesTest.tearDownClass` — [`L580`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L580)
- <a id="CompiledCPCollectivesTest.test_kv_all_gather_waits_each_collective_once"></a>`CompiledCPCollectivesTest.test_kv_all_gather_waits_each_collective_once` — [`L659`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L659)
- <a id="CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits"></a>`CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits` — [`L685`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L685)
- <a id="CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block"></a>`CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block` — [`L688`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L688)
- <a id="CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.__init__"></a>`CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.__init__` — [`L690`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L690)
- <a id="CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.forward"></a>`CompiledCPCollectivesTest.test_tpu_selective_ac_recomputes_collectives_with_their_waits.Block.forward` — [`L694`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L694)
- <a id="CompiledCPCollectivesTest.test_ulysses_waits_each_all_to_all_once"></a>`CompiledCPCollectivesTest.test_ulysses_waits_each_all_to_all_once` — [`L643`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L643)
- <a id="CompiledCPCollectivesTest.waits_on_saved_tensors"></a>`CompiledCPCollectivesTest.waits_on_saved_tensors` — [`L701`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L701)
- <a id="InstallTPUCPPatchesTest"></a>`InstallTPUCPPatchesTest` — [`L888`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L888)
- <a id="InstallTPUCPPatchesTest.dims"></a>`InstallTPUCPPatchesTest.dims` — [`L935`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L935)
- <a id="InstallTPUCPPatchesTest.resolve"></a>`InstallTPUCPPatchesTest.resolve` — [`L901`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L901)
- <a id="InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once"></a>`InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once` — [`L891`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L891)
- <a id="InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh"></a>`InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh` — [`L894`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L894)
- <a id="InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh.__getitem__"></a>`InstallTPUCPPatchesTest.test_flattens_dp_shard_and_cp_once.FakeMesh.__getitem__` — [`L896`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L896)
- <a id="_AllToAll"></a>`_AllToAll` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L103)
- <a id="_AllToAll.backward"></a>`_AllToAll.backward` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L112)
- <a id="_AllToAll.forward"></a>`_AllToAll.forward` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L107)
- <a id="_C10D"></a>`_C10D` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L51)
- <a id="_COLLECTIVES"></a>`_COLLECTIVES` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L53)
- <a id="_DOCS"></a>`_DOCS` — [`L253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L253)
- <a id="_Ranks"></a>`_Ranks` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L60)
- <a id="_Ranks.__init__"></a>`_Ranks.__init__` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L63)
- <a id="_Ranks._barrier"></a>`_Ranks._barrier` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L65)
- <a id="_Ranks._local"></a>`_Ranks._local` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L67)
- <a id="_Ranks._slots"></a>`_Ranks._slots` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L66)
- <a id="_Ranks.exchange"></a>`_Ranks.exchange` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L76)
- <a id="_Ranks.group"></a>`_Ranks.group` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L73)
- <a id="_Ranks.rank"></a>`_Ranks.rank` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L70)
- <a id="_Ranks.run"></a>`_Ranks.run` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L84)
- <a id="_Ranks.run_rank"></a>`_Ranks.run_rank` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L85)
- <a id="_Ranks.world_size"></a>`_Ranks.world_size` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L64)
- <a id="_Redistribute"></a>`_Redistribute` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L116)
- <a id="_Redistribute.backward"></a>`_Redistribute.backward` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L128)
- <a id="_Redistribute.forward"></a>`_Redistribute.forward` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L120)
- <a id="_SEQ_LEN"></a>`_SEQ_LEN` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L252)
- <a id="_WAIT"></a>`_WAIT` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L52)
- <a id="_all_to_all"></a>`_all_to_all` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L97)
- <a id="_dense_attention"></a>`_dense_attention` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L217)
- <a id="_dense_local_attention"></a>`_dense_local_attention` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L238)
- <a id="_emulated_cp_group"></a>`_emulated_cp_group` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L139)
- <a id="_emulated_cp_group.all_gather_tensor"></a>`_emulated_cp_group.all_gather_tensor` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L147)
- <a id="_emulated_cp_group.all_to_all_single"></a>`_emulated_cp_group.all_to_all_single` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L142)
- <a id="_emulated_cp_group.redistribute"></a>`_emulated_cp_group.redistribute` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L159)
- <a id="_emulated_cp_group.reduce_scatter_tensor"></a>`_emulated_cp_group.reduce_scatter_tensor` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L151)
- <a id="_packed_positions"></a>`_packed_positions` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L210)
- <a id="_shard"></a>`_shard` — [`L186`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L186) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
- <a id="_unshard"></a>`_unshard` — [`L197`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_cp_attention.py#L197) — documented in [tpu-context-parallel-attention](../../../../../concepts/tpu-context-parallel-attention.md)
