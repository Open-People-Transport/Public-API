from typing import Optional
from uuid import UUID

from opt_public_server.static.core import CompanyRoute
from opt_public_server.static.repositories import CompanyRouteRepository


class CompanyRouteService:
    def __init__(self, repository: CompanyRouteRepository) -> None:
        self.repository = repository

    def list(
        self,
        company_id: Optional[UUID] = None,
        route_id: Optional[UUID] = None,
    ) -> list[CompanyRoute]:
        return self.repository.list(company_id=company_id, route_id=route_id)

    def get(self, company_id: UUID, route_id: UUID) -> CompanyRoute:
        return self.repository.get(company_id=company_id, route_id=route_id)

    def add(self, model: CompanyRoute) -> CompanyRoute:
        self.repository.create(model)
        return self.get(company_id=model.company_id, route_id=model.route_id)
