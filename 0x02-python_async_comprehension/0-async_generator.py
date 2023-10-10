#!/usr/bin/env python3
"""
module: 0-async_generator.py
"""
import asyncio
import random


async def async_generator() -> float:
    """
    loop 10 times, each time asynchronously wait 1 second, then
    yield a random number between 0 and 10. Use the random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
