from uuid import UUID

from pydantic import BaseModel, Field, validator
from uuid6 import uuid7

from ._types import Latitude, Longitude


class Node(BaseModel):
    """
    An object with a universally unique identifier.
    """

    id: UUID = Field(default_factory=uuid7)


class Geolocation(BaseModel):
    """
    Single geographical point.
    """

    lat: Latitude
    lon: Longitude


class Geobounds(BaseModel):
    """
    Rectangular geographical bounds.
    """

    min_lat: Latitude
    min_lon: Longitude
    max_lat: Latitude
    max_lon: Longitude

    @validator("max_lat")
    def check_max_lat_is_max(cls, max_lat, values):
        if max_lat < values["min_lat"]:
            raise ValueError("Maximum latitude has to be greater than the minimum")
        return max_lat

    @validator("max_lon")
    def check_max_lon_is_max(cls, max_lon, values):
        if max_lon < values["min_lon"]:
            raise ValueError("Maximum longitude has to be greater than the minimum")
        return max_lon
