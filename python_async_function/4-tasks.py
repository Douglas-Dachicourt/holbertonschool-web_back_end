#!/usr/bin/env python3

from typing import List
"""
    import List from typing module

"""
task_wait_random = __import__('3-tasks').task_wait_random
"""
    import task_wait_random from task 3
"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Arguments:
            - n: type int, represent the number of delays
                inserted in our list
            - max_delay: type int, represented by function
            task_wait_random

        Returns: a list of float number, respectively the delays
        allowed by n times - List[float] type

    """
    array = []
    for elem in range(0, n):
        delays = await task_wait_random(max_delay)
        array.append(delays)

    new_array = sorted(array)
    return new_array
