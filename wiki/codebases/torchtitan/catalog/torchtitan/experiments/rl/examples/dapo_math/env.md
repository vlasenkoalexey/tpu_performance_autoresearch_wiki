---
title: 'Module: torchtitan/experiments/rl/examples/dapo_math/env.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/dapo_math/env.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.dapo_math.env`/DapoMathEnv#
symbols:
  DapoMathEnv.Config: Config#
  DapoMathEnv: ''
  DapoMathEnv.init: init().
  DapoMathEnv.__init__: __init__().
  DapoMathEnv.step: step().
  DapoMathEnv._prompt: _prompt.
---
# Module: [`torchtitan/experiments/rl/examples/dapo_math/env.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py)

## Classes
### <a id="DapoMathEnv"></a>`DapoMathEnv`  ·  implements/extends MessageEnv
- def: [`torchtitan/experiments/rl/examples/dapo_math/env.py:21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L21)
- doc: Single-turn message environment for a verifiable math problem.
- signature: `class DapoMathEnv(MessageEnv):`
- members:
  - <a id="DapoMathEnv.init"></a>`init(self)` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L32) — Return the problem as one user message.
  - <a id="DapoMathEnv.step"></a>`step(self, completion_message: Message)` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L38) — End after the model's first response; the rubric scores its final answer.
- protocol/private: <a id="DapoMathEnv.__init__"></a>`__init__`[`L28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L28), <a id="DapoMathEnv._prompt"></a>`_prompt`[`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L30)
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`MessageEnvStepOutput`](../../environment/message.md#MessageEnvStepOutput), [`MessageEnvInitOutput`](../../environment/message.md#MessageEnvInitOutput), [`done`](../../environment/message.md#MessageEnvStepOutput.done), [`init_prompt_messages`](../../environment/message.md#MessageEnvInitOutput.init_prompt_messages)  (3 test-only)
- used by: [`MessageEnv`](../../environment/message.md#MessageEnv), [`step`](../../environment/message.md#MessageEnv.step), [`init`](../../environment/message.md#MessageEnv.init)  (2 test-only)

### <a id="DapoMathEnv.Config"></a>`DapoMathEnv.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/env.py:25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/env.py#L25)
- signature: `class Config(MessageEnv.Config):`
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`Config`](../../environment/message.md#MessageEnv.Config)
- used by: (3 test-only callers)

