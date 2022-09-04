from dataclasses import dataclass
from typing import Any, TypeAlias

import strawberry
import strawberry.types
import strawberry.types.types
from strawberry.fastapi import BaseContext

from opt_public_server.static.services import (
    CityService,
    CompanyRouteService,
    CompanyService,
    RouteService,
)


@dataclass(kw_only=True, slots=True)
class Context(BaseContext):
    city_service: CityService
    company_service: CompanyService
    route_service: RouteService
    company_route_service: CompanyRouteService


Info: TypeAlias = strawberry.types.Info[Context, Any]
