import strawberry

from opt_public_server.common import core
from opt_public_server.common.utils import description


FullName = strawberry.scalar(
    core.FullName,
    description=description(core.FullName),
)

Abbreviation = strawberry.scalar(
    core.Abbreviation,
    description=description(core.Abbreviation),
)


Latitude = strawberry.scalar(
    core.Latitude,
    description=description(core.Latitude),
    serialize="{:8.6f}".format,
    parse_literal=lambda l: core.Latitude(l.value),
)


Longitude = strawberry.scalar(
    core.Longitude,
    description=description(core.Longitude),
    serialize="{:9.6f}".format,
    parse_literal=lambda l: core.Longitude(l.value),
)
