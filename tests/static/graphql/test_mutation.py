def test_add_city(exec_query, assert_snapshot_match):
    result = exec_query()
    assert_snapshot_match(result)


def test_add_company(exec_query, assert_snapshot_match):
    result = exec_query()
    assert_snapshot_match(result)
