from decimal import Decimal

from pydantic import BaseModel


class LocationOut(BaseModel):
    lat: Decimal
    long: Decimal
    postcode: str
