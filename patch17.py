import re

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "r") as f:
    text = f.read()

text = text.replace(
    "def glu_fwd_kernel(x_ref, w_up_ref, w_gate_ref, o_ref, acc_up_ref, acc_gate_ref):\n    @pl.when(pl.program_id(2) == 0)\n    def _():\n        acc_up_ref[...] = jnp.zeros_like(acc_up_ref)\n        acc_gate_ref[...] = jnp.zeros_like(acc_gate_ref)\n    \n    acc_up_ref[...] += jnp.dot(x_ref[...], w_up_ref[...].T, preferred_element_type=acc_up_ref.dtype)\n    acc_gate_ref[...] += jnp.dot(x_ref[...], w_gate_ref[...].T, preferred_element_type=acc_gate_ref.dtype)\n    \n    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)\n    def _():\n        o_ref[...] = (acc_up_ref[...] * jax.nn.silu(acc_gate_ref[...])).astype(o_ref.dtype)",
    "def glu_fwd_kernel(x_ref, w_up_ref, w_gate_ref, o_ref, acc_up_ref, acc_gate_ref):\n    x = x_ref[...]\n    w_up = w_up_ref[...]\n    w_gate = w_gate_ref[...]\n    @pl.when(pl.program_id(2) == 0)\n    def _():\n        acc_up_ref[...] = jnp.zeros_like(acc_up_ref)\n        acc_gate_ref[...] = jnp.zeros_like(acc_gate_ref)\n    \n    acc_up_ref[...] += jnp.dot(x, w_up.T, preferred_element_type=acc_up_ref.dtype)\n    acc_gate_ref[...] += jnp.dot(x, w_gate.T, preferred_element_type=acc_gate_ref.dtype)\n    \n    @pl.when(pl.program_id(2) == pl.num_programs(2) - 1)\n    def _():\n        o_ref[...] = (acc_up_ref[...] * jax.nn.silu(acc_gate_ref[...])).astype(o_ref.dtype)"
)

with open("/mnt/disks/persist/torch-tpu/tpu_performance_autoresearch_wiki_ag_demo/wiki/experiments/qwen3_ag_autoresearch_optimization/jax/.repo/2026-06-27-v019-fused-glu-fori-splash-bwd/model/fused_glu.py", "w") as f:
    f.write(text)

