---
title: "Retrospective — qwen3_ag / jax as of 2026-07-03 (Exhausted)"
type: analysis
tags: [retrospective, qwen3_ag, jax, exhausted]
model: qwen3_ag
lane: jax
created: 2026-07-03
updated: 2026-07-03
---

# qwen3_ag / jax retrospective — 2026-07-03 (Sequence Exhausted)

**Scope**: 8B/v6e-8 variant
**Period**: 2026-06-02 → 2026-07-03
**Experiments**: 105 total (98 from prior + 7 new)
**Frontier**: 33.1% MFU / 32.5% MFU natively in bf16 @ seq8192 bs3 (v039). The higher 34.6% MFU from earlier runs could not be sustained due to memory/compilation constraints when stabilizing the architecture.

## Search-strategy assessment

⚠️ **LANE EXHAUSTED (Cross-Entropy Optimization Sequence)**
The JAX lane is officially **exhausted** for the massive cross-entropy reduction optimization sequence. The sequence of experiments from `v031` to `v039` conclusively proved we are stuck at `bs=3`:
- **Tokamax (mosaic_tpu)**: Buggy with `bfloat16`, causing `Invalid dtype for swap` crashes (`v031`).
- **Tokamax (xla fallback)**: Lowers to an un-sharded reference implementation that redundantly computes logits on all devices, tanking effective MFU to 32.9% (`v034`).
- **Standard Optax (bf16)**: Bounded by strict HBM limits. OOMs during XLA compilation at `bs=4` and `bs=6` (`v036`, `v037`) because XLA materializes massive intermediate buffers for the 151k vocabulary reduction.
- **Chunked CE (`jax.lax.scan`)**: OOMs due to program space blow-up (43.82G) because XLA unrolls the `scan` completely during the backward pass (`v038`).

**Conclusion**: We are strictly bounded by HBM and XLA compilation limits on v6e. The maximum stable configuration is standard optax CE at `bs=3` natively in `bf16`, yielding 32.5% MFU (`v039`). Further iteration on CE within standard JAX/Flax on v6e is an anti-recommendation without upstream compiler/Pallas fixes.

## Mechanism tree

- **pallas-kernels** (36 experiments)
  - ❌ tokamax mosaic_tpu — refuted (buggy with bf16, v031)
  - ❌ tokamax xla fallback — refuted (un-sharded redundant compute, v034)
  - 🔵 fused RMSNorm+RoPE+QKV — UNEXPLORED
- **batch-seq-amortization / ce-optimization** (14 experiments)
  - 🏆 optax bf16 CE bs=3 — supported (stable at 32.5% MFU, v039)
  - ❌ optax bf16 CE bs>3 — refuted (OOMs at bs=4 and bs=6, v036, v037)
- **compile-scan / graph-trainer**
  - ❌ chunked CE via `scan` — refuted (unrolls backward pass causing 43.8G program OOM, v038)
- **activation-checkpointing** (14 experiments)
  - ⚠️ 14 in-progress/pending experiments
- **tensor-parallelism** (13 experiments)
  - ⚠️ 13 in-progress/pending experiments
- **splash-attention** (12 experiments)
  - 🏆 v020-splash-attn-only: 32.3% MFU replacing jax.checkpoint with nnx.scan+remat
  - ⚠️ 9 in-progress/pending experiments
- **op-fusion** (6 experiments)
  - 🏆 1 supported experiments (e.g. v042 33.0% MFU)
  - ⚠️ 5 in-progress/pending experiments
- **fsdp-collective** (3 experiments)
- **topology-hw** (2 experiments)
- **baseline** (2 experiments)

## Coverage gaps — what's NOT been explored

| Topic | Catalog options | Tried | Unexplored |
|---|---|---|---|
| Splash attention | 3 | 2 | DeepSeek NSA (Native Sparse Attention) |
| Tensor Parallelism | 3 | 1 | TP=2 across DCN with Scan-over-layers |
| Op fusion | 4 | 2 | Fused Cross-Entropy kernel (properly sharded) |

## Recommended next directions

| # | Direction | Topic | Gain | Conf | Effort | Score | Source |
|---|---|---|---|---|---|---|---|
| 1 | Suspend CE optimization on JAX / wait for compiler fixes | pallas | 0 | high | S | N/A | local-gap: lane exhausted |
| 2 | Shift focus to Tensor Parallelism (TP=2) | TP | Unblocks bs>3 | medium | M | 1.5 | local-gap: index |
| 3 | DeepSeek NSA / Ring Attention with v020 base | Splash | Amortizes seq=16k | medium | L | 0.8 | local-gap: catalog |

## Anti-recommendations

- **Cross-Entropy batch scaling on v6e (bs > 3)**: Structurally closed. XLA materializes massive intermediate buffers, and chunking the backward pass unrolls into program space OOMs.
- **Custom Tokamax Pallas kernels for CE**: Currently broken for `bfloat16` or fall back to un-sharded reference code. Do not pursue until upstream `mosaic_tpu` dtype bugs are resolved.

## Cross-lane brief

### Sibling lane summaries

- **qwen3-cc-torchax**: 8B/v6e-8 frontier at baseline = 19.2% MFU @ seq 2048 bs 8 (66% TC idle).
  - Universal levers transferable: Splash attention, tokamax CE (if implemented in Triton for Torch).

## Experiment ledger (machine-readable)

This ledger inherits from `2026-07-03-qwen3_ag-jax-retrospective.md` and appends the recent CE experiments (`v030`-`v039`).

| v-ID | Date | Variant | Topic | Verdict | Frontier-shift |
|---|---|---|---|---|---|
| v030 | 2026-07-03 | 8B/v6e-8 | pallas-kernels | pending | no |
| v031 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | refuted | no |
| v034 | 2026-07-03 | 8B/v6e-8 | pallas-kernels | refuted | no |
| v035 | 2026-07-03 | 8B/v6e-8 | batch-seq-amortization | pending | no |
| v036 | 2026-07-03 | 8B/v6e-8 | batch-seq-amortization | refuted | no |
| v037 | 2026-07-03 | 8B/v6e-8 | batch-seq-amortization | refuted | no |
| v038 | 2026-07-03 | 8B/v6e-8 | compile-scan | refuted | no |
| v039 | 2026-07-03 | 8B/v6e-8 | batch-seq-amortization | supported | yes (32.5% MFU) |
| v057 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v008 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | yes (35% MFU) |
| v021 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v045 | 2026-06-05 | 8B/v6e-8 | splash-attention | open | no |
| v018 | 2026-06-03 | 8B/v6e-8 | fsdp-collective | in_progress | no |
| v028 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v052 | 2026-06-13 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v019 | 2026-06-03 | 8B/v6e-8 | uncategorized | in_progress | no |
| v042 | 2026-06-04 | 8B/v6e-8 | op-fusion | supported | yes (33.0% MFU) |
| v014 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v022 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v033 | 2026-06-03 | 8B/v6e-8 | fsdp-collective | in_progress | no |
| v003 | 2026-06-02 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v020 | 2026-07-03 | 8B/v6e-8 | topology-hw | confirmed | yes (32.3% MFU) |
| v043 | 2026-06-05 | 8B/v6e-8 | batch-seq-amortization | refuted | no |
| v004 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | no |
| v051 | 2026-06-13 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v007 | 2026-06-02 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v006 | 2026-06-02 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v049 | 2026-06-13 | 8B/v6e-8 | splash-attention | in_progress | no |
| v053 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v016 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v041 | 2026-06-04 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v001 | 2026-06-02 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v044 | 2026-06-05 | 8B/v6e-8 | batch-seq-amortization | open | no |
| v017 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v009 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | no |
| v024 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v010 | 2026-06-02 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v055 | 2026-06-15 | 8B/v6e-8 | activation-checkpointing | in_progress | no |
| v050 | 2026-06-13 | 8B/v6e-8 | splash-attention | in_progress | no |
| v025 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | yes (35% MFU) |
| v046 | 2026-06-05 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v011 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | no |
| v002 | 2026-06-02 | 8B/v6e-8 | fsdp-collective | invalid | no |
| v054 | 2026-06-15 | 8B/v6e-8 | op-fusion | in_progress | no |
| v012 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | yes (35% MFU) |
| v056 | 2026-06-15 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v032 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v013 | 2026-06-03 | 8B/v6e-8 | pallas-kernels | refuted | no |
| v047 | 2026-06-12 | 8B/v6e-8 | batch-seq-amortization | in_progress | no |
| v030 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v029 | 2026-06-03 | 8B/v6e-8 | data-transformation | in_progress | no |
| v6e8-baseline | 2026-06-02 | 8B/v6e-8 | baseline | supported | no |
| v023 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v040 | 2026-06-04 | 8B/v6e-8 | pallas-kernels | in_progress | no |
| v005 | 2026-06-02 | 8B/v6e-8 | splash-attention | in_progress | no |
| v026 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v027 | 2026-06-03 | 8B/v6e-8 | tensor-parallelism | in_progress | no |
| v020-splash-attn-only | 2026-07-03 | 8B/v6e-8 | splash-attention | supported | yes (32.3% MFU) |

## Sources

- Per-lane log: `wiki/experiments/qwen3_ag_autoresearch_optimization/jax/log.md`
- Model page: `wiki/models/qwen3-ag-jax.md`
- Topic taxonomy: `wiki/model-optimization-index.md`
- Pallas catalog: `wiki/analyses/2026-04-23-pallas-kernel-directory.md`
- Prior retrospective: `wiki/analyses/2026-07-03-qwen3_ag-jax-retrospective.md`
