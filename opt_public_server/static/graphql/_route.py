from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import NamePrefix, Node, ShorterName
from opt_public_server.common.utils import ModelInfo
from opt_public_server.static import core

from ._types import Type


@strawberry.type(description=ModelInfo(core.Route).gqldescription)
class Route(Node):
    id: UUID
    number: ShorterName
    number_prefix: NamePrefix
    type: Type

    @classmethod
    def from_model(cls, model: core.Route):
        return Route(
            id=model.id,
            number=model.number,
            number_prefix=model.number_prefix,
            type=model.type,
        )


@strawberry.input(description=ModelInfo(core.CompanyRoute).gqldescription)
class RouteCompanyInput:
    company_id: UUID

    def to_model(self, route_id: UUID) -> core.CompanyRoute:
        return core.CompanyRoute(
            company_id=self.company_id,
            route_id=route_id,
        )


@strawberry.input(description=ModelInfo(core.Route).gqldescription)
class RouteInput:
    number: ShorterName
    number_prefix: NamePrefix
    type: Type
    city_id: UUID
    company_edges: list[RouteCompanyInput]
    id: Optional[UUID] = None

    def to_model(self) -> core.Route:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return core.Route(
            number=self.number,
            number_prefix=self.number_prefix,
            type=self.type,
            city_id=self.city_id,
            **kwargs,
        )
