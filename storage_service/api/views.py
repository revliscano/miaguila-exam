from fastapi import APIRouter, UploadFile, File, HTTPException
from psycopg2.errors import BadCopyFileFormat

from database.repository import Repository


postcodes = APIRouter()


@postcodes.post('/uploadcsv/')
async def upload_csvfile(file: UploadFile = File(...)):
    try:
        repository = Repository()
        repository.copy_content_of(file.file)
        return {"filename": file.filename}
    except BadCopyFileFormat:
        raise HTTPException(
            status_code=400, detail="Incorrect file"
        )
