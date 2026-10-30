---
title: Public API paths and the torch.tpu module structure
type: doc-concept
provenance: doc
source: docs/developers/api_design_guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# Public API paths and the torch.tpu module structure

## Definition
TorchTPU wants to read as part of PyTorch, so every public Python API lives under `torch.tpu.*` (like `torch.cuda`). The `torch_tpu` package itself and `torch.backends.tpu` expose nothing public. A **public path** is any dotted name with no `_`-prefixed component that reaches a TorchTPU object, and every such path is an API that needs owner approval. Each object gets **at most one** non-deprecated public module-level path. The guide notes this is stricter than PyTorch and closer to JAX's `jax._src` layout.

## In torch_tpu (grounded)
- The public tree is generated, not hand-written: [`public_api`](../catalog/src/torch_tpu/_internal/public_api.md) holds a declarative table of [`ModuleSpec`](../catalog/src/torch_tpu/_internal/public_api.md#ModuleSpec) entries (exports, optional [`Property`](../catalog/src/torch_tpu/_internal/public_api.md#Property) descriptors for settable globals, a `__tt_api_stages__` map). [`install`](../catalog/src/torch_tpu/_internal/public_api.md#install) runs at import from the loader and registers the modules in `sys.modules`. Attributes resolve lazily (PEP 562) from `torch_tpu._internal`, so `import torch` stays fast and internal imports never leak onto public names.
- The documented layout is `torch.tpu` plus `compiler`, `distributed`, `exceptions`, `ops`, `optimizers`, `pallas` and `profiler`. In v0.2.0 the table defines `torch.tpu` and the `compiler`, `distributed`, `ops`, `optimizers`, `pallas` and `profiler` submodules.
- **Custom ops all live in `torch.tpu.ops`**, whether C++ or Python. C++ ops must be registered under `torch.ops.tpu`, so they are registered with a leading underscore (`torch.ops.tpu._foo`) to keep that path internal, and the public name is served from `torch.tpu.ops`. The guide shows a direct alias (`foo = torch.ops.tpu._foo`). In v0.2.0 the table instead points at thin Python wrappers, e.g. [`optimization_barrier`](../catalog/src/torch_tpu/_internal/ops/ops.md#optimization_barrier) calls `torch.ops.tpu._optimization_barrier`, and [`align_jagged_to_multiple`](../catalog/src/torch_tpu/_internal/ops/jagged.md#align_jagged_to_multiple) is a pure-Python op exported the same way.
- **Instance attributes of public classes must be `_`-prefixed.** The API scanner cannot see `self.lr`, so state is exposed through properties (read-only when there is no setter). `tests/api/tt_apis_test.py` enforces this. Dataclass fields are exempt.

## Why it matters / when it applies
- For perf work this tells you **where to look for a TorchTPU knob or op**: `torch.tpu` (device, streams, `eager_mode`, `allow_excess_precision`, `synchronize`), `torch.tpu.compiler` (compiler options), `torch.tpu.ops` (ragged dot, collectives with dims, optimization barrier, pooling), `torch.tpu.optimizers` (fused optimizers), `torch.tpu.pallas` (custom kernels), `torch.tpu.profiler`. Anything only reachable via `torch_tpu._internal` or `torch.ops.tpu._*` is internal and may change without notice.
- When writing model code against an experiment fork, import through the public path. That keeps the code working when an op moves between C++ and Python, which the single-path rule exists to allow.
- Adding a public module, path or rename needs API-owner approval, and the regenerated `tests/api/tt_apis.yaml` must match.

## Connections
- Code concepts: [python-ops](../concepts/python-ops.md), [ragged-collectives-and-sparse-ops](../concepts/ragged-collectives-and-sparse-ops.md), [python-optimizers](../concepts/python-optimizers.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [profiler](../concepts/profiler.md), [aten-kernel-authoring](../concepts/aten-kernel-authoring.md)
- Module catalogs: [src/torch_tpu/_internal/public_api](../catalog/src/torch_tpu/_internal/public_api.md), [src/torch_tpu/_internal/ops/ops](../catalog/src/torch_tpu/_internal/ops/ops.md), [src/torch_tpu/_internal/ops/jagged](../catalog/src/torch_tpu/_internal/ops/jagged.md)
- Related doc-concepts: [api-lifecycle-stages](api-lifecycle-stages.md), [global-and-local-knobs](global-and-local-knobs.md), [tpu-device-backend-initialization](tpu-device-backend-initialization.md)

## Source
Extracted from `docs/developers/api_design_guide.md` (Python API paths + Python API Module Structure sections), which `docs/developers/README.md` indexes (both kept in place).
