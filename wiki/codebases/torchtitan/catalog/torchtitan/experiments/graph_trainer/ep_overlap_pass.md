---
title: 'Module: torchtitan/experiments/graph_trainer/ep_overlap_pass.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/ep_overlap_pass.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.ep_overlap_pass`/
symbols:
  _build_region_phases: _build_region_phases().
  _plan_region: _plan_region().
  _split_token_count_sync_closure: _split_token_count_sync_closure().
  _collect_token_exchanges: _collect_token_exchanges().
  _schedule_ep_overlap_regions: _schedule_ep_overlap_regions().
  _body_deps: _body_deps().
  _marker_closure.visit: _marker_closure().visit().
  _apply_schedule: _apply_schedule().
  _validate_token_count_sync_copies: _validate_token_count_sync_copies().
  _ready_nodes: _ready_nodes().
  _same_region_owner: _same_region_owner().
  _build_region_phases.append_pending: _build_region_phases().append_pending().
  _is_token_exchange_launch: _is_token_exchange_launch().
  _hidden_body_deps: _hidden_body_deps().
  _append_ready_blocks: _append_ready_blocks().
  _exchange_labels: _exchange_labels().
  _ep_label: _ep_label().
  _body_ancestors: _body_ancestors().
  _marker_closure: _marker_closure().
  _phase_order_deps: _phase_order_deps().
  _TokenExchange: _TokenExchange#
  _ScheduledRegion: _ScheduledRegion#
  _is_token_count_sync_copy: _is_token_count_sync_copy().
  ep_overlap_schedule_pass: ep_overlap_schedule_pass().
  _ScheduledRegion.region: _ScheduledRegion#region.
  _exchange_signature: _exchange_signature().
  _custom_meta: _custom_meta().
  _validate_exchange_labels: _validate_exchange_labels().
  ep_overlap_validate_pass: ep_overlap_validate_pass().
  _build_region_phases.rewrite_sync_copies: _build_region_phases().rewrite_sync_copies().
  _TokenExchange.launch: _TokenExchange#launch.
  _ScheduledRegion.phases: _ScheduledRegion#phases.
  _SyncClosureParts.copies: _SyncClosureParts#copies.
  _is_c10d_functional_node: _is_c10d_functional_node().
  _is_wait_for_token_exchange: _is_wait_for_token_exchange().
  _SyncClosureParts: _SyncClosureParts#
  _SyncClosureParts.pre_copy: _SyncClosureParts#pre_copy.
  _SyncClosureParts.post_copy: _SyncClosureParts#post_copy.
  _SyncClosureParts.launches: _SyncClosureParts#launches.
  _GRAPH_BOUNDARY_OPS: _GRAPH_BOUNDARY_OPS.
  _EP_PHASES: _EP_PHASES.
  _TokenExchange.label: _TokenExchange#label.
  _phase_order_deps.add_dep: _phase_order_deps().add_dep().
  _is_cpu_destination_copy: _is_cpu_destination_copy().
  _set_copy_non_blocking: _set_copy_non_blocking().
  _build_region_phases.future_candidates: _build_region_phases().future_candidates().
---
# Module: [`torchtitan/experiments/graph_trainer/ep_overlap_pass.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py)

## Classes
### <a id="_ScheduledRegion"></a>`_ScheduledRegion`
- def: [`torchtitan/experiments/graph_trainer/ep_overlap_pass.py:95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L95)
- signature: `class _ScheduledRegion:`
- members:
  - <a id="_ScheduledRegion.phases"></a>`phases` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L97)
  - <a id="_ScheduledRegion.region"></a>`region` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L96)
- uses (calls/refs, reference-scoped): [`ChunkedRegion`](ep_pass_utils.md#ChunkedRegion)
- used by: [`_plan_region`](ep_overlap_pass.md#_plan_region), [`_apply_schedule`](ep_overlap_pass.md#_apply_schedule), [`_phase_order_deps`](ep_overlap_pass.md#_phase_order_deps)  (1 test-only)

### <a id="_SyncClosureParts"></a>`_SyncClosureParts`
- def: [`torchtitan/experiments/graph_trainer/ep_overlap_pass.py:101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L101)
- signature: `class _SyncClosureParts:`
- members:
  - <a id="_SyncClosureParts.copies"></a>`copies` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L103)
  - <a id="_SyncClosureParts.launches"></a>`launches` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L105)
  - <a id="_SyncClosureParts.post_copy"></a>`post_copy` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L104)
  - <a id="_SyncClosureParts.pre_copy"></a>`pre_copy` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L102)
- used by: [`_build_region_phases`](ep_overlap_pass.md#_build_region_phases), [`_split_token_count_sync_closure`](ep_overlap_pass.md#_split_token_count_sync_closure)

### <a id="_TokenExchange"></a>`_TokenExchange`
- def: [`torchtitan/experiments/graph_trainer/ep_overlap_pass.py:89`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L89)
- signature: `class _TokenExchange:`
- members:
  - <a id="_TokenExchange.label"></a>`label` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L90)
  - <a id="_TokenExchange.launch"></a>`launch` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L91)
- used by: [`_build_region_phases`](ep_overlap_pass.md#_build_region_phases), [`_collect_token_exchanges`](ep_overlap_pass.md#_collect_token_exchanges), [`_exchange_labels`](ep_overlap_pass.md#_exchange_labels), [`_exchange_signature`](ep_overlap_pass.md#_exchange_signature), [`_validate_exchange_labels`](ep_overlap_pass.md#_validate_exchange_labels)

## Functions
- <a id="_append_ready_blocks"></a>`_append_ready_blocks(blocks: list[tuple[fx.Node, ...]], emitted: set[fx.Node], *, candidates_by_chunk: dict[int, set[fx.Node]], region: ChunkedRegion, chunk_order: tuple[int, ...], order: dict[fx.Node, int], owner_by_node: dict[fx.Node, ChunkOwner], include_waits: bool)` — [`L542`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L542) — Append ready filler/tail blocks until the candidate frontier stalls.
- <a id="_apply_schedule"></a>`_apply_schedule(gm: fx.GraphModule, scheduled_regions: list[_ScheduledRegion])` — [`L883`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L883) — Step 5: apply scheduled order, lint, recompile, and validate phases.
- <a id="_body_ancestors"></a>`_body_ancestors(nodes: tuple[fx.Node, ...], *, body: ChunkBody, owner_by_node: dict[fx.Node, ChunkOwner], node_set: set[fx.Node])` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L332) — Return same-body ancestors needed before the requested body nodes.
- <a id="_body_deps"></a>`_body_deps(node: fx.Node, *, body: ChunkBody, owner_by_node: dict[fx.Node, ChunkOwner])` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L303) — Return same-region body deps, including deps behind unowned plumbing.
- <a id="_build_region_phases"></a>`_build_region_phases(*, region: ChunkedRegion, exchanges_by_chunk: dict[int, tuple[_TokenExchange, ...]], order: dict[fx.Node, int], owner_by_node: dict[fx.Node, ChunkOwner], pair_first_token_exchange: bool, rewrite_token_count_sync_copies: bool)` — [`L576`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L576) — Step 4: construct wait-gated phases for one scheduled region.
- <a id="_collect_token_exchanges"></a>`_collect_token_exchanges(body: ChunkBody, *, order: dict[fx.Node, int])` — [`L193`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L193) — Step 2: collect true token-exchange launches for one chunk body.
- <a id="_custom_meta"></a>`_custom_meta(node: fx.Node)` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L108) — Return mutable custom metadata when present, otherwise an empty dict.
- <a id="_ep_label"></a>`_ep_label(node: fx.Node)` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L114) — Return the optional EP phase label for logs/wait metadata.
- <a id="_exchange_labels"></a>`_exchange_labels(exchanges: tuple[_TokenExchange, ...])` — [`L252`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L252) — Return optional marker labels for diagnostics.
- <a id="_exchange_signature"></a>`_exchange_signature(exchanges: tuple[_TokenExchange, ...])` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L247) — Return the semantic marker sequence used to match chunk pairs.
- <a id="_hidden_body_deps"></a>`_hidden_body_deps(node: fx.Node, *, owner_by_node: dict[fx.Node, ChunkOwner], root_fqn: str, is_backward: bool)` — [`L274`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L274) — Find same-region body deps behind unowned graph plumbing.
- <a id="_is_c10d_functional_node"></a>`_is_c10d_functional_node(node: fx.Node)` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L136) — Return whether a node is a distributed functional op.
- <a id="_is_cpu_destination_copy"></a>`_is_cpu_destination_copy(node: fx.Node)` — [`L149`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L149)
- <a id="_is_token_count_sync_copy"></a>`_is_token_count_sync_copy(node: fx.Node)` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L141)
- <a id="_is_token_exchange_launch"></a>`_is_token_exchange_launch(node: fx.Node)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L120) — Return whether a node is a token-exchange scheduling marker.
- <a id="_is_wait_for_token_exchange"></a>`_is_wait_for_token_exchange(node: fx.Node, node_set: set[fx.Node])` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L183)
- <a id="_marker_closure"></a>`_marker_closure(launch: fx.Node, *, body: ChunkBody, order: dict[fx.Node, int], owner_by_node: dict[fx.Node, ChunkOwner], exchange_index: int, exchange_indices: dict[fx.Node, int])` — [`L428`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L428) — Return the body nodes required to launch one token exchange.
- <a id="_phase_order_deps"></a>`_phase_order_deps(scheduled_regions: list[_ScheduledRegion])` — [`L857`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L857) — Return extra ordering deps that preserve each region's phase schedule.
- <a id="_plan_region"></a>`_plan_region(region: ChunkedRegion, *, order: dict[fx.Node, int], owner_by_node: dict[fx.Node, ChunkOwner], pair_first_token_exchange: bool, rewrite_token_count_sync_copies: bool)` — [`L788`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L788) — Steps 2-4: validate one chunked region and build its schedule phases.
- <a id="_ready_nodes"></a>`_ready_nodes(*, candidates_by_chunk: dict[int, set[fx.Node]], emitted: set[fx.Node], region: ChunkedRegion, chunk_order: tuple[int, ...], order: dict[fx.Node, int], owner_by_node: dict[fx.Node, ChunkOwner], include_waits: bool)` — [`L511`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L511) — Return currently schedulable body nodes from candidate filler sets.
- <a id="_same_region_owner"></a>`_same_region_owner(node: fx.Node, *, owner_by_node: dict[fx.Node, ChunkOwner], root_fqn: str, is_backward: bool)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L165) — Return chunk ownership only when it belongs to the same selected region.
- <a id="_schedule_ep_overlap_regions"></a>`_schedule_ep_overlap_regions(gm: fx.GraphModule, *, module_pattern: str, require_all_to_all: bool, reorder: bool = True, pair_first_token_exchange: bool = False)` — [`L908`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L908) — Run validation or scheduling for all chunked regions matching a pattern.
- <a id="_set_copy_non_blocking"></a>`_set_copy_non_blocking(node: fx.Node, non_blocking: bool)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L159)
- <a id="_split_token_count_sync_closure"></a>`_split_token_count_sync_closure(closure: tuple[fx.Node, ...], *, body: ChunkBody, launch_nodes: set[fx.Node], owner_by_node: dict[fx.Node, ChunkOwner])` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L360) — Split the first token-exchange closure around sync D2H copy launches.
- <a id="_validate_exchange_labels"></a>`_validate_exchange_labels(root: str, direction: str, exchanges_by_chunk: dict[int, tuple[_TokenExchange, ...]])` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L257)
- <a id="_validate_token_count_sync_copies"></a>`_validate_token_count_sync_copies(body: ChunkBody, *, first_closure: tuple[fx.Node, ...])` — [`L407`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L407)
- <a id="_phase_order_deps.add_dep"></a>`add_dep(node: fx.Node, dep: fx.Node)` — [`L863`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L863)
- <a id="_build_region_phases.append_pending"></a>`append_pending(nodes: tuple[fx.Node, ...])` — [`L637`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L637)
- <a id="ep_overlap_schedule_pass"></a>`ep_overlap_schedule_pass(gm: fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, module_pattern: str, require_all_to_all: bool = True, pair_first_token_exchange: bool = False)` — [`L981`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L981) — Reorder already chunked regions around EP all-to-alls.
- <a id="ep_overlap_validate_pass"></a>`ep_overlap_validate_pass(gm: fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, module_pattern: str, require_all_to_all: bool = False, pair_first_token_exchange: bool = False)` — [`L956`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L956) — Validate the already chunked graph without changing node order.
- <a id="_build_region_phases.future_candidates"></a>`future_candidates(exchange_idx: int)` — [`L622`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L622)
- <a id="_build_region_phases.rewrite_sync_copies"></a>`rewrite_sync_copies(copies: tuple[fx.Node, ...])` — [`L643`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L643)
- <a id="_marker_closure.visit"></a>`visit(node: fx.Node, *, allow_peer_chunk: bool = False)` — [`L442`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L442)

## Module values
- <a id="_EP_PHASES"></a>`_EP_PHASES` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L82)
- <a id="_GRAPH_BOUNDARY_OPS"></a>`_GRAPH_BOUNDARY_OPS` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_overlap_pass.py#L81)

