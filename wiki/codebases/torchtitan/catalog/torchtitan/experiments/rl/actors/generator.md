---
title: 'Module: torchtitan/experiments/rl/actors/generator.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/actors/generator.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.actors.generator`/
symbols:
  VLLMGenerator.model_path: VLLMGenerator#model_path.
  VLLMGenerator._engine_loop: VLLMGenerator#_engine_loop().
  SamplingConfig: SamplingConfig#
  VLLMGenerator._tp_rank: VLLMGenerator#_tp_rank.
  VLLMGenerator._decide_next_action: VLLMGenerator#_decide_next_action().
  VLLMGenerator.Config.parallelism: VLLMGenerator#Config#parallelism.
  VLLMGenerator: VLLMGenerator#
  VLLMGenerator.generate: VLLMGenerator#generate().
  RequestDispatcher._rank0_resolve_futures: RequestDispatcher#_rank0_resolve_futures().
  _prepare_generation_request_metrics: _prepare_generation_request_metrics().
  VLLMGenerator._pull_model_state_dict: VLLMGenerator#_pull_model_state_dict().
  VLLMGenerator._request_dispatcher: VLLMGenerator#_request_dispatcher.
  VLLMCudagraphConfig: VLLMCudagraphConfig#
  VLLMGenerator.Config: VLLMGenerator#Config#
  _extract_request_metrics_inputs: _extract_request_metrics_inputs().
  VLLMCudagraphConfig.enable: VLLMCudagraphConfig#enable.
  VLLMGenerator.close: VLLMGenerator#close().
  VLLMGenerator._engine: VLLMGenerator#_engine.
  VLLMGenerator.Config.checkpoint: VLLMGenerator#Config#checkpoint.
  VLLMCudagraphConfig.get_vllm_compilation_config: VLLMCudagraphConfig#get_vllm_compilation_config().
  SamplingConfig.temperature: SamplingConfig#temperature.
  SamplingConfig.top_p: SamplingConfig#top_p.
  SamplingConfig.max_tokens: SamplingConfig#max_tokens.
  RequestDispatcher._build_completions: RequestDispatcher#_build_completions().
  RequestDispatcher._rank0_dp_router: RequestDispatcher#_rank0_dp_router.
  VLLMGenerator.Config.model_dtype: VLLMGenerator#Config#model_dtype.
  VLLMGenerator.Config.sampling: VLLMGenerator#Config#sampling.
  VLLMGenerator.__init__: VLLMGenerator#__init__().
  VLLMGenerator.Config.cudagraph: VLLMGenerator#Config#cudagraph.
  RequestDispatcher.setup: RequestDispatcher#setup().
  VLLMGenerator.Config.__post_init__: VLLMGenerator#Config#__post_init__().
  VLLMGenerator.Config.debug: VLLMGenerator#Config#debug.
  VLLMGenerator._build_sampling_params: VLLMGenerator#_build_sampling_params().
  VLLMGenerator.pull_model_state_dict: VLLMGenerator#pull_model_state_dict().
  RequestDispatcher.process_finished_requests: RequestDispatcher#process_finished_requests().
  RequestDispatcher.rank0_route: RequestDispatcher#rank0_route().
  RequestDispatcher._rank0_generation_futures: RequestDispatcher#_rank0_generation_futures.
  LoopDecision.action: LoopDecision#action.
  VLLMGenerator._rank: VLLMGenerator#_rank.
  LoopAction: LoopAction#
  RequestDispatcher.rank0_register_future: RequestDispatcher#rank0_register_future().
  LoopDecision.requests_per_dp_rank: LoopDecision#requests_per_dp_rank.
  VLLMGenerator._fail_outstanding_futures: VLLMGenerator#_fail_outstanding_futures().
  VLLMGenerator._model_state_dict_pull_request: VLLMGenerator#_model_state_dict_pull_request.
  VLLMCudagraphConfig.mode: VLLMCudagraphConfig#mode.
  RequestDispatcher.rank0_stamp_min_policy_version: RequestDispatcher#rank0_stamp_min_policy_version().
  VLLMGenerator._engine_loop_condition: VLLMGenerator#_engine_loop_condition.
  VLLMGenerator._set_determinism: VLLMGenerator#_set_determinism().
  GenerationRequest: GenerationRequest#
  VLLMGenerator._dp_degree: VLLMGenerator#_dp_degree.
  VLLMGenerator._queued_generation_requests: VLLMGenerator#_queued_generation_requests.
  SamplingConfig.seed: SamplingConfig#seed.
  VLLMGenerator._pull_model_state_dict_future: VLLMGenerator#_pull_model_state_dict_future.
  VLLMGenerator.Config.override: VLLMGenerator#Config#override.
  VLLMGenerator._engine_loop_task: VLLMGenerator#_engine_loop_task.
  GenerationFuture.future: GenerationFuture#future.
  logger: logger.
  VLLMCudagraphConfig.capture_sizes: VLLMCudagraphConfig#capture_sizes.
  VLLMGenerator._rank0_check_engine_loop_running: VLLMGenerator#_rank0_check_engine_loop_running().
  ModelStateDictPullRequest: ModelStateDictPullRequest#
  _RequestMetricsInputs: _RequestMetricsInputs#
  VLLMGenerator.Config.vllm_stat_logger: VLLMGenerator#Config#vllm_stat_logger.
  LoopAction.STEP: LoopAction#STEP.
  VLLMGenerator._dp_rank: VLLMGenerator#_dp_rank.
  VLLMGenerator._close_request: VLLMGenerator#_close_request.
  RequestDispatcher._rank0_drain_results: RequestDispatcher#_rank0_drain_results().
  RequestDispatcher.fail_generation_futures: RequestDispatcher#fail_generation_futures().
  VLLMGenerator.Config.intra_generator_router: VLLMGenerator#Config#intra_generator_router.
  VLLMGenerator.Config.reset_prefix_cache_on_weight_sync: VLLMGenerator#Config#reset_prefix_cache_on_weight_sync.
  VLLMGenerator.Config.profiler: VLLMGenerator#Config#profiler.
  VLLMGenerator.start_engine_loop: VLLMGenerator#start_engine_loop().
  VLLMGenerator._get_spmd_state_dict: VLLMGenerator#_get_spmd_state_dict().
  GenerationRequest.sampling: GenerationRequest#sampling.
  RequestDispatcher: RequestDispatcher#
  RequestDispatcher.__init__: RequestDispatcher#__init__().
  RequestDispatcher._rank: RequestDispatcher#_rank.
  RequestDispatcher._rank0_drain_task: RequestDispatcher#_rank0_drain_task.
  VLLMGenerator.Config.max_num_batched_tokens: VLLMGenerator#Config#max_num_batched_tokens.
  VLLMGenerator.config: VLLMGenerator#config.
  GenerationRequest.request_id: GenerationRequest#request_id.
  GenerationFuture: GenerationFuture#
  _RequestMetricsInputs.num_cached_tokens: _RequestMetricsInputs#num_cached_tokens.
  _RequestMetricsInputs.num_generation_tokens: _RequestMetricsInputs#num_generation_tokens.
  RequestDispatcher._dp_degree: RequestDispatcher#_dp_degree.
  VLLMGenerator.Config.gpu_memory_limit: VLLMGenerator#Config#gpu_memory_limit.
  VLLMGenerator.policy_version: VLLMGenerator#policy_version.
  ModelStateDictPullRequest.version: ModelStateDictPullRequest#version.
  GenerationFuture.metrics_prefix: GenerationFuture#metrics_prefix.
  GenerationFuture.min_policy_version: GenerationFuture#min_policy_version.
  CloseRequest: CloseRequest#
  LoopDecision: LoopDecision#
  RequestDispatcher.rank0_has_pending_futures: RequestDispatcher#rank0_has_pending_futures().
  RequestDispatcher.shutdown: RequestDispatcher#shutdown().
  VLLMGenerator.build_stat_logger: VLLMGenerator#build_stat_logger().
  VLLMGenerator._get_model: VLLMGenerator#_get_model().
  VLLMGenerator.sync_log_step: VLLMGenerator#sync_log_step().
  _RequestMetricsInputs.has_stats: _RequestMetricsInputs#has_stats.
  _RequestMetricsInputs.scheduled_ts: _RequestMetricsInputs#scheduled_ts.
  _RequestMetricsInputs.first_token_ts: _RequestMetricsInputs#first_token_ts.
  SamplingConfig.stop_token_ids: SamplingConfig#stop_token_ids.
  RequestDispatcher._tp_rank: RequestDispatcher#_tp_rank.
  VLLMGenerator.Config.reset_running_requests_on_weight_sync: VLLMGenerator#Config#reset_running_requests_on_weight_sync.
  GenerationRequest.prompt_token_ids: GenerationRequest#prompt_token_ids.
  GenerationRequest.routing_session_id: GenerationRequest#routing_session_id.
  LoopAction.PULL_MODEL_STATE_DICT: LoopAction#PULL_MODEL_STATE_DICT.
  LoopAction.CLOSE: LoopAction#CLOSE.
  LoopDecision.pull_version: LoopDecision#pull_version.
  _RequestMetricsInputs.queued_ts: _RequestMetricsInputs#queued_ts.
  _RequestMetricsInputs.last_token_ts: _RequestMetricsInputs#last_token_ts.
  _RequestMetricsInputs.first_token_latency: _RequestMetricsInputs#first_token_latency.
  RequestDispatcher._result_port: RequestDispatcher#_result_port.
  RequestDispatcher._rank0_result_receiver: RequestDispatcher#_rank0_result_receiver.
  VLLMGenerator._max_num_seqs: VLLMGenerator#_max_num_seqs.
  VLLMGenerator._broadcast_group: VLLMGenerator#_broadcast_group.
  _DEFAULT_MAX_NUM_BATCHED_TOKENS: _DEFAULT_MAX_NUM_BATCHED_TOKENS.
  RequestDispatcher._dp_rank: RequestDispatcher#_dp_rank.
  RequestDispatcher._broadcast_group: RequestDispatcher#_broadcast_group.
  VLLMGenerator.Config.max_engine_steps_between_decisions: VLLMGenerator#Config#max_engine_steps_between_decisions.
  VLLMGenerator.model_spec: VLLMGenerator#model_spec.
---
# Module: [`torchtitan/experiments/rl/actors/generator.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py)

## Classes
### <a id="CloseRequest"></a>`CloseRequest`
- def: [`torchtitan/experiments/rl/actors/generator.py:1467`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1467)
- used by: [`close`](generator.md#VLLMGenerator.close), [`_close_request`](generator.md#VLLMGenerator._close_request)  (1 test-only)

### <a id="GenerationFuture"></a>`GenerationFuture`
- def: [`torchtitan/experiments/rl/actors/generator.py:1475`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1475)
- members:
  - <a id="GenerationFuture.future"></a>`future` — [`L1478`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1478)
  - <a id="GenerationFuture.metrics_prefix"></a>`metrics_prefix` — [`L1479`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1479) — ---
  - <a id="GenerationFuture.min_policy_version"></a>`min_policy_version` — [`L1481`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1481) — ---
- uses (calls/refs, reference-scoped): [`Completion`](../types.md#Completion)
- used by: [`_rank0_resolve_futures`](generator.md#RequestDispatcher._rank0_resolve_futures), [`_rank0_generation_futures`](generator.md#RequestDispatcher._rank0_generation_futures), [`rank0_register_future`](generator.md#RequestDispatcher.rank0_register_future), [`rank0_stamp_min_policy_version`](generator.md#RequestDispatcher.rank0_stamp_min_policy_version), [`fail_generation_futures`](generator.md#RequestDispatcher.fail_generation_futures)  (2 test-only)

### <a id="GenerationRequest"></a>`GenerationRequest`
- def: [`torchtitan/experiments/rl/actors/generator.py:1450`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1450) — documented in [rl-training](../../../../../concepts/rl-training.md)
- members:
  - <a id="GenerationRequest.prompt_token_ids"></a>`prompt_token_ids` — [`L1454`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1454)
  - <a id="GenerationRequest.request_id"></a>`request_id` — [`L1453`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1453)
  - <a id="GenerationRequest.routing_session_id"></a>`routing_session_id` — [`L1456`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1456)
  - <a id="GenerationRequest.sampling"></a>`sampling` — [`L1455`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1455)
- uses (calls/refs, reference-scoped): [`SamplingConfig`](generator.md#SamplingConfig)
- used by: [`_engine_loop`](generator.md#VLLMGenerator._engine_loop), [`generate`](generator.md#VLLMGenerator.generate), [`rank0_route`](generator.md#RequestDispatcher.rank0_route), [`requests_per_dp_rank`](generator.md#LoopDecision.requests_per_dp_rank), [`rank0_stamp_min_policy_version`](generator.md#RequestDispatcher.rank0_stamp_min_policy_version), [`_queued_generation_requests`](generator.md#VLLMGenerator._queued_generation_requests)  (2 test-only)

### <a id="LoopAction"></a>`LoopAction`
- def: [`torchtitan/experiments/rl/actors/generator.py:1485`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1485)
- members:
  - <a id="LoopAction.CLOSE"></a>`CLOSE` — [`L1494`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1494)
  - <a id="LoopAction.PULL_MODEL_STATE_DICT"></a>`PULL_MODEL_STATE_DICT` — [`L1491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1491)
  - <a id="LoopAction.STEP"></a>`STEP` — [`L1488`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1488)
- used by: [`_engine_loop`](generator.md#VLLMGenerator._engine_loop), [`_decide_next_action`](generator.md#VLLMGenerator._decide_next_action), [`action`](generator.md#LoopDecision.action)  (6 test-only)

### <a id="LoopDecision"></a>`LoopDecision`
- def: [`torchtitan/experiments/rl/actors/generator.py:1499`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1499)
- members:
  - <a id="LoopDecision.action"></a>`action` — [`L1503`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1503)
  - <a id="LoopDecision.pull_version"></a>`pull_version` — [`L1510`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1510)
  - <a id="LoopDecision.requests_per_dp_rank"></a>`requests_per_dp_rank` — [`L1505`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1505)
- uses (calls/refs, reference-scoped): [`LoopAction`](generator.md#LoopAction), [`GenerationRequest`](generator.md#GenerationRequest)
- used by: [`_engine_loop`](generator.md#VLLMGenerator._engine_loop), [`_decide_next_action`](generator.md#VLLMGenerator._decide_next_action)  (6 test-only)

### <a id="ModelStateDictPullRequest"></a>`ModelStateDictPullRequest`
- def: [`torchtitan/experiments/rl/actors/generator.py:1460`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1460)
- members:
  - <a id="ModelStateDictPullRequest.version"></a>`version` — [`L1463`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1463)
- used by: [`_decide_next_action`](generator.md#VLLMGenerator._decide_next_action), [`load_model_state_dict`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.load_model_state_dict), [`pull_model_state_dict`](generator.md#VLLMGenerator.pull_model_state_dict), [`__init__`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.__init__), [`_model_state_dict_pull_request`](generator.md#VLLMGenerator._model_state_dict_pull_request), [`refs`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.refs)  (2 test-only)

### <a id="RequestDispatcher"></a>`RequestDispatcher`
- def: [`torchtitan/experiments/rl/actors/generator.py:352`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L352) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Handles the generator's DP/TP request dispatch.
- signature: `class RequestDispatcher:`
- members:
  - <a id="RequestDispatcher._build_completions"></a>`_build_completions(self, request_outputs: list[RequestOutput], policy_version: int)` — [`L544`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L544) — Turn finished ``RequestOutput``s into ``(request_id, Completion, metrics_inputs)``.
  - <a id="RequestDispatcher._rank0_drain_results"></a>`_rank0_drain_results(self)` — [`L626`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L626) — RANK 0 background task which receives and resolves completions pushed
  - <a id="RequestDispatcher._rank0_resolve_futures"></a>`_rank0_resolve_futures(self, completions: list[tuple[str, Completion, _RequestMetricsInputs]])` — [`L585`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L585) — RANK 0: build each completion's metrics (the only place that knows the
  - <a id="RequestDispatcher.fail_generation_futures"></a>`fail_generation_futures(self, exc: BaseException)` — [`L634`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L634) — RANK 0: fail every unresolved generation future after an exception or
  - <a id="RequestDispatcher.process_finished_requests"></a>`process_finished_requests(self, request_outputs: list[RequestOutput], policy_version: int)` — [`L525`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L525) — TP rank 0s send finished completions to global rank 0 after each
  - <a id="RequestDispatcher.rank0_has_pending_futures"></a>`rank0_has_pending_futures(self)` — [`L443`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L443) — RANK 0: whether any request is still in flight (future unresolved).
  - <a id="RequestDispatcher.rank0_register_future"></a>`rank0_register_future(self, request_id: str, metrics_prefix: str)` — [`L431`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L431) — RANK 0: register a future for ``request_id`` and return it to await.
  - <a id="RequestDispatcher.rank0_route"></a>`rank0_route(self, requests: list[GenerationRequest])` — [`L451`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L451) — RANK 0: pick which DP rank serves each queued request.
  - <a id="RequestDispatcher.rank0_stamp_min_policy_version"></a>`rank0_stamp_min_policy_version(self, requests_per_dp_rank: list[list[GenerationRequest]], policy_version: int)` — [`L479`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L479) — RANK 0: stamp the admitted (sampling) version on every future in this STEP
  - <a id="RequestDispatcher.setup"></a>`setup(self)` — [`L493`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L493) — One-time setup before the engine loop starts (DP>1): distribute rank 0's
  - <a id="RequestDispatcher.shutdown"></a>`shutdown(self)` — [`L642`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L642) — Stop rank 0's drain task, if any (no-op elsewhere).
- protocol/private: <a id="RequestDispatcher.__init__"></a>`__init__`[`L391`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L391), <a id="RequestDispatcher._broadcast_group"></a>`_broadcast_group`[`L406`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L406), <a id="RequestDispatcher._dp_degree"></a>`_dp_degree`[`L402`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L402), <a id="RequestDispatcher._dp_rank"></a>`_dp_rank`[`L403`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L403), <a id="RequestDispatcher._rank"></a>`_rank`[`L401`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L401), <a id="RequestDispatcher._rank0_dp_router"></a>`_rank0_dp_router`[`L425`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L425), <a id="RequestDispatcher._rank0_drain_task"></a>`_rank0_drain_task`[`L420`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L420), <a id="RequestDispatcher._rank0_generation_futures"></a>`_rank0_generation_futures`[`L410`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L410), <a id="RequestDispatcher._rank0_result_receiver"></a>`_rank0_result_receiver`[`L419`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L419), <a id="RequestDispatcher._result_port"></a>`_result_port`[`L418`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L418), <a id="RequestDispatcher._tp_rank"></a>`_tp_rank`[`L404`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L404)
- uses (calls/refs, reference-scoped): [`build`](../../../config/configurable.md#Configurable.Config.build), [`Metric`](../observability/metrics/types.md#Metric), [`_prepare_generation_request_metrics`](generator.md#_prepare_generation_request_metrics), [`Mean`](../observability/metrics/types.md#Mean), [`Max`](../observability/metrics/types.md#Max), [`_extract_request_metrics_inputs`](generator.md#_extract_request_metrics_inputs), [`Completion`](../types.md#Completion), [`IntraGeneratorRouter`](../routing/intra_generator_router.md#IntraGeneratorRouter), [`Config`](../routing/intra_generator_router.md#IntraGeneratorRouter.Config), [`reserve`](../routing/intra_generator_router.md#IntraGeneratorRouter.reserve), [`token_ids`](../types.md#Completion.token_ids), [`GenerationRequest`](generator.md#GenerationRequest), [`finish_reason`](../types.md#Completion.finish_reason), [`min_policy_version`](../types.md#Completion.min_policy_version), [`future`](generator.md#GenerationFuture.future), [`release`](../routing/intra_generator_router.md#IntraGeneratorRouter.release), [`max_policy_version`](../types.md#Completion.max_policy_version), [`token_logprobs`](../types.md#Completion.token_logprobs), [`_RequestMetricsInputs`](generator.md#_RequestMetricsInputs), [`metrics`](../types.md#Completion.metrics), [`request_id`](../types.md#Completion.request_id), [`GenerationFuture`](generator.md#GenerationFuture), [`request_id`](generator.md#GenerationRequest.request_id), [`metrics_prefix`](generator.md#GenerationFuture.metrics_prefix), [`min_policy_version`](generator.md#GenerationFuture.min_policy_version), [`routing_session_id`](generator.md#GenerationRequest.routing_session_id)
- used by: [`_engine_loop`](generator.md#VLLMGenerator._engine_loop), [`_decide_next_action`](generator.md#VLLMGenerator._decide_next_action), [`generate`](generator.md#VLLMGenerator.generate), [`_request_dispatcher`](generator.md#VLLMGenerator._request_dispatcher), [`close`](generator.md#VLLMGenerator.close), [`_fail_outstanding_futures`](generator.md#VLLMGenerator._fail_outstanding_futures)  (8 test-only)

### <a id="SamplingConfig"></a>`SamplingConfig`
- def: [`torchtitan/experiments/rl/actors/generator.py:332`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L332)
- doc: Sampling parameters passed to vLLM's SamplingParams.
- signature: `class SamplingConfig:`
- members:
  - <a id="SamplingConfig.max_tokens"></a>`max_tokens` — [`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L341) — ---
  - <a id="SamplingConfig.seed"></a>`seed` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L344) — ---
  - <a id="SamplingConfig.stop_token_ids"></a>`stop_token_ids` — [`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L348) — ---
  - <a id="SamplingConfig.temperature"></a>`temperature` — [`L335`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L335) — ---
  - <a id="SamplingConfig.top_p"></a>`top_p` — [`L338`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L338) — ---
- used by: [`_run_single_rollout`](../rollout/rollouter.md#RolloutWorker._run_single_rollout), [`generate`](generator.md#VLLMGenerator.generate), [`run_group`](../rollout/rollouter.md#RolloutWorker.run_group), [`_collect_validation_rollouts`](../controller.md#Controller._collect_validation_rollouts), [`sampling`](generator.md#VLLMGenerator.Config.sampling), [`_build_sampling_params`](generator.md#VLLMGenerator._build_sampling_params), [`run_group_rollouts`](../rollout/rollouter.md#Rollouter.run_group_rollouts), [`generate`](../controller.md#Controller.generate), [`sampling`](generator.md#GenerationRequest.sampling), [`__call__`](../rollout/types.md#GenerateFn.__call__)  (27 test-only)

### <a id="VLLMCudagraphConfig"></a>`VLLMCudagraphConfig`
- def: [`torchtitan/experiments/rl/actors/generator.py:180`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L180)
- doc: CUDA graph capture settings for the vLLM inference engine.
- signature: `class VLLMCudagraphConfig:`
- members:
  - <a id="VLLMCudagraphConfig.get_vllm_compilation_config"></a>`get_vllm_compilation_config(self, *, max_num_seqs: int, expert_sequence_parallel_size: int, enable_sequence_parallel: bool, max_num_batched_tokens: int | None = None)` — [`L226`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L226) — Build a vLLM ``CompilationConfig`` for the generator.
  - <a id="VLLMCudagraphConfig.capture_sizes"></a>`capture_sizes` — [`L210`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L210) — ---
  - <a id="VLLMCudagraphConfig.enable"></a>`enable` — [`L192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L192) — ---
  - <a id="VLLMCudagraphConfig.mode"></a>`mode` — [`L195`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L195) — ---
- uses (calls/refs, reference-scoped): [`logger`](generator.md#logger), [`_DEFAULT_MAX_NUM_BATCHED_TOKENS`](generator.md#_DEFAULT_MAX_NUM_BATCHED_TOKENS)
- used by: [`model_path`](generator.md#VLLMGenerator.model_path), [`_tp_rank`](generator.md#VLLMGenerator._tp_rank), [`cudagraph`](generator.md#VLLMGenerator.Config.cudagraph)  (24 test-only)

### <a id="VLLMGenerator"></a>`VLLMGenerator`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/actors/generator.py:653`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L653)
- doc: vLLM engine to drive concurrent `generate` calls through one SPMD engine loop.
- signature: `class VLLMGenerator(Actor, Configurable):`
- members:
  - <a id="VLLMGenerator._build_sampling_params"></a>`_build_sampling_params(self, sampling: SamplingConfig)` — [`L1277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1277) — Translate a `SamplingConfig` into vLLM `SamplingParams` (n=1).
  - <a id="VLLMGenerator._decide_next_action"></a>`_decide_next_action(self)` — [`L1232`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1232) — RANK 0: picks the next action. Sleeps until there is something to do.
  - <a id="VLLMGenerator._engine_loop"></a>`_engine_loop(self)` — [`L1131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1131) — Non-stop loop running on all ranks to produce new tokens.
  - <a id="VLLMGenerator._fail_outstanding_futures"></a>`_fail_outstanding_futures(self, exc: BaseException)` — [`L1267`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1267) — Fail every unresolved future after an exception or engine teardown.
  - <a id="VLLMGenerator._get_model"></a>`_get_model(self)` — [`L1042`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1042) — Access the model from the vLLM engine.
  - <a id="VLLMGenerator._get_spmd_state_dict"></a>`_get_spmd_state_dict(self, model_sd: dict, *, model)` — [`L1375`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1375) — Fetch trainer-pushed weights into a spmd_types generator state dict.
  - <a id="VLLMGenerator._pull_model_state_dict"></a>`_pull_model_state_dict(self, version: int)` — [`L1333`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1333) — ALL RANKS: collectively copy the latest weights from TorchStore, optionally drop the
  - <a id="VLLMGenerator._rank0_check_engine_loop_running"></a>`_rank0_check_engine_loop_running(self, endpoint_name: str)` — [`L1059`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1059) — Guard for the rank-0-only endpoints
  - <a id="VLLMGenerator._set_determinism"></a>`_set_determinism(debug: DebugConfig)` — [`L1025`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1025) — Apply deterministic flags for the generator.
  - <a id="VLLMGenerator.build_stat_logger"></a>`build_stat_logger(vllm_config, engine_index)` — [`L954`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L954)
  - <a id="VLLMGenerator.close"></a>`close(self)` — [`L1400`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1400) — Stop the engine loop, then release the vLLM engine.
  - <a id="VLLMGenerator.generate"></a>`generate(self, prompt_token_ids: list[int], *, request_id: str, routing_session_id: str, sampling_config: SamplingConfig | None = None, metrics_prefix: str = "generator")` — [`L1070`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1070) — Generates one completion for one prompt.
  - <a id="VLLMGenerator.pull_model_state_dict"></a>`pull_model_state_dict(self, version: int)` — [`L1302`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1302) — Queues a weight pull for `version` and blocks until the engine loop has finished pulling.
  - <a id="VLLMGenerator.start_engine_loop"></a>`start_engine_loop(self)` — [`L1054`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1054) — Start the background engine loop on every rank (one-time, idempotent).
  - <a id="VLLMGenerator.sync_log_step"></a>`sync_log_step(self, step: int, relative_step: int | None = None)` — [`L1049`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1049) — Sync the structured-logger step counter from the controller.
  - <a id="VLLMGenerator.config"></a>`config` — [`L825`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L825)
  - <a id="VLLMGenerator.model_path"></a>`model_path` — [`L869`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L869)
  - <a id="VLLMGenerator.model_spec"></a>`model_spec` — [`L826`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L826)
  - <a id="VLLMGenerator.policy_version"></a>`policy_version` — [`L992`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L992)
- protocol/private: <a id="VLLMGenerator.__init__"></a>`__init__`[`L804`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L804), <a id="VLLMGenerator._broadcast_group"></a>`_broadcast_group`[`L995`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L995), <a id="VLLMGenerator._close_request"></a>`_close_request`[`L1015`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1015), <a id="VLLMGenerator._dp_degree"></a>`_dp_degree`[`L831`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L831), <a id="VLLMGenerator._dp_rank"></a>`_dp_rank`[`L834`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L834), <a id="VLLMGenerator._engine"></a>`_engine`[`L962`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L962), <a id="VLLMGenerator._engine_loop_condition"></a>`_engine_loop_condition`[`L996`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L996), <a id="VLLMGenerator._engine_loop_task"></a>`_engine_loop_task`[`L1020`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1020), <a id="VLLMGenerator._max_num_seqs"></a>`_max_num_seqs`[`L828`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L828), <a id="VLLMGenerator._model_state_dict_pull_request"></a>`_model_state_dict_pull_request`[`L1014`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1014), <a id="VLLMGenerator._pull_model_state_dict_future"></a>`_pull_model_state_dict_future`[`L1017`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1017), <a id="VLLMGenerator._queued_generation_requests"></a>`_queued_generation_requests`[`L1013`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1013), <a id="VLLMGenerator._rank"></a>`_rank`[`L830`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L830), <a id="VLLMGenerator._request_dispatcher"></a>`_request_dispatcher`[`L1003`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L1003), <a id="VLLMGenerator._tp_rank"></a>`_tp_rank`[`L835`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L835)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`model`](../../../protocols/model_spec.md#ModelSpec.model), [`build`](../../../config/configurable.md#Configurable.Config.build), [`CompileConfig`](../../../config/configs.md#CompileConfig), [`max_context_length`](../../../protocols/model_spec.md#ModelSpec.max_context_length), [`FlexInnerAttention`](../../../models/common/attention.md#FlexInnerAttention), [`ModelSpec`](../../../protocols/model_spec.md#ModelSpec), [`get_spmd_backend`](../../../distributed/utils.md#get_spmd_backend), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`VarlenInnerAttention`](../../../models/common/attention.md#VarlenInnerAttention), [`SamplingConfig`](generator.md#SamplingConfig), [`parallelism`](generator.md#VLLMGenerator.Config.parallelism), [`register_to_vllm`](../models/vllm_registry.md#register_to_vllm), [`Config`](../../../models/common/attention.md#FlexInnerAttention.Config), [`Config`](../../../models/common/attention.md#VarlenInnerAttention.Config), [`tensor_parallel_degree`](../models/vllm_registry.md#InferenceParallelismConfig.tensor_parallel_degree), [`Config`](generator.md#VLLMGenerator.Config), [`DebugConfig`](../../../config/configs.md#DebugConfig), [`data_parallel_degree`](../models/vllm_registry.md#InferenceParallelismConfig.data_parallel_degree), [`has_cuda_capability`](../../../tools/utils.md#has_cuda_capability), [`enable`](generator.md#VLLMCudagraphConfig.enable), [`init_structured_logger`](../../../observability/structured_logger/structured_logging.md#init_structured_logger), [`checkpoint`](generator.md#VLLMGenerator.Config.checkpoint), [`get_vllm_compilation_config`](generator.md#VLLMCudagraphConfig.get_vllm_compilation_config), [`Completion`](../types.md#Completion), [`max_tokens`](generator.md#SamplingConfig.max_tokens), [`temperature`](generator.md#SamplingConfig.temperature), [`top_p`](generator.md#SamplingConfig.top_p), [`model_dtype`](generator.md#VLLMGenerator.Config.model_dtype), [`sampling`](generator.md#VLLMGenerator.Config.sampling), [`cudagraph`](generator.md#VLLMGenerator.Config.cudagraph), [`setup`](generator.md#RequestDispatcher.setup), [`log_trace_instant`](../../../observability/structured_logger/structured_logging.md#log_trace_instant), [`seed`](../../../config/configs.md#DebugConfig.seed), [`set_step`](../../../observability/structured_logger/step_state.md#set_step), [`debug`](generator.md#VLLMGenerator.Config.debug), [`plain_tensor_to_dtensor_state_dict`](../../../distributed/spmd_types.md#plain_tensor_to_dtensor_state_dict), [`init_logger`](../../../tools/logging.md#init_logger), [`process_finished_requests`](generator.md#RequestDispatcher.process_finished_requests), [`rank0_route`](generator.md#RequestDispatcher.rank0_route)  (+53 more)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`generator`](../controller.md#Controller.Config.generator), [`sync_log_step`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.sync_log_step), [`load_model_state_dict`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.load_model_state_dict), [`generator`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.generator), [`__init__`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.__init__), [`close`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.close), [`refs`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.__init__.CustomModelStateDictPullRequest.refs), [`stop_profile`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.stop_profile), [`start_profile`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.start_profile), [`generate`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.generate), [`start_engine_loop`](../../tpu/rl_nc_ray/generator.md#RayVLLMGenerator.start_engine_loop)  (31 test-only)

### <a id="VLLMGenerator.Config"></a>`VLLMGenerator.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/actors/generator.py:702`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L702)
- doc: Generator actor configuration.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="VLLMGenerator.Config.checkpoint"></a>`checkpoint` — [`L740`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L740) — ---
  - <a id="VLLMGenerator.Config.cudagraph"></a>`cudagraph` — [`L737`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L737) — ---
  - <a id="VLLMGenerator.Config.debug"></a>`debug` — [`L748`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L748) — ---
  - <a id="VLLMGenerator.Config.gpu_memory_limit"></a>`gpu_memory_limit` — [`L729`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L729) — ---
  - <a id="VLLMGenerator.Config.intra_generator_router"></a>`intra_generator_router` — [`L711`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L711) — ---
  - <a id="VLLMGenerator.Config.max_engine_steps_between_decisions"></a>`max_engine_steps_between_decisions` — [`L751`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L751) — ---
  - <a id="VLLMGenerator.Config.max_num_batched_tokens"></a>`max_num_batched_tokens` — [`L732`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L732) — ---
  - <a id="VLLMGenerator.Config.model_dtype"></a>`model_dtype` — [`L726`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L726) — ---
  - <a id="VLLMGenerator.Config.override"></a>`override` — [`L721`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L721) — ---
  - <a id="VLLMGenerator.Config.parallelism"></a>`parallelism` — [`L706`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L706) — ---
  - <a id="VLLMGenerator.Config.profiler"></a>`profiler` — [`L771`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L771) — ---
  - <a id="VLLMGenerator.Config.reset_prefix_cache_on_weight_sync"></a>`reset_prefix_cache_on_weight_sync` — [`L757`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L757) — ---
  - <a id="VLLMGenerator.Config.reset_running_requests_on_weight_sync"></a>`reset_running_requests_on_weight_sync` — [`L761`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L761) — ---
  - <a id="VLLMGenerator.Config.sampling"></a>`sampling` — [`L718`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L718) — ---
  - <a id="VLLMGenerator.Config.vllm_stat_logger"></a>`vllm_stat_logger` — [`L766`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L766) — ---
- protocol/private: <a id="VLLMGenerator.Config.__post_init__"></a>`__post_init__`[`L774`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L774)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`CheckpointManager`](../../../components/checkpointer/dcp.md#CheckpointManager), [`Config`](../../../components/checkpointer/dcp.md#CheckpointManager.Config), [`Config`](../../../config/configurable.md#Configurable.Config), [`Profiler`](../../../tools/profiler.md#Profiler), [`SamplingConfig`](generator.md#SamplingConfig), [`InferenceParallelismConfig`](../models/vllm_registry.md#InferenceParallelismConfig), [`tensor_parallel_degree`](../models/vllm_registry.md#InferenceParallelismConfig.tensor_parallel_degree), [`OverrideConfig`](../../../config/override.md#OverrideConfig), [`Config`](../../../tools/profiler.md#Profiler.Config), [`DebugConfig`](../../../config/configs.md#DebugConfig), [`VLLMCudagraphConfig`](generator.md#VLLMCudagraphConfig), [`data_parallel_degree`](../models/vllm_registry.md#InferenceParallelismConfig.data_parallel_degree), [`IntraGeneratorRouter`](../routing/intra_generator_router.md#IntraGeneratorRouter), [`Config`](../observability/vllm_otel_stat_logger.md#VllmOtelStatLogger.Config), [`VllmOtelStatLogger`](../observability/vllm_otel_stat_logger.md#VllmOtelStatLogger), [`Config`](../routing/intra_generator_router.md#IntraGeneratorRouter.Config), [`batch_invariant`](../../../config/configs.md#DebugConfig.batch_invariant), [`expert_parallel_degree`](../models/vllm_registry.md#InferenceParallelismConfig.expert_parallel_degree)
- used by: [`model_path`](generator.md#VLLMGenerator.model_path), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`_multi_node`](../../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`generator`](../controller.md#Controller.Config.generator), [`_engine_loop`](generator.md#VLLMGenerator._engine_loop), [`main`](../train.md#main), [`_tp_rank`](generator.md#VLLMGenerator._tp_rank), [`__post_init__`](../controller.md#Controller.Config.__post_init__), [`generate`](generator.md#VLLMGenerator.generate), [`_pull_model_state_dict`](generator.md#VLLMGenerator._pull_model_state_dict), [`_request_dispatcher`](generator.md#VLLMGenerator._request_dispatcher), [`__init__`](generator.md#VLLMGenerator.__init__), [`_sampling`](../controller.md#Controller._sampling), [`_dp_degree`](generator.md#VLLMGenerator._dp_degree), [`generator_profiler_config`](../../tpu/rl_nc_ray/grpo.md#RayController.generator_profiler_config)  (27 test-only)

### <a id="_RequestMetricsInputs"></a>`_RequestMetricsInputs`
- def: [`torchtitan/experiments/rl/actors/generator.py:76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L76)
- doc: Raw inputs needed to build a request's vLLM metrics. Used to pass
- signature: `class _RequestMetricsInputs:`
- members:
  - <a id="_RequestMetricsInputs.first_token_latency"></a>`first_token_latency` — [`L87`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L87)
  - <a id="_RequestMetricsInputs.first_token_ts"></a>`first_token_ts` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L85)
  - <a id="_RequestMetricsInputs.has_stats"></a>`has_stats` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L82)
  - <a id="_RequestMetricsInputs.last_token_ts"></a>`last_token_ts` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L86)
  - <a id="_RequestMetricsInputs.num_cached_tokens"></a>`num_cached_tokens` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L81)
  - <a id="_RequestMetricsInputs.num_generation_tokens"></a>`num_generation_tokens` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L88)
  - <a id="_RequestMetricsInputs.queued_ts"></a>`queued_ts` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L83)
  - <a id="_RequestMetricsInputs.scheduled_ts"></a>`scheduled_ts` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L84)
- used by: [`_rank0_resolve_futures`](generator.md#RequestDispatcher._rank0_resolve_futures), [`_prepare_generation_request_metrics`](generator.md#_prepare_generation_request_metrics), [`_extract_request_metrics_inputs`](generator.md#_extract_request_metrics_inputs), [`_build_completions`](generator.md#RequestDispatcher._build_completions)

## Functions
- <a id="_extract_request_metrics_inputs"></a>`_extract_request_metrics_inputs(request_output: RequestOutput)` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L91) — Pull the raw metric inputs off a finished ``RequestOutput``.
- <a id="_prepare_generation_request_metrics"></a>`_prepare_generation_request_metrics(inputs: _RequestMetricsInputs, *, prefix: str)` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L112) — Prepare vLLM per-request metrics from the raw inputs.

## Module values
- <a id="_DEFAULT_MAX_NUM_BATCHED_TOKENS"></a>`_DEFAULT_MAX_NUM_BATCHED_TOKENS` — [`L176`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L176)
- <a id="logger"></a>`logger` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/actors/generator.py#L70)

