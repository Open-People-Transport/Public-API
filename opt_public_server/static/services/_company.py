from uuid import UUID

from opt_public_server.static.core import Company, CompanyRoute
from opt_public_server.static.repositories import CompanyRepository


class CompanyService:
    def __init__(self, repository: CompanyRepository) -> None:
        self.repository = repository

    def list(self) -> list[Company]:
        return self.repository.list()

    def get(self, id: UUID) -> Company:
        return self.repository.get(id)

    def add(self, model: Company) -> Company:
        self.repository.create(model)
        return self.get(model.id)

    def add_route(self, model: Company, edge: CompanyRoute) -> None:
        self.repository.add_route(model, edge)
