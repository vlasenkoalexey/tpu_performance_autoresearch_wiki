import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def _kernel(x_ref, w_ref, o_ref):
    x = x_ref[...]
    w = w_ref[...]
    out = jnp.mean(x, axis=-1, keepdims=True)
    o_ref[...] = out

def test():
    x = jnp.ones((1, 128), dtype=jnp.float32)
    w = jnp.ones((128,), dtype=jnp.float32)
    return pl.pallas_call(
        _kernel,
        out_shape=jax.ShapeDtypeStruct((1, 1), jnp.float32),
        in_specs=[
            pl.BlockSpec((1, 128), lambda i: (i, 0)),
            pl.BlockSpec((128,), lambda i: (0,))
        ],
        out_specs=pl.BlockSpec((1, 1), lambda i: (i, 0)),
        grid=(1,)
    )(x, w)

test()
