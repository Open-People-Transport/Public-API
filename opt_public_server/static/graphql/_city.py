from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import (
    Abbreviation,
    Connection,
    Edge,
    FullName,
    Geobounds,
    GeoboundsInput,
    Info,
    Node,
)
from opt_public_server.common.utils import description
from opt_public_server.static import core

from ._company import Company
from ._route import Route


@strawberry.type(description=description(core.City))
class City(Node):
    id: UUID
    name: FullName
    abbreviation: Abbreviation
    geobounds: Geobounds

    @strawberry.field(description="Transport companies that operate in this city")
    def companies(self, info: Info) -> Connection[Company]:
        models = info.context.company_service.list(city_id=self.id)
        nodes = map(Company.from_model, models)
        edges = list(map(lambda node: Edge[Company](node=node), nodes))
        connection = Connection[Company](count=len(edges), edges=edges)
        return connection

    @strawberry.field(description="Transport routes in this city")
    def routes(self, info: Info) -> Connection[Route]:
        models = info.context.route_service.list(city_id=self.id)
        nodes = map(Route.from_model, models)
        edges = list(map(lambda node: Edge[Route](node=node), nodes))
        connection = Connection[Route](count=len(edges), edges=edges)
        return connection

    @classmethod
    def from_model(cls, model: core.City):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geobounds=Geobounds.from_model(model.geobounds),
        )


@strawberry.input(description=description(core.City))
class CityInput:
    name: FullName
    abbreviation: Abbreviation
    geobounds: GeoboundsInput
    id: Optional[UUID] = None

    def to_model(self) -> core.City:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return core.City(
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=self.geobounds.to_model(),
            **kwargs,
        )
