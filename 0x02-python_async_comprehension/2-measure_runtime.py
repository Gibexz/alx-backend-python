#!/usr/bin/env python3
"""
module: 2-measure_runtime.py
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    should measure the total runtime and return it
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    elasped = time.perf_counter() - start
    return elasped
