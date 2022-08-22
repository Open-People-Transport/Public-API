from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import Geolocation, GeolocationInput, Node
from opt_public_server.common.utils import description
from opt_public_server.static import models


@strawberry.type(description=description(models.Company))
class Company(Node):
    id: UUID
    name: str
    abbreviation: str
    geolocation: Geolocation

    @classmethod
    def from_model(cls, model: models.Company):
        return Company(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geolocation=Geolocation.from_model(model.geolocation),
        )


@strawberry.input(description=description(models.Company))
class CompanyInput:
    name: str
    abbreviation: str
    geolocation: GeolocationInput
    city_id: UUID
    id: Optional[UUID] = None

    def to_model(self) -> models.Company:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return models.Company(
            name=self.name,
            abbreviation=self.abbreviation,
            geolocation=self.geolocation.to_model(),
            city_id=self.city_id,
            **kwargs,
        )
