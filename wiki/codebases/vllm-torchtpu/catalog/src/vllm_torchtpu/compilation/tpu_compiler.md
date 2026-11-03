---
title: 'Module: src/vllm_torchtpu/compilation/tpu_compiler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/compilation/tpu_compiler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.compilation.tpu_compiler`/
symbols:
  TpuCompilerAdaptor.compile: TpuCompilerAdaptor#compile().
  TpuCompilerAdaptor.load: TpuCompilerAdaptor#load().
  TpuCompilerAdaptor._save_handle: TpuCompilerAdaptor#_save_handle().
  TpuCompilerAdaptor._replay: TpuCompilerAdaptor#_replay().
  compute_tpu_compilation_hash: compute_tpu_compilation_hash().
  logger: logger.
  TpuCompilerAdaptor.cache_dir: TpuCompilerAdaptor#cache_dir.
  _iter_runtime_cache_key_files: _iter_runtime_cache_key_files().
  TpuCompilerAdaptor._replay_from_peer: TpuCompilerAdaptor#_replay_from_peer().
  TpuCompilerAdaptor._run_backend: TpuCompilerAdaptor#_run_backend().
  _tpu_compile_env_factors: _tpu_compile_env_factors().
  _graph_fingerprint: _graph_fingerprint().
  _reloadable_kernel_relpaths: _reloadable_kernel_relpaths().
  TpuCompilerAdaptor._unwrap_compiled_fn: TpuCompilerAdaptor#_unwrap_compiled_fn().
  TpuCompilerAdaptor.initialize_cache: TpuCompilerAdaptor#initialize_cache().
  wait_for_peer_artifact: wait_for_peer_artifact().
  TpuCompilerAdaptor._peer_paths: TpuCompilerAdaptor#_peer_paths().
  TpuCompilerAdaptor._link_artifact: TpuCompilerAdaptor#_link_artifact().
  TpuCompilationHandle.entry: TpuCompilationHandle#entry.
  TpuCompilationHandle.signature: TpuCompilationHandle#signature.
  TpuCompilationHandle.fingerprint: TpuCompilationHandle#fingerprint.
  _peer_wait: _peer_wait.
  TpuCompilerAdaptor._disable_cache: TpuCompilerAdaptor#_disable_cache.
  TpuCompilerAdaptor.compute_hash: TpuCompilerAdaptor#compute_hash().
  TpuCompilationHandle: TpuCompilationHandle#
  TpuCompilationHandle.was_wrapped: TpuCompilationHandle#was_wrapped.
  _RUNTIME_CACHE_KEY_EXCLUDED_PATHS: _RUNTIME_CACHE_KEY_EXCLUDED_PATHS.
  _ensure_tuple_output: _ensure_tuple_output().
  _single_size: _single_size().
  TpuCompilationHandle.key: TpuCompilationHandle#key.
  _tpu_backend: _tpu_backend.
  _PEER_POLL_S: _PEER_POLL_S.
  _FINGERPRINT_MAX_NUMEL: _FINGERPRINT_MAX_NUMEL.
  _deserialize_entry: _deserialize_entry().
  _TPU_COMPILE_ENV_IGNORED: _TPU_COMPILE_ENV_IGNORED.
  _NATIVE_TPU_COMPILE_ENV_VARS: _NATIVE_TPU_COMPILE_ENV_VARS.
  _RUNTIME_CACHE_KEY_PATHS: _RUNTIME_CACHE_KEY_PATHS.
  TpuCompilerAdaptor.unwrap_fn: TpuCompilerAdaptor#unwrap_fn().
  TpuCompilerAdaptor: TpuCompilerAdaptor#
  TpuCompilerAdaptor.name: TpuCompilerAdaptor#name.
  TpuCompilerAdaptor.__init__: TpuCompilerAdaptor#__init__().
---
# Module: [`src/vllm_torchtpu/compilation/tpu_compiler.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py)

## Classes
### <a id="TpuCompilationHandle"></a>`TpuCompilationHandle`
- def: [`src/vllm_torchtpu/compilation/tpu_compiler.py:56`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L56)
- doc: Metadata handle saved to vLLM's compilation cache directory.
- signature: `class TpuCompilationHandle:`
- members:
  - <a id="TpuCompilationHandle.entry"></a>`entry` — [`L78`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L78)
  - <a id="TpuCompilationHandle.fingerprint"></a>`fingerprint` — [`L81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L81)
  - <a id="TpuCompilationHandle.key"></a>`key` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L77)
  - <a id="TpuCompilationHandle.signature"></a>`signature` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L79)
  - <a id="TpuCompilationHandle.was_wrapped"></a>`was_wrapped` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L80)
- used by: [`_replay`](tpu_compiler.md#TpuCompilerAdaptor._replay), [`_save_handle`](tpu_compiler.md#TpuCompilerAdaptor._save_handle)

### <a id="TpuCompilerAdaptor"></a>`TpuCompilerAdaptor`
- def: [`src/vllm_torchtpu/compilation/tpu_compiler.py:519`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L519)
- doc: CompilerInterface implementation for TPU.
- signature: `class TpuCompilerAdaptor(CompilerInterface):`
- members:
  - <a id="TpuCompilerAdaptor._link_artifact"></a>`_link_artifact(src: str, dst: str)` — [`L771`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L771) — Make `dst` the same file as `src`: a hard link, a copy if `src`
  - <a id="TpuCompilerAdaptor._peer_paths"></a>`_peer_paths(self, key: str)` — [`L722`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L722) — Where the other ranks have saved their artifact for `key`.
  - <a id="TpuCompilerAdaptor._replay"></a>`_replay(self, path: str, graph: fx.GraphModule, was_wrapped: bool, fingerprint: str | None = None)` — [`L658`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L658) — Rebuild the runnable saved at `path`, or None to recompile. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor._replay_from_peer"></a>`_replay_from_peer(self, key: str, graph: fx.GraphModule, was_wrapped: bool, fingerprint: str)` — [`L746`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L746) — Replay the artifact another rank saved for this bucket. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor._run_backend"></a>`_run_backend(self, graph: fx.GraphModule, example_inputs: list[Any])` — [`L555`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L555) — Compile `graph` with TpuBackend, and grab its serializable entry. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor._save_handle"></a>`_save_handle(self, key: str, path: str, entry: Any, graph: fx.GraphModule, was_wrapped: bool, fingerprint: str | None)` — [`L616`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L616) — Write the bundled entry for `graph` to `path`. True if it landed. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor.compile"></a>`compile(self, graph: fx.GraphModule, example_inputs: list[Any], compiler_config: dict[str, Any], compile_range: Range, key: str | None = None)` — [`L791`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L791) — Compile a Dynamo-level FX graph to a TPU PjRt executable. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor.compute_hash"></a>`compute_hash(self, vllm_config: VllmConfig)` — [`L539`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L539) — Hash TPU runtime sources that sit behind custom-op boundaries. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor.initialize_cache"></a>`initialize_cache(self, cache_dir: str, disable_cache: bool = False, prefix: str = "")` — [`L533`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L533)
  - <a id="TpuCompilerAdaptor.load"></a>`load(self, handle: Any, graph: fx.GraphModule, example_inputs: list[Any], graph_index: int, compile_range: Range)` — [`L913`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L913) — Rebuild a compiled runnable from the artifact `compile` saved. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor.unwrap_fn"></a>`unwrap_fn(*args, **kwargs)` — [`L547`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L547)
  - <a id="TpuCompilerAdaptor.cache_dir"></a>`cache_dir` — [`L530`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L530) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="TpuCompilerAdaptor.name"></a>`name` — [`L527`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L527)
- protocol/private: <a id="TpuCompilerAdaptor.__init__"></a>`__init__`[`L529`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L529), <a id="TpuCompilerAdaptor._disable_cache"></a>`_disable_cache`[`L531`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L531), <a id="TpuCompilerAdaptor._unwrap_compiled_fn"></a>`_unwrap_compiled_fn`[`L544`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L544)
- uses (calls/refs, reference-scoped): [`runnable_for`](shape_variants.md#runnable_for), [`compute_tpu_compilation_hash`](tpu_compiler.md#compute_tpu_compilation_hash), [`logger`](tpu_compiler.md#logger), [`remember`](shape_variants.md#remember), [`_graph_fingerprint`](tpu_compiler.md#_graph_fingerprint), [`reset_scheduling_group_ids`](../kernels/deepseek_v4/streamindex_topk/config.md#reset_scheduling_group_ids), [`graph_signature`](shape_variants.md#graph_signature), [`TPU_PRECOMPILE_PEER_REPLAY`](../envs.md#TPU_PRECOMPILE_PEER_REPLAY), [`_peer_wait`](tpu_compiler.md#_peer_wait), [`entry`](tpu_compiler.md#TpuCompilationHandle.entry), [`fingerprint`](tpu_compiler.md#TpuCompilationHandle.fingerprint), [`signature`](tpu_compiler.md#TpuCompilationHandle.signature), [`TpuCompilationHandle`](tpu_compiler.md#TpuCompilationHandle), [`_ensure_tuple_output`](tpu_compiler.md#_ensure_tuple_output), [`_single_size`](tpu_compiler.md#_single_size), [`was_wrapped`](tpu_compiler.md#TpuCompilationHandle.was_wrapped), [`_PEER_POLL_S`](tpu_compiler.md#_PEER_POLL_S), [`_deserialize_entry`](tpu_compiler.md#_deserialize_entry), [`_tpu_backend`](tpu_compiler.md#_tpu_backend), [`key`](tpu_compiler.md#TpuCompilationHandle.key)

## Functions
- <a id="_deserialize_entry"></a>`_deserialize_entry(entry: Any)` — [`L149`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L149) — Rebuild a runnable from a bundled AOTAutograd entry.
- <a id="_ensure_tuple_output"></a>`_ensure_tuple_output(graph: fx.GraphModule)` — [`L485`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L485) — Wrap a graph module to return a tuple if it returns a single tensor.
- <a id="_graph_fingerprint"></a>`_graph_fingerprint(graph: fx.GraphModule)` — [`L114`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L114) — Hash of the code of `graph` and its submodules and of their constants. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_iter_runtime_cache_key_files"></a>`_iter_runtime_cache_key_files(repo_root: Path)` — [`L338`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L338) — Return runtime source files that affect TPU custom-op lowering. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_reloadable_kernel_relpaths"></a>`_reloadable_kernel_relpaths(repo_root: Path)` — [`L372`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L372) — Repo-relative paths of the hot-reloadable kernel modules. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_single_size"></a>`_single_size(compile_range: Range)` — [`L514`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L514) — The token bucket a compile range pins, or None for a size range.
- <a id="_tpu_compile_env_factors"></a>`_tpu_compile_env_factors()` — [`L402`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L402) — Return TorchTPU plugin env values that can affect compilation. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="compute_tpu_compilation_hash"></a>`compute_tpu_compilation_hash(vllm_config: VllmConfig)` — [`L417`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L417) — Hash TPU-specific factors used by both AOT and piecewise caches. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="wait_for_peer_artifact"></a>`wait_for_peer_artifact(timeout_s: float)` — [`L100`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L100) — Within this block, `compile` waits up to `timeout_s` for another rank

## Module values
- <a id="_FINGERPRINT_MAX_NUMEL"></a>`_FINGERPRINT_MAX_NUMEL` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L94)
- <a id="_NATIVE_TPU_COMPILE_ENV_VARS"></a>`_NATIVE_TPU_COMPILE_ENV_VARS` — [`L280`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L280)
- <a id="_PEER_POLL_S"></a>`_PEER_POLL_S` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L91)
- <a id="_RUNTIME_CACHE_KEY_EXCLUDED_PATHS"></a>`_RUNTIME_CACHE_KEY_EXCLUDED_PATHS` — [`L331`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L331)
- <a id="_RUNTIME_CACHE_KEY_PATHS"></a>`_RUNTIME_CACHE_KEY_PATHS` — [`L287`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L287)
- <a id="_TPU_COMPILE_ENV_IGNORED"></a>`_TPU_COMPILE_ENV_IGNORED` — [`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L175)
- <a id="_peer_wait"></a>`_peer_wait` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L96)
- <a id="_tpu_backend"></a>`_tpu_backend` — [`L84`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L84)
- <a id="logger"></a>`logger` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/tpu_compiler.py#L52)

