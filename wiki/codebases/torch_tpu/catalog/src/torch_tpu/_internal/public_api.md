---
title: 'Module: src/torch_tpu/_internal/public_api.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/public_api.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.public_api`/
symbols:
  _PUBLIC_MODULES._PUBLIC_MODULES: _PUBLIC_MODULES._PUBLIC_MODULES.
  _tpu_attr: _tpu_attr().
  _PublicApiModule.__getattr__: _PublicApiModule#__getattr__().
  _PublicApiLoader.create_module: _PublicApiLoader#create_module().
  install: install().
  ModuleSpec: ModuleSpec#
  ModuleSpec.exports: ModuleSpec#exports.
  _PublicApiFinder.find_spec: _PublicApiFinder#find_spec().
  _PublicApiModule._get_stages_map: _PublicApiModule#_get_stages_map().
  _PublicApiLoader._module_name: _PublicApiLoader#_module_name.
  ModuleSpec.doc: ModuleSpec#doc.
  _ExecutablePublicApiLoader._find_target_loader: _ExecutablePublicApiLoader#_find_target_loader().
  _PublicApiLoader: _PublicApiLoader#
  _ExecutablePublicApiLoader.get_filename: _ExecutablePublicApiLoader#get_filename().
  _PublicApiModule._all_names: _PublicApiModule#_all_names.
  _ExecutablePublicApiLoader._target_module: _ExecutablePublicApiLoader#_target_module.
  _FINDER._FINDER: _FINDER._FINDER.
  Property: Property#
  _PublicApiLoader.is_package: _PublicApiLoader#is_package().
  _PublicApiFinder.register: _PublicApiFinder#register().
  ModuleSpec.stages: ModuleSpec#stages.
  _PublicApiModule.__init__: _PublicApiModule#__init__().
  _PublicApiModule._spec: _PublicApiModule#_spec.
  _PublicApiLoader.exec_module: _PublicApiLoader#exec_module().
  _ExecutablePublicApiLoader.__init__: _ExecutablePublicApiLoader#__init__().
  _ExecutablePublicApiLoader.get_source: _ExecutablePublicApiLoader#get_source().
  _ExecutablePublicApiLoader.get_code: _ExecutablePublicApiLoader#get_code().
  _ExecutablePublicApiLoader: _ExecutablePublicApiLoader#
  _TPU_DEVICE_CLASS._TPU_DEVICE_CLASS: _TPU_DEVICE_CLASS._TPU_DEVICE_CLASS.
  _DISTRIBUTED_PROPERTIES_CLASS._DISTRIBUTED_PROPERTIES_CLASS: _DISTRIBUTED_PROPERTIES_CLASS._DISTRIBUTED_PROPERTIES_CLASS.
  _import_target: _import_target().
  _PublicApiModule: _PublicApiModule#
  _DEVICE_MODULE._DEVICE_MODULE: _DEVICE_MODULE._DEVICE_MODULE.
  _PublicApiLoader.__init__: _PublicApiLoader#__init__().
  Export.Export: Export.Export.
  ModuleSpec.main: ModuleSpec#main.
  _PublicApiModule.__all__: _PublicApiModule#__all__.
  _PublicApiModule.__dir__: _PublicApiModule#__dir__().
  _PublicApiFinder.__init__: _PublicApiFinder#__init__().
  Property.target: Property#target.
  ModuleSpec.private_fallback: ModuleSpec#private_fallback.
  _PublicApiModule._module_name: _PublicApiModule#_module_name.
  _PublicApiModule._child_names: _PublicApiModule#_child_names.
  _PublicApiLoader._spec: _PublicApiLoader#_spec.
  _PublicApiLoader._child_names: _PublicApiLoader#_child_names.
  _PublicApiFinder: _PublicApiFinder#
  _PublicApiFinder._loaders: _PublicApiFinder#_loaders.
  _DISTRIBUTED_MODULE._DISTRIBUTED_MODULE: _DISTRIBUTED_MODULE._DISTRIBUTED_MODULE.
  _PublicApiModule._attr_exports: _PublicApiModule#_attr_exports.
  _PublicApiLoader._is_package: _PublicApiLoader#_is_package.
---
# Module: [`src/torch_tpu/_internal/public_api.py`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py)

## Classes
### <a id="ModuleSpec"></a>`ModuleSpec`
- def: [`src/torch_tpu/_internal/public_api.py:55`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L55)
- doc: Specification of a public module.
- signature: `class ModuleSpec:`
- members:
  - <a id="ModuleSpec.doc"></a>`doc` — [`L74`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L74)
  - <a id="ModuleSpec.exports"></a>`exports` — [`L70`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L70)
  - <a id="ModuleSpec.main"></a>`main` — [`L73`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L73)
  - <a id="ModuleSpec.private_fallback"></a>`private_fallback` — [`L71`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L71)
  - <a id="ModuleSpec.stages"></a>`stages` — [`L72`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L72)
- uses (calls/refs, reference-scoped): [`Export`](public_api.md#Export.Export)
- used by: [`_PUBLIC_MODULES`](public_api.md#_PUBLIC_MODULES._PUBLIC_MODULES), [`__getattr__`](public_api.md#_PublicApiModule.__getattr__), [`create_module`](public_api.md#_PublicApiLoader.create_module), [`install`](public_api.md#install), [`_get_stages_map`](public_api.md#_PublicApiModule._get_stages_map), [`_all_names`](public_api.md#_PublicApiModule._all_names), [`__init__`](public_api.md#_ExecutablePublicApiLoader.__init__), [`__init__`](public_api.md#_PublicApiModule.__init__), [`__init__`](public_api.md#_PublicApiLoader.__init__)

### <a id="Property"></a>`Property`
- def: [`src/torch_tpu/_internal/public_api.py:39`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L39)
- doc: A property descriptor installed on the public module's type.
- signature: `class Property:`
- members:
  - <a id="Property.target"></a>`target` — [`L48`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L48)
- used by: [`_PUBLIC_MODULES`](public_api.md#_PUBLIC_MODULES._PUBLIC_MODULES), [`create_module`](public_api.md#_PublicApiLoader.create_module), [`Export`](public_api.md#Export.Export)

### <a id="_ExecutablePublicApiLoader"></a>`_ExecutablePublicApiLoader`  ·  implements/extends ExecutionLoader, _PublicApiLoader
- def: [`src/torch_tpu/_internal/public_api.py:454`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L454)
- doc: Loader that also delegates `python -m` execution to an internal module.
- signature: `class _ExecutablePublicApiLoader(_PublicApiLoader, importlib.abc.ExecutionLoader):`
- members:
  - <a id="_ExecutablePublicApiLoader.get_code"></a>`get_code(self, fullname: str)` — [`L499`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L499)
  - <a id="_ExecutablePublicApiLoader.get_filename"></a>`get_filename(self, fullname: str)` — [`L480`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L480)
  - <a id="_ExecutablePublicApiLoader.get_source"></a>`get_source(self, fullname: str)` — [`L492`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L492)
- protocol/private: <a id="_ExecutablePublicApiLoader.__init__"></a>`__init__`[`L459`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L459), <a id="_ExecutablePublicApiLoader._find_target_loader"></a>`_find_target_loader`[`L470`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L470), <a id="_ExecutablePublicApiLoader._target_module"></a>`_target_module`[`L468`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L468)
- uses (calls/refs, reference-scoped): [`ModuleSpec`](public_api.md#ModuleSpec), [`_module_name`](public_api.md#_PublicApiLoader._module_name), [`_PublicApiLoader`](public_api.md#_PublicApiLoader), [`__init__`](public_api.md#_PublicApiLoader.__init__)
- used by: [`install`](public_api.md#install), [`find_spec`](public_api.md#_PublicApiFinder.find_spec), [`_PublicApiLoader`](public_api.md#_PublicApiLoader)

### <a id="_PublicApiFinder"></a>`_PublicApiFinder`  ·  implements/extends MetaPathFinder
- def: [`src/torch_tpu/_internal/public_api.py:507`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L507)
- doc: MetaPathFinder serving virtual public modules registered via `install()`.
- signature: `class _PublicApiFinder(importlib.abc.MetaPathFinder):`
- members:
  - <a id="_PublicApiFinder.find_spec"></a>`find_spec(self, fullname: str, path: Sequence[str] | None = None, target: types.ModuleType | None = None)` — [`L516`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L516)
  - <a id="_PublicApiFinder.register"></a>`register(self, loaders: Mapping[str, _PublicApiLoader])` — [`L513`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L513)
- protocol/private: <a id="_PublicApiFinder.__init__"></a>`__init__`[`L510`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L510), <a id="_PublicApiFinder._loaders"></a>`_loaders`[`L511`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L511)
- uses (calls/refs, reference-scoped): [`_PublicApiLoader`](public_api.md#_PublicApiLoader), [`_target_module`](public_api.md#_ExecutablePublicApiLoader._target_module), [`is_package`](public_api.md#_PublicApiLoader.is_package), [`_ExecutablePublicApiLoader`](public_api.md#_ExecutablePublicApiLoader)
- used by: [`install`](public_api.md#install), [`_FINDER`](public_api.md#_FINDER._FINDER)

### <a id="_PublicApiLoader"></a>`_PublicApiLoader`  ·  implements/extends Loader
- def: [`src/torch_tpu/_internal/public_api.py:386`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L386)
- doc: Loader that creates and configures a `_PublicApiModule` from a `ModuleSpec`.
- signature: `class _PublicApiLoader(importlib.abc.Loader):`
- members:
  - <a id="_PublicApiLoader.create_module"></a>`create_module(self, spec: importlib.machinery.ModuleSpec)` — [`L409`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L409)
  - <a id="_PublicApiLoader.exec_module"></a>`exec_module(self, module: types.ModuleType)` — [`L446`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L446)
  - <a id="_PublicApiLoader.is_package"></a>`is_package(self, fullname: str)` — [`L401`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L401)
- protocol/private: <a id="_PublicApiLoader.__init__"></a>`__init__`[`L389`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L389), <a id="_PublicApiLoader._child_names"></a>`_child_names`[`L398`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L398), <a id="_PublicApiLoader._is_package"></a>`_is_package`[`L399`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L399), <a id="_PublicApiLoader._module_name"></a>`_module_name`[`L396`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L396), <a id="_PublicApiLoader._spec"></a>`_spec`[`L397`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L397)
- uses (calls/refs, reference-scoped): [`ModuleSpec`](public_api.md#ModuleSpec), [`exports`](public_api.md#ModuleSpec.exports), [`Property`](public_api.md#Property), [`_ExecutablePublicApiLoader`](public_api.md#_ExecutablePublicApiLoader), [`_PublicApiModule`](public_api.md#_PublicApiModule), [`_import_target`](public_api.md#_import_target), [`target`](public_api.md#Property.target)
- used by: [`install`](public_api.md#install), [`find_spec`](public_api.md#_PublicApiFinder.find_spec), [`_find_target_loader`](public_api.md#_ExecutablePublicApiLoader._find_target_loader), [`get_filename`](public_api.md#_ExecutablePublicApiLoader.get_filename), [`register`](public_api.md#_PublicApiFinder.register), [`__init__`](public_api.md#_ExecutablePublicApiLoader.__init__), [`_ExecutablePublicApiLoader`](public_api.md#_ExecutablePublicApiLoader), [`__init__`](public_api.md#_PublicApiFinder.__init__)

### <a id="_PublicApiModule"></a>`_PublicApiModule`  ·  implements/extends ModuleType
- def: [`src/torch_tpu/_internal/public_api.py:320`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L320)
- doc: Lazy `torch.tpu` module backed by a `ModuleSpec`.
- signature: `class _PublicApiModule(types.ModuleType):`
- members:
  - <a id="_PublicApiModule._get_stages_map"></a>`_get_stages_map(self)` — [`L340`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L340) — Lazily builds and caches `__tt_api_stages__` on this module.
- protocol/private: <a id="_PublicApiModule.__all__"></a>`__all__`[`L338`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L338), <a id="_PublicApiModule.__dir__"></a>`__dir__`[`L382`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L382), <a id="_PublicApiModule.__getattr__"></a>`__getattr__`[`L350`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L350), <a id="_PublicApiModule.__init__"></a>`__init__`[`L323`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L323), <a id="_PublicApiModule._all_names"></a>`_all_names`[`L335`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L335), <a id="_PublicApiModule._attr_exports"></a>`_attr_exports`[`L334`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L334), <a id="_PublicApiModule._child_names"></a>`_child_names`[`L333`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L333), <a id="_PublicApiModule._module_name"></a>`_module_name`[`L331`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L331), <a id="_PublicApiModule._spec"></a>`_spec`[`L332`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L332)
- uses (calls/refs, reference-scoped): [`ModuleSpec`](public_api.md#ModuleSpec), [`exports`](public_api.md#ModuleSpec.exports), [`doc`](public_api.md#ModuleSpec.doc), [`stages`](public_api.md#ModuleSpec.stages), [`_import_target`](public_api.md#_import_target), [`private_fallback`](public_api.md#ModuleSpec.private_fallback)
- used by: [`create_module`](public_api.md#_PublicApiLoader.create_module)

## Functions
- <a id="_import_target"></a>`_import_target(target: str)` — [`L311`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L311) — Imports and resolves a `pkg.mod:Qual.name` target.
- <a id="_tpu_attr"></a>`_tpu_attr(name: str)` — [`L87`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L87)
- <a id="install"></a>`install(table: Mapping[str, ModuleSpec] = _PUBLIC_MODULES)` — [`L545`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L545) — Registers and initializes the public modules defined in `table`.

## Module values
- <a id="Export.Export"></a>`Export` — [`L51`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L51)
- <a id="_DEVICE_MODULE._DEVICE_MODULE"></a>`_DEVICE_MODULE` — [`L77`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L77)
- <a id="_DISTRIBUTED_MODULE._DISTRIBUTED_MODULE"></a>`_DISTRIBUTED_MODULE` — [`L79`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L79)
- <a id="_DISTRIBUTED_PROPERTIES_CLASS._DISTRIBUTED_PROPERTIES_CLASS"></a>`_DISTRIBUTED_PROPERTIES_CLASS` — [`L82`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L82)
- <a id="_FINDER._FINDER"></a>`_FINDER` — [`L542`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L542)
- <a id="_PUBLIC_MODULES._PUBLIC_MODULES"></a>`_PUBLIC_MODULES` — [`L130`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L130)
- <a id="_TPU_DEVICE_CLASS._TPU_DEVICE_CLASS"></a>`_TPU_DEVICE_CLASS` — [`L78`](../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/public_api.py#L78)

