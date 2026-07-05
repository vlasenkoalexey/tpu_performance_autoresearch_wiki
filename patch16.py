import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "    out = pl.pallas_call(\n        glu_fwd_kernel,\n        out_shape=jax.ShapeDtypeStruct((B, F), x_flat.dtype),\n        grid=grid,\n                in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda i, j, k: (i, k)),\n            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),\n            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),\n        ],\n        out_specs=pl.BlockSpec((block_b, block_f), lambda i, j, k: (i, j)),\n        scratch_shapes=[",
    "    out = pl.pallas_call(\n        glu_fwd_kernel,\n        out_shape=jax.ShapeDtypeStruct((B, F), x_flat.dtype),\n        grid=grid,\n        in_specs=[\n            pl.BlockSpec((block_b, block_d), lambda i, j, k: (i, k)),\n            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),\n            pl.BlockSpec((block_f, block_d), lambda i, j, k: (j, k)),\n        ],\n        out_specs=pl.BlockSpec((block_b, block_f), lambda i, j, k: (i, j)),\n        scratch_shapes=["
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

