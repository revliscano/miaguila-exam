from typing import List, Mapping

from fastapi import APIRouter

from api.models import LocationOut
from api.postcodes import include_postcodes


postcodes = APIRouter()


@postcodes.post('/combine/', response_model=List[LocationOut])
async def combine_locations_with_postcodes(payload: List[Mapping[str, float]]):
    return include_postcodes(payload)
