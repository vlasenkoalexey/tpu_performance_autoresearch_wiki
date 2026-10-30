---
title: 'Module: src/torch_tpu/_versioned_so_loader.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_versioned_so_loader.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._versioned_so_loader`/
symbols:
  install_hook: install_hook().
  VersionDispatchFinder.find_spec: VersionDispatchFinder#find_spec().
  torch_version_suffix: torch_version_suffix().
  ExtensionProxyLoader._real_loader: ExtensionProxyLoader#_real_loader.
  ExtensionProxyLoader.create_module: ExtensionProxyLoader#create_module().
  _VERSION_SUFFIX._VERSION_SUFFIX: _VERSION_SUFFIX._VERSION_SUFFIX.
  _parse: _parse().
  version_suffix: version_suffix().
  discover_built_suffixes: discover_built_suffixes().
  resolve_suffix: resolve_suffix().
  ExtensionProxyLoader.exec_module: ExtensionProxyLoader#exec_module().
  ExtensionProxyLoader.__getattr__: ExtensionProxyLoader#__getattr__().
  VersionDispatchFinder: VersionDispatchFinder#
  installed_torch_version: installed_torch_version().
  _RELEASE_TRIPLE: _RELEASE_TRIPLE.
  _glue_suffix: _glue_suffix().
  ExtensionProxyLoader: ExtensionProxyLoader#
  ExtensionProxyLoader._unversioned_name: ExtensionProxyLoader#_unversioned_name.
  _INTERNAL_PREFIX._INTERNAL_PREFIX: _INTERNAL_PREFIX._INTERNAL_PREFIX.
  ExtensionProxyLoader.__init__: ExtensionProxyLoader#__init__().
  ExtensionProxyLoader._versioned_name: ExtensionProxyLoader#_versioned_name.
---
# Module: [`src/torch_tpu/_versioned_so_loader.py`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py)

## Classes
### <a id="ExtensionProxyLoader"></a>`ExtensionProxyLoader`  ·  implements/extends Loader
- def: [`src/torch_tpu/_versioned_so_loader.py:193`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L193)
- doc: Loads a version-suffixed glue under its unversioned module name.
- signature: `class ExtensionProxyLoader(importlib.abc.Loader):`
- members:
  - <a id="ExtensionProxyLoader.create_module"></a>`create_module(self, spec)` — [`L207`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L207)
  - <a id="ExtensionProxyLoader.exec_module"></a>`exec_module(self, module)` — [`L219`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L219)
- protocol/private: <a id="ExtensionProxyLoader.__getattr__"></a>`__getattr__`[`L223`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L223), <a id="ExtensionProxyLoader.__init__"></a>`__init__`[`L202`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L202), <a id="ExtensionProxyLoader._real_loader"></a>`_real_loader`[`L203`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L203), <a id="ExtensionProxyLoader._unversioned_name"></a>`_unversioned_name`[`L204`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L204), <a id="ExtensionProxyLoader._versioned_name"></a>`_versioned_name`[`L205`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L205)
- used by: [`find_spec`](_versioned_so_loader.md#VersionDispatchFinder.find_spec)

### <a id="VersionDispatchFinder"></a>`VersionDispatchFinder`  ·  implements/extends MetaPathFinder
- def: [`src/torch_tpu/_versioned_so_loader.py:227`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L227)
- doc: Redirects `torch_tpu._internal.<m>` imports to the resolved glue.
- signature: `class VersionDispatchFinder(importlib.abc.MetaPathFinder):`
- members:
  - <a id="VersionDispatchFinder.find_spec"></a>`find_spec(self, fullname, path, target=None)` — [`L230`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L230) — Redirects a `torch_tpu._internal` import to its versioned artifact.
- uses (calls/refs, reference-scoped): [`_VERSION_SUFFIX`](_versioned_so_loader.md#_VERSION_SUFFIX._VERSION_SUFFIX), [`ExtensionProxyLoader`](_versioned_so_loader.md#ExtensionProxyLoader), [`_INTERNAL_PREFIX`](_versioned_so_loader.md#_INTERNAL_PREFIX._INTERNAL_PREFIX)
- used by: [`install_hook`](_versioned_so_loader.md#install_hook)

## Functions
- <a id="_glue_suffix"></a>`_glue_suffix(so_name: str)` — [`L116`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L116) — Extracts the version suffix of a versioned glue filename.
- <a id="_parse"></a>`_parse(suffix: str)` — [`L60`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L60)
- <a id="discover_built_suffixes"></a>`discover_built_suffixes(package_dir: pathlib.Path)` — [`L135`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L135) — Returns the set of glue suffixes bundled under `package_dir`.
- <a id="install_hook"></a>`install_hook(package_dir: pathlib.Path)` — [`L274`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L274) — Selects the matching glue variant and installs the import hook.
- <a id="installed_torch_version"></a>`installed_torch_version()` — [`L64`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L64) — Returns the installed torch's full version string, or None.
- <a id="resolve_suffix"></a>`resolve_suffix(running: str | None, built: Collection[str])` — [`L146`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L146) — Chooses the glue suffix to load, or None to disable dispatch.
- <a id="torch_version_suffix"></a>`torch_version_suffix()` — [`L108`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L108) — Returns the installed torch's "<major>_<minor>_<patch>", or None.
- <a id="version_suffix"></a>`version_suffix(version: str)` — [`L100`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L100) — Turns a torch version into a glue suffix ("2.13.0+cpu" -> "2_13_0").

## Module values
- <a id="_INTERNAL_PREFIX._INTERNAL_PREFIX"></a>`_INTERNAL_PREFIX` — [`L53`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L53)
- <a id="_RELEASE_TRIPLE"></a>`_RELEASE_TRIPLE` — [`L88`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L88)
- <a id="_VERSION_SUFFIX._VERSION_SUFFIX"></a>`_VERSION_SUFFIX` — [`L57`](../../../../../../raw/code/torch_tpu/src/torch_tpu/_versioned_so_loader.py#L57)

