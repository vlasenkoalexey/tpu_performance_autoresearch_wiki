---
title: 'Module: torchtitan/models/kimi_k3/vision_encoder.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/vision_encoder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.vision_encoder`/
symbols:
  KimiK3VisionEncoder.Config: KimiK3VisionEncoder#Config#
  KimiK3VisionEncoder: KimiK3VisionEncoder#
  KimiK3VisionProjector.forward: KimiK3VisionProjector#forward().
  KimiK3VisionProjector.Config: KimiK3VisionProjector#Config#
  KimiK3VisionProjector.Config.linear_1: KimiK3VisionProjector#Config#linear_1.
  KimiK3VisionProjector.Config.linear_2: KimiK3VisionProjector#Config#linear_2.
  KimiK3VisionProjector.Config.post_norm: KimiK3VisionProjector#Config#post_norm.
  KimiK3VisionProjector.Config.activation: KimiK3VisionProjector#Config#activation.
  KimiK3VisionProjector.linear_1: KimiK3VisionProjector#linear_1.
  KimiK3VisionProjector.linear_2: KimiK3VisionProjector#linear_2.
  KimiK3VisionProjector.post_norm: KimiK3VisionProjector#post_norm.
  KimiK3VisionProjector.activation: KimiK3VisionProjector#activation.
  KimiK3VisionEncoder.Config.final_norm: KimiK3VisionEncoder#Config#final_norm.
  KimiK3VisionProjector: KimiK3VisionProjector#
  KimiK3VisionEncoder.Config.patch_size: KimiK3VisionEncoder#Config#patch_size.
  KimiK3VisionProjector.__init__: KimiK3VisionProjector#__init__().
  KimiK3VisionEncoder.Config.in_channels: KimiK3VisionEncoder#Config#in_channels.
  KimiK3VisionEncoder.Config.merge_kernel_size: KimiK3VisionEncoder#Config#merge_kernel_size.
  KimiK3VisionEncoder.Config.max_num_frames: KimiK3VisionEncoder#Config#max_num_frames.
  KimiK3VisionEncoder.Config.projector: KimiK3VisionEncoder#Config#projector.
---
# Module: [`torchtitan/models/kimi_k3/vision_encoder.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py)

## Classes
### <a id="KimiK3VisionEncoder"></a>`KimiK3VisionEncoder`  ·  implements/extends MoonViTEncoder
- def: [`torchtitan/models/kimi_k3/vision_encoder.py:47`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L47) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- signature: `class KimiK3VisionEncoder(MoonViTEncoder):`
- uses (calls/refs, reference-scoped): [`MoonViTEncoder`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`_set_vision_buffer_sharding`](sharding.md#_set_vision_buffer_sharding), [`MoonViTEncoder`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder), [`vision_encoder`](model.md#KimiK3Model.Config.vision_encoder)

### <a id="KimiK3VisionEncoder.Config"></a>`KimiK3VisionEncoder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/vision_encoder.py:49`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L49) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- signature: `class Config(MoonViTEncoder.Config):`
- members:
  - <a id="KimiK3VisionEncoder.Config.final_norm"></a>`final_norm` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L55)
  - <a id="KimiK3VisionEncoder.Config.in_channels"></a>`in_channels` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L51)
  - <a id="KimiK3VisionEncoder.Config.max_num_frames"></a>`max_num_frames` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L53)
  - <a id="KimiK3VisionEncoder.Config.merge_kernel_size"></a>`merge_kernel_size` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L52)
  - <a id="KimiK3VisionEncoder.Config.patch_size"></a>`patch_size` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L50)
  - <a id="KimiK3VisionEncoder.Config.projector"></a>`projector` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L56)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`MoonViTEncoder`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder), [`Config`](../kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config), [`Config`](vision_encoder.md#KimiK3VisionProjector.Config), [`KimiK3VisionProjector`](vision_encoder.md#KimiK3VisionProjector)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`to_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.to_hf), [`_set_vision_buffer_sharding`](sharding.md#_set_vision_buffer_sharding), [`vision_encoder`](model.md#KimiK3Model.Config.vision_encoder)

### <a id="KimiK3VisionProjector"></a>`KimiK3VisionProjector`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/vision_encoder.py:25`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L25)
- doc: PatchMergerMLPV2 projector from merged vision features to text width.
- signature: `class KimiK3VisionProjector(Module):`
- members:
  - <a id="KimiK3VisionProjector.forward"></a>`forward(self, merged_MF: torch.Tensor)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L42)
  - <a id="KimiK3VisionProjector.activation"></a>`activation` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L40)
  - <a id="KimiK3VisionProjector.linear_1"></a>`linear_1` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L37)
  - <a id="KimiK3VisionProjector.linear_2"></a>`linear_2` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L38)
  - <a id="KimiK3VisionProjector.post_norm"></a>`post_norm` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L39)
- protocol/private: <a id="KimiK3VisionProjector.__init__"></a>`__init__`[`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L35)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](vision_encoder.md#KimiK3VisionProjector.Config), [`activation`](vision_encoder.md#KimiK3VisionProjector.Config.activation), [`linear_1`](vision_encoder.md#KimiK3VisionProjector.Config.linear_1), [`linear_2`](vision_encoder.md#KimiK3VisionProjector.Config.linear_2), [`post_norm`](vision_encoder.md#KimiK3VisionProjector.Config.post_norm)
- used by: [`Module`](../../protocols/module.md#Module), [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`Config`](vision_encoder.md#KimiK3VisionEncoder.Config)

### <a id="KimiK3VisionProjector.Config"></a>`KimiK3VisionProjector.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/vision_encoder.py:29`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L29)
- signature: `class Config(Module.Config):`
- members:
  - <a id="KimiK3VisionProjector.Config.activation"></a>`activation` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L33)
  - <a id="KimiK3VisionProjector.Config.linear_1"></a>`linear_1` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L30)
  - <a id="KimiK3VisionProjector.Config.linear_2"></a>`linear_2` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L31)
  - <a id="KimiK3VisionProjector.Config.post_norm"></a>`post_norm` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/vision_encoder.py#L32)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`GELU`](../common/nn_modules.md#GELU), [`Config`](../common/nn_modules.md#GELU.Config)
- used by: [`_vision_encoder_config`](__init__.md#_vision_encoder_config), [`Config`](vision_encoder.md#KimiK3VisionEncoder.Config), [`activation`](vision_encoder.md#KimiK3VisionProjector.activation), [`linear_1`](vision_encoder.md#KimiK3VisionProjector.linear_1), [`linear_2`](vision_encoder.md#KimiK3VisionProjector.linear_2), [`post_norm`](vision_encoder.md#KimiK3VisionProjector.post_norm), [`__init__`](vision_encoder.md#KimiK3VisionProjector.__init__)

