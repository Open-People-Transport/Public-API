from typing import Optional
from uuid import UUID

from opt_public_server.static.core import CompanyRoute, Route
from opt_public_server.static.repositories import RouteRepository


class RouteService:
    def __init__(self, repository: RouteRepository) -> None:
        self.repository = repository

    def list(self, city_id: Optional[UUID] = None) -> list[Route]:
        return self.repository.list(city_id=city_id)

    def get(self, id: UUID) -> Route:
        return self.repository.get(id)

    def add(self, model: Route) -> Route:
        self.repository.create(model)
        return self.get(model.id)

    def add_company(self, model: Route, edge: CompanyRoute) -> None:
        self.repository.add_company(model, edge)
