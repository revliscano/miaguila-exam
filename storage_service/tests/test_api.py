from .conftests import database_object


def test_one(database_object):
    assert 1 == 1
