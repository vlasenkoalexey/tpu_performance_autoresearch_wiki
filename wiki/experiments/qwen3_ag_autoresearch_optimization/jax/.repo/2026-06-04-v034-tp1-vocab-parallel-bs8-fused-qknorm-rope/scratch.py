import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl

def test_pallas(x):
    B, H, T, D = x.shape
    block_size = 128
    
    def kernel(x_ref, out_ref):
        # x_ref has shape (1, 1, block_size, D)
        out_ref[0, 0, :, :] = x_ref[0, 0, :, :]
        
    out = pl.pallas_call(
        kernel,
        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
        grid=(B, H, T // block_size),
        in_specs=[
            pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
        ],
        out_specs=pl.BlockSpec((1, 1, block_size, D), lambda b, h, t: (b, h, t, 0)),
        interpret=True
    )(x)
    return out

x = jax.numpy.zeros((2, 4, 256, 128))
out = test_pallas(x)
print(out.shape)
