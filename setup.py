import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='doviz',
    version='0.1',
    py_modules=['doviz'],
    author="Erhan BÜTE",
    author_email="erhanbute@outlook.com",
    url="https://github.com/erhan/doviz",
    description=("""Cli doviz"""),
    install_requires=[
        'lxml',
        'Click',
        'requests',
        'bs4'
    ],
    entry_points='''
        [console_scripts]
        doviz=doviz:get_exchange_rate
    '''
)
