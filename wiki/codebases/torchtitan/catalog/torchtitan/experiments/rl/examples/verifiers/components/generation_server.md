---
title: 'Module: torchtitan/experiments/rl/examples/verifiers/components/generation_server.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/verifiers/components/generation_server.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.verifiers.components.generation_server`/
symbols:
  GenerationServer._handle_generate_request: GenerationServer#_handle_generate_request().
  GenerationServer.start: GenerationServer#start().
  _parse_sampling_config: _parse_sampling_config().
  GenerationServer.close: GenerationServer#close().
  GenerationServer: GenerationServer#
  GenerationServer.Config: GenerationServer#Config#
  GenerationServer.pop_generation_metadata: GenerationServer#pop_generation_metadata().
  VerifiersGenerationMetadata: VerifiersGenerationMetadata#
  VerifiersGenerationMetadata.metrics: VerifiersGenerationMetadata#metrics.
  GenerationServer.generation_metadata: GenerationServer#generation_metadata.
  GenerationServer.set_generate_fn: GenerationServer#set_generate_fn().
  GenerationServer.host: GenerationServer#host.
  GenerationServer.generate_fn: GenerationServer#generate_fn.
  VerifiersGenerationMetadata.min_policy_version: VerifiersGenerationMetadata#min_policy_version.
  VerifiersGenerationMetadata.max_policy_version: VerifiersGenerationMetadata#max_policy_version.
  GenerationServer.bound_port: GenerationServer#bound_port.
  GenerationServer.base_url: GenerationServer#base_url().
  GenerationServer.runner: GenerationServer#runner.
  GenerationServer.request_counts: GenerationServer#request_counts.
  GenerationServer.requested_port: GenerationServer#requested_port.
  GenerationServer.port: GenerationServer#port().
  GenerationServer.Config.__post_init__: GenerationServer#Config#__post_init__().
  GenerationServer.__init__: GenerationServer#__init__().
  logger: logger.
  _SESSION_ID_HEADER: _SESSION_ID_HEADER.
  GenerationServer.Config.port: GenerationServer#Config#port.
  _validate_token_ids: _validate_token_ids().
  GenerationServer.Config.host: GenerationServer#Config#host.
  GenerationServer.model_id: GenerationServer#model_id.
  GenerationServer._handle_health_request: GenerationServer#_handle_health_request().
---
# Module: [`torchtitan/experiments/rl/examples/verifiers/components/generation_server.py`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py)

## Classes
### <a id="GenerationServer"></a>`GenerationServer`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/examples/verifiers/components/generation_server.py:45`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L45)
- doc: Expose a TorchTitan `GenerateFn` through Verifiers' model API.
- signature: `class GenerationServer(Configurable):`
- members:
  - <a id="GenerationServer.base_url"></a>`base_url(self)` — [`L85`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L85) — OpenAI-compatible base URL used by the local Verifiers client.
  - <a id="GenerationServer.close"></a>`close(self)` — [`L114`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L114)
  - <a id="GenerationServer.pop_generation_metadata"></a>`pop_generation_metadata(self, session_id: str)` — [`L123`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L123) — Detach the generation metadata accumulated for one rollout.
  - <a id="GenerationServer.port"></a>`port(self)` — [`L79`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L79)
  - <a id="GenerationServer.set_generate_fn"></a>`set_generate_fn(self, generate_fn: GenerateFn)` — [`L89`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L89)
  - <a id="GenerationServer.start"></a>`start(self)` — [`L92`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L92)
  - <a id="GenerationServer.bound_port"></a>`bound_port` — [`L74`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L74)
  - <a id="GenerationServer.generate_fn"></a>`generate_fn` — [`L72`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L72)
  - <a id="GenerationServer.generation_metadata"></a>`generation_metadata` — [`L76`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L76)
  - <a id="GenerationServer.host"></a>`host` — [`L70`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L70)
  - <a id="GenerationServer.model_id"></a>`model_id` — [`L67`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L67)
  - <a id="GenerationServer.request_counts"></a>`request_counts` — [`L75`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L75)
  - <a id="GenerationServer.requested_port"></a>`requested_port` — [`L71`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L71)
  - <a id="GenerationServer.runner"></a>`runner` — [`L73`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L73)
- protocol/private: <a id="GenerationServer.__init__"></a>`__init__`[`L69`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L69), <a id="GenerationServer._handle_generate_request"></a>`_handle_generate_request`[`L134`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L134), <a id="GenerationServer._handle_health_request"></a>`_handle_health_request`[`L130`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L130)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable), [`GenerateFn`](../../../rollout/types.md#GenerateFn), [`token_ids`](../../../types.md#Completion.token_ids), [`finish_reason`](../../../types.md#Completion.finish_reason), [`min_policy_version`](../../../types.md#Completion.min_policy_version), [`max_policy_version`](../../../types.md#Completion.max_policy_version), [`token_logprobs`](../../../types.md#Completion.token_logprobs), [`metrics`](../../../types.md#Completion.metrics), [`request_id`](../../../types.md#Completion.request_id), `_server`  (11 test-only)
- used by: [`Configurable`](../../../../../config/configurable.md#Configurable)  (7 test-only)

### <a id="GenerationServer.Config"></a>`GenerationServer.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/verifiers/components/generation_server.py:56`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L56)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="GenerationServer.Config.host"></a>`host` — [`L57`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L57) — ---
  - <a id="GenerationServer.Config.port"></a>`port` — [`L60`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L60) — ---
- protocol/private: <a id="GenerationServer.Config.__post_init__"></a>`__post_init__`[`L63`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L63)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../../../config/configurable.md#Configurable), [`Config`](../../../../../config/configurable.md#Configurable.Config)
- used by: (6 test-only callers)

### <a id="VerifiersGenerationMetadata"></a>`VerifiersGenerationMetadata`
- def: [`torchtitan/experiments/rl/examples/verifiers/components/generation_server.py:27`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L27)
- doc: TorchTitan generation data aggregated over one Verifiers rollout.
- signature: `class VerifiersGenerationMetadata:`
- members:
  - <a id="VerifiersGenerationMetadata.max_policy_version"></a>`max_policy_version` — [`L38`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L38) — ---
  - <a id="VerifiersGenerationMetadata.metrics"></a>`metrics` — [`L41`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L41) — ---
  - <a id="VerifiersGenerationMetadata.min_policy_version"></a>`min_policy_version` — [`L35`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L35) — ---
- uses (calls/refs, reference-scoped): [`Metric`](../../../observability/metrics/types.md#Metric)
- used by: (6 test-only callers)

## Functions
- <a id="_parse_sampling_config"></a>`_parse_sampling_config(value: object)` — [`L248`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L248) — Convert Verifiers' vLLM sampling payload to TorchTitan config.
- <a id="_validate_token_ids"></a>`_validate_token_ids(value: object, *, field_name: str)` — [`L238`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L238) — Validate an untyped JSON value as integer token IDs and return a copy.

## Module values
- <a id="_SESSION_ID_HEADER"></a>`_SESSION_ID_HEADER` — [`L23`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L23)
- <a id="logger"></a>`logger` — [`L21`](../../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/verifiers/components/generation_server.py#L21)

