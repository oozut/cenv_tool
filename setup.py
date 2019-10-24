# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='cenv_tool',
    version='2.1.0',
    description='conda environment creation and update from meta.yaml',
    python_requires='>=3.7',
    project_urls={
        'homepage': 'https://www.cenv.ouroboros.info',
        'repository': 'https://github.com/skallfass/cenv_tool'
    },
    author='Simon Kallfass',
    author_email='skallfass@ouroboros.info',
    license='MIT',
    keywords='conda environment dependencies',
    classifiers=[
        'Operating System :: Unix', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': [
            'cenv = cenv_tool.project:main',
            'init_cenv = cenv_tool.init_cenv:main'
        ]
    },
    packages=['cenv_tool'],
    package_data={'cenv_tool': ['*.sh', '*.yml']},
    install_requires=[
        'attrs>=19', 'jinja2>=2', 'marshmallow<3,>=2.19', 'pyyaml==5.*,>=5.0.0',
        'six>=1.12'
    ],
    extras_require={
        'tests': [
            'coverage>=4', 'coverage-badge>=1', 'pytest>=5', 'pytest-cov>=2',
            'pytest-datafiles>=2'
        ],
        'dev': [
            'coverage>=4', 'coverage-badge>=1', 'ipython>=7', 'pylint>=2.4',
            'pytest>=5', 'pytest-cov>=2', 'pytest-datafiles>=2', 'sphinx>=2',
            'sphinx-autodoc-typehints>=1.8.0', 'sphinx-rtd-theme>=0', 'yapf>=0'
        ],
        'docs': ['sphinx>=2', 'sphinx-autodoc-typehints>=1.8.0']
    },
)
