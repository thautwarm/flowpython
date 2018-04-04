# # -*- coding: utf-8 -*-
# from setuptools import setup, find_packages
# import io
# import os
# import sys
# import platform
# is_linux = any(platform.linux_distribution())
# HOME = os.environ['HOME' if is_linux else 'HOMEPATH']

# with io.open('./flowpython/ReadMe.rst', encoding='utf-8') as f:
#     readme = f.read()
# if input("Are you using MacOS?[yes|no]") != 'yes':
#     print("I'm sorry to be so poor to get a MacOS machine, so no distribution for that os :(")
#     print("Or you can buy me one and I'll make the corresponding binaries for you :)")
#     sys.exit(0)
# else:
#     cat = os.path.join
#     setup(
#         name = 'flowpython',
#         version = '0.3',
#         keywords='gramamr, ast, readability',
#         description = "Additional Grammar Compatible to CPython",
#         long_description=readme,
#         license = 'MIT License',
#         url = 'https://github.com/thautwarm/flowpython',
#         author = 'Thautwarm',
#         author_email = 'twshere@outlook.com',
#         packages = find_packages(),
#         include_package_data = True,
#         platforms  = ['windows', 'linux'],
#         classifiers=['Programming Language :: Python :: 3.6','Programming Language :: Python :: Implementation :: CPython']
#     )
#     try:
#         os.remove(cat(HOME, '.flowpy'))
#     except FileNotFoundError:
#         pass


