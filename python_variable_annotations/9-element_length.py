#!/usr/bin/env python3

from typing import Iterable, Tuple, Sequence, List
"""
    Iterable, Tuple, Sequence and List imported from typing module
    to get annotations type
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Argument: an iterable containing sequence

        Returns: a list of tuples, including themselves sequences with
        their length

    """
    return [(i, len(i)) for i in lst]
