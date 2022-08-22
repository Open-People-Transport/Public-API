from uuid import uuid4

import pytest
from sqlalchemy.exc import NoResultFound

from opt_public_server.common.models import Geobounds, Geolocation, Latitude, Longitude
from opt_public_server.static.database import (
    CityRepository,
    CompanyRepository,
    gen_session,
)
from opt_public_server.static.models import City, Company


@pytest.fixture
def session():
    yield from gen_session()


def test_city_repository(session):
    city_repo = CityRepository(session)
    city = City(
        id=uuid4(),
        name="Test City",
        abbreviation="testcity",
        geobounds=Geobounds(
            min_lat=Latitude("12.345678"),
            min_lon=Longitude("123.456789"),
            max_lat=Latitude("12.345678"),
            max_lon=Longitude("123.456789"),
        ),
    )

    assert city_repo.create(city) is None
    assert city_repo.get(city.id) == city
    assert city in city_repo.list()

    assert city_repo.delete(city.id) is None
    with pytest.raises(NoResultFound):
        city_repo.get(city.id)
    assert city not in city_repo.list()


def test_company_repository(session):
    city_repo = CityRepository(session)
    city_list = city_repo.list()
    assert city_list, "Database contains no City to test against"
    city = city_list[0]

    company_repo = CompanyRepository(session)
    company = Company(
        id=uuid4(),
        name="Test Company",
        abbreviation="testcomp",
        geolocation=Geolocation(
            lat=Latitude("12.345678"),
            lon=Longitude("123.456789"),
        ),
        city_id=city.id,
    )

    assert company_repo.create(company) is None
    assert company_repo.get(company.id) == company
    assert company in company_repo.list()

    assert company_repo.delete(company.id) is None
    with pytest.raises(NoResultFound):
        company_repo.get(company.id)
    assert company not in company_repo.list()
