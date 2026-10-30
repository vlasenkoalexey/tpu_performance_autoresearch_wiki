---
title: 'Module: torchtitan/models/deepseek_v3/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v3.model`/
symbols:
  Attention.forward: Attention#forward().
  DeepSeekV3Model: DeepSeekV3Model#
  Attention: Attention#
  DeepSeekV3Model.Config: DeepSeekV3Model#Config#
  Attention.softmax_scale: Attention#softmax_scale.
  get_deepseek_v3_nparams_and_flops: get_deepseek_v3_nparams_and_flops().
  DeepSeekV3TransformerBlock.forward: DeepSeekV3TransformerBlock#forward().
  Attention.Config: Attention#Config#
  Attention.Config.inner_attention: Attention#Config#inner_attention.
  Attention.wq: Attention#wq.
  DeepSeekV3Model.Config.dim: DeepSeekV3Model#Config#dim.
  DeepSeekV3Model.Config.vocab_size: DeepSeekV3Model#Config#vocab_size.
  Attention.rope: Attention#rope.
  Attention.Config.rope: Attention#Config#rope.
  Attention.qk_nope_head_dim: Attention#qk_nope_head_dim.
  Attention.v_head_dim: Attention#v_head_dim.
  Attention.Config.wq: Attention#Config#wq.
  Attention.Config.wq_a: Attention#Config#wq_a.
  Attention.Config.wq_b: Attention#Config#wq_b.
  Attention.inner_attention: Attention#inner_attention.
  DeepSeekV3Model.Config.update_from_config: DeepSeekV3Model#Config#update_from_config().
  DeepSeekV3TransformerBlock: DeepSeekV3TransformerBlock#
  Attention.Config.wkv_a: Attention#Config#wkv_a.
  Attention.Config.wkv_b: Attention#Config#wkv_b.
  Attention.Config.wo: Attention#Config#wo.
  Attention.Config.q_norm: Attention#Config#q_norm.
  Attention.Config.kv_norm: Attention#Config#kv_norm.
  Attention.qk_head_dim: Attention#qk_head_dim.
  DeepSeekV3TransformerBlock.Config: DeepSeekV3TransformerBlock#Config#
  DeepSeekV3TransformerBlock.moe: DeepSeekV3TransformerBlock#moe.
  Attention.wq_b: Attention#wq_b.
  Attention.wkv_b: Attention#wkv_b.
  Attention.wq_a: Attention#wq_a.
  Attention.q_norm: Attention#q_norm.
  Attention.wkv_a: Attention#wkv_a.
  Attention.kv_norm: Attention#kv_norm.
  Attention.wo: Attention#wo.
  DeepSeekV3TransformerBlock.ffn_norm: DeepSeekV3TransformerBlock#ffn_norm.
  DeepSeekV3TransformerBlock.moe_enabled: DeepSeekV3TransformerBlock#moe_enabled.
  Attention.q_lora_rank: Attention#q_lora_rank.
  Attention.Config.qk_nope_head_dim: Attention#Config#qk_nope_head_dim.
  DeepSeekV3TransformerBlock.attention: DeepSeekV3TransformerBlock#attention.
  DeepSeekV3TransformerBlock.attention_norm: DeepSeekV3TransformerBlock#attention_norm.
  DeepSeekV3TransformerBlock.feed_forward: DeepSeekV3TransformerBlock#feed_forward.
  Attention.qk_rope_head_dim: Attention#qk_rope_head_dim.
  Attention.Config.q_lora_rank: Attention#Config#q_lora_rank.
  Attention.Config.qk_rope_head_dim: Attention#Config#qk_rope_head_dim.
  Attention.kv_lora_rank: Attention#kv_lora_rank.
  Attention.Config.v_head_dim: Attention#Config#v_head_dim.
  Attention.__init__: Attention#__init__().
  Attention.Config.n_heads: Attention#Config#n_heads.
  Attention.Config.dim: Attention#Config#dim.
  Attention.Config.kv_lora_rank: Attention#Config#kv_lora_rank.
  Attention.dim: Attention#dim.
  Attention.n_heads: Attention#n_heads.
  DeepSeekV3TransformerBlock.__init__: DeepSeekV3TransformerBlock#__init__().
  DeepSeekV3Model.Config.get_nparams_and_flops: DeepSeekV3Model#Config#get_nparams_and_flops().
  Attention.Config.mscale: Attention#Config#mscale.
---
# Module: [`torchtitan/models/deepseek_v3/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py)

## Classes
### <a id="Attention"></a>`Attention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/deepseek_v3/model.py:32`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L32) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- doc: Multi-head latent attention (MLA) module.
- signature: `class Attention(BaseAttention):`
- members:
  - <a id="Attention.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L99) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="Attention.dim"></a>`dim` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L64)
  - <a id="Attention.inner_attention"></a>`inner_attention` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L96)
  - <a id="Attention.kv_lora_rank"></a>`kv_lora_rank` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L67)
  - <a id="Attention.kv_norm"></a>`kv_norm` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L87)
  - <a id="Attention.n_heads"></a>`n_heads` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L65)
  - <a id="Attention.q_lora_rank"></a>`q_lora_rank` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L66)
  - <a id="Attention.q_norm"></a>`q_norm` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L81)
  - <a id="Attention.qk_head_dim"></a>`qk_head_dim` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L70)
  - <a id="Attention.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L68)
  - <a id="Attention.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L69)
  - <a id="Attention.rope"></a>`rope` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L97)
  - <a id="Attention.softmax_scale"></a>`softmax_scale` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L90) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="Attention.v_head_dim"></a>`v_head_dim` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L71)
  - <a id="Attention.wkv_a"></a>`wkv_a` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L86)
  - <a id="Attention.wkv_b"></a>`wkv_b` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L88)
  - <a id="Attention.wo"></a>`wo` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L89)
  - <a id="Attention.wq"></a>`wq` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L75)
  - <a id="Attention.wq_a"></a>`wq_a` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L80)
  - <a id="Attention.wq_b"></a>`wq_b` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L82)
- protocol/private: <a id="Attention.__init__"></a>`__init__`[`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L62)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`forward`](../../overrides/fused_mla.md#FusedMLAAttention.forward), [`BaseAttention`](../common/attention.md#BaseAttention), [`scaling`](../common/rope.md#RoPE.Config.scaling), [`rope_factor`](../common/rope.md#RoPE.Config.rope_factor), [`Config`](model.md#Attention.Config), [`inner_attention`](model.md#Attention.Config.inner_attention), [`rope`](model.md#Attention.Config.rope), [`wq`](model.md#Attention.Config.wq), [`wq_a`](model.md#Attention.Config.wq_a), [`wq_b`](model.md#Attention.Config.wq_b), [`kv_norm`](model.md#Attention.Config.kv_norm), [`q_norm`](model.md#Attention.Config.q_norm), [`wkv_a`](model.md#Attention.Config.wkv_a), [`wkv_b`](model.md#Attention.Config.wkv_b), [`wo`](model.md#Attention.Config.wo), [`qk_nope_head_dim`](model.md#Attention.Config.qk_nope_head_dim), [`q_lora_rank`](model.md#Attention.Config.q_lora_rank), [`qk_rope_head_dim`](model.md#Attention.Config.qk_rope_head_dim), [`FusedMLAAttention`](../../overrides/fused_mla.md#FusedMLAAttention), [`v_head_dim`](model.md#Attention.Config.v_head_dim), [`dim`](model.md#Attention.Config.dim), [`kv_lora_rank`](model.md#Attention.Config.kv_lora_rank), [`n_heads`](model.md#Attention.Config.n_heads), [`mscale`](model.md#Attention.Config.mscale)
- used by: [`_dist_muon_optimizer`](../kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_set_deepseek_v3_layer_sharding`](sharding.md#_set_deepseek_v3_layer_sharding), [`make_mla_attention_config`](__init__.md#make_mla_attention_config), [`forward`](../../overrides/fused_mla.md#FusedMLAAttention.forward), [`BaseAttention`](../common/attention.md#BaseAttention), [`_clip_mla_weights`](../kimi_k2_7/qk_clip.md#_clip_mla_weights), [`fused_mla`](../../overrides/fused_mla.md#fused_mla), [`qk_clip`](../kimi_k2_7/qk_clip.md#qk_clip), [`__init__`](../../overrides/fused_mla.md#FusedMLAAttention.__init__), [`Config`](../../overrides/fused_mla.md#FusedMLAAttention.Config), [`FusedMLAAttention`](../../overrides/fused_mla.md#FusedMLAAttention)  (4 test-only)

### <a id="Attention.Config"></a>`Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/model.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L40) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="Attention.Config.dim"></a>`dim` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L42)
  - <a id="Attention.Config.inner_attention"></a>`inner_attention` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L57)
  - <a id="Attention.Config.kv_lora_rank"></a>`kv_lora_rank` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L50)
  - <a id="Attention.Config.kv_norm"></a>`kv_norm` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L52)
  - <a id="Attention.Config.mscale"></a>`mscale` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L60)
  - <a id="Attention.Config.n_heads"></a>`n_heads` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L41)
  - <a id="Attention.Config.q_lora_rank"></a>`q_lora_rank` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L49)
  - <a id="Attention.Config.q_norm"></a>`q_norm` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L51)
  - <a id="Attention.Config.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L53)
  - <a id="Attention.Config.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L54)
  - <a id="Attention.Config.rope"></a>`rope` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L56)
  - <a id="Attention.Config.v_head_dim"></a>`v_head_dim` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L55)
  - <a id="Attention.Config.wkv_a"></a>`wkv_a` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L46)
  - <a id="Attention.Config.wkv_b"></a>`wkv_b` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L47)
  - <a id="Attention.Config.wo"></a>`wo` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L48)
  - <a id="Attention.Config.wq"></a>`wq` — [`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L43)
  - <a id="Attention.Config.wq_a"></a>`wq_a` — [`L44`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L44)
  - <a id="Attention.Config.wq_b"></a>`wq_b` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L45)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`BaseAttention`](../common/attention.md#BaseAttention), [`RoPE`](../common/rope.md#RoPE), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`Config`](../common/rope.md#RoPE.Config), [`Config`](../common/attention.md#BaseAttention.Config)
- used by: [`_dist_muon_optimizer`](../kimi_k2_7/config_registry.md#_dist_muon_optimizer), [`_set_deepseek_v3_layer_sharding`](sharding.md#_set_deepseek_v3_layer_sharding), [`make_mla_attention_config`](__init__.md#make_mla_attention_config), [`softmax_scale`](model.md#Attention.softmax_scale), [`fused_mla`](../../overrides/fused_mla.md#fused_mla), [`wq`](model.md#Attention.wq), [`rope`](model.md#Attention.rope), [`qk_nope_head_dim`](model.md#Attention.qk_nope_head_dim), [`v_head_dim`](model.md#Attention.v_head_dim), [`inner_attention`](model.md#Attention.inner_attention), [`qk_head_dim`](model.md#Attention.qk_head_dim), [`Config`](../../overrides/fused_mla.md#FusedMLAAttention.Config), [`wkv_b`](model.md#Attention.wkv_b), [`wq_b`](model.md#Attention.wq_b), [`kv_norm`](model.md#Attention.kv_norm), [`q_norm`](model.md#Attention.q_norm), [`wkv_a`](model.md#Attention.wkv_a), [`wo`](model.md#Attention.wo), [`wq_a`](model.md#Attention.wq_a), [`q_lora_rank`](model.md#Attention.q_lora_rank), [`qk_rope_head_dim`](model.md#Attention.qk_rope_head_dim), [`kv_lora_rank`](model.md#Attention.kv_lora_rank), [`__init__`](model.md#Attention.__init__), [`dim`](model.md#Attention.dim), [`n_heads`](model.md#Attention.n_heads)  (1 test-only)

### <a id="DeepSeekV3Model"></a>`DeepSeekV3Model`  ·  implements/extends MTPDecoder
- def: [`torchtitan/models/deepseek_v3/model.py:237`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L237) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- doc: DeepSeek-V3 Transformer model with attention and feed-forward layers.
- signature: `class DeepSeekV3Model(MTPDecoder):`
- uses (calls/refs, reference-scoped): [`KimiK25Model`](../kimi_k2_7/model.md#KimiK25Model), [`MTPDecoder`](mtp.md#MTPDecoder), [`GraphTrainerDeepSeekV3Model`](../../experiments/graph_trainer/deepseek_v3/model.md#GraphTrainerDeepSeekV3Model)
- used by: [`_16b`](__init__.md#_16b), [`_236b`](__init__.md#_236b), [`_671b`](__init__.md#_671b), [`_debugmodel`](__init__.md#_debugmodel), [`_testmodel`](__init__.md#_testmodel), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`set_deepseek_v3_sharding_config`](sharding.md#set_deepseek_v3_sharding_config), [`KimiK25Model`](../kimi_k2_7/model.md#KimiK25Model), [`Config`](../kimi_k2_7/model.md#KimiK25Model.Config), [`MTPDecoder`](mtp.md#MTPDecoder), [`__init__`](state_dict_adapter.md#DeepSeekV3StateDictAdapter.__init__), [`GraphTrainerDeepSeekV3Model`](../../experiments/graph_trainer/deepseek_v3/model.md#GraphTrainerDeepSeekV3Model), [`Config`](../../experiments/graph_trainer/deepseek_v3/model.md#GraphTrainerDeepSeekV3Model.Config)  (8 test-only)

### <a id="DeepSeekV3Model.Config"></a>`DeepSeekV3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/model.py:243`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L243) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- signature: `class Config(MTPDecoder.Config):`
- members:
  - <a id="DeepSeekV3Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L266`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L266)
  - <a id="DeepSeekV3Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L247)
  - <a id="DeepSeekV3Model.Config.dim"></a>`dim` — [`L244`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L244) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
  - <a id="DeepSeekV3Model.Config.vocab_size"></a>`vocab_size` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L245) — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)
- uses (calls/refs, reference-scoped): [`set_deepseek_v3_sharding_config`](sharding.md#set_deepseek_v3_sharding_config), [`get_deepseek_v3_nparams_and_flops`](model.md#get_deepseek_v3_nparams_and_flops), [`update_from_config`](mtp.md#MTPDecoder.Config.update_from_config), [`MTPDecoder`](mtp.md#MTPDecoder), [`Config`](mtp.md#MTPDecoder.Config)
- used by: [`_16b`](__init__.md#_16b), [`_236b`](__init__.md#_236b), [`_671b`](__init__.md#_671b), [`_debugmodel`](__init__.md#_debugmodel), [`_testmodel`](__init__.md#_testmodel), [`_debugmodel`](../kimi_k2_7/__init__.md#_debugmodel), [`_kimi_k2_5`](../kimi_k2_7/__init__.md#_kimi_k2_5), [`_testmodel`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel), [`_testmodel_moe`](../../experiments/tpu/deepseek_v3/__init__.md#_testmodel_moe), [`_moonlight_16b_a3b_config`](../kimi_k2_7/__init__.md#_moonlight_16b_a3b_config), [`set_deepseek_v3_sharding_config`](sharding.md#set_deepseek_v3_sharding_config), [`Config`](../kimi_k2_7/model.md#KimiK25Model.Config), [`__init__`](state_dict_adapter.md#DeepSeekV3StateDictAdapter.__init__), [`Config`](../../experiments/graph_trainer/deepseek_v3/model.md#GraphTrainerDeepSeekV3Model.Config)  (6 test-only)

### <a id="DeepSeekV3TransformerBlock"></a>`DeepSeekV3TransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/deepseek_v3/model.py:162`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L162)
- doc: DeepSeek V3 Transformer block with attention and feed-forward layers.
- signature: `class DeepSeekV3TransformerBlock(TransformerBlock):`
- members:
  - <a id="DeepSeekV3TransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L185)
  - <a id="DeepSeekV3TransformerBlock.attention"></a>`attention` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L173)
  - <a id="DeepSeekV3TransformerBlock.attention_norm"></a>`attention_norm` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L174)
  - <a id="DeepSeekV3TransformerBlock.feed_forward"></a>`feed_forward` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L183)
  - <a id="DeepSeekV3TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L175)
  - <a id="DeepSeekV3TransformerBlock.moe"></a>`moe` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L180)
  - <a id="DeepSeekV3TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L177)
- protocol/private: <a id="DeepSeekV3TransformerBlock.__init__"></a>`__init__`[`L171`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L171)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`moe`](../common/decoder.md#TransformerBlock.Config.moe), [`Config`](model.md#DeepSeekV3TransformerBlock.Config)
- used by: [`_set_deepseek_v3_layer_sharding`](sharding.md#_set_deepseek_v3_layer_sharding), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`build_mla_moe_layers`](__init__.md#build_mla_moe_layers), [`_build_mtp_layers`](__init__.md#_build_mtp_layers)  (1 test-only)

### <a id="DeepSeekV3TransformerBlock.Config"></a>`DeepSeekV3TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v3/model.py:168`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L168)
- signature: `class Config(TransformerBlock.Config):`
- uses (calls/refs, reference-scoped): [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_set_deepseek_v3_layer_sharding`](sharding.md#_set_deepseek_v3_layer_sharding), [`build_mla_moe_layers`](__init__.md#build_mla_moe_layers), [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`__init__`](model.md#DeepSeekV3TransformerBlock.__init__)

## Functions
- <a id="get_deepseek_v3_nparams_and_flops"></a>`get_deepseek_v3_nparams_and_flops(model_config: MTPDecoder.Config, model: nn.Module, seq_len: int, *, modules_excluded_from_active_params: Iterable[nn.Module | None] = ())` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v3/model.py#L202) — Estimate DeepSeek-style decoder FLOPs from the final model config. — documented in [deepseek-v3-model](../../../../concepts/deepseek-v3-model.md)

