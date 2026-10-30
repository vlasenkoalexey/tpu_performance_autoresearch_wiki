---
title: 'Module: torchtitan/experiments/rl/examples/alphabet_sort/data.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/alphabet_sort/data.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.alphabet_sort.data`/
symbols:
  AlphabetSortDataset._sample: AlphabetSortDataset#_sample().
  AlphabetSortDataset: AlphabetSortDataset#
  AlphabetSortDataset.Config: AlphabetSortDataset#Config#
  AlphabetSortSample.new_names_per_turn: AlphabetSortSample#new_names_per_turn.
  AlphabetSortSample: AlphabetSortSample#
  AlphabetSortSample.expected_names: AlphabetSortSample#expected_names.
  AlphabetSortDataset.Config.seed: AlphabetSortDataset#Config#seed.
  AlphabetSortSample.sort_by_first_name: AlphabetSortSample#sort_by_first_name.
  AlphabetSortDataset.Config.max_turns: AlphabetSortDataset#Config#max_turns.
  AlphabetSortDataset._rng: AlphabetSortDataset#_rng.
  AlphabetSortDataset.Config.max_names_per_turn: AlphabetSortDataset#Config#max_names_per_turn.
  AlphabetSortDataset._author_pool: AlphabetSortDataset#_author_pool.
  AlphabetSortDataset.name_sort_key: AlphabetSortDataset#name_sort_key().
  _Author: _Author#
  AlphabetSortDataset.Config.__post_init__: AlphabetSortDataset#Config#__post_init__().
  AlphabetSortDataset.__next__: AlphabetSortDataset#__next__().
  _Author.display: _Author#display.
  _Author.first: _Author#first.
  _Author.last: _Author#last.
  AlphabetSortDataset.state_dict: AlphabetSortDataset#state_dict().
  AlphabetSortDataset.load_state_dict: AlphabetSortDataset#load_state_dict().
  _load_authors: _load_authors().
  AlphabetSortDataset.__init__: AlphabetSortDataset#__init__().
  AlphabetSortDataset.__iter__: AlphabetSortDataset#__iter__().
  AlphabetSortDataset.Config.hf_dataset: AlphabetSortDataset#Config#hf_dataset.
  AlphabetSortDataset.Config.hf_split: AlphabetSortDataset#Config#hf_split.
  AlphabetSortDataset._config: AlphabetSortDataset#_config.
---
# Module: [`torchtitan/experiments/rl/examples/alphabet_sort/data.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py)

## Classes
### <a id="AlphabetSortDataset"></a>`AlphabetSortDataset`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/data.py:47`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L47)
- doc: Provides lists of researchers' names to sort alphabetically, over one or more turns.
- signature: `class AlphabetSortDataset(Configurable):`
- members:
  - <a id="AlphabetSortDataset._sample"></a>`_sample(self)` — [`L98`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L98) — Build one sample: pick the turn count and names, then for each turn record the names
  - <a id="AlphabetSortDataset.load_state_dict"></a>`load_state_dict(self, state_dict: dict)` — [`L95`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L95)
  - <a id="AlphabetSortDataset.name_sort_key"></a>`name_sort_key(author: _Author)` — [`L120`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L120)
  - <a id="AlphabetSortDataset.state_dict"></a>`state_dict(self)` — [`L91`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L91) — Snapshot the RNG so a run can resume at the same point in the stream.
- protocol/private: <a id="AlphabetSortDataset.__init__"></a>`__init__`[`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L80), <a id="AlphabetSortDataset.__iter__"></a>`__iter__`[`L85`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L85), <a id="AlphabetSortDataset.__next__"></a>`__next__`[`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L88), <a id="AlphabetSortDataset._author_pool"></a>`_author_pool`[`L82`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L82), <a id="AlphabetSortDataset._config"></a>`_config`[`L81`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L81), <a id="AlphabetSortDataset._rng"></a>`_rng`[`L83`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L83)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable)  (15 test-only)
- used by: [`Configurable`](../../../../config/configurable.md#Configurable)  (11 test-only)

### <a id="AlphabetSortDataset.Config"></a>`AlphabetSortDataset.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/data.py:60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L60)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="AlphabetSortDataset.Config.hf_dataset"></a>`hf_dataset` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L69)
  - <a id="AlphabetSortDataset.Config.hf_split"></a>`hf_split` — [`L70`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L70)
  - <a id="AlphabetSortDataset.Config.max_names_per_turn"></a>`max_names_per_turn` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L66) — ---
  - <a id="AlphabetSortDataset.Config.max_turns"></a>`max_turns` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L63) — ---
  - <a id="AlphabetSortDataset.Config.seed"></a>`seed` — [`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L61)
- protocol/private: <a id="AlphabetSortDataset.Config.__post_init__"></a>`__post_init__`[`L72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L72)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../config/configurable.md#Configurable), [`Config`](../../../../config/configurable.md#Configurable.Config)
- used by: (15 test-only callers)

### <a id="AlphabetSortSample"></a>`AlphabetSortSample`
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/data.py:27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L27)
- doc: The names shown and the expected sorted answer for each turn of one AlphabetSort problem.
- signature: `class AlphabetSortSample:`
- members:
  - <a id="AlphabetSortSample.expected_names"></a>`expected_names` — [`L43`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L43)
  - <a id="AlphabetSortSample.new_names_per_turn"></a>`new_names_per_turn` — [`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L42)
  - <a id="AlphabetSortSample.sort_by_first_name"></a>`sort_by_first_name` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L44)
- used by: (17 test-only callers)

### <a id="_Author"></a>`_Author`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/data.py:19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L19)
- signature: `class _Author(NamedTuple):`
- members:
  - <a id="_Author.display"></a>`display` — [`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L21)
  - <a id="_Author.first"></a>`first` — [`L22`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L22)
  - <a id="_Author.last"></a>`last` — [`L23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L23)
- used by: (6 test-only callers)

## Functions
- <a id="_load_authors"></a>`_load_authors(hf_dataset: str, hf_split: str)` — [`L164`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/data.py#L164) — Load + dedupe arXiv authors, splitting each `"First Last"` name at its space.

