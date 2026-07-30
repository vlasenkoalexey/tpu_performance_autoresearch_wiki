"""Paged-attention decode spec (6p family layout).

Inputs: (queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens) with
queries (num_seqs, Hq, D), pages (total_pages, page_size, Hkv, D), one query
token per sequence, sequence i owning pages [i*pages_per_seq, (i+1)*pps).
Output: (num_seqs, Hq, D).

Probes (derived from the campaign 6p/7p verifier batteries — probe A/C in
verify_7p_v004/battery3_probes.py):
  - GQA group isolation: perturb one KV head's V pages of sequence 0 — only
    that head's q-head group in sequence 0's output row may change; catches
    the group-aliasing class (rerun_lane_6p cand_v003).
  - per-sequence isolation: perturb every V page of one sequence — only that
    sequence's output row may change.
  - invalid-token no-leak: with shortened kv_lens as the base point, corrupt
    all K/V tokens at positions >= kv_len — NOTHING may change (attention
    weights of masked positions are exactly zero in the reference semantics).
"""
from __future__ import annotations

import numpy as np

POWER_THRESHOLD = 1e-3
SCALE_INPUT = 1  # k_pages

HEAD_SPIKE = 0.5
# K perturbations MUST vary across key positions: a constant added to every
# K row shifts all logits of a query equally and softmax is shift-invariant
# (zero power — verified empirically on the 6p baseline). Use seeded noise.
K_NOISE_SCALE = 2.0
PROBED_KV_HEAD = 3
ISOLATED_SEQ = 5
NOLEAK_LENS = (4096, 2048, 1000, 300, 64, 16, 1)
CORRUPT_VALUE = 50.0


def _cfg(baseline_module):
    cfg = baseline_module.CONFIG
    return (int(cfg["num_seqs"]), int(cfg["num_query_heads"]),
            int(cfg["num_kv_heads"]), int(cfg["head_dim"]),
            int(cfg["page_size"]), int(cfg["pages_per_seq"]))


def perturb_regions(baseline_module, inputs):
    import jax.numpy as jnp
    queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens = inputs
    num_seqs, Hq, Hkv, D, page_size, pps = _cfg(baseline_module)
    G = Hq // Hkv
    out_shape = (num_seqs, Hq, D)
    probes = []

    # --- GQA group isolation on sequence 0 ---
    # BOTH a V-side and a K-side probe are required: when G == Hkv a
    # (group, kv-head) axis transposition maps the V of head h onto exactly
    # the q-head block [h*G,(h+1)*G) again, so the V probe alone cannot see
    # the aliasing (observed on the rerun_lane_6p cand_v003 fixture). The
    # K-side probe breaks the symmetry: under the transposition, kv-head h's
    # attention weights land in q-heads {g*Hkv + h}, not [h*G,(h+1)*G).
    h = PROBED_KV_HEAD
    v2 = v_pages.at[0:pps, :, h, :].add(HEAD_SPIKE)
    mask = np.zeros(out_shape, dtype=bool)
    mask[0, h * G:(h + 1) * G, :] = True
    probes.append({
        "name": "gqa: v kvhead[%d] seq0 -> qheads[%d:%d]" % (h, h * G, (h + 1) * G),
        "inputs": (queries, k_pages, v2, kv_lens, page_indices, cu_q_lens),
        "affected_mask": mask,
    })
    rng = np.random.default_rng(0)
    k_noise = jnp.asarray(
        rng.standard_normal((pps,) + k_pages.shape[1:2] + (D,)) * K_NOISE_SCALE
    ).astype(k_pages.dtype)
    k2 = k_pages.at[0:pps, :, h, :].add(k_noise)
    mask = np.zeros(out_shape, dtype=bool)
    mask[0, h * G:(h + 1) * G, :] = True
    probes.append({
        "name": "gqa: k kvhead[%d] seq0 -> qheads[%d:%d]" % (h, h * G, (h + 1) * G),
        "inputs": (queries, k2, v_pages, kv_lens, page_indices, cu_q_lens),
        "affected_mask": mask,
    })

    # --- per-sequence isolation ---
    s = ISOLATED_SEQ
    v3 = v_pages.at[s * pps:(s + 1) * pps].add(HEAD_SPIKE)
    mask = np.zeros(out_shape, dtype=bool)
    mask[s] = True
    probes.append({
        "name": "seq-isolation: v pages of seq[%d]" % s,
        "inputs": (queries, k_pages, v3, kv_lens, page_indices, cu_q_lens),
        "affected_mask": mask,
    })

    # --- invalid-token no-leak (base point uses shortened kv_lens) ---
    lens = [NOLEAK_LENS[i] if i < len(NOLEAK_LENS) else int(kv_lens[i])
            for i in range(num_seqs)]
    short_lens = jnp.asarray(lens, jnp.int32)
    base_inputs = (queries, k_pages, v_pages, short_lens, page_indices, cu_q_lens)

    token_pos = np.arange(pps * page_size).reshape(pps, page_size)  # per-seq positions
    k_np = np.asarray(k_pages).astype(np.float32)
    v_np = np.asarray(v_pages).astype(np.float32)
    for i, L in enumerate(lens):
        if L >= pps * page_size:
            continue
        invalid = token_pos >= L  # (pps, page_size)
        base = i * pps
        k_np[base:base + pps][invalid] = CORRUPT_VALUE
        v_np[base:base + pps][invalid] = -CORRUPT_VALUE
    k_corrupt = jnp.asarray(k_np).astype(k_pages.dtype)
    v_corrupt = jnp.asarray(v_np).astype(v_pages.dtype)
    probes.append({
        "name": "no-leak: corrupt tokens >= kv_len",
        "base_inputs": base_inputs,
        "inputs": (queries, k_corrupt, v_corrupt, short_lens, page_indices, cu_q_lens),
        "affected_mask": np.zeros(out_shape, dtype=bool),
    })
    return probes
