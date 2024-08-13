#!/usr/bin/env python3
"""
    Function that spawn wait_random n times with the specified max_delay
"""
from typing import List
"""
    import List from typing module
"""
wait_random = __import__('0-basic_async_syntax').wait_random
"""
    import of wait_random function previously coded
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Arguments:
            - n: type int, represent the number of delays
                inserted in our list
            - max_delay: type int, represented by function
            wait_random

        Returns: a list of float number, respectively the delays
        allowed by n times - List[float] type

    """
    array = []
    for elem in range(0, n):
        delays = await wait_random(max_delay)
        array.append(delays)

    new_array = sorted(array)
    return new_array
