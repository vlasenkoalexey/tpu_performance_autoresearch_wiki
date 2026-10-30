---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_tpu_host_offload`/
symbols:
  ScanOffloadTest._pair: ScanOffloadTest#_pair().
  ScanOffloadTest.test_a_dead_reader_of_the_stack_does_not_block_the_offload: ScanOffloadTest#test_a_dead_reader_of_the_stack_does_not_block_the_offload().
  ScanOffloadTest.test_the_offload_goes_in_the_forward_body_and_the_reload_in_the_backward: ScanOffloadTest#test_the_offload_goes_in_the_forward_body_and_the_reload_in_the_backward().
  ScanOffloadTest.test_a_live_second_reader_leaves_the_stack_on_device: ScanOffloadTest#test_a_live_second_reader_leaves_the_stack_on_device().
  ScanOffloadTest.test_a_body_that_reads_the_stack_whole_is_left_on_device: ScanOffloadTest#test_a_body_that_reads_the_stack_whole_is_left_on_device().
  ScanOffloadTest.graph: ScanOffloadTest#graph.
  ScanOffloadTest.test_a_graph_with_no_scan_at_all_is_an_error_not_a_quiet_no_op: ScanOffloadTest#test_a_graph_with_no_scan_at_all_is_an_error_not_a_quiet_no_op().
  _ao_targets: _ao_targets().
  _mm: _mm().
  ScanOffloadTest.x: ScanOffloadTest#x.
  ScanOffloadTest._gm: ScanOffloadTest#_gm().
  _bwd_body: _bwd_body().
  _body_of: _body_of().
  ScanOffloadTest._attach: ScanOffloadTest#_attach().
  _AO: _AO.
  _fwd_body: _fwd_body().
  _ROW: _ROW.
  _STACK: _STACK.
  _RELOAD: _RELOAD.
  _OFFLOAD: _OFFLOAD.
  ScanOffloadTest.root: ScanOffloadTest#root.
  _SCAN: _SCAN.
  ScanOffloadTest: ScanOffloadTest#
  ScanOffloadTest.setUp: ScanOffloadTest#setUp().
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py)

> **Collapsed catalog** (24 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="ScanOffloadTest"></a>`ScanOffloadTest` — [`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L85)
- <a id="ScanOffloadTest._attach"></a>`ScanOffloadTest._attach` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L97)
- <a id="ScanOffloadTest._gm"></a>`ScanOffloadTest._gm` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L94)
- <a id="ScanOffloadTest._pair"></a>`ScanOffloadTest._pair` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L103)
- <a id="ScanOffloadTest.graph"></a>`ScanOffloadTest.graph` — [`L90`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L90)
- <a id="ScanOffloadTest.root"></a>`ScanOffloadTest.root` — [`L89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L89)
- <a id="ScanOffloadTest.setUp"></a>`ScanOffloadTest.setUp` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L87)
- <a id="ScanOffloadTest.test_a_body_that_reads_the_stack_whole_is_left_on_device"></a>`ScanOffloadTest.test_a_body_that_reads_the_stack_whole_is_left_on_device` — [`L182`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L182)
- <a id="ScanOffloadTest.test_a_dead_reader_of_the_stack_does_not_block_the_offload"></a>`ScanOffloadTest.test_a_dead_reader_of_the_stack_does_not_block_the_offload` — [`L149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L149)
- <a id="ScanOffloadTest.test_a_graph_with_no_scan_at_all_is_an_error_not_a_quiet_no_op"></a>`ScanOffloadTest.test_a_graph_with_no_scan_at_all_is_an_error_not_a_quiet_no_op` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L195)
- <a id="ScanOffloadTest.test_a_live_second_reader_leaves_the_stack_on_device"></a>`ScanOffloadTest.test_a_live_second_reader_leaves_the_stack_on_device` — [`L166`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L166)
- <a id="ScanOffloadTest.test_the_offload_goes_in_the_forward_body_and_the_reload_in_the_backward"></a>`ScanOffloadTest.test_the_offload_goes_in_the_forward_body_and_the_reload_in_the_backward` — [`L127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L127)
- <a id="ScanOffloadTest.x"></a>`ScanOffloadTest.x` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L91)
- <a id="_AO"></a>`_AO` — [`L31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L31)
- <a id="_OFFLOAD"></a>`_OFFLOAD` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L29)
- <a id="_RELOAD"></a>`_RELOAD` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L30)
- <a id="_ROW"></a>`_ROW` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L34)
- <a id="_SCAN"></a>`_SCAN` — [`L28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L28)
- <a id="_STACK"></a>`_STACK` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L33)
- <a id="_ao_targets"></a>`_ao_targets` — [`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L37)
- <a id="_body_of"></a>`_body_of` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L41)
- <a id="_bwd_body"></a>`_bwd_body` — [`L65`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L65)
- <a id="_fwd_body"></a>`_fwd_body` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L55)
- <a id="_mm"></a>`_mm` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_host_offload.py#L45)
