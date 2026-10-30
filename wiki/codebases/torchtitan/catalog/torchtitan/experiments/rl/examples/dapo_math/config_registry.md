---
title: 'Module: torchtitan/experiments/rl/examples/dapo_math/config_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/dapo_math/config_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.dapo_math.config_registry`/
symbols:
  _qwen3_4b_dapo_math_config: _qwen3_4b_dapo_math_config().
  rl_dapo_qwen3_4b_math_8k: rl_dapo_qwen3_4b_math_8k().
  rl_dapo_qwen3_4b_math_32k: rl_dapo_qwen3_4b_math_32k().
---
# Module: [`torchtitan/experiments/rl/examples/dapo_math/config_registry.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/config_registry.py)

## Functions
- <a id="_qwen3_4b_dapo_math_config"></a>`_qwen3_4b_dapo_math_config(*, max_response_tokens: int, max_total_tokens: int, dump_folder: str)` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/config_registry.py#L46) — Build the shared Qwen3-4B DAPO-Math configuration. — documented in [job-config](../../../../../../concepts/job-config.md)
- <a id="rl_dapo_qwen3_4b_math_32k"></a>`rl_dapo_qwen3_4b_math_32k()` — [`L163`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/config_registry.py#L163) — Run 32K responses on one node: one TP=2 trainer and six TP=1 generators.
- <a id="rl_dapo_qwen3_4b_math_8k"></a>`rl_dapo_qwen3_4b_math_8k()` — [`L154`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/config_registry.py#L154) — Run 8K responses on one node: one TP=2 trainer and six TP=1 generators.

