from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from opt_public_server.static.core import City, Company, CompanyRoute, Route


class CityRepository(ABC):
    @abstractmethod
    def list(self) -> list[City]:
        ...

    @abstractmethod
    def get(self, id: UUID) -> City:
        ...

    @abstractmethod
    def create(self, model: City) -> None:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> None:
        ...


class CompanyRepository(ABC):
    @abstractmethod
    def list(self, city_id: Optional[UUID] = None) -> list[Company]:
        ...

    @abstractmethod
    def get(self, id: UUID) -> Company:
        ...

    @abstractmethod
    def create(self, model: Company) -> None:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> None:
        ...

    @abstractmethod
    def add_route(self, model: Company, edge: CompanyRoute) -> None:
        ...


class RouteRepository(ABC):
    @abstractmethod
    def list(self, city_id: Optional[UUID] = None) -> list[Route]:
        ...

    @abstractmethod
    def get(self, id: UUID) -> Route:
        ...

    @abstractmethod
    def create(self, model: Route) -> None:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> None:
        ...

    @abstractmethod
    def add_company(self, model: Route, edge: CompanyRoute) -> None:
        ...


class CompanyRouteRepository(ABC):
    @abstractmethod
    def list(
        self,
        company_id: Optional[UUID] = None,
        route_id: Optional[UUID] = None,
    ) -> list[CompanyRoute]:
        ...

    @abstractmethod
    def get(self, company_id: UUID, route_id: UUID) -> CompanyRoute:
        ...

    @abstractmethod
    def create(self, model: CompanyRoute) -> None:
        ...

    @abstractmethod
    def delete(self, company_id: UUID, route_id: UUID) -> None:
        ...
