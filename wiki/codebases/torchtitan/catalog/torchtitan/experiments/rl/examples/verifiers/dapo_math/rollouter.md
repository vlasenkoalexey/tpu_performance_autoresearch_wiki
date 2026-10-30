---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.dapo_math.rollouter`/
symbols:
  VerifiersMathRollouter.Config: VerifiersMathRollouter#Config#
  VerifiersMathRollouter.Config.validation_dataset: VerifiersMathRollouter#Config#validation_dataset.
  VerifiersMathRollouter.Config.train_dataset: VerifiersMathRollouter#Config#train_dataset.
  VerifiersMathRollouter.Config.verifiers_env_server: VerifiersMathRollouter#Config#verifiers_env_server.
  VerifiersMathRollouter: VerifiersMathRollouter#
  _math_taskset_config: _math_taskset_config().
  VerifiersMathRollouter.Config.rubric: VerifiersMathRollouter#Config#rubric.
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py)

## Classes
### <a id="VerifiersMathRollouter"></a>`VerifiersMathRollouter`  ·  implements/extends VerifiersRollouter
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py:37`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L37)
- doc: Run DAPO-Math and AIME through a local Verifiers environment server.
- signature: `class VerifiersMathRollouter(VerifiersRollouter):`
- uses (calls/refs, reference-scoped): (1 test-only callers)
- used by: (4 test-only callers)

### <a id="VerifiersMathRollouter.Config"></a>`VerifiersMathRollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py:46`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L46)
- signature: `class Config(VerifiersRollouter.Config):`
- members:
  - <a id="VerifiersMathRollouter.Config.rubric"></a>`rubric` — [`L77`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L77)
  - <a id="VerifiersMathRollouter.Config.train_dataset"></a>`train_dataset` — [`L47`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L47)
  - <a id="VerifiersMathRollouter.Config.validation_dataset"></a>`validation_dataset` — [`L53`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L53)
  - <a id="VerifiersMathRollouter.Config.verifiers_env_server"></a>`verifiers_env_server` — [`L60`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L60)
- uses (calls/refs, reference-scoped): [`Rubric`](../../../rubrics/rubric.md#Rubric), [`Config`](../../../rubrics/rubric.md#Rubric.Config), [`reward_fns`](../../../rubrics/rubric.md#Rubric.Config.reward_fns), [`error_reward`](../../../rubrics/rubric.md#Rubric.Config.error_reward), [`weight`](../../../rubrics/rubric.md#RewardFn.Config.weight)  (14 test-only)
- used by: (3 test-only callers)

## Functions
- <a id="_math_taskset_config"></a>`_math_taskset_config(dataset: Literal["dapo_math", "aime2025"])` — [`L30`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/rollouter.py#L30)

