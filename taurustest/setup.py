"""
This file was autogenerated by taurusgui --new-gui.
"""

from setuptools import setup, find_packages

# version (bumpversion style)
__version = '0.1.0'

# Example of classifier
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Scientific/Engineering',
    'Environment :: X11 Applications :: Qt',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5'
]

_entry_points = {
    "console_scripts": ["taurustest=tgconf_taurustest:run"]
}

setup(
    name="tgconf_taurustest",
    version=__version,
    include_package_data=True,
    packages=find_packages(),
    entry_points=_entry_points,
    url='http://www.taurus-scada.org/en/latest/',
    keywords='APP',
    description='taurustest Taurus GUI',
    requires=['setuptools (>=1.1)'],
    install_requires=['taurus[taurus-qt]'],
    classifiers=classifiers
)