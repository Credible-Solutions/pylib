import pytest

from pylib.sample import sample


@pytest.fixture
def user_input():
    return "hello world"


def test_sample(user_input):
    assert sample(user_input) == user_input


@pytest.mark.parametrize("user_input", ["test", "123", "abc"])
def test_sample_multiple_inputs(user_input):
    assert sample(user_input) == user_input
