---
title: TPU generations, support tiers and logical devices per chip
type: doc-concept
provenance: doc
source: docs/getting_started/tpu_setup.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU generations, support tiers and logical devices per chip

## Definition
The setup doc sorts TPU generations into three tiers for vllm-torchtpu: **v7x (Ironwood)
recommended** - "the generation vllm-torchtpu is continuously validated on in CI";
**v6e (Trillium) supported** - "not covered by CI"; **v5e, v5p, v4 experimental**. Its one
load-bearing hardware fact is the v7x dual-core note: each physical v7x chip exposes **2
logical TensorCore devices** to PyTorch and JAX, so a 4-chip `tpu7x-8` host gives 8 devices
(`--tensor-parallel-size=8`) and 768 GB HBM. Parallelism sizes in every recipe are counted in
these logical devices, not chips.

## In vllm-torchtpu (grounded)
How the plugin encodes "devices per chip" per generation:

| Generation | Interconnect | Devices per chip seen by vLLM | Topology map used for multi-host |
|---|---|---|---|
| v5e, v6e | 2D torus | 1 | [`TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP) |
| v4, v5p | 3D torus | 1 (megacore presents the core pair as one device) | 3D torus map |
| v7x | 3D torus | 2 (each core a separate device) | [`TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TPU_3D_TORUS_DUAL_DEVICE_TOPOLOGY_MAP) - same meshes as v4/v5p, keyed by twice the device count (16 -> `2,2,2,2`) |
| v8i | hierarchical BoardFly | - | v8i map (present in code; not mentioned in the doc) |

- [`get_tpu_multihost_topology`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#get_tpu_multihost_topology)
  resolves the mesh string: `TORCH_TPU_TOPOLOGY` (set by GKE; `AxBxC` normalized to `A,B,C`)
  wins, otherwise the generation's map keyed by world size, else it raises asking you to export
  `TORCH_TPU_TOPOLOGY`. Generation comes from
  [`TpuPlatform.get_device_name`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.get_device_name).
- [`get_chip_topology`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#get_chip_topology)
  groups visible devices by physical chip into a
  [`ChipTopology`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#ChipTopology)
  (`cores_per_chip` = 2 on v7x). That is what makes the dual-core layout exploitable:
  [`hierarchical_moe_split`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#hierarchical_moe_split)
  runs expert parallelism between chips and tensor parallelism between the two cores of a chip,
  and `distributed/intra_chip.py` builds a per-chip process group whose collectives stay
  on-package (its docstring: halving each core's HBM read beats the added on-chip hop). Both
  return None / do nothing on 1-device-per-chip generations.
- Per-generation constants elsewhere: [`TpuPlatform.fp8_dtype`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.fp8_dtype)
  (e5m2 FP8 KV on v6e, e4m3 elsewhere) and
  [`_TPU_VMEM_BYTES_PER_TENSOR_CORE`](../catalog/src/vllm_torchtpu/env_override.md#_TPU_VMEM_BYTES_PER_TENSOR_CORE)
  (64 MiB per core on v7x and v5p, 128 MiB on v6e and v5e).

## Why it matters / when it applies
- **Count in devices.** On v7x, TP=8 is one host, TP=32 is four hosts (Kimi-K3 recipe); the
  `google.com/tpu: 4` limit in GKE manifests is chips, not devices.
- **The two cores of a v7x chip are a cheap axis.** On-package exchange is much cheaper than
  ICI, which is why chip-aware MoE/projection splits exist and why "TP within a chip, EP/DP
  across chips" is a recurring layout lever.
- **Tier = evidence.** Only v7x has CI perf baselines; v6e and older generations have none, so
  results there need a self-established baseline.
- **Provisioning path differs by generation** (doc): v6e and v5p via the Compute Engine API,
  v7x, v5e and v4 via queued resources; flex-start (DWS) capacity is available on all but v4.
  `tpu-info` (installed with the package) shows per-chip utilization and HBM use.

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [tpu-platform](../concepts/tpu-platform.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [kimi-k3-model](../concepts/kimi-k3-model.md).
- Module catalogs: [platforms/tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md),
  [distributed/chip_topology](../catalog/src/vllm_torchtpu/distributed/chip_topology.md),
  [env_override](../catalog/src/vllm_torchtpu/env_override.md).
- Related doc-concepts: [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md),
  [v6e-serving-recipe-matrix](v6e-serving-recipe-matrix.md),
  [gke-multihost-jobset-deployment](gke-multihost-jobset-deployment.md),
  [dp-ep-moe-layouts](dp-ep-moe-layouts.md), [multihost-execution-backends](multihost-execution-backends.md).

## Source
Extracted from `docs/getting_started/tpu_setup.md` (kept in place); the v7x device/HBM figures
also appear in `docs/deployment/v7x_recipes.md`.
Also stated in `README.md` ("Supported hardware": v7x recommended and validated in CI on every PR and nightly; v6e supported, not in CI; v5e/v5p experimental) and `docs/user_guide/parallelism.md` (an engine group consumes `DP * TP * PP * PCP` logical devices; a 4-chip v7x host = 8, e.g. `TP=8`, `DP=8,TP=1`, `DP=4,TP=2`) - see [composable-6d-parallelism](composable-6d-parallelism.md).
