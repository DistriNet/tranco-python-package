import zipfile
from io import BytesIO

import requests
import os
from datetime import datetime, timedelta


class TrancoList():
    def __init__(self, date, list_id, lst):
        self.date = date
        self.list_id = list_id
        self.list_page = "https://tranco-list.eu/list/{}/1000000".format(list_id)
        self.list = lst

    def top(self, num=1000000):
        return self.list[:num]

    def rank(self, domain):
        try:
            return self.list.index(domain) + 1
        except ValueError:
            return -1

class Tranco():
    def __init__(self, **kwargs):
        """
        :param kwargs:
            cache: <bool> enables/disables caching, default: True
            cache_dir: <str> directory used to cache Tranco top lists, default: cwd + .tranco/
        """

        self.should_cache = kwargs.get('cache', True)
        self.cache_dir = kwargs.get('cache_dir', None)
        if self.cache_dir is None:
            cwd = os.getcwd()
            self.cache_dir = os.path.join(cwd, '.tranco')

        if self.should_cache and not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def _cache_path(self, date):
        return os.path.join(self.cache_dir, date + '-DEFAULT.csv')

    def list(self, date='latest'):
        if date is 'latest':
            yesterday = (datetime.utcnow() - timedelta(days=1))
            date = yesterday.strftime('%Y-%m-%d')
        list_id = self._get_list_id_for_date(date)

        if self.should_cache and os.path.exists(self._cache_path(list_id)):
            with open(self._cache_path(list_id)) as f:
                top_list_text = f.read()
        else:
            top_list_text = self._download_zip_file(list_id)

        return TrancoList(date, list_id, list(map(lambda x: x[x.index(',') + 1:], top_list_text.splitlines())))

    def _get_list_id_for_date(self, date):
        r1 = requests.get('https://tranco-list.eu/daily_list_id?date={}'.format(date))
        if r1.status_code == 200:
            return r1.text
        else:
            raise AttributeError("The daily list for this date is currently unavailable.")

    def _download_zip_file(self, list_id):
        download_url = 'https://tranco-list.eu/download_daily/{}'.format(list_id)
        r = requests.get(download_url, stream=True)
        with zipfile.ZipFile(BytesIO(r.content)) as z:
            with z.open('top-1m.csv') as csvf:
                lst = csvf.read().decode("utf-8")
                if self.should_cache:
                    with open(self._cache_path(list_id), 'w') as f:
                        f.write(lst)
                return lst
