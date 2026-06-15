import os
os.environ["XLA_FLAGS"] = "--xla_force_host_platform_device_count=8"
import jax
import jax.numpy as jnp
from jax.experimental import pallas as pl
from jax.experimental import mesh_utils
from jax.sharding import Mesh, PartitionSpec as P

@jax.custom_vjp
def my_op(x):
    # Primal function uses standard ops for linearize
    return x * 2.0

def fwd(x):
    def _kernel(x_ref, o_ref):
        o_ref[...] = x_ref[...]
    
    out = pl.pallas_call(
        _kernel,
        out_shape=jax.ShapeDtypeStruct(x.shape, x.dtype),
        in_specs=[pl.BlockSpec(x.shape, lambda: (0,))],
        out_specs=pl.BlockSpec(x.shape, lambda: (0,)),
        grid=()
    )(x)
    return out, x

def bwd(res, g):
    return (g * 100.0,)

my_op.defvjp(fwd, bwd)

@jax.checkpoint
def layer(x):
    return my_op(x)

def loss(x):
    return jnp.sum(layer(x))

try:
    x = jnp.ones((10,), dtype=jnp.float32)
    print("Testing trick with pallas...")
    jax.grad(loss)(x)
    print("Success")
except Exception as e:
    import traceback
    traceback.print_exc()
