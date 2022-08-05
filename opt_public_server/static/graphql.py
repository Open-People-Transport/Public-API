import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def available(self) -> bool:
        return True
