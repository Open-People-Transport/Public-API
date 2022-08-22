from __future__ import annotations

from uuid import UUID

import inflection
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    declared_attr,
    mapped_column,
    registry,
)

from opt_public_server.common import models as common_models
from opt_public_server.common.database import (
    UUIDPK,
    Abbreviation,
    FullName,
    Latitude,
    Longitude,
    type_annotation_map,
)
from opt_public_server.static import models


class Base(MappedAsDataclass, DeclarativeBase):
    registry = registry(type_annotation_map=type_annotation_map)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return inflection.underscore(cls.__name__)


class City(Base, kw_only=True):
    id: Mapped[UUIDPK]
    name: Mapped[FullName]
    abbreviation: Mapped[Abbreviation]
    min_lat: Mapped[Latitude]
    min_lon: Mapped[Longitude]
    max_lat: Mapped[Latitude]
    max_lon: Mapped[Longitude]

    def to_model(self) -> models.City:
        return models.City(
            id=self.id,
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=common_models.Geobounds(
                min_lat=common_models.Latitude(self.min_lat),
                min_lon=common_models.Longitude(self.min_lon),
                max_lat=common_models.Latitude(self.max_lat),
                max_lon=common_models.Longitude(self.max_lon),
            ),
        )

    @classmethod
    def from_model(cls: type[City], model: models.City):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            min_lat=model.geobounds.min_lat,
            min_lon=model.geobounds.min_lon,
            max_lat=model.geobounds.max_lat,
            max_lon=model.geobounds.max_lon,
        )


class Company(Base, kw_only=True):
    id: Mapped[UUIDPK]
    name: Mapped[FullName]
    abbreviation: Mapped[Abbreviation]
    lat: Mapped[Latitude]
    lon: Mapped[Longitude]
    city_id: Mapped[UUID] = mapped_column(ForeignKey(City.id))

    def to_model(self) -> models.Company:
        return models.Company(
            id=self.id,
            name=self.name,
            abbreviation=self.abbreviation,
            geolocation=common_models.Geolocation(
                lat=common_models.Latitude(self.lat),
                lon=common_models.Longitude(self.lon),
            ),
            city_id=self.city_id,
        )

    @classmethod
    def from_model(cls: type[Company], model: models.Company):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            lat=model.geolocation.lat,
            lon=model.geolocation.lon,
            city_id=model.city_id,
        )
