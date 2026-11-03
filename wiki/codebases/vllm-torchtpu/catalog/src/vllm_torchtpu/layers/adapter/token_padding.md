---
title: 'Module: src/vllm_torchtpu/layers/adapter/token_padding.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/token_padding.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.token_padding`/
symbols:
  _padding_state._padding_state: _padding_state._padding_state.
  zero_routing_weights_for_padding: zero_routing_weights_for_padding().
  mark_padding: mark_padding().
  TokenPaddingState.get_local_padding_mask: TokenPaddingState#get_local_padding_mask().
  set_padding_state: set_padding_state().
  mask_router_logits_for_padding: mask_router_logits_for_padding().
  TokenPaddingState: TokenPaddingState#
  TokenPaddingState.local_padding_mask: TokenPaddingState#local_padding_mask.
  TokenPaddingState.create: TokenPaddingState#create().
  TokenPaddingState.update: TokenPaddingState#update().
---
# Module: [`src/vllm_torchtpu/layers/adapter/token_padding.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py)

## Classes
### <a id="TokenPaddingState"></a>`TokenPaddingState`
- def: [`src/vllm_torchtpu/layers/adapter/token_padding.py:23`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L23)
- members:
  - <a id="TokenPaddingState.create"></a>`create(cls, max_local_tokens: int, device)` — [`L29`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L29)
  - <a id="TokenPaddingState.get_local_padding_mask"></a>`get_local_padding_mask(self, num_tokens: int)` — [`L42`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L42)
  - <a id="TokenPaddingState.update"></a>`update(self, local_valid_tokens: int, local_padded_tokens: int)` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L35) — Write this rank's token padding mask.
  - <a id="TokenPaddingState.local_padding_mask"></a>`local_padding_mask` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L26)
- used by: [`device`](../../runner/tpu_runner.md#TPUModelRunner.device), [`_padding_state`](token_padding.md#_padding_state._padding_state), [`moe_tp_decode_forward`](moe_tp_decode.md#moe_tp_decode_forward), [`zero_routing_weights_for_padding`](token_padding.md#zero_routing_weights_for_padding), [`mark_padding`](token_padding.md#mark_padding), [`mask_router_logits_for_padding`](token_padding.md#mask_router_logits_for_padding), [`set_padding_state`](token_padding.md#set_padding_state), [`_token_padding_state`](../../runner/tpu_runner.md#TPUModelRunner._token_padding_state)

## Functions
- <a id="mark_padding"></a>`mark_padding(num_valid_tokens: int, num_padded_tokens: int)` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L51) — Describe the rows of the next forward: [num_valid_tokens,
- <a id="mask_router_logits_for_padding"></a>`mask_router_logits_for_padding(router_logits: torch.Tensor)` — [`L112`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L112) — Replace padded rows of local router_logits with NaN.
- <a id="set_padding_state"></a>`set_padding_state(state: TokenPaddingState | None)` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L46)
- <a id="zero_routing_weights_for_padding"></a>`zero_routing_weights_for_padding(topk_ids: torch.Tensor, topk_weights: torch.Tensor, is_local_tensor: bool = False)` — [`L62`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L62) — Set routing weights to 0 for padded tokens.

## Module values
- <a id="_padding_state._padding_state"></a>`_padding_state` — [`L19`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/token_padding.py#L19)

