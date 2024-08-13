#!/usr/bin/env python3
"""
    Function that measures the total execution
    time for wait_n(n, max_delay) function, and returns total_time / n
"""
import time
import asyncio
"""
    import time and asyncio modules
"""
wait_n = __import__('1-concurrent_coroutines').wait_n
"""
    import wait_n function from previous encoded file
"""


def measure_time(n: int, max_delay: int) -> float:
    """
        Arguments:
            - n: int, number of times for the function execution
            - max_delay: int, delay allowed for each execution

        Returns:
            Average total time for each execution, float number

    """
    start_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()

    total_time = (end_time - start_time) / n

    return total_time
