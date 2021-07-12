from logging_python.strategy import Strategy
from ..logger import Logger


def test_logger_init_strategies():
    l1 = Logger()
    assert l1.strategies() == []
    l2 = Logger(None)
    assert l2.strategies() == []
    s_list = [Strategy(),Strategy()]
    l3 = Logger(s_list)
    assert l3.strategies() == s_list


def test_logger_add_strategy():
    l = Logger()
    s1 = Strategy()
    assert l.add_strategy(s1) == True and s1 in l.strategies()
    assert l.add_strategy(s1) == False and l.strategies().count(s1) == 1
    s2 = Strategy()
    assert l.add_strategy(s2) == True and s2 in l.strategies() and len(l.strategies()) == 2 and l.strategies().count(s2) == 1
    assert l.add_strategy(None) == False and None not in l.strategies()
    assert l.add_strategy() == False and l.strategies() == [s1, s2]


def test_logger__log():
    l = Logger()
    for _ in range(3):
        l.add_strategy(Strategy())

    l._log("String", None)

    # for s in l.strategies():
    #     s.