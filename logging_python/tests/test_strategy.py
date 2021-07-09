from ..mutator import Mutator
from ..filter import Filter
from ..strategy import Strategy
from pytest import raises
from datetime import datetime


def test_strategy__log():
    with raises(NotImplementedError):
        s = Strategy()
        s._log("string", None)


def test_strategy_init_filters_mutators():
    s = Strategy()
    assert s.filters() == [] and s.mutators() == []
    s = Strategy(None)
    assert s.filters() == [] and s.mutators() == []


def test_strategy_add_mutator():
    s = Strategy()
    m1 = Mutator()
    assert s.add_mutator(m1) == True and m1 in s.mutators()
    assert s.add_mutator(m1) == False and s.mutators().count(m1) == 1
    m2 = Mutator()
    assert s.add_mutator(m2) == True and m2 in s.mutators() and len(s.mutators()) == 2 and s.mutators().count(m2) == 1
    assert s.add_mutator(None) == False and None not in s.mutators()
    assert s.add_mutator() == False


def test_strategy_remove_mutator():
    s = Strategy()
    m1 = Mutator()
    m2 = Mutator()
    s.add_mutator(m1)
    s.add_mutator(m2)

    assert s.remove_mutator() == False and s.mutators() == [m1, m2]
    assert s.remove_mutator(None) == False and s.mutators() == [m1, m2]
    assert s.remove_mutator(m1) == True and s.mutators() == [m2]
    assert s.remove_mutator(m1) == False and s.mutators() == [m2]


def test_strategy_clear_mutators():
    s = Strategy()
    m1 = Mutator()
    s.add_mutator(m1)

    assert s.clear_mutators() == True and s.mutators() == []
    assert s.clear_mutators() == True


def test_strategy_add_filter():
    s = Strategy()
    f1 = Filter()
    assert s.add_filter(f1) == True and f1 in s.filters()
    assert s.add_filter(f1)  == False and s.filters().count(f1) == 1
    f2 = Filter()
    assert s.add_filter(f2)  == True and f2 in s.filters() and len(s.filters()) == 2 and s.filters().count(f2) == 1
    assert s.add_filter(None) == False and None not in s.filters()
    assert s.add_filter() == False


def test_strategy_remove_filter():
    s = Strategy()
    f1 = Filter()
    f2 = Filter()
    s.add_filter(f1)
    s.add_filter(f2)

    assert s.remove_filter() == False and s.filters() == [f1, f2]
    assert s.remove_filter(None) == False and s.filters() == [f1, f2]
    assert s.remove_filter(f1) == True and s.filters() == [f2]
    assert s.remove_filter(f1) == False and s.filters() == [f2]


def test_strategy_clear_filters():
    s = Strategy()
    f1 = Filter()
    s.add_filter(f1)

    assert s.clear_filters() == True and s.filters() == []
    assert s.clear_filters() == True


class TimeStamp(Mutator):
    def mutate(self, text: str, extra_data: dict[str, str] = None) -> str:
        if extra_data is not None and "time" in extra_data.keys():
            ts = extra_data.get("time")
            return f"{ts}: {text}"
        now = datetime.now()
        ts = str(now).split(".")[0]
        return f"{ts}: {text}"


def test_strategy__mutate():
    s = Strategy()
    s.add_mutator(TimeStamp)
    assert s.mutators[0].mutate("string", {"time":"123"}) == "123: string"


class FilterByLength(Filter):
    def filter(self, text: str, **extra_data: int) -> bool:
       
        if extra_data is not None:
            if len(extra_data) == 2 and extra_data[0] < len(text) < extra_data[1]:
                return False
            if len(extra_data) == 1 and len(text) > extra_data[0]:
                return True
        return True
        

def test_strategy__filter():
    s = Strategy()
    s.add_filter(FilterByLength)
    assert s.filters[0].filter("str", 0, 4) == False
    assert s.filters[0].filter("str", 0, 3) == True
    assert s.filters[0].filter("str", 3, 4) == False
    assert s.filters[0].filter("str", None) == False
    assert s.filters[0].filter("str", 2) == True


class StrategyImpl(Strategy):
    def __init__(self):
        Strategy().__init__()

    def _log(self, text: str, **extra_data):
        return text

def test_strategy_log():
    s = StrategyImpl()
    s.add_filter(FilterByLength)
    s.add_mutator(TimeStamp)

    assert s.log("string") == True
    assert s.log("string", 5) == False
    