"""KernelGate — verification gates for TPU kernel benchmarking (CLI: kgate).

Productionizes the campaign kernel benchmarking/verification methodology:
co-measured interleaved timing (both orderings, adaptive trial count),
floor-normalized oracle parity (fp32, fp64 escalation for HIGHEST-class
baselines), spec-driven + declarative sensitivity coverage batteries,
parity-gated block-size sweeps, a 4-leg flag-fairness harness, a compile-only
config-fit sweep, speed-of-light roofline gates, tamper-evident run receipts,
and a static AST prefilter for known reward-hacking patterns.

A benchmark case is any Python module exposing the problem-module protocol:

    CONFIG        dict of operating-point parameters
    create_inputs [seed], [dtype] -> tuple of input arrays
    workload(*inputs) -> output array(s)   (entry name is resolvable/overridable)
"""

__version__ = "0.2.0"

EXIT_PASS = 0
EXIT_ADVISORY = 1   # lint findings (advisory)
EXIT_FAIL = 2       # gate failure / anomaly / invalid
