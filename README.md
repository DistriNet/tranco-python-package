# Tranco

This package allows easy access to the Tranco list, published at [https://tranco-list.eu](https://tranco-list.eu/).

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

This method returns a `TrancoList`, which allows you to retrieve a certain prefix of the list (`top`), 
the list ID (`list_id`), the list page (`list_page`) or the rank of a domain (`rank`):
```python
latest_list.top(10000)
latest_list.list_id
latest_list.list_page
latest_list.rank("google.com")
latest_list.rank("not.in.ranking") # returns -1
```

You can also generate custom lists. 
First, create a `Tranco` object with valid credentials 
(available from your [account page](https://tranco-list.eu/account)):
```python
from tranco import Tranco
t = Tranco(account_email="abc@xyz.eu", api_key="123ABC")
```

Then, pass the configuration (according to [this schema](https://tranco-list.eu/api_documentation#datatypes-configuration))
of your custom list to `configure`:
```python
c = t.configure(
    {
        'providers': ['alexa', 'umbrella', 'majestic'],
        'startDate': '2021-01-01',
        'endDate': '2021-01-30',
        'combinationMethod': 'dowdall',
        'listPrefix': 'full',
        'filterPLD': 'on',
    }
)
```
This method returns a tuple: whether the list is already available or is still being generated, 
and the ID that has been/will be assigned to the list.

You can retrieve metadata for a list through `list_metadata`:
```python
m = t.list_metadata(list_id="6P7X")
```
If a list is still being generated, you can use this method to track the progress; 
once a list has been generated, this metadata will indicate how the list was configured.
