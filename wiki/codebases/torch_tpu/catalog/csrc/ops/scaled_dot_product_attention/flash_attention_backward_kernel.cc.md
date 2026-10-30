---
title: 'Module: csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc
status: fresh
symbol_base: cxx . . $ mlir/torch_tpu/
symbols:
  buildBackwardDkvModule: buildBackwardDkvModule(7c2a940e2048fc66).
  buildBackwardDqModule: buildBackwardDqModule(7c2a940e2048fc66).
  CreateBackwardDqKernel: CreateBackwardDqKernel(5655a7067ede568e).
  CreateBackwardDkvKernel: CreateBackwardDkvKernel(5655a7067ede568e).
  SetBackwardDkvKernelAttributes: SetBackwardDkvKernelAttributes(e4a09dda2e48a5b3).
  LoadAndCastTiles: LoadAndCastTiles(ab923ab7f3c1a288).
  SetBackwardDqKernelAttributes: SetBackwardDqKernelAttributes(187da6fbabc1540d).
  ComputeSharedBackwardLogic: ComputeSharedBackwardLogic(4586389595507bbb).
  GetBwdArgIndices: GetBwdArgIndices(69d1d8ccd1c689f3).
  LoadedTiles.do_2d: LoadedTiles#do_2d.
  BwdArgIndices.next_idx: BwdArgIndices#next_idx.
  BwdArgIndices: BwdArgIndices#
  ConstantOp: ConstantOp#
  IfOp: IfOp#
  SharedBwdResult.ds_trunc: SharedBwdResult#ds_trunc.
  LoadedTiles: LoadedTiles#
  LoadedTiles.k_tile: LoadedTiles#k_tile.
  LoadedTiles.q_tile: LoadedTiles#q_tile.
  LoadedTiles.lse_tile: LoadedTiles#lse_tile.
  LoadedTiles.v_tile: LoadedTiles#v_tile.
  BwdArgIndices.seed: BwdArgIndices#seed.
  LoadedTiles.mask_tile: LoadedTiles#mask_tile.
  LoadedTiles.di_tile: LoadedTiles#di_tile.
  SubFOp: SubFOp#
  ReturnOp: ReturnOp#
  BroadcastOp: BroadcastOp#
  AndIOp: AndIOp#
  CmpFPredicate: CmpFPredicate#
  SelectOp: SelectOp#
  YieldOp: YieldOp#
  CmpIOp: CmpIOp#
  AddFOp: AddFOp#
  CmpIPredicate: CmpIPredicate#
  MulFOp: MulFOp#
  Exp2Op: Exp2Op#
  CmpFOp: CmpFOp#
  BwdArgIndices.k: BwdArgIndices#k.
  BwdArgIndices.q: BwdArgIndices#q.
  BwdArgIndices.do_arg: BwdArgIndices#do_arg.
  BwdArgIndices.di: BwdArgIndices#di.
  BwdArgIndices.mask: BwdArgIndices#mask.
  BwdArgIndices.v: BwdArgIndices#v.
  BwdArgIndices.lse: BwdArgIndices#lse.
  SharedBwdResult: SharedBwdResult#
  SharedBwdResult.p: SharedBwdResult#p.
  ShapeCastOp: ShapeCastOp#
---
# Module: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc)

## Classes
### <a id="AddFOp"></a>`AddFOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:60`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L60)
- signature: `using mlir::arith::AddFOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="AndIOp"></a>`AndIOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:61`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L61)
- signature: `using mlir::arith::AndIOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="BroadcastOp"></a>`BroadcastOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:74`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L74)
- signature: `using mlir::vector::BroadcastOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="BwdArgIndices"></a>`BwdArgIndices`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:150`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L150)
- signature: `struct BwdArgIndices`
- members:
  - <a id="BwdArgIndices.di"></a>`di` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L157)
  - <a id="BwdArgIndices.do_arg"></a>`do_arg` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L155)
  - <a id="BwdArgIndices.k"></a>`k` — [`L153`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L153)
  - <a id="BwdArgIndices.lse"></a>`lse` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L156)
  - <a id="BwdArgIndices.mask"></a>`mask` — [`L158`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L158)
  - <a id="BwdArgIndices.next_idx"></a>`next_idx` — [`L159`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L159)
  - <a id="BwdArgIndices.q"></a>`q` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L152)
  - <a id="BwdArgIndices.seed"></a>`seed` — [`L151`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L151)
  - <a id="BwdArgIndices.v"></a>`v` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L154)
- used by: [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule), [`LoadAndCastTiles`](flash_attention_backward_kernel.cc.md#LoadAndCastTiles), [`GetBwdArgIndices`](flash_attention_backward_kernel.cc.md#GetBwdArgIndices)

### <a id="CmpFOp"></a>`CmpFOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:62`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L62)
- signature: `using mlir::arith::CmpFOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="CmpFPredicate"></a>`CmpFPredicate`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:63`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L63)
- signature: `using mlir::arith::CmpFPredicate`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="CmpIOp"></a>`CmpIOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:64`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L64)
- signature: `using mlir::arith::CmpIOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="CmpIPredicate"></a>`CmpIPredicate`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:65`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L65)
- signature: `using mlir::arith::CmpIPredicate`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="ConstantOp"></a>`ConstantOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:66`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L66)
- signature: `using mlir::arith::ConstantOp`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`buildModule`](flash_attention_kernel.cc.md#buildModule), [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule)

### <a id="Exp2Op"></a>`Exp2Op`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:71`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L71)
- signature: `using mlir::math::Exp2Op`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="IfOp"></a>`IfOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L72)
- signature: `using mlir::scf::IfOp`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule)

### <a id="LoadedTiles"></a>`LoadedTiles`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:182`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L182)
- signature: `struct LoadedTiles`
- members:
  - <a id="LoadedTiles.di_tile"></a>`di_tile` — [`L184`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L184)
  - <a id="LoadedTiles.do_2d"></a>`do_2d` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L189)
  - <a id="LoadedTiles.k_tile"></a>`k_tile` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L187)
  - <a id="LoadedTiles.lse_tile"></a>`lse_tile` — [`L183`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L183)
  - <a id="LoadedTiles.mask_tile"></a>`mask_tile` — [`L185`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L185)
  - <a id="LoadedTiles.q_tile"></a>`q_tile` — [`L186`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L186)
  - <a id="LoadedTiles.v_tile"></a>`v_tile` — [`L188`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L188)
- used by: [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule), [`LoadAndCastTiles`](flash_attention_backward_kernel.cc.md#LoadAndCastTiles)

### <a id="MulFOp"></a>`MulFOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:67`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L67)
- signature: `using mlir::arith::MulFOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="ReturnOp"></a>`ReturnOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:70`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L70)
- signature: `using mlir::func::ReturnOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="SelectOp"></a>`SelectOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:68`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L68)
- signature: `using mlir::arith::SelectOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="ShapeCastOp"></a>`ShapeCastOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:75`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L75)
- signature: `using mlir::vector::ShapeCastOp`

### <a id="SharedBwdResult"></a>`SharedBwdResult`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:77`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L77)
- signature: `struct SharedBwdResult`
- members:
  - <a id="SharedBwdResult.ds_trunc"></a>`ds_trunc` — [`L79`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L79)
  - <a id="SharedBwdResult.p"></a>`p` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L78)
- used by: [`buildBackwardDkvModule`](flash_attention_backward_kernel.cc.md#buildBackwardDkvModule), [`buildBackwardDqModule`](flash_attention_backward_kernel.cc.md#buildBackwardDqModule)

### <a id="SubFOp"></a>`SubFOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:69`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L69)
- signature: `using mlir::arith::SubFOp`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="YieldOp"></a>`YieldOp`
- def: [`csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc:73`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L73)
- signature: `using mlir::scf::YieldOp`
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="ComputeSharedBackwardLogic"></a>`ComputeSharedBackwardLogic(ImplicitLocOpBuilder& fn_builder, const FlashAttnConfig& config, int64_t qt, int64_t kt, Value q_2d, Value k_2d, Value v_2d, Value do_2d, Value lse_tile, Value di_tile, Value user_bias, Value batch_idx, Value q_head_idx, Value row_block_idx, Value col_block_idx, Value seed_arg, Type oty, Type ity, IntegerType i32, MLIRContext* context)` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L82) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- <a id="CreateBackwardDkvKernel"></a>`CreateBackwardDkvKernel(MLIRContext* context, const FlashAttnConfig& config, const Tiling& tiling)` — [`L568`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L568) — Creates the flash attention backward DKV kernel for the given configuration. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="CreateBackwardDqKernel"></a>`CreateBackwardDqKernel(MLIRContext* context, const FlashAttnConfig& config, const Tiling& tiling)` — [`L710`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L710) — Creates the flash attention backward DQ kernel for the given configuration. — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="GetBwdArgIndices"></a>`GetBwdArgIndices(const FlashAttnConfig& config, int num_iteration_dims = 4)` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L162)
- <a id="LoadAndCastTiles"></a>`LoadAndCastTiles(ImplicitLocOpBuilder& fn_builder, func::FuncOp fn, const FlashAttnConfig& config, const Tiling& tiling, Type oty, const BwdArgIndices& arg_indices)` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L192)
- `LoadAndCastTiles(ImplicitLocOpBuilder& fn_builder, func::FuncOp fn, const FlashAttnConfig& config, const Tiling& tiling, Type oty, const BwdArgIndices& arg_indices)` — [`L192`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L192)
- <a id="SetBackwardDkvKernelAttributes"></a>`SetBackwardDkvKernelAttributes(const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L359`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L359) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `SetBackwardDkvKernelAttributes(const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L359`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L359)
- `SetBackwardDqKernelAttributes(const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L496`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L496)
- <a id="SetBackwardDqKernelAttributes"></a>`SetBackwardDqKernelAttributes(const FlashAttnConfig& config, const Tiling& tiling, func::FuncOp fn, OpBuilder& builder)` — [`L496`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L496) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- <a id="buildBackwardDkvModule"></a>`buildBackwardDkvModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L218`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L218) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `buildBackwardDkvModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L218`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L218)
- <a id="buildBackwardDqModule"></a>`buildBackwardDqModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L600`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L600) — documented in [mosaic-matmul](../../../../concepts/mosaic-matmul.md)
- `buildBackwardDqModule(ImplicitLocOpBuilder& module_builder, const FlashAttnConfig& config, const Tiling& tiling)` — [`L600`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/flash_attention_backward_kernel.cc#L600)

