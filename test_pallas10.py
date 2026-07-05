import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def kernel(x_ref, y_ref, scratch_ref, *, block_size):
    idx = pl.program_id(0)
    # create a slice ref?
    # No, async_copy takes src_ref, dst_ref
    # wait, how to pass indices to async_copy?
    pass

print(help(pltpu.async_copy))
