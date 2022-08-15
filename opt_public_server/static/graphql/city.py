from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql.connections import Node
from opt_public_server.common.graphql.geography import Geobounds, GeoboundsInput
from opt_public_server.common.utils import description
from opt_public_server.static.models.city import City as CityModel


@strawberry.type(description=description(CityModel))
class City(Node):
    id: UUID
    name: str
    abbreviation: str
    geobounds: Geobounds

    @classmethod
    def from_model(cls, model: CityModel):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geobounds=Geobounds.from_model(model.geobounds),
        )


@strawberry.input(description=description(CityModel))
class CityInput:
    name: str
    abbreviation: str
    geobounds: GeoboundsInput
    id: Optional[UUID] = None

    def to_model(self) -> CityModel:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return CityModel(
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=self.geobounds.to_model(),
            **kwargs,
        )
