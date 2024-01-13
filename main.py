import os
import sys
import argparse
import subprocess
from pyfiglet import figlet_format
from pyfiglet import FontNotFound
from pyfiglet import Figlet

parser = argparse.ArgumentParser()

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
        print(figlet_format(text, font=font_name), end="")

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt, Exception):
        print("Program Stopped.")
