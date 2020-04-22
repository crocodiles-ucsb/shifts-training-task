import pytest
from src.Task import parse_args


@pytest.mark.parametrize(
    ('args', 'result'),
    [
        (
            ['-f', '3 10', '-s', '10 45 50'],
            "Namespace(first_string='3 10', second_string='10 45 50')",
        )
    ],
)
def test_parser(args, result):
    parser = parse_args(args)
    # assert True
    assert str(parser) == result
