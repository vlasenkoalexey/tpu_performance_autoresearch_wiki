# KernelGate regression fixture — copied verbatim from:
#   /tmp/claude-2015485509/-mnt-disks-persist-torch-tpu-tpu-performance-autoresearch-wiki-private/0ad85ff5-18a7-4fa1-81ab-e5d9628337cc/scratchpad/ag_finals/5p_Flex_Attention/optimized.py
# KNOWN-GOOD: campaign final flex-attention Pallas kernel. Entry: workload_cand.
# Do not edit: this file is a pinned reproduction of campaign history.
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu
import time
import numpy as np

CONFIG = {
    'name': 'llama3_70b_flex_attention',
    'model': 'Llama-3.1-70B',
    'operator': 'flex_attention',
    'batch': 4,
    'seq_len': 4096,
    'num_heads': 64,
    'head_dim': 128,
}

def create_inputs(seed=42, dtype=jnp.bfloat16):
    key = jax.random.key(seed)
    k1, k2, k3, k4 = jax.random.split(key, 4)
    B = CONFIG['batch']
    S = CONFIG['seq_len']
    H = CONFIG['num_heads']
    D = CONFIG['head_dim']
    q = jax.random.normal(k1, (B, H, S, D), dtype=dtype)
    k = jax.random.normal(k2, (B, H, S, D), dtype=dtype) * 0.02
    v = jax.random.normal(k3, (B, H, S, D), dtype=dtype) * 0.02
    rel_pos_bias = jax.random.normal(k4, (H, S, S), dtype=dtype) * 0.01
    return q, k, v, rel_pos_bias

def flex_attn_kernel(q_idxs_ref, k_idxs_ref, q_ref, k_ref, v_ref, bias_ref, o_ref,
                     acc_o_ref, acc_l_ref):
    p = pl.program_id(2)
    q_idx = q_idxs_ref[p]
    k_idx = k_idxs_ref[p]
    
    @pl.when(k_idx == 0)
    def _():
        acc_o_ref[...] = jnp.zeros_like(acc_o_ref)
        acc_l_ref[...] = jnp.zeros_like(acc_l_ref)
        
    q_blk = q_ref[0, 0, ...]
    k_blk = k_ref[0, 0, ...]
    v_blk = v_ref[0, 0, ...]
    bias_blk = bias_ref[0, ...]
    
    sm_scale = 128 ** -0.5
    attn = jnp.dot(q_blk, k_blk.T, preferred_element_type=jnp.float32) * sm_scale
    attn = attn + bias_blk
    
    row_idx = q_idx * q_blk.shape[0] + jnp.arange(q_blk.shape[0])[:, None]
    col_idx = k_idx * k_blk.shape[0] + jnp.arange(k_blk.shape[0])[None, :]
    attn = jnp.where(row_idx >= col_idx, attn, -1e30)
    
    attn_exp = jnp.exp(attn)
    
    l_prev = acc_l_ref[...]
    l_curr = l_prev + jnp.sum(attn_exp, axis=1)
    
    o_prev = acc_o_ref[...]
    o_curr = o_prev + jnp.dot(attn_exp.astype(v_blk.dtype), v_blk, preferred_element_type=jnp.float32)
    
    acc_l_ref[...] = l_curr
    acc_o_ref[...] = o_curr
    
    @pl.when(k_idx == q_idx)
    def _():
        o_ref[0, 0, ...] = (acc_o_ref[...] / acc_l_ref[...][:, None]).astype(o_ref.dtype)

def workload_cand(q, k, v, rel_pos_bias):
    B, H, S, D = q.shape
    BQ = 1024
    BK = 1024
    
    num_q = S // BQ
    num_pairs = num_q * (num_q + 1) // 2
    
    q_idxs = np.zeros(num_pairs, dtype=np.int32)
    k_idxs = np.zeros(num_pairs, dtype=np.int32)
    
    idx = 0
    for q_i in range(num_q):
        for k_i in range(q_i + 1):
            q_idxs[idx] = q_i
            k_idxs[idx] = k_i
            idx += 1
            
    q_idxs = jnp.array(q_idxs)
    k_idxs = jnp.array(k_idxs)
    
    def q_map(b, h, p, q_idxs_ref, k_idxs_ref): return (b, h, q_idxs_ref[p], 0)
    def k_map(b, h, p, q_idxs_ref, k_idxs_ref): return (b, h, k_idxs_ref[p], 0)
    def v_map(b, h, p, q_idxs_ref, k_idxs_ref): return (b, h, k_idxs_ref[p], 0)
    def bias_map(b, h, p, q_idxs_ref, k_idxs_ref): return (h, q_idxs_ref[p], k_idxs_ref[p])
    def o_map(b, h, p, q_idxs_ref, k_idxs_ref): return (b, h, q_idxs_ref[p], 0)
    
    grid_spec = pltpu.PrefetchScalarGridSpec(
        num_scalar_prefetch=2,
        grid=(B, H, num_pairs),
        in_specs=[
            pl.BlockSpec((1, 1, BQ, D), q_map),
            pl.BlockSpec((1, 1, BK, D), k_map),
            pl.BlockSpec((1, 1, BK, D), v_map),
            pl.BlockSpec((1, BQ, BK), bias_map),
        ],
        out_specs=pl.BlockSpec((1, 1, BQ, D), o_map),
        scratch_shapes=[
            pltpu.VMEM((BQ, D), jnp.float32),
            pltpu.VMEM((BQ,), jnp.float32)
        ]
    )
    
    return pl.pallas_call(
        flex_attn_kernel,
        grid_spec=grid_spec,
        out_shape=jax.ShapeDtypeStruct(q.shape, q.dtype)
    )(q_idxs, k_idxs, q, k, v, rel_pos_bias)

def workload_naive(q, k, v, rel_pos_bias):
    sm_scale = 128 ** -0.5
    attn = jnp.einsum('bhqd,bhkd->bhqk', q, k) * sm_scale
    attn = attn + rel_pos_bias[None, :, :, :]
    causal = jnp.tril(jnp.ones((4096, 4096), dtype=jnp.bool_))
    attn = jnp.where(causal[None, None, :, :], attn, -1e30)
    attn = jax.nn.softmax(attn, axis=-1)
    out = jnp.einsum('bhqk,bhkd->bhqd', attn, v)
    return out

def check_parity(seed=42):
    q, k, v, bias = create_inputs(seed, jnp.float32)
    out_ref = jax.jit(workload_naive)(q, k, v, bias)
    
    q_bf, k_bf, v_bf, bias_bf = [x.astype(jnp.bfloat16) for x in (q, k, v, bias)]
    out_naive_bf = jax.jit(workload_naive)(q_bf, k_bf, v_bf, bias_bf)
    out_cand_bf = jax.jit(workload_cand)(q_bf, k_bf, v_bf, bias_bf)
    
    max_abs_naive = jnp.max(jnp.abs(out_naive_bf.astype(jnp.float32) - out_ref))
    max_abs_cand = jnp.max(jnp.abs(out_cand_bf.astype(jnp.float32) - out_ref))
    max_rel_naive = jnp.max(jnp.abs(out_naive_bf.astype(jnp.float32) - out_ref) / jnp.maximum(1e-5, jnp.abs(out_ref)))
    max_rel_cand = jnp.max(jnp.abs(out_cand_bf.astype(jnp.float32) - out_ref) / jnp.maximum(1e-5, jnp.abs(out_ref)))
    
    print(f"Naive vs Oracle - max_abs: {max_abs_naive:.6f}, max_rel: {max_rel_naive:.6f}")
    print(f"Cand vs Oracle - max_abs: {max_abs_cand:.6f}, max_rel: {max_rel_cand:.6f}")
    print(f"CORRECTNESS_MAX_ABS: {max_abs_cand:.6f}")
    print(f"CORRECTNESS_MAX_REL: {max_rel_cand:.6f}")

def bench_interleaved(fn_naive, fn_cand, *args, warmup=5, iters=50):
    for _ in range(warmup):
        jax.block_until_ready(fn_naive(*args))
        jax.block_until_ready(fn_cand(*args))
        
    ts_naive = []
    ts_cand = []
    for _ in range(iters):
        t0 = time.perf_counter()
        jax.block_until_ready(fn_naive(*args))
        ts_naive.append((time.perf_counter() - t0) * 1e3)
        
        t0 = time.perf_counter()
        jax.block_until_ready(fn_cand(*args))
        ts_cand.append((time.perf_counter() - t0) * 1e3)
        
    a_naive = np.array(ts_naive)
    a_cand = np.array(ts_cand)
    p50_naive = np.percentile(a_naive, 50)
    p50_cand = np.percentile(a_cand, 50)
    print(f"NAIVE p50={p50_naive:.3f}ms std={a_naive.std():.3f} min={a_naive.min():.3f} n={iters}")
    print(f"CAND  p50={p50_cand:.3f}ms std={a_cand.std():.3f} min={a_cand.min():.3f} n={iters}")
    print(f"RESULT_TIME_MS: {p50_cand:.3f}")
    return float(p50_naive), float(p50_cand)

if __name__ == '__main__':
    for seed in [42, 43]:
        print(f"--- SEED {seed} ---")
        print("Checking parity...")
        check_parity(seed)
    
    q, k, v, bias = create_inputs(42)
    fn_cand = jax.jit(workload_cand)
    fn_naive = jax.jit(workload_naive)
    print("\nBenchmarking candidate interleaved with naive (seed 42)...")
    bench_interleaved(fn_naive, fn_cand, q, k, v, bias)
