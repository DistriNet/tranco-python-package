import uuid


def test_top_10(tranco_list):
    assert len(tranco_list.top(10)) == 10


def test_top_1000000(tranco_list):
    assert len(tranco_list.top(1000000)) == 1000000


def test_domain_rank(tranco_list):
    top_1 = tranco_list.top(1)[0]
    assert tranco_list.rank(top_1) == 1


def test_domain_not_in_list_rank(tranco_list):
    assert tranco_list.rank(f"domaindoesntexist{uuid.uuid4().hex.upper()[0:6]}.com") == -1
