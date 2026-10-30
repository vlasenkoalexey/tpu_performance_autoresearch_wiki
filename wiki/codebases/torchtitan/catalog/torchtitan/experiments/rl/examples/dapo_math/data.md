---
title: 'Module: torchtitan/experiments/rl/examples/dapo_math/data.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/dapo_math/data.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.dapo_math.data`/
symbols:
  AIME2025Dataset.__init__: AIME2025Dataset#__init__().
  DapoMathDataset.__init__: DapoMathDataset#__init__().
  DapoMathSample: DapoMathSample#
  _CyclingDataset.__next__: _CyclingDataset#__next__().
  AIME2025Dataset: AIME2025Dataset#
  AIME2025Dataset.Config: AIME2025Dataset#Config#
  _CyclingDataset._order: _CyclingDataset#_order.
  DapoMathDataset: DapoMathDataset#
  DapoMathDataset.Config: DapoMathDataset#Config#
  _CyclingDataset: _CyclingDataset#
  DapoMathSample.prompt: DapoMathSample#prompt.
  DapoMathSample.ground_truth: DapoMathSample#ground_truth.
  _CyclingDataset.state_dict: _CyclingDataset#state_dict().
  _CyclingDataset.load_state_dict: _CyclingDataset#load_state_dict().
  _CyclingDataset._position: _CyclingDataset#_position.
  _CyclingDataset.__init__: _CyclingDataset#__init__().
  _CyclingDataset._rng: _CyclingDataset#_rng.
  AIME2025Dataset.Config.num_samples: AIME2025Dataset#Config#num_samples.
  _CyclingDataset.__iter__: _CyclingDataset#__iter__().
  _MATH_PROMPT_TEMPLATE: _MATH_PROMPT_TEMPLATE.
  DapoMathDataset.Config.seed: DapoMathDataset#Config#seed.
  DapoMathDataset.Config.shuffle: DapoMathDataset#Config#shuffle.
  _CyclingDataset._samples: _CyclingDataset#_samples.
  _CyclingDataset._shuffle: _CyclingDataset#_shuffle.
  DapoMathDataset.Config.repo_id: DapoMathDataset#Config#repo_id.
  DapoMathDataset.Config.split: DapoMathDataset#Config#split.
  AIME2025Dataset.Config.repo_id: AIME2025Dataset#Config#repo_id.
  AIME2025Dataset.Config.subsets: AIME2025Dataset#Config#subsets.
  AIME2025Dataset.Config.split: AIME2025Dataset#Config#split.
  AIME2025Dataset.Config.seed: AIME2025Dataset#Config#seed.
  AIME2025Dataset.Config.shuffle: AIME2025Dataset#Config#shuffle.
---
# Module: [`torchtitan/experiments/rl/examples/dapo_math/data.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py)

## Classes
### <a id="AIME2025Dataset"></a>`AIME2025Dataset`  ·  implements/extends _CyclingDataset
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L112)
- doc: Provides AIME 2025 I+II problems using the DAPO answer format.
- signature: `class AIME2025Dataset(_CyclingDataset):`
- protocol/private: <a id="AIME2025Dataset.__init__"></a>`__init__`[`L124`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L124)
- uses (calls/refs, reference-scoped): (13 test-only callers)
- used by: (6 test-only callers)

### <a id="AIME2025Dataset.Config"></a>`AIME2025Dataset.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L116)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="AIME2025Dataset.Config.num_samples"></a>`num_samples` — [`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L122)
  - <a id="AIME2025Dataset.Config.repo_id"></a>`repo_id` — [`L117`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L117)
  - <a id="AIME2025Dataset.Config.seed"></a>`seed` — [`L120`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L120)
  - <a id="AIME2025Dataset.Config.shuffle"></a>`shuffle` — [`L121`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L121)
  - <a id="AIME2025Dataset.Config.split"></a>`split` — [`L119`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L119)
  - <a id="AIME2025Dataset.Config.subsets"></a>`subsets` — [`L118`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L118)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable), [`Config`](../../../../config/configurable.md#Configurable.Config)
- used by: (6 test-only callers)

### <a id="DapoMathDataset"></a>`DapoMathDataset`  ·  implements/extends _CyclingDataset
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L85)
- doc: Provides filtered DAPO-Math problems in the original `Answer:` format.
- signature: `class DapoMathDataset(_CyclingDataset):`
- protocol/private: <a id="DapoMathDataset.__init__"></a>`__init__`[`L95`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L95)
- uses (calls/refs, reference-scoped): (11 test-only callers)
- used by: (4 test-only callers)

### <a id="DapoMathDataset.Config"></a>`DapoMathDataset.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:89`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L89)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="DapoMathDataset.Config.repo_id"></a>`repo_id` — [`L90`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L90)
  - <a id="DapoMathDataset.Config.seed"></a>`seed` — [`L92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L92)
  - <a id="DapoMathDataset.Config.shuffle"></a>`shuffle` — [`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L93)
  - <a id="DapoMathDataset.Config.split"></a>`split` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L91)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable), [`Config`](../../../../config/configurable.md#Configurable.Config)
- used by: (4 test-only callers)

### <a id="DapoMathSample"></a>`DapoMathSample`
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L27)
- doc: A math prompt paired with its expected final answer.
- signature: `class DapoMathSample:`
- members:
  - <a id="DapoMathSample.ground_truth"></a>`ground_truth` — [`L31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L31)
  - <a id="DapoMathSample.prompt"></a>`prompt` — [`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L30)
- used by: (13 test-only callers)

### <a id="_CyclingDataset"></a>`_CyclingDataset`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/dapo_math/data.py:36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L36)
- doc: Provides an endless, resumable stream over a finite sample list.
- signature: `class _CyclingDataset(Configurable):`
- members:
  - <a id="_CyclingDataset.load_state_dict"></a>`load_state_dict(self, state_dict: dict)` — [`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L78) — Restore state returned by `state_dict`.
  - <a id="_CyclingDataset.state_dict"></a>`state_dict(self)` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L70) — Snapshot row order and position so resume continues the same stream.
- protocol/private: <a id="_CyclingDataset.__init__"></a>`__init__`[`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L39), <a id="_CyclingDataset.__iter__"></a>`__iter__`[`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L56), <a id="_CyclingDataset.__next__"></a>`__next__`[`L59`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L59), <a id="_CyclingDataset._order"></a>`_order`[`L51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L51), <a id="_CyclingDataset._position"></a>`_position`[`L54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L54), <a id="_CyclingDataset._rng"></a>`_rng`[`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L49), <a id="_CyclingDataset._samples"></a>`_samples`[`L48`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L48), <a id="_CyclingDataset._shuffle"></a>`_shuffle`[`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L50)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable)  (3 test-only)
- used by: [`Configurable`](../../../../config/configurable.md#Configurable)  (4 test-only)

## Module values
- <a id="_MATH_PROMPT_TEMPLATE"></a>`_MATH_PROMPT_TEMPLATE` — [`L17`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/data.py#L17)

