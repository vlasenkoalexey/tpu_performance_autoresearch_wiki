---
title: 'Module: src/vllm_torchtpu/model_loader_patches.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/model_loader_patches.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.model_loader_patches`/
symbols:
  logger: logger.
  ExpertParamStager.flush: ExpertParamStager#flush().
  _sharded_runai_weights_iterator: _sharded_runai_weights_iterator().
  _OnlineFp8LayerFinisher._owners: _OnlineFp8LayerFinisher#_owners.
  _OnlineFp8LayerFinisher.consumed: _OnlineFp8LayerFinisher#consumed().
  ExpertParamStager.host_param: ExpertParamStager#host_param().
  patch_moe_expert_write_staging.weight_loader: patch_moe_expert_write_staging().weight_loader().
  evict_loaded_weights_page_cache: evict_loaded_weights_page_cache().
  patch_runai_sharded_expert_streaming: patch_runai_sharded_expert_streaming().
  patch_default_loader_ep_weight_filter: patch_default_loader_ep_weight_filter().
  patch_default_model_loader_page_cache: patch_default_model_loader_page_cache().
  patch_moe_expert_write_staging: patch_moe_expert_write_staging().
  patch_runai_sharded_expert_streaming._get_weights_iterator: patch_runai_sharded_expert_streaming()._get_weights_iterator().
  ExpertParamStager.written: ExpertParamStager#written().
  ExpertParamStager.flush_all: ExpertParamStager#flush_all().
  patch_moe_expert_write_staging.process_weights_after_loading: patch_moe_expert_write_staging().process_weights_after_loading().
  ExpertParamStager._staged: ExpertParamStager#_staged.
  _should_skip_weight_tpu: _should_skip_weight_tpu().
  patch_default_loader_ep_weight_filter.safetensors_weights_iterator: patch_default_loader_ep_weight_filter().safetensors_weights_iterator().
  _unused_weight_predicate._unused_weight_predicate: _unused_weight_predicate._unused_weight_predicate.
  _patch_runai_local_rank_discovery: _patch_runai_local_rank_discovery().
  _start_ep_range_prefetch: _start_ep_range_prefetch().
  _start_ep_range_prefetch.run: _start_ep_range_prefetch().run().
  _evict_checkpoint_page_cache: _evict_checkpoint_page_cache().
  ExpertWriteTracker.record: ExpertWriteTracker#record().
  _should_skip: _should_skip().
  _OnlineFp8LayerFinisher._layers: _OnlineFp8LayerFinisher#_layers.
  _sharded_runai_weights_iterator._device_sync: _sharded_runai_weights_iterator()._device_sync().
  ExpertParamStager._pool: ExpertParamStager#_pool.
  ExpertParamStager.flushed: ExpertParamStager#flushed.
  _loaded_weight_files._loaded_weight_files: _loaded_weight_files._loaded_weight_files.
  _compute_local_expert_ids: _compute_local_expert_ids().
  patch_default_loader_ep_weight_filter._get_weights_iterator: patch_default_loader_ep_weight_filter()._get_weights_iterator().
  patch_default_loader_ep_weight_filter._get_weights_iterator._iter_skipping_unused: patch_default_loader_ep_weight_filter()._get_weights_iterator()._iter_skipping_unused().
  _local_tensor_ranges: _local_tensor_ranges().
  _evict_one_checkpoint_file: _evict_one_checkpoint_file().
  patch_default_model_loader_page_cache.load_weights: patch_default_model_loader_page_cache().load_weights().
  ExpertParamStager._tracker: ExpertParamStager#_tracker.
  ExpertParamStager.staging: ExpertParamStager#staging().
  _OnlineFp8LayerFinisher._pending: _OnlineFp8LayerFinisher#_pending.
  _OnlineFp8LayerFinisher.__init__: _OnlineFp8LayerFinisher#__init__().
  ExpertParamStager.__len__: ExpertParamStager#__len__().
  _sharded_runai_weights_iterator._flush: _sharded_runai_weights_iterator()._flush().
  ExpertWriteTracker._seen: ExpertWriteTracker#_seen.
  _rss_gib: _rss_gib().
  ExpertParamStager.written_early: ExpertParamStager#written_early.
  _EXPERT_WEIGHT_SUFFIXES: _EXPERT_WEIGHT_SUFFIXES.
  _OnlineFp8LayerFinisher: _OnlineFp8LayerFinisher#
  _patch_runai_local_rank_discovery.find_local_ranks: _patch_runai_local_rank_discovery().find_local_ranks().
  patch_runai_sharded_expert_streaming.load_weights: patch_runai_sharded_expert_streaming().load_weights().
  patch_default_model_loader_page_cache._prepare_weights: patch_default_model_loader_page_cache()._prepare_weights().
  _SHARDS_PER_EXPERT: _SHARDS_PER_EXPERT.
  ExpertWriteTracker: ExpertWriteTracker#
  _UPLOAD_CHUNK_BYTES: _UPLOAD_CHUNK_BYTES.
  _MAX_STAGED: _MAX_STAGED.
  ExpertParamStager: ExpertParamStager#
  ExpertWriteTracker.__init__: ExpertWriteTracker#__init__().
  ExpertParamStager.__init__: ExpertParamStager#__init__().
---
# Module: [`src/vllm_torchtpu/model_loader_patches.py`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py)

## Classes
### <a id="ExpertParamStager"></a>`ExpertParamStager`
- def: [`src/vllm_torchtpu/model_loader_patches.py:821`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L821)
- doc: Host stand-ins for expert parameters while their experts stream in.
- signature: `class ExpertParamStager:`
- members:
  - <a id="ExpertParamStager.flush"></a>`flush(self, param: torch.nn.Parameter)` — [`L875`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L875) — Upload ``param``'s stand-in to the device in slices and join them. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="ExpertParamStager.flush_all"></a>`flush_all(self)` — [`L913`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L913)
  - <a id="ExpertParamStager.host_param"></a>`host_param(self, param: torch.nn.Parameter)` — [`L846`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L846)
  - <a id="ExpertParamStager.staging"></a>`staging(self, param: torch.nn.Parameter)` — [`L838`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L838) — Whether writes to ``param`` still go through a stand-in.
  - <a id="ExpertParamStager.written"></a>`written(self, param: torch.nn.Parameter, expert_id: int, shard_id: str)` — [`L868`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L868) — Note one expert write; flush the parameter if it is complete.
  - <a id="ExpertParamStager.flushed"></a>`flushed` — [`L836`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L836)
  - <a id="ExpertParamStager.written_early"></a>`written_early` — [`L835`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L835)
- protocol/private: <a id="ExpertParamStager.__init__"></a>`__init__`[`L831`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L831), <a id="ExpertParamStager.__len__"></a>`__len__`[`L918`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L918), <a id="ExpertParamStager._pool"></a>`_pool`[`L833`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L833), <a id="ExpertParamStager._staged"></a>`_staged`[`L832`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L832), <a id="ExpertParamStager._tracker"></a>`_tracker`[`L834`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L834)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](utils.md#synchronize_tensors), [`logger`](model_loader_patches.md#logger), [`record`](model_loader_patches.md#ExpertWriteTracker.record), [`_rss_gib`](model_loader_patches.md#_rss_gib), [`ExpertWriteTracker`](model_loader_patches.md#ExpertWriteTracker), [`_MAX_STAGED`](model_loader_patches.md#_MAX_STAGED), [`_UPLOAD_CHUNK_BYTES`](model_loader_patches.md#_UPLOAD_CHUNK_BYTES)
- used by: [`weight_loader`](model_loader_patches.md#patch_moe_expert_write_staging.weight_loader), [`patch_moe_expert_write_staging`](model_loader_patches.md#patch_moe_expert_write_staging), [`process_weights_after_loading`](model_loader_patches.md#patch_moe_expert_write_staging.process_weights_after_loading)

### <a id="ExpertWriteTracker"></a>`ExpertWriteTracker`
- def: [`src/vllm_torchtpu/model_loader_patches.py:784`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L784)
- doc: Tells when every expert of a parameter has been written.
- signature: `class ExpertWriteTracker:`
- members:
  - <a id="ExpertWriteTracker.record"></a>`record(self, param: torch.Tensor, expert_id: int, shard_id: str)` — [`L798`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L798)
- protocol/private: <a id="ExpertWriteTracker.__init__"></a>`__init__`[`L795`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L795), <a id="ExpertWriteTracker._seen"></a>`_seen`[`L796`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L796)
- uses (calls/refs, reference-scoped): [`_SHARDS_PER_EXPERT`](model_loader_patches.md#_SHARDS_PER_EXPERT)
- used by: [`written`](model_loader_patches.md#ExpertParamStager.written), [`_tracker`](model_loader_patches.md#ExpertParamStager._tracker)

### <a id="_OnlineFp8LayerFinisher"></a>`_OnlineFp8LayerFinisher`
- def: [`src/vllm_torchtpu/model_loader_patches.py:175`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L175)
- doc: Quantizes each decoder layer after all its checkpoint tensors are consumed.
- signature: `class _OnlineFp8LayerFinisher:`
- members:
  - <a id="_OnlineFp8LayerFinisher.consumed"></a>`consumed(self, name: str)` — [`L217`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L217) — documented in [quantization-methods](../../../concepts/quantization-methods.md)
- protocol/private: <a id="_OnlineFp8LayerFinisher.__init__"></a>`__init__`[`L178`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L178), <a id="_OnlineFp8LayerFinisher._layers"></a>`_layers`[`L191`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L191), <a id="_OnlineFp8LayerFinisher._owners"></a>`_owners`[`L195`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L195), <a id="_OnlineFp8LayerFinisher._pending"></a>`_pending`[`L194`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L194)
- uses (calls/refs, reference-scoped): [`process_weights_after_loading`](layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU.process_weights_after_loading), [`logger`](model_loader_patches.md#logger), [`VllmFp8LinearMethodTPU`](layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU), [`online_fp8`](layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU.online_fp8)
- used by: [`_sharded_runai_weights_iterator`](model_loader_patches.md#_sharded_runai_weights_iterator)

## Functions
- <a id="_compute_local_expert_ids"></a>`_compute_local_expert_ids()` — [`L112`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L112) — Local expert ids for this rank, or None when filtering is off.
- <a id="_sharded_runai_weights_iterator._device_sync"></a>`_device_sync()` — [`L337`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L337)
- <a id="_evict_checkpoint_page_cache"></a>`_evict_checkpoint_page_cache(files: list[str])` — [`L693`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L693) — Drop clean host page cache for weight files via posix_fadvise.
- <a id="_evict_one_checkpoint_file"></a>`_evict_one_checkpoint_file(fpath: str)` — [`L671`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L671)
- <a id="_sharded_runai_weights_iterator._flush"></a>`_flush(path: str)` — [`L275`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L275)
- <a id="patch_runai_sharded_expert_streaming._get_weights_iterator"></a>`_get_weights_iterator(self, model_or_path: str, revision: str | None)` — [`L442`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L442)
- <a id="patch_default_loader_ep_weight_filter._get_weights_iterator"></a>`_get_weights_iterator(self, source)` — [`L564`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L564)
- <a id="patch_default_loader_ep_weight_filter._get_weights_iterator._iter_skipping_unused"></a>`_iter_skipping_unused()` — [`L569`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L569)
- <a id="_local_tensor_ranges"></a>`_local_tensor_ranges(path: str, local_expert_ids: set[int])` — [`L592`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L592) — Merged [start, end) file offsets of the tensors this rank keeps.
- <a id="_patch_runai_local_rank_discovery"></a>`_patch_runai_local_rank_discovery()` — [`L382`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L382) — Reuse the exported host-rank count instead of rediscovering it.
- <a id="patch_default_model_loader_page_cache._prepare_weights"></a>`_prepare_weights(self, *args, **kwargs)` — [`L738`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L738)
- <a id="_rss_gib"></a>`_rss_gib()` — [`L816`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L816)
- <a id="_sharded_runai_weights_iterator"></a>`_sharded_runai_weights_iterator(hf_weights_files: list[str], local_expert_ids: set[int], use_tqdm_on_load: bool, model: torch.nn.Module | None = None)` — [`L231`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L231) — Stream only this rank's tensors from the safetensors files.
- <a id="_should_skip"></a>`_should_skip(name: str, local_expert_ids: set[int])` — [`L80`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L80)
- <a id="_should_skip_weight_tpu"></a>`_should_skip_weight_tpu(weight_name: str, local_expert_ids: set[int] | None)` — [`L91`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L91) — Drop-in replacement for vLLM's ``should_skip_weight``.
- <a id="_start_ep_range_prefetch"></a>`_start_ep_range_prefetch(sorted_files: list[str], local_expert_ids: set[int], num_threads: int, block_size: int)` — [`L614`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L614) — Read this rank's tensors into the page cache in a background thread.
- <a id="evict_loaded_weights_page_cache"></a>`evict_loaded_weights_page_cache()` — [`L761`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L761) — Evict host page cache for every weight file loaded so far.
- <a id="_patch_runai_local_rank_discovery.find_local_ranks"></a>`find_local_ranks(self)` — [`L409`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L409)
- <a id="patch_runai_sharded_expert_streaming.load_weights"></a>`load_weights(self, model, model_config)` — [`L435`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L435)
- <a id="patch_default_model_loader_page_cache.load_weights"></a>`load_weights(self, model: torch.nn.Module, model_config: ModelConfig)` — [`L744`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L744)
- <a id="patch_default_loader_ep_weight_filter"></a>`patch_default_loader_ep_weight_filter()` — [`L488`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L488) — Widen ``DefaultModelLoader``'s EP weight filter to MXFP4 names.
- <a id="patch_default_model_loader_page_cache"></a>`patch_default_model_loader_page_cache()` — [`L710`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L710) — Evict host page cache for weight files once loaded into TPU HBM. — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="patch_moe_expert_write_staging"></a>`patch_moe_expert_write_staging()` — [`L922`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L922) — Load expert parameters through host stand-ins written to the device — documented in [kv-cache-layout-and-hbm-budget](../../../concepts/kv-cache-layout-and-hbm-budget.md)
- <a id="patch_runai_sharded_expert_streaming"></a>`patch_runai_sharded_expert_streaming()` — [`L419`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L419) — Make ``RunaiModelStreamerLoader`` fetch only this rank's tensors.
- <a id="patch_moe_expert_write_staging.process_weights_after_loading"></a>`process_weights_after_loading(model, model_config, target_device)` — [`L997`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L997)
- <a id="_start_ep_range_prefetch.run"></a>`run()` — [`L628`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L628)
- <a id="patch_default_loader_ep_weight_filter.safetensors_weights_iterator"></a>`safetensors_weights_iterator(hf_weights_files, use_tqdm_on_load, safetensors_load_strategy=None, local_expert_ids=None, **kwargs)` — [`L526`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L526)
- <a id="patch_moe_expert_write_staging.weight_loader"></a>`weight_loader(self, param, loaded_weight, weight_name, shard_id, expert_id, return_success=False)` — [`L951`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L951)

## Module values
- <a id="_EXPERT_WEIGHT_SUFFIXES"></a>`_EXPERT_WEIGHT_SUFFIXES` — [`L73`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L73)
- <a id="_MAX_STAGED"></a>`_MAX_STAGED` — [`L813`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L813)
- <a id="_SHARDS_PER_EXPERT"></a>`_SHARDS_PER_EXPERT` — [`L781`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L781)
- <a id="_UPLOAD_CHUNK_BYTES"></a>`_UPLOAD_CHUNK_BYTES` — [`L811`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L811)
- <a id="_loaded_weight_files._loaded_weight_files"></a>`_loaded_weight_files` — [`L758`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L758)
- <a id="_unused_weight_predicate._unused_weight_predicate"></a>`_unused_weight_predicate` — [`L77`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L77)
- <a id="logger"></a>`logger` — [`L67`](../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/model_loader_patches.py#L67)

