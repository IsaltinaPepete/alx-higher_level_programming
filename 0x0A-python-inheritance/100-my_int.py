#!/usr/bin/python3
""""Defines class int"""


class MyInt(int):
    """Represent a class"""

    def __eq__(self, other):
        """
        Override the == operator.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Override the != operator.
        """
        return not super().__ne__(other)
