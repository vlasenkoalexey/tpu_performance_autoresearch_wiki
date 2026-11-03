---
title: 'Module: src/vllm_torchtpu/experimental/export/universal_adapter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/universal_adapter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.universal_adapter`/
symbols:
  build_export_config_from_vllm: build_export_config_from_vllm().
  UniversalVllmExportableLLM._layer_state_specs: UniversalVllmExportableLLM#_layer_state_specs().
  make_attention_metadata: make_attention_metadata().
  UniversalVllmExportableLLM.abstract_states: UniversalVllmExportableLLM#abstract_states().
  UniversalVllmExportableLLM.abstract_params: UniversalVllmExportableLLM#abstract_params().
  UniversalVllmExportableLLM.fit_num_blocks_to_hbm: UniversalVllmExportableLLM#fit_num_blocks_to_hbm().
  load_vllm_model: load_vllm_model().
  UniversalVllmExportableLLM.forward: UniversalVllmExportableLLM#forward().
  UniversalVllmExportableLLM._export_config: UniversalVllmExportableLLM#_export_config.
  UniversalVllmExportableLLM._model: UniversalVllmExportableLLM#_model.
  UniversalVllmExportableLLM._state_bytes: UniversalVllmExportableLLM#_state_bytes().
  UniversalVllmExportableLLM._patched_rope_modules: UniversalVllmExportableLLM#_patched_rope_modules.
  UniversalVllmExportableLLM._vllm_config: UniversalVllmExportableLLM#_vllm_config.
  _extract_hf_field: _extract_hf_field().
  UniversalVllmExportableLLM._invoke_backbone: UniversalVllmExportableLLM#_invoke_backbone().
  UniversalVllmExportableLLM.extra_user_inputs: UniversalVllmExportableLLM#extra_user_inputs().
  UniversalVllmExportableLLM.compute_logits: UniversalVllmExportableLLM#compute_logits().
  UniversalVllmExportableLLM._named_attention_layers: UniversalVllmExportableLLM#_named_attention_layers().
  init_export_distributed_environment: init_export_distributed_environment().
  _recurrent_state_specs: _recurrent_state_specs().
  UniversalVllmExportableLLM._has_recurrent_layers: UniversalVllmExportableLLM#_has_recurrent_layers().
  _is_recurrent_layer: _is_recurrent_layer().
  UniversalVllmExportableLLM.export_config: UniversalVllmExportableLLM#export_config().
  UniversalVllmExportableLLM.constant_axis_values: UniversalVllmExportableLLM#constant_axis_values().
  create_export_vllm_config: create_export_vllm_config().
  UniversalVllmExportableLLM: UniversalVllmExportableLLM#
  UniversalVllmExportableLLM._attention_layers: UniversalVllmExportableLLM#_attention_layers().
  check_supported_parallelism: check_supported_parallelism().
  default_req_buckets: default_req_buckets().
  run_model_loader: run_model_loader().
  load_dummy_vllm_model: load_dummy_vllm_model().
  UniversalVllmExportableLLM._call: UniversalVllmExportableLLM#_call().
  UniversalVllmExportableLLM._local_logits: UniversalVllmExportableLLM#_local_logits().
  UniversalVllmExportableLLM.__init__: UniversalVllmExportableLLM#__init__().
  UniversalVllmExportableLLM.model: UniversalVllmExportableLLM#model().
  UniversalVllmExportableLLM.vllm_config: UniversalVllmExportableLLM#vllm_config().
  UniversalVllmExportableLLM.constant_names: UniversalVllmExportableLLM#constant_names().
  UniversalVllmExportableLLM.sample_tokens: UniversalVllmExportableLLM#sample_tokens().
  _MAX_CONSTANT_ELEMENTS: _MAX_CONSTANT_ELEMENTS.
  _MIN_REQ_BUCKET: _MIN_REQ_BUCKET.
  _min_smem_page_size: _min_smem_page_size().
  resolve_hf_checkpoint_dir: resolve_hf_checkpoint_dir().
  _create_single_device_tpu_mesh: _create_single_device_tpu_mesh().
  _backbone_kwargs: _backbone_kwargs().
  _weights_bound_in_place: _weights_bound_in_place().
  _check_recurrent_layer_supported: _check_recurrent_layer_supported().
  UniversalVllmExportableLLM.pallas_interpret: UniversalVllmExportableLLM#pallas_interpret().
---
# Module: [`src/vllm_torchtpu/experimental/export/universal_adapter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py)

## Classes
### <a id="UniversalVllmExportableLLM"></a>`UniversalVllmExportableLLM`  ·  implements/extends ExportableTextOnlyLLM
- def: [`src/vllm_torchtpu/experimental/export/universal_adapter.py:622`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L622)
- doc: Universal adapter wrapping any vLLM causal LM for standardized AOT export.
- signature: `class UniversalVllmExportableLLM(api.ExportableTextOnlyLLM):`
- members:
  - <a id="UniversalVllmExportableLLM._attention_layers"></a>`_attention_layers(self)` — [`L856`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L856) — Returns the ordered attention layers of the wrapped model.
  - <a id="UniversalVllmExportableLLM._layer_state_specs"></a>`_layer_state_specs(self)` — [`L863`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L863) — The state tensors of each attention layer, or None if any is unknown. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="UniversalVllmExportableLLM._named_attention_layers"></a>`_named_attention_layers(self)` — [`L836`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L836) — Returns the ordered `(layer name, layer)` attention layers of the model.
  - <a id="UniversalVllmExportableLLM._state_bytes"></a>`_state_bytes(self, num_blocks: int)` — [`L750`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L750) — Bytes of this rank's state tensors when exported with `num_blocks`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="UniversalVllmExportableLLM.abstract_params"></a>`abstract_params(self)` — [`L762`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L762) — Builds abstract specs for the model's parameters and buffers. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="UniversalVllmExportableLLM.abstract_states"></a>`abstract_states(self)` — [`L957`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L957) — Returns the state tensors of every attention layer, in layer order. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="UniversalVllmExportableLLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor, lm_head_weight: torch.Tensor)` — [`L1125`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L1125) — Projects `hidden_states[R, hidden_size]` to `logits[R, vocab_size]`.
  - <a id="UniversalVllmExportableLLM.constant_axis_values"></a>`constant_axis_values(self, name: str)` — [`L816`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L816) — Values of buffer `name` on every tensor-parallel rank, in rank order.
  - <a id="UniversalVllmExportableLLM.constant_names"></a>`constant_names(self)` — [`L811`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L811) — Names in `abstract_params()` that are buffers rather than parameters.
  - <a id="UniversalVllmExportableLLM.export_config"></a>`export_config(self)` — [`L687`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L687)
  - <a id="UniversalVllmExportableLLM.extra_user_inputs"></a>`extra_user_inputs(self)` — [`L947`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L947) — Control inputs beyond the standard six that `forward` takes.
  - <a id="UniversalVllmExportableLLM.fit_num_blocks_to_hbm"></a>`fit_num_blocks_to_hbm(self, gpu_memory_utilization: float, kv_cache_memory_bytes: int | None = None, devices: Sequence[Any] | None = None)` — [`L691`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L691) — Sets `num_blocks` to the KV blocks that fit this rank's KV budget. — documented in [kv-cache-layout-and-hbm-budget](../../../../../concepts/kv-cache-layout-and-hbm-budget.md)
  - <a id="UniversalVllmExportableLLM.forward"></a>`forward(self, weights: Mapping[str, Any], kv_caches: Sequence[Any], *, input_ids: Any, positions: Any, kv_lens: Any, block_tables: Any, query_start_loc: Any, req_dist: Any, **extra_controls: Any)` — [`L976`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L976) — Executes one flattened continuous-batching forward pass.
  - <a id="UniversalVllmExportableLLM.model"></a>`model(self)` — [`L673`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L673) — Returns the underlying PyTorch `nn.Module`.
  - <a id="UniversalVllmExportableLLM.pallas_interpret"></a>`pallas_interpret(self)` — [`L683`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L683)
  - <a id="UniversalVllmExportableLLM.sample_tokens"></a>`sample_tokens(self, logits: Any, *, temperature: Any | None = None, top_k: Any | None = None, top_p: Any | None = None, min_p: Any | None = None, uniform: Any | None = None, repetition_penalty: Any | None = None, presence_penalty: Any | None = None, frequency_penalty: Any | None = None, history: Any | None = None, output_start: Any | None = None)` — [`L1159`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L1159) — Samples token ids `i64[R, 1]` from `logits[R, vocab_size]`.
  - <a id="UniversalVllmExportableLLM.vllm_config"></a>`vllm_config(self)` — [`L678`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L678) — Returns the optional `VllmConfig`.
- protocol/private: <a id="UniversalVllmExportableLLM.__init__"></a>`__init__`[`L637`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L637), <a id="UniversalVllmExportableLLM._call"></a>`_call`[`L1047`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L1047), <a id="UniversalVllmExportableLLM._export_config"></a>`_export_config`[`L658`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L658), <a id="UniversalVllmExportableLLM._has_recurrent_layers"></a>`_has_recurrent_layers`[`L860`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L860), <a id="UniversalVllmExportableLLM._invoke_backbone"></a>`_invoke_backbone`[`L1037`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L1037), <a id="UniversalVllmExportableLLM._local_logits"></a>`_local_logits`[`L1142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L1142), <a id="UniversalVllmExportableLLM._model"></a>`_model`[`L659`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L659), <a id="UniversalVllmExportableLLM._patched_rope_modules"></a>`_patched_rope_modules`[`L660`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L660), <a id="UniversalVllmExportableLLM._vllm_config"></a>`_vllm_config`[`L648`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L648)
- uses (calls/refs, reference-scoped): [`build_export_config_from_vllm`](universal_adapter.md#build_export_config_from_vllm), [`set_vllm_model_wrapper_context`](../../models/vllm/vllm_model_wrapper_context.md#set_vllm_model_wrapper_context), [`ShapeDtypeStruct`](api.md#ShapeDtypeStruct), [`PallasAttentionBackend`](../../layers/adapter/attention.md#PallasAttentionBackend), [`make_attention_metadata`](universal_adapter.md#make_attention_metadata), [`dtype_name`](tpu_lowering.md#dtype_name), [`get_kv_cache_shape`](../../layers/adapter/attention.md#PallasMLAttentionBackend.get_kv_cache_shape), [`PallasMLAttentionBackend`](../../layers/adapter/attention.md#PallasMLAttentionBackend), [`PallasAttentionBackendImpl`](../../layers/adapter/attention.md#PallasAttentionBackendImpl), [`head_size`](../../layers/adapter/attention.md#PallasAttentionBackendImpl.head_size), [`ExportableTextOnlyLLM`](api.md#ExportableTextOnlyLLM), [`trace`](trace.md#trace), [`compute_hbm_budget`](../../utils.md#compute_hbm_budget), [`get_kv_cache_shape`](../../layers/adapter/attention.md#PallasAttentionBackend.get_kv_cache_shape), [`TextOnlyLLMExportConfig`](api.md#TextOnlyLLMExportConfig), [`patch_in_graph_rotary_embedding`](rope_patch.md#patch_in_graph_rotary_embedding), [`tensor_parallel_size`](api.md#ModelExportConfig.tensor_parallel_size), [`torch_dtype`](tpu_lowering.md#torch_dtype), [`num_blocks`](api.md#TextOnlyLLMExportConfig.num_blocks), [`dispatch_sample_tokens`](sampling.md#dispatch_sample_tokens), [`PallasMLAttentionBackendImpl`](../../layers/adapter/attention.md#PallasMLAttentionBackendImpl), [`block_size`](api.md#TextOnlyLLMExportConfig.block_size), [`max_num_seqs`](api.md#TextOnlyLLMExportConfig.max_num_seqs), [`vocab_size`](api.md#TextOnlyLLMExportConfig.vocab_size), [`_recurrent_state_specs`](universal_adapter.md#_recurrent_state_specs), [`shape`](api.md#ShapeDtypeStruct.shape), [`num_state_slots`](api.md#TextOnlyLLMExportConfig.num_state_slots), [`_is_recurrent_layer`](universal_adapter.md#_is_recurrent_layer), [`dtype`](api.md#ShapeDtypeStruct.dtype), [`dtype`](api.md#TextOnlyLLMExportConfig.dtype), [`num_kv_heads`](../../layers/adapter/attention.md#PallasAttentionBackendImpl.num_kv_heads), [`infer_weight_sharding`](weight_mapper.md#infer_weight_sharding), [`tied_lm_head_alias`](weight_mapper.md#tied_lm_head_alias), [`available`](../../utils.md#HbmBudget.available), [`load_dummy_vllm_model`](universal_adapter.md#load_dummy_vllm_model), [`cap`](../../utils.md#HbmBudget.cap), [`compute_mrope_dim_modalities`](rope_patch.md#compute_mrope_dim_modalities), [`head_dim`](api.md#TextOnlyLLMExportConfig.head_dim), [`num_kv_heads`](api.md#TextOnlyLLMExportConfig.num_kv_heads), [`num_layers`](api.md#TextOnlyLLMExportConfig.num_layers)  (+8 more)
- used by: [`run_export_from_args`](cli.md#run_export_from_args), [`ExportableTextOnlyLLM`](api.md#ExportableTextOnlyLLM), [`export_config`](api.md#ExportableTextOnlyLLM.export_config), [`abstract_params`](api.md#ExportableModel.abstract_params), [`compute_logits`](api.md#ExportableTextOnlyLLM.compute_logits), [`forward`](api.md#ExportableTextOnlyLLM.forward), [`pallas_interpret`](api.md#ExportableModel.pallas_interpret), [`sample_tokens`](api.md#ExportableTextOnlyLLM.sample_tokens)

## Functions
- <a id="_backbone_kwargs"></a>`_backbone_kwargs(backbone: nn.Module, *, input_ids: Any, positions: Any, kv_caches: Sequence[Any], attn_metadata: Any)` — [`L477`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L477) — Keyword arguments for `backbone.forward`, chosen from its signature.
- <a id="_check_recurrent_layer_supported"></a>`_check_recurrent_layer_supported(layer: Any)` — [`L572`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L572) — Raises unless export can bind `layer`'s state and drive its forward.
- <a id="_create_single_device_tpu_mesh"></a>`_create_single_device_tpu_mesh()` — [`L324`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L324) — Creates a 1-device mesh on `axis_names=('model',)` for Pallas kernels.
- <a id="_extract_hf_field"></a>`_extract_hf_field(hf_config: Any, *keys: str, default: Any = None)` — [`L87`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L87) — Reads the first present attribute or dict entry from `hf_config`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_is_recurrent_layer"></a>`_is_recurrent_layer(layer: Any)` — [`L563`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L563) — Whether `layer` keeps fixed-size recurrent state (e.g. GDN linear attention).
- <a id="_min_smem_page_size"></a>`_min_smem_page_size(parallel_cfg: Any, max_num_seqs: int, max_model_len: int)` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L104) — Smallest power-of-two page size whose block table fits half of SMEM.
- <a id="_recurrent_state_specs"></a>`_recurrent_state_specs(layer: Any, num_slots: int, tp_size: int)` — [`L590`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L590) — Device-local `[num_slots, ...]` specs of a recurrent layer's two states.
- <a id="_weights_bound_in_place"></a>`_weights_bound_in_place(module: nn.Module, weights: Mapping[str, Any])` — [`L503`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L503) — Rebinds `weights` on plain objects and restores shared submodules on exit.
- <a id="build_export_config_from_vllm"></a>`build_export_config_from_vllm(vllm_config: Any, *, model_name: str | None = None, hf_checkpoint_dir: str | None = None, target_tpu: str | None = None, token_buckets: Sequence[int] | None = None, req_buckets: Sequence[int] | None = None)` — [`L168`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L168) — Derives a `TextOnlyLLMExportConfig` from a `VllmConfig` (or mock config). — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="check_supported_parallelism"></a>`check_supported_parallelism(parallel_cfg: Any)` — [`L122`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L122) — Returns `(dp, pp)` after rejecting data or pipeline parallel sizes above 1.
- <a id="create_export_vllm_config"></a>`create_export_vllm_config(args: Any)` — [`L391`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L391) — Creates the `VllmConfig` an export runs with from parsed `EngineArgs`.
- <a id="default_req_buckets"></a>`default_req_buckets(max_num_seqs: int)` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L44) — Request buckets as the vLLM TPU runner pads `num_reqs` (`_get_req_paddings`).
- <a id="init_export_distributed_environment"></a>`init_export_distributed_environment(vllm_config: Any)` — [`L340`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L340) — Joins the process group the export launcher set up for this rank.
- <a id="load_dummy_vllm_model"></a>`load_dummy_vllm_model(vllm_config: Any)` — [`L385`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L385) — Loads a vLLM model with `load_format='dummy'` on TPU (zero disk weight IO).
- <a id="load_vllm_model"></a>`load_vllm_model(vllm_config: Any, *, load_format: str)` — [`L406`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L406) — Loads a vLLM model with `load_format`, running vLLM's weight processing. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="make_attention_metadata"></a>`make_attention_metadata(*, input_positions: Any, block_tables: Any = None, seq_lens: Any = None, query_start_loc: Any = None, request_distribution: Any = None, mamba_state_indices: Any = None, mamba_slot_read_offsets: Any = None, mamba_ckpt_indices: Any = None, mamba_request_distribution: Any = None)` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L61) — Constructs an `AttentionMetadata` instance directly from control tensors. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="resolve_hf_checkpoint_dir"></a>`resolve_hf_checkpoint_dir(model: str | None)` — [`L137`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L137) — Returns the local checkpoint directory for a path or a Hub repo id.
- <a id="run_model_loader"></a>`run_model_loader(vllm_config: Any)` — [`L361`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L361) — Builds the model and loads its weights with vLLM's loader for `load_config`.

## Module values
- <a id="_MAX_CONSTANT_ELEMENTS"></a>`_MAX_CONSTANT_ELEMENTS` — [`L474`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L474)
- <a id="_MIN_REQ_BUCKET"></a>`_MIN_REQ_BUCKET` — [`L41`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/universal_adapter.py#L41)

