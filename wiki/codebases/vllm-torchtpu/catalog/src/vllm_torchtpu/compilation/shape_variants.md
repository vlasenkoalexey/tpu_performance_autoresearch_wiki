---
title: 'Module: src/vllm_torchtpu/compilation/shape_variants.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/compilation/shape_variants.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.compilation.shape_variants`/
symbols:
  defer: defer().
  _session._session: _session._session.
  runnable_for: runnable_for().
  _deferred._deferred: _deferred._deferred.
  _signature: _signature().
  BucketExecutables.get: BucketExecutables#get().
  retrace: retrace().
  trace_only: trace_only().
  _placeholder_runnable: _placeholder_runnable().
  remember: remember().
  unsupported_reason: unsupported_reason().
  aot_cache_tag: aot_cache_tag().
  ShapeSpecializationError: ShapeSpecializationError#
  BucketExecutables.refused: BucketExecutables#refused.
  BucketExecutables.put: BucketExecutables#put().
  warmup: warmup().
  DeferredTraces.compile: DeferredTraces#compile().
  trace_shape_env: trace_shape_env().
  graph_signature: graph_signature().
  logger: logger.
  _placeholder_values: _placeholder_values().
  _placeholder_runnable.concrete: _placeholder_runnable().concrete().
  BucketExecutables.traces: BucketExecutables#traces.
  _deferred_compiler._deferred_compiler: _deferred_compiler._deferred_compiler.
  BucketExecutables.needs_retrace: BucketExecutables#needs_retrace().
  runnable_for.refuse: runnable_for().refuse().
  register_deferred_compiler: register_deferred_compiler().
  deferring: deferring().
  refusing_runnable: refusing_runnable().
  refusing_runnable.refuse: refusing_runnable().refuse().
  _placeholder_runnable.for_size: _placeholder_runnable().for_size().
  _placeholder_runnable.for_size.run: _placeholder_runnable().for_size().run().
  BucketExecutables: BucketExecutables#
  DeferredTraces: DeferredTraces#
  _placeholder_value: _placeholder_value().
  _finite: _finite().
  BucketExecutables._runnables: BucketExecutables#_runnables.
  DeferredTraces.backends: DeferredTraces#backends.
  DeferredTraces.accepted: DeferredTraces#accepted.
  _holds_at: _holds_at().
  _signature.shape: _signature().shape().
  BucketExecutables.__init__: BucketExecutables#__init__().
  DeferredTraces.__init__: DeferredTraces#__init__().
---
# Module: [`src/vllm_torchtpu/compilation/shape_variants.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py)

## Classes
### <a id="BucketExecutables"></a>`BucketExecutables`
- def: [`src/vllm_torchtpu/compilation/shape_variants.py:186`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L186) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- doc: What earlier traces of the model being warmed up already compiled.
- signature: `class BucketExecutables:`
- members:
  - <a id="BucketExecutables.get"></a>`get(self, cache_dir: str | None, key: str, graph: fx.GraphModule)` — [`L203`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L203) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="BucketExecutables.needs_retrace"></a>`needs_retrace(self, size: int)` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L229) — Whether a graph refused this bucket and no trace has built it yet.
  - <a id="BucketExecutables.put"></a>`put(self, cache_dir: str | None, key: str, graph: fx.GraphModule, runnable: Callable[..., Any])` — [`L220`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L220) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="BucketExecutables.refused"></a>`refused` — [`L200`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L200) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="BucketExecutables.traces"></a>`traces` — [`L201`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L201) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- protocol/private: <a id="BucketExecutables.__init__"></a>`__init__`[`L196`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L196), <a id="BucketExecutables._runnables"></a>`_runnables`[`L197`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L197)
- uses (calls/refs, reference-scoped): [`_signature`](shape_variants.md#_signature), [`ShapeSpecializationError`](shape_variants.md#ShapeSpecializationError)
- used by: [`_precompile_backbone`](../runner/tpu_runner.md#TPUModelRunner._precompile_backbone), [`defer`](shape_variants.md#defer), [`_session`](shape_variants.md#_session._session), [`runnable_for`](shape_variants.md#runnable_for), [`retrace`](shape_variants.md#retrace), [`remember`](shape_variants.md#remember), [`aot_cache_tag`](shape_variants.md#aot_cache_tag), [`warmup`](shape_variants.md#warmup)

### <a id="DeferredTraces"></a>`DeferredTraces`
- def: [`src/vllm_torchtpu/compilation/shape_variants.py:372`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L372) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- doc: The piecewise backends traced while their compiles are deferred.
- signature: `class DeferredTraces:`
- members:
  - <a id="DeferredTraces.compile"></a>`compile(self)` — [`L391`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L391) — Compile every deferred bucket (see ``_patch_vllm_compile_all_ranges``). — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="DeferredTraces.accepted"></a>`accepted` — [`L389`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L389) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
  - <a id="DeferredTraces.backends"></a>`backends` — [`L386`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L386) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- protocol/private: <a id="DeferredTraces.__init__"></a>`__init__`[`L385`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L385)
- uses (calls/refs, reference-scoped): [`_deferred_compiler`](shape_variants.md#_deferred_compiler._deferred_compiler)
- used by: [`_precompile_backbone`](../runner/tpu_runner.md#TPUModelRunner._precompile_backbone), [`defer`](shape_variants.md#defer), [`_deferred`](shape_variants.md#_deferred._deferred), [`trace_only`](shape_variants.md#trace_only)

### <a id="ShapeSpecializationError"></a>`ShapeSpecializationError`  ·  implements/extends RuntimeError
- def: [`src/vllm_torchtpu/compilation/shape_variants.py:63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L63) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- doc: A token bucket cannot be served by the graph asked to compile it.
- signature: `class ShapeSpecializationError(RuntimeError):`
- used by: [`_precompile_backbone`](../runner/tpu_runner.md#TPUModelRunner._precompile_backbone), [`runnable_for`](shape_variants.md#runnable_for), [`get`](shape_variants.md#BucketExecutables.get), [`concrete`](shape_variants.md#_placeholder_runnable.concrete), [`refuse`](shape_variants.md#refusing_runnable.refuse), [`refuse`](shape_variants.md#runnable_for.refuse)

## Functions
- <a id="_finite"></a>`_finite(value: Any)` — [`L96`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L96) — A ValueRanges endpoint as an int, or None when it is infinite.
- <a id="_holds_at"></a>`_holds_at(expr: sympy.Expr, substitution: dict)` — [`L106`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L106) — Whether a guard holds under the substitution; None if undecidable.
- <a id="_placeholder_runnable"></a>`_placeholder_runnable(graph: fx.GraphModule, sym_shape_indices: Sequence[int])` — [`L477`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L477) — A stand-in for a deferred bucket: zeros in the traced output's shapes. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_placeholder_value"></a>`_placeholder_value(node: fx.Node)` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L72)
- <a id="_placeholder_values"></a>`_placeholder_values(graph: fx.GraphModule)` — [`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L76)
- <a id="_signature"></a>`_signature(graph: fx.GraphModule)` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L152) — The submodule input list a handed-over runnable has to match. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="aot_cache_tag"></a>`aot_cache_tag()` — [`L307`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L307) — Discriminator for vLLM's AOT artifact path while several traces run. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_placeholder_runnable.concrete"></a>`concrete(dim: Any, substitution: dict)` — [`L498`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L498)
- <a id="defer"></a>`defer(backend: Any)` — [`L428`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L428) — Record a freshly traced piecewise backend instead of compiling it. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="deferring"></a>`deferring()` — [`L423`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L423) — Whether a backend traced now should defer its compiles.
- <a id="_placeholder_runnable.for_size"></a>`for_size(size: int | None)` — [`L509`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L509) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="graph_signature"></a>`graph_signature(graph: fx.GraphModule)` — [`L171`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L171) — :func:`_signature`, for callers outside this module.
- <a id="runnable_for.refuse"></a>`refuse(*_args: Any, **_kwargs: Any)` — [`L290`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L290) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="refusing_runnable.refuse"></a>`refuse(*_args: Any, **_kwargs: Any)` — [`L469`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L469)
- <a id="refusing_runnable"></a>`refusing_runnable(key: str)` — [`L466`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L466) — The runnable of a bucket an earlier, replaced trace refused: never run.
- <a id="register_deferred_compiler"></a>`register_deferred_compiler(fn: Callable[[list[Any]], None])` — [`L405`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L405)
- <a id="remember"></a>`remember(cache_dir: str | None, key: str, graph: fx.GraphModule, runnable: Callable[..., Any])` — [`L299`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L299) — Offer a bucket, freshly compiled or loaded, to the traces that follow. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="retrace"></a>`retrace(model: torch.nn.Module, vllm_config: VllmConfig)` — [`L321`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L321) — Give the model's compiled modules a fresh, untraced torch.compile wrapper. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_placeholder_runnable.for_size.run"></a>`run(*args: Any)` — [`L510`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L510)
- <a id="runnable_for"></a>`runnable_for(cache_dir: str | None, key: str, graph: fx.GraphModule, size: int | None = None)` — [`L256`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L256) — What this compile should use instead of compiling, if anything. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_signature.shape"></a>`shape(value: Any)` — [`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L160)
- <a id="trace_only"></a>`trace_only()` — [`L411`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L411) — Scope in which a traced backend defers its compiles (see DeferredTraces). — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="trace_shape_env"></a>`trace_shape_env(graph: fx.GraphModule)` — [`L87`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L87) — The ShapeEnv of the trace this graph came from, if it has one. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="unsupported_reason"></a>`unsupported_reason(shape_env: Any, size: int)` — [`L117`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L117) — Why a trace cannot serve ``size`` tokens, or None if it can. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="warmup"></a>`warmup()` — [`L245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L245) — Scope in which traces of one model may hand buckets to one another. — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)

## Module values
- <a id="_deferred._deferred"></a>`_deferred` — [`L401`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L401) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_deferred_compiler._deferred_compiler"></a>`_deferred_compiler` — [`L402`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L402) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="_session._session"></a>`_session` — [`L241`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L241) — documented in [compilation-and-graph-capture](../../../../concepts/compilation-and-graph-capture.md)
- <a id="logger"></a>`logger` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/compilation/shape_variants.py#L60)

