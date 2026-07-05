import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental.pallas import tpu as pltpu

def kernel(x_ref, y_ref, *, block_size):
    idx = pl.program_id(0)
    # create a VMEM scratch ref
    scratch_ref = pl.run_scoped(
        lambda ref: pltpu.async_copy(x_ref, ref, pltpu.SemaphoreType.REGULAR).wait() or ref,
        pl.BlockSpec((block_size,), lambda: (0,), memory_space=pltpu.VMEM)
    ) # wait run_scoped syntax might be wrong
    pass

