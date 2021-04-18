import pytest


@pytest.fixture(scope='function')
def data_from_storage_service():
    return [
        {"longitude": -2.08205, "latitude": 51.905654},
        {"longitude": -0.964052, "latitude": 51.284118}
    ]
