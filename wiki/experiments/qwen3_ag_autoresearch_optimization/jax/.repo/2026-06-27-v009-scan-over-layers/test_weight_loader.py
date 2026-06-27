import jax.numpy as jnp
from model import Qwen3ForCausalLM
from flax import nnx
import transformers

c = transformers.AutoConfig.from_pretrained("Qwen/Qwen3-8B")
# Create a tiny model
c.num_hidden_layers = 1
m = Qwen3ForCausalLM(c, rngs=nnx.Rngs(0))

from model.weight_loader import get_param

print(get_param(m, "model.layers.0.self_attn.q_proj.weight"))
