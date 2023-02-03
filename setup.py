#!/usr/bin/env python
from __future__ import print_function

try:
    # python setup.py test
    import multiprocessing  # NOQA
except ImportError:
    pass

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


cmdclass = {}
cmdclass['test'] = PyTest

with open('README.md', 'rb') as f:
    long_description = f.read().decode('utf-8')


requirements = []
requirements_file = "requirements.txt"
if os.path.isfile(requirements_file):
    with open(requirements_file, "r") as f:
        requirements = [l for l in f.read().splitlines() if l]

setup(
    name='wechatpy',
    version='2.0.0.telesoho',
    author='messense',
    author_email='messense@icloud.com',
    url='https://github.com/telesoho/wechatpy',
    packages=find_packages(exclude=('tests', 'tests.*')),
    keywords='WeChat, weixin, SDK',
    description='WeChat SDK for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    include_package_data=True,
    tests_require=[
        'pytest',
        'httmock',
        'redis',
        'pymemcache',
        'shove',
    ],
    cmdclass=cmdclass,
    classifiers=[
    ],
    extras_require={
        'cryptography': ['cryptography'],
        'pycrypto': ['pycryptodome'],
    }
)