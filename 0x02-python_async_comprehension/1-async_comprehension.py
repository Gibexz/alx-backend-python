#!/usr/bin/env python3
"""
module: 1-async_comprehension.py
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[]:
    """
    collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    random_num_list = [num async for num in async_generator()]
    return random_num_list
