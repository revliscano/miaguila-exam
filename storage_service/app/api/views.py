from typing import List

from fastapi import APIRouter, UploadFile, File, HTTPException
from psycopg2.errors import BadCopyFileFormat

from database.repository import Repository
from api.models import LocationOut


locations = APIRouter()


@locations.post('/uploadcsv/', status_code=202)
async def upload_csvfile(file: UploadFile = File(...)):
    try:
        repository = Repository()
        rows_copied = repository.copy_content_of(file.file)
        return {"message": f"{rows_copied} rows copied"}
    except BadCopyFileFormat:
        raise HTTPException(
            status_code=400, detail="Incorrect file"
        )


@locations.get('/without-postcodes/', response_model=List[LocationOut])
async def fetch_locations_without_postcodes():
    repository = Repository()
    locations = repository.fetch_locations_without_postcodes()

    if not locations:
        raise HTTPException(
            status_code=404, detail="No locations without postcodes were found"
        )

    return locations


@locations.put('/update/')
async def update_locations(locations: List[dict]):
    repository = Repository()
    locations_updated = repository.update(locations)
    return {'message': f'{locations_updated} rows updated'}
