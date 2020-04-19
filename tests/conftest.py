import pytest

values = [
    {'speed': 10, 'number': 0, 'distance': 10, 'time': 1.0},
    {'speed': 45, 'number': 1, 'distance': 10, 'time': float(10 / 45 + 1)},
    {'speed': 50, 'number': 5, 'distance': 50, 'time': 6.0},
    {'speed': 25, 'number': 0, 'distance': 50, 'time': 2.0},
]


@pytest.fixture(params=values)
def get_dict(request):
    return request.param
