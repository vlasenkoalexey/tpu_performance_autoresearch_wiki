import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax._src.pallas.pallas_call import _trace_kernel_to_jaxpr
from jax.experimental.pallas.core import GridMapping, BlockMapping, Blocked

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


def test_trace():
    x_shape = (1, 1, 256, 128)
    x_aval = jax.core.ShapedArray(x_shape, jnp.float32)
    w_aval = jax.core.ShapedArray((128,), jnp.float32)
    c_aval = jax.core.ShapedArray((1, 256, 128), jnp.float32)
    s_aval = jax.core.ShapedArray((1, 256, 128), jnp.float32)
    eps_aval = jax.core.ShapedArray((1,), jnp.float32)
    
    in_avals = (x_aval, w_aval, c_aval, s_aval, eps_aval)
    out_avals = (x_aval,)
    
    # This is rough, let's just use jax.make_jaxpr directly on the kernel wrapper
    pass

# We can just check the consts returned by _trace_kernel_to_jaxpr
def trace():
    from jax._src.pallas.pallas_call import pallas_call_p
    # Easiest way: monkeypatch _trace_kernel_to_jaxpr inside pallas_call or just run pallas_call
    # and catch the error if it captures consts. But pallas_call does raise ValueError if consts!
    pass

