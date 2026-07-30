# KernelGate regression fixture — copied verbatim from:
#   /tmp/claude-2015485509/-mnt-disks-persist-torch-tpu-tpu-performance-autoresearch-wiki-private/0ad85ff5-18a7-4fa1-81ab-e5d9628337cc/scratchpad/ag_finals/6p_Paged_Attention/optimized.py
# KNOWN-GOOD: campaign final paged-attention kernel. Entry: workload.
# Do not edit: this file is a pinned reproduction of campaign history.
import time
import numpy as np
import jax
import jax.numpy as jnp
CONFIG = {
    'name': 'llama3_70b_paged_attention',
    'model': 'Llama-3.1-70B',
    'operator': 'paged_attention',
    'num_seqs': 64,
    'max_seq_len': 4096,
    'num_query_heads': 64,
    'num_kv_heads': 8,
    'head_dim': 128,
    'page_size': 16,
    'pages_per_seq': 256,
}

def create_inputs(dtype=jnp.bfloat16):
    key = jax.random.key(42)
    keys = jax.random.split(key, 5)
    num_seqs = CONFIG['num_seqs']
    num_q_heads = CONFIG['num_query_heads']
    num_kv_heads = CONFIG['num_kv_heads']
    head_dim = CONFIG['head_dim']
    page_size = CONFIG['page_size']
    pages_per_seq = CONFIG['pages_per_seq']
    total_pages = num_seqs * pages_per_seq
    max_seq_len = pages_per_seq * page_size
    max_num_tokens = num_seqs
    queries = jax.random.normal(keys[0], (max_num_tokens, num_q_heads, head_dim), dtype=dtype)
    k_pages = jax.random.normal(keys[1], (total_pages, page_size, num_kv_heads, head_dim), dtype=dtype) * 0.02
    v_pages = jax.random.normal(keys[2], (total_pages, page_size, num_kv_heads, head_dim), dtype=dtype) * 0.02
    kv_lens = jnp.full((num_seqs,), max_seq_len, dtype=jnp.int32)
    page_indices = jnp.arange(total_pages, dtype=jnp.int32).reshape(num_seqs, pages_per_seq)
    cu_q_lens = jnp.arange(num_seqs + 1, dtype=jnp.int32)
    return queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens

def workload_naive(queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens):
    num_seqs = CONFIG['num_seqs']
    num_q_heads = CONFIG['num_query_heads']
    num_kv_heads = CONFIG['num_kv_heads']
    head_dim = CONFIG['head_dim']
    page_size = CONFIG['page_size']
    max_seq_len = CONFIG['pages_per_seq'] * page_size
    num_q_per_kv = num_q_heads // num_kv_heads
    sm_scale = head_dim ** -0.5

    def attend_one_seq(seq_idx):
        q_start = cu_q_lens[seq_idx]
        q = jax.lax.dynamic_slice(queries, (q_start, 0, 0), (1, num_q_heads, head_dim))
        seq_pages = page_indices[seq_idx]
        k = k_pages[seq_pages].reshape(max_seq_len, num_kv_heads, head_dim)
        v = v_pages[seq_pages].reshape(max_seq_len, num_kv_heads, head_dim)
        k = jnp.repeat(k, num_q_per_kv, axis=1)
        v = jnp.repeat(v, num_q_per_kv, axis=1)
        attn = jnp.einsum('qhd,khd->hqk', q, k) * sm_scale
        kv_len = kv_lens[seq_idx]
        mask = jnp.arange(max_seq_len) < kv_len
        attn = jnp.where(mask[None, None, :], attn, -1e30)
        attn = jax.nn.softmax(attn, axis=-1)
        out = jnp.einsum('hqk,khd->qhd', attn, v)
        return out.squeeze(0)

    return jax.vmap(attend_one_seq)(jnp.arange(num_seqs))

def workload(queries, k_pages, v_pages, kv_lens, page_indices, cu_q_lens):
    num_seqs = CONFIG['num_seqs']
    num_q_heads = CONFIG['num_query_heads']
    num_kv_heads = CONFIG['num_kv_heads']
    head_dim = CONFIG['head_dim']
    page_size = CONFIG['page_size']
    max_seq_len = CONFIG['pages_per_seq'] * page_size
    num_q_per_kv = num_q_heads // num_kv_heads
    sm_scale = head_dim ** -0.5

    def attend_one_seq(seq_idx):
        q_start = cu_q_lens[seq_idx]
        q = jax.lax.dynamic_slice(queries, (q_start, 0, 0), (1, num_q_heads, head_dim))  # (1, H_q, D)
        # Reshape q to (1, num_kv_heads, num_q_per_kv, D)
        q = q.reshape(1, num_kv_heads, num_q_per_kv, head_dim)
        
        # Gather KV pages
        seq_pages = page_indices[seq_idx]  # (pages_per_seq,)
        k = k_pages[seq_pages].reshape(max_seq_len, num_kv_heads, head_dim)  # (S, H_kv, D)
        v = v_pages[seq_pages].reshape(max_seq_len, num_kv_heads, head_dim)  # (S, H_kv, D)
        
        # Attention: (1, K, H, D) x (S, K, D) -> (K, H, 1, S)
        attn = jnp.einsum('1KHD,SKD->KH1S', q, k) * sm_scale
        
        kv_len = kv_lens[seq_idx]
        mask = jnp.arange(max_seq_len) < kv_len
        attn = jnp.where(mask[None, None, None, :], attn, -1e30)
        attn = jax.nn.softmax(attn, axis=-1)
        
        # Multiply by v: (K, H, 1, S) x (S, K, D) -> (K, H, 1, D)
        out = jnp.einsum('KH1S,SKD->KH1D', attn, v)
        # reshape back to (H_q, D)
        return out.reshape(num_q_heads, head_dim)

    outputs = jax.vmap(attend_one_seq)(jnp.arange(num_seqs))
    return outputs

def get_parity(scale_multiplier=1.0):
    inputs = create_inputs()
    # Apply scale multiplier
    inputs = list(inputs)
    inputs[1] = inputs[1] * scale_multiplier
    inputs[2] = inputs[2] * scale_multiplier
    
    inputs_fp32 = [x.astype(jnp.float32) if x.dtype == jnp.bfloat16 else x for x in inputs]
    oracle_fn = jax.jit(workload_naive)
    oracle_out = oracle_fn(*inputs_fp32)
    
    naive_out = workload_naive(*inputs)
    opt_out = workload(*inputs)
    
    naive_abs_diff = float(jnp.max(jnp.abs(naive_out - oracle_out)))
    naive_rel_diff = float(jnp.max(jnp.abs((naive_out - oracle_out) / jnp.clip(jnp.abs(oracle_out), 1e-5))))
    
    cand_abs_diff = float(jnp.max(jnp.abs(opt_out - oracle_out)))
    cand_rel_diff = float(jnp.max(jnp.abs((opt_out - oracle_out) / jnp.clip(jnp.abs(oracle_out), 1e-5))))
    
    print(f"--- Multiplier {scale_multiplier} ---")
    print(f"Naive vs Oracle: max_abs_diff={naive_abs_diff:.6f} max_rel_diff={naive_rel_diff:.6f}")
    print(f"Cand vs Oracle: max_abs_diff={cand_abs_diff:.6f} max_rel_diff={cand_rel_diff:.6f}")
    return cand_abs_diff, cand_rel_diff

def benchmark(num_warmup=5, num_iters=50):
    print("Checking parity at baseline scale (0.02)")
    get_parity(1.0)
    print("Checking parity at K-scale 0.2")
    get_parity(10.0)
    print("Checking parity at K-scale 1.0")
    abs_10, rel_10 = get_parity(50.0)
    
    print(f"Parity: max_abs_diff={abs_10:.6f} max_rel_diff={rel_10:.6f}")
    
    inputs = create_inputs()
    print("Benchmarking naive...")
    baseline_fn = jax.jit(workload_naive)
    for _ in range(num_warmup):
        jax.block_until_ready(baseline_fn(*inputs))
    ts_naive = []
    for _ in range(num_iters):
        t0 = time.perf_counter()
        jax.block_until_ready(baseline_fn(*inputs))
        ts_naive.append((time.perf_counter() - t0) * 1000)
    a_naive = np.array(ts_naive)
    naive_p50 = np.percentile(a_naive, 50)
    print(f"naive_p50={naive_p50:.3f}ms std={a_naive.std():.3f} min={a_naive.min():.3f} n={num_iters}")

    print("Benchmarking cand...")
    opt_fn = jax.jit(workload)
    for _ in range(num_warmup):
        jax.block_until_ready(opt_fn(*inputs))
    ts = []
    for _ in range(num_iters):
        t0 = time.perf_counter()
        jax.block_until_ready(opt_fn(*inputs))
        ts.append((time.perf_counter() - t0) * 1000)
    a = np.array(ts)
    cand_p50 = np.percentile(a, 50)
    print(f"p50={cand_p50:.3f}ms std={a.std():.3f} min={a.min():.3f} n={num_iters}")
    
    print(f"RESULT_TIME_MS: {cand_p50:.3f}")
    print(f"CORRECTNESS_MAX_ABS: {abs_10:.6f}")
    print(f"CORRECTNESS_MAX_REL: {rel_10:.6f}")

if __name__ == "__main__":
    benchmark()
