from tranco import Tranco

l = Tranco(cache=False).list(date='2020-03-26')
print(l.list_id)
print(l.top(10))
print(l.rank("google.com"))
print(l.rank("not.in.ranking"))