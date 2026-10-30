---
title: 'Module: torchtitan/models/flux/model/autoencoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/model/autoencoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.model.autoencoder`/
symbols:
  Encoder.down: Encoder#down.
  Decoder.up: Decoder#up.
  AutoEncoder.decoder: AutoEncoder#decoder.
  AutoEncoder.encoder: AutoEncoder#encoder.
  Encoder.mid: Encoder#mid.
  Decoder.mid: Decoder#mid.
  Encoder.conv_in: Encoder#conv_in.
  ResnetBlock.conv2: ResnetBlock#conv2.
  ResnetBlock.conv1: ResnetBlock#conv1.
  AttnBlock.norm: AttnBlock#norm.
  ResnetBlock.nin_shortcut: ResnetBlock#nin_shortcut.
  Downsample.conv: Downsample#conv.
  Upsample.conv: Upsample#conv.
  Encoder.conv_out: Encoder#conv_out.
  Decoder.conv_in: Decoder#conv_in.
  Decoder.conv_out: Decoder#conv_out.
  ResnetBlock.forward: ResnetBlock#forward().
  Encoder.forward: Encoder#forward().
  Decoder.forward: Decoder#forward().
  AutoEncoder: AutoEncoder#
  _norm: _norm().
  AutoEncoder.Config: AutoEncoder#Config#
  ResnetBlock.Config: ResnetBlock#Config#
  ResnetBlock.Config.out_channels: ResnetBlock#Config#out_channels.
  AutoEncoder.encode: AutoEncoder#encode().
  AttnBlock.attention: AttnBlock#attention().
  ResnetBlock.Config.in_channels: ResnetBlock#Config#in_channels.
  Decoder.ffactor: Decoder#ffactor.
  AutoEncoder.decode: AutoEncoder#decode().
  load_ae: load_ae().
  ResnetBlock: ResnetBlock#
  ResnetBlock.norm1: ResnetBlock#norm1.
  ResnetBlock.norm2: ResnetBlock#norm2.
  AutoEncoder.reg: AutoEncoder#reg.
  AttnBlock.Config: AttnBlock#Config#
  Decoder.num_resolutions: Decoder#num_resolutions.
  Downsample.Config: Downsample#Config#
  Upsample.Config: Upsample#Config#
  Encoder.Config: Encoder#Config#
  Decoder.Config: Decoder#Config#
  DiagonalGaussian.Config: DiagonalGaussian#Config#
  Encoder.num_resolutions: Encoder#num_resolutions.
  AttnBlock.Config.in_channels: AttnBlock#Config#in_channels.
  Encoder.norm_out: Encoder#norm_out.
  Decoder.norm_out: Decoder#norm_out.
  AutoEncoder.Config.resolution: AutoEncoder#Config#resolution.
  AutoEncoder.Config.in_channels: AutoEncoder#Config#in_channels.
  AutoEncoder.Config.ch: AutoEncoder#Config#ch.
  AutoEncoder.Config.ch_mult: AutoEncoder#Config#ch_mult.
  AutoEncoder.Config.num_res_blocks: AutoEncoder#Config#num_res_blocks.
  AutoEncoder.Config.z_channels: AutoEncoder#Config#z_channels.
  AttnBlock.forward: AttnBlock#forward().
  DiagonalGaussian.forward: DiagonalGaussian#forward().
  AutoEncoder.Config.out_ch: AutoEncoder#Config#out_ch.
  AutoEncoder.Config.scale_factor: AutoEncoder#Config#scale_factor.
  AutoEncoder.Config.shift_factor: AutoEncoder#Config#shift_factor.
  AutoEncoder.forward: AutoEncoder#forward().
  AttnBlock: AttnBlock#
  ResnetBlock.in_channels: ResnetBlock#in_channels.
  ResnetBlock.out_channels: ResnetBlock#out_channels.
  Encoder.ch: Encoder#ch.
  Encoder.num_res_blocks: Encoder#num_res_blocks.
  Decoder.num_res_blocks: Decoder#num_res_blocks.
  AutoEncoder.scale_factor: AutoEncoder#scale_factor.
  AutoEncoder.shift_factor: AutoEncoder#shift_factor.
  swish: swish().
  Encoder.Config.ch: Encoder#Config#ch.
  Encoder.Config.ch_mult: Encoder#Config#ch_mult.
  Decoder.Config.ch: Decoder#Config#ch.
  Decoder.Config.ch_mult: Decoder#Config#ch_mult.
  AttnBlock.q: AttnBlock#q.
  AttnBlock.k: AttnBlock#k.
  AttnBlock.v: AttnBlock#v.
  AttnBlock.proj_out: AttnBlock#proj_out.
  Downsample: Downsample#
  Upsample: Upsample#
  Encoder: Encoder#
  Decoder: Decoder#
  DiagonalGaussian: DiagonalGaussian#
  DiagonalGaussian.sample: DiagonalGaussian#sample.
  DiagonalGaussian.chunk_dim: DiagonalGaussian#chunk_dim.
  Downsample.Config.in_channels: Downsample#Config#in_channels.
  Upsample.Config.in_channels: Upsample#Config#in_channels.
  Encoder.Config.resolution: Encoder#Config#resolution.
  Encoder.Config.in_channels: Encoder#Config#in_channels.
  Decoder.Config.resolution: Decoder#Config#resolution.
  Decoder.Config.z_channels: Decoder#Config#z_channels.
  AttnBlock.__init__: AttnBlock#__init__().
  AttnBlock.in_channels: AttnBlock#in_channels.
  ResnetBlock.__init__: ResnetBlock#__init__().
  Downsample.__init__: Downsample#__init__().
  Downsample.forward: Downsample#forward().
  Upsample.__init__: Upsample#__init__().
  Upsample.forward: Upsample#forward().
  Encoder.__init__: Encoder#__init__().
  Encoder.resolution: Encoder#resolution.
  Encoder.in_channels: Encoder#in_channels.
  Decoder.__init__: Decoder#__init__().
  Decoder.ch: Decoder#ch.
  Decoder.resolution: Decoder#resolution.
  Decoder.in_channels: Decoder#in_channels.
  Decoder.z_shape: Decoder#z_shape.
  DiagonalGaussian.__init__: DiagonalGaussian#__init__().
  AutoEncoder.__init__: AutoEncoder#__init__().
  Encoder.Config.num_res_blocks: Encoder#Config#num_res_blocks.
  Encoder.Config.z_channels: Encoder#Config#z_channels.
  Decoder.Config.out_ch: Decoder#Config#out_ch.
  Decoder.Config.num_res_blocks: Decoder#Config#num_res_blocks.
  Decoder.Config.in_channels: Decoder#Config#in_channels.
  DiagonalGaussian.Config.sample: DiagonalGaussian#Config#sample.
  DiagonalGaussian.Config.chunk_dim: DiagonalGaussian#Config#chunk_dim.
  AutoEncoder.init_weights: AutoEncoder#init_weights().
---
# Module: [`torchtitan/models/flux/model/autoencoder.py`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py)

## Classes
### <a id="AttnBlock"></a>`AttnBlock`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:27`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L27)
- signature: `class AttnBlock(Module):`
- members:
  - <a id="AttnBlock.attention"></a>`attention(self, h_: Tensor)` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L48)
  - <a id="AttnBlock.forward"></a>`forward(self, x: Tensor)` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L62)
  - <a id="AttnBlock.in_channels"></a>`in_channels` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L34)
  - <a id="AttnBlock.k"></a>`k` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L44)
  - <a id="AttnBlock.norm"></a>`norm` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L36)
  - <a id="AttnBlock.proj_out"></a>`proj_out` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L46)
  - <a id="AttnBlock.q"></a>`q` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L43)
  - <a id="AttnBlock.v"></a>`v` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L45)
- protocol/private: <a id="AttnBlock.__init__"></a>`__init__`[`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L32)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`_norm`](autoencoder.md#_norm), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`Config`](autoencoder.md#AttnBlock.Config), [`in_channels`](autoencoder.md#AttnBlock.Config.in_channels)
- used by: [`Module`](../../../protocols/module.md#Module), [`mid`](autoencoder.md#Decoder.mid), [`mid`](autoencoder.md#Encoder.mid)

### <a id="AttnBlock.Config"></a>`AttnBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:29`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L29)
- signature: `class Config(Module.Config):`
- members:
  - <a id="AttnBlock.Config.in_channels"></a>`in_channels` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L30)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`mid`](autoencoder.md#Decoder.mid), [`mid`](autoencoder.md#Encoder.mid), [`norm`](autoencoder.md#AttnBlock.norm), [`__init__`](autoencoder.md#AttnBlock.__init__), [`in_channels`](autoencoder.md#AttnBlock.in_channels)

### <a id="AutoEncoder"></a>`AutoEncoder`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:385`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L385) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- signature: `class AutoEncoder(Module):`
- members:
  - <a id="AutoEncoder.decode"></a>`decode(self, z: Tensor)` — [`L427`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L427)
  - <a id="AutoEncoder.encode"></a>`encode(self, x: Tensor)` — [`L422`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L422)
  - <a id="AutoEncoder.forward"></a>`forward(self, x: Tensor)` — [`L431`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L431)
  - <a id="AutoEncoder.init_weights"></a>`init_weights(self)` — [`L434`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L434)
  - <a id="AutoEncoder.decoder"></a>`decoder` — [`L408`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L408) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="AutoEncoder.encoder"></a>`encoder` — [`L400`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L400) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="AutoEncoder.reg"></a>`reg` — [`L417`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L417)
  - <a id="AutoEncoder.scale_factor"></a>`scale_factor` — [`L419`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L419)
  - <a id="AutoEncoder.shift_factor"></a>`shift_factor` — [`L420`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L420)
- protocol/private: <a id="AutoEncoder.__init__"></a>`__init__`[`L398`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L398)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`Config`](autoencoder.md#AutoEncoder.Config), [`Config`](autoencoder.md#Decoder.Config), [`Config`](autoencoder.md#DiagonalGaussian.Config), [`Config`](autoencoder.md#Encoder.Config), [`ch`](autoencoder.md#AutoEncoder.Config.ch), [`ch_mult`](autoencoder.md#AutoEncoder.Config.ch_mult), [`in_channels`](autoencoder.md#AutoEncoder.Config.in_channels), [`num_res_blocks`](autoencoder.md#AutoEncoder.Config.num_res_blocks), [`resolution`](autoencoder.md#AutoEncoder.Config.resolution), [`z_channels`](autoencoder.md#AutoEncoder.Config.z_channels), [`out_ch`](autoencoder.md#AutoEncoder.Config.out_ch), [`scale_factor`](autoencoder.md#AutoEncoder.Config.scale_factor), [`shift_factor`](autoencoder.md#AutoEncoder.Config.shift_factor), [`ch`](autoencoder.md#Decoder.Config.ch), [`ch`](autoencoder.md#Encoder.Config.ch), [`ch_mult`](autoencoder.md#Decoder.Config.ch_mult), [`ch_mult`](autoencoder.md#Encoder.Config.ch_mult), [`Decoder`](autoencoder.md#Decoder), [`DiagonalGaussian`](autoencoder.md#DiagonalGaussian), [`Encoder`](autoencoder.md#Encoder), [`in_channels`](autoencoder.md#Encoder.Config.in_channels), [`resolution`](autoencoder.md#Decoder.Config.resolution), [`resolution`](autoencoder.md#Encoder.Config.resolution), [`z_channels`](autoencoder.md#Decoder.Config.z_channels), [`in_channels`](autoencoder.md#Decoder.Config.in_channels), [`num_res_blocks`](autoencoder.md#Decoder.Config.num_res_blocks), [`num_res_blocks`](autoencoder.md#Encoder.Config.num_res_blocks), [`out_ch`](autoencoder.md#Decoder.Config.out_ch), [`z_channels`](autoencoder.md#Encoder.Config.z_channels)
- used by: [`Module`](../../../protocols/module.md#Module), [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`t5_encoder`](../trainer.md#FluxTrainer.t5_encoder), [`generate_image`](../inference/sampling.md#generate_image), [`preprocess_data`](../utils.md#preprocess_data), [`autoencoder`](model.md#FluxModel.Config.autoencoder), [`load_ae`](autoencoder.md#load_ae), [`flux_init`](../validate.md#FluxValidator.flux_init)

### <a id="AutoEncoder.Config"></a>`AutoEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:387`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L387)
- signature: `class Config(Module.Config):`
- members:
  - <a id="AutoEncoder.Config.ch"></a>`ch` — [`L390`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L390)
  - <a id="AutoEncoder.Config.ch_mult"></a>`ch_mult` — [`L392`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L392)
  - <a id="AutoEncoder.Config.in_channels"></a>`in_channels` — [`L389`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L389)
  - <a id="AutoEncoder.Config.num_res_blocks"></a>`num_res_blocks` — [`L393`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L393)
  - <a id="AutoEncoder.Config.out_ch"></a>`out_ch` — [`L391`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L391)
  - <a id="AutoEncoder.Config.resolution"></a>`resolution` — [`L388`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L388)
  - <a id="AutoEncoder.Config.scale_factor"></a>`scale_factor` — [`L395`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L395)
  - <a id="AutoEncoder.Config.shift_factor"></a>`shift_factor` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L396)
  - <a id="AutoEncoder.Config.z_channels"></a>`z_channels` — [`L394`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L394)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`decoder`](autoencoder.md#AutoEncoder.decoder), [`encoder`](autoencoder.md#AutoEncoder.encoder), [`autoencoder`](model.md#FluxModel.Config.autoencoder), [`load_ae`](autoencoder.md#load_ae), [`scale_factor`](autoencoder.md#AutoEncoder.scale_factor), [`shift_factor`](autoencoder.md#AutoEncoder.shift_factor), [`__init__`](autoencoder.md#AutoEncoder.__init__)

### <a id="Decoder"></a>`Decoder`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:255`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L255)
- signature: `class Decoder(Module):`
- members:
  - <a id="Decoder.forward"></a>`forward(self, z: Tensor)` — [`L328`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L328)
  - <a id="Decoder.ch"></a>`ch` — [`L268`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L268)
  - <a id="Decoder.conv_in"></a>`conv_in` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L281)
  - <a id="Decoder.conv_out"></a>`conv_out` — [`L321`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L321)
  - <a id="Decoder.ffactor"></a>`ffactor` — [`L273`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L273)
  - <a id="Decoder.in_channels"></a>`in_channels` — [`L272`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L272)
  - <a id="Decoder.mid"></a>`mid` — [`L289`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L289) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="Decoder.norm_out"></a>`norm_out` — [`L320`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L320)
  - <a id="Decoder.num_res_blocks"></a>`num_res_blocks` — [`L270`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L270)
  - <a id="Decoder.num_resolutions"></a>`num_resolutions` — [`L269`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L269)
  - <a id="Decoder.resolution"></a>`resolution` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L271)
  - <a id="Decoder.up"></a>`up` — [`L299`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L299) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="Decoder.z_shape"></a>`z_shape` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L278)
- protocol/private: <a id="Decoder.__init__"></a>`__init__`[`L266`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L266)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`ModuleList`](../../../protocols/module.md#ModuleList), [`_norm`](autoencoder.md#_norm), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`Config`](autoencoder.md#ResnetBlock.Config), [`out_channels`](autoencoder.md#ResnetBlock.Config.out_channels), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`in_channels`](autoencoder.md#ResnetBlock.Config.in_channels), [`ResnetBlock`](autoencoder.md#ResnetBlock), [`Config`](autoencoder.md#AttnBlock.Config), [`padding`](../../common/nn_modules.md#Conv2d.Config.padding), [`Config`](autoencoder.md#Decoder.Config), [`Config`](autoencoder.md#Upsample.Config), [`in_channels`](autoencoder.md#AttnBlock.Config.in_channels), [`AttnBlock`](autoencoder.md#AttnBlock), [`ch`](autoencoder.md#Decoder.Config.ch), [`ch_mult`](autoencoder.md#Decoder.Config.ch_mult), [`swish`](autoencoder.md#swish), [`Upsample`](autoencoder.md#Upsample), [`in_channels`](autoencoder.md#Upsample.Config.in_channels), [`resolution`](autoencoder.md#Decoder.Config.resolution), [`z_channels`](autoencoder.md#Decoder.Config.z_channels), [`in_channels`](autoencoder.md#Decoder.Config.in_channels), [`num_res_blocks`](autoencoder.md#Decoder.Config.num_res_blocks), [`out_ch`](autoencoder.md#Decoder.Config.out_ch)
- used by: [`Module`](../../../protocols/module.md#Module), [`decoder`](autoencoder.md#AutoEncoder.decoder)

### <a id="Decoder.Config"></a>`Decoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:257`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L257)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Decoder.Config.ch"></a>`ch` — [`L258`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L258)
  - <a id="Decoder.Config.ch_mult"></a>`ch_mult` — [`L260`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L260)
  - <a id="Decoder.Config.in_channels"></a>`in_channels` — [`L262`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L262)
  - <a id="Decoder.Config.num_res_blocks"></a>`num_res_blocks` — [`L261`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L261)
  - <a id="Decoder.Config.out_ch"></a>`out_ch` — [`L259`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L259)
  - <a id="Decoder.Config.resolution"></a>`resolution` — [`L263`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L263)
  - <a id="Decoder.Config.z_channels"></a>`z_channels` — [`L264`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L264)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`decoder`](autoencoder.md#AutoEncoder.decoder), [`up`](autoencoder.md#Decoder.up), [`conv_in`](autoencoder.md#Decoder.conv_in), [`conv_out`](autoencoder.md#Decoder.conv_out), [`ffactor`](autoencoder.md#Decoder.ffactor), [`num_resolutions`](autoencoder.md#Decoder.num_resolutions), [`num_res_blocks`](autoencoder.md#Decoder.num_res_blocks), [`__init__`](autoencoder.md#Decoder.__init__), [`ch`](autoencoder.md#Decoder.ch), [`in_channels`](autoencoder.md#Decoder.in_channels), [`resolution`](autoencoder.md#Decoder.resolution), [`z_shape`](autoencoder.md#Decoder.z_shape)

### <a id="DiagonalGaussian"></a>`DiagonalGaussian`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:365`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L365)
- signature: `class DiagonalGaussian(Module):`
- members:
  - <a id="DiagonalGaussian.forward"></a>`forward(self, z: Tensor)` — [`L376`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L376)
  - <a id="DiagonalGaussian.chunk_dim"></a>`chunk_dim` — [`L374`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L374)
  - <a id="DiagonalGaussian.sample"></a>`sample` — [`L373`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L373)
- protocol/private: <a id="DiagonalGaussian.__init__"></a>`__init__`[`L371`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L371)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](autoencoder.md#DiagonalGaussian.Config), [`chunk_dim`](autoencoder.md#DiagonalGaussian.Config.chunk_dim), [`sample`](autoencoder.md#DiagonalGaussian.Config.sample)
- used by: [`Module`](../../../protocols/module.md#Module), [`reg`](autoencoder.md#AutoEncoder.reg)

### <a id="DiagonalGaussian.Config"></a>`DiagonalGaussian.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:367`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L367)
- signature: `class Config(Module.Config):`
- members:
  - <a id="DiagonalGaussian.Config.chunk_dim"></a>`chunk_dim` — [`L369`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L369)
  - <a id="DiagonalGaussian.Config.sample"></a>`sample` — [`L368`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L368)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`reg`](autoencoder.md#AutoEncoder.reg), [`chunk_dim`](autoencoder.md#DiagonalGaussian.chunk_dim), [`sample`](autoencoder.md#DiagonalGaussian.sample), [`__init__`](autoencoder.md#DiagonalGaussian.__init__)

### <a id="Downsample"></a>`Downsample`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:114`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L114)
- signature: `class Downsample(Module):`
- members:
  - <a id="Downsample.forward"></a>`forward(self, x: Tensor)` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L129)
  - <a id="Downsample.conv"></a>`conv` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L122)
- protocol/private: <a id="Downsample.__init__"></a>`__init__`[`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L119)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`Config`](autoencoder.md#Downsample.Config), [`in_channels`](autoencoder.md#Downsample.Config.in_channels), [`stride`](../../common/nn_modules.md#Conv2d.Config.stride)
- used by: [`Module`](../../../protocols/module.md#Module), [`down`](autoencoder.md#Encoder.down)

### <a id="Downsample.Config"></a>`Downsample.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:116`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L116)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Downsample.Config.in_channels"></a>`in_channels` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L117)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`down`](autoencoder.md#Encoder.down), [`conv`](autoencoder.md#Downsample.conv), [`__init__`](autoencoder.md#Downsample.__init__)

### <a id="Encoder"></a>`Encoder`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:156`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L156)
- signature: `class Encoder(Module):`
- members:
  - <a id="Encoder.forward"></a>`forward(self, x: Tensor)` — [`L224`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L224)
  - <a id="Encoder.ch"></a>`ch` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L168)
  - <a id="Encoder.conv_in"></a>`conv_in` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L174)
  - <a id="Encoder.conv_out"></a>`conv_out` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L217)
  - <a id="Encoder.down"></a>`down` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L183) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="Encoder.in_channels"></a>`in_channels` — [`L172`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L172)
  - <a id="Encoder.mid"></a>`mid` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L206) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="Encoder.norm_out"></a>`norm_out` — [`L216`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L216)
  - <a id="Encoder.num_res_blocks"></a>`num_res_blocks` — [`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L170)
  - <a id="Encoder.num_resolutions"></a>`num_resolutions` — [`L169`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L169)
  - <a id="Encoder.resolution"></a>`resolution` — [`L171`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L171)
- protocol/private: <a id="Encoder.__init__"></a>`__init__`[`L166`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L166)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`ModuleList`](../../../protocols/module.md#ModuleList), [`_norm`](autoencoder.md#_norm), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`Config`](autoencoder.md#ResnetBlock.Config), [`out_channels`](autoencoder.md#ResnetBlock.Config.out_channels), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`in_channels`](autoencoder.md#ResnetBlock.Config.in_channels), [`ResnetBlock`](autoencoder.md#ResnetBlock), [`Config`](autoencoder.md#AttnBlock.Config), [`padding`](../../common/nn_modules.md#Conv2d.Config.padding), [`Config`](autoencoder.md#Downsample.Config), [`Config`](autoencoder.md#Encoder.Config), [`in_channels`](autoencoder.md#AttnBlock.Config.in_channels), [`AttnBlock`](autoencoder.md#AttnBlock), [`ch`](autoencoder.md#Encoder.Config.ch), [`ch_mult`](autoencoder.md#Encoder.Config.ch_mult), [`swish`](autoencoder.md#swish), [`Downsample`](autoencoder.md#Downsample), [`in_channels`](autoencoder.md#Downsample.Config.in_channels), [`in_channels`](autoencoder.md#Encoder.Config.in_channels), [`resolution`](autoencoder.md#Encoder.Config.resolution), [`num_res_blocks`](autoencoder.md#Encoder.Config.num_res_blocks), [`z_channels`](autoencoder.md#Encoder.Config.z_channels)
- used by: [`Module`](../../../protocols/module.md#Module), [`encoder`](autoencoder.md#AutoEncoder.encoder)

### <a id="Encoder.Config"></a>`Encoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:158`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L158)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Encoder.Config.ch"></a>`ch` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L161)
  - <a id="Encoder.Config.ch_mult"></a>`ch_mult` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L162)
  - <a id="Encoder.Config.in_channels"></a>`in_channels` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L160)
  - <a id="Encoder.Config.num_res_blocks"></a>`num_res_blocks` — [`L163`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L163)
  - <a id="Encoder.Config.resolution"></a>`resolution` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L159)
  - <a id="Encoder.Config.z_channels"></a>`z_channels` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L164)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`down`](autoencoder.md#Encoder.down), [`encoder`](autoencoder.md#AutoEncoder.encoder), [`conv_in`](autoencoder.md#Encoder.conv_in), [`conv_out`](autoencoder.md#Encoder.conv_out), [`num_resolutions`](autoencoder.md#Encoder.num_resolutions), [`ch`](autoencoder.md#Encoder.ch), [`num_res_blocks`](autoencoder.md#Encoder.num_res_blocks), [`__init__`](autoencoder.md#Encoder.__init__), [`in_channels`](autoencoder.md#Encoder.in_channels), [`resolution`](autoencoder.md#Encoder.resolution)

### <a id="ResnetBlock"></a>`ResnetBlock`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:66`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L66)
- signature: `class ResnetBlock(Module):`
- members:
  - <a id="ResnetBlock.forward"></a>`forward(self, x)` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L98)
  - <a id="ResnetBlock.conv1"></a>`conv1` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L78)
  - <a id="ResnetBlock.conv2"></a>`conv2` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L85)
  - <a id="ResnetBlock.in_channels"></a>`in_channels` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L74)
  - <a id="ResnetBlock.nin_shortcut"></a>`nin_shortcut` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L92)
  - <a id="ResnetBlock.norm1"></a>`norm1` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L77)
  - <a id="ResnetBlock.norm2"></a>`norm2` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L84)
  - <a id="ResnetBlock.out_channels"></a>`out_channels` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L75)
- protocol/private: <a id="ResnetBlock.__init__"></a>`__init__`[`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L72)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`_norm`](autoencoder.md#_norm), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`Config`](autoencoder.md#ResnetBlock.Config), [`out_channels`](autoencoder.md#ResnetBlock.Config.out_channels), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`in_channels`](autoencoder.md#ResnetBlock.Config.in_channels), [`padding`](../../common/nn_modules.md#Conv2d.Config.padding), [`swish`](autoencoder.md#swish)
- used by: [`Module`](../../../protocols/module.md#Module), [`down`](autoencoder.md#Encoder.down), [`up`](autoencoder.md#Decoder.up), [`mid`](autoencoder.md#Decoder.mid), [`mid`](autoencoder.md#Encoder.mid)

### <a id="ResnetBlock.Config"></a>`ResnetBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:68`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L68)
- signature: `class Config(Module.Config):`
- members:
  - <a id="ResnetBlock.Config.in_channels"></a>`in_channels` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L69)
  - <a id="ResnetBlock.Config.out_channels"></a>`out_channels` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L70)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`down`](autoencoder.md#Encoder.down), [`up`](autoencoder.md#Decoder.up), [`mid`](autoencoder.md#Decoder.mid), [`mid`](autoencoder.md#Encoder.mid), [`conv2`](autoencoder.md#ResnetBlock.conv2), [`conv1`](autoencoder.md#ResnetBlock.conv1), [`nin_shortcut`](autoencoder.md#ResnetBlock.nin_shortcut), [`norm1`](autoencoder.md#ResnetBlock.norm1), [`norm2`](autoencoder.md#ResnetBlock.norm2), [`in_channels`](autoencoder.md#ResnetBlock.in_channels), [`out_channels`](autoencoder.md#ResnetBlock.out_channels), [`__init__`](autoencoder.md#ResnetBlock.__init__)

### <a id="Upsample"></a>`Upsample`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/autoencoder.py:136`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L136)
- signature: `class Upsample(Module):`
- members:
  - <a id="Upsample.forward"></a>`forward(self, x: Tensor)` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L150)
  - <a id="Upsample.conv"></a>`conv` — [`L143`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L143)
- protocol/private: <a id="Upsample.__init__"></a>`__init__`[`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L141)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`build`](../../../protocols/module.md#Module.Config.build), [`Config`](../../common/nn_modules.md#Conv2d.Config), [`Conv2d`](../../common/nn_modules.md#Conv2d), [`in_channels`](../../common/nn_modules.md#Conv2d.Config.in_channels), [`kernel_size`](../../common/nn_modules.md#Conv2d.Config.kernel_size), [`out_channels`](../../common/nn_modules.md#Conv2d.Config.out_channels), [`padding`](../../common/nn_modules.md#Conv2d.Config.padding), [`Config`](autoencoder.md#Upsample.Config), [`in_channels`](autoencoder.md#Upsample.Config.in_channels)
- used by: [`Module`](../../../protocols/module.md#Module), [`up`](autoencoder.md#Decoder.up)

### <a id="Upsample.Config"></a>`Upsample.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/autoencoder.py:138`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L138)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Upsample.Config.in_channels"></a>`in_channels` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L139)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`up`](autoencoder.md#Decoder.up), [`conv`](autoencoder.md#Upsample.conv), [`__init__`](autoencoder.md#Upsample.__init__)

## Functions
- <a id="_norm"></a>`_norm(num_channels: int)` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L23)
- <a id="load_ae"></a>`load_ae(ckpt_path: str, autoencoder_config: AutoEncoder.Config, device: str | torch.device = "cuda", dtype=torch.bfloat16, random_init=False)` — [`L445`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L445) — Build the autoencoder from a Config and optionally load weights.
- <a id="swish"></a>`swish(x: Tensor)` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/autoencoder.py#L19)

