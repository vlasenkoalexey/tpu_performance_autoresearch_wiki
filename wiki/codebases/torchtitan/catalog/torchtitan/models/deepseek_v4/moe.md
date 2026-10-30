---
title: 'Module: torchtitan/models/deepseek_v4/moe.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/moe.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.moe`/
symbols:
  DeepSeekV4Router.hash: DeepSeekV4Router#hash.
  DeepSeekV4Router.tid2eid: DeepSeekV4Router#tid2eid.
  DeepSeekV4MoE.Config: DeepSeekV4MoE#Config#
  DeepSeekV4Router.Config: DeepSeekV4Router#Config#
  DeepSeekV4Router._select_experts: DeepSeekV4Router#_select_experts().
  DeepSeekV4MoE: DeepSeekV4MoE#
  DeepSeekV4Router: DeepSeekV4Router#
  DeepSeekV4Router.__init__: DeepSeekV4Router#__init__().
  DeepSeekV4Router._init_self_buffers: DeepSeekV4Router#_init_self_buffers().
  DeepSeekV4Router.vocab_size: DeepSeekV4Router#vocab_size.
  DeepSeekV4Router.Config.layer_id: DeepSeekV4Router#Config#layer_id.
  DeepSeekV4MoE.Config.router: DeepSeekV4MoE#Config#router.
  DeepSeekV4Router.Config.n_hash_layers: DeepSeekV4Router#Config#n_hash_layers.
  DeepSeekV4Router.n_hash_layers: DeepSeekV4Router#n_hash_layers.
  DeepSeekV4Router.layer_id: DeepSeekV4Router#layer_id.
  _build_hash_routing_table: _build_hash_routing_table().
  DeepSeekV4Router.Config.vocab_size: DeepSeekV4Router#Config#vocab_size.
---
# Module: [`torchtitan/models/deepseek_v4/moe.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py)

## Classes
### <a id="DeepSeekV4MoE"></a>`DeepSeekV4MoE`  ·  implements/extends MoE
- def: [`torchtitan/models/deepseek_v4/moe.py:94`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L94)
- doc: DeepSeek V4 MoE that forwards token IDs to hash-routing layers.
- signature: `class DeepSeekV4MoE(MoE):`
- uses (calls/refs, reference-scoped): [`MoE`](../common/moe.md#MoE)
- used by: [`MoE`](../common/moe.md#MoE), [`_make_v4_moe_config`](__init__.md#_make_v4_moe_config), [`moe`](model.md#DeepSeekV4TransformerBlock.Config.moe)

### <a id="DeepSeekV4MoE.Config"></a>`DeepSeekV4MoE.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/moe.py:98`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L98)
- signature: `class Config(MoE.Config):`
- members:
  - <a id="DeepSeekV4MoE.Config.router"></a>`router` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L101)
- uses (calls/refs, reference-scoped): [`MoE`](../common/moe.md#MoE), [`Config`](../common/moe.md#MoE.Config), [`Config`](moe.md#DeepSeekV4Router.Config), [`DeepSeekV4Router`](moe.md#DeepSeekV4Router)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`set_deepseek_v4_layer_sharding`](sharding.md#set_deepseek_v4_layer_sharding), [`_make_v4_moe_config`](__init__.md#_make_v4_moe_config), [`moe`](model.md#DeepSeekV4TransformerBlock.Config.moe)

### <a id="DeepSeekV4Router"></a>`DeepSeekV4Router`  ·  implements/extends TokenChoiceTopKRouter
- def: [`torchtitan/models/deepseek_v4/moe.py:34`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L34)
- doc: DeepSeek V4 router with optional hash-based expert selection.
- signature: `class DeepSeekV4Router(TokenChoiceTopKRouter):`
- members:
  - <a id="DeepSeekV4Router.hash"></a>`hash` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L48)
  - <a id="DeepSeekV4Router.layer_id"></a>`layer_id` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L47)
  - <a id="DeepSeekV4Router.n_hash_layers"></a>`n_hash_layers` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L46)
  - <a id="DeepSeekV4Router.tid2eid"></a>`tid2eid` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L66)
  - <a id="DeepSeekV4Router.vocab_size"></a>`vocab_size` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L45)
- protocol/private: <a id="DeepSeekV4Router.__init__"></a>`__init__`[`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L43), <a id="DeepSeekV4Router._init_self_buffers"></a>`_init_self_buffers`[`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L60), <a id="DeepSeekV4Router._select_experts"></a>`_select_experts`[`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L73)
- uses (calls/refs, reference-scoped): [`TokenChoiceTopKRouter`](../common/moe.md#TokenChoiceTopKRouter), [`_select_experts`](../common/moe.md#TokenChoiceTopKRouter._select_experts), [`num_experts`](../common/moe.md#TokenChoiceTopKRouter.num_experts), [`Config`](moe.md#DeepSeekV4Router.Config), [`top_k`](../common/moe.md#TokenChoiceTopKRouter.top_k), [`__init__`](../common/moe.md#TokenChoiceTopKRouter.__init__), [`layer_id`](moe.md#DeepSeekV4Router.Config.layer_id), [`n_hash_layers`](moe.md#DeepSeekV4Router.Config.n_hash_layers), [`_build_hash_routing_table`](moe.md#_build_hash_routing_table), [`vocab_size`](moe.md#DeepSeekV4Router.Config.vocab_size)
- used by: [`_make_v4_moe_config`](__init__.md#_make_v4_moe_config), [`TokenChoiceTopKRouter`](../common/moe.md#TokenChoiceTopKRouter), [`_init_self_buffers`](../../protocols/module.md#Module._init_self_buffers), [`Config`](moe.md#DeepSeekV4MoE.Config), [`_select_experts`](../common/moe.md#TokenChoiceTopKRouter._select_experts)

### <a id="DeepSeekV4Router.Config"></a>`DeepSeekV4Router.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/moe.py:38`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L38)
- signature: `class Config(TokenChoiceTopKRouter.Config):`
- members:
  - <a id="DeepSeekV4Router.Config.layer_id"></a>`layer_id` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L41)
  - <a id="DeepSeekV4Router.Config.n_hash_layers"></a>`n_hash_layers` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L40)
  - <a id="DeepSeekV4Router.Config.vocab_size"></a>`vocab_size` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L39)
- uses (calls/refs, reference-scoped): [`TokenChoiceTopKRouter`](../common/moe.md#TokenChoiceTopKRouter), [`Config`](../common/moe.md#TokenChoiceTopKRouter.Config)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`_make_v4_moe_config`](__init__.md#_make_v4_moe_config), [`hash`](moe.md#DeepSeekV4Router.hash), [`Config`](moe.md#DeepSeekV4MoE.Config), [`__init__`](moe.md#DeepSeekV4Router.__init__), [`vocab_size`](moe.md#DeepSeekV4Router.vocab_size), [`layer_id`](moe.md#DeepSeekV4Router.layer_id), [`n_hash_layers`](moe.md#DeepSeekV4Router.n_hash_layers)

## Functions
- <a id="_build_hash_routing_table"></a>`_build_hash_routing_table(vocab_size: int, num_experts: int, top_k: int, device=None, chunk_size: int = 8192)` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/moe.py#L14)

