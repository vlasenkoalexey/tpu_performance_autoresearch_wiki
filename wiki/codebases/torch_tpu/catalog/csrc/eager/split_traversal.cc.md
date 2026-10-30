---
title: 'Module: csrc/eager/split_traversal.cc'
type: catalog
provenance: extracted
module: csrc/eager/split_traversal.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SplitTraversal: SplitTraversal(cd16dc99f8e6c2c2).
  ApplySplitPoints: '`$anonymous_namespace_csrc/eager/split_traversal.cc`/ApplySplitPoints(59b3491c524acd57).'
  SplitAllMaterializationPoints: '`$anonymous_namespace_csrc/eager/split_traversal.cc`/SplitAllMaterializationPoints(e04342d9656850c6).'
---
# Module: [`csrc/eager/split_traversal.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc)

## Functions
- `ApplySplitPoints(absl_nonnull std::unique_ptr<Traversal> traversal, const absl::flat_hash_set<const DeviceBufferList*>& split_points)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L93) — Creates a new set of traversals, one for each split point in the original
- <a id="ApplySplitPoints"></a>`ApplySplitPoints(absl_nonnull std::unique_ptr<Traversal> traversal, const absl::flat_hash_set<const DeviceBufferList*>& split_points)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L93) — Creates a new set of traversals, one for each split point in the original
- `SplitAllMaterializationPoints()` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L54) — Ensures that if a tensor is used after a materialization point, it is also
- <a id="SplitAllMaterializationPoints"></a>`SplitAllMaterializationPoints()` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L54) — Ensures that if a tensor is used after a materialization point, it is also
- `SplitTraversal(absl_nonnull std::unique_ptr<Traversal> traversal, absl::flat_hash_set<const DeviceBufferList*>& required_outputs)` — [`L123`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L123) — This function splits a given traversal into multiple traversals by applying
- <a id="SplitTraversal"></a>`SplitTraversal(absl_nonnull std::unique_ptr<Traversal> traversal, absl::flat_hash_set<const DeviceBufferList*>& required_outputs)` — [`L123`](../../../../../../raw/code/torch_tpu/csrc/eager/split_traversal.cc#L123) — This function splits a given traversal into multiple traversals by applying

