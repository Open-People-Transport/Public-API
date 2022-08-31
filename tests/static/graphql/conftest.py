import json
from dataclasses import asdict
from pathlib import Path

import pytest
from strawberry import Schema

from opt_public_server.common.graphql import Context
from opt_public_server.static.graphql import Mutation, Query
from opt_public_server.static.services import CityService, CompanyService, RouteService
from tests.static.repositories import (
    CityTestRepository,
    CompanyTestRepository,
    RouteTestRepository,
)


schema = Schema(query=Query, mutation=Mutation)


@pytest.fixture
def context():
    return Context(
        city_service=CityService(CityTestRepository()),
        company_service=CompanyService(CompanyTestRepository()),
        route_service=RouteService(RouteTestRepository()),
    )


@pytest.fixture
def exec_query(context, snapshot):
    query_file: Path = snapshot.snapshot_dir.joinpath("query.gql")
    query = query_file.read_text()

    variables_file: Path = snapshot.snapshot_dir.joinpath("variables.json")
    if variables_file.is_file():
        variables = json.loads(variables_file.read_text())
    else:
        variables = {}

    def _exec_guery():
        return schema.execute_sync(query, variables, context_value=context)

    return _exec_guery


@pytest.fixture
def assert_snapshot_match(snapshot):
    def _assert_snapshot_match(result):
        value = json.dumps(asdict(result), indent=2, default=str)
        snapshot.assert_match(value, "result.json")

    return _assert_snapshot_match
