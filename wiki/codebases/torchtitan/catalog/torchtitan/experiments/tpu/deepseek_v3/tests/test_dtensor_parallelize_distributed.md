---
title: 'Module: torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.deepseek_v3.tests.test_dtensor_parallelize_distributed`/
symbols:
  _verify_dtensor_deepseek_v3_non_moe_tp_forward_worker.apply_tp_wrapper: _verify_dtensor_deepseek_v3_non_moe_tp_forward_worker().apply_tp_wrapper().
  _verify_dtensor_deepseek_v3_tp_backward_worker.apply_tp_wrapper: _verify_dtensor_deepseek_v3_tp_backward_worker().apply_tp_wrapper().
  _verify_dtensor_deepseek_v3_fsdp_training_loop_worker.apply_fsdp_wrapper: _verify_dtensor_deepseek_v3_fsdp_training_loop_worker().apply_fsdp_wrapper().
  _verify_dtensor_deepseek_v3_tp_backward_worker: _verify_dtensor_deepseek_v3_tp_backward_worker().
  _verify_dtensor_deepseek_v3_fsdp_training_loop_worker: _verify_dtensor_deepseek_v3_fsdp_training_loop_worker().
  _verify_dtensor_deepseek_v3_non_moe_tp_forward_worker: _verify_dtensor_deepseek_v3_non_moe_tp_forward_worker().
  _get_deepseek_v3_model_config: _get_deepseek_v3_model_config().
  DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed: DeepSeekV3DTensorParallelizeTest#test_apply_non_moe_tp_forward_equivalence_distributed().
  DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed: DeepSeekV3DTensorParallelizeTest#test_apply_non_moe_tp_backward_equivalence_distributed().
  DeepSeekV3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed: DeepSeekV3DTensorParallelizeTest#test_apply_fsdp_full_training_loop_equivalence_distributed().
  TEST_BATCH_SIZE: TEST_BATCH_SIZE.
  TEST_SEQ_LEN: TEST_SEQ_LEN.
  DeepSeekV3DTensorParallelizeTest: DeepSeekV3DTensorParallelizeTest#
  TEST_TRAINING_STEPS: TEST_TRAINING_STEPS.
---
# Module: [`torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py)

> **Collapsed catalog** (14 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="DeepSeekV3DTensorParallelizeTest"></a>`DeepSeekV3DTensorParallelizeTest` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L193)
- <a id="DeepSeekV3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed"></a>`DeepSeekV3DTensorParallelizeTest.test_apply_fsdp_full_training_loop_equivalence_distributed` — [`L229`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L229)
- <a id="DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed"></a>`DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_backward_equivalence_distributed` — [`L214`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L214)
- <a id="DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed"></a>`DeepSeekV3DTensorParallelizeTest.test_apply_non_moe_tp_forward_equivalence_distributed` — [`L199`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L199)
- <a id="TEST_BATCH_SIZE"></a>`TEST_BATCH_SIZE` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L23)
- <a id="TEST_SEQ_LEN"></a>`TEST_SEQ_LEN` — [`L27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L27)
- <a id="TEST_TRAINING_STEPS"></a>`TEST_TRAINING_STEPS` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L30)
- <a id="_get_deepseek_v3_model_config"></a>`_get_deepseek_v3_model_config` — [`L33`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L33)
- <a id="_verify_dtensor_deepseek_v3_fsdp_training_loop_worker"></a>`_verify_dtensor_deepseek_v3_fsdp_training_loop_worker` — [`L140`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L140)
- <a id="_verify_dtensor_deepseek_v3_fsdp_training_loop_worker.apply_fsdp_wrapper"></a>`_verify_dtensor_deepseek_v3_fsdp_training_loop_worker.apply_fsdp_wrapper` — [`L149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L149)
- <a id="_verify_dtensor_deepseek_v3_non_moe_tp_forward_worker"></a>`_verify_dtensor_deepseek_v3_non_moe_tp_forward_worker` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L44)
- <a id="_verify_dtensor_deepseek_v3_non_moe_tp_forward_worker.apply_tp_wrapper"></a>`_verify_dtensor_deepseek_v3_non_moe_tp_forward_worker.apply_tp_wrapper` — [`L51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L51)
- <a id="_verify_dtensor_deepseek_v3_tp_backward_worker"></a>`_verify_dtensor_deepseek_v3_tp_backward_worker` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L87)
- <a id="_verify_dtensor_deepseek_v3_tp_backward_worker.apply_tp_wrapper"></a>`_verify_dtensor_deepseek_v3_tp_backward_worker.apply_tp_wrapper` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/deepseek_v3/tests/test_dtensor_parallelize_distributed.py#L94)
