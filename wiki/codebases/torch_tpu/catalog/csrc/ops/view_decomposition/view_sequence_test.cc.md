---
title: 'Module: csrc/ops/view_decomposition/view_sequence_test.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/view_sequence_test.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence_test.cc`/
symbols:
  SymbolicViewPrimitive_CastingViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_CastingViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  SimplifyTest: SimplifyTest(83235d787b2148b8).
  Pair: Pair(6330b903d62528c9).
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  ElementsAre: ElementsAre(254ac5060ee5ff9c).
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_PadViewCacheKeys_Test.TestBody: SymbolicViewPrimitive_PadViewCacheKeys_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_NothingToSimplify_Test.TestBody: Simplify_NothingToSimplify_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_DoNotRemoveSameSizeBitcast_Test.TestBody: Simplify_DoNotRemoveSameSizeBitcast_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpPad_Test: Simplify_RemoveNoOpPad_Test#
  Simplify_DoNotRemoveSameSizeBitcast_Test: Simplify_DoNotRemoveSameSizeBitcast_Test#
  Simplify_RemoveNoOpUnfold_Test: Simplify_RemoveNoOpUnfold_Test#
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#
  Simplify_RemoveNoOpReshape_Test: Simplify_RemoveNoOpReshape_Test#
  Simplify_ConjComplex_Test: Simplify_ConjComplex_Test#
  Simplify_RemoveNoOpSlice_Test: Simplify_RemoveNoOpSlice_Test#
  Simplify_MergedReshapeAndSlice_Test: Simplify_MergedReshapeAndSlice_Test#
  SymbolicViewPrimitive_PadViewCacheKeys_Test: SymbolicViewPrimitive_PadViewCacheKeys_Test#
  Simplify_ConjReal_Test: Simplify_ConjReal_Test#
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#
  Simplify_NothingToSimplify_Test: Simplify_NothingToSimplify_Test#
  Simplify_RemoveNoOpBitcast_Test: Simplify_RemoveNoOpBitcast_Test#
  ViewPrimitiveEquality_ConjPrimitive_Test: ViewPrimitiveEquality_ConjPrimitive_Test#
  Simplify_EmptyList_Test: Simplify_EmptyList_Test#
  Simplify_MergedSlice_Test: Simplify_MergedSlice_Test#
  Simplify_ReshapeConj_Test: Simplify_ReshapeConj_Test#
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#
  SymbolicViewPrimitive_CastingViewCacheKeys_Test: SymbolicViewPrimitive_CastingViewCacheKeys_Test#
  Simplify_RemoveNoOpBroadcast_Test: Simplify_RemoveNoOpBroadcast_Test#
  Simplify_DoubleConj_Test: Simplify_DoubleConj_Test#
  ViewPrimitiveEquality_BroadcastPrimitive_Test: ViewPrimitiveEquality_BroadcastPrimitive_Test#
  Simplify_RemoveNoOpPermute_Test: Simplify_RemoveNoOpPermute_Test#
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#
  Simplify_RecursiveSimplify_Test: Simplify_RecursiveSimplify_Test#
  Simplify_MergedReshape_Test: Simplify_MergedReshape_Test#
  Simplify_RecursiveSimplify_Test.TestBody: Simplify_RecursiveSimplify_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_MergedReshapeAndSlice_Test.TestBody: Simplify_MergedReshapeAndSlice_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpBitcast_Test.TestBody: Simplify_RemoveNoOpBitcast_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_ReshapeConj_Test.TestBody: Simplify_ReshapeConj_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_ConjReal_Test.TestBody: Simplify_ConjReal_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_ConjComplex_Test.TestBody: Simplify_ConjComplex_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpBroadcast_Test.TestBody: Simplify_RemoveNoOpBroadcast_Test#TestBody(49f6e7a06ebc5aa8).
  ViewPrimitiveEquality_BroadcastPrimitive_Test.TestBody: ViewPrimitiveEquality_BroadcastPrimitive_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_DoubleConj_Test.TestBody: Simplify_DoubleConj_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpPermute_Test.TestBody: Simplify_RemoveNoOpPermute_Test#TestBody(49f6e7a06ebc5aa8).
  ViewPrimitiveEquality_ConjPrimitive_Test.TestBody: ViewPrimitiveEquality_ConjPrimitive_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpReshape_Test.TestBody: Simplify_RemoveNoOpReshape_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpSlice_Test.TestBody: Simplify_RemoveNoOpSlice_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpPad_Test.TestBody: Simplify_RemoveNoOpPad_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_MergedReshape_Test.TestBody: Simplify_MergedReshape_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpUnfold_Test.TestBody: Simplify_RemoveNoOpUnfold_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_MergedSlice_Test.TestBody: Simplify_MergedSlice_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_EmptyList_Test.TestBody: Simplify_EmptyList_Test#TestBody(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpPad_Test.Simplify_RemoveNoOpPad_Test: Simplify_RemoveNoOpPad_Test#Simplify_RemoveNoOpPad_Test(49f6e7a06ebc5aa8).
  Simplify_ConjReal_Test.Simplify_ConjReal_Test: Simplify_ConjReal_Test#Simplify_ConjReal_Test(ef74ce0124262b0d).
  Simplify_MergedReshapeAndSlice_Test.operator: Simplify_MergedReshapeAndSlice_Test#`operator=`(29098e2801746ece).
  ViewPrimitiveEquality_ConjPrimitive_Test.test_info_: ViewPrimitiveEquality_ConjPrimitive_Test#test_info_.
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test.SymbolicViewPrimitive_TransposeViewCacheKeys_Test: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#SymbolicViewPrimitive_TransposeViewCacheKeys_Test(49f6e7a06ebc5aa8).
  ViewPrimitiveEquality_BroadcastPrimitive_Test.ViewPrimitiveEquality_BroadcastPrimitive_Test: ViewPrimitiveEquality_BroadcastPrimitive_Test#ViewPrimitiveEquality_BroadcastPrimitive_Test(d6230ab38364575a).
  Simplify_DoNotRemoveSameSizeBitcast_Test.Simplify_DoNotRemoveSameSizeBitcast_Test: Simplify_DoNotRemoveSameSizeBitcast_Test#Simplify_DoNotRemoveSameSizeBitcast_Test(6fbf35a1f57f2275).
  Simplify_NothingToSimplify_Test.operator: Simplify_NothingToSimplify_Test#`operator=`(579d09d5074b9671).
  Simplify_MergedSlice_Test.operator: Simplify_MergedSlice_Test#`operator=`(c758ed5456f36ce).
  SymbolicViewPrimitive_CastingViewCacheKeys_Test.SymbolicViewPrimitive_CastingViewCacheKeys_Test: SymbolicViewPrimitive_CastingViewCacheKeys_Test#SymbolicViewPrimitive_CastingViewCacheKeys_Test(eedb3884a331b16b).
  ViewPrimitiveEquality_BroadcastPrimitive_Test.test_info_: ViewPrimitiveEquality_BroadcastPrimitive_Test#test_info_.
  Simplify_EmptyList_Test.Simplify_EmptyList_Test: Simplify_EmptyList_Test#Simplify_EmptyList_Test(41b3bced4eb972f1).
  Simplify_RemoveNoOpReshape_Test.operator: Simplify_RemoveNoOpReshape_Test#`operator=`(cd09b2d8479098be).
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test.operator: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#`operator=`(309e6eb9bcd5b613).
  Simplify_RemoveNoOpSlice_Test.-Simplify_RemoveNoOpSlice_Test: Simplify_RemoveNoOpSlice_Test#`~Simplify_RemoveNoOpSlice_Test`(ced63f7c635d850d).
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#test_info_.
  SymbolicViewPrimitive_PadViewCacheKeys_Test.-SymbolicViewPrimitive_PadViewCacheKeys_Test: SymbolicViewPrimitive_PadViewCacheKeys_Test#`~SymbolicViewPrimitive_PadViewCacheKeys_Test`(ced63f7c635d850d).
  Simplify_NothingToSimplify_Test.test_info_: Simplify_NothingToSimplify_Test#test_info_.
  Simplify_RecursiveSimplify_Test.operator: Simplify_RecursiveSimplify_Test#`operator=`(2da6e9c3b0862089).
  SymbolicViewPrimitive_CastingViewCacheKeys_Test.operator: SymbolicViewPrimitive_CastingViewCacheKeys_Test#`operator=`(7efd56654460c0e3).
  ViewPrimitiveEquality_ConjPrimitive_Test.operator: ViewPrimitiveEquality_ConjPrimitive_Test#`operator=`(db0464802a25e8c3).
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test(49f6e7a06ebc5aa8).
  Simplify_DoubleConj_Test.-Simplify_DoubleConj_Test: Simplify_DoubleConj_Test#`~Simplify_DoubleConj_Test`(ced63f7c635d850d).
  SymbolicViewPrimitive_PadViewCacheKeys_Test.operator: SymbolicViewPrimitive_PadViewCacheKeys_Test#`operator=`(b9cfe2d444fd2f6a).
  Simplify_DoNotRemoveSameSizeBitcast_Test.operator: Simplify_DoNotRemoveSameSizeBitcast_Test#`operator=`(eaf3f8748b6a56f3).
  Simplify_RemoveNoOpPad_Test.operator: Simplify_RemoveNoOpPad_Test#`operator=`(131fabb9139d5d7b).
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.operator: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#`operator=`(26bfd862a201bb9a).
  Simplify_NothingToSimplify_Test.Simplify_NothingToSimplify_Test: Simplify_NothingToSimplify_Test#Simplify_NothingToSimplify_Test(ab0eef8463eb4be).
  Simplify_ConjComplex_Test.operator: Simplify_ConjComplex_Test#`operator=`(1015c9490ecdd4d6).
  Simplify_ConjComplex_Test.test_info_: Simplify_ConjComplex_Test#test_info_.
  Simplify_RemoveNoOpPad_Test.test_info_: Simplify_RemoveNoOpPad_Test#test_info_.
  ViewPrimitiveEquality_ConjPrimitive_Test.-ViewPrimitiveEquality_ConjPrimitive_Test: ViewPrimitiveEquality_ConjPrimitive_Test#`~ViewPrimitiveEquality_ConjPrimitive_Test`(ced63f7c635d850d).
  ViewPrimitiveEquality_ConjPrimitive_Test.ViewPrimitiveEquality_ConjPrimitive_Test: ViewPrimitiveEquality_ConjPrimitive_Test#ViewPrimitiveEquality_ConjPrimitive_Test(3c30411e4f2de591).
  Simplify_RemoveNoOpSlice_Test.Simplify_RemoveNoOpSlice_Test: Simplify_RemoveNoOpSlice_Test#Simplify_RemoveNoOpSlice_Test(c9073b68be5921ce).
  Simplify_RemoveNoOpBitcast_Test.Simplify_RemoveNoOpBitcast_Test: Simplify_RemoveNoOpBitcast_Test#Simplify_RemoveNoOpBitcast_Test(2443b080859a67c2).
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#test_info_.
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.-SymbolicViewPrimitive_BroadcastViewCacheKeys_Test: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#`~SymbolicViewPrimitive_BroadcastViewCacheKeys_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpReshape_Test.Simplify_RemoveNoOpReshape_Test: Simplify_RemoveNoOpReshape_Test#Simplify_RemoveNoOpReshape_Test(de3f38693b3c00c9).
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test.operator: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#`operator=`(56c72985cf6395b4).
  SymbolicViewPrimitive_TransposeViewCacheKeys_Test.-SymbolicViewPrimitive_TransposeViewCacheKeys_Test: SymbolicViewPrimitive_TransposeViewCacheKeys_Test#`~SymbolicViewPrimitive_TransposeViewCacheKeys_Test`(ced63f7c635d850d).
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.SymbolicViewPrimitive_ReshapeViewCacheKeys_Test: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#SymbolicViewPrimitive_ReshapeViewCacheKeys_Test(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#test_info_.
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#test_info_.
  Simplify_RemoveNoOpPermute_Test.operator: Simplify_RemoveNoOpPermute_Test#`operator=`(5201ef5d763e13d9).
  Simplify_MergedReshapeAndSlice_Test.Simplify_MergedReshapeAndSlice_Test: Simplify_MergedReshapeAndSlice_Test#Simplify_MergedReshapeAndSlice_Test(66429bb4db6beb3).
  Simplify_MergedReshapeAndSlice_Test.test_info_: Simplify_MergedReshapeAndSlice_Test#test_info_.
  Simplify_RemoveNoOpPermute_Test.test_info_: Simplify_RemoveNoOpPermute_Test#test_info_.
  Simplify_NothingToSimplify_Test.-Simplify_NothingToSimplify_Test: Simplify_NothingToSimplify_Test#`~Simplify_NothingToSimplify_Test`(ced63f7c635d850d).
  Simplify_DoubleConj_Test.operator: Simplify_DoubleConj_Test#`operator=`(8e89a41e91385a21).
  Simplify_RemoveNoOpBroadcast_Test.Simplify_RemoveNoOpBroadcast_Test: Simplify_RemoveNoOpBroadcast_Test#Simplify_RemoveNoOpBroadcast_Test(49f6e7a06ebc5aa8).
  Simplify_RemoveNoOpBitcast_Test.operator: Simplify_RemoveNoOpBitcast_Test#`operator=`(697794a5e990e1ae).
  Simplify_EmptyList_Test.-Simplify_EmptyList_Test: Simplify_EmptyList_Test#`~Simplify_EmptyList_Test`(ced63f7c635d850d).
  Simplify_RecursiveSimplify_Test.Simplify_RecursiveSimplify_Test: Simplify_RecursiveSimplify_Test#Simplify_RecursiveSimplify_Test(49f6e7a06ebc5aa8).
  SymbolicViewPrimitive_PadViewCacheKeys_Test.SymbolicViewPrimitive_PadViewCacheKeys_Test: SymbolicViewPrimitive_PadViewCacheKeys_Test#SymbolicViewPrimitive_PadViewCacheKeys_Test(79a982de16049b5e).
  SymbolicViewPrimitive_PadViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_PadViewCacheKeys_Test#test_info_.
  Simplify_MergedSlice_Test.Simplify_MergedSlice_Test: Simplify_MergedSlice_Test#Simplify_MergedSlice_Test(724be104a0260151).
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.operator: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#`operator=`(d038337c389fa647).
  Simplify_ConjReal_Test.operator: Simplify_ConjReal_Test#`operator=`(3dac56088a9c44e6).
  Simplify_ReshapeConj_Test.operator: Simplify_ReshapeConj_Test#`operator=`(468ecdfd25399a29).
  Simplify_ReshapeConj_Test.Simplify_ReshapeConj_Test: Simplify_ReshapeConj_Test#Simplify_ReshapeConj_Test(282991ae19cc1abe).
  Simplify_RemoveNoOpBroadcast_Test.test_info_: Simplify_RemoveNoOpBroadcast_Test#test_info_.
  Simplify_RecursiveSimplify_Test.-Simplify_RecursiveSimplify_Test: Simplify_RecursiveSimplify_Test#`~Simplify_RecursiveSimplify_Test`(ced63f7c635d850d).
  Simplify_MergedSlice_Test.test_info_: Simplify_MergedSlice_Test#test_info_.
  Simplify_RemoveNoOpUnfold_Test.Simplify_RemoveNoOpUnfold_Test: Simplify_RemoveNoOpUnfold_Test#Simplify_RemoveNoOpUnfold_Test(c0a03b04d2d6d809).
  Simplify_EmptyList_Test.operator: Simplify_EmptyList_Test#`operator=`(3b71b92233baecf8).
  SymbolicViewPrimitive_CastingViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_CastingViewCacheKeys_Test#test_info_.
  Simplify_RemoveNoOpPad_Test.-Simplify_RemoveNoOpPad_Test: Simplify_RemoveNoOpPad_Test#`~Simplify_RemoveNoOpPad_Test`(ced63f7c635d850d).
  Simplify_MergedReshape_Test.Simplify_MergedReshape_Test: Simplify_MergedReshape_Test#Simplify_MergedReshape_Test(d3397c6224d039).
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test.SymbolicViewPrimitive_MultipleViewCacheKeys_Test: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#SymbolicViewPrimitive_MultipleViewCacheKeys_Test(c8c4e22bf39584bd).
  SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.-SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test: SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test#`~SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpPermute_Test.Simplify_RemoveNoOpPermute_Test: Simplify_RemoveNoOpPermute_Test#Simplify_RemoveNoOpPermute_Test(df846a8ee17b013).
  Simplify_RemoveNoOpUnfold_Test.operator: Simplify_RemoveNoOpUnfold_Test#`operator=`(9f5d6625b894748e).
  SymbolicViewPrimitive_CastingViewCacheKeys_Test.-SymbolicViewPrimitive_CastingViewCacheKeys_Test: SymbolicViewPrimitive_CastingViewCacheKeys_Test#`~SymbolicViewPrimitive_CastingViewCacheKeys_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpUnfold_Test.test_info_: Simplify_RemoveNoOpUnfold_Test#test_info_.
  SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.-SymbolicViewPrimitive_ReshapeViewCacheKeys_Test: SymbolicViewPrimitive_ReshapeViewCacheKeys_Test#`~SymbolicViewPrimitive_ReshapeViewCacheKeys_Test`(ced63f7c635d850d).
  SymbolicViewPrimitive_MultipleViewCacheKeys_Test.-SymbolicViewPrimitive_MultipleViewCacheKeys_Test: SymbolicViewPrimitive_MultipleViewCacheKeys_Test#`~SymbolicViewPrimitive_MultipleViewCacheKeys_Test`(ced63f7c635d850d).
  Simplify_ReshapeConj_Test.-Simplify_ReshapeConj_Test: Simplify_ReshapeConj_Test#`~Simplify_ReshapeConj_Test`(ced63f7c635d850d).
  ViewPrimitiveEquality_BroadcastPrimitive_Test.operator: ViewPrimitiveEquality_BroadcastPrimitive_Test#`operator=`(722edb1b24c38632).
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.SymbolicViewPrimitive_BroadcastViewCacheKeys_Test: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#SymbolicViewPrimitive_BroadcastViewCacheKeys_Test(49f6e7a06ebc5aa8).
  Simplify_DoubleConj_Test.test_info_: Simplify_DoubleConj_Test#test_info_.
  Simplify_ConjReal_Test.test_info_: Simplify_ConjReal_Test#test_info_.
  Simplify_DoubleConj_Test.Simplify_DoubleConj_Test: Simplify_DoubleConj_Test#Simplify_DoubleConj_Test(49f6e7a06ebc5aa8).
  Simplify_MergedReshape_Test.test_info_: Simplify_MergedReshape_Test#test_info_.
  Simplify_MergedReshapeAndSlice_Test.-Simplify_MergedReshapeAndSlice_Test: Simplify_MergedReshapeAndSlice_Test#`~Simplify_MergedReshapeAndSlice_Test`(ced63f7c635d850d).
  Simplify_MergedReshape_Test.operator: Simplify_MergedReshape_Test#`operator=`(821b61b985eef274).
  ViewPrimitiveEquality_BroadcastPrimitive_Test.-ViewPrimitiveEquality_BroadcastPrimitive_Test: ViewPrimitiveEquality_BroadcastPrimitive_Test#`~ViewPrimitiveEquality_BroadcastPrimitive_Test`(ced63f7c635d850d).
  Simplify_RecursiveSimplify_Test.test_info_: Simplify_RecursiveSimplify_Test#test_info_.
  Simplify_ConjComplex_Test.-Simplify_ConjComplex_Test: Simplify_ConjComplex_Test#`~Simplify_ConjComplex_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpPermute_Test.-Simplify_RemoveNoOpPermute_Test: Simplify_RemoveNoOpPermute_Test#`~Simplify_RemoveNoOpPermute_Test`(ced63f7c635d850d).
  Simplify_ConjComplex_Test.Simplify_ConjComplex_Test: Simplify_ConjComplex_Test#Simplify_ConjComplex_Test(cd607a12b43df562).
  Simplify_RemoveNoOpBroadcast_Test.operator: Simplify_RemoveNoOpBroadcast_Test#`operator=`(1133600b990fb2dc).
  Simplify_ReshapeConj_Test.test_info_: Simplify_ReshapeConj_Test#test_info_.
  Simplify_MergedReshape_Test.-Simplify_MergedReshape_Test: Simplify_MergedReshape_Test#`~Simplify_MergedReshape_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpBitcast_Test.-Simplify_RemoveNoOpBitcast_Test: Simplify_RemoveNoOpBitcast_Test#`~Simplify_RemoveNoOpBitcast_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpReshape_Test.test_info_: Simplify_RemoveNoOpReshape_Test#test_info_.
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.operator: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#`operator=`(5f3f4ab885787e42).
  Simplify_DoNotRemoveSameSizeBitcast_Test.-Simplify_DoNotRemoveSameSizeBitcast_Test: Simplify_DoNotRemoveSameSizeBitcast_Test#`~Simplify_DoNotRemoveSameSizeBitcast_Test`(ced63f7c635d850d).
  SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.test_info_: SymbolicViewPrimitive_BroadcastViewCacheKeys_Test#test_info_.
  Simplify_DoNotRemoveSameSizeBitcast_Test.test_info_: Simplify_DoNotRemoveSameSizeBitcast_Test#test_info_.
  Simplify_RemoveNoOpSlice_Test.operator: Simplify_RemoveNoOpSlice_Test#`operator=`(a4ae02b6cc9a708e).
  Simplify_RemoveNoOpBroadcast_Test.-Simplify_RemoveNoOpBroadcast_Test: Simplify_RemoveNoOpBroadcast_Test#`~Simplify_RemoveNoOpBroadcast_Test`(ced63f7c635d850d).
  Simplify_MergedSlice_Test.-Simplify_MergedSlice_Test: Simplify_MergedSlice_Test#`~Simplify_MergedSlice_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpReshape_Test.-Simplify_RemoveNoOpReshape_Test: Simplify_RemoveNoOpReshape_Test#`~Simplify_RemoveNoOpReshape_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpSlice_Test.test_info_: Simplify_RemoveNoOpSlice_Test#test_info_.
  Simplify_EmptyList_Test.test_info_: Simplify_EmptyList_Test#test_info_.
  Simplify_RemoveNoOpUnfold_Test.-Simplify_RemoveNoOpUnfold_Test: Simplify_RemoveNoOpUnfold_Test#`~Simplify_RemoveNoOpUnfold_Test`(ced63f7c635d850d).
  Simplify_RemoveNoOpBitcast_Test.test_info_: Simplify_RemoveNoOpBitcast_Test#test_info_.
  Simplify_ConjReal_Test.-Simplify_ConjReal_Test: Simplify_ConjReal_Test#`~Simplify_ConjReal_Test`(ced63f7c635d850d).
---
# Module: [`csrc/ops/view_decomposition/view_sequence_test.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc)

> **Collapsed catalog** (246 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="ElementsAre"></a>`ElementsAre` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L47)
- <a id="Pair"></a>`Pair` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L48)
- <a id="SimplifyTest"></a>`SimplifyTest` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L50)
- <a id="Simplify_ConjComplex_Test"></a>`Simplify_ConjComplex_Test` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjComplex_Test.-Simplify_ConjComplex_Test"></a>`Simplify_ConjComplex_Test.-Simplify_ConjComplex_Test` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjComplex_Test.Simplify_ConjComplex_Test"></a>`Simplify_ConjComplex_Test.Simplify_ConjComplex_Test` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjComplex_Test.TestBody"></a>`Simplify_ConjComplex_Test.TestBody` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjComplex_Test.operator"></a>`Simplify_ConjComplex_Test.operator` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjComplex_Test.test_info_"></a>`Simplify_ConjComplex_Test.test_info_` — [`L258`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L258)
- <a id="Simplify_ConjReal_Test"></a>`Simplify_ConjReal_Test` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_ConjReal_Test.-Simplify_ConjReal_Test"></a>`Simplify_ConjReal_Test.-Simplify_ConjReal_Test` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_ConjReal_Test.Simplify_ConjReal_Test"></a>`Simplify_ConjReal_Test.Simplify_ConjReal_Test` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_ConjReal_Test.TestBody"></a>`Simplify_ConjReal_Test.TestBody` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_ConjReal_Test.operator"></a>`Simplify_ConjReal_Test.operator` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_ConjReal_Test.test_info_"></a>`Simplify_ConjReal_Test.test_info_` — [`L250`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L250)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test.-Simplify_DoNotRemoveSameSizeBitcast_Test"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test.-Simplify_DoNotRemoveSameSizeBitcast_Test` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test.Simplify_DoNotRemoveSameSizeBitcast_Test"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test.Simplify_DoNotRemoveSameSizeBitcast_Test` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test.TestBody"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test.TestBody` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test.operator"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test.operator` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoNotRemoveSameSizeBitcast_Test.test_info_"></a>`Simplify_DoNotRemoveSameSizeBitcast_Test.test_info_` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L163)
- <a id="Simplify_DoubleConj_Test"></a>`Simplify_DoubleConj_Test` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_DoubleConj_Test.-Simplify_DoubleConj_Test"></a>`Simplify_DoubleConj_Test.-Simplify_DoubleConj_Test` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_DoubleConj_Test.Simplify_DoubleConj_Test"></a>`Simplify_DoubleConj_Test.Simplify_DoubleConj_Test` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_DoubleConj_Test.TestBody"></a>`Simplify_DoubleConj_Test.TestBody` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_DoubleConj_Test.operator"></a>`Simplify_DoubleConj_Test.operator` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_DoubleConj_Test.test_info_"></a>`Simplify_DoubleConj_Test.test_info_` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L264)
- <a id="Simplify_EmptyList_Test"></a>`Simplify_EmptyList_Test` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_EmptyList_Test.-Simplify_EmptyList_Test"></a>`Simplify_EmptyList_Test.-Simplify_EmptyList_Test` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_EmptyList_Test.Simplify_EmptyList_Test"></a>`Simplify_EmptyList_Test.Simplify_EmptyList_Test` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_EmptyList_Test.TestBody"></a>`Simplify_EmptyList_Test.TestBody` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_EmptyList_Test.operator"></a>`Simplify_EmptyList_Test.operator` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_EmptyList_Test.test_info_"></a>`Simplify_EmptyList_Test.test_info_` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L83)
- <a id="Simplify_MergedReshapeAndSlice_Test"></a>`Simplify_MergedReshapeAndSlice_Test` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshapeAndSlice_Test.-Simplify_MergedReshapeAndSlice_Test"></a>`Simplify_MergedReshapeAndSlice_Test.-Simplify_MergedReshapeAndSlice_Test` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshapeAndSlice_Test.Simplify_MergedReshapeAndSlice_Test"></a>`Simplify_MergedReshapeAndSlice_Test.Simplify_MergedReshapeAndSlice_Test` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshapeAndSlice_Test.TestBody"></a>`Simplify_MergedReshapeAndSlice_Test.TestBody` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshapeAndSlice_Test.operator"></a>`Simplify_MergedReshapeAndSlice_Test.operator` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshapeAndSlice_Test.test_info_"></a>`Simplify_MergedReshapeAndSlice_Test.test_info_` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L211)
- <a id="Simplify_MergedReshape_Test"></a>`Simplify_MergedReshape_Test` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedReshape_Test.-Simplify_MergedReshape_Test"></a>`Simplify_MergedReshape_Test.-Simplify_MergedReshape_Test` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedReshape_Test.Simplify_MergedReshape_Test"></a>`Simplify_MergedReshape_Test.Simplify_MergedReshape_Test` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedReshape_Test.TestBody"></a>`Simplify_MergedReshape_Test.TestBody` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedReshape_Test.operator"></a>`Simplify_MergedReshape_Test.operator` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedReshape_Test.test_info_"></a>`Simplify_MergedReshape_Test.test_info_` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L190)
- <a id="Simplify_MergedSlice_Test"></a>`Simplify_MergedSlice_Test` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_MergedSlice_Test.-Simplify_MergedSlice_Test"></a>`Simplify_MergedSlice_Test.-Simplify_MergedSlice_Test` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_MergedSlice_Test.Simplify_MergedSlice_Test"></a>`Simplify_MergedSlice_Test.Simplify_MergedSlice_Test` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_MergedSlice_Test.TestBody"></a>`Simplify_MergedSlice_Test.TestBody` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_MergedSlice_Test.operator"></a>`Simplify_MergedSlice_Test.operator` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_MergedSlice_Test.test_info_"></a>`Simplify_MergedSlice_Test.test_info_` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L197)
- <a id="Simplify_NothingToSimplify_Test"></a>`Simplify_NothingToSimplify_Test` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_NothingToSimplify_Test.-Simplify_NothingToSimplify_Test"></a>`Simplify_NothingToSimplify_Test.-Simplify_NothingToSimplify_Test` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_NothingToSimplify_Test.Simplify_NothingToSimplify_Test"></a>`Simplify_NothingToSimplify_Test.Simplify_NothingToSimplify_Test` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_NothingToSimplify_Test.TestBody"></a>`Simplify_NothingToSimplify_Test.TestBody` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_NothingToSimplify_Test.operator"></a>`Simplify_NothingToSimplify_Test.operator` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_NothingToSimplify_Test.test_info_"></a>`Simplify_NothingToSimplify_Test.test_info_` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L85)
- <a id="Simplify_RecursiveSimplify_Test"></a>`Simplify_RecursiveSimplify_Test` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RecursiveSimplify_Test.-Simplify_RecursiveSimplify_Test"></a>`Simplify_RecursiveSimplify_Test.-Simplify_RecursiveSimplify_Test` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RecursiveSimplify_Test.Simplify_RecursiveSimplify_Test"></a>`Simplify_RecursiveSimplify_Test.Simplify_RecursiveSimplify_Test` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RecursiveSimplify_Test.TestBody"></a>`Simplify_RecursiveSimplify_Test.TestBody` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RecursiveSimplify_Test.operator"></a>`Simplify_RecursiveSimplify_Test.operator` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RecursiveSimplify_Test.test_info_"></a>`Simplify_RecursiveSimplify_Test.test_info_` — [`L234`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L234)
- <a id="Simplify_RemoveNoOpBitcast_Test"></a>`Simplify_RemoveNoOpBitcast_Test` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBitcast_Test.-Simplify_RemoveNoOpBitcast_Test"></a>`Simplify_RemoveNoOpBitcast_Test.-Simplify_RemoveNoOpBitcast_Test` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBitcast_Test.Simplify_RemoveNoOpBitcast_Test"></a>`Simplify_RemoveNoOpBitcast_Test.Simplify_RemoveNoOpBitcast_Test` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBitcast_Test.TestBody"></a>`Simplify_RemoveNoOpBitcast_Test.TestBody` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBitcast_Test.operator"></a>`Simplify_RemoveNoOpBitcast_Test.operator` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBitcast_Test.test_info_"></a>`Simplify_RemoveNoOpBitcast_Test.test_info_` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L145)
- <a id="Simplify_RemoveNoOpBroadcast_Test"></a>`Simplify_RemoveNoOpBroadcast_Test` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpBroadcast_Test.-Simplify_RemoveNoOpBroadcast_Test"></a>`Simplify_RemoveNoOpBroadcast_Test.-Simplify_RemoveNoOpBroadcast_Test` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpBroadcast_Test.Simplify_RemoveNoOpBroadcast_Test"></a>`Simplify_RemoveNoOpBroadcast_Test.Simplify_RemoveNoOpBroadcast_Test` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpBroadcast_Test.TestBody"></a>`Simplify_RemoveNoOpBroadcast_Test.TestBody` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpBroadcast_Test.operator"></a>`Simplify_RemoveNoOpBroadcast_Test.operator` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpBroadcast_Test.test_info_"></a>`Simplify_RemoveNoOpBroadcast_Test.test_info_` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L117)
- <a id="Simplify_RemoveNoOpPad_Test"></a>`Simplify_RemoveNoOpPad_Test` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPad_Test.-Simplify_RemoveNoOpPad_Test"></a>`Simplify_RemoveNoOpPad_Test.-Simplify_RemoveNoOpPad_Test` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPad_Test.Simplify_RemoveNoOpPad_Test"></a>`Simplify_RemoveNoOpPad_Test.Simplify_RemoveNoOpPad_Test` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPad_Test.TestBody"></a>`Simplify_RemoveNoOpPad_Test.TestBody` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPad_Test.operator"></a>`Simplify_RemoveNoOpPad_Test.operator` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPad_Test.test_info_"></a>`Simplify_RemoveNoOpPad_Test.test_info_` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L135)
- <a id="Simplify_RemoveNoOpPermute_Test"></a>`Simplify_RemoveNoOpPermute_Test` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpPermute_Test.-Simplify_RemoveNoOpPermute_Test"></a>`Simplify_RemoveNoOpPermute_Test.-Simplify_RemoveNoOpPermute_Test` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpPermute_Test.Simplify_RemoveNoOpPermute_Test"></a>`Simplify_RemoveNoOpPermute_Test.Simplify_RemoveNoOpPermute_Test` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpPermute_Test.TestBody"></a>`Simplify_RemoveNoOpPermute_Test.TestBody` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpPermute_Test.operator"></a>`Simplify_RemoveNoOpPermute_Test.operator` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpPermute_Test.test_info_"></a>`Simplify_RemoveNoOpPermute_Test.test_info_` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L112)
- <a id="Simplify_RemoveNoOpReshape_Test"></a>`Simplify_RemoveNoOpReshape_Test` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpReshape_Test.-Simplify_RemoveNoOpReshape_Test"></a>`Simplify_RemoveNoOpReshape_Test.-Simplify_RemoveNoOpReshape_Test` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpReshape_Test.Simplify_RemoveNoOpReshape_Test"></a>`Simplify_RemoveNoOpReshape_Test.Simplify_RemoveNoOpReshape_Test` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpReshape_Test.TestBody"></a>`Simplify_RemoveNoOpReshape_Test.TestBody` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpReshape_Test.operator"></a>`Simplify_RemoveNoOpReshape_Test.operator` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpReshape_Test.test_info_"></a>`Simplify_RemoveNoOpReshape_Test.test_info_` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L106)
- <a id="Simplify_RemoveNoOpSlice_Test"></a>`Simplify_RemoveNoOpSlice_Test` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpSlice_Test.-Simplify_RemoveNoOpSlice_Test"></a>`Simplify_RemoveNoOpSlice_Test.-Simplify_RemoveNoOpSlice_Test` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpSlice_Test.Simplify_RemoveNoOpSlice_Test"></a>`Simplify_RemoveNoOpSlice_Test.Simplify_RemoveNoOpSlice_Test` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpSlice_Test.TestBody"></a>`Simplify_RemoveNoOpSlice_Test.TestBody` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpSlice_Test.operator"></a>`Simplify_RemoveNoOpSlice_Test.operator` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpSlice_Test.test_info_"></a>`Simplify_RemoveNoOpSlice_Test.test_info_` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L125)
- <a id="Simplify_RemoveNoOpUnfold_Test"></a>`Simplify_RemoveNoOpUnfold_Test` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_RemoveNoOpUnfold_Test.-Simplify_RemoveNoOpUnfold_Test"></a>`Simplify_RemoveNoOpUnfold_Test.-Simplify_RemoveNoOpUnfold_Test` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_RemoveNoOpUnfold_Test.Simplify_RemoveNoOpUnfold_Test"></a>`Simplify_RemoveNoOpUnfold_Test.Simplify_RemoveNoOpUnfold_Test` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_RemoveNoOpUnfold_Test.TestBody"></a>`Simplify_RemoveNoOpUnfold_Test.TestBody` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_RemoveNoOpUnfold_Test.operator"></a>`Simplify_RemoveNoOpUnfold_Test.operator` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_RemoveNoOpUnfold_Test.test_info_"></a>`Simplify_RemoveNoOpUnfold_Test.test_info_` — [`L152`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L152)
- <a id="Simplify_ReshapeConj_Test"></a>`Simplify_ReshapeConj_Test` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="Simplify_ReshapeConj_Test.-Simplify_ReshapeConj_Test"></a>`Simplify_ReshapeConj_Test.-Simplify_ReshapeConj_Test` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="Simplify_ReshapeConj_Test.Simplify_ReshapeConj_Test"></a>`Simplify_ReshapeConj_Test.Simplify_ReshapeConj_Test` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="Simplify_ReshapeConj_Test.TestBody"></a>`Simplify_ReshapeConj_Test.TestBody` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="Simplify_ReshapeConj_Test.operator"></a>`Simplify_ReshapeConj_Test.operator` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="Simplify_ReshapeConj_Test.test_info_"></a>`Simplify_ReshapeConj_Test.test_info_` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L275)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.-SymbolicViewPrimitive_BroadcastViewCacheKeys_Test"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.-SymbolicViewPrimitive_BroadcastViewCacheKeys_Test` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.SymbolicViewPrimitive_BroadcastViewCacheKeys_Test"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.SymbolicViewPrimitive_BroadcastViewCacheKeys_Test` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.TestBody` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.operator` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.test_info_` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L459)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test.-SymbolicViewPrimitive_CastingViewCacheKeys_Test"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test.-SymbolicViewPrimitive_CastingViewCacheKeys_Test` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test.SymbolicViewPrimitive_CastingViewCacheKeys_Test"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test.SymbolicViewPrimitive_CastingViewCacheKeys_Test` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test.TestBody` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test.operator` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_CastingViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_CastingViewCacheKeys_Test.test_info_` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L405)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test.-SymbolicViewPrimitive_MultipleViewCacheKeys_Test"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test.-SymbolicViewPrimitive_MultipleViewCacheKeys_Test` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test.SymbolicViewPrimitive_MultipleViewCacheKeys_Test"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test.SymbolicViewPrimitive_MultipleViewCacheKeys_Test` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test.TestBody` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test.operator` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_MultipleViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_MultipleViewCacheKeys_Test.test_info_` — [`L481`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L481)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test.-SymbolicViewPrimitive_PadViewCacheKeys_Test"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test.-SymbolicViewPrimitive_PadViewCacheKeys_Test` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test.SymbolicViewPrimitive_PadViewCacheKeys_Test"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test.SymbolicViewPrimitive_PadViewCacheKeys_Test` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test.TestBody` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test.operator` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_PadViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_PadViewCacheKeys_Test.test_info_` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L445)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.-SymbolicViewPrimitive_ReshapeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.-SymbolicViewPrimitive_ReshapeViewCacheKeys_Test` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.SymbolicViewPrimitive_ReshapeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.SymbolicViewPrimitive_ReshapeViewCacheKeys_Test` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.TestBody` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.operator` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_ReshapeViewCacheKeys_Test.test_info_` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L312)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test.-SymbolicViewPrimitive_TransposeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test.-SymbolicViewPrimitive_TransposeViewCacheKeys_Test` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test.SymbolicViewPrimitive_TransposeViewCacheKeys_Test"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test.SymbolicViewPrimitive_TransposeViewCacheKeys_Test` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test.TestBody` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test.operator` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_TransposeViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_TransposeViewCacheKeys_Test.test_info_` — [`L391`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L391)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.-SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.-SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.TestBody"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.TestBody` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.operator"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.operator` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.test_info_"></a>`SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.test_info_` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L510)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test.-ViewPrimitiveEquality_BroadcastPrimitive_Test"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test.-ViewPrimitiveEquality_BroadcastPrimitive_Test` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test.TestBody"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test.TestBody` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test.ViewPrimitiveEquality_BroadcastPrimitive_Test"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test.ViewPrimitiveEquality_BroadcastPrimitive_Test` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test.operator"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test.operator` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_BroadcastPrimitive_Test.test_info_"></a>`ViewPrimitiveEquality_BroadcastPrimitive_Test.test_info_` — [`L297`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L297)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test"></a>`ViewPrimitiveEquality_ConjPrimitive_Test` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test.-ViewPrimitiveEquality_ConjPrimitive_Test"></a>`ViewPrimitiveEquality_ConjPrimitive_Test.-ViewPrimitiveEquality_ConjPrimitive_Test` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test.TestBody"></a>`ViewPrimitiveEquality_ConjPrimitive_Test.TestBody` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test.ViewPrimitiveEquality_ConjPrimitive_Test"></a>`ViewPrimitiveEquality_ConjPrimitive_Test.ViewPrimitiveEquality_ConjPrimitive_Test` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test.operator"></a>`ViewPrimitiveEquality_ConjPrimitive_Test.operator` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
- <a id="ViewPrimitiveEquality_ConjPrimitive_Test.test_info_"></a>`ViewPrimitiveEquality_ConjPrimitive_Test.test_info_` — [`L288`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence_test.cc#L288)
