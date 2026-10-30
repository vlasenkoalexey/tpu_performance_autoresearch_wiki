---
title: 'Module: torchtitan/models/deepseek_v4/mtp.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/mtp.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.mtp`/
symbols:
  MTPBlock.forward: MTPBlock#forward().
  MTPBlock.Config: MTPBlock#Config#
  MTPBlock.Config.enorm: MTPBlock#Config#enorm.
  MTPBlock.Config.hnorm: MTPBlock#Config#hnorm.
  MTPBlock.Config.e_proj: MTPBlock#Config#e_proj.
  MTPBlock.Config.h_proj: MTPBlock#Config#h_proj.
  MTPBlock.Config.mtp_norm: MTPBlock#Config#mtp_norm.
  MTPBlock.Config.hc_head: MTPBlock#Config#hc_head.
  MTPBlock: MTPBlock#
  MTPBlock.h_proj: MTPBlock#h_proj.
  MTPBlock.enorm: MTPBlock#enorm.
  MTPBlock.hnorm: MTPBlock#hnorm.
  MTPBlock.e_proj: MTPBlock#e_proj.
  MTPBlock.mtp_norm: MTPBlock#mtp_norm.
  MTPBlock.hc_head: MTPBlock#hc_head.
  MTPBlock.__init__: MTPBlock#__init__().
  __all__: __all__.
---
# Module: [`torchtitan/models/deepseek_v4/mtp.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py)

## Classes
### <a id="MTPBlock"></a>`MTPBlock`  ·  implements/extends DeepSeekV4TransformerBlock
- def: [`torchtitan/models/deepseek_v4/mtp.py:24`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L24)
- doc: One auxiliary multi-token prediction depth for DeepSeek V4.
- signature: `class MTPBlock(DeepSeekV4TransformerBlock):`
- members:
  - <a id="MTPBlock.forward"></a>`forward(self, mtp_input_embed: torch.Tensor, prev_hc_hidden: torch.Tensor, mtp_input_ids_T: torch.Tensor, mtp_input_valid_mask: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L45)
  - <a id="MTPBlock.e_proj"></a>`e_proj` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L40)
  - <a id="MTPBlock.enorm"></a>`enorm` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L38)
  - <a id="MTPBlock.h_proj"></a>`h_proj` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L41)
  - <a id="MTPBlock.hc_head"></a>`hc_head` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L43)
  - <a id="MTPBlock.hnorm"></a>`hnorm` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L39)
  - <a id="MTPBlock.mtp_norm"></a>`mtp_norm` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L42)
- protocol/private: <a id="MTPBlock.__init__"></a>`__init__`[`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L36)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`forward`](model.md#DeepSeekV4TransformerBlock.forward), [`DeepSeekV4TransformerBlock`](model.md#DeepSeekV4TransformerBlock), [`Config`](mtp.md#MTPBlock.Config), [`e_proj`](mtp.md#MTPBlock.Config.e_proj), [`enorm`](mtp.md#MTPBlock.Config.enorm), [`h_proj`](mtp.md#MTPBlock.Config.h_proj), [`hc_head`](mtp.md#MTPBlock.Config.hc_head), [`hnorm`](mtp.md#MTPBlock.Config.hnorm), [`mtp_norm`](mtp.md#MTPBlock.Config.mtp_norm), [`__init__`](model.md#DeepSeekV4TransformerBlock.__init__)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`get_nparams_and_flops`](model.md#DeepSeekV4Model.Config.get_nparams_and_flops), [`forward`](model.md#DeepSeekV4TransformerBlock.forward), [`DeepSeekV4TransformerBlock`](model.md#DeepSeekV4TransformerBlock), [`mtp_layers`](model.md#DeepSeekV4Model.Config.mtp_layers)

### <a id="MTPBlock.Config"></a>`MTPBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/mtp.py:28`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L28)
- signature: `class Config(DeepSeekV4TransformerBlock.Config):`
- members:
  - <a id="MTPBlock.Config.e_proj"></a>`e_proj` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L31)
  - <a id="MTPBlock.Config.enorm"></a>`enorm` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L29)
  - <a id="MTPBlock.Config.h_proj"></a>`h_proj` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L32)
  - <a id="MTPBlock.Config.hc_head"></a>`hc_head` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L34) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="MTPBlock.Config.hnorm"></a>`hnorm` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L30)
  - <a id="MTPBlock.Config.mtp_norm"></a>`mtp_norm` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L33)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`DeepSeekV4TransformerBlock`](model.md#DeepSeekV4TransformerBlock), [`Config`](model.md#DeepSeekV4TransformerBlock.Config), [`Config`](mhc.md#HcHead.Config), [`HcHead`](mhc.md#HcHead)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`set_deepseek_v4_sharding_config`](sharding.md#set_deepseek_v4_sharding_config), [`mtp_layers`](model.md#DeepSeekV4Model.Config.mtp_layers), [`h_proj`](mtp.md#MTPBlock.h_proj), [`e_proj`](mtp.md#MTPBlock.e_proj), [`enorm`](mtp.md#MTPBlock.enorm), [`hc_head`](mtp.md#MTPBlock.hc_head), [`hnorm`](mtp.md#MTPBlock.hnorm), [`mtp_norm`](mtp.md#MTPBlock.mtp_norm), [`__init__`](mtp.md#MTPBlock.__init__)

## Module values
- <a id="__all__"></a>`__all__` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/mtp.py#L77)

