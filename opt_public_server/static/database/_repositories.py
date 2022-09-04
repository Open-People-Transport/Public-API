from typing import Optional
from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from opt_public_server.static import core, repositories

from ._models import City, Company, CompanyRoute, Route


class CityRepository(repositories.CityRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[core.City]:
        stmt = select(City)
        scalars = self.session.execute(stmt).scalars()
        models = list(map(City.to_model, scalars))
        return models

    def get(self, id: UUID) -> core.City:
        stmt = select(City).where(City.id == id)
        scalar = self.session.execute(stmt).scalar_one()
        model = scalar.to_model()
        return model

    def create(self, model: core.City) -> None:
        scalar = City.from_model(model)
        self.session.add(scalar)
        self.session.commit()

    def delete(self, id: UUID) -> None:
        stmt = delete(City).where(City.id == id)
        self.session.execute(stmt)


class CompanyRepository(repositories.CompanyRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self, city_id: Optional[UUID] = None) -> list[core.Company]:
        stmt = select(Company)
        if city_id is not None:
            stmt = stmt.where(Company.city_id == city_id)
        scalars = self.session.execute(stmt).scalars()
        models = list(map(Company.to_model, scalars))
        return models

    def get(self, id: UUID) -> core.Company:
        stmt = select(Company).where(Company.id == id)
        scalar = self.session.execute(stmt).scalar_one()
        model = scalar.to_model()
        return model

    def create(self, model: core.Company) -> None:
        scalar = Company.from_model(model)
        self.session.add(scalar)
        self.session.commit()

    def delete(self, id: UUID) -> None:
        stmt = delete(Company).where(Company.id == id)
        self.session.execute(stmt)

    def add_route(self, model: core.Company, edge: core.CompanyRoute) -> None:
        scalar = CompanyRoute.from_model(edge)
        self.session.add(scalar)
        self.session.commit()


class RouteRepository(repositories.RouteRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self, city_id: Optional[UUID] = None) -> list[core.Route]:
        stmt = select(Route)
        if city_id is not None:
            stmt = stmt.where(Route.city_id == city_id)
        scalars = self.session.execute(stmt).scalars()
        models = list(map(Route.to_model, scalars))
        return models

    def get(self, id: UUID) -> core.Route:
        stmt = select(Route).where(Route.id == id)
        scalar = self.session.execute(stmt).scalar_one()
        model = scalar.to_model()
        return model

    def create(self, model: core.Route) -> None:
        scalar = Route.from_model(model)
        self.session.add(scalar)
        self.session.commit()

    def delete(self, id: UUID) -> None:
        stmt = delete(Route).where(Route.id == id)
        self.session.execute(stmt)

    def add_company(self, model: core.Route, edge: core.CompanyRoute) -> None:
        scalar = CompanyRoute.from_model(edge)
        self.session.add(scalar)
        self.session.commit()
