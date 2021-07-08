"""Defines the interface the logging filters should comply to.

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


class Filter():  # pylint: disable=too-few-public-methods
    """Used to block messages from being logged based on the `Filter`'s criteria.

    Every `Strategy` may have different filters. Note this is just the interface.
    """
    def filter(self, text: str, **extra_data) -> bool:
        """Determine if a message should be logged or not.

        Args:
            text: The message to check if it should be filtered out or not.
            extra_data: Other parameters supplied along with the message aimed for the `Mutator`s
                and/or strategies, which could also be taken into account for message filtering. You
                could also expect parameters to come here for your filter to act.

        Returns:
            bool: `True` if the message should not be displayed in the log, `False` otherwise.

        Raises:
            NotImplementedError: Since this is just an interface.
        """
        raise NotImplementedError()
