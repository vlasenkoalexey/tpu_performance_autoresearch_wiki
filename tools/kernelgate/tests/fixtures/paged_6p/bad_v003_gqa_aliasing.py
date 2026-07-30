# KernelGate regression fixture — copied verbatim from:
#   /mnt/disks/persist/torch-tpu/rerun_lane_6p/benchmark/jaxbench-nopeek/6p_Paged_Attention/cand_v003.py
# KNOWN-BAD (GQA aliasing class): einsum index labels transpose the (kv-head, group) axes ('qkvd,skd->vkqs' + reshape), mixing q-head groups across KV heads. MUST FAIL the paged_attention coverage spec (group isolation).
# Do not edit: this file is a pinned reproduction of campaign history.
import time
import numpy as np
import jax
import jax.numpy as jnp
import baseline

CONFIG = baseline.CONFIG

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
        
        # Attention: (1, H_kv, H_q_per_kv, D) x (S, H_kv, D) -> (H_kv, H_q_per_kv, 1, S)
        # We can just einsum: 'qkhd,skd->khqs' where k=num_kv_heads, h=num_q_per_kv
        attn = jnp.einsum('qkvd,skd->vkqs', q, k) * sm_scale
        # attn shape is (num_kv_heads, num_q_per_kv, 1, max_seq_len)
        
        kv_len = kv_lens[seq_idx]
        mask = jnp.arange(max_seq_len) < kv_len
        attn = jnp.where(mask[None, None, None, :], attn, -1e30)
        attn = jax.nn.softmax(attn, axis=-1)
        
        # Multiply by v: (num_kv_heads, num_q_per_kv, 1, S) x (S, num_kv_heads, D) -> (num_kv_heads, num_q_per_kv, 1, D)
        out = jnp.einsum('vkqs,svd->vkqd', attn, v)
        # reshape back to (H_q, D)
        return out.reshape(num_q_heads, head_dim)

    outputs = jax.vmap(attend_one_seq)(jnp.arange(num_seqs))
    return outputs

def benchmark(num_warmup=5, num_iters=50):
    inputs = baseline.create_inputs()
    
    # Oracle: full float32 recompute of the baseline
    inputs_fp32 = [x.astype(jnp.float32) if x.dtype == jnp.bfloat16 else x for x in inputs]
    oracle_fn = jax.jit(baseline.workload)
    oracle_out = oracle_fn(*inputs_fp32)
    
    naive_out = baseline.workload(*inputs)
    opt_out = workload(*inputs)
    
    # Naive vs Oracle
    naive_abs_diff = float(jnp.max(jnp.abs(naive_out - oracle_out)))
    naive_rel_diff = float(jnp.max(jnp.abs((naive_out - oracle_out) / jnp.clip(jnp.abs(oracle_out), 1e-5))))
    print(f"Naive vs Oracle: max_abs_diff={naive_abs_diff:.6f} max_rel_diff={naive_rel_diff:.6f}")
    
    # Cand vs Oracle
    cand_abs_diff = float(jnp.max(jnp.abs(opt_out - oracle_out)))
    cand_rel_diff = float(jnp.max(jnp.abs((opt_out - oracle_out) / jnp.clip(jnp.abs(oracle_out), 1e-5))))
    print(f"Cand vs Oracle: max_abs_diff={cand_abs_diff:.6f} max_rel_diff={cand_rel_diff:.6f}")
    
    # Parity gate
    max_abs_diff = cand_abs_diff
    max_rel_diff = cand_rel_diff
    print(f"Parity: max_abs_diff={max_abs_diff:.6f} max_rel_diff={max_rel_diff:.6f}")
    
    print("Benchmarking naive...")
    baseline_fn = jax.jit(baseline.workload)
    for _ in range(num_warmup):
        jax.block_until_ready(baseline_fn(*inputs))
    ts_naive = []
    for _ in range(num_iters):
        t0 = time.perf_counter()
        jax.block_until_ready(baseline_fn(*inputs))
        ts_naive.append((time.perf_counter() - t0) * 1000)
    a_naive = np.array(ts_naive)
    print(f"naive_p50={np.percentile(a_naive, 50):.3f}ms std={a_naive.std():.3f} min={a_naive.min():.3f} n={num_iters}")

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
    print(f"p50={np.percentile(a, 50):.3f}ms std={a.std():.3f} min={a.min():.3f} n={num_iters}")

if __name__ == "__main__":
    benchmark()
