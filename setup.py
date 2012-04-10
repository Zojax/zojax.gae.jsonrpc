# -*- coding: utf-8 -*-
"""Setup script."""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='zojax.gae.jsonrpc',
    version='0.1.0',
    author="Yaroslav D.",
    author_email='blw0rm@gmail.com',
    description=("Implements JSON/RPC for Google App Engine (Python)."),
    long_description=(
        read('README.rst')
        ),
    license="Apache License 2.0",
    keywords="google app engine gae rpc",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        ],
    url='',
    packages=find_packages(),
    package_dir = {'': os.sep.join(['src', 'jsonrpc'])},
    include_package_data=True,
    install_requires=[
        'distribute',
    ],
    zip_safe=False,
)
