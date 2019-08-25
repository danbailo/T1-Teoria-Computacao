#!/usr/bin/python3

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='computer_theory',
    version='1.0',
    description='First work of the discipline of Computer Theory',
    long_description=readme,
    author='Daniel Bailo',
    author_email='danbailoufms@gmail.com',
    url='https://github.com/danbailo/T1-Teoria-Computacao',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

