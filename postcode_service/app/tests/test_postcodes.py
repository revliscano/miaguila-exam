from unittest import TestCase
from unittest import mock
from api.postcodes import (
    include_postcodes,
    call_storage_service_update,
    fetch_from_storage_service
)
from api.postcodes import url as storage_service_url


assert_count_equal = TestCase().assertCountEqual


def test_include_postcodes():
    expected_result = [
        {"long": -2.08205, "lat": 51.905654, "postcode": "GL50 1PP"},
        {"long": -0.964052, "lat": 51.284118, "postcode": "RG27 9JU"}
    ]
    locations_without_postcodes = [
        {"longitude": -2.08205, "latitude": 51.905654},
        {"longitude": -0.964052, "latitude": 51.284118}
    ]
    locations_with_postcodes = include_postcodes(locations_without_postcodes)
    assert_count_equal(expected_result, locations_with_postcodes)


def test_update_locations_does_put_to_storage_service():
    with mock.patch('api.postcodes.httpx') as mocked_httpx:
        locations = [
            {"long": -2.08205, "lat": 51.905654, "postcode": "GL50 1PP"},
            {"long": -0.964052, "lat": 51.284118, "postcode": "RG27 9JU"}
        ]
        call_storage_service_update(locations)
        assert mocked_httpx.put.call_args == mock.call(
            storage_service_url + 'update/', json=locations
        )


def test_fetch_from_storage_service():
    with mock.patch('api.postcodes.httpx') as mocked_httpx:
        expected_data = [
            {"longitude": -2.08205, "latitude": 51.905654},
            {"longitude": -0.964052, "latitude": 51.284118}
        ]
        mocked_httpx.get.return_value.json.return_value = expected_data
        assert fetch_from_storage_service() == expected_data
