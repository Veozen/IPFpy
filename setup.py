"""
Setup configuration for the IPFpy package.

This script handles the packaging, dependency management, and metadata
required to distribute IPFpy via PyPI.
"""

from setuptools import setup, find_packages

setup(
    name='IPFpy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.23.5',
        'pandas>=2.1.2',
        'duckdb>=1.4.0',
    ],
    author='Christian Gagné',
    author_email='christian.gagne@gmail.com',
    description='Performs iterative proportional fitting on tabular data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/veozen/IPF',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
