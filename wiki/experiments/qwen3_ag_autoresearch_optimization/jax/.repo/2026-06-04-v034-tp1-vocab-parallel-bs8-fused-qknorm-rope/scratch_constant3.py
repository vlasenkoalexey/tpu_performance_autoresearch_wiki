import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def test_pallas_constant():
    def _kernel(x_ref, eps_ref, o_ref):
        x = x_ref[...]
        eps = eps_ref[0]
        o_ref[...] = x + eps

    @jax.jit
    def test(x):
        eps_arr = jnp.array([1e-6], dtype=jnp.float32)
        return pl.pallas_call(
            _kernel,
            out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
            in_specs=[
                pl.BlockSpec(x.shape, lambda i: (0,)),
                pl.BlockSpec((1,), lambda i: (0,))
            ],
            out_specs=pl.BlockSpec(x.shape, lambda i: (0,)),
            grid=(1,)
        )(x, eps_arr)
    
    try:
        test(jnp.ones((10,), dtype=jnp.float32))
        print("Success")
    except Exception as e:
        import traceback
        traceback.print_exc()

test_pallas_constant()
