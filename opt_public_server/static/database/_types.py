from sqlalchemy.types import Enum, TypeEngine

from opt_public_server.common.database import (
    type_annotation_map as _common_type_annotation_map,
)
from opt_public_server.static.core import Type


type_annotation_map: dict[type, TypeEngine] = _common_type_annotation_map | {
    Type: Enum(Type)
}
