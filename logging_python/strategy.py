"""Defines the interface the logging strategies should comply with.

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
from .mutator import Mutator
from .filter import Filter


class Strategy():
    """A base class to define the basics of a logging strategy.

    These could actually be used without the need of a `Logger`.
    """
    def __init__(self):
        """Initialize the strategy.

        Creates the internal lists to hold `Mutator`s and `Filter`s.
        """
        self._mutators = []
        self._filters = []

    def _log(self, text: str, **extra_data):
        """Method to be overriden by concrete classes.

        Intended to do the actual logging with the message already mutated by the `Mutator`s. A
        filtered message will not produce an invocation of this method.
        Marked as protected/private because it shouldn't be called directly.

        Args:
            text: The message to be logged.
            extra_data: [Optional] Keyword arguments that might contain data for the `Strategy` to
                work as intended.

        Raises:
            NotImplementedError: As this just defines the method signature for implementors.
        """
        raise NotImplementedError()

    def log(self, text: str, **extra_data) -> bool:
        """Log the given message applying the internal `Mutator`s using the extra data.

        Args:
            text: The message to be logged.
            extra_data: [Optional] Keyword arguments that might contain data for the `Mutator`s to
                work as intended. Note that each `Mutator` could have different requirements, so how
                the `extra_data` is interpreted might vary.

        Returns:
            bool: Confirmation whether the message has been logged or not (i.e. because it was
                filtered out).
        """
        # Turn kwargs into a local dictionary to allow the mutators to actually mutate the
        # parameters such that the filters can act upon the mutated values.
        extra_data = {**extra_data}
        mutated_message = self._mutate(text, extra_data)
        if not self._filter(mutated_message, **extra_data):
            self._log(mutated_message, **extra_data)
            return True
        return False

    def add_mutator(self, mutator: Mutator) -> bool:
        """Adds a `Mutator` to the current `Strategy`.

        Mutators will be applied to the messages to be logged prior to being logged.
        Since one mutator can depend on the work of the previous one, the order matters.

        Args:
            mutator: The `Mutator` to be added to this `Strategy`.

        Returns:
            bool: Confirmation whether the mutator has been added to the mutators list or not.
        """
        if mutator is not None and mutator not in self._mutators:
            self._mutators.append(mutator)
            return True
        return False

    def remove_mutator(self, mutator: Mutator) -> bool:
        """Removes a mutator from the list.

        Args:
            mutator: A reference to the `Mutator` to remove from the list.

        Returns:
            bool: Confirmation whether the mutator has been removed or not.
        """
        if mutator is not None and mutator in self._mutators:
            self._mutators.remove(mutator)
            return True
        return False

    def mutators(self) -> list:
        """Returns the list of `Mutator`s applied in this `Strategy`.

        Returns:
            list: The `list` of `Mutator`s the current `Strategy` holds.
        """
        return self._mutators

    def clear_mutators(self):
        """Clear all `Mutator`s from this `Strategy`."""
        self._mutators.clear()

    def add_filter(self, the_filter: Filter) -> bool:
        """Add the given `Filter` to the current `Strategy` to filter messages.

        Args:
            the_filter: The `Filter` to be added to this `Strategy`.

        Returns:
            bool: Confirmation whether the filter has been added or not.
        """
        if the_filter is not None and the_filter not in self._filters:
            self._filters.append(the_filter)
            return True
        return False

    def remove_filter(self, the_filter: Filter) -> bool:
        """Removes the supplied `Filter` from this `Strategy`, if present.

        Args:
            the_filter: The `Filter` to remove from the current `Strategy`.

        Returns:
            bool: Confirmation whether the `Filter` was able to be removed or not (most likely
                because it was not there in the first place).
        """
        if the_filter in self._filters:
            self._filters.remove(the_filter)
            return True
        return False

    def filters(self) -> list:
        """A getter for filters used by this `Strategy`.

        Returns:
            list: A list of `Filter` objects the current `Strategy` is using.
        """
        return self._filters

    def clear_filters(self):
        """Removes all filters this `Strategy` is using."""
        self._filters.clear()

    def _mutate(self, text: str, extra_data: dict = None) -> str:
        """Apply all mutators to the incoming message.

        Args:
            message: The message to mutate.
            extra_data: Dictionary containing data the `Mutator`s might need.

        Returns:
            str: The mutated message
        """
        message = text
        for mutator in self._mutators:
            message = mutator.mutate(message, extra_data)
        return message

    def _filter(self, text: str, **extra_data) -> bool:
        """Apply filters to incoming messages.

        Args:
            message: The message to check if it should be filtered out or not.
            extra_data: Other parameters supplied along with the message aimed for the `Mutator`s
                and/or strategies, which could also be taken into account for message filtering.

        Returns:
            bool: `True` if the message should be filtered out, `False` otherwise.
        """
        for the_filter in self.filters():
            if the_filter.filter(text, **extra_data):
                return True
        return False
