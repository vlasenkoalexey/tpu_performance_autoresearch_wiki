---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_scan_remat_policy`/
symbols:
  _run: _run().
  TestScanBodyRematWindow.test_the_real_aux_loss_over_two_groups: TestScanBodyRematWindow#test_the_real_aux_loss_over_two_groups().
  TestScanBodyRematWindow.test_an_expert_parallel_body_without_aux_loss_is_as_before: TestScanBodyRematWindow#test_an_expert_parallel_body_without_aux_loss_is_as_before().
  TestCountCollectives.test_finds_the_count_all_reduce_and_not_the_others: TestCountCollectives#test_finds_the_count_all_reduce_and_not_the_others().
  TestCountCollectives.test_ignores_the_expert_parallel_routing_count_exchange: TestCountCollectives#test_ignores_the_expert_parallel_routing_count_exchange().
  TestScanBodyRematWindow.test_backward_no_longer_recomputes_the_counts: TestScanBodyRematWindow#test_backward_no_longer_recomputes_the_counts().
  TestScanBodyRematWindow.test_a_body_without_counts_is_partitioned_as_before: TestScanBodyRematWindow#test_a_body_without_counts_is_partitioned_as_before().
  _real_aux_term.term: _real_aux_term().term().
  EXPERTS: EXPERTS.
  _ops: _ops().
  TestScanBodyRematWindow.test_gradients_are_bitwise_identical: TestScanBodyRematWindow#test_gradients_are_bitwise_identical().
  _counts: _counts().
  _routing_counts: _routing_counts().
  TestCountCollectives.f: TestCountCollectives#f().
  _legacy_window: _legacy_window().
  TestScanBodyRematWindow.test_the_window_closes: TestScanBodyRematWindow#test_the_window_closes().
  _routing_term: _routing_term().
  _has_count_source: _has_count_source().
  TOP_K: TOP_K.
  _aux_term: _aux_term().
  _real_aux_term: _real_aux_term().
  _run.body: _run().body().
  TOKENS: TOKENS.
  _Mesh.get_group: _Mesh#get_group().
  _Mesh.size: _Mesh#size().
  TestCountCollectives.setUp: TestCountCollectives#setUp().
  TestScanBodyRematWindow.setUp: TestScanBodyRematWindow#setUp().
  DIM: DIM.
  _init_single_rank_gloo: _init_single_rank_gloo().
  _Mesh: _Mesh#
  _Mesh._group: _Mesh#_group.
  SEED: SEED.
  N_LAYERS: N_LAYERS.
  _body: _body().
  _run.capture: _run().capture().
  _Mesh.__init__: _Mesh#__init__().
  TestCountCollectives: TestCountCollectives#
  TestCountCollectives.tearDown: TestCountCollectives#tearDown().
  TestScanBodyRematWindow: TestScanBodyRematWindow#
  TestScanBodyRematWindow.tearDown: TestScanBodyRematWindow#tearDown().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py)

> **Collapsed catalog** (40 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="DIM"></a>`DIM` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L33)
- <a id="EXPERTS"></a>`EXPERTS` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L34)
- <a id="N_LAYERS"></a>`N_LAYERS` — [`L31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L31)
- <a id="SEED"></a>`SEED` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L30)
- <a id="TOKENS"></a>`TOKENS` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L32)
- <a id="TOP_K"></a>`TOP_K` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L35)
- <a id="TestCountCollectives"></a>`TestCountCollectives` — [`L167`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L167)
- <a id="TestCountCollectives.f"></a>`TestCountCollectives.f` — [`L178`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L178)
- <a id="TestCountCollectives.setUp"></a>`TestCountCollectives.setUp` — [`L170`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L170)
- <a id="TestCountCollectives.tearDown"></a>`TestCountCollectives.tearDown` — [`L173`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L173)
- <a id="TestCountCollectives.test_finds_the_count_all_reduce_and_not_the_others"></a>`TestCountCollectives.test_finds_the_count_all_reduce_and_not_the_others` — [`L177`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L177)
- <a id="TestCountCollectives.test_ignores_the_expert_parallel_routing_count_exchange"></a>`TestCountCollectives.test_ignores_the_expert_parallel_routing_count_exchange` — [`L212`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L212)
- <a id="TestScanBodyRematWindow"></a>`TestScanBodyRematWindow` — [`L227`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L227)
- <a id="TestScanBodyRematWindow.setUp"></a>`TestScanBodyRematWindow.setUp` — [`L229`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L229)
- <a id="TestScanBodyRematWindow.tearDown"></a>`TestScanBodyRematWindow.tearDown` — [`L232`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L232)
- <a id="TestScanBodyRematWindow.test_a_body_without_counts_is_partitioned_as_before"></a>`TestScanBodyRematWindow.test_a_body_without_counts_is_partitioned_as_before` — [`L293`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L293)
- <a id="TestScanBodyRematWindow.test_an_expert_parallel_body_without_aux_loss_is_as_before"></a>`TestScanBodyRematWindow.test_an_expert_parallel_body_without_aux_loss_is_as_before` — [`L302`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L302)
- <a id="TestScanBodyRematWindow.test_backward_no_longer_recomputes_the_counts"></a>`TestScanBodyRematWindow.test_backward_no_longer_recomputes_the_counts` — [`L243`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L243)
- <a id="TestScanBodyRematWindow.test_gradients_are_bitwise_identical"></a>`TestScanBodyRematWindow.test_gradients_are_bitwise_identical` — [`L236`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L236)
- <a id="TestScanBodyRematWindow.test_the_real_aux_loss_over_two_groups"></a>`TestScanBodyRematWindow.test_the_real_aux_loss_over_two_groups` — [`L262`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L262)
- <a id="TestScanBodyRematWindow.test_the_window_closes"></a>`TestScanBodyRematWindow.test_the_window_closes` — [`L311`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L311)
- <a id="_Mesh"></a>`_Mesh` — [`L83`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L83)
- <a id="_Mesh.__init__"></a>`_Mesh.__init__` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L86)
- <a id="_Mesh._group"></a>`_Mesh._group` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L87)
- <a id="_Mesh.get_group"></a>`_Mesh.get_group` — [`L89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L89)
- <a id="_Mesh.size"></a>`_Mesh.size` — [`L92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L92)
- <a id="_aux_term"></a>`_aux_term` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L57)
- <a id="_body"></a>`_body` — [`L117`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L117)
- <a id="_counts"></a>`_counts` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L48)
- <a id="_has_count_source"></a>`_has_count_source` — [`L157`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L157)
- <a id="_init_single_rank_gloo"></a>`_init_single_rank_gloo` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L38)
- <a id="_legacy_window"></a>`_legacy_window` — [`L153`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L153)
- <a id="_ops"></a>`_ops` — [`L163`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L163)
- <a id="_real_aux_term"></a>`_real_aux_term` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L96)
- <a id="_real_aux_term.term"></a>`_real_aux_term.term` — [`L99`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L99)
- <a id="_routing_counts"></a>`_routing_counts` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L63)
- <a id="_routing_term"></a>`_routing_term` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L78)
- <a id="_run"></a>`_run` — [`L126`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L126)
- <a id="_run.body"></a>`_run.body` — [`L141`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L141)
- <a id="_run.capture"></a>`_run.capture` — [`L136`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_scan_remat_policy.py#L136)
