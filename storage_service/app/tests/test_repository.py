import pytest
from database.repository import Repository
from .conftests import (
    csv_file, invalid_csv_file, testing_database, CSV_LENGTH,
    populated_testing_database, locations_to_update
)
from psycopg2.errors import BadCopyFileFormat


def test_copy_csv_to_database(testing_database, csv_file):
    repository = Repository()
    repository.copy_content_of(csv_file)
    assert len(repository) == CSV_LENGTH


def test_exception_raised_with_invalid_csv(testing_database, invalid_csv_file):
    with pytest.raises(BadCopyFileFormat):
        repository = Repository()
        repository.copy_content_of(invalid_csv_file)


def test_retrieves_100_rows_batch(populated_testing_database):
    repository = Repository()
    batch = repository.fetch_locations_without_postcodes()
    assert len(batch) == 100


def test_update_rows(locations_to_update):
    repository = Repository()
    number_of_updated_rows = repository.update(locations_to_update)
    rows_without_postcodes = len(
        repository.fetch_locations_without_postcodes()
    )
    assert number_of_updated_rows == 100
    assert rows_without_postcodes == CSV_LENGTH - len(locations_to_update)
