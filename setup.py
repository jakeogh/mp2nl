# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = ["click"]

config = {
    "version": "0.1",
    "name": "mp2nl",
    "url": "https://github.com/jakeogh/mp2nl",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "convert messagepacked stdin to \n terminated utf8",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"mp2nl": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
    "entry_points": {
        "console_scripts": [
            "mp2nl=mp2nl.mp2nl:cli",
        ],
    },
}

setup(**config)
