#!/usr/bin/env python3
"""
    Module for working on types annotations

"""

from typing import Iterable, Tuple, Sequence, List
"""
    Iterable, Tuple, Sequence and List imported from typing module
    to get annotations type
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences as an argument.

    For each sequence in the iterable, this function returns a list of tuples,
    where each tuple contains the original sequence and its length.

    Arguments:
        lst (Iterable[Sequence]): An iterable containing sequences
        (e.g., lists, tuples, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples. Each tuple contains
        a sequence from the original iterable and the length
        of that sequence.

    Example:
        >>> element_length(["abc", [1, 2, 3], (4, 5)])
        [("abc", 3), ([1, 2, 3], 3), ((4, 5), 2)]
    """
    return [(i, len(i)) for i in lst]
