import strawberry

from opt_public_server.common.utils import ModelInfo
from opt_public_server.static import core


Type = strawberry.enum(
    core.Type,
    description=ModelInfo(core.Type).gqldescription,
)
