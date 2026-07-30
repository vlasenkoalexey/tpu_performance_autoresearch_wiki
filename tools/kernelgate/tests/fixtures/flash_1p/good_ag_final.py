# KernelGate regression fixture — copied verbatim from:
#   /tmp/claude-2015485509/-mnt-disks-persist-torch-tpu-tpu-performance-autoresearch-wiki-private/0ad85ff5-18a7-4fa1-81ab-e5d9628337cc/scratchpad/ag_finals/1p_Flash_Attention/optimized.py
# KNOWN-GOOD: campaign final Pallas flash-attention kernel (~2.8-3.1x vs baseline). Entry: flash_attention.
# Do not edit: this file is a pinned reproduction of campaign history.
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu
import time
import numpy as np
import functools
import sys

CONFIG = {
    'name': 'flash_attention_pallas',
    'model': 'Pallas-MHA',
    'operator': 'causal_mha',
    'batch': 4,
    'seq_len': 4096,
    'num_heads': 64,
    'head_dim': 128,
}

def create_inputs(dtype=jnp.bfloat16):
    key = jax.random.PRNGKey(42)
    k1, k2, k3 = jax.random.split(key, 3)
    B, S = CONFIG['batch'], CONFIG['seq_len']
    H, D = CONFIG['num_heads'], CONFIG['head_dim']
    query = jax.random.normal(k1, (B, H, S, D), dtype=dtype)
    key_t = jax.random.normal(k2, (B, H, S, D), dtype=dtype)
    value = jax.random.normal(k3, (B, H, S, D), dtype=dtype)
    return query, key_t, value

def flash_attention_kernel(
    q_ref, k_ref, v_ref, o_ref,
    *,
    block_q: int,
    block_k: int,
    D: int,
    num_blocks_k: int,
):
    q_block_idx = pl.program_id(2)

    m = jnp.full((block_q,), -jnp.inf, dtype=jnp.float32)
    l = jnp.zeros((block_q,), dtype=jnp.float32)
    acc = jnp.zeros((block_q, D), dtype=jnp.float32)

    q = q_ref[...]

    def body_fn(k_block_idx, state):
        m_i, l_i, acc_i = state
        
        k = k_ref[k_block_idx]
        v = v_ref[k_block_idx]
        scale = jnp.float32(D ** -0.5)

        attn_weights = jnp.dot(q, k.T, preferred_element_type=jnp.float32) * scale
        
        m_ij = jnp.max(attn_weights, axis=1)
        m_new = jnp.maximum(m_i, m_ij)
        
        diff = attn_weights - m_new[:, None]
        p = jnp.exp(diff)
        
        l_ij = jnp.sum(p, axis=1)
        
        alpha = jnp.exp(m_i - m_new)
        alpha = jnp.where(m_i == -jnp.inf, 0.0, alpha)
        
        l_new = l_i * alpha + l_ij
        acc_i = acc_i * alpha[:, None]
        
        p_bf16 = p.astype(v.dtype)
        acc_update = jnp.dot(p_bf16, v, preferred_element_type=jnp.float32)
        acc_new = acc_i + acc_update
        
        return m_new, l_new, acc_new

    m, l, acc = jax.lax.fori_loop(0, q_block_idx, body_fn, (m, l, acc))

    # Diagonal block
    k_diag = k_ref[q_block_idx]
    v_diag = v_ref[q_block_idx]
    scale = jnp.float32(D ** -0.5)
    
    attn_weights = jnp.dot(q, k_diag.T, preferred_element_type=jnp.float32) * scale
    
    row_indices = q_block_idx * block_q + jnp.arange(block_q)
    col_indices = q_block_idx * block_k + jnp.arange(block_k)
    mask = row_indices[:, None] >= col_indices[None, :]
    attn_weights = jnp.where(mask, attn_weights, -jnp.inf)
    
    m_ij = jnp.max(attn_weights, axis=1)
    m_new = jnp.maximum(m, m_ij)
    
    diff = attn_weights - m_new[:, None]
    p = jnp.exp(diff)
    p = jnp.where(mask, p, 0.0)
    
    l_ij = jnp.sum(p, axis=1)
    
    alpha = jnp.exp(m - m_new)
    alpha = jnp.where(m == -jnp.inf, 0.0, alpha)
    
    l_new = l * alpha + l_ij
    acc_new = acc * alpha[:, None]
    
    p_bf16 = p.astype(v_diag.dtype)
    acc_update = jnp.dot(p_bf16, v_diag, preferred_element_type=jnp.float32)
    acc_new = acc_new + acc_update

    out = acc_new / l_new[:, None]
    o_ref[...] = out.astype(o_ref.dtype)

def flash_attention(query, key, value, block_q=512, block_k=512):
    B, H, S, D = query.shape
    num_blocks_q = S // block_q
    num_blocks_k = S // block_k
    grid = (B, H, num_blocks_q)
    
    kernel = functools.partial(flash_attention_kernel, block_q=block_q, block_k=block_k, D=D, num_blocks_k=num_blocks_k)
    
    k_reshaped = key.reshape(B, H, num_blocks_k, block_k, D)
    v_reshaped = value.reshape(B, H, num_blocks_k, block_k, D)
    
    out = pl.pallas_call(
        kernel,
        out_shape=jax.ShapeDtypeStruct(query.shape, query.dtype),
        in_specs=[
            pl.BlockSpec(block_shape=(None, None, block_q, D), index_map=lambda b, h, i: (b, h, i, 0)), 
            pl.BlockSpec(block_shape=(None, None, num_blocks_k, block_k, D), index_map=lambda b, h, i: (b, h, 0, 0, 0)), 
            pl.BlockSpec(block_shape=(None, None, num_blocks_k, block_k, D), index_map=lambda b, h, i: (b, h, 0, 0, 0)), 
        ],
        out_specs=pl.BlockSpec(block_shape=(None, None, block_q, D), index_map=lambda b, h, i: (b, h, i, 0)),
        grid=grid,
        compiler_params=pltpu.CompilerParams(
            dimension_semantics=("parallel", "parallel", "parallel")),
    )(query, k_reshaped, v_reshaped)
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
    inputs = create_inputs()
    B, S, H, D = CONFIG['batch'], CONFIG['seq_len'], CONFIG['num_heads'], CONFIG['head_dim']
    
    fn = jax.jit(lambda q, k, v: flash_attention(q, k, v, block_q=512, block_k=512))
    
    print("Running perf benchmark...")
    avg = bench(fn, *inputs, warmup=5, iters=50)
    print(f"RESULT_TIME_MS: {avg:.3f}")
