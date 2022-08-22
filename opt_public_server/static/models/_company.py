from uuid import UUID

from pydantic import Field

from opt_public_server.common.models import Geolocation, Node


class Company(Node):
    """
    An organization that owns a fleet of vehicles and serves transport routes.
    """

    name: str = Field(min_length=4, max_length=60)
    abbreviation: str = Field(min_length=2, max_length=12)
    geolocation: Geolocation
    city_id: UUID
