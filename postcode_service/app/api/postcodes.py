import requests


def include_postcodes(locations_without_postcodes):
    payload = {'geolocations': locations_without_postcodes}
    response = call_postcodesapi(payload)
    if not response:
        raise Exception("Couldn't get an expected response")
    return get_locations_with_postcodes(response)


def call_postcodesapi(payload):
    url = (
        'https://api.postcodes.io/postcodes?'
        'limit=1&filter=postcode&widesearch=true'
    )
    response = requests.post(
        url,
        json=payload,
        headers={'Content-Type': 'application/json'}
    )
    return response.json().get('result', None)


def get_locations_with_postcodes(result_set):
    locations = [
        {
            'lat': result['query']['latitude'],
            'long': result['query']['longitude'],
            'postcode': result['result'][0]['postcode'],
        }
        for result in result_set
    ]
    return locations
