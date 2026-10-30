---
title: 'Module: torchtitan/experiments/tpu/base_distributed_device_test.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/base_distributed_device_test.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.base_distributed_device_test`/
symbols:
  BaseDistributedDeviceTest: BaseDistributedDeviceTest#
  BaseDistributedDeviceTest.accelerator_device_type: BaseDistributedDeviceTest#accelerator_device_type.
  _run_cpu_verification: _run_cpu_verification().
  BaseDistributedDeviceTest._test_train_distributed: BaseDistributedDeviceTest#_test_train_distributed().
  DistributedUnitTestRunner.run_backward_parity: DistributedUnitTestRunner#run_backward_parity().
  BaseDistributedDeviceTest.num_devices: BaseDistributedDeviceTest#num_devices.
  DistributedUnitTestRunner.run_forward_parity: DistributedUnitTestRunner#run_forward_parity().
  InputDistribution: InputDistribution#
  DistributedTrainWithRecorder.__call__: DistributedTrainWithRecorder#__call__().
  config_to_input_distribution: config_to_input_distribution().
  DistributedUnitTestRunner._get_local_batch_view: DistributedUnitTestRunner#_get_local_batch_view().
  BaseDistributedDeviceTest._run_trainer_distributed_parity_test: BaseDistributedDeviceTest#_run_trainer_distributed_parity_test().
  DistributedUnitTestRunner.parallel_model: DistributedUnitTestRunner#parallel_model.
  DistributedUnitTestRunner._create_parallel_model: DistributedUnitTestRunner#_create_parallel_model().
  DistributedUnitTestRunner._create_reference_from_parallel: DistributedUnitTestRunner#_create_reference_from_parallel().
  DistributedUnitTestRunner._check_gradients_against_recorded: DistributedUnitTestRunner#_check_gradients_against_recorded().
  DistributedUnitTestRunner: DistributedUnitTestRunner#
  InputDistribution.REPLICATE: InputDistribution#REPLICATE.
  DistributedUnitTestRunner.rank: DistributedUnitTestRunner#rank.
  _capture_distributed_state: _capture_distributed_state().
  _apply_cpu_splash_reference_patch: _apply_cpu_splash_reference_patch().
  DistributedUnitTestRunner.reference_model: DistributedUnitTestRunner#reference_model.
  InputDistribution.SPLIT_BATCH: InputDistribution#SPLIT_BATCH.
  DistributedUnitTestRunner._run_step: DistributedUnitTestRunner#_run_step().
  DistributedUnitTestRunner.__init__: DistributedUnitTestRunner#__init__().
  DistributedUnitTestRunner.current_step: DistributedUnitTestRunner#current_step.
  DistributedUnitTestRunner._generate_global_batch: DistributedUnitTestRunner#_generate_global_batch().
  DistributedUnitTestRunner.device: DistributedUnitTestRunner#device.
  DistributedUnitTestRunner._run_reference_model_pre_run: DistributedUnitTestRunner#_run_reference_model_pre_run().
  _apply_cpu_splash_reference_patch._splash_ref_forward: _apply_cpu_splash_reference_patch()._splash_ref_forward().
  DistributedUnitTestRunner.model_args: DistributedUnitTestRunner#model_args.
  _DistributedInitWrapper.__call__: _DistributedInitWrapper#__call__().
  DistributedUnitTestRunner._gather_weights_wrapper: DistributedUnitTestRunner#_gather_weights_wrapper().
  DistributedTrainWithRecorder.dist_capture_fn: DistributedTrainWithRecorder#dist_capture_fn().
  DistributedUnitTestRunner.input_distribution: DistributedUnitTestRunner#input_distribution.
  _gather_distributed_tensor: _gather_distributed_tensor().
  DistributedUnitTestRunner.model_class: DistributedUnitTestRunner#model_class.
  BaseDistributedDeviceTest.test_gpu_available: BaseDistributedDeviceTest#test_gpu_available().
  DistributedUnitTestRunner.world_size: DistributedUnitTestRunner#world_size.
  ParallelismFunc: ParallelismFunc.
  DistributedUnitTestRunner.use_meta_init: DistributedUnitTestRunner#use_meta_init.
  DistributedUnitTestRunner._gather_output_to_cpu: DistributedUnitTestRunner#_gather_output_to_cpu().
  _DistributedInitWrapper: _DistributedInitWrapper#
  _DistributedInitWrapper.fn: _DistributedInitWrapper#fn.
  DistributedTrainWithRecorder: DistributedTrainWithRecorder#
  DistributedTrainWithRecorder.output_path: DistributedTrainWithRecorder#output_path.
  _DistributedInitWrapper.__init__: _DistributedInitWrapper#__init__().
  DistributedTrainWithRecorder.__init__: DistributedTrainWithRecorder#__init__().
  BaseDistributedDeviceTest.setUp: BaseDistributedDeviceTest#setUp().
---
# Module: [`torchtitan/experiments/tpu/base_distributed_device_test.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py)

> **Collapsed catalog** (49 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="BaseDistributedDeviceTest"></a>`BaseDistributedDeviceTest` — [`L794`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L794)
- <a id="BaseDistributedDeviceTest._run_trainer_distributed_parity_test"></a>`BaseDistributedDeviceTest._run_trainer_distributed_parity_test` — [`L909`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L909)
- <a id="BaseDistributedDeviceTest._test_train_distributed"></a>`BaseDistributedDeviceTest._test_train_distributed` — [`L829`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L829)
- <a id="BaseDistributedDeviceTest.accelerator_device_type"></a>`BaseDistributedDeviceTest.accelerator_device_type` — [`L805`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L805)
- <a id="BaseDistributedDeviceTest.num_devices"></a>`BaseDistributedDeviceTest.num_devices` — [`L804`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L804)
- <a id="BaseDistributedDeviceTest.setUp"></a>`BaseDistributedDeviceTest.setUp` — [`L801`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L801)
- <a id="BaseDistributedDeviceTest.test_gpu_available"></a>`BaseDistributedDeviceTest.test_gpu_available` — [`L824`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L824)
- <a id="DistributedTrainWithRecorder"></a>`DistributedTrainWithRecorder` — [`L745`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L745)
- <a id="DistributedTrainWithRecorder.__call__"></a>`DistributedTrainWithRecorder.__call__` — [`L753`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L753)
- <a id="DistributedTrainWithRecorder.__init__"></a>`DistributedTrainWithRecorder.__init__` — [`L748`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L748)
- <a id="DistributedTrainWithRecorder.dist_capture_fn"></a>`DistributedTrainWithRecorder.dist_capture_fn` — [`L761`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L761)
- <a id="DistributedTrainWithRecorder.output_path"></a>`DistributedTrainWithRecorder.output_path` — [`L749`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L749)
- <a id="DistributedUnitTestRunner"></a>`DistributedUnitTestRunner` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L59)
- <a id="DistributedUnitTestRunner.__init__"></a>`DistributedUnitTestRunner.__init__` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L79)
- <a id="DistributedUnitTestRunner._check_gradients_against_recorded"></a>`DistributedUnitTestRunner._check_gradients_against_recorded` — [`L382`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L382)
- <a id="DistributedUnitTestRunner._create_parallel_model"></a>`DistributedUnitTestRunner._create_parallel_model` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L272)
- <a id="DistributedUnitTestRunner._create_reference_from_parallel"></a>`DistributedUnitTestRunner._create_reference_from_parallel` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L291)
- <a id="DistributedUnitTestRunner._gather_output_to_cpu"></a>`DistributedUnitTestRunner._gather_output_to_cpu` — [`L417`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L417)
- <a id="DistributedUnitTestRunner._gather_weights_wrapper"></a>`DistributedUnitTestRunner._gather_weights_wrapper` — [`L431`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L431)
- <a id="DistributedUnitTestRunner._generate_global_batch"></a>`DistributedUnitTestRunner._generate_global_batch` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L307)
- <a id="DistributedUnitTestRunner._get_local_batch_view"></a>`DistributedUnitTestRunner._get_local_batch_view` — [`L321`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L321)
- <a id="DistributedUnitTestRunner._run_reference_model_pre_run"></a>`DistributedUnitTestRunner._run_reference_model_pre_run` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L159)
- <a id="DistributedUnitTestRunner._run_step"></a>`DistributedUnitTestRunner._run_step` — [`L343`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L343)
- <a id="DistributedUnitTestRunner.current_step"></a>`DistributedUnitTestRunner.current_step` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L107)
- <a id="DistributedUnitTestRunner.device"></a>`DistributedUnitTestRunner.device` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L90)
- <a id="DistributedUnitTestRunner.input_distribution"></a>`DistributedUnitTestRunner.input_distribution` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L95)
- <a id="DistributedUnitTestRunner.model_args"></a>`DistributedUnitTestRunner.model_args` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L94)
- <a id="DistributedUnitTestRunner.model_class"></a>`DistributedUnitTestRunner.model_class` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L93)
- <a id="DistributedUnitTestRunner.parallel_model"></a>`DistributedUnitTestRunner.parallel_model` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L99)
- <a id="DistributedUnitTestRunner.rank"></a>`DistributedUnitTestRunner.rank` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L91)
- <a id="DistributedUnitTestRunner.reference_model"></a>`DistributedUnitTestRunner.reference_model` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L103)
- <a id="DistributedUnitTestRunner.run_backward_parity"></a>`DistributedUnitTestRunner.run_backward_parity` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L187)
- <a id="DistributedUnitTestRunner.run_forward_parity"></a>`DistributedUnitTestRunner.run_forward_parity` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L109)
- <a id="DistributedUnitTestRunner.use_meta_init"></a>`DistributedUnitTestRunner.use_meta_init` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L96)
- <a id="DistributedUnitTestRunner.world_size"></a>`DistributedUnitTestRunner.world_size` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L92)
- <a id="InputDistribution"></a>`InputDistribution` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L34)
- <a id="InputDistribution.REPLICATE"></a>`InputDistribution.REPLICATE` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L37)
- <a id="InputDistribution.SPLIT_BATCH"></a>`InputDistribution.SPLIT_BATCH` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L38)
- <a id="ParallelismFunc"></a>`ParallelismFunc` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L31)
- <a id="_DistributedInitWrapper"></a>`_DistributedInitWrapper` — [`L722`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L722)
- <a id="_DistributedInitWrapper.__call__"></a>`_DistributedInitWrapper.__call__` — [`L740`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L740)
- <a id="_DistributedInitWrapper.__init__"></a>`_DistributedInitWrapper.__init__` — [`L735`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L735)
- <a id="_DistributedInitWrapper.fn"></a>`_DistributedInitWrapper.fn` — [`L736`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L736)
- <a id="_apply_cpu_splash_reference_patch"></a>`_apply_cpu_splash_reference_patch` — [`L500`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L500)
- <a id="_apply_cpu_splash_reference_patch._splash_ref_forward"></a>`_apply_cpu_splash_reference_patch._splash_ref_forward` — [`L512`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L512)
- <a id="_capture_distributed_state"></a>`_capture_distributed_state` — [`L438`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L438)
- <a id="_gather_distributed_tensor"></a>`_gather_distributed_tensor` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L45)
- <a id="_run_cpu_verification"></a>`_run_cpu_verification` — [`L576`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L576)
- <a id="config_to_input_distribution"></a>`config_to_input_distribution` — [`L480`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/base_distributed_device_test.py#L480)
