from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql.connections import Node
from opt_public_server.common.graphql.geography import Geolocation, GeolocationInput
from opt_public_server.common.utils import description
from opt_public_server.static.models.company import Company as CompanyModel


@strawberry.type(description=description(CompanyModel))
class Company(Node):
    id: UUID
    name: str
    abbreviation: str
    geolocation: Geolocation

    @classmethod
    def from_model(cls, model: CompanyModel):
        return Company(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geolocation=Geolocation.from_model(model.geolocation),
        )


@strawberry.input(description=description(CompanyModel))
class CompanyInput:
    name: str
    abbreviation: str
    geolocation: GeolocationInput
    id: Optional[UUID] = None

    def to_model(self) -> CompanyModel:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return CompanyModel(
            name=self.name,
            abbreviation=self.abbreviation,
            geolocation=self.geolocation.to_model(),
            **kwargs,
        )
