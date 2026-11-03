---
title: 'Module: src/vllm_torchtpu/compilation/kernel_reload.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/compilation/kernel_reload.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.compilation.kernel_reload`/
symbols:
  reload_kernels: reload_kernels().
  default_reload_modules: default_reload_modules().
  _KernelDispatch.__call__: _KernelDispatch#__call__().
  logger: logger.
  _LIVE._LIVE: _LIVE._LIVE.
  _KernelDispatch._name: _KernelDispatch#_name.
  make_dispatcher: make_dispatcher().
  set_live: set_live().
  register_builder: register_builder().
  is_enabled: is_enabled().
  get_live: get_live().
  _KernelDispatch: _KernelDispatch#
  _BUILDERS._BUILDERS: _BUILDERS._BUILDERS.
  _DEFAULT_RELOAD_MODULES: _DEFAULT_RELOAD_MODULES.
  _KernelDispatch._COPY_ATTRS: _KernelDispatch#_COPY_ATTRS.
  _KernelDispatch.__init__: _KernelDispatch#__init__().
  _KernelDispatch.__wrapped__: _KernelDispatch#__wrapped__.
---
# Module: [`src/vllm_torchtpu/compilation/kernel_reload.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py)

## Classes
### <a id="_KernelDispatch"></a>`_KernelDispatch`
- def: [`src/vllm_torchtpu/compilation/kernel_reload.py:81`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L81)
- doc: Per-call indirection so the registered torch op survives reloads.
- signature: `class _KernelDispatch:`
- protocol/private: <a id="_KernelDispatch._COPY_ATTRS"></a>`_COPY_ATTRS`[`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L91), <a id="_KernelDispatch.__call__"></a>`__call__`[`L113`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L113), <a id="_KernelDispatch.__init__"></a>`__init__`[`L103`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L103), <a id="_KernelDispatch.__wrapped__"></a>`__wrapped__`[`L111`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L111), <a id="_KernelDispatch._name"></a>`_name`[`L104`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L104)
- uses (calls/refs, reference-scoped): [`_LIVE`](kernel_reload.md#_LIVE._LIVE)
- used by: [`make_dispatcher`](kernel_reload.md#make_dispatcher)

## Functions
- <a id="default_reload_modules"></a>`default_reload_modules()` — [`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L74) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="get_live"></a>`get_live(name: str)` — [`L126`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L126)
- <a id="is_enabled"></a>`is_enabled()` — [`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L70)
- <a id="make_dispatcher"></a>`make_dispatcher(name: str, template: Callable)` — [`L117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L117)
- <a id="register_builder"></a>`register_builder(name: str, builder: Callable[[], Callable])` — [`L130`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L130) — Register the rebuild recipe for op ``name``.
- <a id="reload_kernels"></a>`reload_kernels(modules: Sequence[str] | None = None)` — [`L139`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L139) — Re-import kernel sources and swap every registered op. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="set_live"></a>`set_live(name: str, callable_: Callable)` — [`L121`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L121) — Set the current dispatch target for op ``name``.

## Module values
- <a id="_BUILDERS._BUILDERS"></a>`_BUILDERS` — [`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L67) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_DEFAULT_RELOAD_MODULES"></a>`_DEFAULT_RELOAD_MODULES` — [`L52`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L52)
- <a id="_LIVE._LIVE"></a>`_LIVE` — [`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L65) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="logger"></a>`logger` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/kernel_reload.py#L46)

