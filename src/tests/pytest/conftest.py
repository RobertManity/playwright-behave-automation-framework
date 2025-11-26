# src/tests/pytest/conftest.py
import pytest

@pytest.fixture
def browser_context_args(browser_context_args):
    
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }
