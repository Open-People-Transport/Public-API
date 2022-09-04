from pytest import raises
from sqlalchemy.exc import NoResultFound

from opt_public_server.static.database import CityRepository, CompanyRepository


def test_city_repository(session, city1):
    city_repo = CityRepository(session)

    assert city_repo.create(city1) is None
    assert city_repo.get(city1.id) == city1
    assert city_repo.list() == [city1]

    assert city_repo.delete(city1.id) is None
    with raises(NoResultFound):
        city_repo.get(city1.id)
    assert city_repo.list() == []


def test_company_repository(session, city1, company1):
    city_repo = CityRepository(session)
    company_repo = CompanyRepository(session)

    city_repo.create(city1)

    assert company_repo.create(company1) is None
    assert company_repo.get(company1.id) == company1
    assert company1 in company_repo.list()

    assert company_repo.delete(company1.id) is None
    with raises(NoResultFound):
        company_repo.get(company1.id)
    assert company1 not in company_repo.list()
