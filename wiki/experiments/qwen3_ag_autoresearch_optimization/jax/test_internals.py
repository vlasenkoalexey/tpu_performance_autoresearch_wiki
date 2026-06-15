import jax.numpy as jnp
import torch
import numpy as np
from transformers import Qwen3Config, Qwen3ForCausalLM
from model import Qwen3ForCausalLM as FlaxQwen3ForCausalLM
from model import load_hf_state_dict
from flax import nnx
import jax

cfg = Qwen3Config(
    vocab_size=256,
    hidden_size=64,
    intermediate_size=128,
    num_hidden_layers=4,
    num_attention_heads=4,
    num_key_value_heads=2,
    head_dim=16,
    max_position_embeddings=64,
    tie_word_embeddings=False,
    rms_norm_eps=1e-6,
)

torch.manual_seed(0)
ref = Qwen3ForCausalLM(cfg).to(torch.float32).eval()
input_ids = torch.randint(0, cfg.vocab_size, (1, 16))

model = FlaxQwen3ForCausalLM(cfg, weights_dtype=jnp.float32, compute_dtype=jnp.float32, rngs=nnx.Rngs(0))
load_hf_state_dict(model, ref.state_dict(), dtype=jnp.float32)

with torch.no_grad():
    hidden_ref = ref.model.embed_tokens(input_ids)
    print("embed_tokens diff:", np.max(np.abs(model.model.embed_tokens(input_ids.numpy()) - hidden_ref.numpy())))
    
    pos_ids = torch.arange(16).unsqueeze(0)
    cos, sin = ref.model.rotary_emb(hidden_ref, pos_ids)
    jcos, jsin = model.model.rotary_emb(pos_ids.numpy(), jnp.float32)
    print("cos diff:", np.max(np.abs(cos.numpy() - jcos)))
    print("sin diff:", np.max(np.abs(sin.numpy() - jsin)))
    
    layer = ref.model.layers[0]
    jlayer = model.model.layers
    
    attn_mask = ref.model._update_causal_mask(None, input_ids, None, None)
    
    h_norm_ref = layer.input_layernorm(hidden_ref)
    h_norm_jax = jlayer.input_layernorm(hidden_ref.numpy())
    print("input_layernorm diff:", np.max(np.abs(h_norm_ref.numpy() - h_norm_jax)))
    
    attn_ref, _ = layer.self_attn(h_norm_ref, position_embeddings=(cos, sin), attention_mask=attn_mask)
    attn_jax = jlayer.self_attn(h_norm_jax, position_embeddings=(jcos, jsin), attention_mask=None)
    print("attn diff:", np.max(np.abs(attn_ref.numpy() - attn_jax)))
    
    q_ref = layer.self_attn.q_proj(h_norm_ref).view(1, 16, 4, 16).transpose(1, 2)
    q_jax = jlayer.self_attn.q_proj(h_norm_jax).reshape(1, 16, 4, 16).transpose((0, 2, 1, 3))
    print("q_proj diff:", np.max(np.abs(q_ref.numpy() - q_jax)))

    qn_ref = layer.self_attn.q_norm(q_ref.transpose(1, 2)).transpose(1, 2)
    qn_jax = jlayer.self_attn.q_norm(q_jax)
    print("q_norm diff:", np.max(np.abs(qn_ref.numpy() - qn_jax)))

    # SwiGLU diff
    mlp_ref = layer.mlp(hidden_ref)
    mlp_jax = jlayer.mlp(hidden_ref.numpy())
    print("mlp diff:", np.max(np.abs(mlp_ref.numpy() - mlp_jax)))

