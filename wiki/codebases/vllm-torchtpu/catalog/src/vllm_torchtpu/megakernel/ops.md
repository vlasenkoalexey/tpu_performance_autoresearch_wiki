---
title: 'Module: src/vllm_torchtpu/megakernel/ops.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/megakernel/ops.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.megakernel.ops`/
symbols:
  BF16: BF16.
  FP8: FP8.
  I32: I32.
  rup: rup().
  F32: F32.
  U32: U32.
  rnd: rnd().
  bswitch.rec: bswitch().rec().
  rmsnorm: rmsnorm().
  bswitch: bswitch().
  rms_zc: rms_zc().
  silu_mul: silu_mul().
  rope_partial: rope_partial().
  scope_fn: scope_fn().
---
# Module: [`src/vllm_torchtpu/megakernel/ops.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py)

## Functions
- <a id="bswitch"></a>`bswitch(idx: jax.Array, fns: list)` — [`L41`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L41) — Balanced binary tree of `lax.cond` (O(log N) select depth).
- <a id="bswitch.rec"></a>`rec(lo: int, hi: int)` — [`L46`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L46)
- <a id="rms_zc"></a>`rms_zc(x: jax.Array, w: jax.Array, eps: float = 0.000001)` — [`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L68) — Zero-centered RMSNorm (`1.0 + w`) with BF16 intermediate rounding.
- <a id="rmsnorm"></a>`rmsnorm(x: jax.Array, w: jax.Array, eps: float = 0.000001, *, zero_centered: bool = False)` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L55) — RMSNorm in float32 with BF16 rounding (`1.0 + w` if `zero_centered`).
- <a id="rnd"></a>`rnd(x: jax.Array)` — [`L36`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L36) — Round float32 tensor through bfloat16 back to float32.
- <a id="rope_partial"></a>`rope_partial(x: jax.Array, cos: jax.Array, sin: jax.Array, rot_dim: int)` — [`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L73) — Partial rotary positional embedding on the leading `rot_dim` columns.
- <a id="rup"></a>`rup(n: int, k: int)` — [`L31`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L31) — Round `n` up to the next multiple of `k`.
- <a id="scope_fn"></a>`scope_fn(enabled: bool)` — [`L94`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L94) — Return a context manager factory for `jax.named_scope` when `enabled=True`.
- <a id="silu_mul"></a>`silu_mul(gate: jax.Array, up: jax.Array)` — [`L89`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L89) — SwiGLU activation `silu(gate) * up` rounded to BF16.

## Module values
- <a id="BF16"></a>`BF16` — [`L24`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L24) — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="F32"></a>`F32` — [`L25`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L25)
- <a id="FP8"></a>`FP8` — [`L28`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L28) — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="I32"></a>`I32` — [`L26`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L26) — documented in [megakernel](../../../../concepts/megakernel.md)
- <a id="U32"></a>`U32` — [`L27`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/megakernel/ops.py#L27)

