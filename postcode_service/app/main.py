import sys
import os

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI
from api.views import postcodes


app = FastAPI()
app.include_router(postcodes, prefix='/api/v1/postcodes', tags=['postcodes'])
