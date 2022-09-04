from pathlib import Path
from typing import Optional

from pydantic import parse_file_as

from opt_public_server.static.core import City, Company, CompanyRoute, Route
from opt_public_server.static.repositories import (
    CityRepository,
    CompanyRepository,
    RouteRepository,
)


_initial_data = parse_file_as(
    dict[str, list[City | Company | Route]], Path(__file__) / ".." / "data.json"
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

    def add_route(self, model: Company, edge: CompanyRoute) -> None:
        raise NotImplementedError


class RouteTestRepository(_TestRepository, RouteRepository):
    def __init__(self) -> None:
        super().__init__(_initial_data["routes"])

    def add_company(self, model: Route, edge: CompanyRoute) -> None:
        raise NotImplementedError
