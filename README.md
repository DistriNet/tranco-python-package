# Tranco

This package allows easy access to the Tranco list, published at [https://tranco-list.eu]().

## Usage

Create a `Tranco` object, indicating whether you want to cache downloaded lists:
```python
from tranco import Tranco
t = Tranco(cache=True, cache_dir='.tranco')
```

You can then retrieve lists from this object using the `list` method:

```python
latest_list = t.list()
date_list = t.list(date='2019-02-25')
```

This method returns a `TrancoList`, which allows you to retrieve a certain prefix of the list (`top`), the list ID (`list_id`), the list page (`list_page`) or the rank of a domain (`rank`):
```python
latest_list.top(10000)
latest_list.list_id
latest_list.list_page
latest_list.rank("google.com")
latest_list.rank("not.in.ranking") # returns -1
```