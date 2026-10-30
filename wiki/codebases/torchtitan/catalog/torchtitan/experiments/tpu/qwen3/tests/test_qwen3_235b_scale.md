---
title: 'Module: torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.tests.test_qwen3_235b_scale`/
symbols:
  _placed_235b: _placed_235b().
  Qwen3_235BScaleTest.test_the_scan_body_gathers_what_was_sharded_at_2048_ranks: Qwen3_235BScaleTest#test_the_scan_body_gathers_what_was_sharded_at_2048_ranks().
  _FakeParallelDims.get_mesh: _FakeParallelDims#get_mesh().
  Qwen3_235BScaleTest.test_every_weight_shards_evenly_at_2048_ranks: Qwen3_235BScaleTest#test_every_weight_shards_evenly_at_2048_ranks().
  Qwen3_235BScaleTest.test_nothing_large_is_replicated_at_2048_ranks: Qwen3_235BScaleTest#test_nothing_large_is_replicated_at_2048_ranks().
  Qwen3_235BScaleTest.test_128_ranks_still_shards_every_stack_on_dim_one: Qwen3_235BScaleTest#test_128_ranks_still_shards_every_stack_on_dim_one().
  _FakeParallelDims: _FakeParallelDims#
  _FakeParallelDims._mesh: _FakeParallelDims#_mesh.
  _FakeParallelDims.__init__: _FakeParallelDims#__init__().
  _FakeParallelDims.dp_shard: _FakeParallelDims#dp_shard.
  _FakeParallelDims.cp: _FakeParallelDims#cp.
  _FakeParallelDims.dp_replicate_enabled: _FakeParallelDims#dp_replicate_enabled.
  _FakeParallelDims.dp_shard_enabled: _FakeParallelDims#dp_shard_enabled.
  _FakeParallelDims.cp_enabled: _FakeParallelDims#cp_enabled.
  _FakeParallelDims.ep_enabled: _FakeParallelDims#ep_enabled.
  _FakeParallelDims.get_optional_mesh: _FakeParallelDims#get_optional_mesh().
  Qwen3_235BScaleTest: Qwen3_235BScaleTest#
---
# Module: [`torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py)

> **Collapsed catalog** (17 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Qwen3_235BScaleTest"></a>`Qwen3_235BScaleTest` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L80)
- <a id="Qwen3_235BScaleTest.test_128_ranks_still_shards_every_stack_on_dim_one"></a>`Qwen3_235BScaleTest.test_128_ranks_still_shards_every_stack_on_dim_one` — [`L116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L116)
- <a id="Qwen3_235BScaleTest.test_every_weight_shards_evenly_at_2048_ranks"></a>`Qwen3_235BScaleTest.test_every_weight_shards_evenly_at_2048_ranks` — [`L82`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L82)
- <a id="Qwen3_235BScaleTest.test_nothing_large_is_replicated_at_2048_ranks"></a>`Qwen3_235BScaleTest.test_nothing_large_is_replicated_at_2048_ranks` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L93)
- <a id="Qwen3_235BScaleTest.test_the_scan_body_gathers_what_was_sharded_at_2048_ranks"></a>`Qwen3_235BScaleTest.test_the_scan_body_gathers_what_was_sharded_at_2048_ranks` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L103)
- <a id="_FakeParallelDims"></a>`_FakeParallelDims` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L40)
- <a id="_FakeParallelDims.__init__"></a>`_FakeParallelDims.__init__` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L43)
- <a id="_FakeParallelDims._mesh"></a>`_FakeParallelDims._mesh` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L44)
- <a id="_FakeParallelDims.cp"></a>`_FakeParallelDims.cp` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L46)
- <a id="_FakeParallelDims.cp_enabled"></a>`_FakeParallelDims.cp_enabled` — [`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L49)
- <a id="_FakeParallelDims.dp_replicate_enabled"></a>`_FakeParallelDims.dp_replicate_enabled` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L47)
- <a id="_FakeParallelDims.dp_shard"></a>`_FakeParallelDims.dp_shard` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L45)
- <a id="_FakeParallelDims.dp_shard_enabled"></a>`_FakeParallelDims.dp_shard_enabled` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L48)
- <a id="_FakeParallelDims.ep_enabled"></a>`_FakeParallelDims.ep_enabled` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L50)
- <a id="_FakeParallelDims.get_mesh"></a>`_FakeParallelDims.get_mesh` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L52)
- <a id="_FakeParallelDims.get_optional_mesh"></a>`_FakeParallelDims.get_optional_mesh` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L55)
- <a id="_placed_235b"></a>`_placed_235b` — [`L60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_qwen3_235b_scale.py#L60)
