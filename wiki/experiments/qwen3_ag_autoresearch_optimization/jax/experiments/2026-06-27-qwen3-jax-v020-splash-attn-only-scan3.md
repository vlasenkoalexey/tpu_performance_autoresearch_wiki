---
title: "v020 — Qwen3 8B jax: baseline scan recovery"
type: experiment
tags: [qwen3, jax, v6e-8, scan, remat]
variant: 8B/v6e-8
hypothesis: "By removing the OOM-causing custom Pallas GLU backward kernels and replacing the memory-inefficient top-level jax.checkpoint with nnx.scan over Qwen3DecoderLayer along with per-layer nnx.remat, we can recover compilation stability and baseline performance."
commit: TBD
status: complete
verdict: confirmed
---

# v020 — Qwen3 8B jax: baseline scan recovery

## Hypothesis under test
**Hypothesis**: By removing the OOM-causing custom Pallas GLU backward kernels and replacing the memory-inefficient top-level `jax.checkpoint` with `nnx.scan` over `Qwen3DecoderLayer` along with per-layer `nnx.remat`, we can recover compilation stability and baseline performance.
**Mechanism**:
1. Reverted `fused_glu.py` usages in `modeling_qwen3.py`.
2. Replaced `self.layers = nnx.data([...])` with a custom `Qwen3ScannedLayers` module that applies `nnx.scan` and `nnx.remat` over the layer array.
3. Removed `jax.checkpoint(loss_fn)` in `train.py` and updated `sharding.py` to target `model.scanned_layers.layers.*` with an explicit `None` dimension for the scanned axis.
**Predicted signal**: The experiment should successfully compile without RESOURCE_EXHAUSTED and achieve the ~32.5% MFU baseline from `v011`.
**Falsification criterion**: If the workload crashes during compilation or MFU drops below 32%.

## Results
- **Headline metric**: 32.3% MFU (45,019 tok/s, 1455ms step time)
- **Details**:
  - The model compiled successfully within the 31.25 GB HBM limit.
  - Optimizer initialization (AdamW) succeeded.
  - The model achieved 32.3% MFU on v6e-8 at `seqlen=8192` with `global_batch=8`.

## Verdict
- **Reasoning**: The hypothesis is confirmed. By falling back to native `nnx.scan` and `nnx.remat`, we recovered the 32.3% MFU baseline without encountering HLO compile or runtime buffer OOMs. However, this does not yet reach the target 35% MFU. Further architectural optimizations are required.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
