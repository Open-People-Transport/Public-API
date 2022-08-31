from uuid import UUID

from pydantic import BaseModel

from opt_public_server.common.core import (
    Abbreviation,
    FullName,
    Geobounds,
    Geolocation,
    NamePrefix,
    Node,
    ShorterName,
)

from ._types import Type


class City(Node):
    """
    A physical area that combines multiple routes, stops, and companies.
    """

    name: FullName
    abbreviation: Abbreviation
    geobounds: Geobounds


class Company(Node):
    """
    An organization that owns a fleet of vehicles and serves transport routes.
    """

    name: FullName
    abbreviation: Abbreviation
    geolocation: Geolocation
    city_id: UUID


class Route(Node):
    """
    A line that passes through multple stops.
    Each stop is located at a unique distance along a route.
    Serviced by one or more companies.
    """

    number: ShorterName
    number_prefix: NamePrefix
    type: Type
    city_id: UUID


class CompanyRoute(BaseModel):
    """
    A link between a company and a route.
    """

    company_id: UUID
    route_id: UUID
