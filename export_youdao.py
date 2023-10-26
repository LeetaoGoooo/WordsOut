import requests
import time
import random
from typing import TypedDict, List
from http.cookies import SimpleCookie
from requests.utils import cookiejar_from_dict
import argparse

class Book(TypedDict):
    bookName: str
    bookId: str

cj = None

def get_books() -> List[Book]:
    """
    获取所有的单词本列表
    """
    url = "https://dict.youdao.com/wordbook/webapi/v2/opts"
    resp = requests.get(url=url, cookies=cj)
    if resp.status_code != 200:
        print("请求有道单词本失败,请确保已经登录有道单词本: https://www.youdao.com/webwordbook/wordlist")
        return []
    response = resp.json()
    print("获取单词本列表成功,累计获取{}个单词本".format(len(response["data"]["book"])))
    return response["data"]["book"]


def get_words_by_book(limit, offset,sort, book:Book):
    url = "https://dict.youdao.com/wordbook/webapi/v2/word/list"
    resp = requests.get(url=url,params={
        "limit": limit,
        "offset": offset,
        "sort": sort,
        "lanTo": None,
        "lanFrom": None,
        "bookId": book["bookId"],
    }, cookies=cj)
    if resp.status_code != 200:
        print("请求有道单词本失败,请确保已经登录有道单词本: https://www.youdao.com/webwordbook/wordlist")
        return [], 0
    
    response = resp.json()
    total = response["data"]["total"]
    words = response["data"]["itemList"]
    return [word["word"] for word in words], total


def export_book_words(book:Book, limit=48, offset=0, sort="time"):
    words, total = get_words_by_book(limit, offset, sort, book)

    with open("words.txt", "a+") as f:
        f.write("\n".join(words))
        f.write("\n")
    
    offset += limit
    
    print("当前导出单词本【{}】 进度: {}/{}".format(book["bookName"], total if offset > total else offset, total))

    if offset  > total:
        print(f"导出单词本【{book['bookName']}】完成")
        return
    
    sleep_time = random.randint(1, 3)
    print("休息{}秒".format(sleep_time))
    time.sleep(sleep_time)

    return export_book_words(book, limit, offset, sort)    

def export_words_to_txt():
    books = get_books()
    if not books:
        return
    for book in books:
        print("单词本: {}".format(book["bookName"]))
        export_book_words(book)


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

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookie", help="登陆有道单词本后的cookie")
    options = parser.parse_args()
    cj = parse_cookie_string(options.cookie)
    export_words_to_txt()
