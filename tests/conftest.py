import pytest


@pytest.fixture()
def get_dict():
    # return 42
    return {
        'speed': 10,
        'number': 0,
        'distance': 10,
        'time': 1.0,
    }
