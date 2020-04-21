import pytest
from src.Dove import Dove


@pytest.mark.parametrize(
    ('speed', 'number', 'distance', 'result'),
    [
        (10, 0, 10, 'Dove 0 has speed 10 km/min and it will arrive in 1.0 minute'),
        (10, 1, 50, 'Dove 1 has speed 10 km/min and it will arrive in 6.0 minute'),
    ],
)
def test_get_string(speed, number, distance, result):
    Dove.distance = distance
    dove = Dove(speed, number)
    assert str(dove) == result


def test_time(specifications):
    Dove.distance = specifications['distance']
    dove = Dove(specifications['speed'], specifications['number'])
    assert dove.time_of_way == specifications['time']
