---
title: TPU v6e serving recipe matrix (reference configs, not CI-validated)
type: doc-concept
provenance: doc
source: docs/deployment/v6e_recipes.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU v6e serving recipe matrix (reference configs, not CI-validated)

## Definition
The v6e recipe doc sizes `vllm serve` configurations to Trillium's HBM: 1 TensorCore per chip,
32 GB HBM per chip, single-host `v6e-1` (32 GB), `v6e-4` (128 GB), `v6e-8` (256 GB), and
multi-host `v6e-16` (512 GB) and up. Unlike the v7x recipes, the doc says explicitly that these
are **reference configuration examples**, not mirrors of CI benchmark scripts. The single
cross-cutting rule it gives: always pass `--kv-cache-dtype fp8` on v6e to double KV blocks and
avoid preemption at long context or high concurrency.

## Recipe matrix

Sizing table from the doc, merged with the four worked commands it gives. No throughput is
stated, and no perf baselines exist for v6e in the repo.

| Model(s) | Precision | Slice | Layout | Worked command knobs (max-len / MBT / gmu) |
|---|---|---|---|---|
| Llama-3.2-1B/3B-Instruct, Qwen3-8B | bf16 or fp8 | v6e-1 | TP1 | Qwen3-8B: 8192 / 2048 / 0.90, KV fp8, async scheduling |
| Qwen2.5-VL-7B-Instruct, gemma-3-12b-it | bf16 or fp8 | v6e-1 or v6e-4 | TP1 or TP4 | - |
| Qwen3-32B, Qwen3-Coder-30B-A3B-FP8, Qwen3.5-35B-A3B-FP8 | fp8 (bf16 on v6e-4/8) | v6e-4 | TP4 (+EP for MoE) | Qwen3.5-35B-A3B-FP8: 16384 / 4096 / 0.92, `--quantization fp8`, KV fp8, `--attention-backend CUSTOM` |
| Llama-3.3-70B-Instruct, gpt-oss-120b | fp8 / mxfp4 (bf16 on v6e-8) | v6e-8 | TP8 (+EP for MoE) | both: 16384 / 4096 / 0.92, KV fp8, async scheduling |
| Qwen3.5-397B-A17B-FP8 | fp8 | v6e-16 (2 hosts) | TP16, or DP2 x TP8 + EP | - |

Compared with the v7x recipes, the v6e commands use smaller `--max-num-batched-tokens`
(2048-4096 vs 8192 on single-host v7x) and only one of the four passes
`--attention-backend CUSTOM` or `--block-size`.

## In vllm-torchtpu (grounded)
- **One device per chip, 2D torus.** v6e falls in `_TPU_2D_TORUS_GENERATIONS`, so multi-host
  topology strings come from
  [`TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TPU_2D_TORUS_MULTIHOST_TOPOLOGY_MAP)
  (e.g. 16 devices -> `4,4,1`) via
  [`get_tpu_multihost_topology`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#get_tpu_multihost_topology)
  unless `TORCH_TPU_TOPOLOGY` is set. With one core per chip,
  [`hierarchical_moe_split`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#hierarchical_moe_split)
  returns None, so the v7x-only intra-chip TP / inter-chip EP split never applies on v6e.
- **FP8 KV is e5m2 on v6e.** [`TpuPlatform.fp8_dtype`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.fp8_dtype)
  returns `float8_e5m2` when the device is "TPU v6e" (logged as "Automatically using fp8_e5m2
  for FP8 KV cache on TPU v6e") and `float8_e4m3fn` elsewhere. So the doc's "always fp8 KV" tip
  trades mantissa bits (2 vs 3) for the doubled capacity on this generation specifically.
- **VMEM.** [`_TPU_VMEM_BYTES_PER_TENSOR_CORE`](../catalog/src/vllm_torchtpu/env_override.md#_TPU_VMEM_BYTES_PER_TENSOR_CORE)
  records 128 MiB per tensor core for v6e (vs 64 MiB on v7x), used to derive a SparseCore
  offload threshold before libtpu loads; kernel block-size tables (e.g. RPA v3 tuned sizes) carry
  separate "TPU v6e" entries.
- **KV budget.** The same [`TPUWorker.determine_available_memory`](../catalog/src/vllm_torchtpu/worker/tpu_worker.md#TPUWorker.determine_available_memory)
  path as v7x converts `--gpu-memory-utilization` into KV blocks; on 32 GB chips the KV dtype is
  the largest lever on that number.

Owning modules: `platforms/tpu_platform.py`, `distributed/chip_topology.py`, `env_override.py`,
`worker/tpu_worker.py`.

## Doc vs code at this commit
- The doc points to `support_matrices/nightly/v6e/model_support_matrix.csv` "for the latest v6e
  validation status of each checkpoint". At this commit that file has a single row,
  `Qwen/Qwen3.5-397B-A17B`, with UnitTest, Accuracy and Benchmark all "Untested".
- The setup doc labels v6e "Supported ... Not covered by CI", and the CI test pipeline notes
  that several hundred kernel tests call `pytest.fail` rather than skip on v6e. Treat every row
  above as unvalidated until measured.

## Why it matters / when it applies
Use this matrix only as a sizing starting point for a v6e experiment: it tells you which slice
a checkpoint fits on and the HBM-driven knobs (fp8 KV, smaller MBT), but there is no baseline
to regress against. A v6e serving experiment must establish its own baseline first, and should
re-check the kernel choice (`--attention-backend CUSTOM`, block size) that the v7x recipes
always set but most v6e commands omit.

## Connections
- Code concepts: [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md),
  [tpu-platform](../concepts/tpu-platform.md),
  [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md),
  [batched-ragged-paged-attention-kernel](../concepts/batched-ragged-paged-attention-kernel.md),
  [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md),
  [quantization-methods](../concepts/quantization-methods.md).
- Module catalogs: [platforms/tpu_platform](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md),
  [distributed/chip_topology](../catalog/src/vllm_torchtpu/distributed/chip_topology.md),
  [env_override](../catalog/src/vllm_torchtpu/env_override.md),
  [worker/tpu_worker](../catalog/src/vllm_torchtpu/worker/tpu_worker.md).
- Related doc-concepts: [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md),
  [tpu-generations-and-logical-devices](tpu-generations-and-logical-devices.md).

## Source
Extracted from `docs/deployment/v6e_recipes.md` (kept in place); validation status read from
`support_matrices/nightly/v6e/model_support_matrix.csv` and `.buildkite/pipeline_tests.yml`.
