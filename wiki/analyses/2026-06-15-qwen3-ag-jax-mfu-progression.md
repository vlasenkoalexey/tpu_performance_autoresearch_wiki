---
title: "Qwen3-ag jax — per-experiment MFU/TPS data"
type: analysis
created: 2026-06-15
updated: 2026-06-16
tags: [qwen3-ag, jax, mfu, tps, data]
---

# Qwen3-ag jax — per-experiment MFU/TPS data

Best-effort per-experiment extraction for the **ag** lane, in experiment order. MFU is on the causal (MaxText-comparable) basis. Frontiers are clamped to the verified model-page best. MaxText MFU targets: 2k = 38.0%, 8k = 45.3% (native — **different FLOP basis, so compare to MaxText on TPS**). `—` = not recoverable (crash / no metric / unparsed). Regenerate: `python wiki/analyses/qwen3/build_explorer.py`.

**Frontier:** 2k = 33.0% MFU / 4,515 tok/s/chip · 8k = 30.6% MFU / 5,329 tok/s/chip.

| # | Experiment | seq | verdict | MFU (causal) | tok/s/chip |
|---|---|---|---|---|---|
| 1 | 2026-06-02-qwen3-jax-v001-batch-scaling | 2k | — | — | — |
| 2 | 2026-06-02-qwen3-jax-v002-selective-sc-offload | 2k | invalid | — | — |
| 3 | 2026-06-02-qwen3-jax-v003-selective-remat | 2k | — | — | — |
| 4 | 2026-06-02-qwen3-jax-v004-splash-bs2 | 2k | — | 25.3% | 4,515 |
| 5 | 2026-06-02-qwen3-jax-v005-splash-tuned | 2k | — | 22.5% | — |
| 6 | 2026-06-02-qwen3-jax-v006-tokamax-ce | 2k | — | — | — |
| 7 | 2026-06-02-qwen3-jax-v6e8-baseline-repro | 2k | supported | 20.0% | — |
| 8 | 2026-06-02-qwen3-jax-v6e8-baseline | 2k | baseline | 20.5% | — |
| 9 | 2026-06-02-qwen3-jax-v007-tp2-bs2 | 2k | — | — | — |
| 10 | 2026-06-02-qwen3-jax-v008-splash-tp2-bs4 | 2k | — | 28.6% | — |
| 11 | 2026-06-02-qwen3-jax-v009-splash-tp2-bs8 | 2k | — | 28.6% | — |
| 12 | 2026-06-02-qwen3-jax-v010-splash-tp2-tokamax-bs8 | ? | — | — | — |
| 13 | 2026-06-02-qwen3-jax-v011-splash-tp2-remat-dots-bs8 | 2k | — | — | — |
| 14 | 2026-06-02-qwen3-jax-v012-splash-tp4-bs8 | 2k | — | 25.4% | — |
| 15 | 2026-06-03-qwen3-jax-v013-splash-tp2-tokamax-bs4 | 2k | — | 28.6% | — |
| 16 | 2026-06-03-qwen3-jax-v014-splash-tp2-tokamax-remat-bs8 | 2k | — | — | — |
| 17 | 2026-06-03-qwen3-jax-v015-splash-tp2-tokamax-remat-fused-rope-bs8 | 2k | — | — | — |
| 18 | 2026-06-03-qwen3-jax-v016-splash-tp1-tokamax-remat-fused-bs4 | 2k | — | 30.7% | — |
| 19 | 2026-06-03-qwen3-jax-v017-splash-tp2-tokamax-remat-scan-bs8 | 2k | — | 30.8% | — |
| 20 | 2026-06-03-qwen3-jax-v018-collective-matmul-off | ? | — | 29.9% | — |
| 21 | 2026-06-03-qwen3-jax-v019-phase2-bundle | ? | — | — | — |
| 22 | 2026-06-03-qwen3-jax-v020-phase2-bundle-bs4 | ? | — | 28.1% | — |
| 23 | 2026-06-03-qwen3-jax-v021-tp1-vocab-parallel-bs4 | 2k | — | — | — |
| 24 | 2026-06-03-qwen3-jax-v022-tp1-chunked-xla-bs4 | ? | — | — | — |
| 25 | 2026-06-03-qwen3-jax-v023-tp1-chunked-xla-bs4 | 2k | — | — | — |
| 26 | 2026-06-03-qwen3-jax-v024-tp1-xla-bs4 | 2k | — | — | — |
| 27 | 2026-06-03-qwen3-jax-v025-tp1-vocab-parallel-bs2 | 2k | — | 24.3% | — |
| 28 | 2026-06-03-qwen3-jax-v026-tp1-vocab-parallel-bs4-no-outer-ckpt | ? | — | 32.2% | — |
| 29 | 2026-06-03-qwen3-jax-v027-tp1-vocab-parallel-bs8-no-outer-ckpt | ? | — | 32.8% | — |
| 30 | 2026-06-03-qwen3-jax-v028-tp1-vocab-parallel-bs16-no-outer-ckpt | 2k | — | 32.8% | — |
| 31 | 2026-06-03-qwen3-jax-v029-tp1-vocab-parallel-bs8-fix-layout | ? | — | 32.6% | — |
| 32 | 2026-06-03-qwen3-jax-v030-tp1-vocab-parallel-bs8-chunked-xla | ? | — | 32.8% | — |
| 33 | 2026-06-03-qwen3-jax-v031-tp1-vocab-parallel-bs8-mosaic-tpu | ? | — | 32.8% | — |
| 34 | 2026-06-03-qwen3-jax-v032-tp1-vocab-parallel-bs8-mosaic-tpu-patched | ? | — | 32.8% | — |
| 35 | 2026-06-03-qwen3-jax-v033-tp1-vocab-parallel-bs8-collective-overlap | ? | — | 32.8% | — |
| 36 | 2026-06-04-qwen3-jax-v034-tp1-vocab-parallel-bs8-fused-qknorm-rope | 2k | — | 13.3% | — |
| 37 | 2026-06-04-qwen3-jax-v035-tp1-vocab-parallel-bs8-xla-sdpa | 2k | — | 32.8% | — |
| 38 | 2026-06-04-qwen3-jax-v036-tp1-vocab-parallel-bs8-chunked-xla | ? | — | 32.8% | — |
| 39 | 2026-06-04-qwen3-jax-v037-tp1-vocab-parallel-bs8-chunked-xla-splash-fix | 2k | — | 32.8% | — |
| 40 | 2026-06-04-qwen3-jax-v038-tp1-vocab-parallel-bs8-fused-rope | ? | — | 32.8% | — |
| 41 | 2026-06-04-qwen3-jax-v039-tp1-vocab-parallel-bs32-seq1024 | 2k | — | 33.0% | — |
| 42 | 2026-06-04-qwen3-jax-v040-tp1-vocab-parallel-bs16-seq2048-tokamax | 2k | — | — | — |
| 43 | 2026-06-04-qwen3-jax-v041-tp1-vocab-parallel-bs16-seq2048-tokamax-shardmap | 2k | — | 24.5% | — |
| 44 | 2026-06-04-qwen3-jax-v042-tp1-vocab-parallel-bs16-seq2048-tokamax-shardmap-scan | 2k | tbd | — | — |
| 45 | 2026-06-05-qwen3-jax-v042-gate-up-fusion | 2k | supported | 33.0% | — |
| 46 | 2026-06-05-qwen3-jax-v043-bs32 | 2k | refuted | — | — |
| 47 | 2026-06-05-qwen3-jax-v044-bs24 | 2k | open | — | — |
| 48 | 2026-06-05-qwen3-jax-v045-nsa-attention | 2k | open | — | — |
| 49 | 2026-06-05-qwen3-jax-v045-nsa | 2k | refuted | — | — |
| 50 | 2026-06-05-qwen3-jax-v046-nsa-pallas | ? | — | — | — |
| 51 | 2026-06-12-qwen3-jax-v047-seq8k-baseline | 8k | pending | — | — |
| 52 | 2026-06-13-qwen3-jax-v047-seq8k-baseline | 8k | — | 30.6% | 5,329 |
| 53 | 2026-06-13-qwen3-jax-v048-bs64 | 8k | — | — | — |
| 54 | 2026-06-13-qwen3-jax-v049-splash-bs64 | 8k | — | — | — |
| 55 | 2026-06-13-qwen3-jax-v050-splash-tokamax-bs64 | ? | — | — | — |
| 56 | 2026-06-13-qwen3-jax-v051-tokamax-bs64 | 8k | — | — | — |
| 57 | 2026-06-13-qwen3-jax-v052-selective-remat-bs64 | 8k | — | — | — |
| 58 | 2026-06-13-qwen3-jax-v053-block-remat-bs64 | ? | — | — | — |
| 59 | 2026-06-15-qwen3-jax-v053-block-remat-bs64-b | ? | — | — | — |
| 60 | 2026-06-15-qwen3-jax-v053-block-remat-bs64-c | ? | — | — | — |
| 61 | 2026-06-15-qwen3-jax-v053-block-remat-bs64-d | ? | — | — | — |
| 62 | 2026-06-15-qwen3-jax-v053-block-remat-bs64-e | ? | — | — | — |
| 63 | 2026-06-15-qwen3-jax-v054-fused-qknorm-rope-c | ? | — | — | — |
| 64 | 2026-06-15-qwen3-jax-v054-fused-qknorm-rope-d | ? | — | — | — |
| 65 | 2026-06-15-qwen3-jax-v054-fused-qknorm-rope-e | 8k | — | — | — |
| 66 | 2026-06-15-qwen3-jax-v054-fused-qknorm-rope-f | ? | — | — | — |
| 67 | 2026-06-15-qwen3-jax-v055-ac-selective-remat | ? | — | — | — |
| 68 | 2026-06-15-qwen3-jax-v056-splash-vmem-tune | 8k | — | — | — |
| 69 | 2026-06-15-qwen3-jax-v057-d-tokamax-layer-ckpt | 8k | — | — | — |
| 70 | 2026-06-15-qwen3-jax-v057-e-tokamax-layer-ckpt-fix-splash | 8k | — | — | — |
| 71 | 2026-06-15-qwen3-jax-v057-f-tokamax-layer-ckpt-fix-splash | 2k | — | — | — |
| 72 | 2026-06-15-qwen3-jax-v057-g-tokamax-layer-ckpt-fix-splash | 2k | — | — | — |
| 73 | 2026-06-15-qwen3-jax-v057-h-tokamax-block-remat | 2k | — | — | — |
| 74 | 2026-06-15-qwen3-jax-v057-i-tokamax-block-remat-fsdp-fix | 8k | — | — | — |
| 75 | 2026-06-15-qwen3-jax-v057-j-tokamax-layer-ckpt-bs4 | 2k | — | — | — |
| 76 | 2026-06-15-qwen3-jax-v057-k-tokamax-policy | 8k | — | — | — |
| 77 | 2026-06-15-qwen3-jax-v057-l-tokamax-layer-dots | 2k | — | — | — |
| 78 | 2026-06-15-qwen3-jax-v057-m-tokamax-layer-dots-bs8 | 2k | — | — | — |
| 79 | 2026-06-15-qwen3-jax-v057-n-tokamax-layer-dots-bs8 | 8k | — | — | — |
| 80 | 2026-06-15-qwen3-jax-v057-o-tokamax-layer-dots-bs4 | ? | — | — | — |
| 81 | 2026-06-15-qwen3-jax-v057-p-block-remat-bs8 | 8k | — | — | — |
| 82 | 2026-06-15-qwen3-jax-v057-q-block-remat-bs8-no-policy | 8k | — | — | — |
| 83 | 2026-06-15-qwen3-jax-v057-r-nested-ckpt-bs8 | 8k | — | — | — |
| 84 | 2026-06-15-qwen3-jax-v057-s-nested-ckpt-nothing-saveable-bs8 | 8k | — | — | — |
| 85 | 2026-06-15-qwen3-jax-v057-t-nested-ckpt-custom-outer-policy-bs8 | 8k | — | — | — |
| 86 | 2026-06-15-qwen3-jax-v057-tokamax-fix-b | 8k | — | — | — |
| 87 | 2026-06-15-qwen3-jax-v057-tokamax-fix-c | 8k | — | — | — |
| 88 | 2026-06-15-qwen3-jax-v057-tokamax-fix | ? | — | — | — |
| 89 | 2026-06-15-qwen3-jax-v057-u-nested-ckpt-bs4 | 8k | — | — | — |

## See also

- [Interactive explorer](qwen3/mfu-explorer.html) · [progression plot](qwen3/mfu-progression.png)
- [Qwen3 ag — jax model page](../models/qwen3-ag-jax.md)
