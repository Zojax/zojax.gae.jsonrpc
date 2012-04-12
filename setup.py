# -*- coding: utf-8 -*-
"""Setup script."""

import os
from distutils.core import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='zojax.gae.jsonrpc',
    version='0.1.0',
    author="Yaroslav D.",
    author_email='developers@zojax.com',
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
    packages=['zojax', 'zojax.gae', 'zojax.gae.jsonrpc'],
    package_dir = {'': 'src'},
    include_package_data=True,
    namespace_packages=['zojax', 'zojax.gae'],
    install_requires=[
        'distribute',
    ],
    zip_safe=False,
)
