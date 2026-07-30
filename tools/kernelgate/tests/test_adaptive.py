"""Adaptive-stopping logic — pure CPU."""
import random

from kernelgate import timing


def test_converged_constant_series():
    assert timing.check_converged([5.0] * 30)


def test_not_converged_tiny_n():
    assert not timing.check_converged([5.0])
    assert not timing.check_converged([])


def test_not_converged_high_variance():
    rng = random.Random(0)
    ts = [5.0 + rng.uniform(-2, 2) for _ in range(30)]
    assert not timing.check_converged(ts, se_target=0.001)


def test_se_rule_matches_definition():
    # 100 samples, std 0.05, mean 10 -> SE/mean = 0.05/sqrt(100)/10 = 5e-4 < 1e-3
    rng = random.Random(1)
    ts = [10.0 + rng.gauss(0, 0.05) for _ in range(100)]
    assert timing.check_converged(ts, se_target=1e-3)
    assert not timing.check_converged(ts, se_target=1e-5)


def test_adaptive_stops_at_n_min_when_quiet():
    calls = {"a": 0, "b": 0}

    def ta():
        calls["a"] += 1
        return 5.0

    def tb():
        calls["b"] += 1
        return 7.0

    tf, ts, conv = timing.adaptive_interleaved(ta, tb, n_min=30, n_max=120)
    assert conv
    assert len(tf) == len(ts) == 30
    assert calls["a"] == calls["b"] == 30  # strictly interleaved, equal legs


def test_adaptive_caps_at_n_max_when_noisy():
    rng = random.Random(2)

    def noisy():
        return 5.0 + rng.uniform(-3, 3)

    tf, ts, conv = timing.adaptive_interleaved(noisy, noisy, n_min=30, n_max=120)
    assert len(tf) == len(ts) == 120
    assert not conv


def test_adaptive_stops_between_min_and_max():
    # mildly noisy at first, then perfectly quiet: SE/mean over the full
    # series (KernelBot rule: no windowing) crosses the target before n_max
    state = {"n": 0}
    rng = random.Random(3)

    def settling():
        state["n"] += 1
        if state["n"] < 40:
            return 5.0 + rng.uniform(-0.15, 0.15)
        return 5.0

    tf, ts, conv = timing.adaptive_interleaved(settling, settling, n_min=30, n_max=1000)
    assert conv
    assert 30 < len(tf) < 1000


def test_leg_stats_fields():
    s = timing.leg_stats([1.0, 2.0, 3.0])
    assert s["n"] == 3
    assert s["p50_ms"] == 2.0
    assert s["min_ms"] == 1.0
