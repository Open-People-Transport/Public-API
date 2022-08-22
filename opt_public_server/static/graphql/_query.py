from uuid import UUID

import strawberry

from opt_public_server.common.graphql import Connection, Edge, Info

from ._city import City
from ._company import Company


@strawberry.type
class Query:
    @strawberry.field
    def cities(self, info: Info) -> Connection[City]:
        models = info.context.city_service.list()
        nodes = map(City.from_model, models)
        edges = list(map(lambda node: Edge[City](node=node), nodes))
        connection = Connection[City](count=len(edges), edges=edges)
        return connection

    @strawberry.field
    def companies(self, info: Info) -> Connection[Company]:
        models = info.context.company_service.list()
        nodes = map(Company.from_model, models)
        edges = list(map(lambda node: Edge[Company](node=node), nodes))
        connection = Connection[Company](count=len(edges), edges=edges)
        return connection

    @strawberry.field
    def city(self, id: UUID, info: Info) -> Edge[City]:
        model = info.context.city_service.get(id)
        node = City.from_model(model)
        edge = Edge(node=node)
        return edge

    @strawberry.field
    def company(self, id: UUID, info: Info) -> Edge[Company]:
        model = info.context.company_service.get(id)
        node = Company.from_model(model)
        edge = Edge(node=node)
        return edge
