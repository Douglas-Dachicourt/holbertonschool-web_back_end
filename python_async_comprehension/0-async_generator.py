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
        Function async_generator that takes no argument

        Arguments: none

        Returns: AsyncGenerator typing

    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        random_num = random.uniform(0, 10)
        yield random_num
