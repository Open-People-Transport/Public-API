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

from opt_public_server.common import core as common_core
from opt_public_server.common.core import Abbreviation, FullName, Latitude, Longitude
from opt_public_server.common.database import UUIDPK, type_annotation_map
from opt_public_server.static import core


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

    def to_model(self) -> core.City:
        return core.City(
            id=self.id,
            name=self.name,
            abbreviation=self.abbreviation,
            geobounds=common_core.Geobounds(
                min_lat=self.min_lat,
                min_lon=self.min_lon,
                max_lat=self.max_lat,
                max_lon=self.max_lon,
            ),
        )

    @classmethod
    def from_model(cls: type[City], model: core.City):
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

    def to_model(self) -> core.Company:
        return core.Company(
            id=self.id,
            name=self.name,
            abbreviation=self.abbreviation,
            geolocation=common_core.Geolocation(
                lat=self.lat,
                lon=self.lon,
            ),
            city_id=self.city_id,
        )

    @classmethod
    def from_model(cls: type[Company], model: core.Company):
        return cls(
            id=model.id,
            name=model.name,
            abbreviation=model.abbreviation,
            lat=model.geolocation.lat,
            lon=model.geolocation.lon,
            city_id=model.city_id,
        )
