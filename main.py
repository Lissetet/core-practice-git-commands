import pytest


def always_returns_true():
    if False:
        return False
    return True


def test_always_returns_true():
    assert always_returns_true()
