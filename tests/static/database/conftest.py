from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from opt_public_server.static.core import City, Company, Route
from opt_public_server.static.database import Base


DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
make_session = sessionmaker[Session](bind=engine)


@fixture
def session():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with make_session() as session:
        yield session


@fixture
def city1():
    obj = {
        "id": "0183084b-09c2-7947-9159-be96ff795886",
        "name": "Test City 1",
        "abbreviation": "tecity1",
        "geobounds": {
            "min_lat": "-90.000000",
            "min_lon": "-180.000000",
            "max_lat": "90.000000",
            "max_lon": "180.000000",
        },
    }
    return City(**obj)


@fixture
def company1():
    obj = {
        "id": "0183084b-09c6-7bfb-8563-76bf25e2d6b5",
        "name": "Test Company 1",
        "abbreviation": "tecomp1",
        "geolocation": {
            "lat": "0.000000",
            "lon": "0.000000",
        },
        "city_id": "0183084b-09c2-7947-9159-be96ff795886",
    }
    return Company(**obj)


@fixture
def route1():
    obj = {
        "id": "0183084b-09c9-740e-959d-a4e53e61236d",
        "number": "1",
        "number_prefix": "A-",
        "type": "BUS",
        "city_id": "0183084b-09c2-7947-9159-be96ff795886",
    }
    return Route(**obj)  # type: ignore
