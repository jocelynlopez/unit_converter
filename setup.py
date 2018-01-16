#!/usr/bin/env python3
# coding=utf-8

from codecs import open

from setuptools import setup, find_packages

# Packages information :
# -----------------------
requires = []
test_requirements = []

package_data = {'': ['LICENSE']}
# packages = find_packages(exclude=['tests*'])
packages = ['unit_converter']

classifiers = (
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: End Users/Desktop',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
)

# Extract content from README.md
# -------------------------------
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

# Setup
# -----
setup(name='unit_converter',
      version='1.1.0',
      description='Package for converting quantities in different unit.',
      long_description=readme,
      author='Jocelyn LOPEZ',
      author_email='jocelyn.lopez.pro@gmail.com',
      url='https://bitbucket.org/jocelynlopez/unit_converter',
      packages=packages,
      # package_data=package_data,
      include_package_data=True,
      install_requires=requires,
      license='MIT',
      keywords='converter units sciences',
      classifiers=classifiers,
      tests_require=test_requirements)
