import pytest
from fastapi.testclient import TestClient

from main import app
from database.repository import Repository
from .conftests import csv_file, invalid_csv_file, testing_database
from psycopg2.errors import BadCopyFileFormat


client = TestClient(app)


def test_copy_csv_to_database(testing_database, csv_file):
    repository = Repository()
    repository.copy_content_of(csv_file)
    assert len(repository) == 3


def test_exception_raised_with_invalid_csv(testing_database, invalid_csv_file):
    with pytest.raises(BadCopyFileFormat):
        repository = Repository()
        repository.copy_content_of(invalid_csv_file)


def test_OK_RESPONSE_when_sending_valid_file(testing_database, csv_file):
    payload = {"file": ('locations.csv', csv_file, 'multipart/form-data')}
    response = client.post(
        '/uploadcsv/',
        files=payload
    )
    assert response.status_code == 200
    assert response.json() == {"filename": "locations.csv"}
