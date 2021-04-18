import os
import requests


POSTCODE_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/postcodes/'
url = os.getenv('POSTCODE_SERVICE_HOST_URL') or POSTCODE_SERVICE_HOST_URL


def get_postcodes_for(locations):
    response = requests.post(f'{url}combine/', json=locations)
    return response.json()
