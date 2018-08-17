#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

# Package meta-data.
REQUIRES_PYTHON = ">=3.6.0"
requires = []
extras = {}


here = os.path.abspath(os.path.dirname(__file__))


def README():
    return open(os.path.join(here, "README.md")).read()


setup(
    name="{{cookiecutter.project_slug}}",
    # description
    description="{{cookiecutter.project_descr}}",
    long_description=README(),
    long_description_content_type="text/markdown",
    license="MIT",
    # version
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    # author
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    url="https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.project_slug}}",
    # package spec
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    # requirements
    python_requires=REQUIRES_PYTHON,
    install_requires=requires,
    extras_require=extras,
)
