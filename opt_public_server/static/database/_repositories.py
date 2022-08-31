from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from opt_public_server.common.repositories import Repository
from opt_public_server.static import core

from ._models import City, Company


class CityRepository(Repository[core.City]):
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


class CompanyRepository(Repository[core.Company]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[core.Company]:
        stmt = select(Company)
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
