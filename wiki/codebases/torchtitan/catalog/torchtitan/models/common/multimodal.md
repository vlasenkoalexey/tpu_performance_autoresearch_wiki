---
title: 'Module: torchtitan/models/common/multimodal.py'
type: catalog
provenance: extracted
module: torchtitan/models/common/multimodal.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.common.multimodal`/
symbols:
  get_vision_positions: get_vision_positions().
  scatter_vision_embeds: scatter_vision_embeds().
  gather_vision_embeds: gather_vision_embeds().
  build_vision_bank_indices: build_vision_bank_indices().
---
# Module: [`torchtitan/models/common/multimodal.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/multimodal.py)

## Functions
- <a id="build_vision_bank_indices"></a>`build_vision_bank_indices(tokens_T: torch.Tensor, *, placeholder_id: int)` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/multimodal.py#L82) — Map vision placeholder tokens to absolute packed-bank rows.
- <a id="gather_vision_embeds"></a>`gather_vision_embeds(inputs_TD: torch.Tensor, *, vision_bank_VD: torch.Tensor, vision_bank_indices_T: torch.Tensor)` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/multimodal.py#L93) — Gather packed vision features into their placeholder token positions.
- <a id="get_vision_positions"></a>`get_vision_positions(tokens: torch.Tensor, num_vision_tokens_per_item: torch.Tensor, placeholder_id: int)` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/multimodal.py#L21) — Locate each visual item's placeholder run in the token sequence.
- <a id="scatter_vision_embeds"></a>`scatter_vision_embeds(inputs_embeds: torch.Tensor, *, vision_embeds: torch.Tensor, vision_positions: list[tuple[int, int, int]])` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/models/common/multimodal.py#L115) — Copy packed vision features into the text sequence at placeholder runs.

