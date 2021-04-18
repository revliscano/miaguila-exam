from decimal import Decimal
from api.utils import get_list_of_locations


def test_location_out():
    expected_data = [
        {"longitude": -3.578946, "latitude": 51.186390},
        {"longitude": -3.785618, "latitude": 50.315855}
    ]
    data_from_database = [
        (1, None, Decimal('51.186390'), Decimal('-3.578946')),
        (2, None, Decimal('50.315855'), Decimal('-3.785618'))
    ]
    locations = get_list_of_locations(data_from_database)
    assert expected_data == locations
