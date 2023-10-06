#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument and returns a
    function that multiplies a float by the given multiplier.
    """
    def multi_function(x: float) -> float:
        return x * multiplier
    return multi_function
