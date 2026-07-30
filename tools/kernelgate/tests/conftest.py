import os

# CPU-portable by default: unless explicitly running the TPU suite, force the
# CPU backend BEFORE any test imports jax (a TPU host would otherwise grab
# chips for the pure-logic tests).
ON_TPU = os.environ.get("KGATE_TPU") == "1"
if not ON_TPU:
    os.environ.setdefault("JAX_PLATFORMS", "cpu")

import pytest  # noqa: E402

FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

collect_ignore_glob = ["fixtures/*"]


def pytest_collection_modifyitems(config, items):
    if ON_TPU:
        return
    skip = pytest.mark.skip(reason="TPU required — run with KGATE_TPU=1 on a TPU host")
    for item in items:
        if "tpu" in item.keywords:
            item.add_marker(skip)


@pytest.fixture
def fixtures_dir():
    return FIXTURES
