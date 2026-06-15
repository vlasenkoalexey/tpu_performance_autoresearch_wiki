# Copyright 2025 The EasyDeL/ejKernel Author @erfanzar (Erfan Zare Chavoshi).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Native Sparse Attention forward pass implementation using XLA/JAX.

This module provides the forward pass for Native Sparse Attention (NSA),
implementing block-sparse attention where each query only attends to a
selected subset of key-value blocks.

Key Components:
    - _sparse_attention_fwd: Main forward function with block selection

Algorithm:
    Block-sparse attention with dynamic block selection:
    1. For each query token, look up which K/V blocks to attend to
    2. Gather the selected K/V blocks using block_indices
    3. Compute attention only over selected blocks
    4. Apply softmax and weighted sum over selected blocks

Features:
    - Dynamic block selection via block_indices
    - GQA/MQA support with head broadcasting
    - Variable block counts per query via block_counts
    - Efficient JAX vmap/scan implementation

Memory Complexity:
    - O(N * S * B) where N=seq_len, S=num_selected_blocks, B=block_size
    - Much less than full O(N²) for sparse patterns

Note:
    Uses ejit decorator for efficient JIT compilation with
    static argument handling.
"""

import jax
import jax.numpy as jnp
from jaxtyping import Array, Float, Int

from ejkernel.callib import ejit


@ejit(static_argnums=(5,))
def _sparse_attention_fwd(
    q: Float[Array, "batch seq_len num_q_heads head_dim"],
    k: Float[Array, "batch seq_len num_kv_heads head_dim"],
    v: Float[Array, "batch seq_len num_kv_heads head_dim"],
    block_indices: Int[Array, "batch seq_len num_kv_heads num_selected_blocks"],
    block_counts: Int[Array, "batch seq_len num_kv_heads"],
    block_size: int,
    softmax_scale: float,
) -> Float[Array, "batch seq_len num_q_heads head_dim"]:
    """Compute forward pass for block-sparse attention with per-token selection and causal masking.

    For each query token, this function gathers the selected K/V blocks
    specified by block_indices, computes scaled dot-product attention over
    those blocks with causal masking, and returns the weighted sum of values.

    The block selection is dynamic and per-token: each query position can
    attend to a different set of K/V blocks, controlled by block_indices
    and block_counts.

    Args:
        q: Query tensor [batch, seq_len, num_q_heads, head_dim].
        k: Key tensor [batch, seq_len, num_kv_heads, head_dim].
            Padded to block boundaries internally.
        v: Value tensor [batch, seq_len, num_kv_heads, head_dim].
            Padded to block boundaries internally.
        block_indices: Per-token block selection indices
            [batch, seq_len, num_kv_heads, num_selected_blocks].
            Values of -1 are treated as invalid (sentinel) and masked out.
        block_counts: Number of valid blocks per token
            [batch, seq_len, num_kv_heads].
        block_size: Size of each K/V block (static argument).
        softmax_scale: Scaling factor applied to QK^T dot products.

    Returns:
        Attention output [batch, seq_len, num_q_heads, head_dim].
    """
    B, T, HQ, D = q.shape
    HKV = k.shape[2]
    G = HQ // HKV

    NB = (T + block_size - 1) // block_size

    B, T, HQ, D = q.shape
    HKV = k.shape[2]
    G = HQ // HKV

    NB = (T + block_size - 1) // block_size

    # Expand KV to match Q heads
    k_exp = jnp.repeat(k, G, axis=2)
    v_exp = jnp.repeat(v, G, axis=2)

    q_trans = jnp.transpose(q, (0, 2, 1, 3)) # (B, HQ, T, D)
    k_trans = jnp.transpose(k_exp, (0, 2, 1, 3)) # (B, HQ, T, D)
    v_trans = jnp.transpose(v_exp, (0, 2, 1, 3)) # (B, HQ, T, D)
    
    # We will chunk along the T dimension of Q (chunk size e.g. 128)
    chunk_size = 128
    num_chunks = (T + chunk_size - 1) // chunk_size

    bi_exp = jnp.repeat(block_indices, G, axis=2) # (B, T, HQ, S)
    bc_exp = jnp.repeat(block_counts, G, axis=2)  # (B, T, HQ)
    S = bi_exp.shape[-1]
    
    def scan_fn(carry, chunk_idx):
        start_idx = chunk_idx * chunk_size
        q_chunk = jax.lax.dynamic_slice(q_trans, (0, 0, start_idx, 0), (B, HQ, chunk_size, D))
        
        # (B, HQ, chunk_size, T)
        scores = jnp.einsum("bhqd,bhkd->bhqk", q_chunk, k_trans) * softmax_scale
        
        bi_chunk = jax.lax.dynamic_slice(bi_exp, (0, start_idx, 0, 0), (B, chunk_size, HQ, S))
        bc_chunk = jax.lax.dynamic_slice(bc_exp, (0, start_idx, 0), (B, chunk_size, HQ))
        
        S_idx = jnp.arange(S)
        s_mask = S_idx[None, None, None, :] < bc_chunk[..., None]
        
        valid_bi = (bi_chunk >= 0) & (bi_chunk < NB) & s_mask
        bi_safe = jnp.where(valid_bi, bi_chunk, NB + 1)
        
        one_hot_blocks = jax.nn.one_hot(bi_safe, NB, dtype=jnp.bool_) # (B, chunk, HQ, S, NB)
        valid_blocks = one_hot_blocks.any(axis=-2) # (B, chunk, HQ, NB)
        valid_tokens = jnp.repeat(valid_blocks, block_size, axis=-1)[..., :T] # (B, chunk, HQ, T)
        
        # Apply causal mask and block mask
        t_idx = jnp.arange(chunk_size)[:, None] + start_idx
        s_idx = jnp.arange(T)[None, :]
        causal_mask = t_idx >= s_idx
        
        valid_mask = jnp.transpose(valid_tokens, (0, 2, 1, 3)) & causal_mask[None, None, :, :]
        
        scores = jnp.where(valid_mask, scores, -1e9)
        w = jax.nn.softmax(scores, axis=-1)
        
        out_chunk = jnp.einsum("bhqk,bhkd->bhqd", w, v_trans)
        return carry, out_chunk

    _, outs_trans = jax.lax.scan(scan_fn, None, jnp.arange(num_chunks))
    
    # outs_trans is (num_chunks, B, HQ, chunk_size, D)
    outs_trans = jnp.transpose(outs_trans, (1, 2, 0, 3, 4))
    outs_trans = outs_trans.reshape(B, HQ, T, D)
    outs = jnp.transpose(outs_trans, (0, 2, 1, 3))
    
    return outs
