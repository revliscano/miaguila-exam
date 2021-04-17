from fastapi.testclient import TestClient

from main import app
from .conftests import (
    csv_file, invalid_csv_file, testing_database
)


client = TestClient(app)


def test_OK_response_when_sending_valid_file(testing_database, csv_file):
    payload = {"file": ('locations.csv', csv_file, 'multipart/form-data')}
    response = client.post(
        '/uploadcsv/',
        files=payload
    )
    assert response.status_code == 200
    assert response.json() == {"filename": "locations.csv"}


def test_ERROR_response_when_sending_invalid_file(testing_database,
                                                  invalid_csv_file):
    payload = {
        "file": ('locations.csv', invalid_csv_file, 'multipart/form-data')
    }
    response = client.post(
        '/uploadcsv/',
        files=payload
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect file'}
