from logging_python.mutator import Mutator
from ..strategy import Strategy
from pytest import raises


def test_strategy__log():
    with raises(NotImplementedError):
        s = Strategy()
        s._log("string", None)


def test_strategy_init_filters_mutators():
    s = Strategy()
    assert s.filters() == [] and s.mutators() == []
    s = Strategy(None)
    assert s.filters() == [] and s.mutators() == []


def test_strategy_add_mutaror():
    s = Strategy()
    m1 = Mutator()
    assert s.add_mutator(m1) == True and m1 in s.mutators()
    assert s.add_mutator(m1) == False and s.mutators().count(m1) == 1
    m2 = Mutator()
    assert s.add_mutator(m2) == True and m2 in s.mutators() and len(s.mutators()) == 2 and s.mutators().count(m2) == 1
    assert s.add_mutator(None) == False and None not in s.mutators()
    assert s.add_mutator() == False



