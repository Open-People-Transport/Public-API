def test_schema_matches(schema, snapshot):
    snapshot.assert_match(str(schema), "schema.gql")
