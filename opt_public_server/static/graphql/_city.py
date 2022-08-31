from typing import Any, Optional
from uuid import UUID

import strawberry

from opt_public_server.common.graphql import (
    Abbreviation,
    FullName,
    Geobounds,
    GeoboundsInput,
    Node,
)
from opt_public_server.common.utils import description
from opt_public_server.static import core


@strawberry.type(description=description(core.City))
class City(Node):
    id: UUID
    name: FullName
    abbreviation: Abbreviation
    geobounds: Geobounds

    @classmethod
    def from_model(cls, model: core.City):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            geobounds=Geobounds.from_model(model.geobounds),
        )


@strawberry.input(description=description(core.City))
class CityInput:
    name: FullName
    abbreviation: Abbreviation
    geobounds: GeoboundsInput
    id: Optional[UUID] = None

    def to_model(self) -> core.City:
        kwargs = dict[str, Any]()
        if self.id:
            kwargs.update(id=self.id)
        return core.City(
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=self.geobounds.to_model(),
            **kwargs,
        )
