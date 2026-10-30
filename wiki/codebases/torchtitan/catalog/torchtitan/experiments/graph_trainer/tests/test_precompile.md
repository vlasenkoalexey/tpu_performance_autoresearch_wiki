---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_precompile.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_precompile.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_precompile`/
symbols:
  TestPrecompiledFxTraceArtifact.test_artifact_pickle_with_blockmask_treespec: TestPrecompiledFxTraceArtifact#test_artifact_pickle_with_blockmask_treespec().
  TestPrecompiledFxTraceArtifact.test_fx_trace_save_load_fingerprint_mismatch: TestPrecompiledFxTraceArtifact#test_fx_trace_save_load_fingerprint_mismatch().
  TestPrecompiledFxTraceArtifact.test_artifact_pickle_roundtrip: TestPrecompiledFxTraceArtifact#test_artifact_pickle_roundtrip().
  TestConfigFingerprint.test_compile_config_sensitivity: TestConfigFingerprint#test_compile_config_sensitivity().
  TestPrecompiledFxTraceArtifact.test_standalone_inductor_precompile: TestPrecompiledFxTraceArtifact#test_standalone_inductor_precompile().
  _make_stub_model: _make_stub_model().
  TestPrecompiledFxTraceArtifact.test_loaded_artifact_supports_graph_runner: TestPrecompiledFxTraceArtifact#test_loaded_artifact_supports_graph_runner().
  TestConfigFingerprint.test_memory_policy_save_ops_sensitivity: TestConfigFingerprint#test_memory_policy_save_ops_sensitivity().
  _StubCompileConfig: _StubCompileConfig#
  TestConfigFingerprint.test_parallelism_sensitivity: TestConfigFingerprint#test_parallelism_sensitivity().
  TestConfigFingerprint.test_pass_order_sensitive: TestConfigFingerprint#test_pass_order_sensitive().
  TestCudagraphFingerprintConsistency.test_cudagraph_included_in_fingerprint: TestCudagraphFingerprintConsistency#test_cudagraph_included_in_fingerprint().
  TestCudagraphFingerprintConsistency.test_same_config_produces_same_fingerprint: TestCudagraphFingerprintConsistency#test_same_config_produces_same_fingerprint().
  TestDiskStorageAdapter.test_save_load_roundtrip: TestDiskStorageAdapter#test_save_load_roundtrip().
  TestDiskStorageAdapter.test_delete_existing: TestDiskStorageAdapter#test_delete_existing().
  TestPrecompileMain.test_validates_memory_policy_after_model_setup: TestPrecompileMain#test_validates_memory_policy_after_model_setup().
  TestConfigFingerprint.test_deterministic: TestConfigFingerprint#test_deterministic().
  TestConfigFingerprint.test_model_shape_sensitivity: TestConfigFingerprint#test_model_shape_sensitivity().
  TestPrecompileLossSetup.test_chunked_loss_setup_matches_trainer_boundary: TestPrecompileLossSetup#test_chunked_loss_setup_matches_trainer_boundary().
  _StubParallelDims: _StubParallelDims#
  TestCudagraphPass.cuda_i64: TestCudagraphPass#cuda_i64().
  TestDiskStorageAdapter.test_save_creates_subdirs: TestDiskStorageAdapter#test_save_creates_subdirs().
  TestDiskStorageAdapter.test_save_overwrites_existing: TestDiskStorageAdapter#test_save_overwrites_existing().
  TestPrecompiledFxTraceArtifact.test_rejects_trainer_owned_gradient_state: TestPrecompiledFxTraceArtifact#test_rejects_trainer_owned_gradient_state().
  TestCudagraphPass.test_minimal_async_ep_custom_ops_are_wrapped_by_cudagraph_pass: TestCudagraphPass#test_minimal_async_ep_custom_ops_are_wrapped_by_cudagraph_pass().
  _StubCompileConfig.passes: _StubCompileConfig#passes.
  TestCudagraphPass.cuda_f32: TestCudagraphPass#cuda_f32().
  TestDiskStorageAdapter.test_load_nonexistent_raises: TestDiskStorageAdapter#test_load_nonexistent_raises().
  TestDiskStorageAdapter.test_exists_false_for_missing: TestDiskStorageAdapter#test_exists_false_for_missing().
  TestDiskStorageAdapter.test_delete_nonexistent_noop: TestDiskStorageAdapter#test_delete_nonexistent_noop().
  TestDiskStorageAdapter.test_path_traversal_rejected: TestDiskStorageAdapter#test_path_traversal_rejected().
  TestCudagraphPass.test_non_graphmodule_raises: TestCudagraphPass#test_non_graphmodule_raises().
  _StubCompileConfig.ep_overlap: _StubCompileConfig#ep_overlap.
  TestCudagraphPass.test_graphmodule_wraps_forward: TestCudagraphPass#test_graphmodule_wraps_forward().
  _StubCompileConfig.memory_policy: _StubCompileConfig#memory_policy.
  _StubParallelDims.tp: _StubParallelDims#tp.
  TestPrecompiledFxTraceArtifact.train_step: TestPrecompiledFxTraceArtifact#train_step().
  _StubCompileConfig.full_recompute_save_ops: _StubCompileConfig#full_recompute_save_ops.
  TestPrecompileMain.common_setup: TestPrecompileMain#common_setup().
  TestPrecompileMain.validate: TestPrecompileMain#validate().
  TestPrecompileMain.precompile: TestPrecompileMain#precompile().
  TestPrecompiledFxTraceArtifact.forward: TestPrecompiledFxTraceArtifact#forward().
  TestCudagraphPass.plain_fn: TestCudagraphPass#plain_fn().
  TestDiskStorageAdapter: TestDiskStorageAdapter#
  _StubCompileConfig.mode: _StubCompileConfig#mode.
  _StubCompileConfig.backend: _StubCompileConfig#backend.
  _StubParallelDims.world_size: _StubParallelDims#world_size.
  _StubParallelDims.dp_replicate: _StubParallelDims#dp_replicate.
  _StubParallelDims.dp_shard: _StubParallelDims#dp_shard.
  _StubParallelDims.cp: _StubParallelDims#cp.
  _StubParallelDims.pp: _StubParallelDims#pp.
  _StubParallelDims.ep: _StubParallelDims#ep.
  TestPrecompileMain: TestPrecompileMain#
  TestConfigFingerprint: TestConfigFingerprint#
  TestPrecompileLossSetup: TestPrecompileLossSetup#
  TestPrecompiledFxTraceArtifact: TestPrecompiledFxTraceArtifact#
  TestCudagraphPass: TestCudagraphPass#
  TestCudagraphFingerprintConsistency: TestCudagraphFingerprintConsistency#
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_precompile.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py)

> **Collapsed catalog** (58 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestConfigFingerprint"></a>`TestConfigFingerprint` — [`L176`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L176)
- <a id="TestConfigFingerprint.test_compile_config_sensitivity"></a>`TestConfigFingerprint.test_compile_config_sensitivity` — [`L234`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L234)
- <a id="TestConfigFingerprint.test_deterministic"></a>`TestConfigFingerprint.test_deterministic` — [`L177`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L177)
- <a id="TestConfigFingerprint.test_memory_policy_save_ops_sensitivity"></a>`TestConfigFingerprint.test_memory_policy_save_ops_sensitivity` — [`L190`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L190)
- <a id="TestConfigFingerprint.test_model_shape_sensitivity"></a>`TestConfigFingerprint.test_model_shape_sensitivity` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L206)
- <a id="TestConfigFingerprint.test_parallelism_sensitivity"></a>`TestConfigFingerprint.test_parallelism_sensitivity` — [`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L220)
- <a id="TestConfigFingerprint.test_pass_order_sensitive"></a>`TestConfigFingerprint.test_pass_order_sensitive` — [`L263`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L263)
- <a id="TestCudagraphFingerprintConsistency"></a>`TestCudagraphFingerprintConsistency` — [`L619`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L619)
- <a id="TestCudagraphFingerprintConsistency.test_cudagraph_included_in_fingerprint"></a>`TestCudagraphFingerprintConsistency.test_cudagraph_included_in_fingerprint` — [`L627`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L627)
- <a id="TestCudagraphFingerprintConsistency.test_same_config_produces_same_fingerprint"></a>`TestCudagraphFingerprintConsistency.test_same_config_produces_same_fingerprint` — [`L644`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L644)
- <a id="TestCudagraphPass"></a>`TestCudagraphPass` — [`L525`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L525)
- <a id="TestCudagraphPass.cuda_f32"></a>`TestCudagraphPass.cuda_f32` — [`L564`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L564)
- <a id="TestCudagraphPass.cuda_i64"></a>`TestCudagraphPass.cuda_i64` — [`L561`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L561)
- <a id="TestCudagraphPass.plain_fn"></a>`TestCudagraphPass.plain_fn` — [`L533`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L533)
- <a id="TestCudagraphPass.test_graphmodule_wraps_forward"></a>`TestCudagraphPass.test_graphmodule_wraps_forward` — [`L539`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L539)
- <a id="TestCudagraphPass.test_minimal_async_ep_custom_ops_are_wrapped_by_cudagraph_pass"></a>`TestCudagraphPass.test_minimal_async_ep_custom_ops_are_wrapped_by_cudagraph_pass` — [`L556`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L556)
- <a id="TestCudagraphPass.test_non_graphmodule_raises"></a>`TestCudagraphPass.test_non_graphmodule_raises` — [`L528`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L528)
- <a id="TestDiskStorageAdapter"></a>`TestDiskStorageAdapter` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L21)
- <a id="TestDiskStorageAdapter.test_delete_existing"></a>`TestDiskStorageAdapter.test_delete_existing` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L54)
- <a id="TestDiskStorageAdapter.test_delete_nonexistent_noop"></a>`TestDiskStorageAdapter.test_delete_nonexistent_noop` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L62)
- <a id="TestDiskStorageAdapter.test_exists_false_for_missing"></a>`TestDiskStorageAdapter.test_exists_false_for_missing` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L40)
- <a id="TestDiskStorageAdapter.test_load_nonexistent_raises"></a>`TestDiskStorageAdapter.test_load_nonexistent_raises` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L34)
- <a id="TestDiskStorageAdapter.test_path_traversal_rejected"></a>`TestDiskStorageAdapter.test_path_traversal_rejected` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L74)
- <a id="TestDiskStorageAdapter.test_save_creates_subdirs"></a>`TestDiskStorageAdapter.test_save_creates_subdirs` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L45)
- <a id="TestDiskStorageAdapter.test_save_load_roundtrip"></a>`TestDiskStorageAdapter.test_save_load_roundtrip` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L22)
- <a id="TestDiskStorageAdapter.test_save_overwrites_existing"></a>`TestDiskStorageAdapter.test_save_overwrites_existing` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L67)
- <a id="TestPrecompileLossSetup"></a>`TestPrecompileLossSetup` — [`L277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L277)
- <a id="TestPrecompileLossSetup.test_chunked_loss_setup_matches_trainer_boundary"></a>`TestPrecompileLossSetup.test_chunked_loss_setup_matches_trainer_boundary` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L278)
- <a id="TestPrecompileMain"></a>`TestPrecompileMain` — [`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L124)
- <a id="TestPrecompileMain.common_setup"></a>`TestPrecompileMain.common_setup` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L143)
- <a id="TestPrecompileMain.precompile"></a>`TestPrecompileMain.precompile` — [`L152`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L152)
- <a id="TestPrecompileMain.test_validates_memory_policy_after_model_setup"></a>`TestPrecompileMain.test_validates_memory_policy_after_model_setup` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L125)
- <a id="TestPrecompileMain.validate"></a>`TestPrecompileMain.validate` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L147)
- <a id="TestPrecompiledFxTraceArtifact"></a>`TestPrecompiledFxTraceArtifact` — [`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L296)
- <a id="TestPrecompiledFxTraceArtifact.forward"></a>`TestPrecompiledFxTraceArtifact.forward` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L310)
- <a id="TestPrecompiledFxTraceArtifact.test_artifact_pickle_roundtrip"></a>`TestPrecompiledFxTraceArtifact.test_artifact_pickle_roundtrip` — [`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L402)
- <a id="TestPrecompiledFxTraceArtifact.test_artifact_pickle_with_blockmask_treespec"></a>`TestPrecompiledFxTraceArtifact.test_artifact_pickle_with_blockmask_treespec` — [`L436`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L436)
- <a id="TestPrecompiledFxTraceArtifact.test_fx_trace_save_load_fingerprint_mismatch"></a>`TestPrecompiledFxTraceArtifact.test_fx_trace_save_load_fingerprint_mismatch` — [`L494`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L494)
- <a id="TestPrecompiledFxTraceArtifact.test_loaded_artifact_supports_graph_runner"></a>`TestPrecompiledFxTraceArtifact.test_loaded_artifact_supports_graph_runner` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L297)
- <a id="TestPrecompiledFxTraceArtifact.test_rejects_trainer_owned_gradient_state"></a>`TestPrecompiledFxTraceArtifact.test_rejects_trainer_owned_gradient_state` — [`L322`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L322)
- <a id="TestPrecompiledFxTraceArtifact.test_standalone_inductor_precompile"></a>`TestPrecompiledFxTraceArtifact.test_standalone_inductor_precompile` — [`L340`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L340)
- <a id="TestPrecompiledFxTraceArtifact.train_step"></a>`TestPrecompiledFxTraceArtifact.train_step` — [`L359`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L359)
- <a id="_StubCompileConfig"></a>`_StubCompileConfig` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L82)
- <a id="_StubCompileConfig.backend"></a>`_StubCompileConfig.backend` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L84)
- <a id="_StubCompileConfig.ep_overlap"></a>`_StubCompileConfig.ep_overlap` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L88)
- <a id="_StubCompileConfig.full_recompute_save_ops"></a>`_StubCompileConfig.full_recompute_save_ops` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L87)
- <a id="_StubCompileConfig.memory_policy"></a>`_StubCompileConfig.memory_policy` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L86)
- <a id="_StubCompileConfig.mode"></a>`_StubCompileConfig.mode` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L83)
- <a id="_StubCompileConfig.passes"></a>`_StubCompileConfig.passes` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L85)
- <a id="_StubParallelDims"></a>`_StubParallelDims` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L92)
- <a id="_StubParallelDims.cp"></a>`_StubParallelDims.cp` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L96)
- <a id="_StubParallelDims.dp_replicate"></a>`_StubParallelDims.dp_replicate` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L94)
- <a id="_StubParallelDims.dp_shard"></a>`_StubParallelDims.dp_shard` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L95)
- <a id="_StubParallelDims.ep"></a>`_StubParallelDims.ep` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L99)
- <a id="_StubParallelDims.pp"></a>`_StubParallelDims.pp` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L98)
- <a id="_StubParallelDims.tp"></a>`_StubParallelDims.tp` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L97)
- <a id="_StubParallelDims.world_size"></a>`_StubParallelDims.world_size` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L93)
- <a id="_make_stub_model"></a>`_make_stub_model` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_precompile.py#L102)
