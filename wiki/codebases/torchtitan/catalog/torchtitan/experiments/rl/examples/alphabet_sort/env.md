---
title: 'Module: torchtitan/experiments/rl/examples/alphabet_sort/env.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/alphabet_sort/env.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.alphabet_sort.env`/AlphabetSortEnv#
symbols:
  AlphabetSortEnv.step: step().
  AlphabetSortEnv._next_turn: _next_turn.
  AlphabetSortEnv: ''
  AlphabetSortEnv.Config: Config#
  AlphabetSortEnv.__init__: __init__().
  AlphabetSortEnv._env_input: _env_input.
  AlphabetSortEnv.init: init().
---
# Module: [`torchtitan/experiments/rl/examples/alphabet_sort/env.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py)

## Classes
### <a id="AlphabetSortEnv"></a>`AlphabetSortEnv`  ·  implements/extends MessageEnv
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/env.py:21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L21)
- doc: Runs one AlphabetSort sample as a chat: ask the model to sort a list of names, turn by turn.
- signature: `class AlphabetSortEnv(MessageEnv):`
- members:
  - <a id="AlphabetSortEnv.init"></a>`init(self)` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L42) — Ask the model to sort the first batch of names.
  - <a id="AlphabetSortEnv.step"></a>`step(self, completion_message: Message)` — [`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L57) — Introduce the next batch of new names to re-sort, or end the rollout if none are left.
- protocol/private: <a id="AlphabetSortEnv.__init__"></a>`__init__`[`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L39), <a id="AlphabetSortEnv._env_input"></a>`_env_input`[`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L40), <a id="AlphabetSortEnv._next_turn"></a>`_next_turn`[`L45`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L45)
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`MessageEnvStepOutput`](../../environment/message.md#MessageEnvStepOutput), [`env_messages`](../../environment/message.md#MessageEnvStepOutput.env_messages), [`MessageEnvInitOutput`](../../environment/message.md#MessageEnvInitOutput), [`done`](../../environment/message.md#MessageEnvStepOutput.done), [`init_prompt_messages`](../../environment/message.md#MessageEnvInitOutput.init_prompt_messages)  (4 test-only)
- used by: [`MessageEnv`](../../environment/message.md#MessageEnv), [`step`](../../environment/message.md#MessageEnv.step), [`init`](../../environment/message.md#MessageEnv.init)  (4 test-only)

### <a id="AlphabetSortEnv.Config"></a>`AlphabetSortEnv.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/env.py:36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/env.py#L36)
- signature: `class Config(MessageEnv.Config):`
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`Config`](../../environment/message.md#MessageEnv.Config)
- used by: (5 test-only callers)

