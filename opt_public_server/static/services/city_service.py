from uuid import UUID

from opt_public_server.common.graphql import Info
from opt_public_server.static.models.city import City
from opt_public_server.static.repositories.city_repository import CityRepository


class CityService:
    def __init__(self, repository: CityRepository) -> None:
        self.repo = repository

    def list(self) -> list[City]:
        return self.repo.list()

    def get(self, id: UUID) -> City:
        return self.repo.get(id)

    def add(self, model: City) -> City:
        return self.repo.add(model)

    @classmethod
    def from_graphql_info(cls, info: Info):
        repository = CityRepository(db_session=info.context.static_db)
        return cls(repository=repository)
