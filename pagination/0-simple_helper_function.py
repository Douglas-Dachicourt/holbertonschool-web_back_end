#!/usr/bin/env python3
"""
    Module that provide a function that return a tuple of size two
    containing a start index and an end index corresponding to the
    range of indexes to return in a list for those particular pagination
    parameters.
"""
from typing import Tuple
"""
    import Tuple from typing module
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        index_range function that takes two arguments

        Arguments:
            - page: type int,
            - page_size: type int,

        Returns: a tuple of numbers , type int

    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
