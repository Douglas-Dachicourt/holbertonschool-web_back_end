#!/usr/bin/env python3
"""
    Module displays a coroutine that collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers.

"""
from typing import List
"""
    import List from typing module
"""

async_generator = __import__('-0-async_generator').async_generator
"""
    import async_generator from previous task

"""


async def async_comprehension() -> List[float]:
    """
        Couroutine function asyn_comprehension

        Arguments: None

        Returns: a list of awaited numbers via async_generator()


    """
    results = [await number for number in async_generator]
    return results
