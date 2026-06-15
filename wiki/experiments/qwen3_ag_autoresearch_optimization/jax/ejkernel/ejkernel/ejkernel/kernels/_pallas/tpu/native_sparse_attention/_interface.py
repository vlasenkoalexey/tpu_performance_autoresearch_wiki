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

"""Native Sparse Attention interface with block selection and compression.

This module provides the public API for Native Sparse Attention (NSA) on Pallas TPU.
"""

import warnings

import jax
import jax.numpy as jnp
import jaxtyping
from beartype import beartype
from jaxtyping import Array, Float, Int

from ...._registry import Backend, Platform, kernel_registry
from ..._xla.native_sparse_attention._interface import _nsa_compression_xla, _nsa_topk_xla
from ._kernel import apply_native_sparse_attention


@kernel_registry.register("native_sparse_attention", Platform.PALLAS, Backend.TPU)
@jaxtyping.jaxtyped(typechecker=beartype)
def native_sparse_attention(
    query: Float[Array, "batch seq_len num_q_heads head_dim"],
    key: Float[Array, "batch seq_len num_kv_heads head_dim"],
    value: Float[Array, "batch seq_len num_kv_heads head_dim"],
    g_cmp: Float[Array, "batch seq_len num_q_heads"] | None = None,
    g_slc: Float[Array, "batch seq_len num_q_heads"] | None = None,
    block_indices: Int[Array, "batch seq_len num_kv_heads num_selected_blocks"] | None = None,
    block_counts: Int[Array, "batch seq_len num_kv_heads"] | int = 16,
    block_size: int = 64,
    softmax_scale: float | None = None,
    cu_seqlens: Int[Array, "num_seqs_plus_one"] | None = None,
) -> Float[Array, "batch seq_len num_q_heads head_dim"]:
    """
    Native Sparse Attention (NSA) with Pallas TPU implementation.

    Args:
        query: Query tensor `(batch_size, sequence, num_heads, head_dim)`.
        key: Key tensor `(batch_size, sequence, num_heads, head_dim)`.
        value: Value tensor `(batch_size, sequence, num_heads, head_dim)`.
        g_cmp: Optional gate tensor for compressed attention.
        g_slc: Optional gate tensor for selected attention.
        block_indices: Optional pre-computed block indices.
        block_counts: Number of blocks to select.
        block_size: Attention block size.
        softmax_scale: Scale factor.
        cu_seqlens: Cumulative sequence lengths.
    """
    if softmax_scale is None:
        softmax_scale = float(1.0 / jnp.sqrt(query.shape[-1]))
    else:
        softmax_scale = float(softmax_scale)

    if cu_seqlens is not None:
        raise NotImplementedError("cu_seqlens not supported in Pallas NSA.")

    batch, seq_len, _num_q_heads, head_dim = query.shape
    num_kv_heads = key.shape[2]
    num_blocks = (seq_len + block_size - 1) // block_size

    pad_len = num_blocks * block_size - seq_len
    if pad_len > 0:
        k_padded = jnp.pad(key, ((0, 0), (0, pad_len), (0, 0), (0, 0)))
        v_padded = jnp.pad(value, ((0, 0), (0, pad_len), (0, 0), (0, 0)))
    else:
        k_padded = key
        v_padded = value

    k_cmp = k_padded.reshape(batch, num_blocks, block_size, num_kv_heads, head_dim).mean(axis=2)
    v_cmp = v_padded.reshape(batch, num_blocks, block_size, num_kv_heads, head_dim).mean(axis=2)
    o_cmp = None

    if g_cmp is not None:
        o_cmp, lse_cmp = _nsa_compression_xla(
            query=query,
            k_cmp=k_cmp,
            v_cmp=v_cmp,
            block_size=block_size,
            softmax_scale=softmax_scale,
        )
        if block_indices is not None:
            warnings.warn("`block_indices` will be ignored when `g_cmp` is provided", stacklevel=2)

        block_indices = _nsa_topk_xla(
            query=query,
            k_cmp=k_cmp,
            lse=lse_cmp,
            block_counts=block_counts if isinstance(block_counts, int) else int(block_counts[0, 0, 0]),
            block_size=block_size,
            softmax_scale=softmax_scale,
        )
    if block_indices is None:
        raise ValueError("Either `g_cmp` must be provided or `block_indices` must be passed.")

    o_slc = apply_native_sparse_attention(
        query=query,
        key=key,
        value=value,
        block_indices=block_indices,
        block_counts=block_counts,
        block_size=block_size,
        softmax_scale=softmax_scale,
    )

    o = o_slc
    if g_slc is not None:
        o = o_slc * jnp.expand_dims(g_slc, -1)

    if o_cmp is not None and g_cmp is not None:
        o = o + o_cmp * jnp.expand_dims(g_cmp, -1)

    return o
