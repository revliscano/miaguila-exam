import pytest
from databases import Database
from sqlalchemy import create_engine
import testing.postgresql

from database.setup import metadata


@pytest.fixture(scope='session')
def database_object():
    postgres = testing.postgresql.Postgresql()
    engine = create_engine(postgres.url(), echo=False)
    metadata.create_all(engine)
    database = Database(postgres.url())
    return database
