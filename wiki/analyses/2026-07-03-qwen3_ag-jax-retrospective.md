---
title: "Retrospective — qwen3_ag / jax as of 2026-07-03"
type: analysis
tags: [retrospective, qwen3_ag, jax]
model: qwen3_ag
lane: jax
created: 2026-07-03
updated: 2026-07-03
---

# qwen3_ag / jax retrospective — 2026-07-03

**Scope**: 8B/v6e-8 variant
**Period**: 2026-06-02 → 2026-07-03
**Experiments**: 98 total
**Frontier**: 34.6% MFU @ seq8192 bs24 (v036), but recently v020-splash-attn-only achieved 32.3% MFU by disabling custom Pallas kernels and replacing jax.checkpoint with nnx.scan+remat.

## Search-strategy assessment

⚠️ **Single-axis vs kernel work**: Heavy investment in custom Pallas kernels and token routing (~34 experiments) has produced mixed results with many crashes/OOMs. 
✅ **Splash Attention + Scan + Remat**: Recent execution of `v020-splash-attn-only` (32.3% MFU) confirms that standard Splash Attention combined with nnx.scan + nnx.remat layer-over-layer provides a stable, highly performant baseline that avoids the instability of custom fused Pallas kernels.
🔵 **Under-explored topics**: Tensor parallelism scaling with the new scan architecture.

## Mechanism tree

- **pallas-kernels** (34 experiments)
  - ❌ 1 refuted experiments (e.g. v013)
  - ⚠️ 33 in-progress/pending experiments
  - 🔵 fused RMSNorm+RoPE+QKV — UNEXPLORED
- **activation-checkpointing** (14 experiments)
  - ⚠️ 14 in-progress/pending experiments
- **tensor-parallelism** (13 experiments)
  - ⚠️ 13 in-progress/pending experiments
- **splash-attention** (12 experiments)
  - 🏆 1 supported experiments (e.g. v020-splash-attn-only 32.3% MFU)
  - ❌ 1 refuted experiments (e.g. v045)
  - ⚠️ 9 in-progress/pending experiments
  - ✅ v020-splash-attn-only: 32.3% MFU replacing jax.checkpoint with Qwen3ScannedLayers nnx.scan+remat
- **batch-seq-amortization** (9 experiments)
  - ❌ 1 refuted experiments (e.g. v043)
  - ⚠️ 6 in-progress/pending experiments
- **op-fusion** (6 experiments)
  - 🏆 1 supported experiments (e.g. v042 33.0% MFU)
  - ⚠️ 5 in-progress/pending experiments
- **fsdp-collective** (3 experiments)
  - 💥 1 invalid experiments
  - ⚠️ 2 in-progress/pending experiments
- **topology-hw** (2 experiments)
- **baseline** (2 experiments)
  - 🏆 1 supported experiments (e.g. v6e8-baseline )
- **uncategorized** (1 experiments)
  - ⚠️ 1 in-progress/pending experiments
- **data-transformation** (1 experiments)
  - ⚠️ 1 in-progress/pending experiments
- **ring-attention** (1 experiments)
  - ⚠️ 1 in-progress/pending experiments

## Coverage gaps — what's NOT been explored

| Topic | Catalog options | Tried | Unexplored |
|---|---|---|---|
| Splash attention | 3 | 2 | DeepSeek NSA (Native Sparse Attention) |
| Tensor Parallelism | 3 | 1 | TP=2 across DCN with Scan-over-layers |
| Op fusion | 4 | 2 | Fused Cross-Entropy kernel |

## Recommended next directions

| # | Direction | Topic | Gain | Conf | Effort | Score | Source |
|---|---|---|---|---|---|---|---|
| 1 | Standardize on v020 architecture (Splash + nnx.scan/remat) | compile-scan | +2-3pp | high | S | 2.5 | local-gap: v020-splash-attn-only |
| 2 | Tensor Parallelism (TP=2) on top of v020 | TP | Unblocks bs>24 | medium | M | 1.5 | local-gap: index |
| 3 | DeepSeek NSA / Ring Attention with v020 base | Splash | Amortizes seq=16k | medium | L | 0.8 | local-gap: catalog |

## Anti-recommendations

- **Custom fused Pallas kernels (GLU, QKNorm, etc.)** without proper `shard_map` wrapping. Many recent experiments (`v013`, `v054`) have been refuted or crashed due to VMEM limits, OOMs, and XLA redundantly computing forward passes.
- **Pure single-axis batch scaling at TP=1** without memory-saving optimizations (Scan/Remat/Splash) is structurally closed due to HBM limits.

## Cross-lane brief

### Sibling lane summaries

- **qwen3-cc-torchax**: 8B/v6e-8 frontier at baseline = 19.2% MFU @ seq 2048 bs 8 (66% TC idle).
  - Universal levers transferable: Splash attention, tokamax CE.

## Experiment ledger (machine-readable)

| v-ID | Date | Variant | Topic | Verdict | Frontier-shift |
|---|---|---|---|---|---|
| v031 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v008 |  | 8B/v6e-8 | splash-attention | in_progress | yes (35% MFU) |
| v021 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v045 |  | 8B/v6e-8 | splash-attention | open | no |
| v038 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v018 |  | 8B/v6e-8 | fsdp-collective | in_progress | no |
| v028 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v052 | 2026-06-13 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v019 |  | 8B/v6e-8 | uncategorized | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v042 |  | 8B/v6e-8 | op-fusion | supported | yes (33.0% MFU) |
| v014 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v022 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v033 |  | 8B/v6e-8 | fsdp-collective | in_progress | no |
| v003 | 2026-06-02 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v035 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v020 |  | 8B/v6e-8 | topology-hw | confirmed | yes (32.3% MFU) |
| v043 |  | 8B/v6e-8 | batch-seq-amortization | refuted | no |
| v004 |  | 8B/v6e-8 | splash-attention | in_progress | no |
| v051 | 2026-06-13 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v007 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v006 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v015 | 2026-06-27 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v020 |  | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v049 | 2026-06-13 | 8B/v6e-8 | splash-attention | in_progress | no |
| v053 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v016 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v041 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v001 | 2026-06-02 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v034 |  | 8B/v6e-8 | op-fusion | in_progress | no |
| v053 | 2026-06-13 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v053 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v015 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v044 |  | 8B/v6e-8 | batch-seq-amortization | open | no |
| v017 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v045 |  | 8B/v6e-8 | splash-attention | refuted | no |
| v009 |  | 8B/v6e-8 | splash-attention | in_progress | no |
| v024 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v018 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v010 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v042 |  | 8B/v6e-8 | topology-hw | TBD | no |
| v055 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v036 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v050 | 2026-06-13 | 8B/v6e-8 | splash-attention | in_progress | no |
| v025 |  | 8B/v6e-8 | tensor-parallelism | in_progress | yes (35% MFU) |
| v046 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v011 |  | 8B/v6e-8 | splash-attention | in_progress | no |
| v002 | 2026-06-02 | 8B/v6e-8 | fsdp-collective | invalid | no |
| v054 | 2026-06-15 | 8B/v6e-8 | op-fusion | in_progress | no |
| v037 |  | 8B/v6e-8 | splash-attention | in_progress | no |
| v012 |  | 8B/v6e-8 | splash-attention | in_progress | yes (35% MFU) |
| v056 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v053 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v032 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v013 |  | 8B/v6e-8 | pallas-kernels | refuted | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v047 |  | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v013 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v054 | 2026-06-15 | 8B/v6e-8 | op-fusion | in_progress | no |
| v030 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v029 |  | 8B/v6e-8 | data-transformation | in_progress | no |
| v017 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| 2026-06-02-qwen3-jax-v6e8-baseline.md | 2026-06-02 | 8B/v6e-8 | baseline | baseline | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v016 | 2026-06-27 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v054 | 2026-06-15 | 8B/v6e-8 | op-fusion | in_progress | no |
| v048 | 2026-06-13 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v014 | 2026-06-27 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v012 | 2026-06-27 | 8B/v6e-8 | ring-attention | in_progress | no |
| v6e8-baseline | 2026-06-02 | 8B/v6e-8 | baseline | supported | no |
| v023 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v040 |  | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v039 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v053 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v047 |  | 8B/v6e-8 | batch-seq-amortization | pending | no |
| v005 |  | 8B/v6e-8 | splash-attention | in_progress | no |
| v054 | 2026-06-15 | 8B/v6e-8 | op-fusion | in_progress | no |
| v026 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v027 |  | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v020-splash-attn-only | 2026-07-03 | 8B/v6e-8 | splash-attention | supported | yes (32.3% MFU) |

## Sources

- Per-lane log: `wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md`
- Model page: `wiki/models/qwen3-ag-jax.md`
- Topic taxonomy: `wiki/model-optimization-index.md`
- Pallas catalog: `wiki/analyses/2026-04-23-pallas-kernel-directory.md`
- Prior retrospective: `wiki/analyses/2026-06-02-qwen3_ag-jax-retrospective.md`
