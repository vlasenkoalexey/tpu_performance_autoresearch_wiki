---
title: Plugin packaging, version pins and how vLLM loads the TPU platform
type: doc-concept
provenance: doc
source: docs/getting_started/installation.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Plugin packaging, version pins and how vLLM loads the TPU platform

## Definition
vllm-torchtpu is an **out-of-tree vLLM platform plugin**: it never forks vLLM. The installation
doc describes two wheels: `vllm-torchtpu-core` (this repo, `import vllm_torchtpu`) and the
combined `vllm-torchtpu` wrapper, which ships upstream vLLM built with
`VLLM_TARGET_DEVICE="empty"` (no CUDA extensions) and pulls `-core` in. vLLM discovers the
plugin through Python entry points at import time, so users keep running `vllm serve` /
`import vllm`. The docker doc layers images on top: `prod` (runtime only, `:latest` /
`:vX.Y.Z`), `dev` (editable install + test and benchmarking extras, `:nightly`), and an
unpublished `ci` base.

## In vllm-torchtpu (grounded)
- `vllm.platform_plugins` -> [`register_tpu_platform`](../catalog/src/vllm_torchtpu/platforms/__init__.md#register_tpu_platform):
  logs node / TPU type / chip and cores-per-chip info and returns the dotted path of
  [`TpuPlatform`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform), which vLLM
  then uses as `current_platform` (the doc's install check prints
  `current_platform.device_name`).
- `vllm.general_plugins` -> [`register_layers`](../catalog/src/vllm_torchtpu/layers/__init__.md#register_layers):
  runs in every process and registers the TPU model implementations and tokenizers; importing
  the module also imports the TPU attention and linear adapters.
- `vllm_omni.platform_plugins` registers the omni (diffusion) platform when `--extra omni` is
  installed.
- `env_override.py` runs on package import, before torch_tpu / libtpu load, and sets
  process-wide defaults that matter for perf and correctness: `VLLM_CACHE_ROOT` default, TorchTPU
  tier-2/tier-3 compile-cache wiring from
  [`TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT`](../catalog/src/vllm_torchtpu/envs.md#TORCH_TPU_TIER3_COMPILATION_CACHE_ROOT),
  forcing off CUDA-only features (breakable cudagraph, shared-experts stream, the mega AOT
  artifact that never reloads on TPU), and a premapped host buffer pool when the Raiden KV stack
  is on.

Owning modules: `platforms/__init__.py`, `layers/__init__.py`, `env_override.py`, `pyproject.toml`.

## Why it matters / when it applies
- **The pins are perf-relevant.** `pyproject.toml` pins `torch==2.13.0`, `torch_tpu==0.2.0`,
  `jax==0.11.2`, `libtpu==0.0.50` and builds `vllm` v0.32.0 from source in the `vllm` group. Its
  comments warn that the `env_override.py` SparseCore-offload threshold gate and the per-config
  `LIBTPU_INIT_ARGS` in the benchmark configs were tuned against an earlier libtpu (re-verify on
  bump), and that the JAX pin regresses a Pallas remainder loop that `env_override.py`
  monkey-patches (validated on Qwen3.5-397B DP8 EP). A recipe's numbers hold only on its pinned
  stack.
- **CPU torch wheels.** On x86_64, default PyPI serves CUDA torch; the doc requires the PyTorch
  CPU index (`UV_TORCH_BACKEND=cpu` or `--extra-index-url .../whl/cpu`) so no `nvidia-*` stack
  lands on TPU hosts.
- **Image choice.** Benchmarking needs the `dev`/nightly image (`--extra benchmarking`:
  lm-eval, evalscope, `runai-model-streamer[gcs]` for gs:// streaming); `prod` lacks it. The
  `ci`/`dev` images also carry `vllm-router`, used by the disaggregated benchmark clients when a
  serve config sets `AGENTX_PROXY=router`. Containers need `--privileged --net=host` and a large
  `--shm-size` (doc: 150 GB) for `/dev/vfio/*` and shared host memory.
- **Python 3.12 only.** The doc attributes this to the `tpu-sync-torch` / `torch_tpu` wheels;
  `pyproject.toml` gives the reason as the cp312-only `tpu-raiden-torch` wheels.

## Doc vs code at this commit
- The `pyproject.toml` comment on the platform entry point says the function returns the class
  path "when this platform should activate, else None", but `register_tpu_platform`
  unconditionally returns the `TpuPlatform` path.
- Option 3 of the doc says "Currently, `vllm==0.32.0` is supported", consistent with the `vllm`
  dependency group pin.

## Connections
- Code concepts: [tpu-platform](../concepts/tpu-platform.md),
  [vllm-layer-adapters](../concepts/vllm-layer-adapters.md),
  [vllm-model-patches](../concepts/vllm-model-patches.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [omni-diffusion-support](../concepts/omni-diffusion-support.md),
  [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md).
- Module catalogs: [platforms/__init__](../catalog/src/vllm_torchtpu/platforms/__init__.md),
  [platforms/tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md),
  [layers/__init__](../catalog/src/vllm_torchtpu/layers/__init__.md),
  [env_override](../catalog/src/vllm_torchtpu/env_override.md).
- Related doc-concepts: [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md),
  [tpu-patch-registry](tpu-patch-registry.md), [compilation-cache-and-warmup](compilation-cache-and-warmup.md),
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md),
  [benchmark-harness-and-regression-gates](benchmark-harness-and-regression-gates.md).

## Source
Extracted from `docs/getting_started/installation.md` and `docs/getting_started/docker.md`
(kept in place); pins and entry points read from `pyproject.toml`.
