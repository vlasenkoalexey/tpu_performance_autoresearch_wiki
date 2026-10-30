---
title: 'Module: torchtitan/experiments/rl/examples/search_r1/data.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/search_r1/data.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.search_r1.data`/
symbols:
  SearchR1Dataset.__next__: SearchR1Dataset#__next__().
  SearchR1Dataset._order: SearchR1Dataset#_order.
  SearchR1Dataset.__init__: SearchR1Dataset#__init__().
  SearchR1Sample: SearchR1Sample#
  SearchR1Dataset.Config: SearchR1Dataset#Config#
  SearchR1Dataset: SearchR1Dataset#
  SearchR1Dataset.state_dict: SearchR1Dataset#state_dict().
  SearchR1Dataset.load_state_dict: SearchR1Dataset#load_state_dict().
  SearchR1Dataset._rng: SearchR1Dataset#_rng.
  SearchR1Dataset._pos: SearchR1Dataset#_pos.
  SearchR1Sample.golden_answers: SearchR1Sample#golden_answers.
  SearchR1Dataset._shuffle: SearchR1Dataset#_shuffle.
  SearchR1Sample.question: SearchR1Sample#question.
  SearchR1Dataset.Config.filename: SearchR1Dataset#Config#filename.
  SearchR1Dataset.Config.data_source: SearchR1Dataset#Config#data_source.
  SearchR1Dataset._golden_answers: SearchR1Dataset#_golden_answers.
  SearchR1Dataset.Config.data_path: SearchR1Dataset#Config#data_path.
  SearchR1Dataset.Config.seed: SearchR1Dataset#Config#seed.
  SearchR1Dataset._questions: SearchR1Dataset#_questions.
  SearchR1Dataset.__iter__: SearchR1Dataset#__iter__().
  SearchR1Dataset.Config.repo_id: SearchR1Dataset#Config#repo_id.
  SearchR1Dataset.Config.shuffle: SearchR1Dataset#Config#shuffle.
---
# Module: [`torchtitan/experiments/rl/examples/search_r1/data.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py)

## Classes
### <a id="SearchR1Dataset"></a>`SearchR1Dataset`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/search_r1/data.py:29`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L29)
- doc: Endless, seeded stream of Search-R1 QA samples.
- signature: `class SearchR1Dataset(Configurable):`
- members:
  - <a id="SearchR1Dataset.load_state_dict"></a>`load_state_dict(self, state_dict: dict)` — [`L116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L116)
  - <a id="SearchR1Dataset.state_dict"></a>`state_dict(self)` — [`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L108) — Snapshot the RNG + position so a run can resume mid-stream.
- protocol/private: <a id="SearchR1Dataset.__init__"></a>`__init__`[`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L61), <a id="SearchR1Dataset.__iter__"></a>`__iter__`[`L93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L93), <a id="SearchR1Dataset.__next__"></a>`__next__`[`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L96), <a id="SearchR1Dataset._golden_answers"></a>`_golden_answers`[`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L80), <a id="SearchR1Dataset._order"></a>`_order`[`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L88), <a id="SearchR1Dataset._pos"></a>`_pos`[`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L91), <a id="SearchR1Dataset._questions"></a>`_questions`[`L78`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L78), <a id="SearchR1Dataset._rng"></a>`_rng`[`L86`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L86), <a id="SearchR1Dataset._shuffle"></a>`_shuffle`[`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L87)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable)  (10 test-only)
- used by: [`Configurable`](../../../../config/configurable.md#Configurable)  (2 test-only)

### <a id="SearchR1Dataset.Config"></a>`SearchR1Dataset.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/search_r1/data.py:38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L38)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="SearchR1Dataset.Config.data_path"></a>`data_path` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L46) — ---
  - <a id="SearchR1Dataset.Config.data_source"></a>`data_source` — [`L52`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L52) — ---
  - <a id="SearchR1Dataset.Config.filename"></a>`filename` — [`L39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L39) — ---
  - <a id="SearchR1Dataset.Config.repo_id"></a>`repo_id` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L43) — ---
  - <a id="SearchR1Dataset.Config.seed"></a>`seed` — [`L49`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L49) — ---
  - <a id="SearchR1Dataset.Config.shuffle"></a>`shuffle` — [`L56`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L56) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable), [`Config`](../../../../config/configurable.md#Configurable.Config)
- used by: (5 test-only callers)

### <a id="SearchR1Sample"></a>`SearchR1Sample`
- def: [`torchtitan/experiments/rl/examples/search_r1/data.py:19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L19)
- doc: One Search-R1 open-domain QA sample: a question and its accepted answers.
- signature: `class SearchR1Sample:`
- members:
  - <a id="SearchR1Sample.golden_answers"></a>`golden_answers` — [`L25`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L25) — ---
  - <a id="SearchR1Sample.question"></a>`question` — [`L22`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/data.py#L22) — ---
- used by: (7 test-only callers)

