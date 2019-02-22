from tranco import Tranco

l = Tranco(cache=True).list(date='2019-02-19')
print(l.list_id)
print(l.top(10))
print(l.rank("google.com"))
print(l.rank("not.in.ranking"))