from decimal import Decimal


def get_list_of_locations(records):
    locations = []
    for record in records:
        record = iter(record)
        locations.append(
            {
                'latitude': float(get_next_decimal(record)),
                'longitude': float(get_next_decimal(record))
            }
        )
    return locations


def get_next_decimal(record):
    return next(column for column in record if isinstance(column, Decimal))
