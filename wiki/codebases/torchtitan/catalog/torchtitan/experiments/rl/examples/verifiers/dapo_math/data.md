---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.dapo_math.data`/
symbols:
  _load_math_dataset: _load_math_dataset().
  VerifiersMathTaskset.load: VerifiersMathTaskset#load().
  VerifiersMathTask.math_verify: VerifiersMathTask#math_verify().
  VerifiersMathTasksetConfig: VerifiersMathTasksetConfig#
  VerifiersMathTask: VerifiersMathTask#
  VerifiersMathTaskset: VerifiersMathTaskset#
  VerifiersMathTaskset.config: VerifiersMathTaskset#config.
  VerifiersMathData: VerifiersMathData#
  VerifiersMathTask.data: VerifiersMathTask#data.
  VerifiersMathData.ground_truth: VerifiersMathData#ground_truth.
  VerifiersMathTasksetConfig.dataset: VerifiersMathTasksetConfig#dataset.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py)

## Classes
### <a id="VerifiersMathData"></a>`VerifiersMathData`
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py:27`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L27)
- signature: `class VerifiersMathData(vf.TaskData):`
- members:
  - <a id="VerifiersMathData.ground_truth"></a>`ground_truth` — [`L28`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L28)
- used by: (5 test-only callers)

### <a id="VerifiersMathTask"></a>`VerifiersMathTask`
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py:31`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L31)
- signature: `class VerifiersMathTask(vf.Task[VerifiersMathData]):`
- members:
  - <a id="VerifiersMathTask.math_verify"></a>`math_verify(self, trace: vf.Trace)` — [`L35`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L35)
  - <a id="VerifiersMathTask.data"></a>`data` — [`L32`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L32)
- uses (calls/refs, reference-scoped): (3 test-only callers)
- used by: (3 test-only callers)

### <a id="VerifiersMathTaskset"></a>`VerifiersMathTaskset`
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py:45`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L45)
- doc: Expose DAPO-Math or AIME samples through the Verifiers taskset API.
- signature: `class VerifiersMathTaskset(vf.Taskset[VerifiersMathTask, VerifiersMathTasksetConfig]):`
- members:
  - <a id="VerifiersMathTaskset.load"></a>`load(self)` — [`L50`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L50) — Build the tasks consumed by both the dataset and environment server.
  - <a id="VerifiersMathTaskset.config"></a>`config` — [`L48`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L48)
- uses (calls/refs, reference-scoped): (7 test-only callers)

### <a id="VerifiersMathTasksetConfig"></a>`VerifiersMathTasksetConfig`
- def: [`torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py:39`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L39)
- doc: Configuration discovered by Verifiers when this taskset ID is loaded.
- signature: `class VerifiersMathTasksetConfig(vf.TasksetConfig):`
- members:
  - <a id="VerifiersMathTasksetConfig.dataset"></a>`dataset` — [`L42`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L42)
- used by: (5 test-only callers)

## Functions
- <a id="_load_math_dataset"></a>`_load_math_dataset(name: Literal["dapo_math", "aime2025"])` — [`L66`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L66)

## Module values
- <a id="__all__"></a>`__all__` — [`L74`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/dapo_math/data.py#L74)

