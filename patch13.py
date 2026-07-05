import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "    def body_fn(f_idx, acc):\n        x = x_ref[...]",
    "    x = x_ref[...]\n    def body_fn(f_idx, acc):"
)

text = text.replace(
    "    def body_fn(b_idx, accs):\n        w_up = w_up_ref[...]\n        w_gate = w_gate_ref[...]",
    "    w_up = w_up_ref[...]\n    w_gate = w_gate_ref[...]\n    def body_fn(b_idx, accs):"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

