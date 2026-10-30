---
title: 'Module: torchtitan/experiments/rl/environment/message.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/environment/message.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.environment.message`/
symbols:
  MessageEnv: MessageEnv#
  MessageEnvStepOutput: MessageEnvStepOutput#
  MessageEnvStepOutput.env_messages: MessageEnvStepOutput#env_messages.
  MessageEnvInitOutput: MessageEnvInitOutput#
  MessageEnv.step: MessageEnv#step().
  MessageEnv.init: MessageEnv#init().
  MessageEnvStepOutput.done: MessageEnvStepOutput#done.
  MessageEnv.Config: MessageEnv#Config#
  MessageEnvInitOutput.init_prompt_messages: MessageEnvInitOutput#init_prompt_messages.
  MessageEnvInitOutput.tools: MessageEnvInitOutput#tools.
  MessageEnvStepOutput.env_rewards: MessageEnvStepOutput#env_rewards.
  MessageEnvStepOutput.__post_init__: MessageEnvStepOutput#__post_init__().
  MessageEnv.close: MessageEnv#close().
---
# Module: [`torchtitan/experiments/rl/environment/message.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py)

## Classes
### <a id="MessageEnv"></a>`MessageEnv`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/experiments/rl/environment/message.py:51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L51)
- doc: User-written env in message space. Implement `init` + `step`.
- signature: `class MessageEnv(Configurable, abc.ABC):`
- members:
  - <a id="MessageEnv.close"></a>`close(self)` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L107) — Release env-owned resources. Default no-op; idempotent.
  - <a id="MessageEnv.init"></a>`init(self)` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L89) — Return the initial conversation + tools for prompt rendering.
  - <a id="MessageEnv.step"></a>`step(self, completion_message: Message)` — [`L93`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L93) — Advance the env one turn given the completion message.
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`MessageEnvStepOutput`](message.md#MessageEnvStepOutput), [`MessageEnvInitOutput`](message.md#MessageEnvInitOutput)  (9 test-only)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`step`](token.md#TokenEnv.step), [`init`](token.md#TokenEnv.init), [`close`](token.md#TokenEnv.close), [`message_env`](../rollout/rollouter.md#RolloutWorker.Config.message_env), [`__init__`](token.md#TokenEnv.__init__)  (6 test-only)

### <a id="MessageEnv.Config"></a>`MessageEnv.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/environment/message.py:85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L85)
- doc: Static env params; the per-rollout example is passed to `build(env_input=...)`.
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`message_env`](../rollout/rollouter.md#RolloutWorker.Config.message_env)  (3 test-only)

### <a id="MessageEnvInitOutput"></a>`MessageEnvInitOutput`
- def: [`torchtitan/experiments/rl/environment/message.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L18)
- doc: Initial messages + tool specs from `MessageEnv.init`.
- signature: `class MessageEnvInitOutput:`
- members:
  - <a id="MessageEnvInitOutput.init_prompt_messages"></a>`init_prompt_messages` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L21) — ---
  - <a id="MessageEnvInitOutput.tools"></a>`tools` — [`L24`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L24) — ---
- used by: [`init`](token.md#TokenEnv.init), [`init`](message.md#MessageEnv.init)  (8 test-only)

### <a id="MessageEnvStepOutput"></a>`MessageEnvStepOutput`
- def: [`torchtitan/experiments/rl/environment/message.py:29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L29)
- doc: The env's reply to the assistant's turn.
- signature: `class MessageEnvStepOutput:`
- members:
  - <a id="MessageEnvStepOutput.done"></a>`done` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L36) — ---
  - <a id="MessageEnvStepOutput.env_messages"></a>`env_messages` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L32) — ---
  - <a id="MessageEnvStepOutput.env_rewards"></a>`env_rewards` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L39) — ---
- protocol/private: <a id="MessageEnvStepOutput.__post_init__"></a>`__post_init__`[`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/environment/message.py#L43)
- used by: [`step`](token.md#TokenEnv.step), [`step`](message.md#MessageEnv.step)  (9 test-only)

