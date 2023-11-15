import pytest
from tranco.tranco import Tranco


@pytest.fixture(scope="session")
def tranco():
    t = Tranco(cache=True, cache_dir='.tranco')
    t.list()  # prefetch list
    return t


@pytest.fixture(scope="session")
def tranco_list(tranco):
    return tranco.list()

