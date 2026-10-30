---
title: 'Module: torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_muse_glimmer_renderer`/
symbols:
  test_config_build_matches_hf_tokenizer_path: test_config_build_matches_hf_tokenizer_path().
  _renderer: _renderer().
  test_matches_chat_template: test_matches_chat_template().
  test_is_content_covers_non_assistant_bodies: test_is_content_covers_non_assistant_bodies().
  CASES: CASES.
  test_build_snapshots_config: test_build_snapshots_config().
  test_mask_excludes_scaffolding_and_covers_assistant_body: test_mask_excludes_scaffolding_and_covers_assistant_body().
  test_bridge_declines_when_retention_requires_rerender: test_bridge_declines_when_retention_requires_rerender().
  _template_kwargs: _template_kwargs().
  TOOLS: TOOLS.
  test_render_ids_match_encoding_whole_string: test_render_ids_match_encoding_whole_string().
  test_render_mask_aligns_with_ids: test_render_mask_aligns_with_ids().
  test_reasoning_channel_is_trainable_and_ends_with_eom: test_reasoning_channel_is_trainable_and_ends_with_eom().
  test_bridge_extends_without_retokenizing_the_completion: test_bridge_extends_without_retokenizing_the_completion().
  test_bridge_returns_none_when_it_cannot_extend_safely: test_bridge_returns_none_when_it_cannot_extend_safely().
  test_bridge_synthesizes_a_close_for_a_truncated_completion: test_bridge_synthesizes_a_close_for_a_truncated_completion().
  test_rejects_incompatible_tokenizer: test_rejects_incompatible_tokenizer().
  _tool_call: _tool_call().
  test_drop_reasoning_history: test_drop_reasoning_history().
  DEFAULT_TOKENIZER: DEFAULT_TOKENIZER.
  tokenizer: tokenizer().
  test_config_rejects_invalid_values: test_config_rejects_invalid_values().
  test_rejects_incompatible_tokenizer.Shifted.convert_tokens_to_ids: test_rejects_incompatible_tokenizer().Shifted#convert_tokens_to_ids().
  CONFIGS: CONFIGS.
  NAMESPACED_TOOLS: NAMESPACED_TOOLS.
  test_rejects_incompatible_tokenizer.Shifted: test_rejects_incompatible_tokenizer().Shifted#
  Shifted._inner: Shifted#_inner.
  test_rejects_incompatible_tokenizer.Shifted.__init__: test_rejects_incompatible_tokenizer().Shifted#__init__().
  Shifted.bos_token: Shifted#bos_token.
  Shifted.bos_token_id: Shifted#bos_token_id.
---
# Module: [`torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py)

> **Collapsed catalog** (30 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="CASES"></a>`CASES` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L81)
- <a id="CONFIGS"></a>`CONFIGS` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L207)
- <a id="DEFAULT_TOKENIZER"></a>`DEFAULT_TOKENIZER` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L36)
- <a id="NAMESPACED_TOOLS"></a>`NAMESPACED_TOOLS` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L56)
- <a id="Shifted._inner"></a>`Shifted._inner` — [`L549`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L549)
- <a id="Shifted.bos_token"></a>`Shifted.bos_token` — [`L550`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L550)
- <a id="Shifted.bos_token_id"></a>`Shifted.bos_token_id` — [`L551`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L551)
- <a id="TOOLS"></a>`TOOLS` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L38)
- <a id="_renderer"></a>`_renderer` — [`L227`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L227)
- <a id="_template_kwargs"></a>`_template_kwargs` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L271)
- <a id="_tool_call"></a>`_tool_call` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L76)
- <a id="test_bridge_declines_when_retention_requires_rerender"></a>`test_bridge_declines_when_retention_requires_rerender` — [`L405`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L405)
- <a id="test_bridge_extends_without_retokenizing_the_completion"></a>`test_bridge_extends_without_retokenizing_the_completion` — [`L462`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L462)
- <a id="test_bridge_returns_none_when_it_cannot_extend_safely"></a>`test_bridge_returns_none_when_it_cannot_extend_safely` — [`L506`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L506)
- <a id="test_bridge_synthesizes_a_close_for_a_truncated_completion"></a>`test_bridge_synthesizes_a_close_for_a_truncated_completion` — [`L526`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L526)
- <a id="test_build_snapshots_config"></a>`test_build_snapshots_config` — [`L245`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L245)
- <a id="test_config_build_matches_hf_tokenizer_path"></a>`test_config_build_matches_hf_tokenizer_path` — [`L256`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L256)
- <a id="test_config_rejects_invalid_values"></a>`test_config_rejects_invalid_values` — [`L240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L240)
- <a id="test_drop_reasoning_history"></a>`test_drop_reasoning_history` — [`L448`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L448)
- <a id="test_is_content_covers_non_assistant_bodies"></a>`test_is_content_covers_non_assistant_bodies` — [`L370`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L370)
- <a id="test_mask_excludes_scaffolding_and_covers_assistant_body"></a>`test_mask_excludes_scaffolding_and_covers_assistant_body` — [`L345`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L345)
- <a id="test_matches_chat_template"></a>`test_matches_chat_template` — [`L287`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L287)
- <a id="test_reasoning_channel_is_trainable_and_ends_with_eom"></a>`test_reasoning_channel_is_trainable_and_ends_with_eom` — [`L432`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L432)
- <a id="test_rejects_incompatible_tokenizer"></a>`test_rejects_incompatible_tokenizer` — [`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L544)
- <a id="test_rejects_incompatible_tokenizer.Shifted"></a>`test_rejects_incompatible_tokenizer.Shifted` — [`L547`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L547)
- <a id="test_rejects_incompatible_tokenizer.Shifted.__init__"></a>`test_rejects_incompatible_tokenizer.Shifted.__init__` — [`L548`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L548)
- <a id="test_rejects_incompatible_tokenizer.Shifted.convert_tokens_to_ids"></a>`test_rejects_incompatible_tokenizer.Shifted.convert_tokens_to_ids` — [`L553`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L553)
- <a id="test_render_ids_match_encoding_whole_string"></a>`test_render_ids_match_encoding_whole_string` — [`L318`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L318)
- <a id="test_render_mask_aligns_with_ids"></a>`test_render_mask_aligns_with_ids` — [`L332`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L332)
- <a id="tokenizer"></a>`tokenizer` — [`L215`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_muse_glimmer_renderer.py#L215)
