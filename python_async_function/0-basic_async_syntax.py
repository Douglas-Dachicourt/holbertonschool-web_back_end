#!/usr/bin/env python3
"""
    Module that show a asynchronous coroutine that takes in an integer
    argument (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay (included
    and float value) seconds and eventually returns it
"""
import random
import asyncio
"""
    import of random and asyncio modules

"""


async def wait_random(max_delay: int = 10):
    """
        Argument: max_delay , type int, default value equals to 10

        Returns: random delay (float value)
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
