from pytest import raises
from unittest.mock import Mock, patch

from ..filter import Filter
from ..logger import Logger
from ..mutator import Mutator
from ..strategy import Strategy


class MyMutator(Mutator):
    def mutate(self, text: str, extra_data: dict= None) -> str:
        if extra_data is not None and extra_data["prefix123"]:
            return "123" + text
        return text
    
class MyStrategy(Strategy):
    def _log(self, text: str, **extra_data):
        return text

### Comienzo de los tests ###

def test_underscore_log():
    strat1 = Strategy()
    with raises(NotImplementedError):
        strat1._log("some_text")

def test_text_none():
    m1 = MyMutator()
    s1 = MyStrategy()
    s1.add_mutator(m1)
    param = {"prefix123":True}
    assert s1.log(None, param) == False

def test_param_none():
    s1 = MyStrategy()
    assert s1.log("some_text", None) == True

def test_text_param_none():
    s1 = MyStrategy()
    assert s1.log(None, None) == False


# Test integral donde se prueba que se loguee, luego que se filtre un logueo
# y finalmente que se filtre un logueo luego de que la entrada sea mutada
# para coincidir con un patron de filtrado
def test_log_filter_mutate():
    strat1 = Strategy()

    # Implementando funciones de interfaces para posterior Patcheo
    def _log(text: str, **extra_data):
        """Mocked _log"""
        print(f"LOGGED: {text}")
    mocked_log = _log

    def my_filter(text: str, **extra_data):
        """Mocked filter"""
        return True if text == "filter_me" else False
    mocked_filter = my_filter
    
    def my_mutator(text: str, extra_data):
        """Mocked mutator"""
        return "filter_me"
    mocked_mutator = my_mutator
    # Fin de la implementacion de funciones de interfaces para posterior Patcheo

    strat2 = Strategy()
    f1 = Filter()
    m1 = Mutator()
    with patch.object(strat2, "_log", side_effect=mocked_log):
        # Aca pruebo simplemente que el logueo suceda
        assert strat2.log("some_test") == True

        # Aca pruebo que el logueo NO suceda si el texto enviado esta en un filtro
        # Esto al mismo tiempo me permite testear la logica de filtrado
        with patch.object(f1, "filter", side_effect=mocked_filter):
            strat2.add_filter(f1)
            assert strat2.log("filter_me") == False
            strat1.clear_filters()

            # Aca pruebo que el logueo NO suceda si el texto enviado esta en un filtro
            # Para ser filtrado, un mutador va a cambiar el texto de entrada por uno filtrable
            # Esto al mismo tiempo me permite testear la logica de mutacion
            with patch.object(m1, "mutate", side_effect=mocked_mutator):
                strat2.add_filter(f1)
                strat2.add_mutator(m1)
                assert strat2.log("mutate_me_and_filter_me") == False
                strat2.clear_mutators()
                strat2.clear_filters()

def test_add_remove_mutator():
    m1 = Mutator()
    strat1 = Strategy()

    assert strat1.add_mutator(m1) == True
    assert strat1.add_mutator(m1) == False
    assert m1 in strat1.mutators()

    assert strat1.remove_mutator(m1) == True
    assert strat1.remove_mutator(m1) == False
    assert m1 not in strat1.mutators()

def test_add_remove_filter():
    f1 = Filter()
    strat1 = Strategy()

    assert strat1.add_filter(f1) == True
    assert strat1.add_filter(f1) == False
    assert f1 in strat1.filters()

    assert strat1.remove_filter(f1) == True
    assert strat1.remove_filter(f1) == False
    assert f1 not in strat1.filters()

def test_clear_mutator_filter():
    m1 = Mutator()
    f1 = Filter()
    strat1 = Strategy()

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


def test_mutation_extra_data_approach1():
    m1 = MyMutator()
    s1 = MyStrategy()
    s1.add_mutator(m1)
    param = {"prefix123":True}
    assert s1._mutate("some_text", param).startswith("123")

# def test_mutation_extra_data_approach2():

#     def my_mutator(text: str, **extra_data) -> str:
#         """Mocked mutator"""
#         if extra_data["prefix123"]:
#             return "123" + text
#         return text
#     mocked_mutator = my_mutator

#     def log(text: str, **extra_data) -> str:
#         """Mocked log"""
#         mutated_message = my_mutator(text, **extra_data)
#         return mutated_message
#     mocked_log = log

#     strat2 = Strategy()
#     m1 = Mutator()
#     with patch.object(m1, "mutate", side_effect=mocked_mutator):
#         with patch.object(strat2, "log", side_effect=mocked_log):
#             strat2.add_mutator(m1)
#             assert strat2.log("some_text", prefix123=True).startswith("123")
#             strat2.clear_mutators()
