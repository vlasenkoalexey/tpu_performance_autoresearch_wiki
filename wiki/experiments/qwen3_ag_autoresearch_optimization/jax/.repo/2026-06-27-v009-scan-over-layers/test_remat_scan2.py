import os
import jax
import jax.numpy as jnp
from flax import nnx
import transformers
from model import Qwen3ForCausalLM
from model.weight_loader import get_param, load_hf_state_dict
import numpy as np

c = transformers.AutoConfig.from_pretrained('Qwen/Qwen3-8B')
c.num_hidden_layers = 2
m1 = Qwen3ForCausalLM(c, rngs=nnx.Rngs(0))
m2 = transformers.Qwen2ForCausalLM(c) # use Qwen2 as ref, it's same architecture
m2.eval()

# Check gradients with and without remat
def test_grad(use_remat):
    os.environ["JAX_REMAT"] = str(int(use_remat))
    m = Qwen3ForCausalLM(c, rngs=nnx.Rngs(0))
    # mock load
    
    @jax.jit
    def train_step(m, x):
        def loss_fn(m, x):
            return jnp.sum(m(x)**2)
        return jax.value_and_grad(loss_fn, argnums=0)(m, x)
        
    x = jnp.ones((1, 10), dtype=jnp.int32)
    loss, grad = train_step(m, x)
    return loss, grad.model.scanned_layers.layers.self_attn.q_proj.weight.value

l0, g0 = test_grad(False)
l1, g1 = test_grad(True)

print("loss diff:", jnp.max(jnp.abs(l0 - l1)))
print("grad diff:", jnp.max(jnp.abs(g0 - g1)))
