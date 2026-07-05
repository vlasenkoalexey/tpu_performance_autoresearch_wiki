import jax
import jax.numpy as jnp
from jax.sharding import Mesh, PartitionSpec as P, NamedSharding
from jax.experimental.shard_map import shard_map
from jax.experimental import mesh_utils
from model.fused_glu import fused_glu

mesh = Mesh(mesh_utils.create_device_mesh((jax.device_count(),)), axis_names=("fsdp",))

@jax.jit
def train_step(x, w_up, w_gate):
    x = jax.device_put(x, NamedSharding(mesh, P("fsdp", None, None)))
    w_up = jax.device_put(w_up, NamedSharding(mesh, P(None, "fsdp")))
    w_gate = jax.device_put(w_gate, NamedSharding(mesh, P(None, "fsdp")))
    
    mapped_glu = shard_map(
        fused_glu,
        mesh=mesh,
        in_specs=(P("fsdp", None, None), P(None, None), P(None, None)),
        out_specs=P("fsdp", None, None),
        check_rep=False
    )
    return mapped_glu(x, w_up, w_gate)

x = jnp.ones((16, 2048, 1024), dtype=jnp.bfloat16)
w_up = jnp.ones((1024, 1024), dtype=jnp.bfloat16)
w_gate = jnp.ones((1024, 1024), dtype=jnp.bfloat16)

out = train_step(x, w_up, w_gate)
print("Out shape:", out.shape)
