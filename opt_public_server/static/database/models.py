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

from opt_public_server.common.database.types import (
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
    name: Mapped[FullName] = mapped_column(nullable=False)
    abbreviation: Mapped[Abbreviation] = mapped_column(nullable=False)
    min_lat: Mapped[Latitude] = mapped_column(nullable=False)
    min_lon: Mapped[Longitude] = mapped_column(nullable=False)
    max_lat: Mapped[Latitude] = mapped_column(nullable=False)
    max_lon: Mapped[Longitude] = mapped_column(nullable=False)


class Company(Base, kw_only=True):
    id: Mapped[UUIDPK]
    name: Mapped[FullName] = mapped_column(nullable=False)
    abbreviation: Mapped[Abbreviation] = mapped_column(nullable=False)
    lat: Mapped[Latitude] = mapped_column(nullable=False)
    lon: Mapped[Longitude] = mapped_column(nullable=False)
    city_id: Mapped[UUID] = mapped_column(ForeignKey(City.id), nullable=False)
