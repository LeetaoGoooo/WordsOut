import functools
from http.cookies import SimpleCookie
from requests.utils import cookiejar_from_dict

print = functools.partial(print, flush=True)


def parse_cookie_string(cookie_string:str) -> SimpleCookie:
    """parse cookie string into SimpleCookie"""
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
