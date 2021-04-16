from fastapi import APIRouter, UploadFile, File

from database.repository import Repository


postcodes = APIRouter()


@postcodes.post('/uploadcsv/')
async def upload_csvfile(file: UploadFile = File(...)):
    repository = Repository()
    repository.copy_content_of(file.file)
    return {"filename": file.filename}
