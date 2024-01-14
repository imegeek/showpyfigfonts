from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'Alternative to showfigfonts for python'
LONG_DESCRIPTION = 'Shows installed figlet fonts help of pyfiglet module.'

# Setting up
setup(
    name="showpyfigfonts",
    version=VERSION,
    author="Im Geek (Ankush Bhagat)",
    author_email="<imegeek@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=DESCRIPTION,
    long_description=long_description,
    entry_points={
        'console_scripts': ['showpyfigfonts = showpyfigfonts:main'],
    },
    packages=find_packages(),
    install_requires=['pyfiglet'],
    keywords=['python', 'pyfiglet', 'figlet', 'fonts', 'render'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)