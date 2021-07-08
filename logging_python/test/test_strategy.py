from pytest import raises
from unittest.mock import Mock, patch

from ..filter import Filter
from ..logger import Logger
from ..mutator import Mutator
from ..strategy import Strategy


strat1 = Strategy()

def test_underscore_log():
    with raises(NotImplementedError):
        strat1._log("some_text")

def test_log():

    def _log(text: str, **extra_data):
        """Mocked _log"""
        print(f"LOGGED: {text}")
    mocked_log = _log

    def my_filter(text: str, **extra_data):
        """Mocked filter"""
        return True if text == "filter_me" else False
    mocked_filter = my_filter
    
    def my_mutator(text: str, **extra_data):
        """Mocked mutator"""
        return "filter_me"
    mocked_mutator = my_mutator

    strat2 = Strategy()
    f1 = Filter()
    m1 = Mutator()
    with patch.object(strat2, "_log", return_value=mocked_log):
        assert strat2.log("some_test") == True

        with patch.object(f1, "filter", return_value=mocked_filter):
            strat2.add_filter(f1)
            assert strat2.log("filter_me") == False
            strat1.clear_filters()

            with patch.object(m1, "mutate", return_value=mocked_mutator):
                strat2.add_filter(f1)
                strat2.add_mutator(m1)
                assert strat2.log("mutate_me_and_filter_me") == False
                strat2.clear_mutators()
                strat2.clear_filters()

def test_add_remove_mutator():
    m1 = Mutator()

    assert strat1.add_mutator(m1) == True
    assert strat1.add_mutator(m1) == False
    assert m1 in strat1.mutators()

    assert strat1.remove_mutator(m1) == True
    assert strat1.remove_mutator(m1) == False
    assert m1 not in strat1.mutators()

def test_add_remove_filter():
    f1 = Filter()

    assert strat1.add_filter(f1) == True
    assert strat1.add_filter(f1) == False
    assert f1 in strat1.filters()

    assert strat1.remove_filter(f1) == True
    assert strat1.remove_filter(f1) == False
    assert f1 not in strat1.filters()

def test_clear_mutator_filter():
    m1 = Mutator()
    f1 = Filter()

    strat1.clear_mutators()
    strat1.clear_filters()
    assert strat1.mutators() == []
    assert strat1.filters() == []

    strat1.add_mutator(m1)
    strat1.add_filter(f1)
    strat1.clear_mutators()
    strat1.clear_filters()
    assert strat1.mutators() == []
    assert strat1.filters() == []