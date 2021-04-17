from fastapi import FastAPI

from api.views import locations
from database.setup import data_access_layer


data_access_layer.db_init()

app = FastAPI()
app.include_router(locations)
