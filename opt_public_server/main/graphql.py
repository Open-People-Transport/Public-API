import strawberry
from fastapi import Depends
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types

import opt_public_server.static.database
import opt_public_server.static.graphql
from opt_public_server.common.graphql import Context


def get_context(
    static_db=Depends(opt_public_server.static.database.gen_session),
):
    return Context(static_db=static_db)


Query = merge_types("Query", (opt_public_server.static.graphql.Query,))

schema = strawberry.Schema(query=Query)

router = GraphQLRouter(schema=schema, context_getter=get_context, debug=True)
