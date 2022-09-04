def test_scalars(exec_query, assert_snapshot_match):
    result = exec_query()
    assert_snapshot_match(result)
