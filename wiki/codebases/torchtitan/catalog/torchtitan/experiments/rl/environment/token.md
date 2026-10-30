---
title: 'Module: torchtitan/experiments/rl/environment/token.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/environment/token.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.environment.token`/
symbols:
  TokenEnv.step: TokenEnv#step().
  TokenEnv.init: TokenEnv#init().
  TokenEnv: TokenEnv#
  TokenEnvOutput: TokenEnvOutput#
  TokenEnvOutput.status: TokenEnvOutput#status.
  TokenEnv.Config: TokenEnv#Config#
  TokenEnvOutput.next_prompt_token_ids: TokenEnvOutput#next_prompt_token_ids.
  TokenEnvOutput.next_prompt_messages: TokenEnvOutput#next_prompt_messages.
  TokenEnvOutput.completion_message: TokenEnvOutput#completion_message.
  TokenEnv._messages: TokenEnv#_messages.
  TokenEnv._is_prompt_too_long: TokenEnv#_is_prompt_too_long().
  TokenEnv.close: TokenEnv#close().
  TokenEnvOutput.env_messages: TokenEnvOutput#env_messages.
  TokenEnvOutput.env_rewards: TokenEnvOutput#env_rewards.
  TokenEnv.Config.max_num_turns: TokenEnv#Config#max_num_turns.
  TokenEnv.__init__: TokenEnv#__init__().
  TokenEnv._tools: TokenEnv#_tools.
  TokenEnv.Config.max_rollout_tokens: TokenEnv#Config#max_rollout_tokens.
  TokenEnv._message_env: TokenEnv#_message_env.
  TokenEnv._renderer: TokenEnv#_renderer.
  TokenEnv._config: TokenEnv#_config.
  TokenEnv._last_prompt_token_ids: TokenEnv#_last_prompt_token_ids.
  logger: logger.
  TokenEnv._num_turns: TokenEnv#_num_turns.
  TokenEnv.Config.step_timeout_s: TokenEnv#Config#step_timeout_s.
---
# Module: [`torchtitan/experiments/rl/environment/token.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py)

## Classes
### <a id="TokenEnv"></a>`TokenEnv`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/environment/token.py:52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L52)
- doc: Token-space env used to wrap a `MessageEnv` and drive it in tokens.
- signature: `class TokenEnv(Configurable):`
- members:
  - <a id="TokenEnv.close"></a>`close(self)` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L297)
  - <a id="TokenEnv.init"></a>`init(self)` — [`L116`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L116) — Render the initial conversation into the first generator prompt.
  - <a id="TokenEnv.step"></a>`step(self, completion: Completion)` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L147) — Advance the env by one sampled completion from the generator.
- protocol/private: <a id="TokenEnv.__init__"></a>`__init__`[`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L101), <a id="TokenEnv._config"></a>`_config`[`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L110), <a id="TokenEnv._is_prompt_too_long"></a>`_is_prompt_too_long`[`L300`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L300), <a id="TokenEnv._last_prompt_token_ids"></a>`_last_prompt_token_ids`[`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L113), <a id="TokenEnv._message_env"></a>`_message_env`[`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L108), <a id="TokenEnv._messages"></a>`_messages`[`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L112), <a id="TokenEnv._num_turns"></a>`_num_turns`[`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L114), <a id="TokenEnv._renderer"></a>`_renderer`[`L109`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L109), <a id="TokenEnv._tools"></a>`_tools`[`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L111)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`RolloutStatus`](../rollout/types.md#RolloutStatus), [`Completion`](../types.md#Completion), [`MessageEnv`](message.md#MessageEnv), [`TokenEnvOutput`](token.md#TokenEnvOutput), [`env_messages`](message.md#MessageEnvStepOutput.env_messages), [`status`](token.md#TokenEnvOutput.status), [`Config`](token.md#TokenEnv.Config), [`next_prompt_token_ids`](token.md#TokenEnvOutput.next_prompt_token_ids), [`step`](message.md#MessageEnv.step), [`token_ids`](../types.md#Completion.token_ids), [`finish_reason`](../types.md#Completion.finish_reason), [`init`](message.md#MessageEnv.init), [`next_prompt_messages`](token.md#TokenEnvOutput.next_prompt_messages), [`done`](message.md#MessageEnvStepOutput.done), [`COMPLETED`](../rollout/types.md#RolloutStatus.COMPLETED), [`completion_message`](token.md#TokenEnvOutput.completion_message), [`init_prompt_messages`](message.md#MessageEnvInitOutput.init_prompt_messages), [`ONGOING`](../rollout/types.md#RolloutStatus.ONGOING), [`env_messages`](token.md#TokenEnvOutput.env_messages), [`env_rewards`](token.md#TokenEnvOutput.env_rewards), [`max_num_turns`](token.md#TokenEnv.Config.max_num_turns), [`tools`](message.md#MessageEnvInitOutput.tools), [`env_rewards`](message.md#MessageEnvStepOutput.env_rewards), [`max_rollout_tokens`](token.md#TokenEnv.Config.max_rollout_tokens), [`TRUNCATED_PROMPT_TOO_LONG`](../rollout/types.md#RolloutStatus.TRUNCATED_PROMPT_TOO_LONG), [`TRUNCATED_LENGTH`](../rollout/types.md#RolloutStatus.TRUNCATED_LENGTH), [`TRUNCATED_MAX_TURNS`](../rollout/types.md#RolloutStatus.TRUNCATED_MAX_TURNS), [`logger`](token.md#logger), [`ERROR_ABORT`](../rollout/types.md#RolloutStatus.ERROR_ABORT), [`ERROR_PARSE`](../rollout/types.md#RolloutStatus.ERROR_PARSE), [`ERROR_TIMEOUT`](../rollout/types.md#RolloutStatus.ERROR_TIMEOUT), [`close`](message.md#MessageEnv.close), [`step_timeout_s`](token.md#TokenEnv.Config.step_timeout_s)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_run_single_rollout`](../rollout/rollouter.md#RolloutWorker._run_single_rollout), [`run_group`](../rollout/rollouter.md#RolloutWorker.run_group), [`make_env_group`](../rollout/rollouter.md#RolloutWorker.make_env_group), [`token_env`](../rollout/rollouter.md#RolloutWorker.Config.token_env)  (4 test-only)

### <a id="TokenEnv.Config"></a>`TokenEnv.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/environment/token.py:86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L86)
- doc: Limits enforced by the wrapper
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="TokenEnv.Config.max_num_turns"></a>`max_num_turns` — [`L97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L97) — ---
  - <a id="TokenEnv.Config.max_rollout_tokens"></a>`max_rollout_tokens` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L89) — ---
  - <a id="TokenEnv.Config.step_timeout_s"></a>`step_timeout_s` — [`L94`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L94) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`step`](token.md#TokenEnv.step), [`_is_prompt_too_long`](token.md#TokenEnv._is_prompt_too_long), [`token_env`](../rollout/rollouter.md#RolloutWorker.Config.token_env), [`__init__`](token.md#TokenEnv.__init__)  (4 test-only)

### <a id="TokenEnvOutput"></a>`TokenEnvOutput`
- def: [`torchtitan/experiments/rl/environment/token.py:24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L24)
- doc: What `TokenEnv` produced this turn. Output only — it does not carry the prompt that was fed
- signature: `class TokenEnvOutput:`
- members:
  - <a id="TokenEnvOutput.completion_message"></a>`completion_message` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L39) — ---
  - <a id="TokenEnvOutput.env_messages"></a>`env_messages` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L43) — ---
  - <a id="TokenEnvOutput.env_rewards"></a>`env_rewards` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L47) — ---
  - <a id="TokenEnvOutput.next_prompt_messages"></a>`next_prompt_messages` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L33) — ---
  - <a id="TokenEnvOutput.next_prompt_token_ids"></a>`next_prompt_token_ids` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L29) — ---
  - <a id="TokenEnvOutput.status"></a>`status` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L36) — ---
- uses (calls/refs, reference-scoped): [`RolloutStatus`](../rollout/types.md#RolloutStatus)
- used by: [`_run_single_rollout`](../rollout/rollouter.md#RolloutWorker._run_single_rollout), [`step`](token.md#TokenEnv.step), [`init`](token.md#TokenEnv.init)  (2 test-only)

## Module values
- <a id="logger"></a>`logger` — [`L20`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/token.py#L20)

