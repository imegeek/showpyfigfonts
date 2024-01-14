import os
import sys
import argparse
from pyfiglet import figlet_format
from pyfiglet import FontNotFound
from pyfiglet import Figlet

if sys.version_info < (3, 8):
    raise ImportError(
        f'You are using an unsupported version of Python. Only Python versions 3.8 and above are supported by showpyfigfonts')  # noqa: F541

__author__ = 'IM GEEK'
__license__ = 'MIT'

parser = argparse.ArgumentParser(prog="showpyfigfonts")

parser.add_argument(
    "text",
    nargs="?",
    help="Render fonts by text."
)

parser.add_argument(
    "--font", "-f",
    metavar="name",
    help="Render specific font by name."
)

args = parser.parse_args()
font_name = args.font
text = args.text

fonts = os.listdir(os.path.join(sys.path[5], "pyfiglet/fonts"))
ignore = ["__init__.py", "__pycache__", "__main__.py"]

def main():
    global text
    try:
        if (text or not text) and not font_name:
            for file in fonts:
                font = file.split(".")[0]
                try:
                    if not file in ignore:
                        print(f"{font} :", end="\n")
                        f = Figlet(font=font)
                        if text:
                            print(f.renderText(text))
                        else:
                            print(f.renderText(font))
                except (FontNotFound, Exception):
                    pass
        else:
            print(f"{font_name} :", end="\n")
            if text is None:
                text = font_name
            print(figlet_format(text, font=font_name), end="")
    except (EOFError, KeyboardInterrupt, Exception):
        print("Program Stopped.")

