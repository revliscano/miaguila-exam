from fastapi import FastAPI
from database.setup import metadata, database, engine


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    print('Strting up--')
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
