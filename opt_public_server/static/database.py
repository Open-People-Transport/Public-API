from __future__ import annotations

from decimal import Decimal
from typing import Optional
from uuid import UUID

import inflection
from sqlalchemy import ForeignKey, Integer, UniqueConstraint, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    declared_attr,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Numeric, String, Uuid as SQLUUID
from uuid6 import uuid7

from opt_public_server.main.settings import settings


# Connection setup


engine = create_engine(settings.static_database_url, future=True, echo=True)


class Base(MappedAsDataclass, DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return inflection.tableize(cls.__name__)


# Tables of units


class City(Base, kw_only=True):
    id: Mapped[str] = mapped_column(String(14), primary_key=True)
    full_name: Mapped[str] = mapped_column(String(64))
    routes: Mapped[list[Route]] = relationship(
        back_populates="city", default_factory=list
    )
    stops: Mapped[list[Stop]] = relationship(
        back_populates="city", default_factory=list
    )
    companies: Mapped[list[Company]] = relationship(
        back_populates="city", default_factory=list
    )


class Type(Base, kw_only=True):
    id: Mapped[str] = mapped_column(String(14), primary_key=True)
    routes: Mapped[list[Route]] = relationship(
        back_populates="type", default_factory=list
    )
    vehicles: Mapped[list[Vehicle]] = relationship(
        back_populates="type", default_factory=list
    )


class Route(Base, kw_only=True):
    id: Mapped[UUID] = mapped_column(SQLUUID(), primary_key=True, default_factory=uuid7)
    name: Mapped[str] = mapped_column(String(32))
    number: Mapped[Optional[str]] = mapped_column(String(6))
    city_id: Mapped[str] = mapped_column(
        ForeignKey(City.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    type_id: Mapped[str] = mapped_column(
        ForeignKey(Type.id, onupdate="CASCADE", ondelete="RESTRICT"),
    )
    city: Mapped[City] = relationship(back_populates="routes")
    type: Mapped[Type] = relationship(back_populates="routes")
    route_stops: Mapped[list[RouteStop]] = relationship(
        back_populates="route", default_factory=list
    )
    route_companies: Mapped[list[RouteCompany]] = relationship(
        back_populates="route", default_factory=list
    )


class Stop(Base, kw_only=True):
    id: Mapped[UUID] = mapped_column(SQLUUID(), primary_key=True, default_factory=uuid7)
    full_name: Mapped[str] = mapped_column(String(64))
    short_name: Mapped[str] = mapped_column(String(40))
    lat: Mapped[Decimal] = mapped_column(Numeric(7, 5))
    lon: Mapped[Decimal] = mapped_column(Numeric(8, 5))
    city_id: Mapped[str] = mapped_column(
        ForeignKey(City.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    city: Mapped[City] = relationship(back_populates="stops")
    route_stops: Mapped[list[RouteStop]] = relationship(
        back_populates="stop", default_factory=list
    )
    __table_args__ = (UniqueConstraint("lat", "lon"),)


class Company(Base, kw_only=True):
    id: Mapped[UUID] = mapped_column(SQLUUID(), primary_key=True, default_factory=uuid7)
    full_name: Mapped[str] = mapped_column(String(64))
    short_name: Mapped[str] = mapped_column(String(14))
    lat: Mapped[Optional[Decimal]] = mapped_column(Numeric(7, 5))
    lon: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 5))
    city_id: Mapped[str] = mapped_column(
        ForeignKey(City.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    city: Mapped[City] = relationship(back_populates="companies")
    route_companies: Mapped[list[RouteCompany]] = relationship(
        back_populates="company", default_factory=list
    )
    vehicles: Mapped[list[Vehicle]] = relationship(
        back_populates="company", default_factory=list
    )
    __table_args__ = (UniqueConstraint("lat", "lon"),)


class Vehicle(Base, kw_only=True):
    id: Mapped[UUID] = mapped_column(SQLUUID(), primary_key=True, default_factory=uuid7)
    license_plate: Mapped[Optional[str]] = mapped_column(String(10), unique=True)
    tail_number: Mapped[Optional[str]] = mapped_column(String(10))
    model: Mapped[Optional[str]] = mapped_column(String(20))
    type_id: Mapped[str] = mapped_column(
        ForeignKey(Type.id, onupdate="CASCADE", ondelete="RESTRICT"),
    )
    company_id: Mapped[UUID] = mapped_column(
        ForeignKey(Company.id, ondelete="RESTRICT"),
    )
    type: Mapped[Type] = relationship(back_populates="vehicles")
    company: Mapped[Company] = relationship(back_populates="vehicles")


# Linking tables


class RouteStop(Base, kw_only=True):
    route_id: Mapped[UUID] = mapped_column(
        ForeignKey(Route.id, ondelete="CASCADE"),
        primary_key=True,
    )
    stop_id: Mapped[UUID] = mapped_column(
        ForeignKey(Stop.id, ondelete="RESTRICT"),
        primary_key=True,
    )
    distance: Mapped[int] = mapped_column(Integer())
    route: Mapped[Route] = relationship(back_populates="route_stops")
    stop: Mapped[Stop] = relationship(back_populates="route_stops")


class RouteCompany(Base, kw_only=True):
    route_id: Mapped[UUID] = mapped_column(
        ForeignKey(Route.id, ondelete="CASCADE"),
        primary_key=True,
    )
    company_id: Mapped[UUID] = mapped_column(
        ForeignKey(Company.id, ondelete="CASCADE"),
        primary_key=True,
    )
    route: Mapped[Route] = relationship(back_populates="route_companies")
    company: Mapped[Company] = relationship(back_populates="route_companies")
