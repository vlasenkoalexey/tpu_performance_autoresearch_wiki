---
title: 'Module: torchtitan/components/lora.py'
type: catalog
provenance: extracted
module: torchtitan/components/lora.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.lora`/
symbols:
  LoRALinear.lora_a: LoRALinear#lora_a.
  LoRALinear.lora_b: LoRALinear#lora_b.
  LoRAConverter.convert: LoRAConverter#convert().
  LoRAConverter.target_modules: LoRAConverter#target_modules.
  LoRAConverter._make_lora_config: LoRAConverter#_make_lora_config().
  _get_frozen_config_cls: _get_frozen_config_cls().
  _lora_adapter_sharding: _lora_adapter_sharding().
  LoRALinear._lora_scaling: LoRALinear#_lora_scaling.
  _make_frozen_config: _make_frozen_config().
  LoRAConverter.Config: LoRAConverter#Config#
  _get_lora_cls.LoRALinear.forward: _get_lora_cls().LoRALinear#forward().
  LoRAConverter: LoRAConverter#
  _get_lora_cls: _get_lora_cls().
  LoRAConverter.rank: LoRAConverter#rank.
  LoRAConverter.alpha: LoRAConverter#alpha.
  LoRAConverter.__init__: LoRAConverter#__init__().
  _get_lora_cls.LoRALinear: _get_lora_cls().LoRALinear#
  _get_frozen_config_cls.FrozenConfig: _get_frozen_config_cls().FrozenConfig#
  LoRAConverter.Config.rank: LoRAConverter#Config#rank.
  _get_lora_cls.LoRALinear.Config.rank: _get_lora_cls().LoRALinear#Config#rank.
  LoRAConverter.Config.target_modules: LoRAConverter#Config#target_modules.
  _lora_class_cache._lora_class_cache: _lora_class_cache._lora_class_cache.
  _frozen_config_class_cache._frozen_config_class_cache: _frozen_config_class_cache._frozen_config_class_cache.
  _get_lora_cls.LoRALinear.__init__: _get_lora_cls().LoRALinear#__init__().
  _get_frozen_config_cls.FrozenConfig.build: _get_frozen_config_cls().FrozenConfig#build().
  LoRAConverter.Config.alpha: LoRAConverter#Config#alpha.
  _get_lora_cls.LoRALinear.Config: _get_lora_cls().LoRALinear#Config#
  _get_lora_cls.LoRALinear.Config.alpha: _get_lora_cls().LoRALinear#Config#alpha.
  LoRAConverter.config: LoRAConverter#config.
---
# Module: [`torchtitan/components/lora.py`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py)

## Classes
### <a id="LoRAConverter"></a>`LoRAConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/components/lora.py:141`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L141)
- doc: Apply LoRA adapters to Linear layers in a model.
- signature: `class LoRAConverter(ModelConfigConverter):`
- members:
  - <a id="LoRAConverter._make_lora_config"></a>`_make_lora_config(self, cfg: Linear.Config)` — [`L186`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L186) — Create a LoRALinear.Config from a base Linear.Config.
  - <a id="LoRAConverter.convert"></a>`convert(self, model_config: Module.Config)` — [`L196`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L196) — Walk the module config tree from leaves to root.
  - <a id="LoRAConverter.alpha"></a>`alpha` — [`L171`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L171)
  - <a id="LoRAConverter.config"></a>`config` — [`L169`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L169)
  - <a id="LoRAConverter.rank"></a>`rank` — [`L170`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L170)
  - <a id="LoRAConverter.target_modules"></a>`target_modules` — [`L172`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L172)
- protocol/private: <a id="LoRAConverter.__init__"></a>`__init__`[`L166`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L166)
- uses (calls/refs, reference-scoped): [`logger`](../tools/logging.md#logger), [`Module`](../protocols/module.md#Module), [`Linear`](../models/common/linear.md#Linear), [`Config`](../models/common/linear.md#Linear.Config), [`Config`](../protocols/module.md#Module.Config), [`ModelConfigConverter`](../protocols/model.md#ModelConfigConverter), [`traverse`](../config/configurable.md#Configurable.Config.traverse), [`_owner`](../config/configurable.md#Configurable.Config._owner), [`_make_frozen_config`](lora.md#_make_frozen_config), [`Config`](lora.md#LoRAConverter.Config), [`_get_lora_cls`](lora.md#_get_lora_cls), [`rank`](lora.md#LoRAConverter.Config.rank), [`target_modules`](lora.md#LoRAConverter.Config.target_modules), [`alpha`](lora.md#LoRAConverter.Config.alpha)
- used by: [`ModelConfigConverter`](../protocols/model.md#ModelConfigConverter), [`llama3_debugmodel_float8_emulate_lora`](../models/llama3/config_registry.md#llama3_debugmodel_float8_emulate_lora), [`validate_converter_order`](../models/utils.md#validate_converter_order), [`convert`](../protocols/model.md#ModelConfigConverter.convert)

### <a id="LoRAConverter.Config"></a>`LoRAConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/components/lora.py:155`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L155)
- signature: `class Config(ModelConfigConverter.Config):`
- members:
  - <a id="LoRAConverter.Config.alpha"></a>`alpha` — [`L159`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L159) — ---
  - <a id="LoRAConverter.Config.rank"></a>`rank` — [`L156`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L156) — ---
  - <a id="LoRAConverter.Config.target_modules"></a>`target_modules` — [`L162`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L162) — ---
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../protocols/model.md#ModelConfigConverter), [`Config`](../protocols/model.md#ModelConfigConverter.Config)
- used by: [`llama3_debugmodel_float8_emulate_lora`](../models/llama3/config_registry.md#llama3_debugmodel_float8_emulate_lora), [`validate_converter_order`](../models/utils.md#validate_converter_order), [`target_modules`](lora.md#LoRAConverter.target_modules), [`alpha`](lora.md#LoRAConverter.alpha), [`rank`](lora.md#LoRAConverter.rank), [`__init__`](lora.md#LoRAConverter.__init__)

### <a id="_get_frozen_config_cls.FrozenConfig"></a>`_get_frozen_config_cls.FrozenConfig`  ·  implements/extends Config
- def: [`torchtitan/components/lora.py:122`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L122)
- signature: `class FrozenConfig(config_cls):`
- members:
  - <a id="_get_frozen_config_cls.FrozenConfig.build"></a>`build(self, **kwargs)` — [`L123`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L123)
- uses (calls/refs, reference-scoped): [`build`](../protocols/module.md#Module.Config.build)
- used by: [`_get_frozen_config_cls`](lora.md#_get_frozen_config_cls)

### <a id="_get_lora_cls.LoRALinear"></a>`_get_lora_cls.LoRALinear`
- def: [`torchtitan/components/lora.py:73`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L73)
- signature: `class LoRALinear(parent_cls):`
- members:
  - <a id="_get_lora_cls.LoRALinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L104`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L104)
- protocol/private: <a id="_get_lora_cls.LoRALinear.__init__"></a>`__init__`[`L79`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L79)
- uses (calls/refs, reference-scoped): [`lora_a`](lora.md#LoRALinear.lora_a), [`lora_b`](lora.md#LoRALinear.lora_b), [`_lora_scaling`](lora.md#LoRALinear._lora_scaling), [`Config`](lora.md#_get_lora_cls.LoRALinear.Config)
- used by: [`_get_lora_cls`](lora.md#_get_lora_cls)

### <a id="_get_lora_cls.LoRALinear.Config"></a>`_get_lora_cls.LoRALinear.Config`
- def: [`torchtitan/components/lora.py:75`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L75)
- signature: `class Config(parent_config_cls):`
- members:
  - <a id="_get_lora_cls.LoRALinear.Config.alpha"></a>`alpha` — [`L77`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L77)
  - <a id="_get_lora_cls.LoRALinear.Config.rank"></a>`rank` — [`L76`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L76)
- used by: [`lora_a`](lora.md#LoRALinear.lora_a), [`lora_b`](lora.md#LoRALinear.lora_b), [`_lora_scaling`](lora.md#LoRALinear._lora_scaling), [`__init__`](lora.md#_get_lora_cls.LoRALinear.__init__)

## Functions
- <a id="_get_frozen_config_cls"></a>`_get_frozen_config_cls(config_cls: type[Module.Config])` — [`L115`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L115) — Get or create a config subclass that freezes direct build parameters.
- <a id="_get_lora_cls"></a>`_get_lora_cls(parent_cls: type)` — [`L61`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L61) — Get or create a LoRA subclass for *parent_cls* (e.g. Linear, Float8Linear).
- <a id="_lora_adapter_sharding"></a>`_lora_adapter_sharding(base_sharding: ShardingConfig | None)` — [`L23`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L23) — Derive LoRA adapter sharding from the base linear's TP sharding.
- <a id="_make_frozen_config"></a>`_make_frozen_config(cfg: Module.Config)` — [`L135`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L135) — Create a frozen config that still passes checks for the original type.

## Module values
- <a id="_frozen_config_class_cache._frozen_config_class_cache"></a>`_frozen_config_class_cache` — [`L58`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L58)
- <a id="_lora_class_cache._lora_class_cache"></a>`_lora_class_cache` — [`L57`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L57)

## Other members
- <a id="LoRALinear._lora_scaling"></a>`LoRALinear._lora_scaling` — [`L83`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L83)
- <a id="LoRALinear.lora_a"></a>`LoRALinear.lora_a` — [`L87`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L87)
- <a id="LoRALinear.lora_b"></a>`LoRALinear.lora_b` — [`L96`](../../../../../../raw/code/torchtitan/torchtitan/components/lora.py#L96)

