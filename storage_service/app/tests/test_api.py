from fastapi.testclient import TestClient

from main import app
from .conftests import (
    csv_file, invalid_csv_file, testing_database, populated_testing_database,
    locations_to_update
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


def test_OK_reponse_when_fetching_rows_without_postcodes(populated_testing_database):
    response = client.get('/without-postcodes/')
    retrieved_rows = len(response.json())
    assert response.status_code == 200
    assert retrieved_rows == 100


def test_OK_reponse_when_fetching_rows_without_postcodes(testing_database):
    response = client.get('/without-postcodes/')
    assert response.status_code == 404
    assert response.json() == {
        'detail': 'No locations without postcodes were found'
    }


def test_OK_response_when_updating_locations(locations_to_update):
    response = client.put('/update/', json=locations_to_update)
    assert response.status_code == 200
    assert response.json() == {'message': '100 rows updated'}
