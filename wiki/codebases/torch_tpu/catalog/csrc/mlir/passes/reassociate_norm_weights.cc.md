---
title: 'Module: csrc/mlir/passes/reassociate_norm_weights.cc'
type: catalog
provenance: extracted
module: csrc/mlir/passes/reassociate_norm_weights.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ReassociateMulNormPattern.matchAndRewrite: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateMulNormPattern#matchAndRewrite(e8e02ba4aec83c2).'
  createReassociateNormWeightsPass: createReassociateNormWeightsPass(96f104e05217d2a1).
  MatchOnePlusWeight: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/MatchOnePlusWeight(41e9a9ba022c0255).'
  ReassociateNormWeightsPass: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateNormWeightsPass#'
  IsOneSplat: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/IsOneSplat(f58fb72033f448).'
  MatchedWeight: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/MatchedWeight#'
  MatchedWeight.outer_bcast: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/MatchedWeight#outer_bcast.'
  ReassociateNormWeightsPass.runOnOperation: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateNormWeightsPass#runOnOperation(49f6e7a06ebc5aa8).'
  SkipBroadcasts: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/SkipBroadcasts(75560ca0f84a2ecc).'
  MatchedWeight.raw_weight: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/MatchedWeight#raw_weight.'
  ReassociateMulNormPattern: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateMulNormPattern#'
  ReassociateNormWeightsPass.resolveTypeID: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateNormWeightsPass#resolveTypeID(1920234c947e2cee).'
  ReassociateMulNormPattern.ReassociateMulNormPattern: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateMulNormPattern#ReassociateMulNormPattern(2d3010b6863deec4).'
  ReassociateNormWeightsPass.getArgument: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateNormWeightsPass#getArgument(b9baacb27e9a3fdd).'
  ReassociateNormWeightsPass.getDescription: '`$anonymous_namespace_csrc/mlir/passes/reassociate_norm_weights.cc`/ReassociateNormWeightsPass#getDescription(b9baacb27e9a3fdd).'
---
# Module: [`csrc/mlir/passes/reassociate_norm_weights.cc`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc)

## Classes
### <a id="MatchedWeight"></a>`MatchedWeight`
- def: [`csrc/mlir/passes/reassociate_norm_weights.cc:70`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L70) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- signature: `struct MatchedWeight`
- members:
  - <a id="MatchedWeight.outer_bcast"></a>`outer_bcast` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L72) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
  - <a id="MatchedWeight.raw_weight"></a>`raw_weight` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L71) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`matchAndRewrite`](reassociate_norm_weights.cc.md#ReassociateMulNormPattern.matchAndRewrite), [`MatchOnePlusWeight`](reassociate_norm_weights.cc.md#MatchOnePlusWeight)

### <a id="ReassociateMulNormPattern"></a>`ReassociateMulNormPattern`  ·  implements/extends OpOrInterfaceRewritePatternBase, OpRewritePattern, Pattern, RewritePattern
- def: [`csrc/mlir/passes/reassociate_norm_weights.cc:104`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L104) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- doc: Rewrites:
- signature: `struct ReassociateMulNormPattern : public mlir::OpRewritePattern<mlir::stablehlo::MulOp>`
- members:
  - <a id="ReassociateMulNormPattern.ReassociateMulNormPattern"></a>`ReassociateMulNormPattern` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L106)
  - `ReassociateMulNormPattern` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L106)
  - `ReassociateMulNormPattern` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L106)
  - <a id="ReassociateMulNormPattern.matchAndRewrite"></a>`matchAndRewrite(mlir::stablehlo::MulOp mul_op, mlir::PatternRewriter& rewriter)` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L108) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
  - `matchAndRewrite(mlir::stablehlo::MulOp mul_op, mlir::PatternRewriter& rewriter)` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L108)
- uses (calls/refs, reference-scoped): [`MatchOnePlusWeight`](reassociate_norm_weights.cc.md#MatchOnePlusWeight), [`MatchedWeight`](reassociate_norm_weights.cc.md#MatchedWeight), [`outer_bcast`](reassociate_norm_weights.cc.md#MatchedWeight.outer_bcast), [`SkipBroadcasts`](reassociate_norm_weights.cc.md#SkipBroadcasts), [`raw_weight`](reassociate_norm_weights.cc.md#MatchedWeight.raw_weight)
- used by: [`runOnOperation`](reassociate_norm_weights.cc.md#ReassociateNormWeightsPass.runOnOperation)

### <a id="ReassociateNormWeightsPass"></a>`ReassociateNormWeightsPass`  ·  implements/extends OperationPass, Pass, PassWrapper
- def: [`csrc/mlir/passes/reassociate_norm_weights.cc:159`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L159) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- signature: `struct ReassociateNormWeightsPass : public mlir::PassWrapper<ReassociateNormWeightsPass, mlir::OperationPass<mlir::func::FuncOp>>`
- members:
  - <a id="ReassociateNormWeightsPass.getArgument"></a>`getArgument()` — [`L164`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L164)
  - <a id="ReassociateNormWeightsPass.getDescription"></a>`getDescription()` — [`L167`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L167)
  - <a id="ReassociateNormWeightsPass.resolveTypeID"></a>`resolveTypeID(ReassociateNormWeightsPass)` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L162)
  - <a id="ReassociateNormWeightsPass.runOnOperation"></a>`runOnOperation()` — [`L172`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L172) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- uses (calls/refs, reference-scoped): [`ReassociateMulNormPattern`](reassociate_norm_weights.cc.md#ReassociateMulNormPattern)
- used by: [`createReassociateNormWeightsPass`](reassociate_norm_weights.cc.md#createReassociateNormWeightsPass)

## Functions
- <a id="IsOneSplat"></a>`IsOneSplat(mlir::Value val)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L55) — Checks if a value is a constant 1.0 (float) or 1 (integer) splat. — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- <a id="MatchOnePlusWeight"></a>`MatchOnePlusWeight(mlir::Value val)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L80) — Matches: — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- <a id="SkipBroadcasts"></a>`SkipBroadcasts(mlir::Value v)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L43) — Skips broadcast_in_dim ops to find the underlying value. — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- `createReassociateNormWeightsPass()` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L187)
- <a id="createReassociateNormWeightsPass"></a>`createReassociateNormWeightsPass()` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/reassociate_norm_weights.cc#L187) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)

