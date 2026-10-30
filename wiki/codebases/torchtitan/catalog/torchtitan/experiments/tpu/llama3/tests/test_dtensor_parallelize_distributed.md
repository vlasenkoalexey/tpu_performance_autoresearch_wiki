---
title: 'Module: torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.llama3.tests.test_dtensor_parallelize_distributed`/
symbols:
  _verify_dtensor_llama3_tp_forward_worker.apply_tp_wrapper: _verify_dtensor_llama3_tp_forward_worker().apply_tp_wrapper().
  _verify_dtensor_llama3_tp_backward_worker.apply_tp_wrapper: _verify_dtensor_llama3_tp_backward_worker().apply_tp_wrapper().
  _verify_dtensor_llama3_fsdp_training_loop_worker.apply_fsdp_wrapper: _verify_dtensor_llama3_fsdp_training_loop_worker().apply_fsdp_wrapper().
  _verify_dtensor_llama3_fsdp_training_loop_worker: _verify_dtensor_llama3_fsdp_training_loop_worker().
  _verify_dtensor_llama3_tp_forward_worker: _verify_dtensor_llama3_tp_forward_worker().
  _verify_dtensor_llama3_tp_backward_worker: _verify_dtensor_llama3_tp_backward_worker().
  _get_model_config: _get_model_config().
  Llama3DTensorParallelizeTest.test_dtensor_issue_distributed: Llama3DTensorParallelizeTest#test_dtensor_issue_distributed().
  Llama3DTensorParallelizeTest.test_apply_tp_forward_equivalence_distributed: Llama3DTensorParallelizeTest#test_apply_tp_forward_equivalence_distributed().
  Llama3DTensorParallelizeTest.test_apply_tp_backward_equivalence_distributed: Llama3DTensorParallelizeTest#test_apply_tp_backward_equivalence_distributed().
  Llama3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed: Llama3DTensorParallelizeTest#test_apply_fsdp_full_training_loop_equivalence_distributed().
  _dtensor_issue_worker: _dtensor_issue_worker().
  TEST_BATCH_SIZE: TEST_BATCH_SIZE.
  _dtensor_issue_worker.SimpleModel.forward: _dtensor_issue_worker().SimpleModel#forward().
  Llama3DTensorParallelizeTest: Llama3DTensorParallelizeTest#
  TEST_TRAINING_STEPS: TEST_TRAINING_STEPS.
  _dtensor_issue_worker.SimpleModel: _dtensor_issue_worker().SimpleModel#
  SimpleModel.output: SimpleModel#output.
  _dtensor_issue_worker.SimpleModel.__init__: _dtensor_issue_worker().SimpleModel#__init__().
---
# Module: [`torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py)

> **Collapsed catalog** (19 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Llama3DTensorParallelizeTest"></a>`Llama3DTensorParallelizeTest` — [`L237`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L237)
- <a id="Llama3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed"></a>`Llama3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed` — [`L286`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L286)
- <a id="Llama3DTensorParallelizeTest.test_apply_tp_backward_equivalence_distributed"></a>`Llama3DTensorParallelizeTest.test_apply_tp_backward_equivalence_distributed` — [`L271`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L271)
- <a id="Llama3DTensorParallelizeTest.test_apply_tp_forward_equivalence_distributed"></a>`Llama3DTensorParallelizeTest.test_apply_tp_forward_equivalence_distributed` — [`L255`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L255)
- <a id="Llama3DTensorParallelizeTest.test_dtensor_issue_distributed"></a>`Llama3DTensorParallelizeTest.test_dtensor_issue_distributed` — [`L242`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L242)
- <a id="SimpleModel.output"></a>`SimpleModel.output` — [`L205`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L205)
- <a id="TEST_BATCH_SIZE"></a>`TEST_BATCH_SIZE` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L29)
- <a id="TEST_TRAINING_STEPS"></a>`TEST_TRAINING_STEPS` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L35)
- <a id="_dtensor_issue_worker"></a>`_dtensor_issue_worker` — [`L199`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L199)
- <a id="_dtensor_issue_worker.SimpleModel"></a>`_dtensor_issue_worker.SimpleModel` — [`L201`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L201)
- <a id="_dtensor_issue_worker.SimpleModel.__init__"></a>`_dtensor_issue_worker.SimpleModel.__init__` — [`L203`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L203)
- <a id="_dtensor_issue_worker.SimpleModel.forward"></a>`_dtensor_issue_worker.SimpleModel.forward` — [`L207`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L207)
- <a id="_get_model_config"></a>`_get_model_config` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L38)
- <a id="_verify_dtensor_llama3_fsdp_training_loop_worker"></a>`_verify_dtensor_llama3_fsdp_training_loop_worker` — [`L147`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L147)
- <a id="_verify_dtensor_llama3_fsdp_training_loop_worker.apply_fsdp_wrapper"></a>`_verify_dtensor_llama3_fsdp_training_loop_worker.apply_fsdp_wrapper` — [`L153`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L153)
- <a id="_verify_dtensor_llama3_tp_backward_worker"></a>`_verify_dtensor_llama3_tp_backward_worker` — [`L95`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L95)
- <a id="_verify_dtensor_llama3_tp_backward_worker.apply_tp_wrapper"></a>`_verify_dtensor_llama3_tp_backward_worker.apply_tp_wrapper` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L101)
- <a id="_verify_dtensor_llama3_tp_forward_worker"></a>`_verify_dtensor_llama3_tp_forward_worker` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L47)
- <a id="_verify_dtensor_llama3_tp_forward_worker.apply_tp_wrapper"></a>`_verify_dtensor_llama3_tp_forward_worker.apply_tp_wrapper` — [`L53`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/llama3/tests/test_dtensor_parallelize_distributed.py#L53)
