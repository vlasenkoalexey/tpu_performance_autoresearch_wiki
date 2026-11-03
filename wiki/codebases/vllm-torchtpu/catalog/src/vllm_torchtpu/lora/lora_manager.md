---
title: 'Module: src/vllm_torchtpu/lora/lora_manager.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/lora/lora_manager.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.lora.lora_manager`/
symbols:
  _AdapterSlotWriter.write_slot: _AdapterSlotWriter#write_slot().
  TPULoRAModelManager._slot_writer: TPULoRAModelManager#_slot_writer.
  _AdapterSlotWriter.create: _AdapterSlotWriter#create().
  _AdapterSlotWriter.redirect_writes_to_host: _AdapterSlotWriter#redirect_writes_to_host().
  TPULoRAModelManager.slot_write_hbm_bytes: TPULoRAModelManager#slot_write_hbm_bytes().
  TPULoRAModelManager.activate_adapter: TPULoRAModelManager#activate_adapter().
  _AdapterSlotWriter._host_weights: _AdapterSlotWriter#_host_weights.
  _AdapterSlotWriter._host_views: _AdapterSlotWriter#_host_views().
  _AdapterSlotWriter.precompile: _AdapterSlotWriter#precompile().
  TPULoRAModelManager.precompile_activation: TPULoRAModelManager#precompile_activation().
  TPUWorkerLoRAManager.precompile_activation: TPUWorkerLoRAManager#precompile_activation().
  TPUWorkerLoRAManager.slot_write_hbm_bytes: TPUWorkerLoRAManager#slot_write_hbm_bytes().
  _warn_fallback: _warn_fallback().
  _stacked_weights: _stacked_weights().
  _AdapterSlotWriter._device_weights: _AdapterSlotWriter#_device_weights.
  _AdapterSlotWriter._host_slot_weights: _AdapterSlotWriter#_host_slot_weights.
  TPUWorkerLoRAManager: TPUWorkerLoRAManager#
  logger: logger.
  _AdapterSlotWriter.slot_bytes: _AdapterSlotWriter#slot_bytes().
  TPUWorkerLoRAManager.max_num_batched_tokens: TPUWorkerLoRAManager#max_num_batched_tokens.
  TPULoRAModelManager: TPULoRAModelManager#
  TPUWorkerLoRAManager._manager_cls: TPUWorkerLoRAManager#_manager_cls.
  _host_weights_like: _host_weights_like().
  _AdapterSlotWriter: _AdapterSlotWriter#
  _AdapterSlotWriter._modules: _AdapterSlotWriter#_modules.
  _AdapterSlotWriter._stacked_weights: _AdapterSlotWriter#_stacked_weights.
  _AdapterSlotWriter._slot_indices: _AdapterSlotWriter#_slot_indices.
  _SUPPORTED_LAYERS: _SUPPORTED_LAYERS.
  _as_tuple: _as_tuple().
  _AdapterSlotWriter._device: _AdapterSlotWriter#_device.
  _AdapterSlotWriter.__init__: _AdapterSlotWriter#__init__().
  TPULoRAModelManager.__init__: TPULoRAModelManager#__init__().
  TPUWorkerLoRAManager.__init__: TPUWorkerLoRAManager#__init__().
  TPUWorkerLoRAManager._load_adapter: TPUWorkerLoRAManager#_load_adapter().
---
# Module: [`src/vllm_torchtpu/lora/lora_manager.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py)

## Classes
### <a id="TPULoRAModelManager"></a>`TPULoRAModelManager`
- def: [`src/vllm_torchtpu/lora/lora_manager.py:235`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L235)
- doc: LRU LoRA model manager that loads an adapter into its slot at once.
- signature: `class TPULoRAModelManager(LRUCacheLoRAModelManager):`
- members:
  - <a id="TPULoRAModelManager.activate_adapter"></a>`activate_adapter(self, lora_id: int)` — [`L251`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L251)
  - <a id="TPULoRAModelManager.precompile_activation"></a>`precompile_activation(self)` — [`L268`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L268) — Compiles the slot write program at startup, before any adapter is
  - <a id="TPULoRAModelManager.slot_write_hbm_bytes"></a>`slot_write_hbm_bytes(self)` — [`L278`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L278) — HBM that writing an adapter into its slot takes on top of the LoRA
- protocol/private: <a id="TPULoRAModelManager.__init__"></a>`__init__`[`L245`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L245), <a id="TPULoRAModelManager._slot_writer"></a>`_slot_writer`[`L247`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L247)
- uses (calls/refs, reference-scoped): [`write_slot`](lora_manager.md#_AdapterSlotWriter.write_slot), [`create`](lora_manager.md#_AdapterSlotWriter.create), [`redirect_writes_to_host`](lora_manager.md#_AdapterSlotWriter.redirect_writes_to_host), [`precompile`](lora_manager.md#_AdapterSlotWriter.precompile), [`_stacked_weights`](lora_manager.md#_stacked_weights), [`slot_bytes`](lora_manager.md#_AdapterSlotWriter.slot_bytes), [`_AdapterSlotWriter`](lora_manager.md#_AdapterSlotWriter)
- used by: [`precompile_activation`](lora_manager.md#TPUWorkerLoRAManager.precompile_activation), [`slot_write_hbm_bytes`](lora_manager.md#TPUWorkerLoRAManager.slot_write_hbm_bytes), [`_manager_cls`](lora_manager.md#TPUWorkerLoRAManager._manager_cls)

### <a id="TPUWorkerLoRAManager"></a>`TPUWorkerLoRAManager`
- def: [`src/vllm_torchtpu/lora/lora_manager.py:301`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L301)
- doc: Worker LoRA manager that uses TPULoRAModelManager.
- signature: `class TPUWorkerLoRAManager(LRUCacheWorkerLoRAManager):`
- members:
  - <a id="TPUWorkerLoRAManager._load_adapter"></a>`_load_adapter(self, lora_request: LoRARequest)` — [`L327`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L327) — Loads the adapter and rejects it if any LoRA weight is NaN or Inf.
  - <a id="TPUWorkerLoRAManager.precompile_activation"></a>`precompile_activation(self)` — [`L356`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L356)
  - <a id="TPUWorkerLoRAManager.slot_write_hbm_bytes"></a>`slot_write_hbm_bytes(self)` — [`L361`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L361)
  - <a id="TPUWorkerLoRAManager.max_num_batched_tokens"></a>`max_num_batched_tokens` — [`L325`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L325)
- protocol/private: <a id="TPUWorkerLoRAManager.__init__"></a>`__init__`[`L310`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L310), <a id="TPUWorkerLoRAManager._manager_cls"></a>`_manager_cls`[`L308`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L308)
- uses (calls/refs, reference-scoped): [`slot_write_hbm_bytes`](lora_manager.md#TPULoRAModelManager.slot_write_hbm_bytes), [`precompile_activation`](lora_manager.md#TPULoRAModelManager.precompile_activation), [`TPULoRAModelManager`](lora_manager.md#TPULoRAModelManager)
- used by: [`capture_model`](../runner/tpu_runner.md#TPUModelRunner.capture_model), [`lora_manager`](../runner/tpu_runner.md#TPUModelRunner.lora_manager), [`lora_slot_write_hbm_bytes`](../runner/tpu_runner.md#TPUModelRunner.lora_slot_write_hbm_bytes)

### <a id="_AdapterSlotWriter"></a>`_AdapterSlotWriter`
- def: [`src/vllm_torchtpu/lora/lora_manager.py:95`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L95)
- doc: Loads an adapter into one slot of every stacked LoRA tensor at once.
- signature: `class _AdapterSlotWriter:`
- members:
  - <a id="_AdapterSlotWriter._host_views"></a>`_host_views(self)` — [`L183`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L183) — Makes the CPU views that set_lora writes into, one per tensor in
  - <a id="_AdapterSlotWriter.create"></a>`create(cls, modules: list[BaseLayerWithLoRA], max_loras: int, device: torch.device)` — [`L105`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L105) — Returns None, after a warning, when the writes cannot be staged.
  - <a id="_AdapterSlotWriter.precompile"></a>`precompile(self)` — [`L224`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L224)
  - <a id="_AdapterSlotWriter.redirect_writes_to_host"></a>`redirect_writes_to_host(self)` — [`L204`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L204)
  - <a id="_AdapterSlotWriter.slot_bytes"></a>`slot_bytes(self)` — [`L229`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L229) — Size of one adapter slot, which write_slot holds on the TPU while
  - <a id="_AdapterSlotWriter.write_slot"></a>`write_slot(self, slot: int)` — [`L216`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L216)
- protocol/private: <a id="_AdapterSlotWriter.__init__"></a>`__init__`[`L137`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L137), <a id="_AdapterSlotWriter._device"></a>`_device`[`L164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L164), <a id="_AdapterSlotWriter._device_weights"></a>`_device_weights`[`L168`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L168), <a id="_AdapterSlotWriter._host_slot_weights"></a>`_host_slot_weights`[`L153`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L153), <a id="_AdapterSlotWriter._host_weights"></a>`_host_weights`[`L175`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L175), <a id="_AdapterSlotWriter._modules"></a>`_modules`[`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L144), <a id="_AdapterSlotWriter._slot_indices"></a>`_slot_indices`[`L160`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L160), <a id="_AdapterSlotWriter._stacked_weights"></a>`_stacked_weights`[`L148`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L148)
- uses (calls/refs, reference-scoped): [`_warn_fallback`](lora_manager.md#_warn_fallback), [`_stacked_weights`](lora_manager.md#_stacked_weights), [`write_adapter_to_slot`](../layers/adapter/custom_ops/lora_slot_update_op.md#write_adapter_to_slot), [`_host_weights_like`](lora_manager.md#_host_weights_like), [`_SUPPORTED_LAYERS`](lora_manager.md#_SUPPORTED_LAYERS)
- used by: [`_slot_writer`](lora_manager.md#TPULoRAModelManager._slot_writer), [`slot_write_hbm_bytes`](lora_manager.md#TPULoRAModelManager.slot_write_hbm_bytes), [`activate_adapter`](lora_manager.md#TPULoRAModelManager.activate_adapter), [`precompile_activation`](lora_manager.md#TPULoRAModelManager.precompile_activation)

## Functions
- <a id="_as_tuple"></a>`_as_tuple(weights: torch.Tensor | tuple[torch.Tensor, ...])` — [`L60`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L60)
- <a id="_host_weights_like"></a>`_host_weights_like(device_weights: torch.Tensor | tuple[torch.Tensor, ...], host_views: Iterator[torch.Tensor])` — [`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L75) — Takes the next host views, grouped like device_weights (a tuple or one
- <a id="_stacked_weights"></a>`_stacked_weights(modules: list[BaseLayerWithLoRA])` — [`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L66)
- <a id="_warn_fallback"></a>`_warn_fallback(reason: str)` — [`L86`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L86) — Warns once that adapters keep vLLM's slice-by-slice writes.

## Module values
- <a id="_SUPPORTED_LAYERS"></a>`_SUPPORTED_LAYERS` — [`L47`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L47)
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/lora/lora_manager.py#L43)

