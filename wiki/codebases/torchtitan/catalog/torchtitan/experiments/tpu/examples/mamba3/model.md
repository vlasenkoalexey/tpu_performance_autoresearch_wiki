---
title: 'Module: torchtitan/experiments/tpu/examples/mamba3/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba3.model`/
symbols:
  Mamba3Mixer.forward: Mamba3Mixer#forward().
  Mamba3Mixer.n_heads: Mamba3Mixer#n_heads.
  Mamba3Mixer.Zeta: Mamba3Mixer#Zeta.
  Mamba3Mixer.d_state: Mamba3Mixer#d_state.
  Mamba3Mixer.num_rope_angles: Mamba3Mixer#num_rope_angles.
  Mamba3Mixer.mimo_rank: Mamba3Mixer#mimo_rank.
  Mamba3LM.lm_head: Mamba3LM#lm_head.
  Mamba3LM.init_weights: Mamba3LM#init_weights().
  Mamba3LM.forward: Mamba3LM#forward().
  _Module: _Module.
  Mamba3Config: Mamba3Config#
  Mamba3Config.vocab_size: Mamba3Config#vocab_size.
  Mamba3LM.tok_embeddings: Mamba3LM#tok_embeddings.
  Mamba3Mixer.d_inner: Mamba3Mixer#d_inner.
  Mamba3Config.d_model: Mamba3Config#d_model.
  Mamba3LM: Mamba3LM#
  Mamba3Mixer.B_bias: Mamba3Mixer#B_bias.
  Mamba3Mixer.C_bias: Mamba3Mixer#C_bias.
  Mamba3Mixer.Psi: Mamba3Mixer#Psi.
  Mamba3Mixer.Phi: Mamba3Mixer#Phi.
  Mamba3Config.n_heads: Mamba3Config#n_heads.
  Mamba3Mixer.is_mimo: Mamba3Mixer#is_mimo.
  Mamba3Mixer.head_dim: Mamba3Mixer#head_dim.
  _BaseConfig: _BaseConfig.
  Mamba3Config.d_inner: Mamba3Config#d_inner().
  Mamba3LM.norm: Mamba3LM#norm.
  Mamba3Config.n_layers: Mamba3Config#n_layers.
  Mamba3Config.d_state: Mamba3Config#d_state.
  Mamba3Config.head_dim: Mamba3Config#head_dim().
  Mamba3Mixer.out_proj: Mamba3Mixer#out_proj.
  Mamba3Block.norm: Mamba3Block#norm.
  Mamba3LM.layers: Mamba3LM#layers.
  Mamba3Mixer.d_model: Mamba3Mixer#d_model.
  Mamba3Config.chunk_size: Mamba3Config#chunk_size.
  Mamba3Block.forward: Mamba3Block#forward().
  Mamba3LM.config: Mamba3LM#config.
  _BaseModel: _BaseModel.
  Mamba3Mixer: Mamba3Mixer#
  Mamba3Mixer.in_proj: Mamba3Mixer#in_proj.
  Mamba3Mixer.B_norm_weight: Mamba3Mixer#B_norm_weight.
  Mamba3Mixer.C_norm_weight: Mamba3Mixer#C_norm_weight.
  Mamba3Block: Mamba3Block#
  Mamba3LM.enable_weight_tying: Mamba3LM#enable_weight_tying.
  Mamba3Mixer._rmsnorm: Mamba3Mixer#_rmsnorm().
  Mamba3Mixer.A_floor: Mamba3Mixer#A_floor.
  Mamba3Mixer.D: Mamba3Mixer#D.
  Mamba3Block.mixer: Mamba3Block#mixer.
  Mamba3Config.build: Mamba3Config#build().
  Mamba3Mixer.__init__: Mamba3Mixer#__init__().
  Mamba3Block.__init__: Mamba3Block#__init__().
  Mamba3LM.__init__: Mamba3LM#__init__().
  Mamba3LM.embedding: Mamba3LM#embedding.
  Mamba3LM.norm_f: Mamba3LM#norm_f.
  Mamba3Config.expand: Mamba3Config#expand.
  Mamba3Config.rms_norm_eps: Mamba3Config#rms_norm_eps.
  Mamba3Config.mimo_rank: Mamba3Config#mimo_rank.
  Mamba3Config.tie_embeddings: Mamba3Config#tie_embeddings.
  Mamba3Config.enable_weight_tying: Mamba3Config#enable_weight_tying.
  Mamba3Config.ssm_backend: Mamba3Config#ssm_backend.
  Mamba3Config.is_mimo: Mamba3Config#is_mimo.
  Mamba3Config.rope_fraction: Mamba3Config#rope_fraction.
  Mamba3Mixer.chunk_size: Mamba3Mixer#chunk_size.
  Mamba3Mixer.rope_fraction: Mamba3Mixer#rope_fraction.
  Mamba3Mixer.dt_bias: Mamba3Mixer#dt_bias.
  Mamba3Config.A_floor: Mamba3Config#A_floor.
  Mamba3Config.dt_min: Mamba3Config#dt_min.
  Mamba3Config.dt_max: Mamba3Config#dt_max.
  Mamba3Config.dt_init_floor: Mamba3Config#dt_init_floor.
  Mamba3Config.update_from_config: Mamba3Config#update_from_config().
  Mamba3Config.get_nparams_and_flops: Mamba3Config#get_nparams_and_flops().
  Mamba3Mixer.config: Mamba3Mixer#config.
  Mamba3LM.verify_module_protocol: Mamba3LM#verify_module_protocol().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba3/model.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py)

## Classes
### <a id="Mamba3Block"></a>`Mamba3Block`
- def: [`torchtitan/experiments/tpu/examples/mamba3/model.py:247`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L247)
- doc: A single residual block containing Mamba-3 mixer.
- signature: `class Mamba3Block(_Module):`
- members:
  - <a id="Mamba3Block.forward"></a>`forward(self, x: torch.Tensor, *args, **kwargs)` — [`L255`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L255)
  - <a id="Mamba3Block.mixer"></a>`mixer` — [`L253`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L253)
  - <a id="Mamba3Block.norm"></a>`norm` — [`L252`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L252)
- protocol/private: <a id="Mamba3Block.__init__"></a>`__init__`[`L250`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L250)
- uses (calls/refs, reference-scoped): (5 test-only callers)
- used by: (2 test-only callers)

### <a id="Mamba3Config"></a>`Mamba3Config`
- def: [`torchtitan/experiments/tpu/examples/mamba3/model.py:31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L31)
- doc: Configuration for Mamba-3 architecture.
- signature: `class Mamba3Config(_BaseConfig):`
- members:
  - <a id="Mamba3Config.build"></a>`build(self)` — [`L64`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L64)
  - <a id="Mamba3Config.d_inner"></a>`d_inner(self)` — [`L54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L54)
  - <a id="Mamba3Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L67)
  - <a id="Mamba3Config.head_dim"></a>`head_dim(self)` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L58)
  - <a id="Mamba3Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L61)
  - <a id="Mamba3Config.A_floor"></a>`A_floor` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L48)
  - <a id="Mamba3Config.chunk_size"></a>`chunk_size` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L40)
  - <a id="Mamba3Config.d_model"></a>`d_model` — [`L35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L35)
  - <a id="Mamba3Config.d_state"></a>`d_state` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L38)
  - <a id="Mamba3Config.dt_init_floor"></a>`dt_init_floor` — [`L51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L51)
  - <a id="Mamba3Config.dt_max"></a>`dt_max` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L50)
  - <a id="Mamba3Config.dt_min"></a>`dt_min` — [`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L49)
  - <a id="Mamba3Config.enable_weight_tying"></a>`enable_weight_tying` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L43)
  - <a id="Mamba3Config.expand"></a>`expand` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L39)
  - <a id="Mamba3Config.is_mimo"></a>`is_mimo` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L45)
  - <a id="Mamba3Config.mimo_rank"></a>`mimo_rank` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L46)
  - <a id="Mamba3Config.n_heads"></a>`n_heads` — [`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L37)
  - <a id="Mamba3Config.n_layers"></a>`n_layers` — [`L36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L36)
  - <a id="Mamba3Config.rms_norm_eps"></a>`rms_norm_eps` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L41)
  - <a id="Mamba3Config.rope_fraction"></a>`rope_fraction` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L47)
  - <a id="Mamba3Config.ssm_backend"></a>`ssm_backend` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L44)
  - <a id="Mamba3Config.tie_embeddings"></a>`tie_embeddings` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L42)
  - <a id="Mamba3Config.vocab_size"></a>`vocab_size` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L34)
- uses (calls/refs, reference-scoped): (2 test-only callers)
- used by: (22 test-only callers)

### <a id="Mamba3LM"></a>`Mamba3LM`
- def: [`torchtitan/experiments/tpu/examples/mamba3/model.py:259`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L259)
- members:
  - <a id="Mamba3LM.forward"></a>`forward(self, input_ids: torch.Tensor, *args, **kwargs)` — [`L321`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L321)
  - <a id="Mamba3LM.init_weights"></a>`init_weights(self, buffer_device=None, **kwargs)` — [`L283`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L283)
  - <a id="Mamba3LM.verify_module_protocol"></a>`verify_module_protocol(self)` — [`L280`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L280)
  - <a id="Mamba3LM.config"></a>`config` — [`L264`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L264)
  - <a id="Mamba3LM.embedding"></a>`embedding` — [`L269`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L269)
  - <a id="Mamba3LM.enable_weight_tying"></a>`enable_weight_tying` — [`L265`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L265)
  - <a id="Mamba3LM.layers"></a>`layers` — [`L270`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L270)
  - <a id="Mamba3LM.lm_head"></a>`lm_head` — [`L275`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L275)
  - <a id="Mamba3LM.norm"></a>`norm` — [`L273`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L273)
  - <a id="Mamba3LM.norm_f"></a>`norm_f` — [`L274`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L274)
  - <a id="Mamba3LM.tok_embeddings"></a>`tok_embeddings` — [`L268`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L268)
- protocol/private: <a id="Mamba3LM.__init__"></a>`__init__`[`L262`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L262)
- uses (calls/refs, reference-scoped): [`unflatten_tensor`](../../unflatten_shim.md#unflatten_tensor), [`flatten_tensor`](../../unflatten_shim.md#flatten_tensor)  (9 test-only)
- used by: (7 test-only callers)

### <a id="Mamba3Mixer"></a>`Mamba3Mixer`
- def: [`torchtitan/experiments/tpu/examples/mamba3/model.py:75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L75)
- doc: Mamba-3 SSM Mixer block powered by Pallas custom TPU kernel.
- signature: `class Mamba3Mixer(_Module):`
- members:
  - <a id="Mamba3Mixer.forward"></a>`forward(self, u: torch.Tensor)` — [`L155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L155)
  - <a id="Mamba3Mixer.A_floor"></a>`A_floor` — [`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L88)
  - <a id="Mamba3Mixer.B_bias"></a>`B_bias` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L105)
  - <a id="Mamba3Mixer.B_norm_weight"></a>`B_norm_weight` — [`L142`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L142)
  - <a id="Mamba3Mixer.C_bias"></a>`C_bias` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L108)
  - <a id="Mamba3Mixer.C_norm_weight"></a>`C_norm_weight` — [`L143`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L143)
  - <a id="Mamba3Mixer.D"></a>`D` — [`L144`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L144)
  - <a id="Mamba3Mixer.Phi"></a>`Phi` — [`L115`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L115)
  - <a id="Mamba3Mixer.Psi"></a>`Psi` — [`L111`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L111)
  - <a id="Mamba3Mixer.Zeta"></a>`Zeta` — [`L119`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L119)
  - <a id="Mamba3Mixer.chunk_size"></a>`chunk_size` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L86)
  - <a id="Mamba3Mixer.config"></a>`config` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L80)
  - <a id="Mamba3Mixer.d_inner"></a>`d_inner` — [`L82`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L82)
  - <a id="Mamba3Mixer.d_model"></a>`d_model` — [`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L81)
  - <a id="Mamba3Mixer.d_state"></a>`d_state` — [`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L85)
  - <a id="Mamba3Mixer.dt_bias"></a>`dt_bias` — [`L140`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L140)
  - <a id="Mamba3Mixer.head_dim"></a>`head_dim` — [`L84`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L84)
  - <a id="Mamba3Mixer.in_proj"></a>`in_proj` — [`L104`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L104)
  - <a id="Mamba3Mixer.is_mimo"></a>`is_mimo` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L87)
  - <a id="Mamba3Mixer.mimo_rank"></a>`mimo_rank` — [`L95`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L95)
  - <a id="Mamba3Mixer.n_heads"></a>`n_heads` — [`L83`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L83)
  - <a id="Mamba3Mixer.num_rope_angles"></a>`num_rope_angles` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L97)
  - <a id="Mamba3Mixer.out_proj"></a>`out_proj` — [`L145`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L145)
  - <a id="Mamba3Mixer.rope_fraction"></a>`rope_fraction` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L96)
- protocol/private: <a id="Mamba3Mixer.__init__"></a>`__init__`[`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L78), <a id="Mamba3Mixer._rmsnorm"></a>`_rmsnorm`[`L148`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L148)
- uses (calls/refs, reference-scoped): (9 test-only callers)
- used by: (2 test-only callers)

## Module values
- <a id="_BaseConfig"></a>`_BaseConfig` — [`L20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L20)
- <a id="_BaseModel"></a>`_BaseModel` — [`L19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L19)
- <a id="_Module"></a>`_Module` — [`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba3/model.py#L21)

