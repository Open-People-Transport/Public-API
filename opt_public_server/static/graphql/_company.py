from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import (
    Abbreviation,
    FullName,
    Geolocation,
    GeolocationInput,
    Node,
)
from opt_public_server.common.utils import description
from opt_public_server.static import core


@strawberry.type(description=description(core.Company))
class Company(Node):
    id: UUID
    name: FullName
    abbreviation: Abbreviation
    geolocation: Geolocation

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
