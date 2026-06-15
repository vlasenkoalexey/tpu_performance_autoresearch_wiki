import jax
import jax.numpy as jnp
from flax import nnx

class DummyLayer(nnx.Module):
    def __init__(self, rngs):
        self.w = nnx.Param(jax.random.normal(rngs(), (10, 10)))
    def __call__(self, x):
        return x @ self.w.value

class DummyModel(nnx.Module):
    def __init__(self, rngs):
        @nnx.split_rngs(splits=4)
        @nnx.vmap(in_axes=(0,), out_axes=0)
        def create_layer(local_rngs):
            return DummyLayer(rngs=local_rngs)
        self.layers = create_layer(rngs)
        
    def __call__(self, x):
        return self.layers[0](x)

model = DummyModel(rngs=nnx.Rngs(0))
x = jnp.ones((10,))
try:
    y = model(x)
    print("Success:", y.shape)
except Exception as e:
    print("Error:", type(e).__name__, e)
