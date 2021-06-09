from os import path
from setuptools import find_packages, setup

from fst import __version__

NAME = 'fst'
DESCRIPTION = 'Fading Suns Toolkit for Game Masters'


def get_version():
    return '.'.join(map(str, __version__))


def get_packages():
    pkgs = [
        f'{NAME}.{pkg}' for pkg in find_packages(NAME, exclude=['*.tests'])
    ]
    return [NAME, 'requirements'] + pkgs


CONFIG = {
    'name': NAME,
    'version': get_version(),
    'packages': get_packages(),
    'include_package_data': True,
    'author': 'Dominik Blek',
    'author_email': 'dominikblek86@gmail.com',
    'url': 'https://github.com/zybex86/fading-suns-tools',
    'license': 'MIT',
    'classifiers': [
        'Programming Language :: Python :: 3.8',
        'License :: MIT'
    ],
    'scripts': [
        path.join('scripts', 'fst-manage.py'),
        path.join('scripts', 'fst-run-tests.sh'),
        path.join('scripts', 'fst-run-tests-with-pg.sh'),
        # Helper scripts
        path.join('scripts', 'fst-wait-for-postgresql.py'),
        path.join('scripts', 'colors.sh'),
    ]
}

setup(**CONFIG)
