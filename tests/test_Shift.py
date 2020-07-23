import pytest
from src.Dove import Dove
from src.Shift import create_doves, get_answer, get_parse, get_shift


@pytest.mark.parametrize(
    ('first', 'second', 'parser'),
    [
        (
            '3 10',
            '10 45 50',
            {'count': '3', 'distance': '10', 'speeds': ['10', '45', '50']},
        )
    ],
)
def test_get_parse(first, second, parser):
    assert get_parse(first, second) == parser


@pytest.mark.parametrize(
    ('count', 'distance', 'speeds', 'doves'),
    [('3', '10', ['10', '45', '50'], [Dove(10, 0), Dove(45, 1), Dove(50, 2)])],
)
def test_create_doves(count, distance, speeds, doves):
    assert print(create_doves(count, distance, speeds)) == print(doves)


@pytest.mark.parametrize(
    ('doves', 'result'), [([Dove(10, 0), Dove(45, 1), Dove(50, 2)], 0)]
)
def test_get_shift(doves, result):
    assert get_shift(doves) == result


@pytest.mark.parametrize(('first', 'second', 'result'), [('3 10', '10 45 50', 0)])
def test_get_answer(first, second, result):
    assert get_answer(first, second) == result
