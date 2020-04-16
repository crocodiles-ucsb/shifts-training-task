import pytest
from src.Dove import Dove


@pytest.mark.parametrize(('dist', 'result'), [(5, 5), (0, 0)])
def test_distance(dist, result):
    Dove.distance = dist
    assert Dove.distance == result


@pytest.mark.parametrize(('count', 'result'), [(5, 5), (0, 0)])
def test_count(count, result):
    Dove.count = count
    assert Dove.count == result


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
    assert dove.__str__() == result


def test_time(get_dict):
    # assert get_dict == 42
    speed = get_dict['speed']
    number = get_dict['number']
    distance = get_dict['distance']
    time = get_dict['time']
    Dove.distance = distance
    dove = Dove(speed, number)
    assert dove.time_of_way == time
