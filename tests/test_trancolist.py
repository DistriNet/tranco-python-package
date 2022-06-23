import pytest
from tranco.tranco import Tranco


def test_list_is_same():
    t = Tranco(cache=True, cache_dir='.tranco')
    core_list = t._get_list()
    t_list = t.list()
    for x in t_list.od.items():
        assert core_list[x[1]-1] == x[0]


def test_list_property():
    t = Tranco(cache=True, cache_dir='.tranco')
    core_list = t._get_list()
    t_list = t.list()
    for i, domain in enumerate(t_list.list):
        assert core_list[i] == domain


def test_domain_rank():
    t = Tranco(cache=True, cache_dir='.tranco')
    core_list = t._get_list()
    t_list = t.list()
    for i, domain in enumerate(core_list, start=1):
        assert i == t_list.rank(domain)


def test_domain_not_in_list_rank():
    t = Tranco(cache=True, cache_dir='.tranco')
    t_list = t.list()
    assert t_list.rank("domaindoesntexist.com") == -1


def test_top():
    t = Tranco(cache=True, cache_dir='.tranco')
    core_list = t._get_list()
    t_list = t.list()
    x = core_list[:100]
    y = t_list.top(100)
    assert x == y


# def test_perf():
#     """ Note: this test is commented out because it takes a long time to run """
#     from codetiming import Timer
#     # perf comparison of two lists
#     t = Tranco(cache=True, cache_dir='.tranco')
#     core_list = t._get_list()
#     t_list = t.list()
#     # test ordered dictionary
#     timer = Timer(name="class", logger=None)
#     timer.start()
#     for i, domain in enumerate(core_list, start=1):
#         assert i == t_list.rank(domain)
#     print(timer.stop())
#     # 0.472543328 seconds
#
#     # now run the old way
#     timer = Timer(name="class", logger=None)
#     timer.start()
#     for i, domain in enumerate(core_list, start=1):
#         assert i == core_list.index(domain) + 1
#     print(timer.stop())
#     print()
#     # gave up after 10 min



