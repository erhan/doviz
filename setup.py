from setuptools import setup


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
