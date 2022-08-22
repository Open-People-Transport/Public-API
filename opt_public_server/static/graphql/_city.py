from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import Geobounds, GeoboundsInput, Node
from opt_public_server.common.utils import description
from opt_public_server.static import models


@strawberry.type(description=description(models.City))
class City(Node):
    id: UUID
    name: str
    abbreviation: str
    geobounds: Geobounds

    @classmethod
    def from_model(cls, model: models.City):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geobounds=Geobounds.from_model(model.geobounds),
        )


@strawberry.input(description=description(models.City))
class CityInput:
    name: str
    abbreviation: str
    geobounds: GeoboundsInput
    id: Optional[UUID] = None

    def to_model(self) -> models.City:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return models.City(
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=self.geobounds.to_model(),
            **kwargs,
        )
