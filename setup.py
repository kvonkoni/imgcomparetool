#!/usr/bin/env python

import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

readmePath = thelibFolder + '/README.md'
long_description = ""
if os.path.isfile(requirementPath):
    with open(readmePath, "r") as fh:
        long_description = fh.read()

setup(  name='imgcomparetool',
        version='0.1.0',
        author='Kier von Konigslow',
        author_email='kvonkonigslow@gmail.com',
        maintainer='Ferris',
        maintainer_email='ferris@emaildomain.com',
        description='Image Comparison Tool',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://gitlab.com/kvonkoni/imgcomparetool',
        packages=find_packages(),
        install_requires=install_requires,
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    )
