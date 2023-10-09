#!/usr/bin/env python3
"""
module: 1-concurrent_coroutines.py
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    coroutine that takes in 2 int arguments (n and max_delay, with a default
    value of 10) named wait_n that waits for a random delay between 0 and
    max_delay (included and float value) seconds and eventually returns it
    """
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
