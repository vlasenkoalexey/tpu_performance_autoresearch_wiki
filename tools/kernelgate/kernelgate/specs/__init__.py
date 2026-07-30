"""Shipped coverage specs for the attention benchmark families.

Each spec is a problem-family-specific module implementing:
    perturb_regions(baseline_module, inputs) -> list of probe dicts
and optionally POWER_THRESHOLD / SCALE_INPUT (see kgate.coverage docstring).

Shipped:
    causal_blocks    per-k-block + boundary-column causal sensitivity for
                     MHA/GQA layouts with q,k,v as the first three inputs
                     ((B,H,S,D) or (H,S,D); families 1p/4p/5p)
    gqa_isolation    GQA group isolation for (Hq,S,D) q + (Hkv,S,D) k/v (4p)
    paged_attention  paged decode: GQA isolation + per-seq isolation +
                     invalid-token no-leak (6p)
"""
