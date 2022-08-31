import strawberry

from opt_public_server.common.graphql import Info

from ._city import City, CityInput
from ._company import Company, CompanyInput
from ._route import Route, RouteCompanyInput, RouteInput


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

    @strawberry.field
    def add_route(self, info: Info, route: RouteInput) -> Route:
        input_model = route.to_model()
        model = info.context.route_service.add(input_model)
        for edge in route.company_edges:
            edge_model = edge.to_model(route_id=model.id)
            info.context.route_service.add_company(model, edge_model)
        return Route.from_model(model)
