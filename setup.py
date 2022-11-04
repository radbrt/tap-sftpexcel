#!/usr/bin/env python
from setuptools import setup


with open('requirements.txt', 'r') as fh:
    requirements = fh.read().splitlines()

setup(
    name="tap-sftpexcel",
    version="2.1.2",
    description="Singer.io tap for extracting data",
    author="Henning Holgersen",
    url="http://holgersen.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_sftpexcel"],
    install_requires=requirements,
    entry_points="""
    [console_scripts]
    tap-sftpexcel=tap_sftpexcel.tap:main
    """,
    packages=["tap_sftpexcel", "tap_sftpexcel.singer_encodings"]
)
