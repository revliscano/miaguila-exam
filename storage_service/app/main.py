import sys
import os

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api.views import locations
from database.setup import data_access_layer


API_PREFIX = '/api/v1/locations'

data_access_layer.db_init()

app = FastAPI()
app.include_router(locations, prefix=API_PREFIX, tags=['locations'])
