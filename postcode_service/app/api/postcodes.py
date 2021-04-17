import os

import requests
import httpx


STORAGE_SERVICE_HOST_URL = 'http://localhost:8002/api/v1/locations/'
url = os.environ.get('STORAGE_SERVICE_HOST_URL') or STORAGE_SERVICE_HOST_URL


def put_postcodes_to_locations():
    locations_without_postcodes = fetch_from_storage_service()
    locations_with_postcodes = include_postcodes(locations_without_postcodes)
    call_storage_service_update(locations_with_postcodes)


def fetch_from_storage_service():
    response = httpx.get(f'{url}without-postcodes')
    return response.json()


def call_storage_service_update(locations_with_postcodes):
    httpx.put(
        f'{url}update/',
        json=locations_with_postcodes
    )


def include_postcodes(locations_without_postcodes):
    payload = {'geolocations': locations_without_postcodes}
    response = call_postcodesapi(payload)
    if not response:
        raise Exception("Couldn't get an expected response")
    return get_locations_with_postcodes(response)


def call_postcodesapi(payload):
    url = 'https://api.postcodes.io/postcodes?limit=1&filter=postcode'
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
