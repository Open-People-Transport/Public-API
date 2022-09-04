import strawberry
from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types

import opt_public_server.static.database
from opt_public_server.common.graphql import Context
from opt_public_server.static.database import (
    CityRepository,
    CompanyRepository,
    CompanyRouteRepository,
    RouteRepository,
)
from opt_public_server.static.graphql import (
    Mutation as StaticMutation,
    Query as StaticQuery,
)
from opt_public_server.static.services import (
    CityService,
    CompanyRouteService,
    CompanyService,
    RouteService,
)


def get_context(
    static_db: Session = Depends(opt_public_server.static.database.gen_session),
):
    return Context(
        city_service=CityService(CityRepository(static_db)),
        company_service=CompanyService(CompanyRepository(static_db)),
        route_service=RouteService(RouteRepository(static_db)),
        company_route_service=CompanyRouteService(CompanyRouteRepository(static_db)),
    )


Query = merge_types("Query", (StaticQuery,))
Mutation = merge_types("Mutation", (StaticMutation,))


schema = strawberry.Schema(query=Query, mutation=Mutation)

router = GraphQLRouter(schema=schema, context_getter=get_context, debug=True)
