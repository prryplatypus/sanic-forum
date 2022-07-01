import codecs
import os
import re

from setuptools import setup, find_packages


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)

    return codecs.open(path, mode, encoding)


with open_local(["sanic_forum", "__version__.py"], encoding="latin1") as fp:
    try:
        version = re.findall(
            r"^VERSION = \"([^']+)\"\r?$", fp.read(), re.M
        )[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")


MIGRATE_REQUIRES = ['yoyo-migrations', 'psycopg2']
TEST_REQUIRES = [
    'black', 'flake8', 'isort', 'pytest', 'pytest-asyncio', 'sanic-testing'
]
DEV_REQUIRES = MIGRATE_REQUIRES + TEST_REQUIRES


setup(
    name='sanic-forum',
    version=version,
    description='A forum, built with Sanic',
    author='prryplatypus',
    author_email='github@prryplatypus.dev',
    packages=find_packages(),
    install_requires=[
        'mayim[postgres]',  # Database
        'sanic',
        'sanic-ext',
    ],
    extras_require={
        'migrate': MIGRATE_REQUIRES,
        'test': TEST_REQUIRES,
        'dev': DEV_REQUIRES
    }
)
