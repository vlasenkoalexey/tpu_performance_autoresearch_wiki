---
slug: easydel
repo: raw/code/EasyDeL
acquire: submodule
wiki_subdir: codebases
source_type: code
languages: [python]
index_shards:
  - easydel/layers/**
  - easydel/operations/**
  - easydel/caching/**
  - easydel/trainers/trainer/**
  - easydel/infra/**
# The 75-model zoo under modules/ is per-model transformer boilerplate — out of scope for
# perf work. Collapse it: keep each model's citeable symbol map (156 concept citations still
# resolve) but drop the detailed member body.
coverage_collapse:
  - easydel/modules/*
---

## Concepts
