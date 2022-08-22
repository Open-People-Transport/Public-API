import strawberry

from opt_public_server.common.graphql import Connection, Edge, Info
from opt_public_server.static.services import CityService, CompanyService

from ._city import City
from ._company import Company


@strawberry.type
class Query:
    @strawberry.field
    def cities(self, info: Info) -> Connection[City]:
        models = CityService.from_graphql_info(info).list()
        nodes = map(City.from_model, models)
        edges = list(map(lambda node: Edge[City](node=node), nodes))
        connection = Connection[City](count=len(edges), edges=edges)
        return connection

    @strawberry.field
    def companies(self, info: Info) -> Connection[Company]:
        models = CompanyService.from_graphql_info(info).list()
        nodes = map(Company.from_model, models)
        edges = list(map(lambda node: Edge[Company](node=node), nodes))
        connection = Connection[Company](count=len(edges), edges=edges)
        return connection
