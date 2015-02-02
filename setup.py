#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import os
#import sys
#from setuptools import setup, find_packages
from distutils.core import setup
from setuptools import setup, find_packages

version = "0.1.0"

#if sys.argv[-1] == 'publish':
#    os.system('python setup.py sdist upload')
#    print("You probably want to also tag the version now:")
#    print("  git tag -a %s -m 'version %s'" % (version, version))
#    print("  git push --tags")
#    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-minibugs',
    version=version,
    description="""Minimalistic bugtracker for your django project""",
    long_description=readme + '\n\n' + history,
    author='Mario Signorino',
    author_email='mario.signorino@gnufish.net',
    url='https://github.com/mariosgn/django-minibugs',
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django,bugtracker,minibugs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
