#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-diamond',
    version='0.0.1',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    maintainer='Matt Robenolt',
    maintainer_email='matt@ydekproductions.com',
    license='MIT',
    url='https://github.com/python-diamond/pytest-diamond',
    description='pytest plugin for diamond',
    long_description=read('README.rst'),
    py_modules=['pytest_diamond'],
    install_requires=['pytest>=2.7.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'diamond = pytest_diamond',
        ],
    },
)
