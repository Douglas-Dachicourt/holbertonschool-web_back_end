#!/usr/bin/env python3
"""
    function that takes an integer max_delay and returns a asyncio.Task
"""
import asyncio
"""
    import asyncio module
"""
wait_random = __import__('0-basic_async_syntax').wait_random
"""
    import wait_random from 0-basic_async_syntax
"""


def task_wait_random(max_delay: int):
    """
        Argument : max_delay, int

        Returns: an asyncio Task

    """
    return asyncio.create_task(wait_random(max_delay))
