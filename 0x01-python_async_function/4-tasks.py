#!/usr/bin/env python3
"""
module: 4-tasks.py
"""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of random floats """
    tasks = []
    delays = []
    for i in range(n):
        tasks.append(asyncio.create_task(task_wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
