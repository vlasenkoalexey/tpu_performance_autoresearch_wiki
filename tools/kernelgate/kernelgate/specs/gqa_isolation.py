"""GQA group-isolation spec for the (Hq, S, D) / (Hkv, S, D) layout (4p family).

Perturbing one KV head's K or V may only move the q heads in its group
(qh // G == kv head, G = Hq // Hkv); every other q head reads different KV
heads entirely, so its output must be BIT-IDENTICAL. Catches group-index
aliasing (a q head attending the wrong KV head) and broadcast/repeat-order
bugs that loose atol parity misses.
"""
from __future__ import annotations

import numpy as np

POWER_THRESHOLD = 1e-3
SCALE_INPUT = 1

HEAD_SPIKE = 0.5
# K perturbations MUST vary across key positions: a constant added to every
# K row shifts all logits of a query equally and softmax is shift-invariant
# (zero probe power). Seeded per-position noise instead.
K_NOISE_SCALE = 2.0
PROBED_KV_HEADS = (0, 3)


def perturb_regions(baseline_module, inputs):
    q, k, v = inputs[0], inputs[1], inputs[2]
    rest = tuple(inputs[3:])
    cfg = getattr(baseline_module, "CONFIG", {})
    Hq = int(cfg.get("num_query_heads", q.shape[0]))
    Hkv = int(cfg.get("num_kv_heads", k.shape[0]))
    G = Hq // Hkv
    out_shape = tuple(q.shape)

    def group_mask(h: int):
        mask = np.zeros(out_shape, dtype=bool)
        mask[h * G:(h + 1) * G] = True
        return mask

    probes = []
    for h in PROBED_KV_HEADS:
        v2 = v.at[h].add(HEAD_SPIKE)
        probes.append({
            "name": "v_kvhead[%d] -> qheads[%d:%d]" % (h, h * G, (h + 1) * G),
            "inputs": (q, k, v2) + rest,
            "affected_mask": group_mask(h),
        })
        import jax.numpy as jnp
        rng = np.random.default_rng(h)
        k_noise = jnp.asarray(rng.standard_normal(k.shape[1:]) * K_NOISE_SCALE
                              ).astype(k.dtype)
        k2 = k.at[h].add(k_noise)
        probes.append({
            "name": "k_kvhead[%d] -> qheads[%d:%d]" % (h, h * G, (h + 1) * G),
            "inputs": (q, k2, v) + rest,
            "affected_mask": group_mask(h),
        })
    return probes
