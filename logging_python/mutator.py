"""Defines the interface the logging mutators should comply to.

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


class Mutator():  # pylint: disable=too-few-public-methods
    """Interface to implement different mutators for the logging strategies.

    Note: while it may seem pointless to let strategies have mutators rather than the `Logger`
    itself, truth is that it makes sense because you might want to show different things according
    to the strategy. I.e.: while logging into the console you most likely want to keep messages
    short, but since the file is searchable you can be open to having more information in there (of
    course, when using both strategies at the same time).
    """
    def mutate(self, text: str, extra_data: dict = None) -> str:
        """Allows manipulating the received message.

        This method, on oncrete classes, will be called by the `Strategy` prior to logging the
        message.

        Args:
            message: The message to be logged.
            extra_data: [Optional] Dictionary containing information needed by the mutator
                to work as expected.

        Returns:
            str: The mutated version of the original message.

        Raises:
            NotImplementedError: Because this is just an interface.
        """
        raise NotImplementedError()
