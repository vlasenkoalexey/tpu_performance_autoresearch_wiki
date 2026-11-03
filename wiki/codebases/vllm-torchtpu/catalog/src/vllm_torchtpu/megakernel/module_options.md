---
title: 'Module: src/vllm_torchtpu/megakernel/module_options.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/module_options.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.module_options`/
symbols:
  ModuleOptionsMap: ModuleOptionsMap#
  ModuleOptionsMap.__init__: ModuleOptionsMap#__init__().
  TunablesMap: TunablesMap#
  DebugModulesMap: DebugModulesMap#
  NumericsClass: NumericsClass.
  ModuleOptionsMap._check: ModuleOptionsMap#_check().
  register_tunables: register_tunables().
  tunables_class: tunables_class().
  register_debug: register_debug().
  TunablesMap._check: TunablesMap#_check().
  _TUNABLES._TUNABLES: _TUNABLES._TUNABLES.
  _DEBUG._DEBUG: _DEBUG._DEBUG.
  registered_tunables: registered_tunables().
  debug_class: debug_class().
  registered_debug: registered_debug().
  ModuleOptionsMap.__getitem__: ModuleOptionsMap#__getitem__().
  ModuleOptionsMap.__iter__: ModuleOptionsMap#__iter__().
  ModuleOptionsMap.__len__: ModuleOptionsMap#__len__().
  ModuleOptionsMap.__hash__: ModuleOptionsMap#__hash__().
  ModuleOptionsMap.__eq__: ModuleOptionsMap#__eq__().
  ModuleOptionsMap.__repr__: ModuleOptionsMap#__repr__().
  DebugModulesMap._check: DebugModulesMap#_check().
  ModuleOptionsMap._WHAT: ModuleOptionsMap#_WHAT.
  ModuleOptionsMap._HINT: ModuleOptionsMap#_HINT.
  TunablesMap._HINT: TunablesMap#_HINT.
  ModuleOptionsMap.__slots__: ModuleOptionsMap#__slots__.
  TunablesMap.__slots__: TunablesMap#__slots__.
  TunablesMap._WHAT: TunablesMap#_WHAT.
  DebugModulesMap.__slots__: DebugModulesMap#__slots__.
  DebugModulesMap._WHAT: DebugModulesMap#_WHAT.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/megakernel/module_options.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py)

## Classes
### <a id="DebugModulesMap"></a>`DebugModulesMap`  ·  implements/extends ModuleOptionsMap
- def: [`src/vllm_torchtpu/megakernel/module_options.py:182`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L182)
- doc: `{module name: Debug}` (`DebugOptions.modules`): a `ModuleOptionsMap` whose
- signature: `class DebugModulesMap(ModuleOptionsMap):`
- protocol/private: <a id="DebugModulesMap._WHAT"></a>`_WHAT`[`L188`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L188), <a id="DebugModulesMap.__slots__"></a>`__slots__`[`L187`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L187), <a id="DebugModulesMap._check"></a>`_check`[`L190`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L190)
- uses (calls/refs, reference-scoped): [`ModuleOptionsMap`](module_options.md#ModuleOptionsMap), [`debug_class`](module_options.md#debug_class)
- used by: [`ModuleOptionsMap`](module_options.md#ModuleOptionsMap), [`modules`](exec_spec.md#DebugOptions.modules), [`_check`](module_options.md#ModuleOptionsMap._check), [`__post_init__`](exec_spec.md#DebugOptions.__post_init__)

### <a id="ModuleOptionsMap"></a>`ModuleOptionsMap`  ·  implements/extends Mapping
- def: [`src/vllm_torchtpu/megakernel/module_options.py:106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L106)
- doc: Immutable, hashable `{module name: frozen dataclass}` mapping.
- signature: `class ModuleOptionsMap(Mapping[str, Any]):`
- members:
  - <a id="ModuleOptionsMap._check"></a>`_check(self, name: str, val: Any)` — [`L138`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L138) — Hook: raise if `val` is not a valid entry for `name`.
- protocol/private: <a id="ModuleOptionsMap._HINT"></a>`_HINT`[`L116`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L116), <a id="ModuleOptionsMap._WHAT"></a>`_WHAT`[`L115`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L115), <a id="ModuleOptionsMap.__eq__"></a>`__eq__`[`L155`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L155), <a id="ModuleOptionsMap.__getitem__"></a>`__getitem__`[`L141`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L141), <a id="ModuleOptionsMap.__hash__"></a>`__hash__`[`L150`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L150), <a id="ModuleOptionsMap.__init__"></a>`__init__`[`L118`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L118), <a id="ModuleOptionsMap.__iter__"></a>`__iter__`[`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L144), <a id="ModuleOptionsMap.__len__"></a>`__len__`[`L147`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L147), <a id="ModuleOptionsMap.__repr__"></a>`__repr__`[`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L160), <a id="ModuleOptionsMap.__slots__"></a>`__slots__`[`L113`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L113)
- uses (calls/refs, reference-scoped): [`TunablesMap`](module_options.md#TunablesMap), [`DebugModulesMap`](module_options.md#DebugModulesMap), [`_check`](module_options.md#TunablesMap._check), [`_check`](module_options.md#DebugModulesMap._check)
- used by: [`TunablesMap`](module_options.md#TunablesMap), [`DebugModulesMap`](module_options.md#DebugModulesMap)

### <a id="TunablesMap"></a>`TunablesMap`  ·  implements/extends ModuleOptionsMap
- def: [`src/vllm_torchtpu/megakernel/module_options.py:164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L164)
- doc: `{module name: Tunables}` (`Tiles.modules`): a `ModuleOptionsMap` whose
- signature: `class TunablesMap(ModuleOptionsMap):`
- protocol/private: <a id="TunablesMap._HINT"></a>`_HINT`[`L170`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L170), <a id="TunablesMap._WHAT"></a>`_WHAT`[`L169`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L169), <a id="TunablesMap.__slots__"></a>`__slots__`[`L168`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L168), <a id="TunablesMap._check"></a>`_check`[`L172`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L172)
- uses (calls/refs, reference-scoped): [`ModuleOptionsMap`](module_options.md#ModuleOptionsMap), [`tunables_class`](module_options.md#tunables_class)
- used by: [`ModuleOptionsMap`](module_options.md#ModuleOptionsMap), [`with_modules`](exec_spec.md#Tiles.with_modules), [`modules`](exec_spec.md#Tiles.modules), [`_check`](module_options.md#ModuleOptionsMap._check), [`__post_init__`](exec_spec.md#Tiles.__post_init__)

## Functions
- <a id="debug_class"></a>`debug_class(name: str)` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L91) — The registered `Debug` class of modules named `name`.
- <a id="register_debug"></a>`register_debug(name: str, cls: type)` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L74) — Register `cls` as the `Debug` options class of modules named `name`.
- <a id="register_tunables"></a>`register_tunables(name: str, cls: type)` — [`L30`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L30) — Register `cls` as the `Tunables` of modules named `name`.
- <a id="registered_debug"></a>`registered_debug()` — [`L101`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L101) — All registered `{module name: Debug class}` (a copy).
- <a id="registered_tunables"></a>`registered_tunables()` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L69) — All registered `{module name: Tunables class}` (a copy).
- <a id="tunables_class"></a>`tunables_class(name: str)` — [`L59`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L59) — The registered `Tunables` class of modules named `name`.

## Module values
- <a id="NumericsClass"></a>`NumericsClass` — [`L22`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L22)
- <a id="_DEBUG._DEBUG"></a>`_DEBUG` — [`L27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L27)
- <a id="_TUNABLES._TUNABLES"></a>`_TUNABLES` — [`L25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L25)
- <a id="__all__"></a>`__all__` — [`L199`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/module_options.py#L199)

