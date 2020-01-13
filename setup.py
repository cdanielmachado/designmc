#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = ['reframed>=1.1.0', 'pandas']
test_requirements = requirements + ['cplex']

setup(
    author="Daniel Machado",
    author_email='cdanielmachado@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Microbial Community Designer",
    entry_points={
        'console_scripts': [
            'designmc=designmc.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords='designmc',
    name='designmc',
    packages=find_packages(include=['designmc', 'designmc.*']),
    setup_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cdanielmachado/designmc',
    version='0.1.0',
    zip_safe=False,
)
