---
title: "Retrospective #5 — qwen3_cc / jax vs MaxText config delta (what we never tried)"
type: analysis
tags: [retrospective, qwen3-cc, jax, maxtext, remat, offload, xla-flags, unexplored]
model: qwen3_cc
lane: jax
created: 2026-06-02
updated: 2026-06-02
---

# Retrospective #5 — MaxText config delta: the unexplored optimizations

A **focused** retrospective (not a lane re-read — [#4](2026-06-02-qwen3_cc-jax-retrospective-4.md) did that)
that diffs our v035 frontier against MaxText's **exact** qwen3-8b reference-run config
(`benchmarks/maxtext_trillium_model_configs.py::qwen3_8b_8192_ref` + `benchmarks/xla_flags_library.py`).
**It overturns the "remaining gap is out-of-scope kernel-authoring" conclusion** — there are concrete,
in-scope optimizations MaxText uses that we **never tried, or tried wrong**.

## The headline error — we offloaded the WRONG tensors (v036)

MaxText's reference `remat_policy: "custom"` offload set:

| tensor | MaxText | our v036 | note |
|--------|---------|----------|------|
| `decoder_layer_input` (residual stream into each layer) | **offload → host** | **not offloaded** (recomputed) | MaxText's key checkpoint boundary; one contiguous tensor/layer |
| `query_proj` / `key_proj` / `value_proj` / `out_proj` | **offload → host** | offload → host | matched |
| `mlpwi` (gate+up, `[B,L,12288]`) | **remat (recompute on device)** | **offload → host** | ⚠️ **we did the OPPOSITE** |

So v036 shipped the **giant MLP activations** to host (massive non-overlapped DMA) and **missed the
`decoder_layer_input` offload** — the two most important tensors, both backwards. That is almost certainly
why v036 regressed −18.6%, NOT "our offload can't pipeline." **The offload lever was mis-tested, not refuted.**

## The missing XLA flags

Our v035 frontier `LIBTPU_INIT_ARGS` = scoped_vmem(98304) + 7 scheduler + 4 async-collective-fusion. MaxText
uses a **superset**. Flags MaxText has that we DON'T (and that are not previously-refuted/crashing):

- **`HOST_OFFLOAD_FLAGS` extras** (the offload-pipelining ones — directly relevant to scan+offload):
  `--xla_tpu_aggressive_opt_barrier_removal=ENABLED`, `--xla_lhs_prioritize_async_depth_over_stall=ENABLED`,
  **`--xla_should_allow_loop_variant_parameter_in_chain=ENABLED`**, **`--xla_should_add_loop_invariant_op_in_chain=ENABLED`**.
  The last two are explicitly for **host offload inside loops** — i.e., making the offload pipeline across
  `lax.scan` iterations. This is the exact mechanism I hypothesized we lacked.
- **`LAYOUT_FOR_ALL_REDUCE_SCATTER`** (3): `--xla_tpu_use_minor_sharding_for_major_trivial_input=true`,
  `--xla_tpu_relayout_group_size_threshold_for_reduce_scatter=1`, `--xla_tpu_assign_all_reduce_scatter_layout=true`.
- **`DATA_PARALLEL_OVERLAP`** (2): `--xla_tpu_enable_data_parallel_all_reduce_opt=true`,
  `--xla_tpu_data_parallel_opt_different_sized_ops=true`.
- **`CF_FOR_ALL_GATHER` extras**: `--xla_tpu_overlap_compute_collective_tc=true`, `--xla_enable_async_all_gather=true`.

Flags MaxText uses that we should NOT blindly copy:
- `DISABLE_COLLECTIVE_MATMUL` = `--xla_jf_spmd_threshold_for_windowed_einsum_mib=1000000` — **crashes our libtpu
  build** (v019). MaxText disables collective/windowed-einsum matmul (→ full-size local matmul tiles, plausibly
  the MXU 61% vs our 54%). Needs an alternate flag name for our build, or it's a build-version wall.
- `ENABLE_SPARSECORE_OFFLOADING_FOR_ALL_REDUCE` — we **refuted SparseCore offload** (v003/v017); this is the
  all-reduce variant. Low prior; defer.

## Other deltas

- **Splash blocks**: MaxText uses `sa_block_kv = 2048` (and all dkv/dq blocks 2048); we use **bkv=1024**. We
  swept blocks pre-CE (v021/v022, neutral) but never the exact MaxText all-2048 set at the maxtext-CE frontier.
- vmem 98304 — **matched**. `fused_qkv`/`fused_mlp` False — matched. scan — matched. attention=flash/splash — matched.

## Recommended next directions (ranked, RESUMING the loop)

| # | Direction | Topic | Gain | Conf | Effort | Source |
|---|---|---|---|---|---|---|
| 1 | **Correct offload set** = MaxText's exact recipe (offload decoder_layer_input + q/k/v/o proj; **recompute** mlpwi) + the offload-pipelining flags (loop_variant/invariant, opt_barrier_removal) | remat/offload | up to ~13% (the whole residual) | medium-high | M (model-code: tag decoder_layer_input, fix offload names) + flags | local-gap: MaxText config exact |
| 2 | **Add the missing safe XLA flags** to the v035 frontier (LAYOUT_RS + DATA_PARALLEL_OVERLAP + CF extras + HOST_OFFLOAD extras), NO offload, NO code change | libtpu-flags | +1-3% | medium | S (flag-only) | local-gap: MaxText flag superset |
| 3 | **Splash bkv 1024→2048** (MaxText's value) at the maxtext-CE frontier | splash | +0-2% | low-medium | S | local-gap: MaxText sa_block_kv |
| 4 | Find a working `DISABLE_COLLECTIVE_MATMUL` flag for our build (the MXU 54%→61% candidate) | libtpu-flags/MXU | +2-4% | low | S-M | local-gap; v019 flag crashed |

**This RE-OPENS the offload lever (#1) and the MXU question (#4) that #4/the closing analysis had marked
out-of-scope.** Plan: dispatch #2 (cheap flags-only probe) immediately; implement #1 (the real offload-recipe
fix) in parallel; then #3/#4.

## Anti-recommendations (unchanged)

named-offload **as v036 tagged it** (mlpwi-offloaded) — refuted, but that was the wrong tensor set (see above).
maxtext-CE/scan @ seq2048 (seq-specific). SparseCore (v003/v017) — but the all-reduce-specific flag is untested.

## Sources

- `maxtext-tpu-recipes-v0.1.4/benchmarks/maxtext_trillium_model_configs.py` (qwen3_8b_8192_ref / _2048_ref)
- `maxtext-tpu-recipes-v0.1.4/benchmarks/xla_flags_library.py` + `MaxText/configs/base.yml` (remat custom tensor list)
- [retrospective #4](2026-06-02-qwen3_cc-jax-retrospective-4.md), [maxtext-CE climb](2026-06-02-qwen3-cc-jax-maxtext-ce-climb.md), [v036](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v036-maxtext-ce-offload-s8k-bs3.md), [sharding-matches-maxtext](../observations/qwen3-jax-sharding-matches-maxtext.md)

## See also

- [Qwen3 8B — jax](../models/qwen3-cc-jax.md) · retrospectives [#4](2026-06-02-qwen3_cc-jax-retrospective-4.md)
