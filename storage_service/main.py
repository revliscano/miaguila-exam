from fastapi import FastAPI
from api.views import postcodes


app = FastAPI()
app.include_router(postcodes)
