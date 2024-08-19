#!/usr/bin/env python3
"""
Mdule that display a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1
second, then yield a random number between 0 and 10

"""
from typing import AsyncGenerator
import asyncio
import random
"""
import of Generator from typing
import of asyncio to use async/await
import random to generate a random number
"""


async def async_generator() -> AsyncGenerator[int, None]:
    """
        Coroutine that yields a random float between 0 and 10, ten times.

        Yields:
        float: A random float between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
