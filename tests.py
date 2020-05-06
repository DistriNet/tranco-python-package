from tranco import Tranco

l = Tranco(cache=True).list(date='2020-04-01')
print(l.list_id)
print(l.top(10))
print(l.rank("google.com"))
print(l.rank("not.in.ranking"))
l2 = Tranco(cache=True).list(date='2020-04-01')
print(l2.list_id)
print(l2.top(10))
print(l2.rank("google.com"))
print(l2.rank("not.in.ranking"))
