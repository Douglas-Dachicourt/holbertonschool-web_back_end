#!/usr/bin/env python3
"""
    Module provides a coroutine called async_generator that takes
    no arguments.
    The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10

"""
import asyncio
import random
from typing import AsyncGenerator

"""
    import of AsyncGenerator, asyncio and random modules

"""


async def async_generator() -> AsyncGenerator[float, None]:
    """
        Coroutine function async_generator that yields a random float between
        0 and 10, ten times.

        Arguments: None

        Yields:
        float: A random float between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
