from uuid import UUID

import strawberry

from opt_public_server.common.graphql import Connection, Edge, Info

from ._city import City
from ._company import Company
from ._route import Route


@strawberry.type
class Query:
    @strawberry.field
    def cities(self, info: Info) -> Connection[City]:
        models = info.context.city_service.list()
        nodes = list(map(City.from_model, models))
        edges = list(map(lambda node: Edge[City](node=node), nodes))
        connection = Connection[City](count=len(edges), nodes=nodes, edges=edges)
        return connection

    @strawberry.field
    def companies(self, info: Info) -> Connection[Company]:
        models = info.context.company_service.list()
        nodes = list(map(Company.from_model, models))
        edges = list(map(lambda node: Edge[Company](node=node), nodes))
        connection = Connection[Company](count=len(edges), nodes=nodes, edges=edges)
        return connection

    @strawberry.field
    def routes(self, info: Info) -> Connection[Route]:
        models = info.context.route_service.list()
        nodes = list(map(Route.from_model, models))
        edges = list(map(lambda node: Edge[Route](node=node), nodes))
        connection = Connection[Route](count=len(edges), nodes=nodes, edges=edges)
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

    @strawberry.field
    def route(self, id: UUID, info: Info) -> Edge[Route]:
        model = info.context.route_service.get(id)
        node = Route.from_model(model)
        edge = Edge(node=node)
        return edge
