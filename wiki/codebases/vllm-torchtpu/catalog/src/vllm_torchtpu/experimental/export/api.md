---
title: 'Module: src/vllm_torchtpu/experimental/export/api.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/experimental/export/api.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.experimental.export.api`/
symbols:
  ShapeDtypeStruct: ShapeDtypeStruct#
  ExportableTextOnlyLLM: ExportableTextOnlyLLM#
  TextOnlyLLMExportConfig: TextOnlyLLMExportConfig#
  ExportableTextOnlyLLM.export_config: ExportableTextOnlyLLM#export_config().
  ModelExportConfig.tensor_parallel_size: ModelExportConfig#tensor_parallel_size().
  TextOnlyLLMExportConfig.max_num_pages: TextOnlyLLMExportConfig#max_num_pages().
  TextOnlyLLMExportConfig.num_blocks: TextOnlyLLMExportConfig#num_blocks.
  TextOnlyLLMExportConfig.hf_checkpoint_dir: TextOnlyLLMExportConfig#hf_checkpoint_dir.
  TextOnlyLLMExportConfig.block_size: TextOnlyLLMExportConfig#block_size.
  TextOnlyLLMExportConfig.vocab_size: TextOnlyLLMExportConfig#vocab_size.
  TextOnlyLLMExportConfig.max_num_seqs: TextOnlyLLMExportConfig#max_num_seqs.
  ShapeDtypeStruct.shape: ShapeDtypeStruct#shape.
  ModelExportConfig: ModelExportConfig#
  TextOnlyLLMExportConfig.num_state_slots: TextOnlyLLMExportConfig#num_state_slots().
  ShapeDtypeStruct.dtype: ShapeDtypeStruct#dtype.
  TextOnlyLLMExportConfig.dtype: TextOnlyLLMExportConfig#dtype.
  TextOnlyLLMExportConfig.__post_init__: TextOnlyLLMExportConfig#__post_init__().
  ExportableModel.export_config: ExportableModel#export_config().
  TextOnlyLLMExportConfig.max_cu_seqs: TextOnlyLLMExportConfig#max_cu_seqs().
  ExportableModel: ExportableModel#
  TextOnlyLLMExportConfig.hidden_size: TextOnlyLLMExportConfig#hidden_size.
  TextOnlyLLMExportConfig.max_model_len: TextOnlyLLMExportConfig#max_model_len.
  ExportableModel.abstract_params: ExportableModel#abstract_params().
  ExportableTextOnlyLLM.forward: ExportableTextOnlyLLM#forward().
  ExportableTextOnlyLLM.compute_logits: ExportableTextOnlyLLM#compute_logits().
  ShapeDtypeStruct.sharding: ShapeDtypeStruct#sharding.
  ModelExportConfig.num_replicas: ModelExportConfig#num_replicas.
  ModelExportConfig.num_partitions: ModelExportConfig#num_partitions.
  TextOnlyLLMExportConfig.num_layers: TextOnlyLLMExportConfig#num_layers.
  TextOnlyLLMExportConfig.num_kv_heads: TextOnlyLLMExportConfig#num_kv_heads.
  TextOnlyLLMExportConfig.head_dim: TextOnlyLLMExportConfig#head_dim.
  TextOnlyLLMExportConfig.token_buckets: TextOnlyLLMExportConfig#token_buckets.
  TextOnlyLLMExportConfig.emit_byte_tokenizer: TextOnlyLLMExportConfig#emit_byte_tokenizer.
  ExportableModel.pallas_interpret: ExportableModel#pallas_interpret().
  ExportableTextOnlyLLM.sample_tokens: ExportableTextOnlyLLM#sample_tokens().
  ModelExportConfig.model_name: ModelExportConfig#model_name.
  ModelExportConfig.target_tpu: ModelExportConfig#target_tpu.
  ModelExportConfig.use_spmd_partitioning: ModelExportConfig#use_spmd_partitioning.
  TextOnlyLLMExportConfig.eos_token_id: TextOnlyLLMExportConfig#eos_token_id.
  TextOnlyLLMExportConfig.req_buckets: TextOnlyLLMExportConfig#req_buckets.
  TextOnlyLLMExportConfig.uses_mrope: TextOnlyLLMExportConfig#uses_mrope.
  TextOnlyLLMExportConfig.speculative_config: TextOnlyLLMExportConfig#speculative_config.
  ModelExportConfig.data_parallel_size: ModelExportConfig#data_parallel_size.
  ModelExportConfig.pipeline_parallel_size: ModelExportConfig#pipeline_parallel_size.
  TextOnlyLLMExportConfig.num_q_heads: TextOnlyLLMExportConfig#num_q_heads.
  ShapeDtypeStruct.__init__: ShapeDtypeStruct#__init__().
---
# Module: [`src/vllm_torchtpu/experimental/export/api.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py)

## Classes
### <a id="ExportableModel"></a>`ExportableModel`  ·  implements/extends Protocol
- def: [`src/vllm_torchtpu/experimental/export/api.py:138`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L138)
- doc: Foundational exportable model protocol.
- signature: `class ExportableModel(Protocol):`
- members:
  - <a id="ExportableModel.abstract_params"></a>`abstract_params(self)` — [`L151`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L151) — Ordered mapping of parameter name -> ShapeDtypeStruct.
  - <a id="ExportableModel.export_config"></a>`export_config(self)` — [`L147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L147) — Returns the model's export configuration.
  - <a id="ExportableModel.pallas_interpret"></a>`pallas_interpret(self)` — [`L142`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L142) — When True, lowers Pallas kernels with interpret=True for CPU execution.
- uses (calls/refs, reference-scoped): [`abstract_params`](universal_adapter.md#UniversalVllmExportableLLM.abstract_params), [`ExportableTextOnlyLLM`](api.md#ExportableTextOnlyLLM), [`export_config`](api.md#ExportableTextOnlyLLM.export_config), [`ModelExportConfig`](api.md#ModelExportConfig), [`pallas_interpret`](universal_adapter.md#UniversalVllmExportableLLM.pallas_interpret)
- used by: [`export`](exporter.md#export), [`ExportableTextOnlyLLM`](api.md#ExportableTextOnlyLLM)

### <a id="ExportableTextOnlyLLM"></a>`ExportableTextOnlyLLM`  ·  implements/extends ExportableModel, Protocol
- def: [`src/vllm_torchtpu/experimental/export/api.py:157`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L157) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: Text-only autoregressive LLM export protocol.
- signature: `class ExportableTextOnlyLLM(ExportableModel, Protocol):`
- members:
  - <a id="ExportableTextOnlyLLM.compute_logits"></a>`compute_logits(self, hidden_states: Any, lm_head_weight: Any)` — [`L202`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L202) — Computes logits[R, vocab_size] from hidden_states[R, hidden_size].
  - <a id="ExportableTextOnlyLLM.export_config"></a>`export_config(self)` — [`L169`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L169) — Returns the LLM's export configuration. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="ExportableTextOnlyLLM.forward"></a>`forward(self, weights: Mapping[str, Any], kv_caches: Sequence[Any], *, input_ids: Any, positions: Any, kv_lens: Any, block_tables: Any, query_start_loc: Any, req_dist: Any)` — [`L173`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L173) — Executes one flattened 1D continuous batching forward pass.
  - <a id="ExportableTextOnlyLLM.sample_tokens"></a>`sample_tokens(self, logits: Any, *, temperature: Any | None = None, top_k: Any | None = None, top_p: Any | None = None, min_p: Any | None = None, uniform: Any | None = None, repetition_penalty: Any | None = None, presence_penalty: Any | None = None, frequency_penalty: Any | None = None, history: Any | None = None, output_start: Any | None = None)` — [`L210`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L210) — Samples token ids i64[R, 1] from vocabulary logits[R, vocab_size].
- uses (calls/refs, reference-scoped): [`forward`](universal_adapter.md#UniversalVllmExportableLLM.forward), [`TextOnlyLLMExportConfig`](api.md#TextOnlyLLMExportConfig), [`compute_logits`](universal_adapter.md#UniversalVllmExportableLLM.compute_logits), [`export_config`](universal_adapter.md#UniversalVllmExportableLLM.export_config), [`ExportableModel`](api.md#ExportableModel), [`UniversalVllmExportableLLM`](universal_adapter.md#UniversalVllmExportableLLM), [`sample_tokens`](universal_adapter.md#UniversalVllmExportableLLM.sample_tokens)
- used by: [`_export_text_only_llm_functions`](exporter.md#_export_text_only_llm_functions), [`export`](exporter.md#export), [`run_export_from_args`](cli.md#run_export_from_args), [`_params_read_by_forward`](exporter.md#_params_read_by_forward), [`_state_specs`](exporter.md#_state_specs), [`_tensor_layouts`](exporter.md#_tensor_layouts), [`lower_torch_forward_to_mlir`](tpu_lowering.md#lower_torch_forward_to_mlir), [`_recurrent_serving_config`](exporter.md#_recurrent_serving_config), [`_extra_user_inputs`](exporter.md#_extra_user_inputs), [`export_config`](api.md#ExportableModel.export_config), [`ExportableModel`](api.md#ExportableModel), [`UniversalVllmExportableLLM`](universal_adapter.md#UniversalVllmExportableLLM), [`_logits_entry`](exporter.md#_export_text_only_llm_functions._logits_entry), [`_torch_forward_entry`](tpu_lowering.md#lower_torch_forward_to_mlir._torch_forward_entry)

### <a id="ModelExportConfig"></a>`ModelExportConfig`
- def: [`src/vllm_torchtpu/experimental/export/api.py:43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L43)
- doc: General model export configuration.
- signature: `class ModelExportConfig:`
- members:
  - <a id="ModelExportConfig.tensor_parallel_size"></a>`tensor_parallel_size(self)` — [`L55`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L55) — Size of the serving mesh's 'tp' axis. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="ModelExportConfig.data_parallel_size"></a>`data_parallel_size` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L51)
  - <a id="ModelExportConfig.model_name"></a>`model_name` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L46)
  - <a id="ModelExportConfig.num_partitions"></a>`num_partitions` — [`L49`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L49)
  - <a id="ModelExportConfig.num_replicas"></a>`num_replicas` — [`L48`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L48)
  - <a id="ModelExportConfig.pipeline_parallel_size"></a>`pipeline_parallel_size` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L52)
  - <a id="ModelExportConfig.target_tpu"></a>`target_tpu` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L47)
  - <a id="ModelExportConfig.use_spmd_partitioning"></a>`use_spmd_partitioning` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L50)
- uses (calls/refs, reference-scoped): [`TextOnlyLLMExportConfig`](api.md#TextOnlyLLMExportConfig)
- used by: [`_export_text_only_llm_functions`](exporter.md#_export_text_only_llm_functions), [`build_export_config_from_vllm`](universal_adapter.md#build_export_config_from_vllm), [`export`](exporter.md#export), [`_layer_state_specs`](universal_adapter.md#UniversalVllmExportableLLM._layer_state_specs), [`abstract_params`](universal_adapter.md#UniversalVllmExportableLLM.abstract_params), [`TextOnlyLLMExportConfig`](api.md#TextOnlyLLMExportConfig), [`_axis_sizes`](exporter.md#_axis_sizes), [`export_config`](api.md#ExportableModel.export_config)

### <a id="ShapeDtypeStruct"></a>`ShapeDtypeStruct`
- def: [`src/vllm_torchtpu/experimental/export/api.py:24`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L24) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: Abstract tensor specification carrying shape, dtype, and optional sharding.
- signature: `class ShapeDtypeStruct:`
- members:
  - <a id="ShapeDtypeStruct.dtype"></a>`dtype` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L28)
  - <a id="ShapeDtypeStruct.shape"></a>`shape` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L27)
  - <a id="ShapeDtypeStruct.sharding"></a>`sharding` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L29)
- protocol/private: <a id="ShapeDtypeStruct.__init__"></a>`__init__`[`L31`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L31)
- used by: [`_export_text_only_llm_functions`](exporter.md#_export_text_only_llm_functions), [`_layer_state_specs`](universal_adapter.md#UniversalVllmExportableLLM._layer_state_specs), [`_state_specs`](exporter.md#_state_specs), [`abstract_states`](universal_adapter.md#UniversalVllmExportableLLM.abstract_states), [`abstract_params`](universal_adapter.md#UniversalVllmExportableLLM.abstract_params), [`lower_torch_forward_to_mlir`](tpu_lowering.md#lower_torch_forward_to_mlir), [`lower_torch_callable_to_mlir`](tpu_lowering.md#lower_torch_callable_to_mlir), [`export_samplers`](sampling.md#export_samplers), [`_state_bytes`](universal_adapter.md#UniversalVllmExportableLLM._state_bytes), [`_lowered_params`](exporter.md#_lowered_params), [`lower_abstract_params_mlir`](tpu_lowering.md#lower_abstract_params_mlir), [`_norm_params`](exporter.md#_norm_params), [`_recurrent_state_specs`](universal_adapter.md#_recurrent_state_specs), [`_i32_specs`](tpu_lowering.md#lower_torch_forward_to_mlir._i32_specs)

### <a id="TextOnlyLLMExportConfig"></a>`TextOnlyLLMExportConfig`  ·  implements/extends ModelExportConfig
- def: [`src/vllm_torchtpu/experimental/export/api.py:61`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L61) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
- doc: Text-only autoregressive LLM export configuration.
- signature: `class TextOnlyLLMExportConfig(ModelExportConfig):`
- members:
  - <a id="TextOnlyLLMExportConfig.max_cu_seqs"></a>`max_cu_seqs(self)` — [`L123`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L123) — Length of query_start_loc: one cumulative offset per sequence plus 1.
  - <a id="TextOnlyLLMExportConfig.max_num_pages"></a>`max_num_pages(self)` — [`L115`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L115) — Size of the flattened block table: max_num_seqs * pages per sequence. — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="TextOnlyLLMExportConfig.num_state_slots"></a>`num_state_slots(self)` — [`L128`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L128) — Slots of each recurrent state pool: one per sequence plus null slot 0.
  - <a id="TextOnlyLLMExportConfig.block_size"></a>`block_size` — [`L95`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L95)
  - <a id="TextOnlyLLMExportConfig.dtype"></a>`dtype` — [`L100`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L100)
  - <a id="TextOnlyLLMExportConfig.emit_byte_tokenizer"></a>`emit_byte_tokenizer` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L103)
  - <a id="TextOnlyLLMExportConfig.eos_token_id"></a>`eos_token_id` — [`L99`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L99)
  - <a id="TextOnlyLLMExportConfig.head_dim"></a>`head_dim` — [`L94`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L94)
  - <a id="TextOnlyLLMExportConfig.hf_checkpoint_dir"></a>`hf_checkpoint_dir` — [`L104`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L104) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="TextOnlyLLMExportConfig.hidden_size"></a>`hidden_size` — [`L90`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L90)
  - <a id="TextOnlyLLMExportConfig.max_model_len"></a>`max_model_len` — [`L98`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L98)
  - <a id="TextOnlyLLMExportConfig.max_num_seqs"></a>`max_num_seqs` — [`L97`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L97)
  - <a id="TextOnlyLLMExportConfig.num_blocks"></a>`num_blocks` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L96) — documented in [model-export-and-rust-launcher](../../../../../concepts/model-export-and-rust-launcher.md)
  - <a id="TextOnlyLLMExportConfig.num_kv_heads"></a>`num_kv_heads` — [`L93`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L93)
  - <a id="TextOnlyLLMExportConfig.num_layers"></a>`num_layers` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L91)
  - <a id="TextOnlyLLMExportConfig.num_q_heads"></a>`num_q_heads` — [`L92`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L92)
  - <a id="TextOnlyLLMExportConfig.req_buckets"></a>`req_buckets` — [`L102`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L102)
  - <a id="TextOnlyLLMExportConfig.speculative_config"></a>`speculative_config` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L106)
  - <a id="TextOnlyLLMExportConfig.token_buckets"></a>`token_buckets` — [`L101`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L101)
  - <a id="TextOnlyLLMExportConfig.uses_mrope"></a>`uses_mrope` — [`L105`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L105)
  - <a id="TextOnlyLLMExportConfig.vocab_size"></a>`vocab_size` — [`L89`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L89)
- protocol/private: <a id="TextOnlyLLMExportConfig.__post_init__"></a>`__post_init__`[`L108`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/experimental/export/api.py#L108)
- uses (calls/refs, reference-scoped): [`ModelExportConfig`](api.md#ModelExportConfig)
- used by: [`_export_text_only_llm_functions`](exporter.md#_export_text_only_llm_functions), [`build_export_config_from_vllm`](universal_adapter.md#build_export_config_from_vllm), [`export`](exporter.md#export), [`_layer_state_specs`](universal_adapter.md#UniversalVllmExportableLLM._layer_state_specs), [`run_export_from_args`](cli.md#run_export_from_args), [`_params_read_by_forward`](exporter.md#_params_read_by_forward), [`_state_specs`](exporter.md#_state_specs), [`abstract_states`](universal_adapter.md#UniversalVllmExportableLLM.abstract_states), [`fit_num_blocks_to_hbm`](universal_adapter.md#UniversalVllmExportableLLM.fit_num_blocks_to_hbm), [`_user_inputs`](exporter.md#_user_inputs), [`_emit_model_companion_files`](exporter.md#_emit_model_companion_files), [`_recurrent_serving_config`](exporter.md#_recurrent_serving_config), [`_patched_rope_modules`](universal_adapter.md#UniversalVllmExportableLLM._patched_rope_modules), [`export_config`](api.md#ExportableTextOnlyLLM.export_config), [`compute_logits`](universal_adapter.md#UniversalVllmExportableLLM.compute_logits), [`extra_user_inputs`](universal_adapter.md#UniversalVllmExportableLLM.extra_user_inputs), [`_axis_sizes`](exporter.md#_axis_sizes), [`ModelExportConfig`](api.md#ModelExportConfig), [`export_config`](universal_adapter.md#UniversalVllmExportableLLM.export_config), [`__init__`](universal_adapter.md#UniversalVllmExportableLLM.__init__)

