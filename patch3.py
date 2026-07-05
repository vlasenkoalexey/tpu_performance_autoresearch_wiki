import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "pl.BlockSpec((block_b, F), lambda b, d: (b, 0), memory_space=pltpu.HBM),",
    "pl.BlockSpec((block_b, F), lambda b, d: (b, 0), memory_space=pltpu.ANY),"
)

text = text.replace(
    "pl.BlockSpec((F, block_d), lambda b, d: (0, d), memory_space=pltpu.HBM),",
    "pl.BlockSpec((F, block_d), lambda b, d: (0, d), memory_space=pltpu.ANY),"
)

text = text.replace(
    "pl.BlockSpec((B, block_d), lambda f, d: (0, d), memory_space=pltpu.HBM),",
    "pl.BlockSpec((B, block_d), lambda f, d: (0, d), memory_space=pltpu.ANY),"
)

text = text.replace(
    "pl.BlockSpec((B, block_f), lambda f, d: (0, f), memory_space=pltpu.HBM),",
    "pl.BlockSpec((B, block_f), lambda f, d: (0, f), memory_space=pltpu.ANY),"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

