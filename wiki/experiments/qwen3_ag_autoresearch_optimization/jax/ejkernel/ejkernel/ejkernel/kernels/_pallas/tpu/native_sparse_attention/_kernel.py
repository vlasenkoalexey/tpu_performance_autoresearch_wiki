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

"""Pallas TPU implementation of Native Sparse Attention.

This module implements the core sparse block selection kernel using Pallas.
It reuses the Splash Attention machinery by constructing custom dynamic
MaskInfo objects that route the Pallas grid computation directly to the
selected Top-K key-value blocks.
"""

import warnings

import jax
import jax.numpy as jnp
import jaxtyping
from beartype import beartype
from jaxtyping import Array, Float, Int

from ...._registry import Backend, Platform, kernel_registry
from ..blocksparse_attention import _info as mask_info_lib
from ..blocksparse_attention._kernel import (
    DEFAULT_MASK_VALUE,
    BlockSizes,
    SplashAttentionKernel,
)


@kernel_registry.register("apply_native_sparse_attention", Platform.PALLAS, Backend.TPU)
@jaxtyping.jaxtyped(typechecker=beartype)
def apply_native_sparse_attention(
    query: Float[Array, "batch seq_len num_q_heads head_dim"],
    key: Float[Array, "batch seq_len num_kv_heads head_dim"],
    value: Float[Array, "batch seq_len num_kv_heads head_dim"],
    block_indices: Int[Array, "batch seq_len num_kv_heads num_selected_blocks"]
    | Int[Array, "batch num_kv_heads num_blocks num_selected_blocks"],
    block_counts: Int[Array, "batch seq_len num_kv_heads"] | Int[Array, "batch num_kv_heads num_blocks"] | int = 16,
    block_size: int = 64,
    softmax_scale: float | None = None,
    cu_seqlens: Int[Array, "num_seqs_plus_one"] | None = None,
    token_indices: Int[Array, "total_tokens"] | None = None,
) -> Float[Array, "batch seq_len num_q_heads head_dim"]:
    """
    Applies block-sparse attention using a pre-computed sparsity pattern via Pallas.

    Args:
        query: Query tensor `(batch, seq_len, num_q_heads, head_dim)`.
        key: Key tensor `(batch, seq_len, num_kv_heads, head_dim)`.
        value: Value tensor `(batch, seq_len, num_kv_heads, head_dim)`.
        block_indices: Top-k selected key blocks for each query block/token.
        block_counts: Number of blocks to attend to.
        block_size: Number of tokens per block.
        softmax_scale: Scale for attention scores.
    """
    if cu_seqlens is not None or token_indices is not None:
        raise NotImplementedError("Variable sequence lengths not yet supported in Pallas NSA.")

    batch, seq_len, num_q_heads, head_dim = query.shape
    num_kv_heads = key.shape[2]
    num_blocks = (seq_len + block_size - 1) // block_size

    if softmax_scale is None:
        softmax_scale = 1.0 / (head_dim**0.5)

    is_mqa = (num_q_heads != num_kv_heads) and (num_kv_heads == 1)

    block_indices_arr = jnp.asarray(block_indices, dtype=jnp.int32)
    # Convert per-token block indices to per-block indices if needed.
    # Pallas blocksparse kernel expects block-level granularity.
    if block_indices_arr.ndim == 4 and block_indices_arr.shape[1] == seq_len:
        # Take the indices for the first token of each block, assuming uniform selection per block.
        # Shape: (batch, seq_len, num_kv_heads, S) -> (batch, num_blocks, num_kv_heads, S)
        tok_idx = jnp.arange(0, seq_len, block_size)
        block_indices_blk = block_indices_arr[:, tok_idx, :, :]
        # Transpose to match: (batch, num_kv_heads, num_blocks, S)
        block_indices_blk = jnp.transpose(block_indices_blk, (0, 2, 1, 3))
    elif block_indices_arr.shape[1] == num_kv_heads and block_indices_arr.shape[2] == num_blocks:
        block_indices_blk = block_indices_arr
    else:
        raise ValueError(f"Invalid shape for block_indices: {block_indices_arr.shape}")

    # Now block_indices_blk is (batch, num_kv_heads, num_blocks, S)
    # Pallas SplashAttentionKernel grids over Q heads, not KV heads, so we must broadcast KV block indices to Q heads.
    if num_q_heads != num_kv_heads:
        if num_q_heads % num_kv_heads != 0:
            raise ValueError(f"num_q_heads ({num_q_heads}) must be a multiple of num_kv_heads ({num_kv_heads})")
        group_size = num_q_heads // num_kv_heads
        # (batch, num_kv_heads, 1, num_blocks, S) -> (batch, num_kv_heads, group_size, num_blocks, S)
        block_indices_expanded = jnp.repeat(block_indices_blk[:, :, None, :, :], group_size, axis=2)
        # Reshape to (batch, num_q_heads, num_blocks, S)
        block_indices_q = block_indices_expanded.reshape(batch, num_q_heads, num_blocks, block_indices_blk.shape[-1])
    else:
        block_indices_q = block_indices_blk

    S = block_indices_q.shape[-1]
    
    # Pre-calculate boolean masks.
    # block_indices_q: [batch, num_q_heads, q_blocks, S]
    # We construct MaskInfo directly.
    q_arange = jnp.arange(num_blocks, dtype=jnp.int32)
    # Causal diagonal
    is_diagonal_fwd = block_indices_q == q_arange[None, None, :, None]
    is_valid_fwd = block_indices_q >= 0

    block_mask_fwd = jnp.where(is_diagonal_fwd, 1, 2)
    block_mask_fwd = jnp.where(is_valid_fwd, block_mask_fwd, 0).astype(jnp.int8)

    data_next_fwd = jnp.where(is_valid_fwd, block_indices_q, 0).astype(jnp.int32)
    mask_next_fwd = jnp.zeros_like(data_next_fwd)

    causal_mask = jnp.tril(jnp.ones((block_size, block_size), dtype=jnp.bool_))
    # Shape of partial_mask_blocks should be [num_partial_blocks, bq, bkv] per batch
    # We broadcast batch dimension so vmap works correctly.
    partial_mask_blocks_fwd = jnp.broadcast_to(causal_mask[None, None, ...], (batch, 1, block_size, block_size))

    fwd_mask_info = mask_info_lib.MaskInfo(
        data_next=data_next_fwd,
        mask_next=mask_next_fwd,
        block_mask=block_mask_fwd,
        partial_mask_blocks=partial_mask_blocks_fwd,
        q_sequence=None,
        is_dynamic_mask=True,
    )

    # For backward pass (dKV), we use the unreduced dense block grid because computing
    # the transpose sparse pattern dynamically is inefficient and complex.
    # The grid size (num_blocks x num_blocks) is small enough.
    kv_arange = jnp.arange(num_blocks, dtype=jnp.int32)
    # is_selected: [batch, num_q_heads, num_q_blocks, num_kv_blocks]
    is_selected = jnp.any(block_indices_q[..., None] == kv_arange[None, None, None, :], axis=3)
    is_diagonal_dense = (q_arange[:, None] == kv_arange[None, :])[None, None, :, :]

    block_mask_dkv = jnp.where(is_selected & is_diagonal_dense, 1, 
                     jnp.where(is_selected, 2, 0)).astype(jnp.int8)

    data_next_dkv = jnp.broadcast_to(
        q_arange[None, None, :, None], 
        (batch, num_q_heads, num_blocks, num_blocks)
    ).astype(jnp.int32)
    data_next_dkv = jnp.where(block_mask_dkv == 0, 0, data_next_dkv)

    mask_next_dkv = jnp.zeros((batch, num_q_heads, num_blocks, num_blocks), dtype=jnp.int32)
    partial_mask_blocks_dkv = jnp.broadcast_to(causal_mask.T[None, None, ...], (batch, 1, block_size, block_size))

    dkv_mask_info = mask_info_lib.MaskInfo(
        data_next=data_next_dkv,
        mask_next=mask_next_dkv,
        block_mask=block_mask_dkv,
        partial_mask_blocks=partial_mask_blocks_dkv,
        q_sequence=None,
        is_dynamic_mask=True,
    )

    sizes = BlockSizes(
        block_q=block_size, block_kv=block_size, block_kv_compute=block_size,
        block_q_dkv=block_size, block_kv_dkv=block_size, block_kv_dkv_compute=block_size,
        block_q_dq=block_size, block_kv_dq=block_size,
        use_fused_bwd_kernel=False,
    )

    def attn_static_fn(q, k, v, fwd_mask, dq_mask, dkv_mask):
        kernel = SplashAttentionKernel(
            fwd_mask_info=fwd_mask,
            dq_mask_info=dq_mask,
            dkv_mask_info=dkv_mask,
            block_sizes=sizes,
            is_mqa=is_mqa,
            save_residuals=True,
            mask_value=DEFAULT_MASK_VALUE,
            logits_soft_cap=None,
            residual_checkpoint_name=None,
            mask_function=None,
            interpret=False,
        )
        return kernel(
            q=q, k=k, v=v,
            segment_ids=None,
            sinks=None,
        )

    # vmap over batch dimension
    attn_fn = jax.vmap(attn_static_fn, in_axes=(0, 0, 0, 0, 0, 0))

    # Scale queries before attention as Pallas kernels expect scaled queries.
    out = attn_fn(
        query * softmax_scale,
        key,
        value,
        fwd_mask_info,
        fwd_mask_info, # dQ uses the same sparse pattern as Fwd
        dkv_mask_info,
    )
    return out
