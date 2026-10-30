---
title: 'Module: torchtitan/experiments/tpu/examples/mamba2/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/mamba2/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.mamba2.model`/
symbols:
  Mamba2Mixer.forward: Mamba2Mixer#forward().
  Mamba2Config: Mamba2Config#
  Mamba2Config.vocab_size: Mamba2Config#vocab_size.
  Mamba2LM.lm_head: Mamba2LM#lm_head.
  Mamba2LM.init_weights: Mamba2LM#init_weights().
  Mamba2Config.d_model: Mamba2Config#d_model.
  Mamba2LM.forward: Mamba2LM#forward().
  Mamba2Config.n_heads: Mamba2Config#n_heads.
  Mamba2Mixer.n_groups: Mamba2Mixer#n_groups.
  Mamba2Mixer.in_proj: Mamba2Mixer#in_proj.
  Mamba2Mixer.d_inner: Mamba2Mixer#d_inner.
  Mamba2LM.tok_embeddings: Mamba2LM#tok_embeddings.
  Mamba2Mixer.d_state: Mamba2Mixer#d_state.
  Mamba2LM: Mamba2LM#
  Mamba2Config.n_layers: Mamba2Config#n_layers.
  Mamba2Config.d_state: Mamba2Config#d_state.
  Mamba2Config.d_conv: Mamba2Config#d_conv.
  Mamba2Mixer.conv1d: Mamba2Mixer#conv1d.
  Mamba2Mixer.norm: Mamba2Mixer#norm.
  Mamba2Mixer.n_heads: Mamba2Mixer#n_heads.
  Mamba2Config.expand: Mamba2Config#expand.
  Mamba2Config.d_inner: Mamba2Config#d_inner().
  Mamba2LM.norm: Mamba2LM#norm.
  Mamba2Config.ssm_backend: Mamba2Config#ssm_backend.
  Mamba2Config.head_dim: Mamba2Config#head_dim().
  Mamba2Mixer.D: Mamba2Mixer#D.
  Mamba2Mixer.out_proj: Mamba2Mixer#out_proj.
  Mamba2Block.norm: Mamba2Block#norm.
  Mamba2LM.layers: Mamba2LM#layers.
  Mamba2Mixer: Mamba2Mixer#
  Mamba2Block: Mamba2Block#
  GatedRMSNorm.forward: GatedRMSNorm#forward().
  Mamba2Config.chunk_size: Mamba2Config#chunk_size.
  Mamba2Block.forward: Mamba2Block#forward().
  GatedRMSNorm: GatedRMSNorm#
  Mamba2Mixer.d_model: Mamba2Mixer#d_model.
  Mamba2Mixer.head_dim: Mamba2Mixer#head_dim.
  Mamba2Mixer.d_conv: Mamba2Mixer#d_conv.
  Mamba2LM.enable_weight_tying: Mamba2LM#enable_weight_tying.
  Mamba2Mixer.chunk_size: Mamba2Mixer#chunk_size.
  Mamba2Mixer.A_log: Mamba2Mixer#A_log.
  Mamba2Block.mixer: Mamba2Block#mixer.
  PallasMamba2Config: PallasMamba2Config.
  PallasMamba2LM: PallasMamba2LM.
  PallasMamba2Block: PallasMamba2Block.
  PallasMamba2Mixer: PallasMamba2Mixer.
  Mamba2Config.n_groups: Mamba2Config#n_groups.
  Mamba2Config.rms_norm_eps: Mamba2Config#rms_norm_eps.
  Mamba2Config.build: Mamba2Config#build().
  Mamba2Mixer.__init__: Mamba2Mixer#__init__().
  Mamba2Block.__init__: Mamba2Block#__init__().
  Mamba2LM.__init__: Mamba2LM#__init__().
  Mamba2LM.embedding: Mamba2LM#embedding.
  Mamba2LM.norm_f: Mamba2LM#norm_f.
  GatedRMSNorm.eps: GatedRMSNorm#eps.
  GatedRMSNorm.weight: GatedRMSNorm#weight.
  Mamba2Config.tie_embeddings: Mamba2Config#tie_embeddings.
  Mamba2Config.enable_weight_tying: Mamba2Config#enable_weight_tying.
  Mamba2LM.config: Mamba2LM#config.
  GatedRMSNorm.__init__: GatedRMSNorm#__init__().
  Mamba2Config.update_from_config: Mamba2Config#update_from_config().
  Mamba2Config.get_nparams_and_flops: Mamba2Config#get_nparams_and_flops().
  Mamba2LM.verify_module_protocol: Mamba2LM#verify_module_protocol().
---
# Module: [`torchtitan/experiments/tpu/examples/mamba2/model.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py)

## Classes
### <a id="GatedRMSNorm"></a>`GatedRMSNorm`  ·  implements/extends Module
- def: [`torchtitan/experiments/tpu/examples/mamba2/model.py:22`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L22)
- signature: `class GatedRMSNorm(module.Module):`
- members:
  - <a id="GatedRMSNorm.forward"></a>`forward(self, x: torch.Tensor, z: torch.Tensor)` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L29)
  - <a id="GatedRMSNorm.eps"></a>`eps` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L26)
  - <a id="GatedRMSNorm.weight"></a>`weight` — [`L27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L27)
- protocol/private: <a id="GatedRMSNorm.__init__"></a>`__init__`[`L24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L24)
- uses (calls/refs, reference-scoped): [`Module`](../../../../protocols/module.md#Module)
- used by: [`Module`](../../../../protocols/module.md#Module)  (2 test-only)

### <a id="Mamba2Block"></a>`Mamba2Block`  ·  implements/extends Module
- def: [`torchtitan/experiments/tpu/examples/mamba2/model.py:167`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L167)
- doc: A single residual block containing Mamba-2 mixer.
- signature: `class Mamba2Block(module.Module):`
- members:
  - <a id="Mamba2Block.forward"></a>`forward(self, x: torch.Tensor, *args, **kwargs)` — [`L175`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L175)
  - <a id="Mamba2Block.mixer"></a>`mixer` — [`L173`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L173)
  - <a id="Mamba2Block.norm"></a>`norm` — [`L172`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L172)
- protocol/private: <a id="Mamba2Block.__init__"></a>`__init__`[`L170`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L170)
- uses (calls/refs, reference-scoped): [`Module`](../../../../protocols/module.md#Module)  (4 test-only)
- used by: [`Module`](../../../../protocols/module.md#Module)  (3 test-only)

### <a id="Mamba2Config"></a>`Mamba2Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/mamba2/model.py:34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L34)
- doc: Configuration for Mamba-2 architecture.
- signature: `class Mamba2Config(model_protocol.BaseModel.Config):`
- members:
  - <a id="Mamba2Config.build"></a>`build(self)` — [`L62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L62)
  - <a id="Mamba2Config.d_inner"></a>`d_inner(self)` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L52)
  - <a id="Mamba2Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L65`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L65)
  - <a id="Mamba2Config.head_dim"></a>`head_dim(self)` — [`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L56)
  - <a id="Mamba2Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L59`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L59)
  - <a id="Mamba2Config.chunk_size"></a>`chunk_size` — [`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L45)
  - <a id="Mamba2Config.d_conv"></a>`d_conv` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L43)
  - <a id="Mamba2Config.d_model"></a>`d_model` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L38)
  - <a id="Mamba2Config.d_state"></a>`d_state` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L42)
  - <a id="Mamba2Config.enable_weight_tying"></a>`enable_weight_tying` — [`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L48)
  - <a id="Mamba2Config.expand"></a>`expand` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L44)
  - <a id="Mamba2Config.n_groups"></a>`n_groups` — [`L41`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L41)
  - <a id="Mamba2Config.n_heads"></a>`n_heads` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L40)
  - <a id="Mamba2Config.n_layers"></a>`n_layers` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L39)
  - <a id="Mamba2Config.rms_norm_eps"></a>`rms_norm_eps` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L46)
  - <a id="Mamba2Config.ssm_backend"></a>`ssm_backend` — [`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L49)
  - <a id="Mamba2Config.tie_embeddings"></a>`tie_embeddings` — [`L47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L47)
  - <a id="Mamba2Config.vocab_size"></a>`vocab_size` — [`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L37)
- uses (calls/refs, reference-scoped): [`BaseModel`](../../../../protocols/model.md#BaseModel), [`Config`](../../../../protocols/model.md#BaseModel.Config)  (1 test-only)
- used by: (31 test-only callers)

### <a id="Mamba2LM"></a>`Mamba2LM`
- def: [`torchtitan/experiments/tpu/examples/mamba2/model.py:179`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L179)
- members:
  - <a id="Mamba2LM.forward"></a>`forward(self, input_ids: torch.Tensor, *args, **kwargs)` — [`L229`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L229)
  - <a id="Mamba2LM.init_weights"></a>`init_weights(self, buffer_device=None, **kwargs)` — [`L204`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L204) — Initialize model weights with DTensor support.
  - <a id="Mamba2LM.verify_module_protocol"></a>`verify_module_protocol(self)` — [`L200`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L200) — Verify module protocol compatibility.
  - <a id="Mamba2LM.config"></a>`config` — [`L184`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L184)
  - <a id="Mamba2LM.embedding"></a>`embedding` — [`L189`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L189)
  - <a id="Mamba2LM.enable_weight_tying"></a>`enable_weight_tying` — [`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L185)
  - <a id="Mamba2LM.layers"></a>`layers` — [`L190`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L190)
  - <a id="Mamba2LM.lm_head"></a>`lm_head` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L195)
  - <a id="Mamba2LM.norm"></a>`norm` — [`L193`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L193)
  - <a id="Mamba2LM.norm_f"></a>`norm_f` — [`L194`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L194)
  - <a id="Mamba2LM.tok_embeddings"></a>`tok_embeddings` — [`L188`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L188)
- protocol/private: <a id="Mamba2LM.__init__"></a>`__init__`[`L182`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L182)
- uses (calls/refs, reference-scoped): [`BaseModel`](../../../../protocols/model.md#BaseModel), [`unflatten_tensor`](../../unflatten_shim.md#unflatten_tensor), [`flatten_tensor`](../../unflatten_shim.md#flatten_tensor)  (8 test-only)
- used by: [`init_weights`](../../../../protocols/model.md#BaseModel.init_weights), [`verify_module_protocol`](../../../../protocols/model.md#BaseModel.verify_module_protocol)  (8 test-only)

### <a id="Mamba2Mixer"></a>`Mamba2Mixer`  ·  implements/extends Module
- def: [`torchtitan/experiments/tpu/examples/mamba2/model.py:73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L73)
- doc: Mamba-2 SSD Mixer block powered by Pallas custom TPU kernel.
- signature: `class Mamba2Mixer(module.Module):`
- members:
  - <a id="Mamba2Mixer.forward"></a>`forward(self, u: torch.Tensor)` — [`L116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L116)
  - <a id="Mamba2Mixer.A_log"></a>`A_log` — [`L107`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L107)
  - <a id="Mamba2Mixer.D"></a>`D` — [`L110`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L110)
  - <a id="Mamba2Mixer.chunk_size"></a>`chunk_size` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L87)
  - <a id="Mamba2Mixer.conv1d"></a>`conv1d` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L97)
  - <a id="Mamba2Mixer.d_conv"></a>`d_conv` — [`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L86)
  - <a id="Mamba2Mixer.d_inner"></a>`d_inner` — [`L79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L79)
  - <a id="Mamba2Mixer.d_model"></a>`d_model` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L78)
  - <a id="Mamba2Mixer.d_state"></a>`d_state` — [`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L85)
  - <a id="Mamba2Mixer.head_dim"></a>`head_dim` — [`L84`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L84)
  - <a id="Mamba2Mixer.in_proj"></a>`in_proj` — [`L90`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L90)
  - <a id="Mamba2Mixer.n_groups"></a>`n_groups` — [`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L81)
  - <a id="Mamba2Mixer.n_heads"></a>`n_heads` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L80)
  - <a id="Mamba2Mixer.norm"></a>`norm` — [`L113`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L113)
  - <a id="Mamba2Mixer.out_proj"></a>`out_proj` — [`L114`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L114)
- protocol/private: <a id="Mamba2Mixer.__init__"></a>`__init__`[`L76`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L76)
- uses (calls/refs, reference-scoped): [`Module`](../../../../protocols/module.md#Module)  (12 test-only)
- used by: [`Module`](../../../../protocols/module.md#Module)  (3 test-only)

## Module values
- <a id="PallasMamba2Block"></a>`PallasMamba2Block` — [`L246`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L246)
- <a id="PallasMamba2Config"></a>`PallasMamba2Config` — [`L244`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L244)
- <a id="PallasMamba2LM"></a>`PallasMamba2LM` — [`L245`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L245)
- <a id="PallasMamba2Mixer"></a>`PallasMamba2Mixer` — [`L247`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/mamba2/model.py#L247)

