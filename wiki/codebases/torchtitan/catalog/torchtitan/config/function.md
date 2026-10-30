---
title: 'Module: torchtitan/config/function.py'
type: catalog
provenance: extracted
module: torchtitan/config/function.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.config.function`/
symbols:
  Function: Function#
  Function.Config: Function#Config#
  Function.__init__: Function#__init__().
  Function.__call__: Function#__call__().
  Function.Config.fn: Function#Config#fn.
  R: R.
  Function.fn: Function#fn.
---
# Module: [`torchtitan/config/function.py`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py)

## Classes
### <a id="Function"></a>`Function`  ·  implements/extends Configurable, Generic
- def: [`torchtitan/config/function.py:16`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L16)
- doc: A Configurable wrapper around any callable.
- signature: `class Function(Generic[R], Configurable):`
- members:
  - <a id="Function.fn"></a>`fn` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L37)
- protocol/private: <a id="Function.__call__"></a>`__call__`[`L39`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L39), <a id="Function.__init__"></a>`__init__`[`L36`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L36)
- uses (calls/refs, reference-scoped): [`Configurable`](configurable.md#Configurable), [`Config`](function.md#Function.Config), [`fn`](function.md#Function.Config.fn), [`R`](function.md#R)
- used by: [`Configurable`](configurable.md#Configurable), [`TORCH_DTYPE_MAP`](__init__.md#TORCH_DTYPE_MAP), [`purge_exempt`](../components/checkpointer/base.md#BaseCheckpointManager.Config.purge_exempt)

### <a id="Function.Config"></a>`Function.Config`  ·  implements/extends Config
- def: [`torchtitan/config/function.py:33`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L33)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Function.Config.fn"></a>`fn` — [`L34`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L34)
- uses (calls/refs, reference-scoped): [`Configurable`](configurable.md#Configurable), [`Config`](configurable.md#Configurable.Config), [`R`](function.md#R)
- used by: [`purge_exempt`](../components/checkpointer/base.md#BaseCheckpointManager.Config.purge_exempt), [`__init__`](function.md#Function.__init__)

## Module values
- <a id="R"></a>`R` — [`L13`](../../../../../../raw/code/torchtitan/torchtitan/config/function.py#L13)

