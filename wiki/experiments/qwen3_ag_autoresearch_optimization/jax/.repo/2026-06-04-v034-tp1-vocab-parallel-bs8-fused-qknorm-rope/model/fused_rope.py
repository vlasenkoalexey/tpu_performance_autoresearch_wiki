import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def _fused_qknorm_rope_kernel(x_ref, w_ref, cos_ref, sin_ref, out_ref, eps):
    # x_ref: [1, 1, block_size, D]
    # w_ref: [D]
    # cos_ref: [1, block_size, D]
    # sin_ref: [1, block_size, D]
    # out_ref: [1, 1, block_size, D]
    x = x_ref[0, 0, :, :]
    w = w_ref[:]
    cos = cos_ref[0, :, :]
    sin = sin_ref[0, :, :]
    
    # QK-norm
    x32 = x.astype(jnp.float32)
    var = jnp.mean(x32 * x32, axis=-1, keepdims=True)
    rsqrt = jax.lax.rsqrt(var + eps)
    x_norm = (x32 * rsqrt).astype(x.dtype)
    x_norm = x_norm * w
    
    # RoPE
    d = x.shape[-1]
    half_d = d // 2
    x_rot = jnp.concatenate([-x_norm[:, half_d:], x_norm[:, :half_d]], axis=-1)
    
    out = (x_norm * cos) + (x_rot * sin)
    out_ref[0, 0, :, :] = out.astype(out_ref.dtype)

def fused_qknorm_rope(x, weight, cos, sin, eps=1e-6):
    """
    Applies RMSNorm followed by RoPE in a single Pallas kernel.
    x: [B, H, T, D]
    weight: [D]
    cos: [B, T, D]
    sin: [B, T, D]
    out: [B, H, T, D]
    """
    B, H, T, D = x.shape
    block_size = min(256, T)
    if T % block_size != 0:
        raise ValueError(f"T ({T}) must be divisible by block_size ({block_size})")

    out = pl.pallas_call(
        _fused_qknorm_rope_kernel,
        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
        grid=(B, H, T // block_size),
        in_specs=[
            pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
            pl.BlockSpec((D,), lambda b, h, t: (0,)),
            pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
            pl.BlockSpec((1, block_size, D), lambda b, h, t: (b, t, 0)),
        ],
        out_specs=pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
        eps=eps
    )(x, weight, cos, sin)
    return out
