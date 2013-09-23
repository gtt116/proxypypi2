from setuptools import setup

from proxypypi2 import __version__

setup(
    name='proxypypi2',
    version=__version__,
    author="Richard Jones, Tim Gao",
    author_email="rjones@ekit-inc.com, gtt116@126.com",
    description="A PyPI caching proxy",
    long_description=open('README.md').read(),
    url='https://github.com/gtt116/proxypypi2',
    license="BSD",
    packages=['proxypypi2'],
    entry_points={
        'console_scripts': [
            'proxypypi2 = proxypypi2.server:main',
        ],
    },
    install_requires=['gunicorn', 'bottle', 'lockfile', 'distlib>=0.1.2'],
)
