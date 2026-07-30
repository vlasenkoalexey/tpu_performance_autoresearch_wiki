# KernelGate regression fixture — copied verbatim from:
#   /mnt/disks/persist/torch-tpu/rerun_lane_4p/benchmark/jaxbench-nopeek/4p_Sparse_Attention/v013/cand_1.py
# KNOWN-BAD (semantics class): applies sm_scale = D**-0.5 inside the kernel although this family's baseline already pre-scales q in create_inputs — double scaling. MUST FAIL the parity gate.
# Do not edit: this file is a pinned reproduction of campaign history.
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu
import functools
import time
import numpy as np
import math

def flash_attn_kernel_sparse(
    grid_mapping,
    q_ref, k_ref, v_ref, mask_ref, o_ref,
    acc_ref, max_ref, sum_ref,
    *, bq: int, bk: int, bd: int, sm_scale: float
):
    h = pl.program_id(0)
    block_idx = pl.program_id(1)
    
    q_idx = grid_mapping[block_idx, 0]
    k_idx = grid_mapping[block_idx, 1]
    
    @pl.when(k_idx == 0)
    def _():
        acc_ref[...] = jnp.zeros_like(acc_ref)
        max_ref[...] = jnp.full_like(max_ref, -jnp.inf)
        sum_ref[...] = jnp.zeros_like(sum_ref)

    k_max_seq = (k_idx + 1) * bk - 1
    q_min_seq = q_idx * bq
    q_max_seq = (q_idx + 1) * bq - 1
    k_min_seq = k_idx * bk

    is_fully_visible = k_max_seq < q_min_seq
    is_partially_visible = (k_min_seq <= q_max_seq) & (~is_fully_visible)

    q_block = jnp.squeeze(q_ref[...], axis=0)
    k_block = jnp.squeeze(k_ref[...], axis=0)
    v_block = jnp.squeeze(v_ref[...], axis=0)

    qk = jnp.dot(q_block, k_block.T, preferred_element_type=jnp.float32) * sm_scale

    @pl.when(is_fully_visible)
    def _():
        new_max = jnp.maximum(max_ref[...], jnp.max(qk, axis=1, keepdims=True))
        scale = jnp.exp(max_ref[...] - new_max)
        sum_ref[...] = sum_ref[...] * scale
        acc_ref[...] = acc_ref[...] * scale
        max_ref[...] = new_max

        exp_qk = jnp.exp(qk - new_max)
        sum_ref[...] += jnp.sum(exp_qk, axis=1, keepdims=True)
        acc_ref[...] += jnp.dot(exp_qk.astype(v_block.dtype), v_block, preferred_element_type=jnp.float32)

    @pl.when(is_partially_visible)
    def _():
        mask_block = jnp.squeeze(mask_ref[...], axis=0)
        qk_masked = qk + mask_block

        new_max = jnp.maximum(max_ref[...], jnp.max(qk_masked, axis=1, keepdims=True))
        scale = jnp.exp(max_ref[...] - new_max)
        sum_ref[...] = sum_ref[...] * scale
        acc_ref[...] = acc_ref[...] * scale
        max_ref[...] = new_max

        exp_qk = jnp.exp(qk_masked - new_max)
        # Avoid adding small exp values from -1e30
        exp_qk = jnp.where(mask_block == 0.0, exp_qk, 0.0)
        sum_ref[...] += jnp.sum(exp_qk, axis=1, keepdims=True)
        acc_ref[...] += jnp.dot(exp_qk.astype(v_block.dtype), v_block, preferred_element_type=jnp.float32)

    last_k_idx = (q_idx * bq + bq - 1) // bk
    @pl.when(k_idx == last_k_idx)
    def _():
        out = acc_ref[...] / sum_ref[...]
        o_ref[...] = jnp.expand_dims(out.astype(o_ref.dtype), axis=0)

@functools.partial(jax.jit, static_argnames=['bq', 'bk'])
def flash_attn_forward_sparse(q, k, v, bq=1024, bk=256):
    H_q, S, D = q.shape
    H_kv = k.shape[0]
    num_q_per_kv = H_q // H_kv
    sm_scale = 1.0 / math.sqrt(D)
    
    N_q = S // bq
    N_k = S // bk
    
    # Precompute causal masks for the partially visible blocks
    # shift = ki * bk - qi * bq. Since ki goes from qi * bq // bk to (qi+1)*bq//bk - 1,
    # the relative ki is exactly ki % (bq // bk).
    num_shifts = bq // bk
    shifts = jnp.arange(num_shifts) * bk
    row_idx = jnp.arange(bq)[:, None]
    col_idx = shifts[:, None, None] + jnp.arange(bk)[None, :]
    masks = col_idx <= row_idx
    masks_f32 = jnp.where(masks, 0.0, -1e30).astype(jnp.float32)
    
    grid_list = []
    for qi in range(N_q):
        last_k = (qi * bq + bq - 1) // bk
        for ki in range(last_k + 1):
            grid_list.append([qi, ki])
    grid_mapping = jnp.array(grid_list, dtype=jnp.int32)
    num_live_blocks = len(grid_list)

    grid_spec = pltpu.PrefetchScalarGridSpec(
        num_scalar_prefetch=1,
        grid=(H_q, num_live_blocks),
        in_specs=[
            pl.BlockSpec((1, bq, D), lambda h, b_idx, gmap: (h, gmap[b_idx, 0], 0)), # q
            pl.BlockSpec((1, bk, D), lambda h, b_idx, gmap: (h // num_q_per_kv, gmap[b_idx, 1], 0)), # k
            pl.BlockSpec((1, bk, D), lambda h, b_idx, gmap: (h // num_q_per_kv, gmap[b_idx, 1], 0)), # v
            pl.BlockSpec((1, bq, bk), lambda h, b_idx, gmap: (gmap[b_idx, 1] % num_shifts, 0, 0)), # mask
        ],
        out_specs=pl.BlockSpec((1, bq, D), lambda h, b_idx, gmap: (h, gmap[b_idx, 0], 0)), # out
        scratch_shapes=[
            pltpu.VMEM((bq, D), jnp.float32),
            pltpu.VMEM((bq, 1), jnp.float32),
            pltpu.VMEM((bq, 1), jnp.float32),
        ]
    )

    out = pl.pallas_call(
        functools.partial(flash_attn_kernel_sparse, bq=bq, bk=bk, bd=D, sm_scale=sm_scale),
        grid_spec=grid_spec,
        out_shape=jax.ShapeDtypeStruct((H_q, S, D), q.dtype)
    )(grid_mapping, q, k, v, masks_f32)
    return out

def bench(fn, *args, warmup=5, iters=50):
    for _ in range(warmup):
        jax.block_until_ready(fn(*args))
    ts = []
    for _ in range(iters):
        t0 = time.perf_counter()
        jax.block_until_ready(fn(*args))
        ts.append((time.perf_counter() - t0) * 1e3)
    a = np.array(ts)
    print(f"p50={np.percentile(a, 50):.3f}ms std={a.std():.3f} min={a.min():.3f} n={iters}")
    return float(np.percentile(a, 50))

if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from baseline import create_inputs, workload as naive_workload, CONFIG
    
    q, k, v = create_inputs(jnp.bfloat16)
    q_f32, k_f32, v_f32 = jax.tree.map(lambda x: x.astype(jnp.float32), (q, k, v))
    
    print("\nBenchmarking naive baseline:")
    naive_ms = bench(jax.jit(naive_workload), q, k, v)
    print(f"Naive p50 = {naive_ms:.3f} ms")
    
    configs = [
        (1024, 256),
        (512, 256),
        (256, 256),
    ]
    
    for bq, bk in configs:
        print(f"\nBenchmarking cand bq={bq}, bk={bk}:")
        try:
            fn = jax.jit(functools.partial(flash_attn_forward_sparse, bq=bq, bk=bk))
            cand_ms = bench(fn, q, k, v)
            print(f"Speedup: {naive_ms / cand_ms:.2f}x")
            print(f"RESULT_TIME_MS: {cand_ms:.3f}")
        except Exception as e:
            print(f"Failed: {e}")
