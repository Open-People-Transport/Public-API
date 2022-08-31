from uuid import UUID

from opt_public_server.common.repositories import Repository
from opt_public_server.static.core import Company


class CompanyService:
    def __init__(self, repository: Repository[Company]) -> None:
        self.repository = repository

    def list(self) -> list[Company]:
        return self.repository.list()

    def get(self, id: UUID) -> Company:
        return self.repository.get(id)

    def add(self, model: Company) -> Company:
        self.repository.create(model)
        return self.get(model.id)
