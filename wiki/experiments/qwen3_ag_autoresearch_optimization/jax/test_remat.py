import jax
import jax.numpy as jnp
from flax import nnx

class MLP(nnx.Module):
    def __init__(self, din, dout, rngs):
        self.linear = nnx.Linear(din, dout, rngs=rngs)
    def __call__(self, x):
        return self.linear(x)

m = MLP(10, 10, rngs=nnx.Rngs(0))
x = jnp.ones((10, 10))

# Can we remat an instance?
m_remat = nnx.remat(m)
y = m_remat(x)
print("m_remat(x) worked:", y.shape)

