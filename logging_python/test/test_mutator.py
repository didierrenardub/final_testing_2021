from pytest import raises

from ..mutator import Mutator


def test_filter():
    f = Mutator()
    with raises(NotImplementedError):
        f.mutate("some_text")