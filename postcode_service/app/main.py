import sys
import os

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api.views import locations
from database.setup import data_access_layer


data_access_layer.db_init()

app = FastAPI()
app.include_router(locations, prefix='/api/v1/locations', tags=['locations'])
