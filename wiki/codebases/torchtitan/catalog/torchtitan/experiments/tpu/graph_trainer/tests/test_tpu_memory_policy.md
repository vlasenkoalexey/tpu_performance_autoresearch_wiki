---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.tests.test_tpu_memory_policy`/
symbols:
  _router: _router().
  TestTpuSelectivePolicy._run: TestTpuSelectivePolicy#_run().
  TestSelectSaves.test_last_n_layers_keeps_only_the_last_layers: TestSelectSaves#test_last_n_layers_keeps_only_the_last_layers().
  TestSelectSaves.test_limit_needs_values_inside_the_layers: TestSelectSaves#test_limit_needs_values_inside_the_layers().
  TestTpuSelectivePolicy.tag: TestTpuSelectivePolicy#tag().
  _trace_toy: _trace_toy().
  _trace_simple_fsdp_graph: _trace_simple_fsdp_graph().
  TestTpuSelectivePolicy.test_saves_routing_and_every_splash_by_default: TestTpuSelectivePolicy#test_saves_routing_and_every_splash_by_default().
  TestRoutingRegion.test_selects_the_marked_sort_in_every_layer: TestRoutingRegion#test_selects_the_marked_sort_in_every_layer().
  TestRoutingRegion.test_selects_the_last_topk_of_each_router: TestRoutingRegion#test_selects_the_last_topk_of_each_router().
  TestRoutingRegion.test_selects_top_k_ids_and_permutation_of_every_moe_layer: TestRoutingRegion#test_selects_top_k_ids_and_permutation_of_every_moe_layer().
  TestSplashAttentionRegion.test_selects_both_layouts_once_per_layer: TestSplashAttentionRegion#test_selects_both_layouts_once_per_layer().
  _register_splash_like_op: _register_splash_like_op().
  _splash_cores: _splash_cores().
  _MoE.forward: _MoE#forward().
  TestSelectSaves.test_region_without_candidates_raises: TestSelectSaves#test_region_without_candidates_raises().
  TestTpuSelectivePolicy.test_saves_routing_in_every_layer: TestTpuSelectivePolicy#test_saves_routing_in_every_layer().
  TestTpuSelectivePolicy.test_last_n_layers_saves_only_the_last_splash: TestTpuSelectivePolicy#test_last_n_layers_saves_only_the_last_splash().
  _MoEToy: _MoEToy#
  TestFullRematWithSaves.test_zero2_keeps_all_gather_outputs_saved: TestFullRematWithSaves#test_zero2_keeps_all_gather_outputs_saved().
  TestSelectSaves.test_config_values_are_checked: TestSelectSaves#test_config_values_are_checked().
  TestTpuSelectivePolicy.test_selective_and_offload_keeps_saves_in_hbm: TestTpuSelectivePolicy#test_selective_and_offload_keeps_saves_in_hbm().
  TestTpuSelectivePolicy.test_saved_routing_skips_the_router_topk_recompute: TestTpuSelectivePolicy#test_saved_routing_skips_the_router_topk_recompute().
  _SplashCore.__call__: _SplashCore#__call__().
  _hand_built_routing_graph: _hand_built_routing_graph().
  _MoEToy.layers: _MoEToy#layers.
  _register_splash_like_op.forward: _register_splash_like_op().forward().
  _is_splash_node: _is_splash_node().
  _Attention.forward: _Attention#forward().
  _Block.forward: _Block#forward().
  TestRoutingRegion.test_needs_both_in_the_same_layers: TestRoutingRegion#test_needs_both_in_the_same_layers().
  _STOCK_STYLE_SPLASH: _STOCK_STYLE_SPLASH.
  _selective_config: _selective_config().
  _TOP_K: _TOP_K.
  _register_splash_like_op.backward: _register_splash_like_op().backward().
  _MODEL_LAYOUT_SPLASH: _MODEL_LAYOUT_SPLASH.
  _DenseToy.layers: _DenseToy#layers.
  _MoE.router: _MoE#router.
  _Block.attention: _Block#attention.
  _Block.moe: _Block#moe.
  _trace_toy.step: _trace_toy().step().
  _trace_simple_fsdp_graph.step: _trace_simple_fsdp_graph().step().
  _router_topks: _router_topks().
  _DIM: _DIM.
  _SplashCore: _SplashCore#
  _DenseToy: _DenseToy#
  _ROUTING_SPLASH: _ROUTING_SPLASH.
  _DenseBlock.forward: _DenseBlock#forward().
  _DenseToy.forward: _DenseToy#forward().
  _MoEToy.forward: _MoEToy#forward().
  TestRoutingRegion.test_unexpected_router_topk_raises: TestRoutingRegion#test_unexpected_router_topk_raises().
  TestSplashAttentionRegion.test_matches_stock_and_tokamax_forward_ops_only: TestSplashAttentionRegion#test_matches_stock_and_tokamax_forward_ops_only().
  TestSplashAttentionRegion.test_unexpected_splash_outputs_raise: TestSplashAttentionRegion#test_unexpected_splash_outputs_raise().
  _TOKENS: _TOKENS.
  _EXPERTS: _EXPERTS.
  _HEADS: _HEADS.
  _parallelism: _parallelism().
  _register_splash_like_op.lse_of: _register_splash_like_op().lse_of().
  _register_splash_like_op.backward_op: _register_splash_like_op().backward_op().
  _SplashCore.model_layout: _SplashCore#model_layout.
  _Attention.core: _Attention#core.
  TestTpuSelectivePolicy.offloaded: TestTpuSelectivePolicy#offloaded().
  _register_splash_like_op.setup_context: _register_splash_like_op().setup_context().
  _SplashCore.op: _SplashCore#op.
  _DenseBlock: _DenseBlock#
  _DenseBlock.weight: _DenseBlock#weight.
  _Attention: _Attention#
  _Attention.weight: _Attention#weight.
  _MoE: _MoE#
  _MoE.expert: _MoE#expert.
  _Block: _Block#
  _SplashCore.__init__: _SplashCore#__init__().
  _DenseBlock.__init__: _DenseBlock#__init__().
  _DenseToy.__init__: _DenseToy#__init__().
  _Attention.__init__: _Attention#__init__().
  _MoE.__init__: _MoE#__init__().
  _Block.__init__: _Block#__init__().
  _MoEToy.__init__: _MoEToy#__init__().
  TestFullRematWithSaves: TestFullRematWithSaves#
  TestRoutingRegion: TestRoutingRegion#
  TestSelectSaves: TestSelectSaves#
  TestTpuSelectivePolicy: TestTpuSelectivePolicy#
  TestSplashAttentionRegion: TestSplashAttentionRegion#
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py)

> **Collapsed catalog** (83 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="TestFullRematWithSaves"></a>`TestFullRematWithSaves` — [`L318`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L318)
- <a id="TestFullRematWithSaves.test_zero2_keeps_all_gather_outputs_saved"></a>`TestFullRematWithSaves.test_zero2_keeps_all_gather_outputs_saved` — [`L319`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L319)
- <a id="TestRoutingRegion"></a>`TestRoutingRegion` — [`L377`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L377)
- <a id="TestRoutingRegion.test_needs_both_in_the_same_layers"></a>`TestRoutingRegion.test_needs_both_in_the_same_layers` — [`L441`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L441)
- <a id="TestRoutingRegion.test_selects_the_last_topk_of_each_router"></a>`TestRoutingRegion.test_selects_the_last_topk_of_each_router` — [`L390`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L390)
- <a id="TestRoutingRegion.test_selects_the_marked_sort_in_every_layer"></a>`TestRoutingRegion.test_selects_the_marked_sort_in_every_layer` — [`L378`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L378)
- <a id="TestRoutingRegion.test_selects_top_k_ids_and_permutation_of_every_moe_layer"></a>`TestRoutingRegion.test_selects_top_k_ids_and_permutation_of_every_moe_layer` — [`L426`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L426)
- <a id="TestRoutingRegion.test_unexpected_router_topk_raises"></a>`TestRoutingRegion.test_unexpected_router_topk_raises` — [`L412`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L412)
- <a id="TestSelectSaves"></a>`TestSelectSaves` — [`L467`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L467)
- <a id="TestSelectSaves.test_config_values_are_checked"></a>`TestSelectSaves.test_config_values_are_checked` — [`L511`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L511)
- <a id="TestSelectSaves.test_last_n_layers_keeps_only_the_last_layers"></a>`TestSelectSaves.test_last_n_layers_keeps_only_the_last_layers` — [`L474`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L474)
- <a id="TestSelectSaves.test_limit_needs_values_inside_the_layers"></a>`TestSelectSaves.test_limit_needs_values_inside_the_layers` — [`L498`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L498)
- <a id="TestSelectSaves.test_region_without_candidates_raises"></a>`TestSelectSaves.test_region_without_candidates_raises` — [`L468`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L468)
- <a id="TestSplashAttentionRegion"></a>`TestSplashAttentionRegion` — [`L713`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L713)
- <a id="TestSplashAttentionRegion.test_matches_stock_and_tokamax_forward_ops_only"></a>`TestSplashAttentionRegion.test_matches_stock_and_tokamax_forward_ops_only` — [`L714`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L714)
- <a id="TestSplashAttentionRegion.test_selects_both_layouts_once_per_layer"></a>`TestSplashAttentionRegion.test_selects_both_layouts_once_per_layer` — [`L730`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L730)
- <a id="TestSplashAttentionRegion.test_unexpected_splash_outputs_raise"></a>`TestSplashAttentionRegion.test_unexpected_splash_outputs_raise` — [`L751`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L751)
- <a id="TestTpuSelectivePolicy"></a>`TestTpuSelectivePolicy` — [`L545`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L545)
- <a id="TestTpuSelectivePolicy._run"></a>`TestTpuSelectivePolicy._run` — [`L546`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L546)
- <a id="TestTpuSelectivePolicy.offloaded"></a>`TestTpuSelectivePolicy.offloaded` — [`L657`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L657)
- <a id="TestTpuSelectivePolicy.tag"></a>`TestTpuSelectivePolicy.tag` — [`L645`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L645)
- <a id="TestTpuSelectivePolicy.test_last_n_layers_saves_only_the_last_splash"></a>`TestTpuSelectivePolicy.test_last_n_layers_saves_only_the_last_splash` — [`L630`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L630)
- <a id="TestTpuSelectivePolicy.test_saved_routing_skips_the_router_topk_recompute"></a>`TestTpuSelectivePolicy.test_saved_routing_skips_the_router_topk_recompute` — [`L678`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L678)
- <a id="TestTpuSelectivePolicy.test_saves_routing_and_every_splash_by_default"></a>`TestTpuSelectivePolicy.test_saves_routing_and_every_splash_by_default` — [`L616`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L616)
- <a id="TestTpuSelectivePolicy.test_saves_routing_in_every_layer"></a>`TestTpuSelectivePolicy.test_saves_routing_in_every_layer` — [`L601`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L601)
- <a id="TestTpuSelectivePolicy.test_selective_and_offload_keeps_saves_in_hbm"></a>`TestTpuSelectivePolicy.test_selective_and_offload_keeps_saves_in_hbm` — [`L644`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L644)
- <a id="_Attention"></a>`_Attention` — [`L195`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L195)
- <a id="_Attention.__init__"></a>`_Attention.__init__` — [`L198`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L198)
- <a id="_Attention.core"></a>`_Attention.core` — [`L201`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L201)
- <a id="_Attention.forward"></a>`_Attention.forward` — [`L203`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L203)
- <a id="_Attention.weight"></a>`_Attention.weight` — [`L200`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L200)
- <a id="_Block"></a>`_Block` — [`L242`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L242)
- <a id="_Block.__init__"></a>`_Block.__init__` — [`L243`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L243)
- <a id="_Block.attention"></a>`_Block.attention` — [`L245`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L245)
- <a id="_Block.forward"></a>`_Block.forward` — [`L248`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L248)
- <a id="_Block.moe"></a>`_Block.moe` — [`L246`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L246)
- <a id="_DIM"></a>`_DIM` — [`L74`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L74)
- <a id="_DenseBlock"></a>`_DenseBlock` — [`L175`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L175)
- <a id="_DenseBlock.__init__"></a>`_DenseBlock.__init__` — [`L176`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L176)
- <a id="_DenseBlock.forward"></a>`_DenseBlock.forward` — [`L180`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L180)
- <a id="_DenseBlock.weight"></a>`_DenseBlock.weight` — [`L178`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L178)
- <a id="_DenseToy"></a>`_DenseToy` — [`L184`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L184)
- <a id="_DenseToy.__init__"></a>`_DenseToy.__init__` — [`L185`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L185)
- <a id="_DenseToy.forward"></a>`_DenseToy.forward` — [`L189`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L189)
- <a id="_DenseToy.layers"></a>`_DenseToy.layers` — [`L187`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L187)
- <a id="_EXPERTS"></a>`_EXPERTS` — [`L75`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L75)
- <a id="_HEADS"></a>`_HEADS` — [`L77`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L77)
- <a id="_MODEL_LAYOUT_SPLASH"></a>`_MODEL_LAYOUT_SPLASH` — [`L143`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L143)
- <a id="_MoE"></a>`_MoE` — [`L224`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L224)
- <a id="_MoE.__init__"></a>`_MoE.__init__` — [`L227`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L227)
- <a id="_MoE.expert"></a>`_MoE.expert` — [`L230`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L230)
- <a id="_MoE.forward"></a>`_MoE.forward` — [`L232`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L232)
- <a id="_MoE.router"></a>`_MoE.router` — [`L229`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L229)
- <a id="_MoEToy"></a>`_MoEToy` — [`L253`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L253)
- <a id="_MoEToy.__init__"></a>`_MoEToy.__init__` — [`L254`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L254)
- <a id="_MoEToy.forward"></a>`_MoEToy.forward` — [`L262`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L262)
- <a id="_MoEToy.layers"></a>`_MoEToy.layers` — [`L258`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L258)
- <a id="_ROUTING_SPLASH"></a>`_ROUTING_SPLASH` — [`L464`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L464)
- <a id="_STOCK_STYLE_SPLASH"></a>`_STOCK_STYLE_SPLASH` — [`L139`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L139)
- <a id="_SplashCore"></a>`_SplashCore` — [`L148`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L148)
- <a id="_SplashCore.__call__"></a>`_SplashCore.__call__` — [`L155`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L155)
- <a id="_SplashCore.__init__"></a>`_SplashCore.__init__` — [`L151`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L151)
- <a id="_SplashCore.model_layout"></a>`_SplashCore.model_layout` — [`L153`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L153)
- <a id="_SplashCore.op"></a>`_SplashCore.op` — [`L152`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L152)
- <a id="_TOKENS"></a>`_TOKENS` — [`L73`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L73)
- <a id="_TOP_K"></a>`_TOP_K` — [`L76`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L76)
- <a id="_hand_built_routing_graph"></a>`_hand_built_routing_graph` — [`L351`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L351)
- <a id="_is_splash_node"></a>`_is_splash_node` — [`L707`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L707)
- <a id="_parallelism"></a>`_parallelism` — [`L80`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L80)
- <a id="_register_splash_like_op"></a>`_register_splash_like_op` — [`L87`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L87)
- <a id="_register_splash_like_op.backward"></a>`_register_splash_like_op.backward` — [`L131`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L131)
- <a id="_register_splash_like_op.backward_op"></a>`_register_splash_like_op.backward_op` — [`L113`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L113)
- <a id="_register_splash_like_op.forward"></a>`_register_splash_like_op.forward` — [`L101`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L101)
- <a id="_register_splash_like_op.lse_of"></a>`_register_splash_like_op.lse_of` — [`L96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L96)
- <a id="_register_splash_like_op.setup_context"></a>`_register_splash_like_op.setup_context` — [`L128`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L128)
- <a id="_router"></a>`_router` — [`L208`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L208)
- <a id="_router_topks"></a>`_router_topks` — [`L341`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L341)
- <a id="_selective_config"></a>`_selective_config` — [`L451`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L451)
- <a id="_splash_cores"></a>`_splash_cores` — [`L166`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L166)
- <a id="_trace_simple_fsdp_graph"></a>`_trace_simple_fsdp_graph` — [`L290`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L290)
- <a id="_trace_simple_fsdp_graph.step"></a>`_trace_simple_fsdp_graph.step` — [`L307`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L307)
- <a id="_trace_toy"></a>`_trace_toy` — [`L268`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L268)
- <a id="_trace_toy.step"></a>`_trace_toy.step` — [`L272`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/tests/test_tpu_memory_policy.py#L272)
