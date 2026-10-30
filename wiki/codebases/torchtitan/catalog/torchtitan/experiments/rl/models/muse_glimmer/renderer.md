---
title: 'Module: torchtitan/experiments/rl/models/muse_glimmer/renderer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/muse_glimmer/renderer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.muse_glimmer.renderer`/
symbols:
  MuseGlimmerRenderer.bridge_to_next_turn: MuseGlimmerRenderer#bridge_to_next_turn().
  MuseGlimmerRenderer._build: MuseGlimmerRenderer#_build().
  MuseGlimmerRenderer.block: MuseGlimmerRenderer#block().
  MuseGlimmerRenderer._verify_special_ids: MuseGlimmerRenderer#_verify_special_ids().
  MuseGlimmerRenderer.render: MuseGlimmerRenderer#render().
  MuseGlimmerRenderer._default_system_body: MuseGlimmerRenderer#_default_system_body().
  MuseGlimmerRenderer.parse_response: MuseGlimmerRenderer#parse_response().
  MuseGlimmerRenderer.render_ids: MuseGlimmerRenderer#render_ids().
  EOT_ID: EOT_ID.
  MuseGlimmerRenderer._prepare: MuseGlimmerRenderer#_prepare().
  MuseGlimmerRendererConfig: MuseGlimmerRendererConfig#
  MuseGlimmerRenderer._explicit_system_body: MuseGlimmerRenderer#_explicit_system_body().
  MuseGlimmerRenderer._encode: MuseGlimmerRenderer#_encode().
  MuseGlimmerRenderer._render_text: MuseGlimmerRenderer#_render_text().
  MuseGlimmerRenderer._config: MuseGlimmerRenderer#_config.
  MuseGlimmerRenderer.effective_thinking_retention: MuseGlimmerRenderer#effective_thinking_retention.
  MuseGlimmerRenderer.emit: MuseGlimmerRenderer#emit().
  MuseGlimmerRendererConfig.build: MuseGlimmerRendererConfig#build().
  _render_tool_defs: _render_tool_defs().
  MuseGlimmerRenderer._reasoning_line: MuseGlimmerRenderer#_reasoning_line().
  EOT_STR: EOT_STR.
  START_ID: START_ID.
  MESSAGE_ID: MESSAGE_ID.
  _tojson: _tojson().
  MuseGlimmerRenderer._tok: MuseGlimmerRenderer#_tok.
  MuseGlimmerRenderer.get_stop_token_ids: MuseGlimmerRenderer#get_stop_token_ids().
  EOM_STR: EOM_STR.
  MuseGlimmerRenderer: MuseGlimmerRenderer#
  _tool_namespaces: _tool_namespaces().
  _render_system_meta: _render_system_meta().
  MuseGlimmerRendererConfig.retain_reasoning_in_history: MuseGlimmerRendererConfig#retain_reasoning_in_history.
  EOM_ID: EOM_ID.
  _render_content: _render_content().
  _Piece: _Piece#
  _Piece.token_id: _Piece#token_id.
  _render_atem: _render_atem().
  _parse_channels: _parse_channels().
  MuseGlimmerRendererConfig.reasoning_strength: MuseGlimmerRendererConfig#reasoning_strength.
  MuseGlimmerRendererConfig.current_date: MuseGlimmerRendererConfig#current_date.
  _Piece.text: _Piece#text.
  START_STR: START_STR.
  MuseGlimmerRendererConfig.__post_init__: MuseGlimmerRendererConfig#__post_init__().
  MuseGlimmerRenderer.__init__: MuseGlimmerRenderer#__init__().
  MuseGlimmerRendererConfig.knowledge_cutoff: MuseGlimmerRendererConfig#knowledge_cutoff.
  MuseGlimmerRendererConfig.thinking_retention: MuseGlimmerRendererConfig#thinking_retention.
  _tool_fn: _tool_fn().
  _Piece.msg_idx: _Piece#msg_idx.
  _Piece.is_body: _Piece#is_body.
  MuseGlimmerRenderer._bos: MuseGlimmerRenderer#_bos.
  MESSAGE_STR: MESSAGE_STR.
  MuseGlimmerRendererConfig.answer_from_reasoning_fallback: MuseGlimmerRendererConfig#answer_from_reasoning_fallback.
  EOS_ID: EOS_ID.
  _DEFAULT_REASONING_STRENGTH: _DEFAULT_REASONING_STRENGTH.
  _DEFAULT_KNOWLEDGE_CUTOFF: _DEFAULT_KNOWLEDGE_CUTOFF.
  _FUNCTION_CALLS_BLOCK: _FUNCTION_CALLS_BLOCK.
  _CHANNEL: _CHANNEL.
  _EFFORT_TO_STRENGTH: _EFFORT_TO_STRENGTH.
  _strip_reasoning_history: _strip_reasoning_history().
  _normalize_tool_calls: _normalize_tool_calls().
  _Piece.sampled: _Piece#sampled.
  _Piece.is_generation_prompt: _Piece#is_generation_prompt.
  MuseGlimmerRenderer._tool_name: MuseGlimmerRenderer#_tool_name().
---
# Module: [`torchtitan/experiments/rl/models/muse_glimmer/renderer.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py)

## Classes
### <a id="MuseGlimmerRenderer"></a>`MuseGlimmerRenderer`
- def: [`torchtitan/experiments/rl/models/muse_glimmer/renderer.py:356`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L356)
- members:
  - <a id="MuseGlimmerRenderer._build"></a>`_build(self, messages, *, tools, add_generation_prompt)` — [`L443`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L443) — Render to spans. Concatenating ``.text`` reproduces the chat template exactly.
  - <a id="MuseGlimmerRenderer._default_system_body"></a>`_default_system_body(self, tools)` — [`L404`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L404) — System block synthesised when the caller supplies no system message.
  - <a id="MuseGlimmerRenderer._prepare"></a>`_prepare(self, messages)` — [`L394`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L394) — Apply the history policy, then the tool-call shape rendering expects.
  - <a id="MuseGlimmerRenderer._render_text"></a>`_render_text(self, messages, *, tools=None, add_generation_prompt=False)` — [`L564`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L564) — The rendered prompt as text. Byte-exact against chat_template.jinja.
  - <a id="MuseGlimmerRenderer._tool_name"></a>`_tool_name(message, messages)` — [`L430`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L430) — Tool messages name their tool directly, or via the call id that produced them.
  - <a id="MuseGlimmerRenderer._verify_special_ids"></a>`_verify_special_ids(self)` — [`L373`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L373) — The special-token ids are baked into parse_response and the loss mask.
  - <a id="MuseGlimmerRenderer.block"></a>`block(header: str, body: str, end: str, *, idx: int, sampled: bool)` — [`L466`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L466)
  - <a id="MuseGlimmerRenderer.bridge_to_next_turn"></a>`bridge_to_next_turn(self, previous_prompt_ids: list[int], previous_completion_ids: list[int], new_messages, *, tools=None)` — [`L637`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L637) — Extend prompt + sampled completion with the next turn, without re-rendering.
  - <a id="MuseGlimmerRenderer.emit"></a>`emit(text: str, *, token_id: int | None = None, sampled=False, idx=0, is_body=False, is_generation_prompt=False)` — [`L452`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L452)
  - <a id="MuseGlimmerRenderer.get_stop_token_ids"></a>`get_stop_token_ids(self)` — [`L578`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L578)
  - <a id="MuseGlimmerRenderer.parse_response"></a>`parse_response(self, token_ids, *, tools=None)` — [`L721`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L721) — Parse a Muse Glimmer completion into (content, reasoning_content, tool_calls).
  - <a id="MuseGlimmerRenderer.render"></a>`render(self, messages, *, tools=None, add_generation_prompt: bool = False)` — [`L596`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L596) — Render with per-token attribution for the trainer loss mask.
  - <a id="MuseGlimmerRenderer.render_ids"></a>`render_ids(self, messages, *, tools=None, add_generation_prompt: bool = False)` — [`L583`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L583)
  - <a id="MuseGlimmerRenderer.effective_thinking_retention"></a>`effective_thinking_retention` — [`L367`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L367)
- protocol/private: <a id="MuseGlimmerRenderer.__init__"></a>`__init__`[`L357`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L357), <a id="MuseGlimmerRenderer._bos"></a>`_bos`[`L361`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L361), <a id="MuseGlimmerRenderer._config"></a>`_config`[`L360`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L360), <a id="MuseGlimmerRenderer._encode"></a>`_encode`[`L573`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L573), <a id="MuseGlimmerRenderer._explicit_system_body"></a>`_explicit_system_body`[`L418`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L418), <a id="MuseGlimmerRenderer._reasoning_line"></a>`_reasoning_line`[`L400`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L400), <a id="MuseGlimmerRenderer._tok"></a>`_tok`[`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L359)
- uses (calls/refs, reference-scoped): [`EOT_ID`](renderer.md#EOT_ID), [`MuseGlimmerRendererConfig`](renderer.md#MuseGlimmerRendererConfig), [`parse_atem_tool_calls`](atem.md#parse_atem_tool_calls), [`_render_tool_defs`](renderer.md#_render_tool_defs), [`EOT_STR`](renderer.md#EOT_STR), [`START_ID`](renderer.md#START_ID), [`EOM_STR`](renderer.md#EOM_STR), [`MESSAGE_ID`](renderer.md#MESSAGE_ID), [`_render_system_meta`](renderer.md#_render_system_meta), [`_Piece`](renderer.md#_Piece), [`EOM_ID`](renderer.md#EOM_ID), [`_render_content`](renderer.md#_render_content), [`render_atem_tool_call`](atem.md#render_atem_tool_call), [`retain_reasoning_in_history`](renderer.md#MuseGlimmerRendererConfig.retain_reasoning_in_history), [`token_id`](renderer.md#_Piece.token_id), [`_parse_channels`](renderer.md#_parse_channels), [`_render_atem`](renderer.md#_render_atem), [`START_STR`](renderer.md#START_STR), [`current_date`](renderer.md#MuseGlimmerRendererConfig.current_date), [`reasoning_strength`](renderer.md#MuseGlimmerRendererConfig.reasoning_strength), [`text`](renderer.md#_Piece.text), [`MESSAGE_STR`](renderer.md#MESSAGE_STR), [`is_body`](renderer.md#_Piece.is_body), [`knowledge_cutoff`](renderer.md#MuseGlimmerRendererConfig.knowledge_cutoff), [`msg_idx`](renderer.md#_Piece.msg_idx), [`EOS_ID`](renderer.md#EOS_ID), [`_DEFAULT_KNOWLEDGE_CUTOFF`](renderer.md#_DEFAULT_KNOWLEDGE_CUTOFF), [`_DEFAULT_REASONING_STRENGTH`](renderer.md#_DEFAULT_REASONING_STRENGTH), [`_EFFORT_TO_STRENGTH`](renderer.md#_EFFORT_TO_STRENGTH), [`_FUNCTION_CALLS_BLOCK`](renderer.md#_FUNCTION_CALLS_BLOCK), [`_normalize_tool_calls`](renderer.md#_normalize_tool_calls), [`_strip_reasoning_history`](renderer.md#_strip_reasoning_history), [`answer_from_reasoning_fallback`](renderer.md#MuseGlimmerRendererConfig.answer_from_reasoning_fallback), [`is_generation_prompt`](renderer.md#_Piece.is_generation_prompt), [`sampled`](renderer.md#_Piece.sampled)
- used by: [`build`](renderer.md#MuseGlimmerRendererConfig.build)  (14 test-only)

### <a id="MuseGlimmerRendererConfig"></a>`MuseGlimmerRendererConfig`  ·  implements/extends RendererConfig
- def: [`torchtitan/experiments/rl/models/muse_glimmer/renderer.py:72`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L72)
- doc: Muse Glimmer (harmony chat format + ATEM tool calls) renderer config.
- signature: `class MuseGlimmerRendererConfig(RendererConfig):`
- members:
  - <a id="MuseGlimmerRendererConfig.build"></a>`build(self, *, tokenizer: HuggingFaceTokenizer)` — [`L141`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L141)
  - <a id="MuseGlimmerRendererConfig.answer_from_reasoning_fallback"></a>`answer_from_reasoning_fallback` — [`L109`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L109) — ---
  - <a id="MuseGlimmerRendererConfig.current_date"></a>`current_date` — [`L88`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L88) — ---
  - <a id="MuseGlimmerRendererConfig.knowledge_cutoff"></a>`knowledge_cutoff` — [`L84`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L84) — ---
  - <a id="MuseGlimmerRendererConfig.reasoning_strength"></a>`reasoning_strength` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L75) — ---
  - <a id="MuseGlimmerRendererConfig.retain_reasoning_in_history"></a>`retain_reasoning_in_history` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L96) — ---
  - <a id="MuseGlimmerRendererConfig.thinking_retention"></a>`thinking_retention` — [`L118`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L118) — ---
- protocol/private: <a id="MuseGlimmerRendererConfig.__post_init__"></a>`__post_init__`[`L122`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L122)
- uses (calls/refs, reference-scoped): [`HuggingFaceTokenizer`](../../../../components/tokenizer.md#HuggingFaceTokenizer), [`RendererConfig`](../../renderer.md#RendererConfig), [`RendererTokenizerWrapper`](../../renderer.md#RendererTokenizerWrapper), [`MuseGlimmerRenderer`](renderer.md#MuseGlimmerRenderer)
- used by: [`RendererConfig`](../../renderer.md#RendererConfig), [`_default_system_body`](renderer.md#MuseGlimmerRenderer._default_system_body), [`parse_response`](renderer.md#MuseGlimmerRenderer.parse_response), [`_prepare`](renderer.md#MuseGlimmerRenderer._prepare), [`_config`](renderer.md#MuseGlimmerRenderer._config), [`effective_thinking_retention`](renderer.md#MuseGlimmerRenderer.effective_thinking_retention), [`_reasoning_line`](renderer.md#MuseGlimmerRenderer._reasoning_line), [`build`](../../renderer.md#RendererConfig.build), [`__init__`](renderer.md#MuseGlimmerRenderer.__init__)  (8 test-only)

### <a id="_Piece"></a>`_Piece`  ·  implements/extends NamedTuple
- def: [`torchtitan/experiments/rl/models/muse_glimmer/renderer.py:336`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L336)
- doc: One span of the render: either a literal special token or text to encode.
- signature: `class _Piece(NamedTuple):`
- members:
  - <a id="_Piece.is_body"></a>`is_body` — [`L352`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L352)
  - <a id="_Piece.is_generation_prompt"></a>`is_generation_prompt` — [`L353`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L353)
  - <a id="_Piece.msg_idx"></a>`msg_idx` — [`L351`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L351)
  - <a id="_Piece.sampled"></a>`sampled` — [`L350`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L350)
  - <a id="_Piece.text"></a>`text` — [`L348`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L348)
  - <a id="_Piece.token_id"></a>`token_id` — [`L349`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L349)
- used by: [`bridge_to_next_turn`](renderer.md#MuseGlimmerRenderer.bridge_to_next_turn), [`_build`](renderer.md#MuseGlimmerRenderer._build), [`render`](renderer.md#MuseGlimmerRenderer.render), [`_encode`](renderer.md#MuseGlimmerRenderer._encode), [`_render_text`](renderer.md#MuseGlimmerRenderer._render_text), [`emit`](renderer.md#MuseGlimmerRenderer.emit)

## Functions
- <a id="_normalize_tool_calls"></a>`_normalize_tool_calls(messages)` — [`L302`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L302) — Our ParsedToolCall is flat (.name/.arguments); rendering expects OpenAI-nested.
- <a id="_parse_channels"></a>`_parse_channels(text: str)` — [`L328`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L328) — Split a Muse Glimmer assistant completion into (recipient, body) harmony channels.
- <a id="_render_atem"></a>`_render_atem(tool_call)` — [`L276`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L276) — An assistant tool call as an ATEM block.
- <a id="_render_content"></a>`_render_content(content)` — [`L187`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L187) — A message body: a plain string, or a list of typed multimodal parts.
- <a id="_render_system_meta"></a>`_render_system_meta(tools)` — [`L267`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L267) — The ``# Valid recipients:`` line closing every system message.
- <a id="_render_tool_defs"></a>`_render_tool_defs(tools)` — [`L222`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L222) — The tool-definition block injected into the system message.
- <a id="_strip_reasoning_history"></a>`_strip_reasoning_history(messages)` — [`L288`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L288) — Drop ``reasoning_content`` from assistant messages (see the config field).
- <a id="_tojson"></a>`_tojson(value)` — [`L182`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L182) — Jinja's ``tojson`` as transformers configures it: insertion order, raw unicode.
- <a id="_tool_fn"></a>`_tool_fn(tool)` — [`L205`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L205) — Tools arrive either OpenAI-nested (``{"function": {...}}``) or flat.
- <a id="_tool_namespaces"></a>`_tool_namespaces(tools)` — [`L212`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L212) — Leading dotted segment of each tool name, first-seen order, deduplicated.

## Module values
- <a id="EOM_ID"></a>`EOM_ID` — [`L155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L155)
- <a id="EOM_STR"></a>`EOM_STR` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L150)
- <a id="EOS_ID"></a>`EOS_ID` — [`L156`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L156)
- <a id="EOT_ID"></a>`EOT_ID` — [`L154`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L154)
- <a id="EOT_STR"></a>`EOT_STR` — [`L150`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L150)
- <a id="MESSAGE_ID"></a>`MESSAGE_ID` — [`L153`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L153)
- <a id="MESSAGE_STR"></a>`MESSAGE_STR` — [`L149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L149)
- <a id="START_ID"></a>`START_ID` — [`L152`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L152)
- <a id="START_STR"></a>`START_STR` — [`L149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L149)
- <a id="_CHANNEL"></a>`_CHANNEL` — [`L165`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L165)
- <a id="_DEFAULT_KNOWLEDGE_CUTOFF"></a>`_DEFAULT_KNOWLEDGE_CUTOFF` — [`L159`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L159)
- <a id="_DEFAULT_REASONING_STRENGTH"></a>`_DEFAULT_REASONING_STRENGTH` — [`L158`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L158)
- <a id="_EFFORT_TO_STRENGTH"></a>`_EFFORT_TO_STRENGTH` — [`L174`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L174)
- <a id="_FUNCTION_CALLS_BLOCK"></a>`_FUNCTION_CALLS_BLOCK` — [`L161`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/muse_glimmer/renderer.py#L161)

