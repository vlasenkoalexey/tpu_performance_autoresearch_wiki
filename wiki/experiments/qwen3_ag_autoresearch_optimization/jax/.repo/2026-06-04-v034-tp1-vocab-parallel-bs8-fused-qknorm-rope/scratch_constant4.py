import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def _fused_qknorm_rope_kernel(x_ref, w_ref, cos_ref, sin_ref, eps_ref, out_ref):
    x_val = x_ref[0, 0, :, :]
    w = w_ref[:]
    c = cos_ref[0, :, :]
    s = sin_ref[0, :, :]
    eps_val = eps_ref[0]
    
    # QK-norm
    x32 = x_val.astype(jnp.float32)
    var = jnp.mean(x32 * x32, axis=-1, keepdims=True)
    rsqrt = jax.lax.rsqrt(var + eps_val)
    x_norm = (x32 * rsqrt).astype(x_val.dtype)
    x_norm = x_norm * w
    
    # RoPE
    d = x_val.shape[-1]
    half_d = d // 2
    x_rot = jnp.concatenate([-x_norm[:, half_d:], x_norm[:, :half_d]], axis=-1)
    
    out_val = (x_norm * c) + (x_rot * s)
    out_ref[0, 0, :, :] = out_val.astype(out_ref.dtype)

def test():
    x = jnp.ones((1, 1, 256, 128), dtype=jnp.bfloat16)
    w = jnp.ones((128,), dtype=jnp.bfloat16)
    c = jnp.ones((1, 256, 128), dtype=jnp.bfloat16)
    s = jnp.ones((1, 256, 128), dtype=jnp.bfloat16)
    eps = jnp.array([1e-6], dtype=jnp.float32)

    return pl.pallas_call(
        _fused_qknorm_rope_kernel,
        out_shape=jax.ShapeDtypeStruct((1, 1, 256, 128), jnp.bfloat16),
        in_specs=[
            pl.BlockSpec((1, 1, 256, 128), lambda i: (0, 0, i, 0)),
            pl.BlockSpec((128,), lambda i: (0,)),
            pl.BlockSpec((1, 256, 128), lambda i: (0, i, 0)),
            pl.BlockSpec((1, 256, 128), lambda i: (0, i, 0)),
            pl.BlockSpec((1,), lambda i: (0,)),
        ],
        out_specs=pl.BlockSpec((1, 1, 256, 128), lambda i: (0, 0, i, 0)),
        grid=(1,)
    )(x, w, c, s, eps)

try:
    print(jax.make_jaxpr(test)())
except Exception as e:
    import traceback
    traceback.print_exc()
