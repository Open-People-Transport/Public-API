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

from opt_public_server.common.database import (
    UUIDPK,
    Abbreviation,
    FullName,
    Latitude,
    Longitude,
    type_annotation_map,
)


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


class Company(Base, kw_only=True):
    id: Mapped[UUIDPK]
    name: Mapped[FullName]
    abbreviation: Mapped[Abbreviation]
    lat: Mapped[Latitude]
    lon: Mapped[Longitude]
    city_id: Mapped[UUID] = mapped_column(ForeignKey(City.id))
