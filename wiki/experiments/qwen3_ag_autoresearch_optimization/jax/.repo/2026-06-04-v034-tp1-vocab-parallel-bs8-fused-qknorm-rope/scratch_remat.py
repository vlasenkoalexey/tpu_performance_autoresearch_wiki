import os
os.environ["XLA_FLAGS"] = "--xla_force_host_platform_device_count=8"
import jax
import jax.numpy as jnp

@jax.custom_vjp
def my_op(x):
    # This is a dummy op that throws if JVP is called
    return jax.lax.stop_gradient(x) * 2

def my_op_fwd(x):
    return my_op(x), x

def my_op_bwd(res, g):
    return (g * 2,)

my_op.defvjp(my_op_fwd, my_op_bwd)

@jax.checkpoint
def layer(x):
    return my_op(x)

def loss(x):
    return jnp.sum(layer(x))

try:
    x = jnp.ones((10,), dtype=jnp.float32)
    print("Testing grad through checkpoint with dummy op...")
    jax.grad(loss)(x)
    print("Success")
except Exception as e:
    import traceback
    traceback.print_exc()
