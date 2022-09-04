import strawberry

from opt_public_server.common import core
from opt_public_server.common.utils import ModelInfo


FullName = strawberry.scalar(
    core.FullName,
    description=ModelInfo(core.FullName).gqldescription,
)

Abbreviation = strawberry.scalar(
    core.Abbreviation,
    description=ModelInfo(core.Abbreviation).gqldescription,
)


ShorterName = strawberry.scalar(
    core.ShorterName,
    description=ModelInfo(core.ShorterName).gqldescription,
)

NamePrefix = strawberry.scalar(
    core.NamePrefix,
    description=ModelInfo(core.NamePrefix).gqldescription,
)


Latitude = strawberry.scalar(
    core.Latitude,
    description=ModelInfo(core.Latitude).gqldescription,
    serialize="{:8.6f}".format,
    parse_literal=lambda l: core.Latitude(l.value),
)


Longitude = strawberry.scalar(
    core.Longitude,
    description=ModelInfo(core.Longitude).gqldescription,
    serialize="{:9.6f}".format,
    parse_literal=lambda l: core.Longitude(l.value),
)
