#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages

version = '5.6.7'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

long_description = "\n".join([
    open('README.rst', 'r').read(),
    open('AUTHORS.rst', 'r').read(),
    open('CHANGELOG.rst', 'r').read(),
])


def get_source_files():
    for dirname, _, files in os.walk('ckeditor/static/ckeditor/ckeditor/_source'):
        for filename in files:
            yield os.path.join('/'.join(dirname.split('/')[1:]), filename)


setup(
    name='lc-django-ckeditor',
    version=version,
    description='Django admin CKEditor integration.',
    long_description=long_description,
    author='Shaun Sephton & Piotr Malinski',
    author_email='riklaunim@gmail.com',
    url='https://github.com/LeetCode-OpenSource/django-ckeditor',
    packages=find_packages(exclude=["*.demo"]),
    zip_safe=False,
    install_requires=[
        'django-js-asset',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
