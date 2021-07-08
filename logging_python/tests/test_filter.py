from ..filter import Filter
from pytest import raises

def test_filter():
    with raises(NotImplementedError):
        r = Filter()
        r.filter("string", dict())
        