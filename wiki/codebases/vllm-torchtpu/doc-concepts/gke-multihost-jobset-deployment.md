---
title: GKE JobSet deployment for multi-host slices and P/D disaggregation
type: doc-concept
provenance: doc
source: docs/deployment/kubernetes.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# GKE JobSet deployment for multi-host slices and P/D disaggregation

## Definition
The Kubernetes doc presents the repo's CI JobSet manifests
(`.buildkite/kubernetes/manifests/workloads/`) as reference deployments for two shapes:
**one multi-host v7x slice** serving one engine (via vLLM's native `mp` backend or via Ray),
and **prefill/decode (P/D) disaggregated serving** where each role is its own engine. Its three
best practices: indexed Job completion so GKE places all pods on one interconnected slice;
TPU node selectors (accelerator + topology + `google.com/tpu: 4` chips per v7x host); and
persistent compile/model caches with the `profile_cache` subtree kept on an in-memory
`emptyDir` so the free-HBM probe always runs fresh.

## In vllm-torchtpu (grounded)
**Multi-host slice, `mp` backend (no Ray).** `mp-multihost-slice.yaml` runs one indexed Job
with `parallelism = completions = <hosts>` and `DP_LOCAL=8` (eight devices per host). The plugin
side is `distributed/tpu_mp_multihost.py`:
- [`prepare_mp_multihost_dp_env`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#prepare_mp_multihost_dp_env)
  handles vLLM's native multi-node DP (`--data-parallel-size` wider than
  `--data-parallel-size-local`); [`prepare_mp_multihost_env`](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md#prepare_mp_multihost_env)
  handles `--nnodes N` TP/PP/PCP sharding across hosts.
- Both export the TorchTPU view of the whole ICI mesh before workers fork:
  `TORCH_TPU_SLICEBUILDER_ADDRESSES` (every worker's ip:port in global-rank order, exchanged
  through a short-lived TCPStore rendezvous with host 0 as master), `TORCH_TPU_TOPOLOGY` (from
  [`get_tpu_multihost_topology`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#get_tpu_multihost_topology)),
  and a shared `TORCH_TPU_XPROF_SESSION_ID` so per-host profiler traces can be merged.
- They are called from [`TpuPlatform.check_and_update_config`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.check_and_update_config),
  not from [`TpuMultiprocExecutor`](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md#TpuMultiprocExecutor),
  because vLLM's headless (non-leader) node hardcodes vanilla `MultiprocExecutor`; config
  construction is the only hook that runs identically on every host. The manifest sets
  `POD_IP` so each host publishes the right address into the rendezvous.

**Multi-host slice, Ray.** `ray-multihost-slice.yaml` uses the same one-Job shaping;
`JOB_COMPLETION_INDEX=0` is the Ray head. The address list is built by
[`RayDistributedExecutor`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md#RayDistributedExecutor)
inside its own executor init instead.

**P/D disaggregation.** The 1P1D / P8D8 / DSv4 manifests give each role its **own**
replicatedJob and slice (2x2x1 = one 8-device v7x host per role), and the roles reach each other
over the pod network, not ICI. KV moves through the Raiden transfer stack (`TPU_RAIDEN_*` env,
`TPU_RAIDEN_ADVERTISE_HOST` from the downward API). The Kimi-K3 1P1D manifest is the multi-host
variant: each role on a 2x2x4 slice (4 hosts), TP8 x DP4 x EP32 over vLLM's multi-node DP with
one DP replica per host.

**Caches and the profile run.** Both cache env vars point at the CI fleet's compilation bucket
(`VLLM_CACHE_ROOT` would otherwise default under `$HOME` on the boot disk, set by
`env_override.py`). The `profile_cache` shadow mount exists because
[`TPUModelRunner._profile_isolated_cache`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._profile_isolated_cache)
compiles the kv=0 profiling graph under `<cache_root>/profile_cache/<hash>`; if that persisted,
a later run would load it instead of compiling and the HBM probe would measure nothing. See
[profile-cache-and-free-hbm-probe](profile-cache-and-free-hbm-probe.md).

Owning modules: `distributed/tpu_mp_multihost.py`, `executors/`, `platforms/tpu_platform.py`,
`runner/tpu_runner.py`.

## Why it matters / when it applies
- **One Job per slice, always.** GKE places a multi-host TPU slice as the pods of a single
  indexed Job; two Jobs asking for the same shape get two slices with no interconnect between
  them. P/D roles are the deliberate exception: they are separate engines that only need the
  network.
- **Compile time dominates bring-up.** The mp manifest raises `activeDeadlineSeconds` to 8 h
  because "these models compile for the better part of an hour before the sweep starts" -
  persistent compile caches are a throughput-of-experiments lever, not a nicety.
- **Head-only success.** `successPolicy` on index 0 frees worker chips as soon as the head
  exits instead of tens of seconds later.

## Doc vs code at this commit
- The manifests are **not self-contained**: per `manifests/README.md`, caches and their mounts,
  the gcsfuse sidecar, TPU toleration, service account, restart/retry policy and memory request
  come from a fleet-wide `tpu-ci.google.com/defaults: standard` annotation defined outside this
  repo. Reusing them on another cluster means supplying those yourself.
- `qwen3.5-p8d8-disagg.yaml` is described as "multi-host P8D8 disaggregated serving"; the
  manifest says it is a PCP8 -> TP2xDP4 disaggregation **correctness test** on two single-host
  slices. `dsv4-pd-disagg.yaml` is a DeepSeek-V4-**Flash** DP8/DP8 correctness test (doc: generic
  DeepSeek-V4 serving).
- Two manifests in the directory are not listed in the doc: `kimi-k3-agentx-1p1d.yaml` and
  `qwen3.5-gpc-two-replica.yaml` (global prefix caching across two replicas; its comment notes a
  replica at a nonzero chip offset enumerates devices in physical rather than rank order and
  generates corrupt output, hence one replica per whole host).
- The doc (and the manifests) set `VLLM_XLA_CACHE_PATH`, but no module under
  `src/vllm_torchtpu` reads it at this commit; the plugin's compiled-executable cache is keyed
  under vLLM's compilation `cache_dir` (derived from `VLLM_CACHE_ROOT`). Upstream vLLM or other
  tooling may still consume it.

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md),
  [tpu-platform](../concepts/tpu-platform.md),
  [tpu-model-runner](../concepts/tpu-model-runner.md),
  [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md),
  [kimi-k3-model](../concepts/kimi-k3-model.md).
- Module catalogs: [distributed/tpu_mp_multihost](../catalog/src/vllm_torchtpu/distributed/tpu_mp_multihost.md),
  [executors/ray_distributed_executor](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor.md),
  [executors/tpu_multiproc_executor](../catalog/src/vllm_torchtpu/executors/tpu_multiproc_executor.md),
  [platforms/tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md).
- Related doc-concepts: [multihost-execution-backends](multihost-execution-backends.md) (the mp vs Ray
  backends from the user guide's side), [compilation-cache-and-warmup](compilation-cache-and-warmup.md),
  [profile-cache-and-free-hbm-probe](profile-cache-and-free-hbm-probe.md),
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md),
  [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md),
  [multi-rank-trace-capture](multi-rank-trace-capture.md),
  [disaggregated-pd-trace-correlation](disaggregated-pd-trace-correlation.md).

## Source
Extracted from `docs/deployment/kubernetes.md` (kept in place), which embeds
`.buildkite/kubernetes/manifests/README.md` and `workloads/mp-multihost-slice.yaml`; the other
manifests' header comments were read for the shapes above.
