---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer.tests.test_dtensor_parallelize_distributed`/
symbols:
  _verify_simple_fsdp_training_loop_worker.apply_simple_fsdp: _verify_simple_fsdp_training_loop_worker().apply_simple_fsdp().
  _verify_fsdp_training_loop_worker: _verify_fsdp_training_loop_worker().
  _verify_simple_fsdp_training_loop_worker: _verify_simple_fsdp_training_loop_worker().
  _tp_wrapper.apply_tp: _tp_wrapper().apply_tp().
  _verify_tp_forward_worker: _verify_tp_forward_worker().
  _verify_tp_backward_worker: _verify_tp_backward_worker().
  _parallel_dims: _parallel_dims().
  _verify_fsdp_training_loop_worker.apply_fsdp: _verify_fsdp_training_loop_worker().apply_fsdp().
  _get_model_config: _get_model_config().
  MuseGlimmerParallelizeTest.test_tp_forward_equivalence_distributed: MuseGlimmerParallelizeTest#test_tp_forward_equivalence_distributed().
  MuseGlimmerParallelizeTest._run: MuseGlimmerParallelizeTest#_run().
  MuseGlimmerParallelizeTest.test_tp_backward_equivalence_distributed: MuseGlimmerParallelizeTest#test_tp_backward_equivalence_distributed().
  MuseGlimmerParallelizeTest.test_fsdp_full_training_loop_equivalence_distributed: MuseGlimmerParallelizeTest#test_fsdp_full_training_loop_equivalence_distributed().
  MuseGlimmerParallelizeTest.test_simple_fsdp_full_training_loop_equivalence_distributed: MuseGlimmerParallelizeTest#test_simple_fsdp_full_training_loop_equivalence_distributed().
  _tp_wrapper: _tp_wrapper().
  TEST_BATCH_SIZE: TEST_BATCH_SIZE.
  TEST_SEQ_LEN: TEST_SEQ_LEN.
  MuseGlimmerParallelizeTest: MuseGlimmerParallelizeTest#
  TEST_TRAINING_STEPS: TEST_TRAINING_STEPS.
  _gather_dtensor_output: _gather_dtensor_output().
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py)

> **Collapsed catalog** (20 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="MuseGlimmerParallelizeTest"></a>`MuseGlimmerParallelizeTest` — [`L205`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L205)
- <a id="MuseGlimmerParallelizeTest._run"></a>`MuseGlimmerParallelizeTest._run` — [`L210`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L210)
- <a id="MuseGlimmerParallelizeTest.test_fsdp_full_training_loop_equivalence_distributed"></a>`MuseGlimmerParallelizeTest.test_fsdp_full_training_loop_equivalence_distributed` — [`L235`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L235)
- <a id="MuseGlimmerParallelizeTest.test_simple_fsdp_full_training_loop_equivalence_distributed"></a>`MuseGlimmerParallelizeTest.test_simple_fsdp_full_training_loop_equivalence_distributed` — [`L238`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L238)
- <a id="MuseGlimmerParallelizeTest.test_tp_backward_equivalence_distributed"></a>`MuseGlimmerParallelizeTest.test_tp_backward_equivalence_distributed` — [`L232`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L232)
- <a id="MuseGlimmerParallelizeTest.test_tp_forward_equivalence_distributed"></a>`MuseGlimmerParallelizeTest.test_tp_forward_equivalence_distributed` — [`L223`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L223)
- <a id="TEST_BATCH_SIZE"></a>`TEST_BATCH_SIZE` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L23)
- <a id="TEST_SEQ_LEN"></a>`TEST_SEQ_LEN` — [`L25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L25)
- <a id="TEST_TRAINING_STEPS"></a>`TEST_TRAINING_STEPS` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L26)
- <a id="_gather_dtensor_output"></a>`_gather_dtensor_output` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L55)
- <a id="_get_model_config"></a>`_get_model_config` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L29)
- <a id="_parallel_dims"></a>`_parallel_dims` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L43)
- <a id="_tp_wrapper"></a>`_tp_wrapper` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L67)
- <a id="_tp_wrapper.apply_tp"></a>`_tp_wrapper.apply_tp` — [`L68`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L68)
- <a id="_verify_fsdp_training_loop_worker"></a>`_verify_fsdp_training_loop_worker` — [`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L122)
- <a id="_verify_fsdp_training_loop_worker.apply_fsdp"></a>`_verify_fsdp_training_loop_worker.apply_fsdp` — [`L127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L127)
- <a id="_verify_simple_fsdp_training_loop_worker"></a>`_verify_simple_fsdp_training_loop_worker` — [`L161`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L161)
- <a id="_verify_simple_fsdp_training_loop_worker.apply_simple_fsdp"></a>`_verify_simple_fsdp_training_loop_worker.apply_simple_fsdp` — [`L166`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L166)
- <a id="_verify_tp_backward_worker"></a>`_verify_tp_backward_worker` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L101)
- <a id="_verify_tp_forward_worker"></a>`_verify_tp_forward_worker` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/tests/test_dtensor_parallelize_distributed.py#L86)
