import pytest

from main import addition

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (2, 2, 4)
    ]
)
def test_addition(a: int, b : int, expected: int) -> None:
    assert addition(a, b) == expected
