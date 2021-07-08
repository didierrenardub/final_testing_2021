from ..mutator import Mutator
from pytest import raises

def test_mutator():
    with raises(NotImplementedError):
        m = Mutator()
        m.mutate("string")