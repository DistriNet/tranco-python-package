def test_full(tranco):
    l = tranco.list(list_id="93N82", full=True)
    assert len(l.list) == 8469


def test_subdomains(tranco):
    l = tranco.list(date="2024-01-01", subdomains=True)
    assert l.list_id == "G6Y6K"


def test_top_1m_after_full(tranco):
    lf = tranco.list(list_id="G6Y6K", full=True)
    assert len(lf.list) > 1000000
    ln = tranco.list(list_id="G6Y6K", full=False)
    assert len(ln.list) == 1000000