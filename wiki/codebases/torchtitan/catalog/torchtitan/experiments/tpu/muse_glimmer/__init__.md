---
title: 'Module: torchtitan/experiments/tpu/muse_glimmer/__init__.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/muse_glimmer/__init__.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.muse_glimmer`/
symbols:
  model_registry: model_registry().
  use_tpu_attention: use_tpu_attention().
  _testmodel: _testmodel().
  _upstream_flavor: _upstream_flavor().
  muse_glimmer_configs: muse_glimmer_configs.
  TESTMODEL_MAX_CONTEXT_LENGTH: TESTMODEL_MAX_CONTEXT_LENGTH.
  TESTMODEL_WINDOW_SIZE: TESTMODEL_WINDOW_SIZE.
  _UPSTREAM_TEXT_FLAVORS: _UPSTREAM_TEXT_FLAVORS.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/muse_glimmer/__init__.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py)

## Functions
- <a id="_testmodel"></a>`_testmodel()` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L77) — 4-layer model: layers 0-2 are sliding-window + RoPE, layer 3 global + NoPE.
- <a id="_upstream_flavor"></a>`_upstream_flavor(flavor: str)` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L98) — Builds an upstream flavor at its full context length, with TPU attention.
- <a id="model_registry"></a>`model_registry(flavor: str, *, seq_len: int | None = None, converters: list[ModelConfigConverter.Config] | None = None)` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L114) — Returns a TPU ``ModelSpec`` for a text-only Muse Glimmer flavor.
- <a id="use_tpu_attention"></a>`use_tpu_attention(config: MuseGlimmerModel.Config)` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L49) — Switches each layer to the TPU attention modules.

## Module values
- <a id="TESTMODEL_MAX_CONTEXT_LENGTH"></a>`TESTMODEL_MAX_CONTEXT_LENGTH` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L42)
- <a id="TESTMODEL_WINDOW_SIZE"></a>`TESTMODEL_WINDOW_SIZE` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L43)
- <a id="_UPSTREAM_TEXT_FLAVORS"></a>`_UPSTREAM_TEXT_FLAVORS` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L46)
- <a id="__all__"></a>`__all__` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L29)
- <a id="muse_glimmer_configs"></a>`muse_glimmer_configs` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/muse_glimmer/__init__.py#L108)

