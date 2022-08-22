from dataclasses import dataclass
from typing import Any, TypeAlias

import strawberry
import strawberry.types
import strawberry.types.types
from strawberry.fastapi import BaseContext

from opt_public_server.static.services import CityService, CompanyService


@dataclass(kw_only=True, slots=True)
class Context(BaseContext):
    city_service: CityService
    company_service: CompanyService


Info: TypeAlias = strawberry.types.Info[Context, Any]
