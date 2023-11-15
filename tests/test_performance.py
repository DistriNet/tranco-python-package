from codetiming import Timer
import pytest


def test_performance_rank(tranco_list):
    core_list = tranco_list.top(1000000)     
    # test dictionary
    timer = Timer(name="class", logger=None)
    timer.start()
    for i, domain in enumerate(core_list, start=1):
        assert i == tranco_list.rank(domain)
    print("Rank:", timer.stop())


def test_performance_top(tranco_list):
    # test dictionary
    timer = Timer(name="class", logger=None)
    timer.start()
    core_list = tranco_list.top(1000000)     
    print("Top:", timer.stop())
