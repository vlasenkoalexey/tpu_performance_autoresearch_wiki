from trainer.model.modeling_qwen3 import Qwen3Model, Qwen3Config
from flax import nnx
import jax

config = Qwen3Config(num_hidden_layers=2, hidden_size=64, intermediate_size=128, num_attention_heads=2)
model = Qwen3Model(config, rngs=nnx.Rngs(0))

def _iter_params(module: nnx.Module, prefix: str = ""):
    seen = set()
    for name in sorted(vars(module).keys()):
        if name.startswith("_"):
            continue
        attr = getattr(module, name)
        path = f"{prefix}.{name}" if prefix else name
        if isinstance(attr, nnx.Param):
            if id(attr) in seen:
                continue
            seen.add(id(attr))
            yield path, attr
        elif isinstance(attr, nnx.Module):
            yield from _iter_params(attr, path)
        elif isinstance(attr, list):
            for i, elem in enumerate(attr):
                if isinstance(elem, nnx.Module):
                    yield from _iter_params(elem, f"{path}.{i}")
        elif isinstance(attr, dict):
            for k, v in attr.items():
                if isinstance(v, nnx.Module):
                    yield from _iter_params(v, f"{path}.{k}")

for path, param in _iter_params(model, "model"):
    print(path)
