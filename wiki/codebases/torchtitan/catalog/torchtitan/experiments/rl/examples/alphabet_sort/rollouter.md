---
title: 'Module: torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.alphabet_sort.rollouter`/
symbols:
  AlphabetSortRollouter.Config: AlphabetSortRollouter#Config#
  AlphabetSortRollouter: AlphabetSortRollouter#
  AlphabetSortWorker.Config.rubric: AlphabetSortWorker#Config#rubric.
  AlphabetSortWorker: AlphabetSortWorker#
  AlphabetSortRollouter.Config.train_dataset: AlphabetSortRollouter#Config#train_dataset.
  AlphabetSortRollouter.Config.validation_dataset: AlphabetSortRollouter#Config#validation_dataset.
  AlphabetSortWorker.Config: AlphabetSortWorker#Config#
  AlphabetSortWorker.Config.message_env: AlphabetSortWorker#Config#message_env.
  AlphabetSortRollouter.Config.worker: AlphabetSortRollouter#Config#worker.
---
# Module: [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py)

## Classes
### <a id="AlphabetSortRollouter"></a>`AlphabetSortRollouter`  ·  implements/extends Rollouter
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py:35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L35)
- doc: Wires up the AlphabetSort task: its train/val datasets, env, and reward.
- signature: `class AlphabetSortRollouter(Rollouter):`
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter)
- used by: [`Rollouter`](../../rollout/rollouter.md#Rollouter)  (15 test-only)

### <a id="AlphabetSortRollouter.Config"></a>`AlphabetSortRollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py:63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L63)
- signature: `class Config(Rollouter.Config):`
- members:
  - <a id="AlphabetSortRollouter.Config.train_dataset"></a>`train_dataset` — [`L64`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L64)
  - <a id="AlphabetSortRollouter.Config.validation_dataset"></a>`validation_dataset` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L67)
  - <a id="AlphabetSortRollouter.Config.worker"></a>`worker` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L70)
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter), [`Config`](../../rollout/rollouter.md#Rollouter.Config)  (5 test-only)
- used by: (15 test-only callers)

### <a id="AlphabetSortWorker"></a>`AlphabetSortWorker`  ·  implements/extends RolloutWorker
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py:20`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L20)
- doc: AlphabetSort's env and reward. Pure config; all methods inherited.
- signature: `class AlphabetSortWorker(RolloutWorker):`
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)
- used by: [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)  (3 test-only)

### <a id="AlphabetSortWorker.Config"></a>`AlphabetSortWorker.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py:24`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L24)
- signature: `class Config(RolloutWorker.Config):`
- members:
  - <a id="AlphabetSortWorker.Config.message_env"></a>`message_env` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L30)
  - <a id="AlphabetSortWorker.Config.rubric"></a>`rubric` — [`L25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rollouter.py#L25)
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker), [`Rubric`](../../rubrics/rubric.md#Rubric), [`Config`](../../rubrics/rubric.md#Rubric.Config), [`Config`](../../rollout/rollouter.md#RolloutWorker.Config), [`reward_fns`](../../rubrics/rubric.md#Rubric.Config.reward_fns), [`weight`](../../rubrics/rubric.md#RewardFn.Config.weight)  (4 test-only)
- used by: (2 test-only callers)

