from uuid import UUID

from opt_public_server.common.repositories import Repository
from opt_public_server.static.models import City


class CityService:
    def __init__(self, repository: Repository[City]) -> None:
        self.repository = repository

    def list(self) -> list[City]:
        return self.repository.list()

    def get(self, id: UUID) -> City:
        return self.repository.get(id)

    def add(self, model: City) -> City:
        self.repository.create(model)
        return self.get(model.id)
