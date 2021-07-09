from ..filter import Filter
from ..logger import Logger
from ..mutator import Mutator
from ..strategy import Strategy


logger = Logger()
strat1 = Strategy()

class MyStrategy(Strategy):
    def _log(self, text: str, **extra_data):
        return text

class MyMutator(Mutator):
    def mutate(self, text: str, extra_data: dict= None) -> str:
        return text

class MyFilter(Filter):
    def filter(self, text: str, extra_data: dict= None) -> str:
        return True if text == "filter_me" else False

### Comienzo de las pruebas ###

def test_add_strategy():
    assert logger.add_strategy(strat1) == True
    assert logger.add_strategy(strat1) == False
    assert strat1 in logger.strategies()

def test_log():
    s1 = MyStrategy()
    f1 = MyFilter()
    m1 = MyMutator()
    s1.add_filter(f1)
    s1.add_mutator(m1)   
    logger.add_strategy(s1)
    logger._log("some_text")