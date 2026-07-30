"""Causal per-k-block V-sensitivity spec.

Derived from the campaign verifier batteries (v5p_verify/t3_coverage.py,
v037vrf/coverage.py): perturb V rows in k-block j — every query position
>= the block start must respond, every query position < the block start must
be BIT-IDENTICAL (in exact arithmetic a masked-out V row has softmax weight
exactly 0.0, so the unaffected side is exact, not approximate).

Applies to causal attention families whose first three inputs are q, k, v
with sequence on axis -2 and output shaped like q:
  (B, H, S, D)  — 1p Flash Attention, 5p Flex Attention (extra bias inputs
                  after v are passed through untouched)
  (H, S, D)     — 4p Sparse/GQA Attention (Hkv may differ from Hq)

Catches: skipped k-blocks (50%-coverage class), wrong-side causal reads,
off-by-one block boundary handling.
"""
from __future__ import annotations

import numpy as np

POWER_THRESHOLD = 1e-3
SCALE_INPUT = 1  # K — parity scale probes sharpen softmax conditioning

N_BLOCKS = 8
BLOCK_SPIKE = 0.5
COLUMN_SPIKE = 20.0


def _seq_len(baseline_module, q):
    cfg = getattr(baseline_module, "CONFIG", {})
    return int(cfg.get("seq_len", q.shape[-2]))


def perturb_regions(baseline_module, inputs):
    q, k, v = inputs[0], inputs[1], inputs[2]
    rest = tuple(inputs[3:])
    S = _seq_len(baseline_module, q)
    out_shape = tuple(q.shape)
    seq_axis = len(out_shape) - 2

    def affected_from(pos: int):
        mask = np.zeros(out_shape, dtype=bool)
        idx = [slice(None)] * len(out_shape)
        idx[seq_axis] = slice(pos, None)
        mask[tuple(idx)] = True
        return mask

    probes = []
    blk = S // N_BLOCKS
    for j in range(N_BLOCKS):
        v2 = v.at[..., j * blk:(j + 1) * blk, :].add(BLOCK_SPIKE)
        probes.append({
            "name": "vblock[%d:%d]" % (j * blk, (j + 1) * blk),
            "inputs": (q, k, v2) + rest,
            "affected_mask": affected_from(j * blk),
        })

    for c in (0, S // 2 - 1, S // 2, S - 1):
        v2 = v.at[..., c, :].add(COLUMN_SPIKE)
        probes.append({
            "name": "vcol[%d]" % c,
            "inputs": (q, k, v2) + rest,
            "affected_mask": affected_from(c),
        })
    return probes
