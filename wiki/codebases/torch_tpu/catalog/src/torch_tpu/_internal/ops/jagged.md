---
title: 'Module: src/torch_tpu/_internal/ops/jagged.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/ops/jagged.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.ops.jagged`/
symbols:
  align_jagged_to_multiple: align_jagged_to_multiple().
  strip_jagged_padding: strip_jagged_padding().
  __all__: __all__.
---
# Module: [`src/torch_tpu/_internal/ops/jagged.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/jagged.py)

## Functions
- <a id="align_jagged_to_multiple"></a>`align_jagged_to_multiple(nt: torch.Tensor, multiple: int = 128, padding_value: typing.Union[float, int, bool] = 0)` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/jagged.py#L62) — Pads a jagged tensor's flat values buffer to a multiple of `multiple`.
- <a id="strip_jagged_padding"></a>`strip_jagged_padding(nt: torch.Tensor, valid_tokens: typing.Optional[int] = None)` — [`L105`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/jagged.py#L105) — Removes trailing padding rows from a padded jagged values buffer.

## Module values
- <a id="__all__"></a>`__all__` — [`L53`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/ops/jagged.py#L53)

