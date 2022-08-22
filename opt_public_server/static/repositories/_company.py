from uuid import UUID

from sqlalchemy.orm import Session

from opt_public_server.common.models import Geolocation, Latitude, Longitude
from opt_public_server.static.models import Company


class CompanyRepository:
    def __init__(self, db_session: Session) -> None:
        self.database = db_session

    def list(self) -> list[Company]:
        return [
            self.get(Company.__fields__["id"].default_factory())  # type:ignore
            for _ in range(5)
        ]

    def get(self, id: UUID) -> Company:
        return Company(
            id=id,
            name="Fake Company",
            abbreviation="fkcmp",
            geolocation=Geolocation(
                lat=Latitude(0),
                lon=Longitude(0),
            ),
            city_id=id,
        )

    def add(self, model: Company) -> Company:
        return model
