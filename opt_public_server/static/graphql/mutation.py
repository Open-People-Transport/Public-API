import strawberry

from opt_public_server.common.graphql import Info
from opt_public_server.static.services.city_service import CityService
from opt_public_server.static.services.company_service import CompanyService

from .city import City, CityInput
from .company import Company, CompanyInput


@strawberry.type
class Mutation:
    @strawberry.field
    def add_city(self, info: Info, city: CityInput) -> City:
        input_model = city.to_model()
        model = CityService.from_graphql_info(info).add(input_model)
        return City.from_model(model)

    @strawberry.field
    def add_company(self, info: Info, company: CompanyInput) -> Company:
        input_model = company.to_model()
        model = CompanyService.from_graphql_info(info).add(input_model)
        return Company.from_model(model)
