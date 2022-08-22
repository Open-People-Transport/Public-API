import strawberry

from opt_public_server.common.graphql import Info

from ._city import City, CityInput
from ._company import Company, CompanyInput


@strawberry.type
class Mutation:
    @strawberry.field
    def add_city(self, info: Info, city: CityInput) -> City:
        input_model = city.to_model()
        model = info.context.city_service.add(input_model)
        return City.from_model(model)

    @strawberry.field
    def add_company(self, info: Info, company: CompanyInput) -> Company:
        input_model = company.to_model()
        model = info.context.company_service.add(input_model)
        return Company.from_model(model)
