#!/usr/bin/env python

import sys
from os.path import abspath, dirname, join
from ez_setup import use_setuptools
from setuptools import setup

sys.path.append(join(dirname(__file__), 'src'))
use_setuptools()
version_file = join(dirname(__file__), 'src', 'RequestsLibrary', 'version.py')
exec(compile(open(version_file).read(), version_file, 'exec'))

DESCRIPTION = """
Robot Framework keyword library wrapper around the HTTP client library requests.
"""[1:-1]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: Public Domain
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'robotframework-requests',
      version      = VERSION,
      description  = 'Robot Framework keyword library wrapper around requests',
      long_description = DESCRIPTION,
      author       = 'Bulkan Savun Evcimen',
      author_email = 'bulkan@gmail.com',
      url          = 'http://github.com/bulkan/robotframework-requests',
      license      = 'Public Domain',
      keywords     = 'robotframework testing test automation http client requests',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = ['RequestsLibrary'],
      package_data = {'RequestsLibrary': ['tests/*.txt']},
      install_requires=[
          'robotframework',
          'requests',
          'vcrpy'
      ],
)

""" From now on use this approach

python setup.py sdist upload
git tag -a 1.2.3 -m 'version 1.2.3'
git push --tags"""
