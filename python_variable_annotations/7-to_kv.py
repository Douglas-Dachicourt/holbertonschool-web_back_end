#!/usr/bin/env python3
"""
    Function that takes two arguments and return a tuple
"""
from typing import Tuple, Union
"""
    imports Tuple and Union from type to get the annotation type
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Argument : k has to be a string
                   v is int or float

        Returns : a tuple of both arguments

    """
    return (k, v * v)
