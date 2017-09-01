# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io
with io.open('./flowpython/ReadMe.rst', encoding='utf-8') as f:
    readme = f.read()
with io.open('LICENSE', encoding='utf-8') as f:
    print(f.read())
if input("Do you approve the license terms? [yes|no]") != 'yes':
    print("I'm Sorry that you cannot accept the license. Have a nice day :)")
else:
    import os
    cat = os.path.join
    setup(
        name = 'flowpython',
        version = '0.2.3',
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
        classifiers=['Programming Language :: Python :: 3.6','Programming Language :: Python :: Implementation :: CPython',
                     'Programming Language :: Python :: 3.5','Programming Language :: Python :: Implementation :: CPython']
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


