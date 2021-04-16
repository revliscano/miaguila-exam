from io import StringIO

import pytest
import testing.postgresql

from database.setup import data_access_layer


Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True)


@pytest.fixture(scope='session')
def testing_database():
    postgres = Postgresql()
    data_access_layer.db_init(postgres.url())
    yield data_access_layer
    postgres.stop()


@pytest.fixture(scope='function')
def csv_file():
    file = StringIO(
        'lat,lon\r\n'
        '52.923454,-1.474217\r\n'
        '53.457321,-2.262773\r\n'
        '50.871446,-0.729985\r\n'
    )
    return file


@pytest.fixture(scope='function')
def invalid_csv_file():
    file = StringIO(
        'lat,lon\r\n'
        '52.923454,-1.474217\r\n'
        '0\r\n'
        '50.871446,-0.729985\r\n'
    )
    return file
