---
title: 'Module: src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.collectives.all_gather_matmul`/
symbols:
  all_gather_matmul: all_gather_matmul().
  _all_gather_kernel.debug_print: _all_gather_kernel().debug_print().
  _all_gather_kernel._start_or_wait_copy: _all_gather_kernel()._start_or_wait_copy().
  _all_gather_kernel._start_first_remote_copy: _all_gather_kernel()._start_first_remote_copy().
  _all_gather_kernel._do_first_x_local_copy: _all_gather_kernel()._do_first_x_local_copy().
  _all_gather_kernel._do_subsequent_x_left_local_copy: _all_gather_kernel()._do_subsequent_x_left_local_copy().
  _all_gather_kernel._do_subsequent_x_right_local_copy: _all_gather_kernel()._do_subsequent_x_right_local_copy().
  _all_gather_kernel._do_y_local_copy: _all_gather_kernel()._do_y_local_copy().
  _all_gather_kernel._do_first_left_remote_copy: _all_gather_kernel()._do_first_left_remote_copy().
  _all_gather_kernel._do_first_right_remote_copy: _all_gather_kernel()._do_first_right_remote_copy().
  _all_gather_kernel._do_subsequent_left_remote_copy: _all_gather_kernel()._do_subsequent_left_remote_copy().
  _all_gather_kernel._do_subsequent_right_remote_copy: _all_gather_kernel()._do_subsequent_right_remote_copy().
  _all_gather_kernel._do_o_local_copy: _all_gather_kernel()._do_o_local_copy().
  all_gather_matmul._all_gather_matmul_call: all_gather_matmul()._all_gather_matmul_call().
  _all_gather_kernel._start_subsequent_remote_copy: _all_gather_kernel()._start_subsequent_remote_copy().
  _all_gather_kernel._start_subsequent_x_local_copy: _all_gather_kernel()._start_subsequent_x_local_copy().
  _all_gather_kernel._start_o_local_copy: _all_gather_kernel()._start_o_local_copy().
  _all_gather_kernel._wait_o_local_copy: _all_gather_kernel()._wait_o_local_copy().
  _all_gather_kernel._wait_subsequent_x_local_copy: _all_gather_kernel()._wait_subsequent_x_local_copy().
  _all_gather_kernel._wait_first_remote_copy: _all_gather_kernel()._wait_first_remote_copy().
  _all_gather_kernel._wait_subsequent_remote_copy: _all_gather_kernel()._wait_subsequent_remote_copy().
  P: P.
  _all_gather_kernel: _all_gather_kernel().
  _all_gather_kernel._do_mxu: _all_gather_kernel()._do_mxu().
  _all_gather_kernel._do_mxu._update: _all_gather_kernel()._do_mxu()._update().
  _all_gather_kernel._start_first_x_local_copy: _all_gather_kernel()._start_first_x_local_copy().
  _all_gather_kernel._start_y_local_copy: _all_gather_kernel()._start_y_local_copy().
  _all_gather_kernel._mxu: _all_gather_kernel()._mxu().
  _all_gather_kernel._wait_y_local_copy: _all_gather_kernel()._wait_y_local_copy().
  _all_gather_kernel._wait_first_x_local_copy: _all_gather_kernel()._wait_first_x_local_copy().
  _cdiv: _cdiv().
  _all_gather_kernel._get_start_o_local_copy_cond: _all_gather_kernel()._get_start_o_local_copy_cond().
  _all_gather_kernel._get_wait_o_local_copy_cond: _all_gather_kernel()._get_wait_o_local_copy_cond().
  get_vmem_estimate_bytes: get_vmem_estimate_bytes().
  validate_inputs: validate_inputs().
  get_kernel_name: get_kernel_name().
  _all_gather_kernel.debug_print._debug_print: _all_gather_kernel().debug_print()._debug_print().
---
# Module: [`src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py)

## Functions
- <a id="_all_gather_kernel"></a>`_all_gather_kernel(x_hbm_ref, y_hbm_ref, o_hbm_ref, x_hbm_scratch_ref, x_local_copy_sem, y_local_copy_sem, o_local_copy_sem, send_sems, recv_sems, x_vmem_scratch_ref, y_vmem_scratch_ref, o_vmem_scratch_ref, acc_vmem_scratch_ref, axis_name: str, bn: int, bk: int, debug_mode=False, rhs_transpose: bool = False)` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L43) — Pallas kernel for all-gather.
- <a id="all_gather_matmul._all_gather_matmul_call"></a>`_all_gather_matmul_call(x, y, bn, bk, rhs_transpose)` — [`L705`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L705)
- <a id="_cdiv"></a>`_cdiv(x, y)` — [`L30`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L30)
- <a id="_all_gather_kernel.debug_print._debug_print"></a>`_debug_print()` — [`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L108)
- <a id="_all_gather_kernel._do_first_left_remote_copy"></a>`_do_first_left_remote_copy(wait: bool = False)` — [`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L208)
- <a id="_all_gather_kernel._do_first_right_remote_copy"></a>`_do_first_right_remote_copy(wait: bool = False)` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L228)
- <a id="_all_gather_kernel._do_first_x_local_copy"></a>`_do_first_x_local_copy(wait: bool = False)` — [`L120`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L120)
- <a id="_all_gather_kernel._do_mxu"></a>`_do_mxu()` — [`L292`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L292)
- <a id="_all_gather_kernel._do_o_local_copy"></a>`_do_o_local_copy(wait: bool = False)` — [`L367`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L367)
- <a id="_all_gather_kernel._do_subsequent_left_remote_copy"></a>`_do_subsequent_left_remote_copy(wait: bool = False)` — [`L248`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L248)
- <a id="_all_gather_kernel._do_subsequent_right_remote_copy"></a>`_do_subsequent_right_remote_copy(wait: bool = False)` — [`L270`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L270)
- <a id="_all_gather_kernel._do_subsequent_x_left_local_copy"></a>`_do_subsequent_x_left_local_copy(wait: bool = False)` — [`L136`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L136)
- <a id="_all_gather_kernel._do_subsequent_x_right_local_copy"></a>`_do_subsequent_x_right_local_copy(wait: bool = False)` — [`L161`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L161)
- <a id="_all_gather_kernel._do_y_local_copy"></a>`_do_y_local_copy(wait: bool = False)` — [`L185`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L185)
- <a id="_all_gather_kernel._get_start_o_local_copy_cond"></a>`_get_start_o_local_copy_cond()` — [`L462`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L462)
- <a id="_all_gather_kernel._get_wait_o_local_copy_cond"></a>`_get_wait_o_local_copy_cond()` — [`L486`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L486)
- <a id="_all_gather_kernel._mxu"></a>`_mxu()` — [`L483`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L483)
- <a id="_all_gather_kernel._start_first_remote_copy"></a>`_start_first_remote_copy()` — [`L422`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L422)
- <a id="_all_gather_kernel._start_first_x_local_copy"></a>`_start_first_x_local_copy()` — [`L444`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L444)
- <a id="_all_gather_kernel._start_o_local_copy"></a>`_start_o_local_copy()` — [`L478`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L478)
- <a id="_all_gather_kernel._start_or_wait_copy"></a>`_start_or_wait_copy(op: jax._src.pallas.mosaic.primitives.AsyncCopyDescriptor, wait: bool = False)` — [`L111`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L111)
- <a id="_all_gather_kernel._start_subsequent_remote_copy"></a>`_start_subsequent_remote_copy()` — [`L438`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L438)
- <a id="_all_gather_kernel._start_subsequent_x_local_copy"></a>`_start_subsequent_x_local_copy()` — [`L453`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L453)
- <a id="_all_gather_kernel._start_y_local_copy"></a>`_start_y_local_copy()` — [`L459`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L459)
- <a id="_all_gather_kernel._do_mxu._update"></a>`_update()` — [`L342`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L342)
- <a id="_all_gather_kernel._wait_first_remote_copy"></a>`_wait_first_remote_copy()` — [`L523`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L523)
- <a id="_all_gather_kernel._wait_first_x_local_copy"></a>`_wait_first_x_local_copy()` — [`L512`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L512)
- <a id="_all_gather_kernel._wait_o_local_copy"></a>`_wait_o_local_copy()` — [`L502`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L502)
- <a id="_all_gather_kernel._wait_subsequent_remote_copy"></a>`_wait_subsequent_remote_copy()` — [`L534`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L534)
- <a id="_all_gather_kernel._wait_subsequent_x_local_copy"></a>`_wait_subsequent_x_local_copy()` — [`L517`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L517)
- <a id="_all_gather_kernel._wait_y_local_copy"></a>`_wait_y_local_copy()` — [`L507`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L507)
- <a id="all_gather_matmul"></a>`all_gather_matmul(x: jax.Array, y: jax.Array, mesh: jax.sharding.AbstractMesh, axis_name: str, collective_id: int | None = 0, bn: int | None = None, bk: int | None = None, rhs_transpose: bool = False)` — [`L604`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L604) — Performs all-gather on the input tensor and then a matmul.
- <a id="_all_gather_kernel.debug_print"></a>`debug_print(msg, *args)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L104)
- <a id="get_kernel_name"></a>`get_kernel_name(bn: int, bk: int, rhs_transpose: bool)` — [`L742`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L742)
- <a id="get_vmem_estimate_bytes"></a>`get_vmem_estimate_bytes(m, n, k, bn, acc_bytes, tp_size, x_dtype, y_dtype, out_dtype)` — [`L542`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L542) — Returns the total vmem bytes used by the kernel.
- <a id="validate_inputs"></a>`validate_inputs(x, y, tp_size, rhs_transpose=False)` — [`L566`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L566) — Validates the inputs to the all_gather_matmul kernel.

## Module values
- <a id="P"></a>`P` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/collectives/all_gather_matmul.py#L27)

