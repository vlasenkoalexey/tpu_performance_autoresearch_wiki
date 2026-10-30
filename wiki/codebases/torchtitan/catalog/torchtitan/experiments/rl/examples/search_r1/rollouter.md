---
title: 'Module: torchtitan/experiments/rl/examples/search_r1/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/search_r1/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.search_r1.rollouter`/
symbols:
  SearchR1Worker.Config.rubric: SearchR1Worker#Config#rubric.
  SearchR1Rollouter.Config.validation_dataset: SearchR1Rollouter#Config#validation_dataset.
  SearchR1Rollouter.Config: SearchR1Rollouter#Config#
  SearchR1Worker.Config: SearchR1Worker#Config#
  SearchR1Worker.Config.token_env: SearchR1Worker#Config#token_env.
  SearchR1Rollouter.Config.train_dataset: SearchR1Rollouter#Config#train_dataset.
  SearchR1Worker: SearchR1Worker#
  SearchR1Rollouter: SearchR1Rollouter#
  SearchR1Worker.Config.message_env: SearchR1Worker#Config#message_env.
  SearchR1Rollouter.Config.worker: SearchR1Rollouter#Config#worker.
---
# Module: [`torchtitan/experiments/rl/examples/search_r1/rollouter.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py)

## Classes
### <a id="SearchR1Rollouter"></a>`SearchR1Rollouter`  ·  implements/extends Rollouter
- def: [`torchtitan/experiments/rl/examples/search_r1/rollouter.py:50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L50)
- doc: Search-R1 rollouter: the QA datasets, the multi-turn search env, and the
- signature: `class SearchR1Rollouter(Rollouter):`
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter)
- used by: [`Rollouter`](../../rollout/rollouter.md#Rollouter)  (3 test-only)

### <a id="SearchR1Rollouter.Config"></a>`SearchR1Rollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/search_r1/rollouter.py:57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L57)
- signature: `class Config(Rollouter.Config):`
- members:
  - <a id="SearchR1Rollouter.Config.train_dataset"></a>`train_dataset` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L58)
  - <a id="SearchR1Rollouter.Config.validation_dataset"></a>`validation_dataset` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L63)
  - <a id="SearchR1Rollouter.Config.worker"></a>`worker` — [`L73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L73)
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter), [`Config`](../../rollout/rollouter.md#Rollouter.Config)  (8 test-only)
- used by: (3 test-only callers)

### <a id="SearchR1Worker"></a>`SearchR1Worker`  ·  implements/extends RolloutWorker
- def: [`torchtitan/experiments/rl/examples/search_r1/rollouter.py:21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L21)
- doc: Search-R1's multi-turn search env and rubric.
- signature: `class SearchR1Worker(RolloutWorker):`
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)
- used by: [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)  (4 test-only)

### <a id="SearchR1Worker.Config"></a>`SearchR1Worker.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/search_r1/rollouter.py:28`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L28)
- signature: `class Config(RolloutWorker.Config):`
- members:
  - <a id="SearchR1Worker.Config.message_env"></a>`message_env` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L42)
  - <a id="SearchR1Worker.Config.rubric"></a>`rubric` — [`L29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L29)
  - <a id="SearchR1Worker.Config.token_env"></a>`token_env` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rollouter.py#L43)
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker), [`Rubric`](../../rubrics/rubric.md#Rubric), [`TokenEnv`](../../environment/token.md#TokenEnv), [`Config`](../../rubrics/rubric.md#Rubric.Config), [`Config`](../../environment/token.md#TokenEnv.Config), [`Config`](../../rollout/rollouter.md#RolloutWorker.Config), [`reward_fns`](../../rubrics/rubric.md#Rubric.Config.reward_fns), [`max_num_turns`](../../environment/token.md#TokenEnv.Config.max_num_turns), [`weight`](../../rubrics/rubric.md#RewardFn.Config.weight), [`max_rollout_tokens`](../../environment/token.md#TokenEnv.Config.max_rollout_tokens), [`truncation_reward`](../../rubrics/rubric.md#Rubric.Config.truncation_reward)  (4 test-only)
- used by: (4 test-only callers)

