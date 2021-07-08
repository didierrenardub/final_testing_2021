"""Base logger class.

LICENSE: MIT

Copyright 2021 AoE Mastapizza
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from .strategy import Strategy


class Logger(Strategy):
    """Nucleates the different logging strategies to use them in a centralized way.

    `Logger` is a `Strategy` itself, which allows to pre-mutate all messages with the same `Mutator`
    prior to forwarding the messages to its inner strategies, which can in turn have their own
    mutators.

    Strategies can still be used individually, though.
    """
    def __init__(self, strategies: list = None):
        """Initialize the `Logger` with the given strategies, if any.

        Note that for the `Logger` to work you need to supply at least one strategy, otherwise, the
        `Logger` itself does nothing with the messages.

        Args:
            strategies: A `list` of `Strategy` objects that will define the `Logger` behaves.
        """
        Strategy.__init__(self)
        self._strategies = strategies if strategies is not None else []

    def add_strategy(self, strategy: Strategy) -> bool:
        """Adds the given `Strategy` to the current `Logger`.

        Args:
            strategy: The `Strategy` object that should be applied when logging with the current
                `Logger`.

        Returns:
            bool: Confirmation whether the strategy has been added or not.
        """
        if strategy is not None and strategy not in self.strategies():
            self._strategies.append(strategy)
            return True
        return False

    def strategies(self) -> list:
        """Getter for the strategies held by this `Logger`.

        Returns:
            list: The `list` of `Strategy` objects owned by the current `Logger`.
        """
        return self._strategies

    def _log(self, text: str, **extra_data):
        """Log the given text using the held strategies.

        Args:
            text: The message to be logged by the different strategies.
            extra_data: [Optional] Keyword arguments containing info for the strategies to work as
                intended or to be forwarded to the mutators held by those strategies.
        """
        for strategy in self.strategies():
            strategy.log(text, **extra_data)
