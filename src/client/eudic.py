
from http.cookies import SimpleCookie
from src.client.base import BaseExport
from src.utils import print, parse_cookie_string
import requests


class Eudic(BaseExport):
    name = "Eudic"
    length = 100
    params = {
        "draw": 5,
        "columns[0][data]": "id",
        "columns[0][name]": None,
        "columns[0][searchable]": False,
        "columns[0][orderable]": False,
        "columns[0][search][value]": None,
        "columns[0][search][regex]": False,
        "columns[1][data]": "id",
        "columns[1][name]": None,
        "columns[1][searchable]": True,
        "columns[1][orderable]": False,
        "columns[1][search][value]": None,
        "columns[1][search][regex]": False,
        "columns[2][data]": "word",
        "columns[2][name]": None,
        "columns[2][searchable]": False,
        "columns[2][orderable]": True,
        "columns[2][search][value]": None,
        "columns[2][search][regex]": False,
        "columns[3][data]": "phon",
        "columns[3][name]": None,
        "columns[3][searchable]": True,
        "columns[3][orderable]": False,
        "columns[3][search][value]": None,
        "columns[3][search][regex]": False,
        "columns[4][data]": "exp",
        "columns[4][name]": None,
        "columns[4][searchable]": True,
        "columns[4][orderable]": False,
        "columns[4][search][value]": None,
        "columns[4][search][regex]": False,
        "columns[5][data]": "rating",
        "columns[5][name]": None,
        "columns[5][searchable]": False,
        "columns[5][orderable]": True,
        "columns[5][search][value]": None,
        "columns[5][search][regex]": False,
        "columns[6][data]": "addtime",
        "columns[6][name]": None,
        "columns[6][searchable]": False,
        "columns[6][orderable]": False,
        "columns[6][search][value]": None,
        "columns[6][search][regex]": False,
        "order[0][column]": 6,
        "order[0][dir]": "desc",
        "start": 0,
        "length": length,  # per page words number
        "search[value]": None,
        "search[regex]": False,
        "categoryid": -1
    }

    def export(self, cookie_str: str):
        start = 0
        cookies = parse_cookie_string(cookie_str)
        words,total_count = self.fetch_words(start, cookies=cookies)
        while words:
            self.write_words_to_txt(words)
            self.take_a_break()
            words = []
            start += self.length
            if start <= total_count:
                words,total_count = self.fetch_words(start,cookies=cookies)


    def fetch_words(self, start:int=0, cookies: SimpleCookie=None):
        url = "http://my.eudic.net/StudyList/WordsDataSource"
        self.params.update({"start":start})
        resp = requests.get(url,params=self.params, cookies=cookies)
        resp_json = resp.json()
        total_count = resp_json['recordsTotal']
        print(f'{total_count} words need to exported, current progress:{start+self.length}/{total_count}')
        words = resp_json["data"]
        return [word["uuid"] for word in words], total_count