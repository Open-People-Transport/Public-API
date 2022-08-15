from uuid import UUID

from opt_public_server.common.graphql import Info
from opt_public_server.static.models.company import Company
from opt_public_server.static.repositories.company_repository import CompanyRepository


class CompanyService:
    def __init__(self, repository: CompanyRepository) -> None:
        self.repo = repository

    def list(self) -> list[Company]:
        return self.repo.list()

    def get(self, id: UUID) -> Company:
        return self.repo.get(id)

    def add(self, model: Company) -> Company:
        return self.repo.add(model)

    @classmethod
    def from_graphql_info(cls, info: Info):
        repository = CompanyRepository(db_session=info.context.static_db)
        return cls(repository=repository)
