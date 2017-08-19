# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
with io.open('./flowpython/ReadMe.rst', encoding='utf-8') as f:
    readme = f.read()
import os
cat = os.path.join
setup(
    name = 'flowpython',
    version = '0.2.1.1',
    keywords='gramamr, ast, readability',
    description = "Additional Grammar Compatible to CPython",
    long_description=readme,
    license = 'MIT License',
    url = 'https://github.com/thautwarm/flowpython',
    author = 'Thautwarm',
    author_email = 'twshere@outlook.com',
    packages = find_packages(),
    include_package_data = True,
    platforms  = ['windows','linux'],
    classifiers=['Programming Language :: Python :: 3.6','Programming Language :: Python :: Implementation :: CPython']
)
try:
	os.remove(cat(os.environ["HOME"], '.flowpy'))
except KeyError:
    try:
        os.remove(cat(os.environ["HOMEPATH"], '.flowpy'))
    except FileNotFoundError:
        pass
except FileNotFoundError:
	pass
