# KernelGate regression fixture — copied verbatim from:
#   /mnt/disks/persist/torch-tpu/rerun_lane_5p/benchmark/work/v005/cand_05.py
# KNOWN-BAD (non-compiling class): pl.load with grid-dependent dynamic slices from ANY-memory refs fails Mosaic lowering on TPU. The harness MUST report FAIL with the traceback, not crash.
# Do not edit: this file is a pinned reproduction of campaign history.
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu
import functools

def flex_attention_kernel(
    q_ref, k_ref, v_ref, bias_ref, # Inputs
    o_ref,                         # Outputs
    *, sm_scale, S, bq, bk, hd
):
    q_idx = pl.program_id(0)
    b_idx = pl.program_id(1)
    h_idx = pl.program_id(2)
    
    q_val = jnp.squeeze(q_ref[...], axis=(0, 1)) * sm_scale
    
    # Initialize accumulators in VMEM registers (not scratch)
    acc_o = jnp.zeros((bq, hd), dtype=jnp.float32)
    acc_m = jnp.full((bq,), -jnp.inf, dtype=jnp.float32)
    acc_l = jnp.zeros((bq,), dtype=jnp.float32)

    def body_fn(k_idx, state):
        acc_o, acc_m, acc_l = state
        
        # Manually load K, V, bias blocks
        k_val = pl.load(k_ref, (b_idx, h_idx, pl.ds(k_idx * bk, bk), pl.ds(0, hd)))
        v_val = pl.load(v_ref, (b_idx, h_idx, pl.ds(k_idx * bk, bk), pl.ds(0, hd)))
        bias_val = pl.load(bias_ref, (h_idx, pl.ds(q_idx * bq, bq), pl.ds(k_idx * bk, bk)))
        
        qk = jnp.dot(q_val, k_val.T, preferred_element_type=jnp.float32)
        qk = qk + bias_val

        # Sub-block causal mask inside the diagonal block
        row_idxs = q_idx * bq + jnp.arange(bq)
        col_idxs = k_idx * bk + jnp.arange(bk)
        mask = row_idxs[:, None] >= col_idxs[None, :]
        qk = jnp.where(mask, qk, -1e30)

        # Update running max
        m_curr = jnp.max(qk, axis=-1)
        m_new = jnp.maximum(acc_m, m_curr)
        
        # Rescale factors
        alpha = jnp.exp(acc_m - m_new)
        beta = jnp.exp(qk - m_new[:, None])
        
        # Update running sum of exponentials
        l_new = acc_l * alpha + jnp.sum(beta, axis=-1)
        
        # Scale current output and add new terms
        acc_o_new = acc_o * alpha[:, None] + jnp.dot(beta.astype(v_val.dtype), v_val, preferred_element_type=jnp.float32)

        return acc_o_new, m_new, l_new

    # Loop over k from 0 to q_idx (inclusive)
    acc_o, acc_m, acc_l = jax.lax.fori_loop(0, q_idx + 1, body_fn, (acc_o, acc_m, acc_l))

    out = acc_o / acc_l[:, None]
    out_expanded = jnp.expand_dims(out, axis=(0, 1))
    o_ref[...] = out_expanded.astype(o_ref.dtype)

@functools.partial(jax.jit, static_argnames=['bq', 'bk', 'interpret'])
def flex_attention_pallas(q, k, v, bias, *, bq=256, bk=256, interpret=False):
    B, H, S, D = q.shape
    num_q = S // bq
    sm_scale = D ** -0.5

    return pl.pallas_call(
        functools.partial(flex_attention_kernel, sm_scale=sm_scale, S=S, bq=bq, bk=bk, hd=D),
        grid=(num_q, B, H),
        in_specs=[
            pl.BlockSpec((1, 1, bq, D), lambda q, b, h: (b, h, q, 0)), # q
            pl.BlockSpec(memory_space=pl.ANY), # k
            pl.BlockSpec(memory_space=pl.ANY), # v
            pl.BlockSpec(memory_space=pl.ANY), # bias
        ],
        out_specs=pl.BlockSpec((1, 1, bq, D), lambda q, b, h: (b, h, q, 0)),
        out_shape=jax.ShapeDtypeStruct((B, H, S, D), q.dtype),
        interpret=interpret,
    )(q, k, v, bias)
