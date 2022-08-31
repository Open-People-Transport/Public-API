import strawberry

from opt_public_server.common.utils import description
from opt_public_server.static import core


Type = strawberry.enum(
    core.Type,
    description=description(core.Type),
)
