import functools
from http.cookiejar import CookieJar
from http.cookies import SimpleCookie
from typing import Union
from requests.utils import cookiejar_from_dict

print = functools.partial(print, flush=True)


def parse_cookie_string(cookie_string_or_jar:Union[str, CookieJar]) -> Union[SimpleCookie, CookieJar]:
    """parse cookie string into SimpleCookie"""
    
    if isinstance(cookie_string_or_jar, CookieJar):
        return cookie_string_or_jar
    
    cookie = SimpleCookie()
    cookie.load(cookie_string_or_jar)
    cookies_dict = {}
    cookiejar = None
    for key, morsel in cookie.items():
        cookies_dict[key] = morsel.value
        cookiejar = cookiejar_from_dict(
            cookies_dict, cookiejar=None, overwrite=True
        )
    return cookiejar
