import pytest
from src.get_shifts import get_shifts


@pytest.mark.parametrize(
    ('first_string', 'second_string', 'result'),
    [('3 10', '10 45 50', 0), ('3 50', '10 20 50', 3), ('1 50', '10', 0)],
)
def test_get_shifts(first_string, second_string, result):
    assert get_shifts(first_string, second_string) == result
