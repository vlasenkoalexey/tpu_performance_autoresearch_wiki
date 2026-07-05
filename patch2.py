import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "memory_space=pltpu.ANY",
    "memory_space=pltpu.HBM"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

