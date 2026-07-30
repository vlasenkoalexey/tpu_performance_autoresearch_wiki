"""Declarative perturbation battery — the v042 head-skip regression.

2026-07-17 4p incident (v042): a candidate fit the VMEM envelope and passed
loose parity while computing only head 0 of each group — 1-of-8-heads
coverage. The declarative battery must FAIL such a kernel with the skipped
heads NAMED (probe no-response + dead-slot screening), and pass the correct
kernel. CPU backend, tiny shapes.
"""
import json
import textwrap

import numpy as np
import pytest

from kernelgate import coverage, declspec, protocol

# Per-head independent computation: output head h depends only on x[h], w[h].
BASELINE = '''
import jax
import jax.numpy as jnp

CONFIG = {"name": "tiny_perhead", "heads": 4, "seq": 16, "dim": 8}

def create_inputs(dtype=jnp.float32):
    key = jax.random.key(42)
    k1, k2 = jax.random.split(key)
    H, S, D = CONFIG["heads"], CONFIG["seq"], CONFIG["dim"]
    x = jax.random.normal(k1, (H, S, D), dtype)
    w = jax.random.normal(k2, (H, D, D), dtype)
    return x, w

def workload(x, w):
    return jnp.einsum("hsd,hde->hse", x, w)
'''

GOOD_CAND = '''
import jax.numpy as jnp

def workload_cand(x, w):
    return jnp.stack([x[h] @ w[h] for h in range(x.shape[0])])
'''

# v042 class: computes only head 0, leaves the rest zero.
HEAD_SKIP_CAND = '''
import jax.numpy as jnp

def workload_cand(x, w):
    out = jnp.zeros((x.shape[0], x.shape[1], w.shape[2]), x.dtype)
    return out.at[0].set(x[0] @ w[0])
'''

# aliasing variant: head 0's result broadcast into every head slot.
HEAD_ALIAS_CAND = '''
import jax.numpy as jnp

def workload_cand(x, w):
    h0 = x[0] @ w[0]
    return jnp.broadcast_to(h0[None], (x.shape[0],) + h0.shape)
'''

SPEC = {
    "axes": [
        {"name": "head", "input": 0, "size": 4,
         "input_slice": "[i]", "output_slice": "[i]"},
    ],
    "scale": 2.0,
}

SPEC_MODULE = '''
SPEC = {
    "axes": [
        {"name": "head", "input": 0, "size": 4,
         "input_slice": "[i]", "output_slice": "[i]"},
    ],
}
'''


def _mod(tmp_path, name, src):
    p = tmp_path / name
    p.write_text(textwrap.dedent(src))
    return protocol.load_module(str(p))


@pytest.fixture
def baseline_mod(tmp_path):
    return _mod(tmp_path, "baseline.py", BASELINE)


def test_index_for_exprs():
    assert declspec.index_for("[i]", 2) == 2
    assert declspec.index_for("[:, i]", 3) == (slice(None), 3)
    assert declspec.index_for("[i // 2]", 5) == 2
    assert declspec.index_for(lambda i: (i, slice(None)), 1) == (1, slice(None))
    with pytest.raises(ValueError):
        declspec.index_for("i]", 0)  # must start with '['


def test_normalize_validates_axes():
    with pytest.raises(ValueError):
        declspec.normalize({"axes": [{"name": "head"}]})   # missing keys
    with pytest.raises(ValueError):
        declspec.normalize({"axes": []})
    d = declspec.normalize(SPEC)
    assert d["scale"] == 2.0 and d["add"] == 0.0


def test_good_candidate_passes(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_good.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, SPEC)
    assert rep["status"] == "PASS", rep.get("exception") or rep["violations"]
    assert rep["spec"]["declarative"]
    assert rep["n_fail"] == 0 and not rep["violations"]
    assert [ax["status"] for ax in rep["axes"]] == ["OK"]


def test_head_skip_fails_with_skipped_heads_named(tmp_path, baseline_mod):
    """The v042 acceptance: only head 0 computed -> FAIL, heads 1..3 NAMED."""
    cand = _mod(tmp_path, "cand_skip.py", HEAD_SKIP_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, SPEC)
    assert rep["status"] == "FAIL", rep.get("exception")
    ax = rep["axes"][0]
    assert ax["axis"] == "head" and ax["status"] == "FAIL"
    assert ax["failing_slots"] == [1, 2, 3]        # skipped heads, by name
    # probes: heads 1..3 give no response; dead-slot screen sees all-zero
    assert any("head[1]" in v and "no response" in v for v in rep["violations"])
    assert any("dead slot head[1]" in v and "all-zero" in v
               for v in rep["violations"]), rep["violations"]
    # head 0 is genuinely computed
    assert 0 not in ax["failing_slots"]


def test_head_alias_fails_on_leak(tmp_path, baseline_mod):
    cand = _mod(tmp_path, "cand_alias.py", HEAD_ALIAS_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, SPEC)
    assert rep["status"] == "FAIL"
    # perturbing head 0 moves every head slot -> leak into unaffected set
    assert any("head[0]" in v and "leak" in v for v in rep["violations"]), \
        rep["violations"]


def test_spec_from_python_module(tmp_path, baseline_mod):
    spec_mod = _mod(tmp_path, "spec_mod.py", SPEC_MODULE)
    cand = _mod(tmp_path, "cand_good2.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, spec_mod)
    assert rep["status"] == "PASS", rep.get("exception")


def test_spec_from_json_file(tmp_path, baseline_mod):
    p = tmp_path / "spec.json"
    p.write_text(json.dumps(SPEC))
    spec = declspec.load_spec_file(str(p))
    cand = _mod(tmp_path, "cand_good3.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, spec)
    assert rep["status"] == "PASS", rep.get("exception")


def test_spec_from_yaml_file(tmp_path, baseline_mod):
    yaml = pytest.importorskip("yaml")
    p = tmp_path / "spec.yaml"
    p.write_text(yaml.safe_dump(SPEC))
    spec = declspec.load_spec_file(str(p))
    cand = _mod(tmp_path, "cand_good4.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, spec)
    assert rep["status"] == "PASS", rep.get("exception")


def test_bad_mask_is_spec_error_not_candidate_fail(tmp_path, baseline_mod):
    """A mask that blames the wrong output region must charge the SPEC."""
    bad = {"axes": [{"name": "head", "input": 0, "size": 4,
                     "input_slice": "[i]",
                     "output_slice": "[(i + 1) % 4]"}]}   # off-by-one mapping
    cand = _mod(tmp_path, "cand_good5.py", GOOD_CAND)
    rep = coverage.run_coverage(baseline_mod, cand, bad)
    assert rep["status"] == "SPEC_ERROR"


def test_legacy_family_specs_still_work(tmp_path):
    """The declarative path must not disturb the perturb_regions protocol."""
    from kernelgate.specs import causal_blocks
    from tests.test_gates_cpu import BASELINE as MHA_BASELINE, GOOD_CAND as MHA_GOOD
    base = _mod(tmp_path, "baseline.py", MHA_BASELINE)
    cand = _mod(tmp_path, "cand_mha.py", MHA_GOOD)
    rep = coverage.run_coverage(base, cand, causal_blocks)
    assert rep["status"] == "PASS", rep
    assert not rep["spec"]["declarative"]
