#!/usr/bin/env python3
"""
    function that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
"""

from typing import Callable
"""
    import Callable type from typing module
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Argument : a float type number

        Returns: the argument multiplied by itself


    """
    return multiplier * multiplier
