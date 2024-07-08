from gooey import Gooey,GooeyParser
import browser_cookie3

from src.client.base import registry

def retrieve_cookies_from_browser():
    cj = browser_cookie3.chrome()
    return cj

@Gooey(
    program_name='WordsOut',
)
def main():
    parser = GooeyParser() 
    parser.add_argument(
        "--platform", help="which dictionary do you want export", choices=list(registry.keys()))
    parser.add_argument(
        "--cookies", help="cookie, which is set after you log in")
    parser.add_argument(
        "--admin", help="admin mode, which will access cookies from browser directly (only chrome is supported)", default=False,
        widget="CheckBox",
        action = "store_true",
    )
    args = parser.parse_args()
    platform = args.platform
    cookies_str = args.cookies
    admin = args.admin
    if admin:
        try:
            cookies_str = retrieve_cookies_from_browser()
        except Exception as e:
            print(f'some error happened, {e}, will use default cookies instead')
            cookies_str = args.cookies

    if not platform:
        print("you didn't choose any platform to export!")
        return
    
    if not cookies_str:
        print("cookies weren't set property!")
        return
    
    exporter = registry[platform]
    exporter.export(cookies_str)


if __name__ == '__main__':
    main()
