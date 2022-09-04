from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import (
    Abbreviation,
    Connection,
    Edge,
    FullName,
    Geolocation,
    GeolocationInput,
    Info,
    Node,
)
from opt_public_server.common.utils import description
from opt_public_server.static import core

from ._route import Route


@strawberry.type(description=description(core.Company))
class Company(Node):
    id: UUID
    name: FullName
    abbreviation: Abbreviation
    geolocation: Geolocation

    @strawberry.field(description="Transport routes that this company operates")
    def routes(self, info: Info) -> Connection[Route]:
        edge_models = info.context.company_route_service.list(company_id=self.id)
        node_models = (
            info.context.route_service.get(edge.route_id) for edge in edge_models
        )
        nodes = list(map(Route.from_model, node_models))
        edges = list(map(lambda node: Edge[Route](node=node), nodes))
        connection = Connection[Route](count=len(edges), nodes=nodes, edges=edges)
        return connection

    @classmethod
    def from_model(cls, model: core.Company):
        return Company(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geolocation=Geolocation.from_model(model.geolocation),
        )


@strawberry.input(description=description(core.Company))
class CompanyInput:
    name: FullName
    abbreviation: Abbreviation
    geolocation: GeolocationInput
    city_id: UUID
    id: Optional[UUID] = None

    def to_model(self) -> core.Company:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return core.Company(
            name=self.name,
            abbreviation=self.abbreviation,
            geolocation=self.geolocation.to_model(),
            city_id=self.city_id,
            **kwargs,
        )
