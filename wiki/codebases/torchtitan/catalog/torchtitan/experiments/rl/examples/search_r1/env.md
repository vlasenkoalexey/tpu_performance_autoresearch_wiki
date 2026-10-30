---
title: 'Module: torchtitan/experiments/rl/examples/search_r1/env.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/search_r1/env.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.search_r1.env`/
symbols:
  SearchR1Env.step: SearchR1Env#step().
  SearchR1Env.init: SearchR1Env#init().
  SearchR1Env: SearchR1Env#
  SearchR1Env.Config: SearchR1Env#Config#
  _search: _search().
  SearchR1Env.__init__: SearchR1Env#__init__().
  SearchR1Env._question: SearchR1Env#_question.
  SearchR1Env._search_url: SearchR1Env#_search_url.
  SearchR1Env._topk: SearchR1Env#_topk.
  SearchR1Env._timeout_s: SearchR1Env#_timeout_s.
  logger: logger.
  INSTRUCTION: INSTRUCTION.
  _passages_to_string: _passages_to_string().
  _query_from_tool_call: _query_from_tool_call().
  SearchR1Env.Config.search_url: SearchR1Env#Config#search_url.
  SearchR1Env.Config.topk: SearchR1Env#Config#topk.
  SearchR1Env.Config.timeout_s: SearchR1Env#Config#timeout_s.
  SEARCH_TOOL.SEARCH_TOOL: SEARCH_TOOL.SEARCH_TOOL.
---
# Module: [`torchtitan/experiments/rl/examples/search_r1/env.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py)

## Classes
### <a id="SearchR1Env"></a>`SearchR1Env`  ·  implements/extends MessageEnv
- def: [`torchtitan/experiments/rl/examples/search_r1/env.py:113`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L113)
- doc: Multi-turn open-domain QA env with a `search` tool.
- signature: `class SearchR1Env(MessageEnv):`
- members:
  - <a id="SearchR1Env.init"></a>`init(self)` — [`L141`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L141)
  - <a id="SearchR1Env.step"></a>`step(self, completion_message: Message)` — [`L149`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L149)
- protocol/private: <a id="SearchR1Env.__init__"></a>`__init__`[`L135`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L135), <a id="SearchR1Env._question"></a>`_question`[`L136`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L136), <a id="SearchR1Env._search_url"></a>`_search_url`[`L137`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L137), <a id="SearchR1Env._timeout_s"></a>`_timeout_s`[`L139`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L139), <a id="SearchR1Env._topk"></a>`_topk`[`L138`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L138)
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`MessageEnvStepOutput`](../../environment/message.md#MessageEnvStepOutput), [`env_messages`](../../environment/message.md#MessageEnvStepOutput.env_messages), [`MessageEnvInitOutput`](../../environment/message.md#MessageEnvInitOutput), [`done`](../../environment/message.md#MessageEnvStepOutput.done), [`init_prompt_messages`](../../environment/message.md#MessageEnvInitOutput.init_prompt_messages), [`tools`](../../environment/message.md#MessageEnvInitOutput.tools)  (10 test-only)
- used by: [`MessageEnv`](../../environment/message.md#MessageEnv), [`step`](../../environment/message.md#MessageEnv.step), [`init`](../../environment/message.md#MessageEnv.init)  (6 test-only)

### <a id="SearchR1Env.Config"></a>`SearchR1Env.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/search_r1/env.py:125`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L125)
- signature: `class Config(MessageEnv.Config):`
- members:
  - <a id="SearchR1Env.Config.search_url"></a>`search_url` — [`L126`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L126) — ---
  - <a id="SearchR1Env.Config.timeout_s"></a>`timeout_s` — [`L132`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L132) — ---
  - <a id="SearchR1Env.Config.topk"></a>`topk` — [`L129`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L129) — ---
- uses (calls/refs, reference-scoped): [`MessageEnv`](../../environment/message.md#MessageEnv), [`Config`](../../environment/message.md#MessageEnv.Config)
- used by: (6 test-only callers)

## Functions
- <a id="_passages_to_string"></a>`_passages_to_string(docs: list[dict])` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L58) — Format retrieved docs into the block returned to the model.
- <a id="_query_from_tool_call"></a>`_query_from_tool_call(tool_call: ParsedToolCall)` — [`L99`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L99) — Pull the ``query`` argument out of a renderer-parsed ``search`` tool call.
- <a id="_search"></a>`_search(query: str, *, url: str, topk: int, timeout_s: float = 60)` — [`L76`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L76) — Retrieve the top-``topk`` passages for ``query``, formatted for the model.

## Module values
- <a id="INSTRUCTION"></a>`INSTRUCTION` — [`L50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L50)
- <a id="SEARCH_TOOL.SEARCH_TOOL"></a>`SEARCH_TOOL` — [`L32`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L32)
- <a id="logger"></a>`logger` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/env.py#L26)

