---
title: Plugin architecture - torch model execution, JAX/Pallas kernels, jax_op bridge
type: doc-concept
provenance: doc
source: docs/developers_guide/coding_guidance.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Plugin architecture - torch model execution, JAX/Pallas kernels, jax_op bridge

## Definition
The coding guidance's architecture ground rules (section 2) and "reuse upstream" rules
(section 3). vllm-torchtpu is a **vLLM platform plugin, not a fork**: vLLM installs as a
plain wheel and TPU behavior is injected through the `vllm.platform_plugins` and
`vllm.general_plugins` entry points. Model execution is **torch** - the TPU model runner
subclasses vLLM's GPU runner and runs under `torch.compile(backend="tpu",
fullgraph=True)` - while kernels are **JAX/Pallas**, bridged into torch as custom ops via
TorchTPU's `pallas.jax_op` (and a sharded variant). The directory layout enforces a
one-way dependency from vLLM-facing adapters down to dependency-free kernels.

## In vllm-torchtpu (grounded)
- Entry points (from `pyproject.toml`):
  [`register_tpu_platform`](../catalog/src/vllm_torchtpu/platforms/__init__.md#register_tpu_platform)
  activates [`TpuPlatform`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform);
  [`register_layers`](../catalog/src/vllm_torchtpu/layers/__init__.md#register_layers)
  registers the TPU layer adapters (and a separate omni platform entry point exists).
- Runner: [`TPUModelRunner`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner)
  subclasses upstream `GPUModelRunner`; the `"tpu"` compile backend is
  [`TpuCompilerAdaptor`](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md#TpuCompilerAdaptor)
  (FX -> MLIR -> PjRt, with per-shape disk caching).
- Bridge, one instance among many: `_get_quantized_matmul_op` in
  `layers/adapter/linear_common.py` wraps the Pallas quantized matmul as
  `pallas.jax_op("pallas::quantized_matmul_kernel", ...)`. SPMD kernels use
  [`sharded_jax_op`](../catalog/src/vllm_torchtpu/distributed/sharded_jax_op.md#sharded_jax_op);
  other bridges live under `layers/adapter/custom_ops/*_op.py` and kernel-local
  `vllm_adapter.py` files (e.g.
  [`pcp_streaming_jax_op`](../catalog/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/vllm_adapter.md#pcp_streaming_jax_op)).

## Directory contract (R-2.1 - R-2.4)
| Directory | Role | Allowed dependencies |
|---|---|---|
| `kernels/` | JAX/Pallas kernels, tuned tables, eligibility predicates | jax/pallas + small helpers; **no vLLM, no torch** (except dedicated `vllm_adapter.py` bridges), **no env reads** |
| `layers/core/` | Shared numeric/layout logic | jax first; torch/vLLM only at the boundary |
| `layers/adapter/` | vLLM/torch-facing layer: quant methods, fused-MoE wiring, attention backends, `custom_ops/` bridges | torch, vLLM, layers/core, kernels |
| `platforms/`, `runner/`, `worker/`, `executors/` | vLLM integration surface | thin translation only |

Further rules: interface files stay thin (hardware logic goes to `layers/core/` or the
kernel); kernels are self-contained (everything via arguments, no vLLM config objects in
signatures, tile tuning and envelope predicates next to the kernel); kernels are named by
function (`ragged_paged_attention/`, `quantized_matmul/`), not by model, unless the
component is genuinely model-specific. R-3.x: search vLLM upstream -> vllm-torchtpu ->
JAX/Pallas utilities before writing anything; subclass the deepest vLLM base and
override only what differs; no per-model forks of shared attention/MoE/RoPE; fix
upstream defects upstream; use extension points (`register_oot`,
`AttentionBackendEnum`), not private APIs.

## Project framing (README)
The top-level `README.md` and `docs/README.md` state the same architecture as a product
promise: vllm-torchtpu is "the PyTorch-native TPU backend for vLLM" - an out-of-tree
platform plugin (`vllm-torchtpu`) that runs vLLM's standard PyTorch model definitions on
Cloud TPU through TorchTPU (`torch.compile(backend="tpu")`) plus a library of custom
JAX/Pallas kernels, with "the same vLLM you already use - same CLI, same
OpenAI-compatible server, same model definitions ... with no model code changes". The
README positions the earlier JAX backend (`tpu-inference`, now "vLLM JAX") as the path
for pure-JAX model implementations, and vllm-torchtpu as the recommended path for
PyTorch model definitions. In practice "no model code changes" means no changes in
*upstream vLLM's* model files: TPU-specific model behavior is injected by
`models/vllm/*_patch.py` via the patch registry, and two families (DeepSeek-V4,
Kimi-K3) have dedicated implementations under `models/vllm/`. The README's kernel list
is mapped to code on [tpu-kernel-library-map](tpu-kernel-library-map.md); its hardware
tiers match [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md).

## Why it matters / when it applies
- For performance work this split decides **where** a change goes: a faster attention
  or MoE path is a kernel change (own PR, tuned tables, envelope predicate) plus a thin
  adapter change; a scheduling or batching change is runner/patch territory; model-only
  tweaks go to `models/vllm/*_patch.py` through the
  [patch registry](tpu-patch-registry.md).
- Because kernels take no env reads and no vLLM objects, they can be benchmarked and
  autotuned standalone, and their compiled programs do not silently capture global
  state ([derive-dont-declare](derive-dont-declare.md)).
- Version pins in `pyproject.toml` (JAX, libtpu, torch-tpu, vLLM) are load-bearing:
  write against the pinned API, no compat shims; removing back-compat branches waits
  for a pin bump with before/after perf evidence (R-2.5).

## Connections
- Code concepts: [tpu-platform](../concepts/tpu-platform.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [custom-ops](../concepts/custom-ops.md),
  [vllm-layer-adapters](../concepts/vllm-layer-adapters.md),
  [attention-and-layer-core](../concepts/attention-and-layer-core.md),
  [vllm-model-patches](../concepts/vllm-model-patches.md)
- Module catalogs: [platforms/__init__](../catalog/src/vllm_torchtpu/platforms/__init__.md),
  [tpu_runner](../catalog/src/vllm_torchtpu/runner/tpu_runner.md),
  [compilation/tpu_compiler](../catalog/src/vllm_torchtpu/compilation/tpu_compiler.md),
  [distributed/sharded_jax_op](../catalog/src/vllm_torchtpu/distributed/sharded_jax_op.md),
  [layers/adapter/linear_common](../catalog/src/vllm_torchtpu/layers/adapter/linear_common.md)
- Related doc-concepts: [plugin-packaging-and-registration](plugin-packaging-and-registration.md)
  (install-side view: wheels, pins, entry-point discovery),
  [tpu-patch-registry](tpu-patch-registry.md),
  [derive-dont-declare](derive-dont-declare.md),
  [fail-fast-and-fallback-policy](fail-fast-and-fallback-policy.md),
  [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [generic-quantization-machinery](generic-quantization-machinery.md)

## Source
Extracted from `docs/developers_guide/coding_guidance.md` sections 2-3, with the
directory map in `CONTRIBUTING.md` section 4 (included by
`docs/developers_guide/contributing.md`) (kept in place); project framing from `README.md` and `docs/README.md` (kept in place).
