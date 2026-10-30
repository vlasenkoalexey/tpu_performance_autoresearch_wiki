---
title: 'Module: torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.rl_nc_ray.vllm_mocks`/
symbols:
  vllm_codegen: vllm_codegen.
  patched_init: patched_init().
  vllm_compilation: vllm_compilation.
  vllm_decorators: vllm_decorators.
  e: e.
  logger: logger.
  patched_create_config: patched_create_config().
  patched_attention_forward: patched_attention_forward().
  dummy_support_torch_compile: dummy_support_torch_compile().
  original_create_config: original_create_config.
  original_init: original_init.
  patched_init.patched_build: patched_init().patched_build().
  patched_init.patched_parallelize: patched_init().patched_parallelize().
  original_attention_forward: original_attention_forward.
---
# Module: [`torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py)

## Functions
- <a id="dummy_support_torch_compile"></a>`dummy_support_torch_compile(*args, **kwargs)` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L48) — A mock decorator replacing vllm's support_torch_compile.
- <a id="patched_attention_forward"></a>`patched_attention_forward(self, query, key, value, *args, **kwargs)` — [`L193`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L193)
- <a id="patched_init.patched_build"></a>`patched_build(*b_args, **b_kwargs)` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L153)
- <a id="patched_create_config"></a>`patched_create_config(vllm_config)` — [`L86`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L86) — Intercepts and modifies config translation to prevent world size assertion errors.
- <a id="patched_init"></a>`patched_init(self, *, model_spec, vllm_config, **kwargs)` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L131) — Modified constructor supporting meta device instantiation on TPUs.
- <a id="patched_init.patched_parallelize"></a>`patched_parallelize(*p_args, **p_kwargs)` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L161)

## Module values
- <a id="e"></a>`e` — [`L15`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L15)
- <a id="logger"></a>`logger` — [`L7`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L7)
- <a id="original_attention_forward"></a>`original_attention_forward` — [`L192`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L192)
- <a id="original_create_config"></a>`original_create_config` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L84)
- <a id="original_init"></a>`original_init` — [`L129`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L129)
- <a id="vllm_codegen"></a>`vllm_codegen` — [`L19`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L19)
- <a id="vllm_compilation"></a>`vllm_compilation` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L32)
- <a id="vllm_decorators"></a>`vllm_decorators` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/rl_nc_ray/vllm_mocks.py#L66)

