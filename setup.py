#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Setup module for the Protocol Buffer project
#
# June 2021

from setuptools import setup
import os

# Pull in the essential run-time requirements
# We use an external file so we can do a
# `pip install -r runtime-build-requirements.txt`
# when building a Docker image.
with open('requirements.txt') as file:
    requirements = file.read().splitlines()


# Use the README.rst as the long description.
def get_long_description():
    return open('README.rst').read()


setup(

    name='im-protobuf',
    version=os.environ.get('GITHUB_REF_SLUG', '1.0.2'),
    author='Alan Christie',
    author_email='achristie@informaticsmatters.com',
    url='https://github.com/informaticsmatters/protobuf',
    license='MIT',
    description='Cross-product protocol buffers',
    long_description=get_long_description(),
    keywords='protobuf protoc messaging',
    platforms=['any'],

    # Our modules to package
    package_dir={'': 'src/main/proto'},
    packages=['informaticsmatters.protobuf',
              'informaticsmatters.protobuf.datamanager'],

    # Project classification:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: POSIX :: Linux',
    ],

    install_requires=requirements,

    zip_safe=False,

)
