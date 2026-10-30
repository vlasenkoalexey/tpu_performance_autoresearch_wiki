---
title: 'Module: torchtitan/experiments/rl/models/cast_linear.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/cast_linear.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.cast_linear`/
symbols:
  LMHeadCastConverter.convert: LMHeadCastConverter#convert().
  LMHeadCastConverter: LMHeadCastConverter#
  LMHeadCastConverter.Config: LMHeadCastConverter#Config#
  CastLinear.Config: CastLinear#Config#
  CastLinear: CastLinear#
  CastLinear.compute_dtype: CastLinear#compute_dtype.
  CastLinear.__init__: CastLinear#__init__().
  LMHeadCastConverter._TARGET: LMHeadCastConverter#_TARGET.
  CastLinear.forward: CastLinear#forward().
  LMHeadCastConverter.__init__: LMHeadCastConverter#__init__().
  CastLinear.Config.compute_dtype: CastLinear#Config#compute_dtype.
  LMHeadCastConverter.Config.compute_dtype: LMHeadCastConverter#Config#compute_dtype.
  LMHeadCastConverter.config: LMHeadCastConverter#config.
---
# Module: [`torchtitan/experiments/rl/models/cast_linear.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py)

## Classes
### <a id="CastLinear"></a>`CastLinear`  ·  implements/extends Linear
- def: [`torchtitan/experiments/rl/models/cast_linear.py:33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L33)
- doc: `Linear` whose forward matmul runs in `compute_dtype`.
- signature: `class CastLinear(Linear):`
- members:
  - <a id="CastLinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L52)
  - <a id="CastLinear.compute_dtype"></a>`compute_dtype` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L50)
- protocol/private: <a id="CastLinear.__init__"></a>`__init__`[`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L48)
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`TORCH_DTYPE_MAP`](../../../config/__init__.md#TORCH_DTYPE_MAP), [`__init__`](../../../models/common/linear.md#Linear.__init__), [`Config`](cast_linear.md#CastLinear.Config), [`compute_dtype`](cast_linear.md#CastLinear.Config.compute_dtype)
- used by: [`Linear`](../../../models/common/linear.md#Linear), [`convert`](cast_linear.md#LMHeadCastConverter.convert)  (4 test-only)

### <a id="CastLinear.Config"></a>`CastLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/models/cast_linear.py:44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L44)
- signature: `class Config(Linear.Config):`
- members:
  - <a id="CastLinear.Config.compute_dtype"></a>`compute_dtype` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L45) — ---
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`Config`](../../../models/common/linear.md#Linear.Config)
- used by: [`convert`](cast_linear.md#LMHeadCastConverter.convert), [`compute_dtype`](cast_linear.md#CastLinear.compute_dtype), [`__init__`](cast_linear.md#CastLinear.__init__)  (4 test-only)

### <a id="LMHeadCastConverter"></a>`LMHeadCastConverter`  ·  implements/extends ModelConfigConverter
- def: [`torchtitan/experiments/rl/models/cast_linear.py:63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L63)
- doc: Swap the decoder lm_head's `Linear.Config` to `CastLinear.Config`.
- signature: `class LMHeadCastConverter(ModelConfigConverter):`
- members:
  - <a id="LMHeadCastConverter.convert"></a>`convert(self, model_config)` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L92)
  - <a id="LMHeadCastConverter.config"></a>`config` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L90)
- protocol/private: <a id="LMHeadCastConverter._TARGET"></a>`_TARGET`[`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L82), <a id="LMHeadCastConverter.__init__"></a>`__init__`[`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L89)
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`Config`](../../../models/common/linear.md#Linear.Config), [`ModelConfigConverter`](../../../protocols/model.md#ModelConfigConverter), [`traverse`](../../../config/configurable.md#Configurable.Config.traverse), [`Config`](cast_linear.md#LMHeadCastConverter.Config), [`Config`](cast_linear.md#CastLinear.Config), [`CastLinear`](cast_linear.md#CastLinear), [`compute_dtype`](cast_linear.md#CastLinear.Config.compute_dtype), [`compute_dtype`](cast_linear.md#LMHeadCastConverter.Config.compute_dtype)
- used by: [`ModelConfigConverter`](../../../protocols/model.md#ModelConfigConverter), [`convert`](../../../protocols/model.md#ModelConfigConverter.convert)  (9 test-only)

### <a id="LMHeadCastConverter.Config"></a>`LMHeadCastConverter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/models/cast_linear.py:85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L85)
- signature: `class Config(ModelConfigConverter.Config):`
- members:
  - <a id="LMHeadCastConverter.Config.compute_dtype"></a>`compute_dtype` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/cast_linear.py#L86) — ---
- uses (calls/refs, reference-scoped): [`ModelConfigConverter`](../../../protocols/model.md#ModelConfigConverter), [`Config`](../../../protocols/model.md#ModelConfigConverter.Config)
- used by: [`convert`](cast_linear.md#LMHeadCastConverter.convert), [`__init__`](cast_linear.md#LMHeadCastConverter.__init__)  (9 test-only)

