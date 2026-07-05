import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((B, F), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0)),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda b, d: (b, d)),\n            pl.BlockSpec((B, F), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((F, D), lambda b, d: (0, 0), memory_space=pltpu.HBM),\n        ],"
)

text = text.replace(
    "        in_specs=[\n            pl.BlockSpec((B, D), lambda f, d: (0, 0)),\n            pl.BlockSpec((B, F), lambda f, d: (0, 0)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],",
    "        in_specs=[\n            pl.BlockSpec((B, D), lambda f, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((B, F), lambda f, d: (0, 0), memory_space=pltpu.HBM),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n            pl.BlockSpec((block_f, block_d), lambda f, d: (f, d)),\n        ],"
)

text = text.replace(
    "def fused_glu_bwd(g, x, w_up, w_gate, block_b=512, block_f=512, block_d=512):",
    "def fused_glu_bwd(g, x, w_up, w_gate, block_b=128, block_f=128, block_d=128):"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

