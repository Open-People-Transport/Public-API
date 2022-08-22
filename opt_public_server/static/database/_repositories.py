from uuid import UUID

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from opt_public_server.common.repositories import Repository
from opt_public_server.static import models

from ._models import City, Company


class CityRepository(Repository[models.City]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[models.City]:
        stmt = select(City)
        scalars = self.session.execute(stmt).scalars()
        models = list(map(City.to_model, scalars))
        return models

    def get(self, id: UUID) -> models.City:
        stmt = select(City).where(City.id == id)
        scalar = self.session.execute(stmt).scalar_one()
        model = scalar.to_model()
        return model

    def create(self, model: models.City) -> None:
        scalar = City.from_model(model)
        self.session.add(scalar)
        self.session.commit()

    def delete(self, id: UUID) -> None:
        stmt = delete(City).where(City.id == id)
        self.session.execute(stmt)


class CompanyRepository(Repository[models.Company]):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list(self) -> list[models.Company]:
        stmt = select(Company)
        scalars = self.session.execute(stmt).scalars()
        models = list(map(Company.to_model, scalars))
        return models

    def get(self, id: UUID) -> models.Company:
        stmt = select(Company).where(Company.id == id)
        scalar = self.session.execute(stmt).scalar_one()
        model = scalar.to_model()
        return model

    def create(self, model: models.Company) -> None:
        scalar = Company.from_model(model)
        self.session.add(scalar)
        self.session.commit()

    def delete(self, id: UUID) -> None:
        stmt = delete(Company).where(Company.id == id)
        self.session.execute(stmt)
