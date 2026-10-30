---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/components/data.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/components/data.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.components.data`/
symbols:
  VerifiersTaskDataset.__init__: VerifiersTaskDataset#__init__().
  VerifiersTaskDataset: VerifiersTaskDataset#
  VerifiersTaskDataset.Config: VerifiersTaskDataset#Config#
  VerifiersTaskDataset.Config.verifiers_taskset: VerifiersTaskDataset#Config#verifiers_taskset.
  VerifiersTaskDataset.Config.to_dict: VerifiersTaskDataset#Config#to_dict().
  VerifiersTaskDataset.Config.num_tasks: VerifiersTaskDataset#Config#num_tasks.
  VerifiersTaskSample: VerifiersTaskSample#
  register_local_taskset_alias: register_local_taskset_alias().
  VerifiersTaskDataset.Config.seed: VerifiersTaskDataset#Config#seed.
  VerifiersTaskDataset.__next__: VerifiersTaskDataset#__next__().
  VerifiersTaskDataset.Config.shuffle: VerifiersTaskDataset#Config#shuffle.
  VerifiersTaskDataset._iterator: VerifiersTaskDataset#_iterator.
  VerifiersTaskDataset.Config.__post_init__: VerifiersTaskDataset#Config#__post_init__().
  VerifiersTaskDataset.__iter__: VerifiersTaskDataset#__iter__().
  VerifiersTaskDataset.state_dict: VerifiersTaskDataset#state_dict().
  VerifiersTaskDataset.load_state_dict: VerifiersTaskDataset#load_state_dict().
  VerifiersTaskSample.verifiers_task_data: VerifiersTaskSample#verifiers_task_data.
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/components/data.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py)

## Classes
### <a id="VerifiersTaskDataset"></a>`VerifiersTaskDataset`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/verifiers/components/data.py:44`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L44)
- doc: Adapt one Verifiers taskset to a resumable Grain iterator.
- signature: `class VerifiersTaskDataset(Configurable):`
- members:
  - <a id="VerifiersTaskDataset.load_state_dict"></a>`load_state_dict(self, state_dict: dict)` — [`L120`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L120)
  - <a id="VerifiersTaskDataset.state_dict"></a>`state_dict(self)` — [`L117`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L117)
- protocol/private: <a id="VerifiersTaskDataset.__init__"></a>`__init__`[`L76`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L76), <a id="VerifiersTaskDataset.__iter__"></a>`__iter__`[`L111`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L111), <a id="VerifiersTaskDataset.__next__"></a>`__next__`[`L114`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L114), <a id="VerifiersTaskDataset._iterator"></a>`_iterator`[`L109`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L109)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable)  (8 test-only)
- used by: [`Configurable`](../../../../../config/configurable.md#Configurable)  (5 test-only)

### <a id="VerifiersTaskDataset.Config"></a>`VerifiersTaskDataset.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/components/data.py:51`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L51)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="VerifiersTaskDataset.Config.to_dict"></a>`to_dict(self)` — [`L68`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L68)
  - <a id="VerifiersTaskDataset.Config.num_tasks"></a>`num_tasks` — [`L55`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L55) — ---
  - <a id="VerifiersTaskDataset.Config.seed"></a>`seed` — [`L58`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L58) — ---
  - <a id="VerifiersTaskDataset.Config.shuffle"></a>`shuffle` — [`L61`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L61) — ---
  - <a id="VerifiersTaskDataset.Config.verifiers_taskset"></a>`verifiers_taskset` — [`L52`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L52) — ---
- protocol/private: <a id="VerifiersTaskDataset.Config.__post_init__"></a>`__post_init__`[`L64`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L64)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable), [`Config`](../../../../../config/configurable.md#Configurable.Config)
- used by: (8 test-only callers)

### <a id="VerifiersTaskSample"></a>`VerifiersTaskSample`
- def: [`torchtitan/experiments/rl/examples/verifiers/components/data.py:38`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L38)
- doc: Serialized task data dispatched to a stateless Verifiers EnvServer.
- signature: `class VerifiersTaskSample:`
- members:
  - <a id="VerifiersTaskSample.verifiers_task_data"></a>`verifiers_task_data` — [`L41`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L41)
- used by: (4 test-only callers)

## Functions
- <a id="register_local_taskset_alias"></a>`register_local_taskset_alias(taskset_id: str)` — [`L23`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/data.py#L23) — Register a dotted local taskset under an importable Verifiers plugin ID.

