#!/usr/bin/env python3
"""
module: 1-concurrent_coroutines.py
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of random floats """
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
