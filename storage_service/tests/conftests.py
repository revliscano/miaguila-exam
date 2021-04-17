from io import StringIO
import random

import pytest
import testing.postgresql

from database.setup import data_access_layer


Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True)
CSV_LENGTH = 10


@pytest.fixture(scope='session')
def testing_database():
    postgres = Postgresql()
    data_access_layer.db_init(postgres.url())
    yield data_access_layer
    postgres.stop()


@pytest.fixture(scope='function')
def csv_file():
    header = 'lat,long\r\n'
    rows = '\r\n'.join(
        f'{get_random_latitude()}, {get_random_longitude()}'
        for _ in range(CSV_LENGTH)
    )
    return StringIO(header + rows)


def get_random_latitude():
    decimal_part = round(random.random(), ndigits=6)
    integer_part = random.randint(50, 54)
    return integer_part + decimal_part


def get_random_longitude():
    decimal_part = round(random.random(), ndigits=6)
    integer_part = random.randint(-6, -1)
    return integer_part + decimal_part


@pytest.fixture(scope='function')
def invalid_csv_file():
    file = StringIO(
        'lat,lon\r\n'
        '52.923454,-1.474217\r\n'
        '0\r\n'
        '50.871446,-0.729985\r\n'
    )
    return file
