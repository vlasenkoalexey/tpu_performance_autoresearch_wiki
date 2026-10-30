---
title: 'Module: torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.qwen3.tests.test_dtensor_parallelize_distributed`/
symbols:
  _verify_dtensor_qwen3_non_moe_tp_forward_worker.apply_tp_wrapper: _verify_dtensor_qwen3_non_moe_tp_forward_worker().apply_tp_wrapper().
  _verify_dtensor_qwen3_tp_backward_worker.apply_tp_wrapper: _verify_dtensor_qwen3_tp_backward_worker().apply_tp_wrapper().
  _verify_dtensor_qwen3_fsdp_training_loop_worker.apply_fsdp_wrapper: _verify_dtensor_qwen3_fsdp_training_loop_worker().apply_fsdp_wrapper().
  _verify_dtensor_qwen3_fsdp_training_loop_worker: _verify_dtensor_qwen3_fsdp_training_loop_worker().
  _verify_dtensor_qwen3_non_moe_tp_forward_worker: _verify_dtensor_qwen3_non_moe_tp_forward_worker().
  _verify_dtensor_qwen3_tp_backward_worker: _verify_dtensor_qwen3_tp_backward_worker().
  _get_qwen3_model_config: _get_qwen3_model_config().
  Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed: Qwen3DTensorParallelizeTest#test_apply_non_moe_tp_forward_equivalence_distributed().
  Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed: Qwen3DTensorParallelizeTest#test_apply_non_moe_tp_backward_equivalence_distributed().
  Qwen3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed: Qwen3DTensorParallelizeTest#test_apply_fsdp_full_training_loop_equivalence_distributed().
  TEST_BATCH_SIZE: TEST_BATCH_SIZE.
  TEST_SEQ_LEN: TEST_SEQ_LEN.
  Qwen3DTensorParallelizeTest: Qwen3DTensorParallelizeTest#
  TEST_TRAINING_STEPS: TEST_TRAINING_STEPS.
---
# Module: [`torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py)

> **Collapsed catalog** (14 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="Qwen3DTensorParallelizeTest"></a>`Qwen3DTensorParallelizeTest` — [`L181`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L181)
- <a id="Qwen3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed"></a>`Qwen3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed` — [`L216`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L216)
- <a id="Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed"></a>`Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed` — [`L201`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L201)
- <a id="Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed"></a>`Qwen3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed` — [`L186`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L186)
- <a id="TEST_BATCH_SIZE"></a>`TEST_BATCH_SIZE` — [`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L24)
- <a id="TEST_SEQ_LEN"></a>`TEST_SEQ_LEN` — [`L28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L28)
- <a id="TEST_TRAINING_STEPS"></a>`TEST_TRAINING_STEPS` — [`L31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L31)
- <a id="_get_qwen3_model_config"></a>`_get_qwen3_model_config` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L34)
- <a id="_verify_dtensor_qwen3_fsdp_training_loop_worker"></a>`_verify_dtensor_qwen3_fsdp_training_loop_worker` — [`L130`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L130)
- <a id="_verify_dtensor_qwen3_fsdp_training_loop_worker.apply_fsdp_wrapper"></a>`_verify_dtensor_qwen3_fsdp_training_loop_worker.apply_fsdp_wrapper` — [`L137`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L137)
- <a id="_verify_dtensor_qwen3_non_moe_tp_forward_worker"></a>`_verify_dtensor_qwen3_non_moe_tp_forward_worker` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L43)
- <a id="_verify_dtensor_qwen3_non_moe_tp_forward_worker.apply_tp_wrapper"></a>`_verify_dtensor_qwen3_non_moe_tp_forward_worker.apply_tp_wrapper` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L48)
- <a id="_verify_dtensor_qwen3_tp_backward_worker"></a>`_verify_dtensor_qwen3_tp_backward_worker` — [`L84`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L84)
- <a id="_verify_dtensor_qwen3_tp_backward_worker.apply_tp_wrapper"></a>`_verify_dtensor_qwen3_tp_backward_worker.apply_tp_wrapper` — [`L89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/qwen3/tests/test_dtensor_parallelize_distributed.py#L89)
