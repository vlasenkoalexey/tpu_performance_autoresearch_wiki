import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "    x_shape = jax.eval_shape(lambda: x_ref[...])\n    acc = jnp.zeros(x_shape.shape, dtype=jnp.float32)",
    "    acc = jnp.zeros((block_b, block_d), dtype=jnp.float32)"
)

text = text.replace(
    "    acc_up = jnp.zeros_like(w_up_ref[...], dtype=jnp.float32)\n    acc_gate = jnp.zeros_like(w_gate_ref[...], dtype=jnp.float32)",
    "    acc_up = jnp.zeros((block_f, block_d), dtype=jnp.float32)\n    acc_gate = jnp.zeros((block_f, block_d), dtype=jnp.float32)"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

