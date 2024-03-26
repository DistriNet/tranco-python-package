def test_daily(tranco):
    l = tranco.list(date="2024-01-01")
    assert l.list_id == "V929N"
