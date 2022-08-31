from uuid import UUID


from opt_public_server.common.core import (
    Abbreviation,
    FullName,
    Geobounds,
    Geolocation,
    Node,
)

from opt_public_server.common.core import Geobounds, Geolocation, Node


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
