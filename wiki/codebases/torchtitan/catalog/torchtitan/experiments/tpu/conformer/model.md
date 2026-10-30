---
title: 'Module: torchtitan/experiments/tpu/conformer/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/conformer/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.conformer.model`/
symbols:
  PatchedMHA.forward: PatchedMHA#forward().
  Conformer.conformer_layers: Conformer#conformer_layers.
  ConformerModelArgs.update_from_config: ConformerModelArgs#update_from_config().
  ConformerLayer.forward: ConformerLayer#forward().
  ConformerModelArgs: ConformerModelArgs#
  ConformerModelArgs.get_nparams_and_flops: ConformerModelArgs#get_nparams_and_flops().
  Conformer.fc: Conformer#fc.
  ConformerModelArgs.vocab_size: ConformerModelArgs#vocab_size.
  ConformerModelArgs.hidden_dim: ConformerModelArgs#hidden_dim.
  Conformer.forward: Conformer#forward().
  PatchedMHA.out_proj: PatchedMHA#out_proj.
  Conformer.embedding: Conformer#embedding.
  ConformerModelArgs.num_layers: ConformerModelArgs#num_layers.
  ConformerModelArgs.kernel_size: ConformerModelArgs#kernel_size.
  TPUGLU.forward: TPUGLU#forward().
  _ConvolutionModule.forward: _ConvolutionModule#forward().
  ConformerModelArgs.num_heads: ConformerModelArgs#num_heads.
  PatchedMHA.num_heads: PatchedMHA#num_heads.
  _ConvolutionModule.sequential: _ConvolutionModule#sequential.
  ConformerLayer.ffn1: ConformerLayer#ffn1.
  ConformerLayer.self_attn: ConformerLayer#self_attn.
  ConformerLayer.conv_module: ConformerLayer#conv_module.
  ConformerLayer.ffn2: ConformerLayer#ffn2.
  Conformer: Conformer#
  PatchedMHA.embed_dim: PatchedMHA#embed_dim.
  PatchedMHA.in_proj: PatchedMHA#in_proj.
  _FeedForwardModule.forward: _FeedForwardModule#forward().
  Conformer.Config: Conformer#Config.
  Conformer.__init__: Conformer#__init__().
  Conformer.init_weights: Conformer#init_weights().
  ConformerModelArgs.max_seq_len: ConformerModelArgs#max_seq_len.
  ConformerModelArgs.use_splash: ConformerModelArgs#use_splash.
  ConformerModelArgs.use_vmap_bwd: ConformerModelArgs#use_vmap_bwd.
  PatchedMHA: PatchedMHA#
  _FeedForwardModule: _FeedForwardModule#
  tpu_glu: tpu_glu().
  TPUGLU: TPUGLU#
  TPUGLU.dim: TPUGLU#dim.
  PatchedMHA.dropout: PatchedMHA#dropout.
  PatchedMHA.head_dim: PatchedMHA#head_dim.
  PatchedMHA.use_splash: PatchedMHA#use_splash.
  PatchedMHA.use_vmap_bwd: PatchedMHA#use_vmap_bwd.
  _FeedForwardModule.sequential: _FeedForwardModule#sequential.
  _ConvolutionModule: _ConvolutionModule#
  _ConvolutionModule.layer_norm: _ConvolutionModule#layer_norm.
  ConformerLayer: ConformerLayer#
  ConformerLayer.self_attn_layer_norm: ConformerLayer#self_attn_layer_norm.
  ConformerLayer.self_attn_dropout: ConformerLayer#self_attn_dropout.
  ConformerLayer.final_layer_norm: ConformerLayer#final_layer_norm.
  TPUGLU.__init__: TPUGLU#__init__().
  PatchedMHA.__init__: PatchedMHA#__init__().
  _FeedForwardModule.__init__: _FeedForwardModule#__init__().
  _ConvolutionModule.__init__: _ConvolutionModule#__init__().
  ConformerLayer.__init__: ConformerLayer#__init__().
  Conformer.config: Conformer#config.
  Conformer._model_args: Conformer#_model_args.
---
# Module: [`torchtitan/experiments/tpu/conformer/model.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py)

## Classes
### <a id="Conformer"></a>`Conformer`  ·  implements/extends BaseModel
- def: [`torchtitan/experiments/tpu/conformer/model.py:254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L254)
- doc: Build a conformer model matching torchaudio.models.Conformer architecture.
- signature: `class Conformer(BaseModel):`
- members:
  - <a id="Conformer.forward"></a>`forward(self, inputs: torch.Tensor, **kwargs)` — [`L279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L279)
  - <a id="Conformer.init_weights"></a>`init_weights(self, buffer_device: torch.device | None = None)` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L286)
  - <a id="Conformer.Config"></a>`Config` — [`L257`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L257)
  - <a id="Conformer.config"></a>`config` — [`L261`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L261)
  - <a id="Conformer.conformer_layers"></a>`conformer_layers` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L265)
  - <a id="Conformer.embedding"></a>`embedding` — [`L263`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L263)
  - <a id="Conformer.fc"></a>`fc` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L276)
- protocol/private: <a id="Conformer.__init__"></a>`__init__`[`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L259), <a id="Conformer._model_args"></a>`_model_args`[`L262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L262)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`BaseModel`](../../../protocols/model.md#BaseModel), [`ConformerModelArgs`](model.md#ConformerModelArgs), [`hidden_dim`](model.md#ConformerModelArgs.hidden_dim), [`vocab_size`](model.md#ConformerModelArgs.vocab_size), [`kernel_size`](model.md#ConformerModelArgs.kernel_size), [`num_layers`](model.md#ConformerModelArgs.num_layers), [`num_heads`](model.md#ConformerModelArgs.num_heads), [`use_splash`](model.md#ConformerModelArgs.use_splash), [`use_vmap_bwd`](model.md#ConformerModelArgs.use_vmap_bwd), [`ConformerLayer`](model.md#ConformerLayer)
- used by: [`BaseModel`](../../../protocols/model.md#BaseModel), [`init_weights`](../../../protocols/model.md#BaseModel.init_weights)  (1 test-only)

### <a id="ConformerLayer"></a>`ConformerLayer`
- def: [`torchtitan/experiments/tpu/conformer/model.py:218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L218)
- signature: `class ConformerLayer(nn.Module):`
- members:
  - <a id="ConformerLayer.forward"></a>`forward(self, x)` — [`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L242)
  - <a id="ConformerLayer.conv_module"></a>`conv_module` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L238)
  - <a id="ConformerLayer.ffn1"></a>`ffn1` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L231)
  - <a id="ConformerLayer.ffn2"></a>`ffn2` — [`L239`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L239)
  - <a id="ConformerLayer.final_layer_norm"></a>`final_layer_norm` — [`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L240)
  - <a id="ConformerLayer.self_attn"></a>`self_attn` — [`L234`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L234)
  - <a id="ConformerLayer.self_attn_dropout"></a>`self_attn_dropout` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L237)
  - <a id="ConformerLayer.self_attn_layer_norm"></a>`self_attn_layer_norm` — [`L232`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L232)
- protocol/private: <a id="ConformerLayer.__init__"></a>`__init__`[`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L220)
- uses (calls/refs, reference-scoped): [`PatchedMHA`](model.md#PatchedMHA), [`_FeedForwardModule`](model.md#_FeedForwardModule), [`_ConvolutionModule`](model.md#_ConvolutionModule)
- used by: [`conformer_layers`](model.md#Conformer.conformer_layers)

### <a id="ConformerModelArgs"></a>`ConformerModelArgs`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/conformer/model.py:15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L15)
- doc: Arguments for Conformer model configuration.
- signature: `class ConformerModelArgs(BaseModel.Config):`
- members:
  - <a id="ConformerModelArgs.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L41)
  - <a id="ConformerModelArgs.update_from_config"></a>`update_from_config(self, train_config, **kwargs)` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L27)
  - <a id="ConformerModelArgs.hidden_dim"></a>`hidden_dim` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L19)
  - <a id="ConformerModelArgs.kernel_size"></a>`kernel_size` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L22)
  - <a id="ConformerModelArgs.max_seq_len"></a>`max_seq_len` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L23)
  - <a id="ConformerModelArgs.num_heads"></a>`num_heads` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L21)
  - <a id="ConformerModelArgs.num_layers"></a>`num_layers` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L20)
  - <a id="ConformerModelArgs.use_splash"></a>`use_splash` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L24)
  - <a id="ConformerModelArgs.use_vmap_bwd"></a>`use_vmap_bwd` — [`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L25)
  - <a id="ConformerModelArgs.vocab_size"></a>`vocab_size` — [`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L18)
- uses (calls/refs, reference-scoped): [`TPUTrainerConfig`](../tpu_job_config.md#TPUTrainerConfig), [`BaseModel`](../../../protocols/model.md#BaseModel), [`splash_attention_kernel`](../tpu_job_config.md#BaseTPUTrainerConfig.splash_attention_kernel), [`Config`](../../../protocols/model.md#BaseModel.Config), [`use_splash_attention_kernel`](../tpu_job_config.md#SplashAttentionKernelConfig.use_splash_attention_kernel), [`use_vmap_bwd`](../tpu_job_config.md#SplashAttentionKernelConfig.use_vmap_bwd)
- used by: [`_conformer_model_spec`](config_registry.md#_conformer_model_spec), [`conformer_layers`](model.md#Conformer.conformer_layers), [`conformer_args`](__init__.md#conformer_args), [`fc`](model.md#Conformer.fc), [`embedding`](model.md#Conformer.embedding), [`Config`](model.md#Conformer.Config), [`__init__`](model.md#Conformer.__init__)  (1 test-only)

### <a id="PatchedMHA"></a>`PatchedMHA`
- def: [`torchtitan/experiments/tpu/conformer/model.py:103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L103)
- signature: `class PatchedMHA(nn.Module):`
- members:
  - <a id="PatchedMHA.forward"></a>`forward(self, query, key, value, key_padding_mask=None, need_weights=True, attn_mask=None, average_attn_weights=True, is_causal=False)` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L116)
  - <a id="PatchedMHA.dropout"></a>`dropout` — [`L109`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L109)
  - <a id="PatchedMHA.embed_dim"></a>`embed_dim` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L107)
  - <a id="PatchedMHA.head_dim"></a>`head_dim` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L110)
  - <a id="PatchedMHA.in_proj"></a>`in_proj` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L111)
  - <a id="PatchedMHA.num_heads"></a>`num_heads` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L108)
  - <a id="PatchedMHA.out_proj"></a>`out_proj` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L112)
  - <a id="PatchedMHA.use_splash"></a>`use_splash` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L113)
  - <a id="PatchedMHA.use_vmap_bwd"></a>`use_vmap_bwd` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L114)
- protocol/private: <a id="PatchedMHA.__init__"></a>`__init__`[`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L105)
- uses (calls/refs, reference-scoped): [`splash_sdpa`](../kernels/splash_attention.md#splash_sdpa)
- used by: [`self_attn`](model.md#ConformerLayer.self_attn)  (1 test-only)

### <a id="TPUGLU"></a>`TPUGLU`
- def: [`torchtitan/experiments/tpu/conformer/model.py:92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L92)
- signature: `class TPUGLU(torch.nn.Module):`
- members:
  - <a id="TPUGLU.forward"></a>`forward(self, x)` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L98)
  - <a id="TPUGLU.dim"></a>`dim` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L96)
- protocol/private: <a id="TPUGLU.__init__"></a>`__init__`[`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L94)
- uses (calls/refs, reference-scoped): [`tpu_glu`](model.md#tpu_glu)
- used by: [`sequential`](model.md#_ConvolutionModule.sequential)

### <a id="_ConvolutionModule"></a>`_ConvolutionModule`
- def: [`torchtitan/experiments/tpu/conformer/model.py:187`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L187)
- signature: `class _ConvolutionModule(nn.Module):`
- members:
  - <a id="_ConvolutionModule.forward"></a>`forward(self, x)` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L210)
  - <a id="_ConvolutionModule.layer_norm"></a>`layer_norm` — [`L192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L192)
  - <a id="_ConvolutionModule.sequential"></a>`sequential` — [`L193`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L193)
- protocol/private: <a id="_ConvolutionModule.__init__"></a>`__init__`[`L189`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L189)
- uses (calls/refs, reference-scoped): [`TPUGLU`](model.md#TPUGLU)
- used by: [`conv_module`](model.md#ConformerLayer.conv_module)

### <a id="_FeedForwardModule"></a>`_FeedForwardModule`
- def: [`torchtitan/experiments/tpu/conformer/model.py:170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L170)
- signature: `class _FeedForwardModule(nn.Module):`
- members:
  - <a id="_FeedForwardModule.forward"></a>`forward(self, x)` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L183)
  - <a id="_FeedForwardModule.sequential"></a>`sequential` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L174)
- protocol/private: <a id="_FeedForwardModule.__init__"></a>`__init__`[`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L172)
- used by: [`ffn1`](model.md#ConformerLayer.ffn1), [`ffn2`](model.md#ConformerLayer.ffn2)

## Functions
- <a id="tpu_glu"></a>`tpu_glu(input, dim=-1)` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/conformer/model.py#L87)

