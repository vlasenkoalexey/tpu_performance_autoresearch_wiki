---
title: 'Module: easydel/modules/mamba/modeling_mamba.py'
type: catalog
provenance: extracted
module: easydel/modules/mamba/modeling_mamba.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mamba.modeling_mamba`/
symbols:
  MambaMixer.__call__: MambaMixer#__call__().
  MambaConv1D.__call__: MambaConv1D#__call__().
  MambaModel.__call__: MambaModel#__call__().
  MambaBlock.norm: MambaBlock#norm.
  MambaForCausalLM.prepare_inputs_for_generation: MambaForCausalLM#prepare_inputs_for_generation().
  MambaForCausalLM: MambaForCausalLM#
  MambaModel: MambaModel#
  MambaBlock.__call__: MambaBlock#__call__().
  MambaMixer.act: MambaMixer#act.
  MambaMixer.precision: MambaMixer#precision.
  MambaMixer.conv1d: MambaMixer#conv1d.
  MambaModel.embeddings: MambaModel#embeddings.
  MambaMixer.init_bias_dt: MambaMixer#init_bias_dt().
  MambaModel.norm_f: MambaModel#norm_f.
  MambaForCausalLM.__init__: MambaForCausalLM#__init__().
  MambaForCausalLM.__call__: MambaForCausalLM#__call__().
  MambaConv1D.kernel: MambaConv1D#kernel.
  MambaConv1D.bias: MambaConv1D#bias.
  MambaModel.layers: MambaModel#layers.
  _T: _T.
  MambaMixer.A_log: MambaMixer#A_log.
  MambaMixer.D: MambaMixer#D.
  MambaOutput: MambaOutput#
  create_tuple_parser: create_tuple_parser().
  MambaMixer.__init__: MambaMixer#__init__().
  MambaModel.__init__: MambaModel#__init__().
  MambaForCausalLM._task_type: MambaForCausalLM#_task_type.
  MambaCausalLMOutput: MambaCausalLMOutput#
  MambaMixer.time_step_rank: MambaMixer#time_step_rank.
  create_tuple_parser.parse: create_tuple_parser().parse().
  MambaMixer.activation: MambaMixer#activation.
  MambaMixer.in_proj: MambaMixer#in_proj.
  MambaMixer.dt_proj: MambaMixer#dt_proj.
  MambaMixer.out_proj: MambaMixer#out_proj.
  MambaMixer.ssm_op: MambaMixer#ssm_op.
  MambaBlock.residual_in_fp32: MambaBlock#residual_in_fp32.
  MambaConv1D.dtype: MambaConv1D#dtype.
  MambaMixer.conv_kernel_size: MambaMixer#conv_kernel_size.
  MambaOutput.cache: MambaOutput#cache.
  MambaCausalLMOutput.cache: MambaCausalLMOutput#cache.
  Lambda.__call__: Lambda#__call__().
  MambaBlock.__init__: MambaBlock#__init__().
  MambaModel.get_embedding: MambaModel#get_embedding().
  MambaForCausalLM._config_class: MambaForCausalLM#_config_class.
  MambaForCausalLM.update_inputs_for_generation: MambaForCausalLM#update_inputs_for_generation().
  MambaConv1D.padding: MambaConv1D#padding.
  MambaConv1D.use_bias: MambaConv1D#use_bias.
  MambaMixer.config: MambaMixer#config.
  MambaMixer.ssm_state_size: MambaMixer#ssm_state_size.
  Lambda.fn: Lambda#fn.
  MambaConv1D: MambaConv1D#
  MambaConv1D.stride: MambaConv1D#stride.
  MambaConv1D.dilation: MambaConv1D#dilation.
  MambaConv1D.groups: MambaConv1D#groups.
  MambaConv1D.num_spatial_dims: MambaConv1D#num_spatial_dims.
  MambaMixer: MambaMixer#
  MambaMixer.x_proj: MambaMixer#x_proj.
  MambaMixer.intermediate_size: MambaMixer#intermediate_size.
  MambaBlock: MambaBlock#
  MambaBlock.config: MambaBlock#config.
  MambaBlock.mixer: MambaBlock#mixer.
  init_to_value: init_to_value().
  MambaOutput.last_hidden_state: MambaOutput#last_hidden_state.
  MambaOutput.hidden_states: MambaOutput#hidden_states.
  MambaCausalLMOutput.logits: MambaCausalLMOutput#logits.
  MambaCausalLMOutput.hidden_states: MambaCausalLMOutput#hidden_states.
  MambaCausalLMOutput.last_hidden_state: MambaCausalLMOutput#last_hidden_state.
  Lambda: Lambda#
  MambaConv1D.__init__: MambaConv1D#__init__().
  MambaConv1D.features: MambaConv1D#features.
  MambaConv1D.kernel_size: MambaConv1D#kernel_size.
  MambaConv1D.param_dtype: MambaConv1D#param_dtype.
  MambaConv1D.precision: MambaConv1D#precision.
  MambaConv1D.craft_sharding: MambaConv1D#craft_sharding().
  MambaMixer.layer_idx: MambaMixer#layer_idx.
  MambaMixer.dtype: MambaMixer#dtype.
  MambaMixer.param_dtype: MambaMixer#param_dtype.
  MambaMixer.craft_sharding: MambaMixer#craft_sharding().
  MambaBlock.layer_idx: MambaBlock#layer_idx.
  MambaBlock.dtype: MambaBlock#dtype.
  MambaBlock.param_dtype: MambaBlock#param_dtype.
  MambaBlock.precision: MambaBlock#precision.
  MambaModel.get_encoder: MambaModel#get_encoder().
  MambaModel.get_decoder: MambaModel#get_decoder().
  MambaModel.get_lm_head: MambaModel#get_lm_head().
  MambaForCausalLM._model_type: MambaForCausalLM#_model_type.
  MambaForCausalLM.get_encoder: MambaForCausalLM#get_encoder().
  MambaForCausalLM.get_decoder: MambaForCausalLM#get_decoder().
  MambaForCausalLM.get_lm_head: MambaForCausalLM#get_lm_head().
  MambaForCausalLM.get_embedding: MambaForCausalLM#get_embedding().
---
# Module: [`easydel/modules/mamba/modeling_mamba.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py)

## Classes
### `Lambda`  ·  implements/extends Module
- def: [`easydel/modules/mamba/modeling_mamba.py:92`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L92)
- doc: Convenience wrapper to insert callables into module pipelines.
- signature: `class Lambda(nn.Module):`
- members:
  - `fn` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L95)
- protocol/private: `__call__`[`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L97)

### `MambaBlock`  ·  implements/extends Module
- def: [`easydel/modules/mamba/modeling_mamba.py:489`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L489)
- doc: Single Mamba layer combining normalization, SSM mixer, and residual connections.
- signature: `class MambaBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, cache: RecurrentCacheView | None = None, position_ids: Array | None = None, attention_mask: Array | None = None)` — [`L551`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L551) — Forward pass through the Mamba block.
  - `__init__(self, config: MambaConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L504`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L504) — Initialize Mamba block.
  - `config` — [`L524`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L524)
  - `dtype` — [`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L526)
  - `layer_idx` — [`L525`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L525)
  - `mixer` — [`L542`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L542)
  - `norm` — [`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L530)
  - `param_dtype` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L527)
  - `precision` — [`L528`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L528)
  - `residual_in_fp32` — [`L529`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L529)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`RecurrentCacheView`](../../caching/recurrent/cache.md#RecurrentCacheView), [`MambaConfig`](mamba_configuration.md#MambaConfig), [`hidden_size`](mamba_configuration.md#MambaConfig.hidden_size), [`layer_norm_epsilon`](mamba_configuration.md#MambaConfig.layer_norm_epsilon), [`MambaMixer`](modeling_mamba.md#MambaMixer), [`gradient_checkpointing`](mamba_configuration.md#MambaConfig.gradient_checkpointing), [`residual_in_fp32`](mamba_configuration.md#MambaConfig.residual_in_fp32)
- used by: [`layers`](modeling_mamba.md#MambaModel.layers)

### `MambaCausalLMOutput`  ·  implements/extends BaseModelOutput
- def: [`easydel/modules/mamba/modeling_mamba.py:63`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L63)
- doc: Causal LM output including logits and cache for Mamba decoding.
- signature: `class MambaCausalLMOutput(BaseModelOutput):`
- members:
  - `cache` — [`L67`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L67)
  - `hidden_states` — [`L68`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L68)
  - `last_hidden_state` — [`L69`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L69)
  - `logits` — [`L66`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L66)
- uses (calls/refs, reference-scoped): [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`RecurrentCache`](../../caching/recurrent/cache.md#RecurrentCache)
- used by: [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`__call__`](modeling_mamba.md#MambaForCausalLM.__call__)

### `MambaConv1D`  ·  implements/extends Module
- def: [`easydel/modules/mamba/modeling_mamba.py:101`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L101)
- doc: Minimal 1D convolution layer for Mamba mixer implementation.
- signature: `class MambaConv1D(nn.Module):`
- members:
  - `__call__(self, x: Array)` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L176) — Apply 1D convolution to input tensor.
  - `__init__(self, features: int, kernel_size: int = 1, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, use_bias: bool = True, num_spatial_dims: int = 1, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L109) — Initialize Mamba 1D convolution layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L169) — Return sharding specs for convolution parameters.
  - `bias` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L150)
  - `dilation` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L161)
  - `dtype` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L165)
  - `features` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L157)
  - `groups` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L162)
  - `kernel` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L142)
  - `kernel_size` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L158)
  - `num_spatial_dims` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L164)
  - `padding` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L160)
  - `param_dtype` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L166)
  - `precision` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L167)
  - `stride` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L159)
  - `use_bias` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L163)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`__call__`](modeling_mamba.md#MambaMixer.__call__), [`conv1d`](modeling_mamba.md#MambaMixer.conv1d)

### `MambaForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/mamba/modeling_mamba.py:785`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L785)
- doc: Mamba model with a language modeling head for causal language modeling tasks.
- signature: `class MambaForCausalLM(BaseCausalLMModule[MambaModel, MambaConfig]):`
- members:
  - `__call__(self, input_ids: Array | None = None, inputs_embeds: Array | None = None, cache: RecurrentCache | None = None, position_ids: Array | None = None, apply_lm_head: bool = True, attention_mask: Array | None = None, output_hidden_states: bool | None = None, **kwargs)` — [`L832`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L832) — Forward pass for causal language modeling.
  - `__init__(self, config: MambaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L803`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L803) — Initialize Mamba model for causal language modeling.
  - `get_decoder(self)` — [`L968`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L968) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L980`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L980) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L961`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L961) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L974`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L974) — Returns the language model head of the module.
  - `prepare_inputs_for_generation(self, input_ids, max_length: int, pad_token_id: int, starts: int | None = None, **kwargs)` — [`L911`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L911) — Prepare model inputs for text generation.
  - `update_inputs_for_generation(self, outputs: MambaOutput, model_kwargs: dict[str, tp.Any], **kwargs)` — [`L889`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L889) — Update model inputs for the next generation step.
- protocol/private: `_config_class`[`L801`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L801), `_model_type`[`L800`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L800), `_task_type`[`L799`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L799)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`RecurrentCache`](../../caching/recurrent/cache.md#RecurrentCache), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`compute_lm_logits`](../_base/causal_lm_module.md#BaseCausalLMModule.compute_lm_logits), [`RecurrentCacheConfig`](../../caching/recurrent/cache.md#RecurrentCacheConfig), [`MambaModel`](modeling_mamba.md#MambaModel), [`MambaConfig`](mamba_configuration.md#MambaConfig), [`init_cache`](../../caching/recurrent/cache.md#RecurrentCache.init_cache), [`prepare_inputs_for_call`](../../infra/base_module.md#EasyDeLBaseModule.prepare_inputs_for_call), [`create_for_mamba`](../../caching/recurrent/cache.md#RecurrentCacheConfig.create_for_mamba), [`MambaOutput`](modeling_mamba.md#MambaOutput), [`MambaCausalLMOutput`](modeling_mamba.md#MambaCausalLMOutput)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`get_encoder`](../_base/_base_task_module.md#BaseTaskModule.get_encoder), [`get_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.get_lm_head), [`prepare_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.prepare_inputs_for_generation), [`update_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.update_inputs_for_generation)

### `MambaMixer`  ·  implements/extends Module
- def: [`easydel/modules/mamba/modeling_mamba.py:209`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L209)
- doc: Core selective state space mixer for Mamba blocks.
- signature: `class MambaMixer(nn.Module):`
- members:
  - `__call__(self, input_states: Array, cache: RecurrentCacheView | None = None, position_ids: Array | None = None, attention_mask: Array | None = None)` — [`L368`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L368) — Apply selective state space transformation.
  - `__init__(self, config: MambaConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L225) — Initialize Mamba selective state space mixer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L361`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L361) — Return sharding specs for state space parameters.
  - `init_bias_dt(key, shape, dtype)` — [`L284`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L284)
  - `A_log` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L335)
  - `D` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L342)
  - `act` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L268)
  - `activation` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L267)
  - `config` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L245)
  - `conv1d` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L258)
  - `conv_kernel_size` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L351)
  - `dt_proj` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L319)
  - `dtype` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L247)
  - `in_proj` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L307)
  - `intermediate_size` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L350)
  - `layer_idx` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L246)
  - `out_proj` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L327)
  - `param_dtype` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L248)
  - `precision` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L249)
  - `ssm_op` — [`L359`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L359)
  - `ssm_state_size` — [`L349`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L349)
  - `time_step_rank` — [`L352`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L352)
  - `x_proj` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L313)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`RecurrentCacheView`](../../caching/recurrent/cache.md#RecurrentCacheView), [`bound`](../../infra/utils.md#ArrayParam.bound), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`OperationMetadata`](../../operations/_operation_meta.md#OperationMetadata), [`conv_state`](../../caching/recurrent/cache.md#RecurrentCacheView.conv_state), [`concatenate_to_cache`](../../caching/recurrent/cache.md#RecurrentCacheView.concatenate_to_cache), [`recurrent_state`](../../caching/recurrent/cache.md#RecurrentCacheView.recurrent_state), [`MambaConfig`](mamba_configuration.md#MambaConfig), [`SSM1Op`](../../operations/kernels/ssm1.md#SSM1Op), [`ssm_state`](../../operations/kernels/ssm1.md#SSM1Output.ssm_state), [`bias`](modeling_mamba.md#MambaConv1D.bias), [`kernel`](modeling_mamba.md#MambaConv1D.kernel), [`hidden_size`](mamba_configuration.md#MambaConfig.hidden_size), [`intermediate_size`](mamba_configuration.md#MambaConfig.intermediate_size), [`time_step_rank`](mamba_configuration.md#MambaConfig.time_step_rank), [`conv_kernel`](mamba_configuration.md#MambaConfig.conv_kernel), [`hidden_act`](mamba_configuration.md#MambaConfig.hidden_act), [`time_step_init_scheme`](mamba_configuration.md#MambaConfig.time_step_init_scheme), [`time_step_max`](mamba_configuration.md#MambaConfig.time_step_max), [`time_step_min`](mamba_configuration.md#MambaConfig.time_step_min), [`use_bias`](mamba_configuration.md#MambaConfig.use_bias), [`use_bias`](modeling_mamba.md#MambaConv1D.use_bias), [`MambaConv1D`](modeling_mamba.md#MambaConv1D), [`initializer_range`](mamba_configuration.md#MambaConfig.initializer_range), [`state_size`](mamba_configuration.md#MambaConfig.state_size), [`time_step_floor`](mamba_configuration.md#MambaConfig.time_step_floor), [`time_step_scale`](mamba_configuration.md#MambaConfig.time_step_scale), [`use_conv_bias`](mamba_configuration.md#MambaConfig.use_conv_bias)
- used by: [`norm`](modeling_mamba.md#MambaBlock.norm)

### `MambaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/mamba/modeling_mamba.py:596`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L596)
- doc: Mamba selective state space model implementation.
- signature: `class MambaModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Array | None = None, inputs_embeds: Array | None = None, cache: RecurrentCache | None = None, position_ids: Array | None = None, attention_mask: Array | None = None, output_hidden_states: bool | None = None, **kwargs)` — [`L663`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L663) — Forward pass through the Mamba base model.
  - `__init__(self, config: MambaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L611`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L611) — Initialize Mamba base model.
  - `get_decoder(self)` — [`L764`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L764) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L777`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L777) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L757`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L757) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L770`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L770) — Returns the language model head of the module.
  - `embeddings` — [`L636`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L636)
  - `layers` — [`L643`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L643)
  - `norm_f` — [`L656`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L656)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`RecurrentCache`](../../caching/recurrent/cache.md#RecurrentCache), `output_hidden_states`, [`views`](../../caching/recurrent/cache.md#RecurrentCache.views), [`MambaConfig`](mamba_configuration.md#MambaConfig), [`hidden_size`](mamba_configuration.md#MambaConfig.hidden_size), [`MambaOutput`](modeling_mamba.md#MambaOutput), [`init_empty`](../../caching/recurrent/cache.md#RecurrentCache.init_empty), [`layer_norm_epsilon`](mamba_configuration.md#MambaConfig.layer_norm_epsilon), [`num_hidden_layers`](mamba_configuration.md#MambaConfig.num_hidden_layers), [`MambaBlock`](modeling_mamba.md#MambaBlock), [`vocab_size`](mamba_configuration.md#MambaConfig.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`MambaForCausalLM`](modeling_mamba.md#MambaForCausalLM), [`__init__`](modeling_mamba.md#MambaForCausalLM.__init__)

### `MambaOutput`  ·  implements/extends BaseModelOutput
- def: [`easydel/modules/mamba/modeling_mamba.py:54`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L54)
- doc: Output container for the base Mamba model with cached state.
- signature: `class MambaOutput(BaseModelOutput):`
- members:
  - `cache` — [`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L58)
  - `hidden_states` — [`L59`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L59)
  - `last_hidden_state` — [`L57`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L57)
- uses (calls/refs, reference-scoped): [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`RecurrentCache`](../../caching/recurrent/cache.md#RecurrentCache)
- used by: [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`__call__`](modeling_mamba.md#MambaModel.__call__), [`update_inputs_for_generation`](modeling_mamba.md#MambaForCausalLM.update_inputs_for_generation)

## Functions
- `create_tuple_parser(n: int)` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L75) — Normalize a scalar or sequence into a tuple of length ``n``.
- `init_to_value(x, dtype)` — [`L48`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L48) — Return initializer that fills parameters with a broadcasted constant.
- `parse(x: _T | Sequence[_T])` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L80)

## Module values
- `_T` — [`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/mamba/modeling_mamba.py#L72)

