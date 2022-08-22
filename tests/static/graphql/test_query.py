def test_cities(exec_query, assert_snapshot_match):
    result = exec_query()
    assert_snapshot_match(result)


def test_companies(exec_query, assert_snapshot_match):
    result = exec_query()
    assert_snapshot_match(result)
