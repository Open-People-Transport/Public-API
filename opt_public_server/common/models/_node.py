from uuid import UUID

from pydantic import BaseModel, Field
from uuid6 import uuid7


class Node(BaseModel):
    """
    An object with a universally unique identifier.
    """

    id: UUID = Field(default_factory=uuid7)
