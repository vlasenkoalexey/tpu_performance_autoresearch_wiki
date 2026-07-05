import os
os.environ["JAX_PLATFORMS"] = "cpu"
import jax
import jax.numpy as jnp
from flax import nnx

class MLP(nnx.Module):
    def __init__(self, rngs):
        self.w1 = nnx.Param(jax.random.normal(rngs(), (10, 100)))
        self.w2 = nnx.Param(jax.random.normal(rngs(), (100, 10)))
    
    @nnx.remat
    def __call__(self, x):
        h = x @ self.w1.value
        h = jax.nn.relu(h)
        return h @ self.w2.value

class ScannedMLP(nnx.Module):
    def __init__(self, rngs):
        @nnx.split_rngs(splits=12)
        @nnx.vmap(in_axes=(0,), out_axes=0)
        def create_layer(rngs):
            return MLP(rngs=rngs)
        self.layers = create_layer(rngs)
        
    def __call__(self, x):
        @nnx.scan(in_axes=(nnx.Carry, 0), out_axes=nnx.Carry)
        def forward(hs, layer):
            return layer(hs)
        return forward(x, self.layers)

m = ScannedMLP(nnx.Rngs(0))
x = jnp.ones((4, 1024, 10))

def f(m, x):
    return jnp.sum(m(x))
grad_fn = jax.value_and_grad(f)

hlo = jax.jit(grad_fn).lower(m, x).compiler_ir()
hlo_text = str(hlo)
if "12x4x1024x100" in hlo_text:
    print("UNROLLED OR SAVED ACTIVATIONS!")
else:
    print("NOT SAVED! SUCCESS")
