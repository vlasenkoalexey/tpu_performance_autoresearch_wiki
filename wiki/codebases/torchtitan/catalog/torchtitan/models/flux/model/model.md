---
title: 'Module: torchtitan/models/flux/model/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/model/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.model.model`/FluxModel#
symbols:
  FluxModel.Config.get_nparams_and_flops: Config#get_nparams_and_flops().
  FluxModel.forward: forward().
  FluxModel: ''
  FluxModel.Config: Config#
  FluxModel.Config.double_blocks: Config#double_blocks.
  FluxModel.Config.single_blocks: Config#single_blocks.
  FluxModel.Config.final_layer_config: Config#final_layer_config.
  FluxModel.Config.img_in: Config#img_in.
  FluxModel.Config.txt_in: Config#txt_in.
  FluxModel.Config.autoencoder: Config#autoencoder.
  FluxModel.Config.clip_encoder: Config#clip_encoder.
  FluxModel.Config.t5_encoder: Config#t5_encoder.
  FluxModel.Config.pe_config: Config#pe_config.
  FluxModel.Config.time_in_config: Config#time_in_config.
  FluxModel.Config.vector_in_config: Config#vector_in_config.
  FluxModel.out_channels: out_channels.
  FluxModel.Config.hidden_size: Config#hidden_size.
  FluxModel.double_blocks: double_blocks.
  FluxModel.single_blocks: single_blocks.
  FluxModel.Config.num_heads: Config#num_heads.
  FluxModel.Config.depth: Config#depth.
  FluxModel.Config.depth_single_blocks: Config#depth_single_blocks.
  FluxModel.Config.axes_dim: Config#axes_dim.
  FluxModel.pe_embedder: pe_embedder.
  FluxModel.img_in: img_in.
  FluxModel.time_in: time_in.
  FluxModel.vector_in: vector_in.
  FluxModel.txt_in: txt_in.
  FluxModel.final_layer: final_layer.
  FluxModel.Config.in_channels: Config#in_channels.
  FluxModel.Config.out_channels: Config#out_channels.
  FluxModel.Config.vec_in_dim: Config#vec_in_dim.
  FluxModel.Config.context_in_dim: Config#context_in_dim.
  FluxModel.Config.mlp_ratio: Config#mlp_ratio.
  FluxModel.Config.theta: Config#theta.
  FluxModel.Config.qkv_bias: Config#qkv_bias.
  FluxModel.Config.update_from_config: Config#update_from_config().
  FluxModel.__init__: __init__().
  FluxModel.in_channels: in_channels.
  FluxModel.hidden_size: hidden_size.
  FluxModel.num_heads: num_heads.
  FluxModel._local_concat_text_image: _local_concat_text_image().
---
# Module: [`torchtitan/models/flux/model/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py)

## Classes
### <a id="FluxModel"></a>`FluxModel`  ·  implements/extends BaseModel
- def: [`torchtitan/models/flux/model/model.py:30`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L30) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- doc: Transformer model for flow matching on sequences.
- signature: `class FluxModel(BaseModel):`
- members:
  - <a id="FluxModel.forward"></a>`forward(self, img: Tensor, img_ids: Tensor, txt: Tensor, txt_ids: Tensor, timesteps: Tensor, y: Tensor)` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L168)
  - <a id="FluxModel.double_blocks"></a>`double_blocks` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L162)
  - <a id="FluxModel.final_layer"></a>`final_layer` — [`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L166)
  - <a id="FluxModel.hidden_size"></a>`hidden_size` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L154)
  - <a id="FluxModel.img_in"></a>`img_in` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L157)
  - <a id="FluxModel.in_channels"></a>`in_channels` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L143)
  - <a id="FluxModel.num_heads"></a>`num_heads` — [`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L155)
  - <a id="FluxModel.out_channels"></a>`out_channels` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L144)
  - <a id="FluxModel.pe_embedder"></a>`pe_embedder` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L156)
  - <a id="FluxModel.single_blocks"></a>`single_blocks` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L164)
  - <a id="FluxModel.time_in"></a>`time_in` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L158)
  - <a id="FluxModel.txt_in"></a>`txt_in` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L160)
  - <a id="FluxModel.vector_in"></a>`vector_in` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L159)
- protocol/private: <a id="FluxModel.__init__"></a>`__init__`[`L140`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L140), <a id="FluxModel._local_concat_text_image"></a>`_local_concat_text_image`[`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L184)
- uses (calls/refs, reference-scoped): [`build`](../../../protocols/module.md#Module.Config.build), [`BaseModel`](../../../protocols/model.md#BaseModel), [`ModuleList`](../../../protocols/module.md#ModuleList), [`Config`](model.md#FluxModel.Config), [`double_blocks`](model.md#FluxModel.Config.double_blocks), [`single_blocks`](model.md#FluxModel.Config.single_blocks), [`final_layer_config`](model.md#FluxModel.Config.final_layer_config), [`img_in`](model.md#FluxModel.Config.img_in), [`pe_config`](model.md#FluxModel.Config.pe_config), [`time_in_config`](model.md#FluxModel.Config.time_in_config), [`txt_in`](model.md#FluxModel.Config.txt_in), [`vector_in_config`](model.md#FluxModel.Config.vector_in_config), [`hidden_size`](model.md#FluxModel.Config.hidden_size), [`num_heads`](model.md#FluxModel.Config.num_heads), [`axes_dim`](model.md#FluxModel.Config.axes_dim), [`in_channels`](model.md#FluxModel.Config.in_channels), [`out_channels`](model.md#FluxModel.Config.out_channels), [`local_split_text_image`](layers.md#local_split_text_image), [`timestep_embedding`](layers.md#timestep_embedding)
- used by: [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`parallelize_flux`](../parallelize.md#parallelize_flux), [`BaseModel`](../../../protocols/model.md#BaseModel), [`_dtype`](../trainer.md#FluxTrainer._dtype), [`set_flux_sharding_config`](../sharding.md#set_flux_sharding_config), [`generate_image`](../inference/sampling.md#generate_image), [`denoise`](../inference/sampling.md#denoise), [`__init__`](state_dict_adapter.md#FluxStateDictAdapter.__init__)

### <a id="FluxModel.Config"></a>`FluxModel.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/model.py:36`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L36) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- signature: `class Config(BaseModel.Config):`
- members:
  - <a id="FluxModel.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L71)
  - <a id="FluxModel.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L66)
  - <a id="FluxModel.Config.autoencoder"></a>`autoencoder` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L51)
  - <a id="FluxModel.Config.axes_dim"></a>`axes_dim` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L48)
  - <a id="FluxModel.Config.clip_encoder"></a>`clip_encoder` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L55)
  - <a id="FluxModel.Config.context_in_dim"></a>`context_in_dim` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L42)
  - <a id="FluxModel.Config.depth"></a>`depth` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L46)
  - <a id="FluxModel.Config.depth_single_blocks"></a>`depth_single_blocks` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L47)
  - <a id="FluxModel.Config.double_blocks"></a>`double_blocks` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L63)
  - <a id="FluxModel.Config.final_layer_config"></a>`final_layer_config` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L62)
  - <a id="FluxModel.Config.hidden_size"></a>`hidden_size` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L43)
  - <a id="FluxModel.Config.img_in"></a>`img_in` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L37)
  - <a id="FluxModel.Config.in_channels"></a>`in_channels` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L39)
  - <a id="FluxModel.Config.mlp_ratio"></a>`mlp_ratio` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L44)
  - <a id="FluxModel.Config.num_heads"></a>`num_heads` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L45)
  - <a id="FluxModel.Config.out_channels"></a>`out_channels` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L40)
  - <a id="FluxModel.Config.pe_config"></a>`pe_config` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L59)
  - <a id="FluxModel.Config.qkv_bias"></a>`qkv_bias` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L50)
  - <a id="FluxModel.Config.single_blocks"></a>`single_blocks` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L64)
  - <a id="FluxModel.Config.t5_encoder"></a>`t5_encoder` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L56)
  - <a id="FluxModel.Config.theta"></a>`theta` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L49)
  - <a id="FluxModel.Config.time_in_config"></a>`time_in_config` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L60)
  - <a id="FluxModel.Config.txt_in"></a>`txt_in` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L38)
  - <a id="FluxModel.Config.vec_in_dim"></a>`vec_in_dim` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L41)
  - <a id="FluxModel.Config.vector_in_config"></a>`vector_in_config` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/model.py#L61)
- uses (calls/refs, reference-scoped): [`Linear`](../../common/linear.md#Linear), [`Config`](../../common/linear.md#Linear.Config), [`BaseModel`](../../../protocols/model.md#BaseModel), [`set_flux_sharding_config`](../sharding.md#set_flux_sharding_config), [`FluxEmbedder`](hf_embedder.md#FluxEmbedder), [`Config`](../../../protocols/model.md#BaseModel.Config), [`quadratic_attention_flops_per_token`](../../utils.md#quadratic_attention_flops_per_token), [`AutoEncoder`](autoencoder.md#AutoEncoder), [`Config`](hf_embedder.md#FluxEmbedder.Config), [`Config`](layers.md#MLPEmbedder.Config), [`MLPEmbedder`](layers.md#MLPEmbedder), [`Config`](autoencoder.md#AutoEncoder.Config), [`Config`](layers.md#EmbedND.Config), [`Config`](layers.md#LastLayer.Config), [`EmbedND`](layers.md#EmbedND), [`LastLayer`](layers.md#LastLayer), [`Config`](layers.md#DoubleStreamBlock.Config), [`Config`](layers.md#SingleStreamBlock.Config), [`DoubleStreamBlock`](layers.md#DoubleStreamBlock), [`SingleStreamBlock`](layers.md#SingleStreamBlock), [`hidden_size`](layers.md#SingleStreamBlock.Config.hidden_size), [`hidden_size`](layers.md#LastLayer.Config.hidden_size), [`hidden_size`](layers.md#DoubleStreamBlock.Config.hidden_size), [`num_heads`](layers.md#SingleStreamBlock.Config.num_heads), [`num_heads`](layers.md#DoubleStreamBlock.Config.num_heads), [`mlp_ratio`](layers.md#DoubleStreamBlock.Config.mlp_ratio)
- used by: [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`t5_encoder`](../trainer.md#FluxTrainer.t5_encoder), [`_dtype`](../trainer.md#FluxTrainer._dtype), [`set_flux_sharding_config`](../sharding.md#set_flux_sharding_config), [`__init__`](state_dict_adapter.md#FluxStateDictAdapter.__init__), [`to_hf`](state_dict_adapter.md#FluxStateDictAdapter.to_hf), [`out_channels`](model.md#FluxModel.out_channels), [`double_blocks`](model.md#FluxModel.double_blocks), [`single_blocks`](model.md#FluxModel.single_blocks), [`final_layer`](model.md#FluxModel.final_layer), [`img_in`](model.md#FluxModel.img_in), [`pe_embedder`](model.md#FluxModel.pe_embedder), [`time_in`](model.md#FluxModel.time_in), [`txt_in`](model.md#FluxModel.txt_in), [`vector_in`](model.md#FluxModel.vector_in), [`__init__`](model.md#FluxModel.__init__), [`hidden_size`](model.md#FluxModel.hidden_size), [`in_channels`](model.md#FluxModel.in_channels), [`num_heads`](model.md#FluxModel.num_heads)

