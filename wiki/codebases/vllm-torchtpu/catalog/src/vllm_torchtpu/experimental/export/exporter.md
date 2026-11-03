---
title: 'Module: src/vllm_torchtpu/experimental/export/exporter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/exporter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.exporter`/
symbols:
  _export_text_only_llm_functions: _export_text_only_llm_functions().
  export: export().
  _params_read_by_forward: _params_read_by_forward().
  _state_specs: _state_specs().
  _tensor_layouts: _tensor_layouts().
  _io_entry: _io_entry().
  _user_inputs: _user_inputs().
  _export_abstract_params: _export_abstract_params().
  _recurrent_serving_config: _recurrent_serving_config().
  _emit_model_companion_files: _emit_model_companion_files().
  _weight_input_entry: _weight_input_entry().
  _lowered_params: _lowered_params().
  _TensorLayout: _TensorLayout#
  _replicated: _replicated().
  _mesh_sharding: _mesh_sharding().
  _axis_sizes: _axis_sizes().
  _global_shape: _global_shape().
  _NUM_USER_INPUTS: _NUM_USER_INPUTS.
  _TensorLayout.sharding: _TensorLayout#sharding.
  Sharding: Sharding.
  _xla_option_overrides: _xla_option_overrides().
  _state_sharding: _state_sharding().
  _weight_reshapes: _weight_reshapes().
  _norm_params: _norm_params().
  _extra_user_inputs: _extra_user_inputs().
  _TensorLayout.shape: _TensorLayout#shape.
  _TensorLayout.lowered_shape: _TensorLayout#lowered_shape.
  _weight_slots: _weight_slots().
  _export_text_only_llm_functions._logits_entry: _export_text_only_llm_functions()._logits_entry().
  _TensorLayout.reshape: _TensorLayout#reshape.
  _USER_INPUT_NAMES: _USER_INPUT_NAMES.
  _lm_head_name: _lm_head_name().
  _AXIS_NAMES: _AXIS_NAMES.
  _MESH_AXIS_BY_ALIAS: _MESH_AXIS_BY_ALIAS.
  _MLIR_SHAPES: _MLIR_SHAPES.
  _option_value: _option_value().
  _axes_size: _axes_size().
  _main_args_read: _main_args_read().
  _hf_chat_template: _hf_chat_template().
---
# Module: [`src/vllm_torchtpu/experimental/export/exporter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py)

## Classes
### <a id="_TensorLayout"></a>`_TensorLayout`
- def: [`src/vllm_torchtpu/experimental/export/exporter.py:148`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L148) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: How a weight or constant appears globally and in the lowered modules.
- signature: `class _TensorLayout:`
- members:
  - <a id="_TensorLayout.lowered_shape"></a>`lowered_shape` — [`L153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L153)
  - <a id="_TensorLayout.reshape"></a>`reshape` — [`L155`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L155)
  - <a id="_TensorLayout.shape"></a>`shape` — [`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L151)
  - <a id="_TensorLayout.sharding"></a>`sharding` — [`L152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L152)
- uses (calls/refs, reference-scoped): [`Sharding`](exporter.md#Sharding)
- used by: [`_export_text_only_llm_functions`](exporter.md#_export_text_only_llm_functions), [`_tensor_layouts`](exporter.md#_tensor_layouts), [`_export_abstract_params`](exporter.md#_export_abstract_params), [`_weight_input_entry`](exporter.md#_weight_input_entry), [`_lowered_params`](exporter.md#_lowered_params), [`_weight_reshapes`](exporter.md#_weight_reshapes)

## Functions
- <a id="_axes_size"></a>`_axes_size(entry: str | list[str] | None, axis_sizes: Mapping[str, int])` — [`L122`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L122)
- <a id="_axis_sizes"></a>`_axis_sizes(cfg: api.TextOnlyLLMExportConfig)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L91) — Size of each mesh axis, keyed by `_AXIS_NAMES`.
- <a id="_emit_model_companion_files"></a>`_emit_model_companion_files(cfg: api.TextOnlyLLMExportConfig, output_dir: str)` — [`L716`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L716) — Copies companion files into the artifact; returns their `serving_config` entries. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_export_abstract_params"></a>`_export_abstract_params(params_map: Mapping[str, Any], layouts: Mapping[str, _TensorLayout], output_dir: str, *, constants: frozenset[str] = frozenset(), subdir: str = "subgraphs")` — [`L306`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L306) — Lowers the `abstract_params.mlir` identity, input `i` aliased to output `i`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_export_text_only_llm_functions"></a>`_export_text_only_llm_functions(model: api.ExportableTextOnlyLLM, params_map: Mapping[str, Any], layouts: Mapping[str, _TensorLayout], weight_slots: Mapping[str, int], output_dir: str, *, constants: frozenset[str] = frozenset(), subdir: str = "subgraphs")` — [`L489`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L489) — Lowers `forward`, `compute_logits`, and the samplers across all buckets. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_extra_user_inputs"></a>`_extra_user_inputs(model: api.ExportableTextOnlyLLM)` — [`L416`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L416) — `(name, shape)` of the int32 control inputs the model takes after its state.
- <a id="_global_shape"></a>`_global_shape(local_shape: Sequence[int], sharding: Sharding, axis_sizes: Mapping[str, int])` — [`L129`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L129) — The global shape whose shards, cut along `sharding`, are `local_shape`.
- <a id="_hf_chat_template"></a>`_hf_chat_template(hf_checkpoint_dir: str)` — [`L786`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L786) — The checkpoint's chat template, as HuggingFace finds it.
- <a id="_io_entry"></a>`_io_entry(*, arg_index: int, index: int, name: str, shape: Sequence[int], dtype: Any, argument_type: str, sharding: Sharding | None = None, buffer_donor: bool = False, is_input: bool = True)` — [`L227`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L227) — A `metadata.json` entry for a non-weight input or output. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_lm_head_name"></a>`_lm_head_name(params_map: Mapping[str, Any])` — [`L362`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L362) — The weight `compute_logits` projects with (tied embeddings fall back).
- <a id="_export_text_only_llm_functions._logits_entry"></a>`_logits_entry(hidden_states: Any, lm_head_w: Any)` — [`L644`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L644)
- <a id="_lowered_params"></a>`_lowered_params(params_map: Mapping[str, Any], layouts: Mapping[str, _TensorLayout])` — [`L208`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L208) — Param specs with the shard-local shapes the modules are lowered with. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_main_args_read"></a>`_main_args_read(mlir_text: str)` — [`L447`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L447) — Indices of the `@main` arguments that its body reads.
- <a id="_mesh_sharding"></a>`_mesh_sharding(raw: Any, rank: int)` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L101) — Converts `weight_mapper.infer_weight_sharding` output to a mesh sharding.
- <a id="_norm_params"></a>`_norm_params(params_map: Mapping[str, Any])` — [`L376`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L376)
- <a id="_option_value"></a>`_option_value(text: str)` — [`L76`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L76)
- <a id="_params_read_by_forward"></a>`_params_read_by_forward(model: api.ExportableTextOnlyLLM, params_map: Mapping[str, Any])` — [`L462`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L462) — Drops the forward weights that the forward graph never reads. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_recurrent_serving_config"></a>`_recurrent_serving_config(model: api.ExportableTextOnlyLLM)` — [`L428`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L428) — `num_state_slots` for a model with recurrent state, else nothing. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_replicated"></a>`_replicated(rank: int)` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L97)
- <a id="_state_sharding"></a>`_state_sharding(shape: Sequence[int], tp_size: int)` — [`L139`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L139) — KV cache shards hold this device's KV heads, the third dimension.
- <a id="_state_specs"></a>`_state_specs(model: api.ExportableTextOnlyLLM)` — [`L387`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L387) — Per-layer KV cache specs, from the model when it reports them. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_tensor_layouts"></a>`_tensor_layouts(model: api.ExportableTextOnlyLLM, params_map: Mapping[str, Any], constants: frozenset[str], axis_sizes: Mapping[str, int])` — [`L158`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L158) — Lays out every weight and constant as a global, sharded tensor. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_user_inputs"></a>`_user_inputs(cfg: api.TextOnlyLLMExportConfig, bucket_size: int)` — [`L256`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L256) — Returns `(name, shape)` of the int32 user inputs of `forward_bucket{B}`. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_weight_input_entry"></a>`_weight_input_entry(name: str, spec: Any, layout: _TensorLayout, *, arg_index: int, slot: int, buffer_donor: bool, constant: bool = False)` — [`L281`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L281) — Returns the `metadata.json` input entry for a weight or constant argument. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- <a id="_weight_reshapes"></a>`_weight_reshapes(layouts: Mapping[str, _TensorLayout])` — [`L221`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L221)
- <a id="_weight_slots"></a>`_weight_slots(params_map: Mapping[str, Any])` — [`L274`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L274) — Assigns each param its serving slot, after the user inputs.
- <a id="_xla_option_overrides"></a>`_xla_option_overrides()` — [`L61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L61) — The XLA flags libtpu runs with, for `env_option_overrides`.
- <a id="export"></a>`export(model: api.ExportableTextOnlyLLM, output_dir: str, *, subdir: str = "subgraphs")` — [`L809`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L809) — Exports an `ExportableTextOnlyLLM` to a serving artifact directory. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)

## Module values
- <a id="Sharding"></a>`Sharding` — [`L58`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L58)
- <a id="_AXIS_NAMES"></a>`_AXIS_NAMES` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L51)
- <a id="_MESH_AXIS_BY_ALIAS"></a>`_MESH_AXIS_BY_ALIAS` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L52)
- <a id="_MLIR_SHAPES"></a>`_MLIR_SHAPES` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L56)
- <a id="_NUM_USER_INPUTS"></a>`_NUM_USER_INPUTS` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L47)
- <a id="_USER_INPUT_NAMES"></a>`_USER_INPUT_NAMES` — [`L39`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/exporter.py#L39)

