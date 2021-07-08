from ..logger import Logger
from ..strategy import Strategy


logger = Logger()
strat1 = Strategy()
strat2 = Strategy()

def test_add_strategy():
    assert logger.add_strategy(strat1) == True
    assert logger.add_strategy(strat1) == False
    assert strat1 in logger.strategies()