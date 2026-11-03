---
title: 'Module: src/vllm_torchtpu/runner/tpu_pooling.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/runner/tpu_pooling.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.runner.tpu_pooling`/
symbols:
  static_pool: static_pool().
  build_static_pool_inputs: build_static_pool_inputs().
  build_dummy_static_pool_inputs: build_dummy_static_pool_inputs().
  resolve_static_pooler_spec: resolve_static_pooler_spec().
  unpack_static_pool_output: unpack_static_pool_output().
  _install_tpu_pooling_patches_locked: _install_tpu_pooling_patches_locked().
  install_tpu_pooling_patches: install_tpu_pooling_patches().
  PromptTokenIdsTensor.req_id_map: PromptTokenIdsTensor#req_id_map.
  build_pooling_metadata: build_pooling_metadata().
  StaticPoolerSpec: StaticPoolerSpec#
  StaticPoolerSpec.pooling_type: StaticPoolerSpec#pooling_type.
  _to_device: _to_device().
  PromptTokenIdsTensor.__getitem__: PromptTokenIdsTensor#__getitem__().
  StaticPoolInputs: StaticPoolInputs#
  compute_pooling_kv_cache_cap_bytes: compute_pooling_kv_cache_cap_bytes().
  StaticPoolerSpec.out_dim: StaticPoolerSpec#out_dim.
  StaticPoolInputs.finished: StaticPoolInputs#finished.
  StaticPoolerChunkOutput: StaticPoolerChunkOutput#
  _static_pool_compiled: _static_pool_compiled.
  _tpu_pooling_patches_installed: _tpu_pooling_patches_installed.
  StaticPoolInputs.gather_idx: StaticPoolInputs#gather_idx.
  StaticPoolInputs.seg_ids: StaticPoolInputs#seg_ids.
  StaticPoolInputs.lens: StaticPoolInputs#lens.
  StaticPoolInputs.dims: StaticPoolInputs#dims.
  StaticPoolInputs.use_act: StaticPoolInputs#use_act.
  StaticPoolInputs.num_reqs: StaticPoolInputs#num_reqs.
  StaticPoolInputs.out_dims: StaticPoolInputs#out_dims.
  StaticPoolerChunkOutput.padded: StaticPoolerChunkOutput#padded.
  StaticPoolerChunkOutput.num_reqs: StaticPoolerChunkOutput#num_reqs.
  PromptTokenIdsTensor.get: PromptTokenIdsTensor#get().
  PromptTokenIdsTensor.__contains__: PromptTokenIdsTensor#__contains__().
  PromptTokenIdsTensor.items: PromptTokenIdsTensor#items().
  PromptTokenIdsTensor.keys: PromptTokenIdsTensor#keys().
  PromptTokenIdsTensor.values: PromptTokenIdsTensor#values().
  PromptTokenIdsTensor: PromptTokenIdsTensor#
  StaticPoolerSpec.head_dtype: StaticPoolerSpec#head_dtype.
  StaticPoolerSpec.projector: StaticPoolerSpec#projector.
  StaticPoolerSpec.normalize: StaticPoolerSpec#normalize.
  _static_pool_impl: _static_pool_impl().
  iter_pooler_precompile_grid: iter_pooler_precompile_grid().
  StaticPoolerChunkOutput.finished: StaticPoolerChunkOutput#finished.
  StaticPoolerChunkOutput.out_dims: StaticPoolerChunkOutput#out_dims.
  gate_unfinished: gate_unfinished().
  TPUMeanPool: TPUMeanPool#
  TPUMeanPool.forward: TPUMeanPool#forward().
  _tpu_pooling_patches_lock: _tpu_pooling_patches_lock.
  _install_tpu_pooling_patches_locked.safe_embed_forward: _install_tpu_pooling_patches_locked().safe_embed_forward().
  _install_tpu_pooling_patches_locked.safe_get_prompt_token_ids: _install_tpu_pooling_patches_locked().safe_get_prompt_token_ids().
  build_pooling_metadata._extract_prompt_len: build_pooling_metadata()._extract_prompt_len().
  _resolve_head_dtype: _resolve_head_dtype().
  _projector_out_dim: _projector_out_dim().
  compute_pooling_kv_cache_cap_tokens: compute_pooling_kv_cache_cap_tokens().
  _STATIC_POOLING_TYPES._STATIC_POOLING_TYPES: _STATIC_POOLING_TYPES._STATIC_POOLING_TYPES.
  PromptTokenIdsTensor.__new__: PromptTokenIdsTensor#__new__().
  PromptTokenIdsTensor.__init__: PromptTokenIdsTensor#__init__().
---
# Module: [`src/vllm_torchtpu/runner/tpu_pooling.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py)

## Classes
### <a id="PromptTokenIdsTensor"></a>`PromptTokenIdsTensor`
- def: [`src/vllm_torchtpu/runner/tpu_pooling.py:44`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L44)
- doc: A 2D CPU torch.Tensor representing batched prompt token IDs.
- signature: `class PromptTokenIdsTensor(torch.Tensor):`
- members:
  - <a id="PromptTokenIdsTensor.get"></a>`get(self, key, default=None)` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L69)
  - <a id="PromptTokenIdsTensor.items"></a>`items(self)` — [`L79`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L79)
  - <a id="PromptTokenIdsTensor.keys"></a>`keys(self)` — [`L82`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L82)
  - <a id="PromptTokenIdsTensor.values"></a>`values(self)` — [`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L85)
  - <a id="PromptTokenIdsTensor.req_id_map"></a>`req_id_map` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L59)
- protocol/private: <a id="PromptTokenIdsTensor.__contains__"></a>`__contains__`[`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L74), <a id="PromptTokenIdsTensor.__getitem__"></a>`__getitem__`[`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L61), <a id="PromptTokenIdsTensor.__init__"></a>`__init__`[`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L58), <a id="PromptTokenIdsTensor.__new__"></a>`__new__`[`L53`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L53)
- used by: [`build_pooling_metadata`](tpu_pooling.md#build_pooling_metadata)

### <a id="StaticPoolInputs"></a>`StaticPoolInputs`
- def: [`src/vllm_torchtpu/runner/tpu_pooling.py:499`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L499)
- doc: Device inputs of one static-pool call plus host-side bookkeeping.
- signature: `class StaticPoolInputs:`
- members:
  - <a id="StaticPoolInputs.dims"></a>`dims` — [`L505`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L505)
  - <a id="StaticPoolInputs.finished"></a>`finished` — [`L509`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L509)
  - <a id="StaticPoolInputs.gather_idx"></a>`gather_idx` — [`L502`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L502)
  - <a id="StaticPoolInputs.lens"></a>`lens` — [`L504`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L504)
  - <a id="StaticPoolInputs.num_reqs"></a>`num_reqs` — [`L508`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L508)
  - <a id="StaticPoolInputs.out_dims"></a>`out_dims` — [`L510`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L510)
  - <a id="StaticPoolInputs.seg_ids"></a>`seg_ids` — [`L503`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L503)
  - <a id="StaticPoolInputs.use_act"></a>`use_act` — [`L506`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L506)
- used by: [`_pool_chunk`](tpu_runner.md#TPUModelRunner._pool_chunk), [`static_pool`](tpu_pooling.md#static_pool), [`build_static_pool_inputs`](tpu_pooling.md#build_static_pool_inputs), [`build_dummy_static_pool_inputs`](tpu_pooling.md#build_dummy_static_pool_inputs)

### <a id="StaticPoolerChunkOutput"></a>`StaticPoolerChunkOutput`
- def: [`src/vllm_torchtpu/runner/tpu_pooling.py:688`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L688)
- doc: Deferred static-pool output of one chunk (unpacked in sample_tokens).
- signature: `class StaticPoolerChunkOutput:`
- members:
  - <a id="StaticPoolerChunkOutput.finished"></a>`finished` — [`L694`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L694)
  - <a id="StaticPoolerChunkOutput.num_reqs"></a>`num_reqs` — [`L693`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L693)
  - <a id="StaticPoolerChunkOutput.out_dims"></a>`out_dims` — [`L695`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L695)
  - <a id="StaticPoolerChunkOutput.padded"></a>`padded` — [`L692`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L692)
- used by: [`sample_tokens`](tpu_runner.md#TPUModelRunner.sample_tokens), [`_pool_chunk`](tpu_runner.md#TPUModelRunner._pool_chunk), [`unpack_static_pool_output`](tpu_pooling.md#unpack_static_pool_output)

### <a id="StaticPoolerSpec"></a>`StaticPoolerSpec`
- def: [`src/vllm_torchtpu/runner/tpu_pooling.py:336`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L336)
- doc: Per-process static configuration of the compiled pooler.
- signature: `class StaticPoolerSpec:`
- members:
  - <a id="StaticPoolerSpec.head_dtype"></a>`head_dtype` — [`L342`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L342)
  - <a id="StaticPoolerSpec.normalize"></a>`normalize` — [`L346`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L346)
  - <a id="StaticPoolerSpec.out_dim"></a>`out_dim` — [`L348`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L348)
  - <a id="StaticPoolerSpec.pooling_type"></a>`pooling_type` — [`L340`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L340)
  - <a id="StaticPoolerSpec.projector"></a>`projector` — [`L344`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L344)
- used by: [`static_pool`](tpu_pooling.md#static_pool), [`build_static_pool_inputs`](tpu_pooling.md#build_static_pool_inputs), [`build_dummy_static_pool_inputs`](tpu_pooling.md#build_dummy_static_pool_inputs), [`resolve_static_pooler_spec`](tpu_pooling.md#resolve_static_pooler_spec), [`_static_pooler_spec`](tpu_runner.md#TPUModelRunner._static_pooler_spec)

### <a id="TPUMeanPool"></a>`TPUMeanPool`
- def: [`src/vllm_torchtpu/runner/tpu_pooling.py:89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L89)
- doc: TPU-native MeanPool with online FP32 accumulation across chunked prefill.
- signature: `class TPUMeanPool(SequencePoolingMethod):`
- members:
  - <a id="TPUMeanPool.forward"></a>`forward(self, hidden_states: torch.Tensor, pooling_metadata: PoolingMetadata)` — [`L92`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L92)
- used by: [`_install_tpu_pooling_patches_locked`](tpu_pooling.md#_install_tpu_pooling_patches_locked)

## Functions
- <a id="build_pooling_metadata._extract_prompt_len"></a>`_extract_prompt_len(r)` — [`L270`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L270)
- <a id="_install_tpu_pooling_patches_locked"></a>`_install_tpu_pooling_patches_locked()` — [`L188`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L188)
- <a id="_projector_out_dim"></a>`_projector_out_dim(projector: torch.nn.Module)` — [`L361`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L361)
- <a id="_resolve_head_dtype"></a>`_resolve_head_dtype(head_dtype: Any)` — [`L351`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L351)
- <a id="_static_pool_impl"></a>`_static_pool_impl(hidden_states: torch.Tensor, gather_idx: torch.Tensor | None, seg_ids: torch.Tensor | None, lens: torch.Tensor | None, dims: torch.Tensor, use_act: torch.Tensor, *, pooling_type: str, head_dtype: torch.dtype | None, projector: torch.nn.Module | None, normalize: bool)` — [`L433`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L433) — Pool a padded bucket into ``[R_pad, out_dim]``.
- <a id="_to_device"></a>`_to_device(array: np.ndarray, device: torch.device | str)` — [`L538`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L538)
- <a id="build_dummy_static_pool_inputs"></a>`build_dummy_static_pool_inputs(spec: StaticPoolerSpec, num_tokens: int, num_reqs: int, device: torch.device | str)` — [`L640`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L640) — Precompile inputs with the exact runtime dtypes and shapes.
- <a id="build_pooling_metadata"></a>`build_pooling_metadata(batch, runner_requests: dict | None = None)` — [`L244`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L244) — Build PoolingMetadata with prompt_token_ids_cpu and persistent pooling_states.
- <a id="build_static_pool_inputs"></a>`build_static_pool_inputs(spec: StaticPoolerSpec, pooling_params: Sequence[Any], prompt_lens_np: np.ndarray, num_computed_np: np.ndarray, num_scheduled_np: np.ndarray, num_tokens_padded: int, padded_num_reqs: int, device: torch.device | str, last_token_idx: torch.Tensor | None = None)` — [`L542`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L542) — Build padded static-pool inputs on the host; None if ineligible.
- <a id="compute_pooling_kv_cache_cap_bytes"></a>`compute_pooling_kv_cache_cap_bytes(kv_cache_spec: dict[str, Any] | None, *, max_model_len: int, max_num_batched_tokens: int, max_num_seqs: int, async_scheduling: bool, long_prefill_token_threshold: int | None = 0, override_tokens: int | None = None)` — [`L785`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L785) — Invert vLLM's ``available // page_size // num_layers`` block sizing.
- <a id="compute_pooling_kv_cache_cap_tokens"></a>`compute_pooling_kv_cache_cap_tokens(*, max_model_len: int, max_num_batched_tokens: int, max_num_seqs: int, block_size: int, async_scheduling: bool, long_prefill_token_threshold: int | None = 0, override_tokens: int | None = None)` — [`L749`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L749) — Block-aligned KV token budget for a pure pooling (prefill-only) model.
- <a id="gate_unfinished"></a>`gate_unfinished(pooler_output: Any, finished: np.ndarray)` — [`L723`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L723) — Replace rows of unfinished requests with None (eager fallback).
- <a id="install_tpu_pooling_patches"></a>`install_tpu_pooling_patches()` — [`L178`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L178) — Install TPU-native pooling patches non-invasively (thread-safe, idempotent).
- <a id="iter_pooler_precompile_grid"></a>`iter_pooler_precompile_grid(num_tokens_paddings: Sequence[int], num_reqs_paddings: Sequence[int], max_num_reqs: int)` — [`L670`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L670) — Yield the reachable ``(num_tokens, num_reqs)`` static-pool buckets.
- <a id="resolve_static_pooler_spec"></a>`resolve_static_pooler_spec(model: Any, model_config: Any)` — [`L369`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L369) — Return ``(spec, reason)`` for the model's embed pooler.
- <a id="_install_tpu_pooling_patches_locked.safe_embed_forward"></a>`safe_embed_forward(self, pooled_data, pooling_metadata)` — [`L195`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L195)
- <a id="_install_tpu_pooling_patches_locked.safe_get_prompt_token_ids"></a>`safe_get_prompt_token_ids(self, prompt_token_ids)` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L229)
- <a id="static_pool"></a>`static_pool(hidden_states: torch.Tensor, inputs: StaticPoolInputs, spec: StaticPoolerSpec)` — [`L513`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L513) — Run the static pooler: compiled on TPU, eager elsewhere (CPU tests).
- <a id="unpack_static_pool_output"></a>`unpack_static_pool_output(out: StaticPoolerChunkOutput)` — [`L698`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L698) — One D2H per chunk; None for unfinished rows; ``row[:d]`` for matryoshka.

## Module values
- <a id="_STATIC_POOLING_TYPES._STATIC_POOLING_TYPES"></a>`_STATIC_POOLING_TYPES` — [`L328`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L328)
- <a id="_static_pool_compiled"></a>`_static_pool_compiled` — [`L493`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L493)
- <a id="_tpu_pooling_patches_installed"></a>`_tpu_pooling_patches_installed` — [`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L175)
- <a id="_tpu_pooling_patches_lock"></a>`_tpu_pooling_patches_lock` — [`L174`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/runner/tpu_pooling.py#L174)

