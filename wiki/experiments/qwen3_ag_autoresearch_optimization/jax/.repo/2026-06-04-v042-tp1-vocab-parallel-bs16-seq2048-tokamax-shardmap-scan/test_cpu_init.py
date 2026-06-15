import jax
from flax import nnx
import numpy as np

class Linear(nnx.Module):
    def __init__(self, rngs):
        self.w = nnx.Param(jax.random.normal(rngs.params(), (1024, 1024)))

with jax.default_device(jax.devices("cpu")[0]):
    l = Linear(rngs=nnx.Rngs(0))
    
print(l.w.value.device())
