from unittest import TestCase
from api.postcodes import include_postcodes


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
