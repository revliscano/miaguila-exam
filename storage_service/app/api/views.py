from fastapi import (
    APIRouter, UploadFile, File, HTTPException, BackgroundTasks
)
from psycopg2.errors import BadCopyFileFormat

from database.repository import Repository
from api.utils import get_list_of_locations
from api.services import get_postcodes_for


locations = APIRouter()


@locations.post('/uploadcsv/', status_code=202)
async def upload_csvfile(background_tasks: BackgroundTasks,
                         file: UploadFile = File(...)):
    try:
        repository = Repository()
        rows_copied = repository.copy_content_of(file.file)
        background_tasks.add_task(add_postcodes_to_locations, rows_copied)
        return {"message": f"{rows_copied} rows copied"}
    except BadCopyFileFormat:
        raise HTTPException(
            status_code=400, detail="Incorrect file"
        )


def add_postcodes_to_locations(rows_left):
    while rows_left > 0:
        repository = Repository()
        locations = get_list_of_locations(
            repository.fetch_locations_without_postcodes()
        )
        locations_with_postcodes = get_postcodes_for(locations)
        rows_updated = repository.update(locations_with_postcodes)
        rows_left -= rows_updated
