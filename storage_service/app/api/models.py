from decimal import Decimal
from pydantic import BaseModel


class LocationOut(BaseModel):
    latitude: Decimal
    longitude: Decimal
