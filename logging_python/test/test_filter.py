from pytest import raises

from ..filter import Filter


def test_filter():
    f = Filter()
    with raises(NotImplementedError):
        f.filter("some_text")