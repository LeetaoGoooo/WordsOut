from http.cookiejar import CookieJar
from http.cookies import SimpleCookie
from typing import List, TypedDict, Union

import requests
from src.client.base import BaseExport
from src.utils import parse_cookie_string


class Book(TypedDict):
    bookName: str
    bookId: str


class YouDao(BaseExport):
    name = "Youdao"

    def get_books(self, cookies:SimpleCookie) -> List[Book]:
        """
        Fetched all books
        """
        url = "https://dict.youdao.com/wordbook/webapi/v2/opts"
        resp = requests.get(url=url, cookies=cookies)
        if resp.status_code != 200:
            print("Request failed. Make sure you're logged in: https://www.youdao.com/webwordbook/wordlist")
            return []
        response = resp.json()
        print("Fetched the book successfully, getting {} books in total".format(len(response["data"]["book"])))
        return response["data"]["book"]


    def get_words_by_book(self, limit, offset,sort, book:Book, cookies:SimpleCookie):
        url = "https://dict.youdao.com/wordbook/webapi/v2/word/list"
        resp = requests.get(url=url,params={
            "limit": limit,
            "offset": offset,
            "sort": sort,
            "lanTo": None,
            "lanFrom": None,
            "bookId": book["bookId"],
        }, cookies=cookies)

        if resp.status_code != 200:
            print("Request failed. Make sure you're logged in: https://www.youdao.com/webwordbook/wordlist")
            return [], 0
        
        response = resp.json()
        total = response["data"]["total"]
        words = response["data"]["itemList"]
        return [word["word"] for word in words], total


    def export_book_words(self, book:Book, limit=48, offset=0, sort="time", cookies:SimpleCookie=None):
        words, total = self.get_words_by_book(limit, offset, sort, book, cookies)

        self.write_words_to_txt(words)
        
        offset += limit
        
        print("Export【{}】Book current progress: {}/{}".format(book["bookName"], total if offset > total else offset, total))

        if offset  > total:
            print(f"Already export【{book['bookName']}】book")
            return
        
        self.take_a_break()

        return self.export_book_words(book, limit, offset, sort, cookies)  
    
    def export(self, cookie_str: Union[str, CookieJar]):
        cookies = parse_cookie_string(cookie_str)
        books = self.get_books(cookies)
        if not books:
            return
        for book in books:
            print("Book: {}".format(book["bookName"]))
            self.export_book_words(book, cookies=cookies)
