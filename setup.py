#!/usr/bin/env python

from collections import OrderedDict

import setuptools

with open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

name = "cds411"
version = "0.1"
release = "0.1.0"

setuptools.setup(
    name=name,
    author="James K. Glasbrenner",
    author_email="jglasbr2@gmu.edu",
    license="Creative Commons Attribution-ShareAlike 4.0 International",
    version=release,
    project_urls=OrderedDict(
        (("Repo", "https://github.com/jkglasbrenner/cds411-course-materials"), )
    ),
    description=("Course materials for CDS 411: Modeling and simulation II."),
    long_description=readme,
    python_requires=">=3.7",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "jupyter >= 1.0.0",
        "jupyterlab >= 0.34.3",
        "matplotlib >= 2.2.3",
        "numpy >= 1.15.0",
        "pandas >= 0.23.4",
        "rpy2 >= 2.9.4",
        "scikit-learn >= 0.19.1",
        "scipy >= 1.1.0",
        "seaborn >= 0.9.0",
        "statsmodels >= 0.9.0",
    ],
    extras_require={
        "dev": [
            "autopep8 >= 1.3.5",
            "flake8 >= 3.5.0",
            "importmagic >= 0.1.7",
            "jedi >= 0.12",
            "pydocstyle >= 2.1.1",
            "PyHamcrest >= 1.9.0",
            "pytest >= 3.7.3",
            "rope >= 0.11.0",
            "yapf >= 0.23.0",
        ],
    },
)
