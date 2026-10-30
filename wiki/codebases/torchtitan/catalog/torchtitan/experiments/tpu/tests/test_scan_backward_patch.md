---
title: 'Module: torchtitan/experiments/tpu/tests/test_scan_backward_patch.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/tests/test_scan_backward_patch.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.tests.test_scan_backward_patch`/
symbols:
  ScanBackwardPatchTest._backward: ScanBackwardPatchTest#_backward().
  ScanBackwardPatchTest.test_it_launches_its_scan_with_torch_s_own_names: ScanBackwardPatchTest#test_it_launches_its_scan_with_torch_s_own_names().
  ScanBackwardPatchTest._install_fake_bump: ScanBackwardPatchTest#_install_fake_bump().
  ScanBackwardPatchTest._backend: ScanBackwardPatchTest#_backend.
  ScanBackwardPatchTest.test_it_asks_torch_tpu_for_a_reverse_loop_without_index_copy: ScanBackwardPatchTest#test_it_asks_torch_tpu_for_a_reverse_loop_without_index_copy().
  ScanBackwardPatchTest.test_it_absorbs_an_upstream_change_that_is_not_the_reversal: ScanBackwardPatchTest#test_it_absorbs_an_upstream_change_that_is_not_the_reversal().
  ScanBackwardPatchTest.test_it_raises_rather_than_reverse_by_copy: ScanBackwardPatchTest#test_it_raises_rather_than_reverse_by_copy().
  ScanBackwardPatchTest.test_it_refuses_to_install_when_the_source_says_the_fix_landed: ScanBackwardPatchTest#test_it_refuses_to_install_when_the_source_says_the_fix_landed().
  ScanBackwardPatchTest.test_it_raises_when_a_flip_is_added_before_the_scan: ScanBackwardPatchTest#test_it_raises_when_a_flip_is_added_before_the_scan().
  ScanBackwardPatchTest.test_it_does_not_swallow_a_flip_added_after_the_scan: ScanBackwardPatchTest#test_it_does_not_swallow_a_flip_added_after_the_scan().
  ScanBackwardPatchTest.test_it_falls_back_on_a_device_that_ignores_the_reverse_request: ScanBackwardPatchTest#test_it_falls_back_on_a_device_that_ignores_the_reverse_request().
  _SCAN_MODULE: _SCAN_MODULE.
  ScanBackwardPatchTest._unpatched: ScanBackwardPatchTest#_unpatched.
  ScanBackwardPatchTest.test_it_removes_the_flips_and_leaves_the_gradients_alone: ScanBackwardPatchTest#test_it_removes_the_flips_and_leaves_the_gradients_alone().
  ScanBackwardPatchTest.test_the_gradients_depend_on_torch_tpu_reversing_the_loop: ScanBackwardPatchTest#test_the_gradients_depend_on_torch_tpu_reversing_the_loop().
  ScanBackwardPatchTest.test_it_refuses_to_install_over_someone_else: ScanBackwardPatchTest#test_it_refuses_to_install_over_someone_else().
  ScanBackwardPatchTest._record_rewritten_scans: ScanBackwardPatchTest#_record_rewritten_scans().
  ScanBackwardPatchTest.recording: ScanBackwardPatchTest#recording().
  _scan_of_tanh: _scan_of_tanh().
  ScanBackwardPatchTest.no_longer_flips: ScanBackwardPatchTest#no_longer_flips().
  _RecordOps.__torch_dispatch__: _RecordOps#__torch_dispatch__().
  ScanBackwardPatchTest: ScanBackwardPatchTest#
  ScanBackwardPatchTest.setUp: ScanBackwardPatchTest#setUp().
  _RecordOps.ops: _RecordOps#ops.
  ScanBackwardPatchTest.not_the_method: ScanBackwardPatchTest#not_the_method().
  _body: _body().
  _RecordOps: _RecordOps#
  _RecordOps.supports_higher_order_operators: _RecordOps#supports_higher_order_operators.
  _RecordOps.__init__: _RecordOps#__init__().
---
# Module: [`torchtitan/experiments/tpu/tests/test_scan_backward_patch.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py)

> **Collapsed catalog** (29 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="ScanBackwardPatchTest"></a>`ScanBackwardPatchTest` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L65)
- <a id="ScanBackwardPatchTest._backend"></a>`ScanBackwardPatchTest._backend` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L80)
- <a id="ScanBackwardPatchTest._backward"></a>`ScanBackwardPatchTest._backward` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L86)
- <a id="ScanBackwardPatchTest._install_fake_bump"></a>`ScanBackwardPatchTest._install_fake_bump` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L100)
- <a id="ScanBackwardPatchTest._record_rewritten_scans"></a>`ScanBackwardPatchTest._record_rewritten_scans` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L137)
- <a id="ScanBackwardPatchTest._unpatched"></a>`ScanBackwardPatchTest._unpatched` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L69)
- <a id="ScanBackwardPatchTest.no_longer_flips"></a>`ScanBackwardPatchTest.no_longer_flips` — [`L282`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L282)
- <a id="ScanBackwardPatchTest.not_the_method"></a>`ScanBackwardPatchTest.not_the_method` — [`L291`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L291)
- <a id="ScanBackwardPatchTest.recording"></a>`ScanBackwardPatchTest.recording` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L142)
- <a id="ScanBackwardPatchTest.setUp"></a>`ScanBackwardPatchTest.setUp` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L67)
- <a id="ScanBackwardPatchTest.test_it_absorbs_an_upstream_change_that_is_not_the_reversal"></a>`ScanBackwardPatchTest.test_it_absorbs_an_upstream_change_that_is_not_the_reversal` — [`L230`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L230)
- <a id="ScanBackwardPatchTest.test_it_asks_torch_tpu_for_a_reverse_loop_without_index_copy"></a>`ScanBackwardPatchTest.test_it_asks_torch_tpu_for_a_reverse_loop_without_index_copy` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L151)
- <a id="ScanBackwardPatchTest.test_it_does_not_swallow_a_flip_added_after_the_scan"></a>`ScanBackwardPatchTest.test_it_does_not_swallow_a_flip_added_after_the_scan` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L316)
- <a id="ScanBackwardPatchTest.test_it_falls_back_on_a_device_that_ignores_the_reverse_request"></a>`ScanBackwardPatchTest.test_it_falls_back_on_a_device_that_ignores_the_reverse_request` — [`L334`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L334)
- <a id="ScanBackwardPatchTest.test_it_launches_its_scan_with_torch_s_own_names"></a>`ScanBackwardPatchTest.test_it_launches_its_scan_with_torch_s_own_names` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L199)
- <a id="ScanBackwardPatchTest.test_it_raises_rather_than_reverse_by_copy"></a>`ScanBackwardPatchTest.test_it_raises_rather_than_reverse_by_copy` — [`L261`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L261)
- <a id="ScanBackwardPatchTest.test_it_raises_when_a_flip_is_added_before_the_scan"></a>`ScanBackwardPatchTest.test_it_raises_when_a_flip_is_added_before_the_scan` — [`L298`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L298)
- <a id="ScanBackwardPatchTest.test_it_refuses_to_install_over_someone_else"></a>`ScanBackwardPatchTest.test_it_refuses_to_install_over_someone_else` — [`L290`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L290)
- <a id="ScanBackwardPatchTest.test_it_refuses_to_install_when_the_source_says_the_fix_landed"></a>`ScanBackwardPatchTest.test_it_refuses_to_install_when_the_source_says_the_fix_landed` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L279)
- <a id="ScanBackwardPatchTest.test_it_removes_the_flips_and_leaves_the_gradients_alone"></a>`ScanBackwardPatchTest.test_it_removes_the_flips_and_leaves_the_gradients_alone` — [`L118`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L118)
- <a id="ScanBackwardPatchTest.test_the_gradients_depend_on_torch_tpu_reversing_the_loop"></a>`ScanBackwardPatchTest.test_the_gradients_depend_on_torch_tpu_reversing_the_loop` — [`L176`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L176)
- <a id="_RecordOps"></a>`_RecordOps` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L50)
- <a id="_RecordOps.__init__"></a>`_RecordOps.__init__` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L56)
- <a id="_RecordOps.__torch_dispatch__"></a>`_RecordOps.__torch_dispatch__` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L60)
- <a id="_RecordOps.ops"></a>`_RecordOps.ops` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L58)
- <a id="_RecordOps.supports_higher_order_operators"></a>`_RecordOps.supports_higher_order_operators` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L54)
- <a id="_SCAN_MODULE"></a>`_SCAN_MODULE` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L36)
- <a id="_body"></a>`_body` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L39)
- <a id="_scan_of_tanh"></a>`_scan_of_tanh` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/tests/test_scan_backward_patch.py#L45)
