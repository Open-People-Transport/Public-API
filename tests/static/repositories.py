from uuid import UUID

from opt_public_server.common.core import Geobounds, Geolocation, Latitude, Longitude
from opt_public_server.static.core import City, Company, CompanyRoute, Route
from opt_public_server.static.repositories import (
    CityRepository,
    CompanyRepository,
    RouteRepository,
)


class CityTestRepository(CityRepository):
    def __init__(self) -> None:
        self._list = [
            City(
                id=UUID("0182c670-fe8e-7686-b0bc-569973c69c40"),
                name="Test City 1",
                abbreviation="testcity1",
                geobounds=Geobounds(
                    min_lat=Latitude("12.345678"),
                    min_lon=Longitude("12.345678"),
                    max_lat=Latitude("87.654321"),
                    max_lon=Longitude("87.654321"),
                ),
            ),
            City(
                id=UUID("0182c671-4f9a-7bac-8223-f92a7fe4be6d"),
                name="Test City 2",
                abbreviation="testcity2",
                geobounds=Geobounds(
                    min_lat=Latitude("12.345678"),
                    min_lon=Longitude("12.345678"),
                    max_lat=Latitude("87.654321"),
                    max_lon=Longitude("87.654321"),
                ),
            ),
        ]

    def list(self) -> list[City]:
        return list(self._list)

    def get(self, id: UUID) -> City:
        return next(filter(lambda c: c.id == id, self._list))

    def create(self, model: City) -> None:
        return self._list.append(model)

    def delete(self, id: UUID) -> None:
        return self._list.remove(self.get(id))


class CompanyTestRepository(CompanyRepository):
    def __init__(self) -> None:
        self._list = [
            Company(
                id=UUID("0182c68d-0dda-7cce-b641-c8b0a4d531d1"),
                name="Test Company 1",
                abbreviation="testcomp1",
                geolocation=Geolocation(
                    lat=Latitude("12.345678"),
                    lon=Longitude("123.456789"),
                ),
                city_id=UUID("0182c670-fe8e-7686-b0bc-569973c69c40"),
            ),
            Company(
                id=UUID("0182c68d-11a9-7584-ad76-7bcf720b8dd6"),
                name="Test Company 2",
                abbreviation="testcomp2",
                geolocation=Geolocation(
                    lat=Latitude("12.345678"),
                    lon=Longitude("123.456789"),
                ),
                city_id=UUID("0182c670-fe8e-7686-b0bc-569973c69c40"),
            ),
            Company(
                id=UUID("0182c68d-131d-770f-a41d-742ee9a19d7a"),
                name="Test Company 3",
                abbreviation="testcomp3",
                geolocation=Geolocation(
                    lat=Latitude("12.345678"),
                    lon=Longitude("123.456789"),
                ),
                city_id=UUID("0182c671-4f9a-7bac-8223-f92a7fe4be6d"),
            ),
        ]

    def list(self) -> list[Company]:
        return list(self._list)

    def get(self, id: UUID) -> Company:
        return next(filter(lambda c: c.id == id, self._list))

    def create(self, model: Company) -> None:
        return self._list.append(model)

    def delete(self, id: UUID) -> None:
        return self._list.remove(self.get(id))

    def add_route(self, model: Company, edge: CompanyRoute) -> None:
        raise NotImplementedError


class RouteTestRepository(RouteRepository):
    def __init__(self) -> None:
        self._list = [
            Route(
                id=UUID("0182f596-bce6-773d-9c2c-d0d3fbf70aab"),
                number="1",
                number_prefix="A-",
                type="BUS",
                city_id=UUID("0182c670-fe8e-7686-b0bc-569973c69c40"),
            ),
            Route(
                id=UUID("0182f596-bfce-7401-a8c5-4650dd30db4d"),
                number="2",
                number_prefix="A-",
                type="BUS",
                city_id=UUID("0182c670-fe8e-7686-b0bc-569973c69c40"),
            ),
            Route(
                id=UUID("0182f596-c115-7b83-b914-502e27815c33"),
                number="1",
                number_prefix="Tl-",
                type="TROLLEY",
                city_id=UUID("0182c671-4f9a-7bac-8223-f92a7fe4be6d"),
            ),
            Route(
                id=UUID("0182f596-c257-73e6-8c4e-0d2452fc9f10"),
                number="2",
                number_prefix="Tm-",
                type="TRAM",
                city_id=UUID("0182c671-4f9a-7bac-8223-f92a7fe4be6d"),
            ),
            Route(
                id=UUID("0182f596-c257-73e6-8c4e-0d2452fc9f10"),
                number="3",
                number_prefix="T-",
                type="MINIBUS",
                city_id=UUID("0182c671-4f9a-7bac-8223-f92a7fe4be6d"),
            ),
        ]

    def list(self) -> list[Route]:
        return list(self._list)

    def get(self, id: UUID) -> Route:
        return next(filter(lambda c: c.id == id, self._list))

    def create(self, model: Route) -> None:
        return self._list.append(model)

    def delete(self, id: UUID) -> None:
        return self._list.remove(self.get(id))

    def add_company(self, model: Route, edge: CompanyRoute) -> None:
        raise NotImplementedError
