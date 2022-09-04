from pathlib import Path
from typing import Optional
from uuid import UUID

from pydantic import parse_file_as

from opt_public_server.common.utils import multifilter
from opt_public_server.static.core import City, Company, CompanyRoute, Route
from opt_public_server.static.repositories import (
    CityRepository,
    CompanyRepository,
    CompanyRouteRepository,
    RouteRepository,
)


_initial_data = parse_file_as(
    dict[str, list[City | Company | Route | CompanyRoute]],
    Path(__file__) / ".." / "data.json",
)


class _TestRepository:
    def __init__(self, initial_models: Optional[list] = None) -> None:
        self._data = {model.id: model.copy() for model in (initial_models or [])}

    def list(self):
        return list(self._data.values())

    def get(self, id):
        return self._data.get(id)

    def create(self, model):
        assert model.id not in self._data
        self._data[model.id] = model

    def delete(self, id):
        return self._data.pop(id)


class CityTestRepository(_TestRepository, CityRepository):
    def __init__(self) -> None:
        super().__init__(_initial_data["cities"])


class CompanyTestRepository(_TestRepository, CompanyRepository):
    def __init__(self) -> None:
        super().__init__(_initial_data["companies"])

    def list(self, city_id: Optional[UUID] = None):
        filters = []
        if city_id is not None:
            filters.append(lambda c: c.city_id == city_id)
        return list(multifilter(filters, self._data.values()))

    def add_route(self, model: Company, edge: CompanyRoute) -> None:
        raise NotImplementedError


class RouteTestRepository(_TestRepository, RouteRepository):
    def __init__(self) -> None:
        super().__init__(_initial_data["routes"])

    def list(self, city_id: Optional[UUID] = None):
        filters = []
        if city_id is not None:
            filters.append(lambda r: r.city_id == city_id)
        return list(multifilter(filters, self._data.values()))

    def add_company(self, model: Route, edge: CompanyRoute) -> None:
        raise NotImplementedError


class CompanyRouteTestRepository(CompanyRouteRepository):
    def __init__(self) -> None:
        initial_models: list[CompanyRoute] = _initial_data[
            "company_routes"
        ]  # type: ignore
        self._data = {
            (model.company_id, model.route_id): model.copy()
            for model in (initial_models or [])
        }

    def list(self, company_id: Optional[UUID] = None, route_id: Optional[UUID] = None):
        filters = []
        if company_id is not None:
            filters.append(lambda cr: cr.company_id == company_id)
        if route_id is not None:
            filters.append(lambda cr: cr.route_id == route_id)
        return list(multifilter(filters, self._data.values()))

    def get(self, company_id, route_id):
        return self._data.get((company_id, route_id))

    def create(self, model):
        assert (model.company_id, model.route_id) not in self._data
        self._data[(model.company_id, model.route_id)] = model

    def delete(self, company_id, route_id):
        return self._data.pop((company_id, route_id))
