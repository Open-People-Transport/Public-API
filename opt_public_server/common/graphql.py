from dataclasses import dataclass
from typing import Any, TypeAlias

import strawberry.types
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext


@dataclass(kw_only=True, slots=True)
class Context(BaseContext):
    static_db: Session


Info: TypeAlias = strawberry.types.Info[Context, Any]
