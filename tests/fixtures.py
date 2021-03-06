import os
import os.path

import pytest

import idb


CD = os.path.dirname(__file__)


@pytest.yield_fixture
def empty_idb():
    path = os.path.join(CD, 'data', 'empty', 'empty.idb')
    with idb.from_file(path) as db:
        yield db


@pytest.yield_fixture
def kernel32_idb():
    path = os.path.join(CD, 'data', 'kernel32', 'kernel32.idb')
    with idb.from_file(path) as db:
        yield db

@pytest.yield_fixture
def small_idb():
    path = os.path.join(CD, 'data', 'small', 'small-colored.idb')
    with idb.from_file(path) as db:
        yield db
