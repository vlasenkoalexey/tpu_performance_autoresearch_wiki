"""Regression gates on the real campaign kernels — requires a TPU chip.

Run on a TPU host with:  KGATE_TPU=1 python -m pytest tests/test_tpu_gates.py -v

Known-BAD fixtures MUST FAIL their gates; known-GOOD fixtures MUST PASS.
Each test loads modules fresh (module cache keyed by path, so repeated loads
are cheap) and runs the same library entry points the CLI uses.
"""
import os

import pytest

from kernelgate import coverage, parity, protocol, timing

pytestmark = pytest.mark.tpu

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def _load(rel):
    return protocol.load_module(os.path.join(FIX, rel))


# ---------------------------------------------------------------- known-good

def test_good_1p_measure_and_parity():
    base = _load("flash_1p/baseline.py")
    cand = _load("flash_1p/good_ag_final.py")
    rep = timing.run_measure(base, cand)
    assert rep["status"] == "PASS", rep["anomalies"]
    assert rep["timing"]["pooled"]["speedup_p50"] > 1.5
    # fp32 oracle needs per-batch chunking at this op point (17 GB full-shape)
    prep = parity.run_parity(base, cand, seeds=(42, 43), chunk={0: 0, 1: 0, 2: 0})
    assert prep["status"] == "PASS", prep.get("exception")


def test_good_5p_parity():
    base = _load("flex_5p/baseline.py")
    cand = _load("flex_5p/good_ag_final.py")
    rep = parity.run_parity(base, cand, seeds=(42, 43), chunk={0: 0, 1: 0, 2: 0})
    assert rep["status"] == "PASS", rep.get("exception")


def test_good_6p_parity_and_coverage():
    from kernelgate.specs import paged_attention
    base = _load("paged_6p/baseline.py")
    cand = _load("paged_6p/good_ag_final.py")
    rep = parity.run_parity(base, cand, seeds=(42, 43))
    assert rep["status"] == "PASS", rep.get("exception")
    cov = coverage.run_coverage(base, cand, paged_attention)
    assert cov["status"] == "PASS", cov


# ----------------------------------------------------------------- known-bad

def test_bad_4p_v002_coverage_bug_fails_parity():
    base = _load("sparse_4p/baseline.py")
    cand = _load("sparse_4p/bad_v002_coverage.py")
    rep = parity.run_parity(base, cand, seeds=(42,))
    assert rep["status"] == "FAIL"


def test_bad_4p_v002_coverage_bug_fails_coverage():
    from kernelgate.specs import causal_blocks
    base = _load("sparse_4p/baseline.py")
    cand = _load("sparse_4p/bad_v002_coverage.py")
    rep = coverage.run_coverage(base, cand, causal_blocks)
    assert rep["status"] == "FAIL", rep


def test_bad_4p_v013_double_scale_fails_parity():
    base = _load("sparse_4p/baseline.py")
    cand = _load("sparse_4p/bad_v013_double_scale.py")
    rep = parity.run_parity(base, cand, seeds=(42,))
    assert rep["status"] == "FAIL"


def test_bad_5p_noncompiling_fails_cleanly():
    base = _load("flex_5p/baseline.py")
    cand = _load("flex_5p/bad_v005_noncompiling.py")
    rep = parity.run_parity(base, cand, seeds=(42,), chunk={0: 0, 1: 0, 2: 0})
    assert rep["status"] == "FAIL"          # FAIL, not an unhandled crash
    assert rep.get("exception")             # traceback preserved


def test_bad_6p_gqa_aliasing_fails_coverage():
    from kernelgate.specs import paged_attention
    base = _load("paged_6p/baseline.py")
    cand = _load("paged_6p/bad_v003_gqa_aliasing.py")
    rep = coverage.run_coverage(base, cand, paged_attention)
    assert rep["status"] == "FAIL", rep
    failing = [p["name"] for p in rep["probes"] if p["status"] == "FAIL"]
    assert any("gqa" in n for n in failing), (
        failing, rep.get("exception"),
        [(p["name"], p["status"]) for p in rep["probes"]])
