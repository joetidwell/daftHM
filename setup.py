#!/usr/bin/env python


try:
    from setuptools import setup, Extension
    setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    setup, Extension

import os
import re
import sys

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

vre = re.compile("__version__ = \"(.*?)\"")
m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "daftHM.py")).read()
version = vre.findall(m)[0]


setup(
    name="daftHM",
    version=version,
    description="PGM rendering at its finest.",
    long_description=open("README.rst").read(),
    author="Joe Tidwell",
    author_email="joetidwell@umd.edu",
    url="https://github.com/joetidwell/daftHM",
    py_modules=["daftHM"],
    package_data={"": ["LICENSE.rst"]},
    include_package_data=True,
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
