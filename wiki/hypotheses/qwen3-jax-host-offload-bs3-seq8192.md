---
title: "Qwen3 jax — host-offload of decoder-input + projections to fit bs3 @ seq8192"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: open
expected_gain: "+20-30% tok/s/chip @ seq8192 (close the gap to MaxText 6,942)"
confidence: medium-high
effort: M
origin: 2026-06-02-maxtext-qwen3-8b-v6e8-ref-seq8192
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 jax — host-offload to fit bs3 @ seq8192

The MaxText reference run proved the **achievable seq8192 ceiling is 45.3% MFU / 6,942 tok/s/chip** —
**+31% tok/s/chip** over our jax frontier (v009, 30.4% / 5,305, bs1). The decisive lever MaxText uses and
the jax lane never tried: **host-DRAM offload of the decoder-layer input + the QKV/out projections**
(`decoder_layer_input=offload` + `out/query/key/value_proj=offload`, with `remat_policy=custom`), which
frees enough HBM to fit **bs3 at seq8192**. Our jax lane was stuck at bs1 there (remat alone insufficient;
tokamax-CE enabled bs2 but didn't raise throughput — [v016](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v016-s8k-ce-bs2.md)).

## Statement

Adding MaxText-style host-offload (offload decoder-layer input + the four attention projections to host
DRAM during the forward, recompute/reload on backward) to the jax trainer fits **bs3 (global 24) at
seq8192** and raises tok/s/chip materially above v009's 5,305 — target ≥ +20% (toward the MaxText 6,942
ceiling), with loss parity and no semantic change.

## Rationale

- **Reference proof**: MaxText hits 45.3% @ seq8192 bs3 on the identical architecture/hardware via exactly
  this offload recipe ([reference baseline](../experiments/qwen3_cc_autoresearch_optimization/maxtext/experiments/2026-06-02-maxtext-qwen3-8b-v6e8-ref-seq8192.md)). This is not speculative — it's a measured, transferable lever.
- **Category match**: this is a memory/scheduling (host-offload) lever — the *compiler/runtime* category that
  transfers to qwen3-jax (XLA scheduler flags gave +3.4 pp / v018), unlike kernel-swap levers that regress.
- The jax v018 profile already shows host-offload machinery active (`host_transfer_overlap_limit=24`,
  `copy-start/done` to S(4) host DRAM) — the infra exists; this hypothesis *directs* it at the
  layer-input + projection tensors to unlock the bigger batch, rather than just remat tensors.

## Proposed experiment

Code change (via `/edit-model-code`): add activation/projection host-offload to the jax trainer's decoder
layer (offload the layer input + Q/K/V/out projection activations to host, reload on backward), gated by a
flag; combine with the existing remat. Re-run `test_equivalence.py` for parity, build a tagged image, run
at seq8192 bs2 then bs3. Measure tok/s/chip vs v009 (5,305) and the MaxText ceiling (6,942).

## Risks

- JAX host-offload (`jax.experimental` device_put to host / `Format` memory_kind="pinned_host") is fiddlier
  than MaxText's integrated path; the port may not capture the full benefit. Effort M, possibly L.
- If bs3 still OOMs or the offload overhead isn't repaid, falls back to documenting the residual gap.

## Dependencies

Trainer/model edit + image build + equivalence re-verification. Supersedes the earlier "jax at ceiling"
read for the seq8192 frontier.
