import requests
import time
import random
from typing import TypedDict, List
from http.cookies import SimpleCookie
from requests.utils import cookiejar_from_dict
import argparse
from gooey import Gooey
import functools
print = functools.partial(print, flush=True)

class Book(TypedDict):
    bookName: str
    bookId: str

def get_books(cookies:SimpleCookie) -> List[Book]:
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


def get_words_by_book(limit, offset,sort, book:Book, cookies:SimpleCookie):
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


def export_book_words(book:Book, limit=48, offset=0, sort="time", cookies:SimpleCookie=None):
    words, total = get_words_by_book(limit, offset, sort, book, cookies)

    with open("words.txt", "a+") as f:
        f.write("\n".join(words))
        f.write("\n")
    
    offset += limit
    
    print("Export【{}】Book current progress: {}/{}".format(book["bookName"], total if offset > total else offset, total))

    if offset  > total:
        print(f"Already export【{book['bookName']}】book")
        return
    
    sleep_time = random.randint(1, 3)
    print("Task a random sleep for {}s".format(sleep_time))
    time.sleep(sleep_time)

    return export_book_words(book, limit, offset, sort, cookies)    

def export_words_to_txt(cookies:SimpleCookie):
    books = get_books(cookies)
    if not books:
        return
    for book in books:
        print("Book: {}".format(book["bookName"]))
        export_book_words(book, cookies=cookies)


def parse_cookie_string(cookie_string):
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies_dict = {}
    cookiejar = None
    for key, morsel in cookie.items():
        cookies_dict[key] = morsel.value
        cookiejar = cookiejar_from_dict(
            cookies_dict, cookiejar=None, overwrite=True
        )
    return cookiejar

    

@Gooey(
    program_name='Youdao Dictionary Exporter', 
)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie", help="cookie, which is set after you log in")
    options = parser.parse_args()
    cj = parse_cookie_string(options.cookie)
    export_words_to_txt(cookies=cj)


if __name__ == '__main__':
    main()