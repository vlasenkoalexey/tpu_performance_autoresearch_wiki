---
slug: stablehlo
repo: raw/code/stablehlo
acquire: submodule
wiki_subdir: codebases
source_type: docs
# StableHLO is a reference, not an optimization target — its value is the op-set spec + pass docs,
# not its C++/MLIR call graph. Ingest as DOCS mode: grounding anchored to a source doc + section.
doc_globs:
  - docs/**/*.md
synthesis_focus: "TPU performance — op semantics, compiler passes, layout, collectives, precision"
---

## Concepts
