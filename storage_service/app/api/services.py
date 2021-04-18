import os
import httpx


POSTCODE_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/postcodes/'
url = os.environ.get('POSTCODE_SERVICE_HOST_URL') or POSTCODE_SERVICE_HOST_URL


def get_postcodes_for(locations):
    response = httpx.post(f'{url}combine/', json=locations)
    return response.json()
