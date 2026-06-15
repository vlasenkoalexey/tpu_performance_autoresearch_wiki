import os
os.environ["XLA_FLAGS"] = "--xla_force_host_platform_device_count=8"
import jax
import jax.numpy as jnp
from model.fused_rope import fused_qknorm_rope
from jax.experimental import mesh_utils
from jax.sharding import Mesh, PartitionSpec as P

mesh = Mesh(mesh_utils.create_device_mesh((8, 1)), axis_names=('fsdp', 'tp'))

B, H, T, D = 8, 32, 256, 128
x = jax.random.normal(jax.random.PRNGKey(0), (B, H, T, D))
weight = jax.random.normal(jax.random.PRNGKey(1), (D,))
cos = jax.random.normal(jax.random.PRNGKey(2), (B, T, D))
sin = jax.random.normal(jax.random.PRNGKey(3), (B, T, D))

@jax.checkpoint
def layer(x, weight, cos, sin):
    return fused_qknorm_rope(x, weight, cos, sin)

def loss(x, weight, cos, sin):
    return jnp.sum(layer(x, weight, cos, sin))

with mesh:
    # Set up sharding
    sharding_x = jax.sharding.NamedSharding(mesh, P('fsdp', None, None, None))
    sharding_weight = jax.sharding.NamedSharding(mesh, P(None))
    sharding_cos = jax.sharding.NamedSharding(mesh, P('fsdp', None, None))
    sharding_sin = jax.sharding.NamedSharding(mesh, P('fsdp', None, None))
    
    x_s = jax.device_put(x, sharding_x)
    weight_s = jax.device_put(weight, sharding_weight)
    cos_s = jax.device_put(cos, sharding_cos)
    sin_s = jax.device_put(sin, sharding_sin)

    try:
        print("Testing final gradient through checkpoint...")
        grad_fn = jax.value_and_grad(loss)
        grad_fn(x_s, weight_s, cos_s, sin_s)
        print("Success")
    except Exception as e:
        import traceback
        traceback.print_exc()
