#!/usr/bin/env python3
# coding=utf-8

import os
import re
import sys

from codecs import open

from setuptools import setup, find_packages


# Packages informations :
# -----------------------
requires = []
test_requirements = []

package_data = {'': ['LICENSE']}
packages = find_packages(exclude=['tests*'])

classifiers = (
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: End Users/Desktop',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
)


# Extract infos from __init__.py
# ------------------------------
def extract_value_from__init__(name):
    with open('generic_converter/__init__.py', 'r') as fd:
        r = re.search('^__%s__\s*=\s*[\'"]([^\'"]*)[\'"]' %
                      name, fd.read(), re.MULTILINE)
    if not r:
        raise RuntimeError('Cannot find __%s__ information' % name)
    else:
        return r.group(1)

name = extract_value_from__init__('title')
version = extract_value_from__init__('version')
author = extract_value_from__init__('author')
author_email = extract_value_from__init__('author_email')
url = extract_value_from__init__('url')
license = extract_value_from__init__('license')
description = extract_value_from__init__('description')
keywords = extract_value_from__init__('keywords')


# Extract content from README.md
# -------------------------------
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

# Setup
# -----
setup(name=name,
      version=version,
      description=description,
      long_description=readme,
      author=author,
      author_email=author_email,
      url=url,
      packages=packages,
      # package_data=package_data,
      include_package_data=True,
      install_requires=requires,
      license=license,
      keywords=keywords,
      classifiers=classifiers,
      tests_require=test_requirements)
