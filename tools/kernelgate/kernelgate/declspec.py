"""Declarative perturbation-battery specs for `kgate coverage`.

Instead of hand-writing a `perturb_regions` family spec (the modules in
kernelgate/specs/), a declarative spec names the semantic AXES of the problem
(head, batch, kv-block, ...) and how each axis slot maps input -> output.
kgate generates one probe per (axis, slot): perturb the input slice, assert
the mapped output region MOVES and everything else is BIT-IDENTICAL — and
additionally flags dead output slots (all-NaN / all-zero) in the clean
candidate run. The v042 class (kernel computes only head 0 of a group,
passes loose parity, skips the rest) fails with the skipped slots NAMED.

Spec forms (equivalent):
  - a Python module defining SPEC = {...} (or top-level AXES = [...],
    optional SCALE / ADD defaults)
  - a .json / .yaml / .yml file containing the same dict
  - a plain dict passed to coverage.run_coverage directly

  SPEC = {
    "axes": [
      {"name": "head", "input": 0, "size": 8,
       "input_slice":  "[i]",    # numpy index into the perturbed input; i = slot
       "output_slice": "[i]",    # output region that MUST move for slot i;
                                 # everything else MUST NOT move. "all" = the
                                 # whole output must move (no unaffected set).
       "scale": 2.0, "add": 0.0},  # optional per-axis perturbation override
    ],
    "scale": 2.0, "add": 0.0,      # spec-wide perturbation defaults
  }

Index expressions are evaluated as `np.s_<expr>` with `i` bound to the slot
index — "[:, i]", "[i // 4]", "[..., i, :]" all work. Python-module specs may
use a callable `slicer(i) -> index` instead of the expression string.
Perturbation: slice -> slice * scale + add (set `add` when the slice may be
all zeros, otherwise a pure scale has no power).
"""
from __future__ import annotations

import json
import os

DEFAULT_SCALE = 2.0
DEFAULT_ADD = 0.0

AXIS_KEYS = {"name", "input", "size", "input_slice", "output_slice", "scale", "add"}


def load_spec_file(path: str) -> dict:
    """Load a declarative spec from a .json / .yaml / .yml file."""
    ext = os.path.splitext(path)[1].lower()
    with open(path) as f:
        text = f.read()
    if ext in (".yaml", ".yml"):
        import yaml  # optional dependency, only needed for YAML specs
        spec = yaml.safe_load(text)
    else:
        spec = json.loads(text)
    spec["__kgate_path__"] = os.path.abspath(path)
    return spec


def is_declarative(spec) -> bool:
    """True when `spec` (module or dict) is a declarative axes spec rather
    than a legacy perturb_regions family module."""
    if hasattr(spec, "perturb_regions"):
        return False
    if isinstance(spec, dict):
        return "axes" in spec
    return hasattr(spec, "SPEC") or hasattr(spec, "AXES")


def normalize(spec) -> dict:
    """Module / dict -> canonical {"axes": [...], "scale": s, "add": a}."""
    if isinstance(spec, dict):
        d = dict(spec)
    elif hasattr(spec, "SPEC"):
        d = dict(spec.SPEC)
        d.setdefault("__kgate_path__", getattr(spec, "__kgate_path__", None))
    elif hasattr(spec, "AXES"):
        d = {"axes": spec.AXES,
             "scale": getattr(spec, "SCALE", DEFAULT_SCALE),
             "add": getattr(spec, "ADD", DEFAULT_ADD),
             "__kgate_path__": getattr(spec, "__kgate_path__", None)}
    else:
        raise ValueError("not a declarative spec: %r" % (spec,))
    if not d.get("axes"):
        raise ValueError("declarative spec has no axes")
    d.setdefault("scale", DEFAULT_SCALE)
    d.setdefault("add", DEFAULT_ADD)
    for ax in d["axes"]:
        missing = {"name", "input", "size", "input_slice", "output_slice"} - set(ax)
        if missing:
            raise ValueError("axis %r missing keys: %s" % (ax.get("name"), sorted(missing)))
        unknown = set(ax) - AXIS_KEYS
        if unknown:
            raise ValueError("axis %r has unknown keys: %s" % (ax["name"], sorted(unknown)))
    return d


def index_for(sl, i: int):
    """Slice spec -> concrete numpy index for slot i.

    `sl` is either an index-expression string like "[:, i]" (evaluated as
    np.s_[:, i] with only np and i in scope) or a callable slicer(i)."""
    import numpy as np
    if callable(sl):
        return sl(i)
    if not isinstance(sl, str):
        raise ValueError("slice spec must be an index-expr string or callable, got %r" % (sl,))
    expr = sl.strip()
    if not expr.startswith("["):
        raise ValueError("index expr must start with '[': %r" % expr)
    return eval("np.s_%s" % expr, {"np": np, "i": i, "__builtins__": {}})


def build_probes(spec: dict, inputs, out_shape) -> list[dict]:
    """Generate coverage-protocol probes ({name, inputs, affected_mask}, plus
    axis/slot bookkeeping) from a normalized declarative spec."""
    import numpy as np
    probes = []
    for ax in spec["axes"]:
        scale = float(ax.get("scale", spec["scale"]))
        add = float(ax.get("add", spec["add"]))
        x = inputs[ax["input"]]
        for i in range(int(ax["size"])):
            idx = index_for(ax["input_slice"], i)
            x2 = x.at[idx].multiply(scale)
            if add:
                x2 = x2.at[idx].add(add)
            perturbed = tuple(x2 if j == ax["input"] else v
                              for j, v in enumerate(inputs))
            mask = np.zeros(out_shape, dtype=bool)
            if ax["output_slice"] == "all":
                mask[...] = True
            else:
                mask[index_for(ax["output_slice"], i)] = True
            probes.append({
                "name": "%s[%d]" % (ax["name"], i),
                "axis": ax["name"], "slot": i,
                "inputs": perturbed,
                "affected_mask": mask,
            })
    return probes


def dead_slot_checks(spec: dict, baseline_out, candidate_out) -> list[dict]:
    """Per (axis, slot) NaN / all-zero screening of the CLEAN candidate output.

    A slot whose output region is all-NaN or all-zero while the baseline's is
    not = skipped work (the v042 head-skip signature), caught even when the
    probe response check would need a perturbation to see it. A slot where the
    BASELINE region is itself degenerate is a SPEC_ERROR (mask charged to the
    spec, not the candidate)."""
    import numpy as np
    b = np.asarray(baseline_out).astype(np.float32)
    c = np.asarray(candidate_out).astype(np.float32)
    checks = []
    for ax in spec["axes"]:
        if ax["output_slice"] == "all":
            continue
        for i in range(int(ax["size"])):
            idx = index_for(ax["output_slice"], i)
            bb, cc = b[idx], c[idx]
            rec = {"axis": ax["name"], "slot": i, "name": "%s[%d]" % (ax["name"], i)}
            if bb.size == 0:
                rec["status"] = "SPEC_ERROR"
                rec["detail"] = "output_slice selects an empty region"
            elif not np.isfinite(bb).all() or not bb.any():
                rec["status"] = "SPEC_ERROR"
                rec["detail"] = ("baseline output slot is itself degenerate "
                                 "(non-finite or all-zero) — mask is wrong")
            elif np.isnan(cc).all():
                rec["status"] = "FAIL"
                rec["detail"] = "candidate output slot is all-NaN"
            elif not cc.any():
                rec["status"] = "FAIL"
                rec["detail"] = "candidate output slot is all-zero (skipped work)"
            else:
                rec["status"] = "OK"
            checks.append(rec)
    return checks
