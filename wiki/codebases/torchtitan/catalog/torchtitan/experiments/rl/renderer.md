---
title: 'Module: torchtitan/experiments/rl/renderer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/renderer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.renderer`/
symbols:
  RenderersLibraryConfig: RenderersLibraryConfig#
  RenderersLibraryConfig.renderers_config: RenderersLibraryConfig#renderers_config.
  RendererConfig: RendererConfig#
  RenderersLibraryConfig.build: RenderersLibraryConfig#build().
  RendererConfig.build: RendererConfig#build().
  RendererTokenizerWrapper._tokenizer_backend: RendererTokenizerWrapper#_tokenizer_backend.
  RendererTokenizerWrapper: RendererTokenizerWrapper#
  RendererTokenizerWrapper.encode: RendererTokenizerWrapper#encode().
  RendererTokenizerWrapper.eos_token_id: RendererTokenizerWrapper#eos_token_id.
  RendererTokenizerWrapper.convert_tokens_to_ids: RendererTokenizerWrapper#convert_tokens_to_ids().
  RenderersLibraryConfig.to_dict: RenderersLibraryConfig#to_dict().
  RendererTokenizerWrapper.__init__: RendererTokenizerWrapper#__init__().
  RendererTokenizerWrapper.name_or_path: RendererTokenizerWrapper#name_or_path.
  RendererTokenizerWrapper.bos_token: RendererTokenizerWrapper#bos_token.
  RendererTokenizerWrapper.eos_token: RendererTokenizerWrapper#eos_token.
  RendererTokenizerWrapper.bos_token_id: RendererTokenizerWrapper#bos_token_id.
  RendererTokenizerWrapper.decode: RendererTokenizerWrapper#decode().
  RendererTokenizerWrapper.__call__: RendererTokenizerWrapper#__call__().
  RendererTokenizerWrapper.unk_token_id: RendererTokenizerWrapper#unk_token_id.
---
# Module: [`torchtitan/experiments/rl/renderer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py)

## Classes
### <a id="RendererConfig"></a>`RendererConfig`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/renderer.py:21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L21)
- doc: Base config of a renderer; `build` returns a `renderers.Renderer` on TorchTitan's tokenizer.
- signature: `class RendererConfig(Configurable.Config):`
- members:
  - <a id="RendererConfig.build"></a>`build(self, *, tokenizer: HuggingFaceTokenizer)` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L28)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config), [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`RenderersLibraryConfig`](renderer.md#RenderersLibraryConfig), [`MuseGlimmerRendererConfig`](models/muse_glimmer/renderer.md#MuseGlimmerRendererConfig), [`build`](renderer.md#RenderersLibraryConfig.build), [`build`](models/muse_glimmer/renderer.md#MuseGlimmerRendererConfig.build)
- used by: [`RenderersLibraryConfig`](renderer.md#RenderersLibraryConfig), [`setup_async`](rollout/rollouter.md#Rollouter.setup_async), [`renderer`](controller.md#Controller.Config.renderer), [`setup_async`](rollout/rollouter.md#RolloutWorker.setup_async), [`MuseGlimmerRendererConfig`](models/muse_glimmer/renderer.md#MuseGlimmerRendererConfig), [`setup_async`](actors/rollout_worker.md#RolloutWorkerActor.setup_async), [`renderer`](controller.md#Controller.renderer)  (2 test-only)

### <a id="RendererTokenizerWrapper"></a>`RendererTokenizerWrapper`
- def: [`torchtitan/experiments/rl/renderer.py:78`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L78)
- members:
  - <a id="RendererTokenizerWrapper.convert_tokens_to_ids"></a>`convert_tokens_to_ids(self, tokens: str | list[str])` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L131)
  - <a id="RendererTokenizerWrapper.decode"></a>`decode(self, token_ids, skip_special_tokens: bool = False, **kwargs)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L126)
  - <a id="RendererTokenizerWrapper.encode"></a>`encode(self, text: str, add_special_tokens: bool = False, **kwargs)` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L119)
  - <a id="RendererTokenizerWrapper.bos_token"></a>`bos_token` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L112)
  - <a id="RendererTokenizerWrapper.bos_token_id"></a>`bos_token_id` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L114)
  - <a id="RendererTokenizerWrapper.eos_token"></a>`eos_token` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L113)
  - <a id="RendererTokenizerWrapper.eos_token_id"></a>`eos_token_id` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L115)
  - <a id="RendererTokenizerWrapper.name_or_path"></a>`name_or_path` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L111)
  - <a id="RendererTokenizerWrapper.unk_token_id"></a>`unk_token_id` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L117)
- protocol/private: <a id="RendererTokenizerWrapper.__call__"></a>`__call__`[`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L138), <a id="RendererTokenizerWrapper.__init__"></a>`__init__`[`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L108), <a id="RendererTokenizerWrapper._tokenizer_backend"></a>`_tokenizer_backend`[`L110`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L110)
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`tokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer.tokenizer), [`eos_id`](../../components/tokenizer.md#BaseTokenizer.eos_id), [`bos_id`](../../components/tokenizer.md#HuggingFaceTokenizer.bos_id), [`bos_token`](../../components/tokenizer.md#HuggingFaceTokenizer.bos_token), [`eos_token`](../../components/tokenizer.md#HuggingFaceTokenizer.eos_token), [`tokenizer_path`](../../components/tokenizer.md#HuggingFaceTokenizer.tokenizer_path)
- used by: [`build`](renderer.md#RenderersLibraryConfig.build), [`build`](models/muse_glimmer/renderer.md#MuseGlimmerRendererConfig.build)  (3 test-only)

### <a id="RenderersLibraryConfig"></a>`RenderersLibraryConfig`  ·  implements/extends RendererConfig
- def: [`torchtitan/experiments/rl/renderer.py:33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L33)
- doc: Builds one of the `renderers` library's renderers on TorchTitan's tokenizer.
- signature: `class RenderersLibraryConfig(RendererConfig):`
- members:
  - <a id="RenderersLibraryConfig.build"></a>`build(self, *, tokenizer: HuggingFaceTokenizer)` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L60)
  - <a id="RenderersLibraryConfig.to_dict"></a>`to_dict(self)` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L57)
  - <a id="RenderersLibraryConfig.renderers_config"></a>`renderers_config` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/renderer.py#L52) — ---
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../components/tokenizer.md#HuggingFaceTokenizer), [`RendererConfig`](renderer.md#RendererConfig), [`RendererTokenizerWrapper`](renderer.md#RendererTokenizerWrapper), [`tokenizer_path`](../../components/tokenizer.md#HuggingFaceTokenizer.tokenizer_path)
- used by: [`RendererConfig`](renderer.md#RendererConfig), [`build`](renderer.md#RendererConfig.build)  (24 test-only)

