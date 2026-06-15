import jax
import jax.numpy as jnp

@jax.custom_vjp
def my_op(x):
    # This is the function that JAX tracing sees for JVP/linearize!
    # So we use standard ops here!
    return x * 2.0

def fwd(x):
    # This is the actual forward pass executed!
    # We can use our non-linearizable op here!
    from jax.core import CallPrimitive
    # Let's simulate a non-linearizable op by using stop_gradient or something else?
    # Wait, JAX evaluates fwd(x) directly!
    print("Executing fwd with non-linearizable op")
    return x * 2.0, x

def bwd(res, g):
    return (g * 100.0,)

my_op.defvjp(fwd, bwd)

@jax.checkpoint
def layer(x):
    return my_op(x)

def loss(x):
    return jnp.sum(layer(x))

jax.grad(loss)(jnp.ones(10))
