from http.cookies import SimpleCookie
from src.client.base import BaseExport
from src.utils import parse_cookie_string
import requests
import execjs
from pathlib import Path
import json
from src.utils import print

class Shanbay(BaseExport):

    name = "Shanbay"

    def export(self, cookie_str: str):
        words = []
        cookies = parse_cookie_string(cookie_str)
        req_groups = (("/learning_items", "DESC", "CREATED_AT"),
                      ("/unlearned_items", "DESC"))
        for req_group in req_groups:
            page = 1
            words = self.get_words(*req_group, page=page, cookies=cookies)
            while words:
                page += 1
                words = self.get_words(*req_group, page=page, cookies=cookies)

    def decode_response(self, data: str) -> dict:
        root_dir = Path().cwd()
        with open(root_dir.joinpath("src", "assets", "shanbay.js"), "r", encoding='utf-8') as f:
            source_code = " ".join(f.readlines())
            ctx = execjs.compile(source_code)
            resp_json = json.loads(ctx.call("decodeJson", data))
            return resp_json

    def get_words(self, end_point: str, order: str, order_by: str = None, ipp: int = 10, page: int = 1, cookies: SimpleCookie = None):
        host = "https://apiv3.shanbay.com/wordscollection/learning/words"
        url = f'{host}{end_point}'
        params = {
            "order": order,
            "order_by": order_by,
            "ipp": ipp,
            "page": page
        }
        print(f"request url:{url} params: {params}")
        resp = requests.get(url, params=params, cookies=cookies)
        resp_json = resp.json()
        data = resp_json["data"]
        resp_json = self.decode_response(data)
        vocabulary_list = resp_json["objects"]
        words = [vocabulary["vocabulary"]['word'] for vocabulary in vocabulary_list]
        self.write_words_to_txt(words)
        self.take_a_break()
        return words
