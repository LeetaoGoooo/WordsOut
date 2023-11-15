import argparse
from gooey import Gooey
from src.client.base import registry


@Gooey(
    program_name='WordsOut',
)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform", help="which dictionary do you want export", choices=list(registry.keys()))
    parser.add_argument(
        "--cookies", help="cookie, which is set after you log in")
    args = parser.parse_args()

    platform = args.platform
    cookies_str = args.cookies

    exporter = registry[platform]
    exporter.export(cookies_str)


if __name__ == '__main__':
    main()
