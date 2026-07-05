import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def kernel(x_ref, y_ref, *, block_size):
    idx = pl.program_id(0)
    x_chunk = x_ref[pl.ds(idx * block_size, block_size)]
    y_ref[...] = x_chunk * 2.0

@jax.jit
def test_call(x):
    B = x.shape[0]
    block_size = 128
    return pl.pallas_call(
        lambda x_ref, y_ref: kernel(x_ref, y_ref, block_size=block_size),
        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
        grid=(B // block_size,),
        in_specs=[pl.BlockSpec((B,), lambda i: (0,), memory_space=pltpu.HBM)],
        out_specs=pl.BlockSpec((block_size,), lambda i: (i,)),
        compiler_params=pltpu.CompilerParams(dimension_semantics=('parallel',))
    )(x)

x = jnp.arange(128, dtype=jnp.float32)
print(test_call(x))
