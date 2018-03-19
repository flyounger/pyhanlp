# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 20:54
from os.path import abspath, join, dirname
from pyhanlp.util import smart_open
from setuptools import find_packages, setup

this_dir = abspath(dirname(__file__))
with smart_open(join(this_dir, 'README.md')) as file:
    long_description = file.read()

setup(
    name='pyhanlp',
    version='0.1.1',
    description='Python wrapper for HanLP: Han Language Processing',
    long_description=long_description,
    url='https://github.com/hankcs/pyhanlp',
    author='hankcs',
    author_email='hankcshe@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'
    ],
    keywords='corpus,machine-learning,NLU,NLP',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=['jpype1'],
    entry_points={
        'console_scripts': [
            'hanlp=pyhanlp.main:main',
        ],
    },
)
