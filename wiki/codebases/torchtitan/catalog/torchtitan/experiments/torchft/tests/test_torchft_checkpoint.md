---
title: 'Module: torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.torchft.tests.test_torchft_checkpoint`/
symbols:
  TestFTCheckpointManager._build_replica: TestFTCheckpointManager#_build_replica().
  TestFTCheckpointManager.test_torchft_async_save_calls_maybe_wait_for_saving: TestFTCheckpointManager#test_torchft_async_save_calls_maybe_wait_for_saving().
  TestFTCheckpointManager._manager: TestFTCheckpointManager#_manager().
  TestFTCheckpointManager.test_load_restores_ft_checkpoint_before_main_checkpoint: TestFTCheckpointManager#test_load_restores_ft_checkpoint_before_main_checkpoint().
  TestFTCheckpointManager.test_folder: TestFTCheckpointManager#test_folder.
  TestFTCheckpointManager.test_save_returns_whether_the_full_checkpoint_was_written: TestFTCheckpointManager#test_save_returns_whether_the_full_checkpoint_was_written().
  TestFTCheckpointManager.tearDown: TestFTCheckpointManager#tearDown().
  TestFTCheckpointManager.test_disabled_load_does_not_restore_ft_checkpoint: TestFTCheckpointManager#test_disabled_load_does_not_restore_ft_checkpoint().
  DummyFTManager.manager: DummyFTManager#manager.
  fake_async_save: fake_async_save().
  TestFTCheckpointManager.optimizers: TestFTCheckpointManager#optimizers.
  TestFTCheckpointManager.lr_schedulers: TestFTCheckpointManager#lr_schedulers.
  TestFTCheckpointManager.data_loader: TestFTCheckpointManager#data_loader.
  TestFTCheckpointManager.patcher_group: TestFTCheckpointManager#patcher_group.
  TestFTCheckpointManager.patcher_destroy: TestFTCheckpointManager#patcher_destroy.
  TestFTCheckpointManager.ft_manager: TestFTCheckpointManager#ft_manager.
  DummyFTManager: DummyFTManager#
  FakeOptimizersContainer.state_dict: FakeOptimizersContainer#state_dict().
  FakeOptimizersContainer.load_state_dict: FakeOptimizersContainer#load_state_dict().
  DummyFTManager.enabled: DummyFTManager#enabled().
  TestFTCheckpointManager.test_optimizer_cache_metadata_changes_only_after_explicit_refresh: TestFTCheckpointManager#test_optimizer_cache_metadata_changes_only_after_explicit_refresh().
  TestFTCheckpointManager.test_joining_replica_restores_healthy_replica_learning_rate: TestFTCheckpointManager#test_joining_replica_restores_healthy_replica_learning_rate().
  TestFTCheckpointManager.test_first_rejoined_update_matches_healthy_replica: TestFTCheckpointManager#test_first_rejoined_update_matches_healthy_replica().
  FakeOptimizersContainer._fake_param: FakeOptimizersContainer#_fake_param.
  TestFTCheckpointManager.base_temp_dir: TestFTCheckpointManager#base_temp_dir.
  TestFTCheckpointManager.model_parts: TestFTCheckpointManager#model_parts.
  TestFTCheckpointManager.states: TestFTCheckpointManager#states.
  FakeOptimizersContainer: FakeOptimizersContainer#
  FakeLRSchedulersContainer: FakeLRSchedulersContainer#
  FakeDataLoader: FakeDataLoader#
  DummyFuture: DummyFuture#
  DummyFTManager._enabled: DummyFTManager#_enabled.
  TestFTCheckpointManager.load_ft_checkpoint: TestFTCheckpointManager#load_ft_checkpoint().
  FakeOptimizersContainer.__init__: FakeOptimizersContainer#__init__().
  FakeOptimizersContainer.init_cache_state_dict: FakeOptimizersContainer#init_cache_state_dict().
  FakeLRSchedulersContainer.state_dict: FakeLRSchedulersContainer#state_dict().
  FakeLRSchedulersContainer.load_state_dict: FakeLRSchedulersContainer#load_state_dict().
  FakeDataLoader.__init__: FakeDataLoader#__init__().
  FakeDataLoader.state_dict: FakeDataLoader#state_dict().
  FakeDataLoader.load_state_dict: FakeDataLoader#load_state_dict().
  DummyFuture.__new__: DummyFuture#__new__().
  DummyFTManager.__init__: DummyFTManager#__init__().
  DummyFTManager.replica_id: DummyFTManager#replica_id.
  TestFTCheckpointManager: TestFTCheckpointManager#
  TestFTCheckpointManager.setUp: TestFTCheckpointManager#setUp().
---
# Module: [`torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py)

> **Collapsed catalog** (45 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="DummyFTManager"></a>`DummyFTManager` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L75)
- <a id="DummyFTManager.__init__"></a>`DummyFTManager.__init__` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L78)
- <a id="DummyFTManager._enabled"></a>`DummyFTManager._enabled` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L79)
- <a id="DummyFTManager.enabled"></a>`DummyFTManager.enabled` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L88)
- <a id="DummyFTManager.manager"></a>`DummyFTManager.manager` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L82)
- <a id="DummyFTManager.replica_id"></a>`DummyFTManager.replica_id` — [`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L80)
- <a id="DummyFuture"></a>`DummyFuture` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L61)
- <a id="DummyFuture.__new__"></a>`DummyFuture.__new__` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L62)
- <a id="FakeDataLoader"></a>`FakeDataLoader` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L50)
- <a id="FakeDataLoader.__init__"></a>`FakeDataLoader.__init__` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L51)
- <a id="FakeDataLoader.load_state_dict"></a>`FakeDataLoader.load_state_dict` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L57)
- <a id="FakeDataLoader.state_dict"></a>`FakeDataLoader.state_dict` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L54)
- <a id="FakeLRSchedulersContainer"></a>`FakeLRSchedulersContainer` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L42)
- <a id="FakeLRSchedulersContainer.load_state_dict"></a>`FakeLRSchedulersContainer.load_state_dict` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L46)
- <a id="FakeLRSchedulersContainer.state_dict"></a>`FakeLRSchedulersContainer.state_dict` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L43)
- <a id="FakeOptimizersContainer"></a>`FakeOptimizersContainer` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L27)
- <a id="FakeOptimizersContainer.__init__"></a>`FakeOptimizersContainer.__init__` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L28)
- <a id="FakeOptimizersContainer._fake_param"></a>`FakeOptimizersContainer._fake_param` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L29)
- <a id="FakeOptimizersContainer.init_cache_state_dict"></a>`FakeOptimizersContainer.init_cache_state_dict` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L38)
- <a id="FakeOptimizersContainer.load_state_dict"></a>`FakeOptimizersContainer.load_state_dict` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L34)
- <a id="FakeOptimizersContainer.state_dict"></a>`FakeOptimizersContainer.state_dict` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L31)
- <a id="TestFTCheckpointManager"></a>`TestFTCheckpointManager` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L92)
- <a id="TestFTCheckpointManager._build_replica"></a>`TestFTCheckpointManager._build_replica` — [`L253`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L253)
- <a id="TestFTCheckpointManager._manager"></a>`TestFTCheckpointManager._manager` — [`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L170)
- <a id="TestFTCheckpointManager.base_temp_dir"></a>`TestFTCheckpointManager.base_temp_dir` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L94)
- <a id="TestFTCheckpointManager.data_loader"></a>`TestFTCheckpointManager.data_loader` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L101)
- <a id="TestFTCheckpointManager.ft_manager"></a>`TestFTCheckpointManager.ft_manager` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L102)
- <a id="TestFTCheckpointManager.load_ft_checkpoint"></a>`TestFTCheckpointManager.load_ft_checkpoint` — [`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L225)
- <a id="TestFTCheckpointManager.lr_schedulers"></a>`TestFTCheckpointManager.lr_schedulers` — [`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L100)
- <a id="TestFTCheckpointManager.model_parts"></a>`TestFTCheckpointManager.model_parts` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L97)
- <a id="TestFTCheckpointManager.optimizers"></a>`TestFTCheckpointManager.optimizers` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L99)
- <a id="TestFTCheckpointManager.patcher_destroy"></a>`TestFTCheckpointManager.patcher_destroy` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L108)
- <a id="TestFTCheckpointManager.patcher_group"></a>`TestFTCheckpointManager.patcher_group` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L103)
- <a id="TestFTCheckpointManager.setUp"></a>`TestFTCheckpointManager.setUp` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L93)
- <a id="TestFTCheckpointManager.states"></a>`TestFTCheckpointManager.states` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L98)
- <a id="TestFTCheckpointManager.tearDown"></a>`TestFTCheckpointManager.tearDown` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L111)
- <a id="TestFTCheckpointManager.test_disabled_load_does_not_restore_ft_checkpoint"></a>`TestFTCheckpointManager.test_disabled_load_does_not_restore_ft_checkpoint` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L244)
- <a id="TestFTCheckpointManager.test_first_rejoined_update_matches_healthy_replica"></a>`TestFTCheckpointManager.test_first_rejoined_update_matches_healthy_replica` — [`L356`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L356)
- <a id="TestFTCheckpointManager.test_folder"></a>`TestFTCheckpointManager.test_folder` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L95)
- <a id="TestFTCheckpointManager.test_joining_replica_restores_healthy_replica_learning_rate"></a>`TestFTCheckpointManager.test_joining_replica_restores_healthy_replica_learning_rate` — [`L334`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L334)
- <a id="TestFTCheckpointManager.test_load_restores_ft_checkpoint_before_main_checkpoint"></a>`TestFTCheckpointManager.test_load_restores_ft_checkpoint_before_main_checkpoint` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L217)
- <a id="TestFTCheckpointManager.test_optimizer_cache_metadata_changes_only_after_explicit_refresh"></a>`TestFTCheckpointManager.test_optimizer_cache_metadata_changes_only_after_explicit_refresh` — [`L304`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L304)
- <a id="TestFTCheckpointManager.test_save_returns_whether_the_full_checkpoint_was_written"></a>`TestFTCheckpointManager.test_save_returns_whether_the_full_checkpoint_was_written` — [`L200`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L200)
- <a id="TestFTCheckpointManager.test_torchft_async_save_calls_maybe_wait_for_saving"></a>`TestFTCheckpointManager.test_torchft_async_save_calls_maybe_wait_for_saving` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L123)
- <a id="fake_async_save"></a>`fake_async_save` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/torchft/tests/test_torchft_checkpoint.py#L71)
