import jax
import jax.numpy as jnp
from jax.experimental.shard_map import shard_map
from jax.sharding import PartitionSpec as P
from jax.lax import psum
import tokamax

mesh = jax.make_mesh((1,), ("fsdp",))
x = jnp.ones((2, 4))
y = jnp.array([0, 1])
w = jnp.ones((4, 10))

with mesh:
    def _sharded_ce(x_sharded, y_sharded, w_sharded):
        loss_sum = tokamax.linear_softmax_cross_entropy_loss(x_sharded, y_sharded, w_sharded, reduction='sum')
        return psum(loss_sum, 'fsdp')

    loss = shard_map(
        _sharded_ce, mesh,
        in_specs=(P('fsdp', None), P('fsdp'), P(None, None)),
        out_specs=P()
    )(x, y, w)
    
    print(loss)
