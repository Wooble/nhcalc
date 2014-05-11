#!/usr/bin/env python

from setuptools import setup
from nhcalc import __version__

setup(
    name = "nhcalc",
    version = __version__,
    author = "Geoffrey Spear",
    author_email = "geoffspear@gmail.com",
    description = 'NetHack Calculator',
    license = "BSD",
    keywords = "NetHack",
    url = "http://pythonhosted.org/nhcalc",
    packages = ['nhcalc'],
    install_requires = ['six'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Nethack General Public License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ],
    )
