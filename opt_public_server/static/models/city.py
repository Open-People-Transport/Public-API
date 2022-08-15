from pydantic import Field

from opt_public_server.common.models.geography import Geobounds
from opt_public_server.common.models.node import Node


class City(Node):
    """
    A physical area that combines multiple routes, stops, and companies.
    """

    name: str = Field(min_length=4, max_length=60)
    abbreviation: str = Field(min_length=2, max_length=12)
    geobounds: Geobounds
