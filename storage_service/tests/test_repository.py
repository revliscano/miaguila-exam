import pytest
from database.repository import Repository
from .conftests import (
    csv_file, invalid_csv_file, testing_database, CSV_LENGTH
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
