from unittest import mock

from fastapi.testclient import TestClient

from main import app, API_PREFIX
from database.repository import Repository
from api.views import add_postcodes_to_locations
from .conftests import (
    csv_file, invalid_csv_file, testing_database, populated_testing_database,
    locations_to_update, CSV_LENGTH
)


client = TestClient(app)


def test_OK_response_when_sending_valid_file(testing_database, csv_file):
    with mock.patch('api.views.add_postcodes_to_locations') as mocked_backgroud_task:
        payload = {"file": ('locations.csv', csv_file, 'multipart/form-data')}
        response = client.post(
            f'{API_PREFIX}/uploadcsv/',
            files=payload
        )
        assert response.status_code == 202
        assert response.json() == {"message": f"{CSV_LENGTH} rows copied"}


def test_ERROR_response_when_sending_invalid_file(testing_database,
                                                  invalid_csv_file):
    payload = {
        "file": ('locations.csv', invalid_csv_file, 'multipart/form-data')
    }
    response = client.post(
        f'{API_PREFIX}/uploadcsv/',
        files=payload
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect file'}


def test_backgroundtask(locations_to_update):
    with mock.patch('api.services.httpx') as mocked_httpx:
        mocked_httpx.post.return_value.json.return_value = locations_to_update
        add_postcodes_to_locations(CSV_LENGTH)
        repository = Repository()
        locations_without_postcodes = (
            repository.fetch_locations_without_postcodes()
        )
        assert len(locations_without_postcodes) == 0
