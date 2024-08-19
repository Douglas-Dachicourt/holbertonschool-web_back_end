#!/usr/bin/env python3
"""
    Module that measures the runtime of executing async_comprehension
    four times concurrently.
"""
import asyncio
import time
"""
    import of asyncio and time modules
"""

async_comprehension = __import__('1-async_comprehension').async_comprehension
"""
    import async_comprehension function from previous encoded file
"""


async def measure_runtime() -> float:
    """
    Coroutine that measures the time taken to run async_comprehension
    four times concurrently.

    Arguments: None

    Returns: total_time, type float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )

    end_time = time.perf_counter()

    total_time = float(end_time - start_time)

    return (total_time)
