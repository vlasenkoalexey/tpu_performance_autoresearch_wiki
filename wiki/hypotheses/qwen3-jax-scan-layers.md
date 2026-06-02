---
title: "Qwen3 jax — scan-over-layers"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: open
expected_gain: "compile-HBM ↓; MFU neutral-to-small; may enable denser shapes"
confidence: low
effort: M
origin: 2026-06-02-v021-splash-bq1024
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 jax — scan-over-layers

The model currently runs a **Python for-loop over 36 transformer layers** (unrolled into the HLO).
Replacing it with `nnx.scan` (a single scanned layer body over a stacked-param leading axis) is the
structural lever the llama3-jax sibling used. It cuts compile time and compile-time HBM, and can let
XLA schedule a tighter steady-state loop.

## Statement

Converting the layer stack to `nnx.scan` preserves loss (semantics-exact) and either improves MFU on
the v018 frontier or enables a denser shape (e.g. bs>4 at seq2048, or bs>1 at seq8192) that the
unrolled graph couldn't compile — net frontier gain ≥ +1 pp or a new feasible variant.

## Rationale

- **Category match**: qwen3-jax has shown that *compiler/structural* levers transfer from llama3-jax
  (XLA scheduler flags +3.4 pp / v018) while *kernel-swap* levers do not (tokamax-splash −8.5% / v020,
  SparseCore-offload refuted). scan is structural → in the transferable category.
- Unrolled 36-layer graph is large; scan shrinks the compiled program and reduces live activation
  ranges, which the v018 memory-pressure-aware scheduler may exploit.
- llama3-jax used scan as part of its 43.3% stack.

## Proposed experiment

Code change via `/edit-model-code`: wrap the decoder layer stack in `nnx.scan` (stack per-layer params
on a new leading axis; share the scanned body). Re-run the CPU equivalence test (`test_equivalence.py`)
to confirm loss/grad parity BEFORE TPU dispatch. Build a tagged image FROM the splash image, smoke-test
`--help`, dispatch on the v018 frontier shape. Measure MFU + compile time + loss parity; also probe
whether it unlocks a denser shape.

## Risks

- nnx.scan requires homogeneous layers + stacked params — a real refactor; correctness risk (must pass
  the equivalence test, else `invalid`).
- MFU upside is uncertain (scan is often compile-time-only); the win may be "enables a shape" not "+MFU".

## Dependencies

Trainer/model edit + image build + equivalence re-verification.
