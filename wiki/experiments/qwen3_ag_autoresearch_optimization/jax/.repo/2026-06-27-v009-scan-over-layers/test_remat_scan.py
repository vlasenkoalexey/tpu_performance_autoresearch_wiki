import jax
import jax.numpy as jnp
from flax import nnx

class Qwen3DecoderLayer(nnx.Module):
    def __init__(self, config, layer_idx, rngs=None):
        self.w = nnx.Param(jax.random.normal(rngs.params(), (1,)))
    def __call__(self, x, position_embeddings, attention_mask=None):
        return x + self.w.value * position_embeddings

class ScannedLayers(nnx.Module):
    def __init__(self, config, num_layers, rngs):
        @nnx.split_rngs(splits=num_layers)
        @nnx.vmap(in_axes=(0,), out_axes=0)
        def create_layer(rngs: nnx.Rngs):
            return Qwen3DecoderLayer(config, 0, rngs=rngs)
            
        self.layers = create_layer(rngs)
        
    def __call__(self, hidden_states, position_embeddings, attention_mask=None):
        import os
        use_remat = os.environ.get("JAX_REMAT", "0") == "1"
        
        @nnx.scan(in_axes=(nnx.Carry, 0, None, None), out_axes=nnx.Carry)
        def forward(hs, layer, pos_emb, mask):
            if use_remat:
                return nnx.remat(layer)(hs, pos_emb, mask)
            return layer(hs, pos_emb, mask)
            
        return forward(hidden_states, self.layers, position_embeddings, attention_mask)

class DummyModel(nnx.Module):
    def __init__(self):
        rngs = nnx.Rngs(0)
        self.scanned = ScannedLayers(None, 4, rngs)
    
    def __call__(self, x):
        return self.scanned(x, 1.0, None)

@jax.jit
def train_step(m, x):
    def loss_fn(m, x):
        return jnp.sum(m(x)**2)
    return jax.value_and_grad(loss_fn, argnums=0)(m, x)

m1 = DummyModel()
m2 = DummyModel()
m2.scanned.layers.w.value = m1.scanned.layers.w.value

import os
os.environ["JAX_REMAT"] = "0"
loss1, grad1 = train_step(m1, jnp.ones((1,)))

os.environ["JAX_REMAT"] = "1"
loss2, grad2 = train_step(m2, jnp.ones((1,)))

print("loss diff:", jnp.max(jnp.abs(loss1 - loss2)))
print("grad diff:", jnp.max(jnp.abs(grad1.scanned.layers.w.value - grad2.scanned.layers.w.value)))
