# KernelGate regression fixture — copied verbatim from:
#   /mnt/disks/persist/torch-tpu/rerun_lane_4p/benchmark/jaxbench-nopeek/4p_Sparse_Attention/v002/cand_1.py
# KNOWN-BAD (coverage class): writes the output block when k_idx == q_idx, but q/k block indices are in different units (bq=1024 vs bk=256), so accumulation is cut short — the 50%-coverage failure class. MUST FAIL parity and coverage gates.
# Do not edit: this file is a pinned reproduction of campaign history.
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu
import functools
import math

def flash_attn_kernel_sparse(
    grid_mapping,
    q_ref, k_ref, v_ref, o_ref,
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

    q_block = jnp.squeeze(q_ref[...], axis=0)
    k_block = jnp.squeeze(k_ref[...], axis=0)
    v_block = jnp.squeeze(v_ref[...], axis=0)

    qk = jnp.dot(q_block, k_block.T, preferred_element_type=jnp.float32) * sm_scale

    @pl.when(k_idx < q_idx)
    def _():
        # Unmasked block (fully visible)
        new_max = jnp.maximum(max_ref[...], jnp.max(qk, axis=1, keepdims=True))
        
        scale = jnp.exp(max_ref[...] - new_max)
        sum_ref[...] = sum_ref[...] * scale
        acc_ref[...] = acc_ref[...] * scale
        max_ref[...] = new_max

        exp_qk = jnp.exp(qk - new_max)
        sum_ref[...] += jnp.sum(exp_qk, axis=1, keepdims=True)
        
        exp_qk_bf16 = exp_qk.astype(v_block.dtype)
        acc_ref[...] += jnp.dot(exp_qk_bf16, v_block, preferred_element_type=jnp.float32)

    @pl.when(k_idx == q_idx)
    def _():
        # Masked diagonal block
        row_idx = q_idx * bq + jnp.arange(bq)[:, None]
        col_idx = k_idx * bk + jnp.arange(bk)[None, :]
        mask = col_idx <= row_idx
        
        qk_masked = jnp.where(mask, qk, -1e30)

        new_max = jnp.maximum(max_ref[...], jnp.max(qk_masked, axis=1, keepdims=True))
        
        scale = jnp.exp(max_ref[...] - new_max)
        sum_ref[...] = sum_ref[...] * scale
        acc_ref[...] = acc_ref[...] * scale
        max_ref[...] = new_max

        exp_qk = jnp.exp(qk_masked - new_max)
        exp_qk = jnp.where(mask, exp_qk, 0.0)
        sum_ref[...] += jnp.sum(exp_qk, axis=1, keepdims=True)
        
        exp_qk_bf16 = exp_qk.astype(v_block.dtype)
        acc_ref[...] += jnp.dot(exp_qk_bf16, v_block, preferred_element_type=jnp.float32)

    @pl.when(k_idx == q_idx)
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
    
    # Generate causal mapping: (q_idx, k_idx) pairs where k_idx <= q_idx
    grid_list = []
    for qi in range(N_q):
        for ki in range(qi + 1):
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
        ],
        out_specs=pl.BlockSpec((1, bq, D), lambda h, b_idx, gmap: (h, gmap[b_idx, 0], 0)), # out
        scratch_shapes=[
            pltpu.VMEM((bq, D), jnp.float32), # acc
            pltpu.VMEM((bq, 1), jnp.float32), # max
            pltpu.VMEM((bq, 1), jnp.float32), # sum
        ]
    )

    out = pl.pallas_call(
        functools.partial(flash_attn_kernel_sparse, bq=bq, bk=bk, bd=D, sm_scale=sm_scale),
        grid_spec=grid_spec,
        out_shape=jax.ShapeDtypeStruct((H_q, S, D), q.dtype)
    )(grid_mapping, q, k, v)
    return out
