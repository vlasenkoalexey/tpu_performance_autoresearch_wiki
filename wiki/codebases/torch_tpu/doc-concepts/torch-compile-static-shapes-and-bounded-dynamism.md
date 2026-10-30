---
title: torch.compile(backend="tpu") - the dynamic=False rule and bounded dynamism
type: doc-concept
provenance: doc
source: docs/markdown/advanced_compile.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# torch.compile(backend="tpu") - the dynamic=False rule and bounded dynamism

## Definition
TorchTPU registers a TorchDynamo backend named `"tpu"` that lowers whole FX graphs to StableHLO and compiles them with XLA (`torch.compile(model, backend="tpu", dynamic=False)`). The advanced-compile doc's first rule: **compiled graphs must have static shapes** - always pass `dynamic=False`; `dynamic=True` and `dynamic=None` are described as unsupported. Any input dimension that varies (end-of-epoch batch, variable sequence length) triggers a full recompilation, so pad or slice *outside* the compiled region to keep input shapes constant. The first call is the compile ("1-2 minutes" for the doc's toy model) - the "compilation warming" step.

The intro doc adds the forward-looking half: **bounded dynamism** via `torch._dynamo.mark_dynamic` lets one compiled graph serve varying batch sizes or sequence lengths up to a declared bound without recompiling. It is "required to support SymInts, but not enabled by default yet", which is why `dynamic=False` is currently mandatory.

## In torch_tpu (grounded)
- [`TpuBackend`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend) is the registered `compiler_fn`; [`TpuBackend.__call__`](../catalog/src/torch_tpu/_internal/compile/_backend.md#TpuBackend.__call__) receives the Dynamo graph and example inputs. It raises `NotImplementedError` when `torch._dynamo.config.assume_static_by_default` is off - i.e. for `dynamic=True` specifically. (Code vs doc: the error text suggests `dynamic=None`/default is acceptable; the doc still recommends `dynamic=False`, which also stops Dynamo's automatic-dynamic recompiles from introducing SymInts.)
- [`make_backend_compiler`](../catalog/src/torch_tpu/_internal/compile/_backend.md#make_backend_compiler) branches on [`has_dynamic_symints`](../catalog/src/torch_tpu/_internal/compile/compiler.md#has_dynamic_symints): static graphs go to [`StaticCompiler`](../catalog/src/torch_tpu/_internal/compile/compiler.md#StaticCompiler), graphs with SymInts (from `mark_dynamic`) go to [`DynamicCompiler`](../catalog/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.md#DynamicCompiler); both are wrapped by [`SplitCompiler`](../catalog/src/torch_tpu/_internal/compile/split_compiler.md#SplitCompiler).
- Bounded dynamism in `DynamicCompiler` compiles `bucket_size`-aligned shape buckets. The bounds of each SymInt come from [`SymBoundsManager`](../catalog/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.md#SymBoundsManager); the backend options `num_dynamic_buckets` (1 to [`_MAX_DYNAMIC_BUCKETS`](../catalog/src/torch_tpu/_internal/compile/_backend.md#_MAX_DYNAMIC_BUCKETS) = 8) and `bucket_size` (default 128) are passed via `torch.compile(..., options={...})`. The eager-side counterpart is the bounded-dynamic cache entry with padding adapters ([graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md)).
- Other backend options, from the `__call__` docstring: `async_compile` (compile in the background), `serializable` (AOTAutogradCache save/load; forced off for dynamic graphs), `debug_callback`. [`async_compile`](../catalog/src/torch_tpu/_internal/compile/_backend.md#async_compile) is a helper that wraps `torch.compile(fn, backend="tpu", fullgraph=True, dynamic=False, options={"async_compile": True})`.

## Why it matters / when it applies
- Each distinct input shape is a separate XLA compile; with `dynamic=False` that is the whole cost model - shape churn equals compile churn. Keep shapes fixed or bucketed, and use `drop_last=True` in the DataLoader.
- Bounded dynamism trades a little padding compute for eliminating recompiles; it is the intended route for variable-length inference (vLLM-style) once enabled. Until then, padding to a few fixed buckets by hand gets the same cache behavior.
- Allocate model and inputs directly on device (`with torch.device("tpu"):`) before compiling, as the doc's example does, so the traced graph sees device tensors.
- Whole-graph compile is the doc's recommended config for production serving and peak throughput - it fuses across forward and backward, which fused eager cannot ([eager-execution-modes.md](eager-execution-modes.md)). Graph breaks undo this ([graph-breaks-on-tpu.md](graph-breaks-on-tpu.md)).

## Connections
- Code concepts: [torch-compile-backend](../concepts/torch-compile-backend.md), [dynamic-shapes-compiler](../concepts/dynamic-shapes-compiler.md), [compiled-mode](../concepts/compiled-mode.md), [fx-graph-passes](../concepts/fx-graph-passes.md), [compilation-pipeline](../concepts/compilation-pipeline.md), [dynamic-shape-ops](../concepts/dynamic-shape-ops.md), [compilation-cache](../concepts/compilation-cache.md)
- Module catalogs: [src/torch_tpu/_internal/compile/_backend](../catalog/src/torch_tpu/_internal/compile/_backend.md), [src/torch_tpu/_internal/compile/compiler](../catalog/src/torch_tpu/_internal/compile/compiler.md), [src/torch_tpu/_internal/compile/split_compiler](../catalog/src/torch_tpu/_internal/compile/split_compiler.md), [src/torch_tpu/_internal/compile/dynamic/dynamic_compiler](../catalog/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.md), [src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager](../catalog/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.md)
- Related doc-concepts: [graph-breaks-on-tpu.md](graph-breaks-on-tpu.md), [single-trace-trainer.md](single-trace-trainer.md), [graph-fingerprint-and-recompilation.md](graph-fingerprint-and-recompilation.md), [multi-tier-compilation-cache.md](multi-tier-compilation-cache.md), [xla-lowering-stablehlo-hlo-llo.md](xla-lowering-stablehlo-hlo-llo.md)

## Source
Extracted from `docs/markdown/advanced_compile.md` (section 1) and the "Graph compilation with torch.compile" bullet of `docs/markdown/intro_to_torchtpu.md` (= `docs/markdown/1_basics_1_intro_to_torchtpu.md`) (kept in place).
