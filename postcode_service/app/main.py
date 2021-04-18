import sys
import os

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api.views import postcodes


API_PREFIX = '/api/v1/postcodes'


app = FastAPI()
app.include_router(postcodes, prefix=API_PREFIX, tags=['postcodes'])
