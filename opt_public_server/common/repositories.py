from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel


Model = TypeVar("Model", bound=BaseModel)


class Repository(ABC, Generic[Model]):
    @abstractmethod
    def list(self) -> list[Model]:
        ...

    @abstractmethod
    def get(self, id: UUID) -> Model:
        ...

    @abstractmethod
    def create(self, model: Model) -> None:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> None:
        ...
