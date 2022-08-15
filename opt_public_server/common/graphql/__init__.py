from dataclasses import dataclass
from typing import Any, TypeAlias

import strawberry
import strawberry.types
import strawberry.types.types
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext


@dataclass(kw_only=True, slots=True)
class Context(BaseContext):
    static_db: Session


Info: TypeAlias = strawberry.types.Info[Context, Any]
