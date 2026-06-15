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
        @nnx.split_rngs(splits=2)
        @nnx.vmap(in_axes=(0,), out_axes=0)
        def create_blocks(rngs1):
            @nnx.split_rngs(splits=4)
            @nnx.vmap(in_axes=(0,), out_axes=0)
            def create_layers(rngs2):
                return DummyLayer(rngs=rngs2)
            return create_layers(rngs1)
        self.blocks = create_blocks(rngs)
        
    def __call__(self, x):
        @nnx.scan(in_axes=(nnx.Carry, 0), out_axes=nnx.Carry)
        @nnx.remat
        def scan_blocks(x, block):
            @nnx.scan(in_axes=(nnx.Carry, 0), out_axes=nnx.Carry)
            def scan_layers(x, layer):
                return layer(x)
            return scan_layers(x, block)
        return scan_blocks(x, self.blocks)

model = DummyModel(rngs=nnx.Rngs(0))
x = jnp.ones((10,))
try:
    y = model(x)
    print("Success:", y.shape)
    _, state = nnx.split(model)
    print("Keys:", state.keys())
    print("Shape:", state['blocks']['w'].value.shape)
except Exception as e:
    print("Error:", type(e).__name__, e)
