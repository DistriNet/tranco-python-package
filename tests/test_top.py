def test_top_10(tranco_list):
    assert len(tranco_list.top(10)) == 10


def test_top_1000000(tranco_list):
    assert len(tranco_list.top(1000000)) == 1000000


