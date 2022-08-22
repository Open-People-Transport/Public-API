from uuid import UUID

from sqlalchemy.orm import Session

from opt_public_server.common.models import Geobounds, Latitude, Longitude
from opt_public_server.static.models import City


class CityRepository:
    def __init__(self, db_session: Session) -> None:
        self.database = db_session

    def list(self) -> list[City]:
        return [
            self.get(City.__fields__["id"].default_factory())  # type:ignore
            for _ in range(3)
        ]

    def get(self, id: UUID) -> City:
        return City(
            id=id,
            name="Fake City",
            abbreviation="fkct",
            geobounds=Geobounds(
                min_lat=Latitude(-10),
                min_lon=Longitude(-10),
                max_lat=Latitude(10),
                max_lon=Longitude(10),
            ),
        )

    def add(self, model: City) -> City:
        return model
