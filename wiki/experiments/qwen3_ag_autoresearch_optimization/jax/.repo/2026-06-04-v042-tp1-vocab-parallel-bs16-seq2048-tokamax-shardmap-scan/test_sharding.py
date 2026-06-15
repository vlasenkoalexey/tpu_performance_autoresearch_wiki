from trainer.model.modeling_qwen3 import Qwen3ForCausalLM, Qwen3Config
from trainer.model.sharding import build_plan, _iter_params, _process_sharding_name, SHARDING_PLAN
from flax import nnx
import jax

config = Qwen3Config(num_hidden_layers=2, hidden_size=64, intermediate_size=128, num_attention_heads=2)
model = Qwen3ForCausalLM(config, rngs=nnx.Rngs(0))

for path, _ in _iter_params(model):
    name = _process_sharding_name(path)
    spec = SHARDING_PLAN.get(name)
    if spec is None:
        print(f"UNMATCHED: {path} -> {name}")
    else:
        print(f"MATCHED: {path} -> {name} -> {spec}")
