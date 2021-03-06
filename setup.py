import os
import numpy as np
from setuptools import setup, find_packages, Extension
from distutils.util import convert_path
from Cython.Build import cythonize

NAME = 'te5t9527'


def get_version():
    ns = {}
    with open(convert_path(f'{NAME}/version.py')) as f:
        exec(f.read(), ns)
    return ns['__version__']


extensions = [
    Extension(NAME + '.c_utils', sources = [NAME + '/c_utils.pyx'], include_dirs = [np.get_include()]),
]


setup(
    name = NAME,
    version = get_version(),
    description = 'test python publish by travis-ci',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Secbone/py_publish_test',
    author = 'Secbone',
    author_email = 'secbone@gmail.com',
    packages = find_packages(exclude = ['tests']),
    ext_modules = cythonize(extensions),
    include_package_data = True,
    python_requires = '>=3.5',
    setup_requires = [
        'setuptools',
    ],
    install_requires = [
        'pandas',
    ],
    license = 'MIT',
    entry_points = {
        'console_scripts': [
            'te5t9527 = te5t9527.cli:main',
        ],
    },
)
